(function () {
  const config = window.LAWYER_SITE_CONFIG || {};
  const form = document.getElementById("mobile-consult-form");
  const statusNode = document.getElementById("mobile-form-status");

  if (!form || !statusNode) {
    return;
  }

  const regionField = form.elements.namedItem("contact_region");
  const phoneField = form.elements.namedItem("contact_phone");
  const phoneError = document.getElementById("mobile-phone-error");
  const submitButton = form.querySelector('button[type="submit"]');
  const submitLabel = submitButton ? submitButton.textContent.trim() : "提交初步咨询";
  const phoneLengths = { "+852": 8, "+86": 11, "+853": 8 };
  let clientIpPromise = null;

  hydrateHiddenFields();
  syncPhoneRule();
  ensureClientIp().catch(function () { return ""; });

  if (regionField && phoneField) {
    regionField.addEventListener("change", function () {
      phoneField.value = phoneField.value.replace(/\D+/g, "");
      syncPhoneRule();
      validatePhone();
    });
    phoneField.addEventListener("input", function () {
      const maxLength = getPhoneLength();
      phoneField.value = phoneField.value.replace(/\D+/g, "").slice(0, maxLength);
      validatePhone();
    });
    phoneField.addEventListener("blur", validatePhone);
  }

  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    setStatus("", "");

    const endpoint = config.formEndpoint;
    if (!endpoint || endpoint.indexOf("REPLACE_WITH") !== -1) {
      setStatus("表单提交地址尚未设置，请稍后再试。", "error");
      return;
    }

    const phoneValid = validatePhone();
    if (!phoneValid || !form.reportValidity()) {
      return;
    }

    await ensureClientIp();
    hydrateHiddenFields();

    try {
      setLoading(true);
      setStatus("正在安全提交资料，请稍候。", "loading");
      await fetch(endpoint, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" },
        body: buildPayload().toString()
      });

      setStatus("资料已送出，正在为你跳转。", "success");
      if (typeof window.gtag === "function" && config.conversionId) {
        window.gtag("event", "conversion", { send_to: config.conversionId });
      }
      window.setTimeout(function () {
        window.location.href = "lh-thanks.html";
      }, 900);
    } catch (error) {
      setStatus("提交失败，请稍后再试。", "error");
      setLoading(false);
    }
  });

  function hydrateHiddenFields() {
    const url = new URL(window.location.href);
    setValue("referrer", document.referrer || "");
    setValue("landing_url", window.location.href);
    setValue("submitted_at", new Date().toISOString());
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"].forEach(function (name) {
      setValue(name, url.searchParams.get(name) || "");
    });
  }

  function buildPayload() {
    const payload = new URLSearchParams();
    const append = function (name, value) { payload.append(name, value == null ? "" : String(value)); };
    const matters = Array.from(form.querySelectorAll('input[name="mainland_matter"]:checked')).map(function (field) {
      return field.value;
    });
    const summary = getValue("summary");
    const location = getValue("current_location");
    const message = [
      "涉及内地内容：" + (matters.length ? matters.join("、") : "未选择"),
      "目前所在地：" + location,
      "简要情况：" + (summary || "未填写")
    ].join("\n");

    append("submitted_at", getValue("submitted_at") || new Date().toISOString());
    append("site", config.siteCode || "liuyi-divorce-lh");
    append("language", "zh-CN");
    append("page_title", document.title);
    append("page_url", window.location.href);
    append("name", getValue("name"));
    append("area_code", getValue("contact_region"));
    append("phone", getValue("contact_phone").replace(/\D+/g, ""));
    append("wechat", getValue("social_contact"));
    append("inquiry_type", getValue("case_type"));
    append("message", message);
    append("source", "github-pages");
    append("user_agent", navigator.userAgent);
    append("client_ip", getValue("client_ip"));
    append("source_page", getValue("source_page"));
    append("stage", getValue("stage"));
    append("property_city", getValue("property_city"));
    append("referrer", getValue("referrer"));
    append("landing_url", getValue("landing_url"));
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"].forEach(function (name) {
      append(name, getValue(name));
    });
    return payload;
  }

  function getPhoneLength() {
    return phoneLengths[getValue("contact_region")] || 20;
  }

  function syncPhoneRule() {
    if (!phoneField) {
      return;
    }
    const region = getValue("contact_region");
    const expected = phoneLengths[region];
    phoneField.maxLength = expected || 20;
    phoneField.placeholder = expected === 11 ? "请输入11位号码" : expected === 8 ? "请输入8位号码" : "请输入电话号码";
  }

  function validatePhone() {
    if (!phoneField) {
      return true;
    }
    const digits = phoneField.value.replace(/\D+/g, "");
    const region = getValue("contact_region");
    const expected = phoneLengths[region];
    let message = "";
    if (!digits) {
      message = "请填写联系电话。";
    } else if (expected && digits.length !== expected) {
      message = region + " 电话请填写 " + expected + " 位数字。";
    } else if (!expected && (digits.length < 6 || digits.length > 20)) {
      message = "请输入 6 至 20 位电话号码。";
    }
    phoneField.setCustomValidity(message);
    phoneField.classList.toggle("is-invalid", Boolean(message));
    if (phoneError) {
      phoneError.textContent = message;
      phoneError.hidden = !message;
    }
    return !message;
  }

  function setLoading(loading) {
    if (!submitButton) {
      return;
    }
    submitButton.disabled = loading;
    submitButton.textContent = loading ? "提交中" : submitLabel;
    form.setAttribute("aria-busy", loading ? "true" : "false");
  }

  function setStatus(message, state) {
    statusNode.textContent = message;
    statusNode.dataset.state = state || "";
  }

  function setValue(name, value) {
    const field = form.elements.namedItem(name);
    if (field) {
      field.value = value;
    }
  }

  function getValue(name) {
    const field = form.elements.namedItem(name);
    return field ? String(field.value || "").trim() : "";
  }

  async function ensureClientIp() {
    if (getValue("client_ip")) {
      return getValue("client_ip");
    }
    if (!clientIpPromise) {
      clientIpPromise = fetch("https://api64.ipify.org?format=json", { cache: "no-store" })
        .then(function (response) { return response.ok ? response.json() : {}; })
        .then(function (data) { return data && data.ip ? String(data.ip).trim() : ""; })
        .catch(function () { return ""; });
    }
    const ip = await clientIpPromise;
    if (ip) {
      setValue("client_ip", ip);
    }
    return ip;
  }
})();
