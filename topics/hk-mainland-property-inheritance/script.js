(function () {
  const form = document.getElementById("contactForm");
  const areaCode = document.getElementById("areaCode");
  const phone = document.getElementById("phone");
  const phoneHint = document.getElementById("phoneHint");
  const status = document.getElementById("formStatus");
  const modal = document.getElementById("successModal");
  const closeButton = document.getElementById("modalCloseBtn");

  const phoneRules = {
    "+852": { pattern: /^[0-9]{8}$/, hint: "香港电话请输入 8 位数字", alert: "香港电话请输入 8 位数字" },
    "+86": { pattern: /^[0-9]{11}$/, hint: "中国内地手机请输入 11 位数字", alert: "中国内地手机请输入 11 位数字" },
    "+853": { pattern: /^[0-9]{8}$/, hint: "澳门电话请输入 8 位数字", alert: "澳门电话请输入 8 位数字" },
    "+1": { pattern: /^[0-9]{10}$/, hint: "美国/加拿大电话请输入 10 位数字", alert: "美国/加拿大电话请输入 10 位数字" },
    "+65": { pattern: /^[0-9]{8}$/, hint: "新加坡电话请输入 8 位数字", alert: "新加坡电话请输入 8 位数字" },
    "+60": { pattern: /^[0-9]{8,10}$/, hint: "马来西亚电话请输入 8 至 10 位数字", alert: "马来西亚电话请输入 8 至 10 位数字" }
  };

  function cleanPhone(value) {
    return String(value || "").replace(/[-\s()]/g, "");
  }

  function endpoint() {
    if (!window.SITE_CONFIG || typeof window.SITE_CONFIG.googleSheetsEndpoint !== "string") return "";
    return window.SITE_CONFIG.googleSheetsEndpoint.trim();
  }

  function inquiryType() {
    const checked = form.querySelector('input[name="zxsx"]:checked');
    return checked ? checked.value : "";
  }

  function updateHint() {
    const rule = phoneRules[areaCode.value];
    phoneHint.textContent = rule ? rule.hint : "请输入有效电话号码";
    phoneHint.style.color = "#5f6b7a";
  }

  function validatePhone() {
    const rule = phoneRules[areaCode.value];
    const cleaned = cleanPhone(phone.value);
    return rule ? rule.pattern.test(cleaned) : cleaned.length >= 6;
  }

  function payload() {
    const data = new URLSearchParams();
    data.append("submitted_at", new Date().toISOString());
    data.append("site", document.body.dataset.site || "hk-mainland-property-inheritance");
    data.append("language", document.documentElement.lang || "zh-CN");
    data.append("page_title", document.title);
    data.append("page_url", window.location.href);
    data.append("name", document.getElementById("name").value.trim());
    data.append("area_code", areaCode.value);
    data.append("phone", cleanPhone(phone.value));
    data.append("wechat", document.getElementById("wechat").value.trim());
    data.append("inquiry_type", inquiryType());
    data.append("message", document.getElementById("message").value.trim());
    data.append("source", "seo-topic-page");
    data.append("topic", "hk-mainland-property-inheritance");
    data.append("user_agent", navigator.userAgent);
    return data;
  }

  function showSuccess() {
    status.textContent = "已提交，我们会主动联系你。";
    status.style.color = "#116466";
    modal.hidden = false;
    window.setTimeout(function () {
      modal.hidden = true;
    }, 3200);
  }

  if (!form || !areaCode || !phone || !phoneHint) return;

  updateHint();
  areaCode.addEventListener("change", updateHint);
  phone.addEventListener("input", function () {
    if (!phone.value) {
      updateHint();
      return;
    }
    if (validatePhone()) {
      phoneHint.textContent = "格式正确";
      phoneHint.style.color = "#116466";
    } else {
      updateHint();
      phoneHint.style.color = "#8a1f2d";
    }
  });

  form.addEventListener("submit", async function (event) {
    event.preventDefault();
    document.getElementById("page_url").value = window.location.href;

    const name = document.getElementById("name").value.trim();
    const target = endpoint();
    if (!name) {
      window.alert("请填写称呼");
      return;
    }
    if (!cleanPhone(phone.value)) {
      window.alert("请填写联系电话");
      return;
    }
    if (!validatePhone()) {
      window.alert((phoneRules[areaCode.value] || {}).alert || "请输入有效电话号码");
      phone.focus();
      return;
    }
    if (!target) {
      window.alert("提交接口暂未配置，请稍后再试。");
      return;
    }

    const button = form.querySelector(".submit-btn");
    const originalText = button.textContent;
    button.disabled = true;
    button.textContent = "提交中...";
    status.textContent = "";

    try {
      await fetch(target, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" },
        body: payload().toString()
      });
      form.reset();
      updateHint();
      showSuccess();
    } catch (error) {
      status.textContent = "提交失败，请稍后再试。";
      status.style.color = "#8a1f2d";
    } finally {
      button.disabled = false;
      button.textContent = originalText;
    }
  });

  closeButton.addEventListener("click", function () {
    modal.hidden = true;
  });

  modal.addEventListener("click", function (event) {
    if (event.target === modal) modal.hidden = true;
  });
})();
