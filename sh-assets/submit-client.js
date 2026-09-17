(function () {
  'use strict';
  const attemptsByForm = new WeakMap();
  const sleep = ms => new Promise(resolve => window.setTimeout(resolve, ms));

  function fingerprint(payload) {
    const copy = new URLSearchParams(payload);
    ['submitted_at', 'client_ip', 'user_agent', 'submission_id'].forEach(key => copy.delete(key));
    copy.sort();
    return copy.toString();
  }

  function newId() {
    const bytes = new Uint8Array(16);
    window.crypto.getRandomValues(bytes);
    return Array.from(bytes, byte => byte.toString(16).padStart(2, '0')).join('');
  }

  async function submit(endpoint, payload, form) {
    const signature = fingerprint(payload);
    let attempt = attemptsByForm.get(form);
    if (!attempt || attempt.signature !== signature) {
      attempt = { signature, id: newId() };
      attemptsByForm.set(form, attempt);
    }
    payload.set('submission_id', attempt.id);
    const body = payload.toString();
    let lastError;
    for (let retry = 0; retry < 3; retry++) {
      const controller = new AbortController();
      const timeout = window.setTimeout(() => controller.abort(), 12000);
      try {
        const response = await fetch(endpoint, {
          method: 'POST', mode: 'cors', credentials: 'omit',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' },
          body, signal: controller.signal
        });
        const result = await response.json();
        if (response.ok && result.ok === true && result.saved === true && result.submission_id === attempt.id) {
          return result;
        }
        const error = new Error('Server did not confirm durable receipt');
        error.permanent = response.status >= 400 && response.status < 500 && response.status !== 429;
        throw error;
      } catch (error) {
        lastError = error;
        if (error.permanent) throw error;
      } finally {
        window.clearTimeout(timeout);
      }
      if (retry < 2) await sleep(500 * (retry + 1));
    }
    throw lastError;
  }

  function finish(receipt, conversionId) {
    let navigated = false;
    const navigate = function () {
      if (navigated) return;
      navigated = true;
      window.location.assign('sh-thanks.html');
    };
    window.setTimeout(navigate, 250);
    if (typeof window.gtag === 'function' && conversionId) {
      try {
        window.gtag('event', 'conversion', {
          send_to: conversionId, transaction_id: receipt.submission_id,
          event_callback: navigate, event_timeout: 250
        });
      } catch (_) { navigate(); }
    }
  }
  window.SH_SUBMISSION = { submit, finish };
})();
