document.addEventListener('DOMContentLoaded', function () {
    'use strict';
    const form = document.getElementById('contactForm');
    const areaCode = document.getElementById('areaCode');
    const phone = document.getElementById('phone');
    const hint = document.getElementById('phoneHint');
    const errorBox = document.getElementById('formError');
    const modal = document.getElementById('successModal');
    const close = document.getElementById('modalCloseBtn');
    if (!form || !areaCode || !phone || !hint || !errorBox || !modal || !close) return;

    const rules = {
        '+852': { pattern: /^[0-9]{8}$/, message: '請輸入8位數字', error: '香港電話號碼必須是8位數字' },
        '+86': { pattern: /^[0-9]{11}$/, message: '請輸入11位數字', error: '內地電話號碼必須是11位數字' }
    };
    let submitting = false;
    let attempt = null;
    let modalTimer;
    const normalizePhone = value => value.trim().replace(/[-\s]/g, '');
    const validPhone = () => !!rules[areaCode.value] && rules[areaCode.value].pattern.test(normalizePhone(phone.value));

    function updateHint() {
        const rule = rules[areaCode.value];
        const message = rule ? rule.message : '請輸入有效電話號碼';
        phone.placeholder = message;
        hint.textContent = phone.value && validPhone() ? '✓ 格式正確' : message;
        hint.style.color = phone.value ? (validPhone() ? '#4CAF50' : '#ff4444') : '#666';
    }

    function showError(message) {
        errorBox.textContent = message;
        errorBox.focus();
    }

    // IP lookup is optional and must never hold up a lead submission.
    const clientIp = fetch('https://api64.ipify.org?format=json', { cache: 'no-store' })
        .then(response => response.ok ? response.json() : {})
        .then(result => typeof result.ip === 'string' ? result.ip : '')
        .catch(() => '');

    function buildPayload(ip) {
        const selected = form.querySelector('input[name="zxsx"]:checked, input[name="zxsx1"]:checked');
        return new URLSearchParams({
            submitted_at: new Date().toISOString(),
            site: document.body.dataset.site || 'hk-main',
            language: document.documentElement.lang || 'zh-HK',
            page_title: document.title,
            page_url: window.location.href,
            name: document.getElementById('name').value.trim(),
            area_code: areaCode.value,
            phone: normalizePhone(phone.value),
            wechat: document.getElementById('wechat').value.trim(),
            inquiry_type: selected ? selected.value : '',
            message: document.getElementById('message').value.trim(),
            source: 'github-pages',
            user_agent: navigator.userAgent,
            client_ip: ip || ''
        });
    }

    async function sendWithReceipt(endpoint, payload) {
        const stable = new URLSearchParams(payload);
        ['submitted_at', 'client_ip', 'user_agent'].forEach(key => stable.delete(key));
        stable.sort();
        const signature = stable.toString();
        if (!attempt || attempt.signature !== signature) {
            const bytes = new Uint8Array(16);
            window.crypto.getRandomValues(bytes);
            attempt = { signature, id: Array.from(bytes, byte => byte.toString(16).padStart(2, '0')).join('') };
        }
        payload.set('submission_id', attempt.id);
        const body = payload.toString();
        const controller = new AbortController();
        const timeout = window.setTimeout(() => controller.abort(), 20000);
        try {
            const response = await fetch(endpoint, {
                method: 'POST', mode: 'cors', credentials: 'omit',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8' },
                body, signal: controller.signal
            });
            const result = await response.json();
            // The current relay confirms storage without echoing the submitted ID.
            const matchingId = result.submission_id === undefined || result.submission_id === attempt.id;
            if (response.ok && result.ok === true && result.saved === true && matchingId) {
                return { ...result, submission_id: attempt.id };
            }
            throw new Error('Server did not confirm receipt');
        } finally {
            window.clearTimeout(timeout);
        }
        // Do not automatically resend an ambiguous request: the relay may have saved it.
    }

    areaCode.addEventListener('change', updateHint);
    phone.addEventListener('input', updateHint);
    close.addEventListener('click', () => { modal.style.display = 'none'; });
    modal.addEventListener('click', event => { if (event.target === modal) modal.style.display = 'none'; });

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        if (submitting) return;
        errorBox.textContent = '';
        document.getElementById('page_url').value = window.location.href;
        if (!document.getElementById('name').value.trim()) return showError('請填寫您的稱呼');
        if (!phone.value.trim()) return showError('請填寫聯絡電話');
        if (!validPhone()) {
            showError(rules[areaCode.value] ? rules[areaCode.value].error : '請輸入有效電話號碼');
            phone.focus();
            return;
        }
        const endpoint = window.SITE_CONFIG && window.SITE_CONFIG.googleSheetsEndpoint;
        if (typeof endpoint !== 'string' || !endpoint.trim() || endpoint.includes('PASTE_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE')) {
            return showError('暫時未能提交，請稍後再試。');
        }
        const button = form.querySelector('.submit-btn');
        const originalText = button.textContent;
        submitting = true;
        button.disabled = true;
        button.textContent = '提交中...';
        try {
            const ip = await Promise.race([clientIp, new Promise(resolve => window.setTimeout(() => resolve(''), 1200))]);
            const receipt = await sendWithReceipt(endpoint.trim(), buildPayload(ip));
            // Only a confirmed durable receipt can clear the form or count a conversion.
            modal.style.display = 'flex';
            window.clearTimeout(modalTimer);
            modalTimer = window.setTimeout(() => { modal.style.display = 'none'; }, 3000);
            const selectedArea = areaCode.value;
            form.reset();
            areaCode.value = selectedArea;
            updateHint();
            attempt = null;
            if (typeof window.gtag === 'function') {
                try {
                    window.gtag('event', 'conversion', {
                        send_to: 'AW-18003046397/yLGoCM6KjowcEP3fwohD',
                        transaction_id: receipt.submission_id
                    });
                } catch (_) { /* Analytics must not turn a saved lead into an error. */ }
            }
        } catch (error) {
            console.error('Submission was not confirmed:', error);
            showError('暫時未能確認提交，請稍後再試。您填寫嘅資料已保留。');
        } finally {
            submitting = false;
            button.disabled = false;
            button.textContent = originalText;
        }
    });
    updateHint();
});
