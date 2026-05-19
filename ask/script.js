(function () {
  const chatBody = document.getElementById("chatBody");
  const quickReplies = document.getElementById("quickReplies");
  const form = document.getElementById("chatForm");
  const input = document.getElementById("chatInput");
  const submitButton = form?.querySelector("button[type='submit']");
  const SESSION_KEY = "jingwei.ask.chat.session.v1";
  const BACKUP_KEY = "jingwei.ask.chat.backup.v1";
  const STORAGE_MAX_AGE_MS = 1000 * 60 * 60 * 24 * 3;
  let isComposing = false;

  const adTitle = document.getElementById("adTitle");
  const adCopy = document.getElementById("adCopy");
  const adLink = document.getElementById("adLink");

  const state = {
    stage: "region",
    region: "",
    mainland: "",
    matter: "",
    summary: "",
    messages: [],
    activeRequestId: 0
  };

  const regionChips = [
    { label: "美国华人", value: "us_chinese" },
    { label: "美国客户", value: "us_general" },
    { label: "澳门", value: "macau" },
    { label: "马来西亚", value: "malaysia" },
    { label: "新加坡", value: "singapore" },
    { label: "其他海外地区", value: "other" }
  ];

  const mainlandChips = [
    { label: "涉及中国内地", value: "yes" },
    { label: "暂时不确定", value: "unsure" },
    { label: "只涉及当地法律", value: "no" }
  ];

  const matterChips = [
    { label: "合同/商业合作", value: "contract" },
    { label: "公司/股权", value: "company" },
    { label: "婚姻家事/继承", value: "family" },
    { label: "身份/授权/文件", value: "identity" },
    { label: "其他民商事问题", value: "other" }
  ];

  const localRoutes = {
    us_chinese: { label: "美国华人中文入口", url: "/us/index_cn.html" },
    us_general: { label: "美国客户英文入口", url: "/us/index_us.html" },
    macau: { label: "澳门繁体入口", url: "/am/index_tc.html" },
    malaysia: { label: "马来西亚中文入口", url: "/ml/index_cn.html" },
    singapore: { label: "新加坡中文入口", url: "/xj/index_cn.html" },
    other: { label: "美国华人中文入口", url: "/us/index_cn.html" }
  };

  function apiEndpoint() {
    if (window.JINGWEI_AI_API) return window.JINGWEI_AI_API;
    if (window.SITE_CONFIG && window.SITE_CONFIG.aiEndpoint) return window.SITE_CONFIG.aiEndpoint;

    if (window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost") {
      return "http://127.0.0.1:4100/chat";
    }
    return "https://api.jingwei-law.com/chat";
  }

  function scrollToBottom() {
    chatBody.scrollTop = chatBody.scrollHeight;
  }

  function addMessage(text, type, options) {
    const row = document.createElement("div");
    row.className = "msg-row " + type + (options && options.typing ? " typing" : "");

    const avatar = document.createElement("span");
    avatar.className = "msg-avatar";
    avatar.textContent = type === "user" ? "我" : "律";

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.textContent = text;

    row.appendChild(avatar);
    row.appendChild(bubble);
    chatBody.appendChild(row);
    scrollToBottom();
    return row;
  }

  function addBot(text) {
    state.messages.push({ role: "assistant", content: text });
    saveChatSession();
    return addMessage(text, "bot");
  }

  function addUser(text) {
    state.messages.push({ role: "user", content: text });
    saveChatSession();
    return addMessage(text, "user");
  }

  function setBusy(busy) {
    if (submitButton) submitButton.disabled = busy;
    input.disabled = busy;
  }

  function setChips(items) {
    quickReplies.innerHTML = "";
    (items || []).forEach((item) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "reply-chip";
      button.textContent = item.label;
      button.dataset.value = item.value;
      button.addEventListener("click", function () {
        handleTurn(item.label, { fromChip: true, value: item.value });
      });
      quickReplies.appendChild(button);
    });
  }

  function updatePlaceholder(text) {
    input.placeholder = text || "也可以继续补充你的情况";
  }

  function stageUi(stage) {
    if (stage === "region") {
      return { chips: regionChips, placeholder: "也可以直接输入你现在主要所在地区" };
    }
    if (stage === "mainland") {
      return { chips: mainlandChips, placeholder: "输入是否涉及中国内地" };
    }
    if (stage === "matter") {
      return { chips: matterChips, placeholder: "输入大致事务类型" };
    }
    if (stage === "summary") {
      return { chips: [], placeholder: "例如：我人在美国，对方公司在深圳，合同履行地在内地" };
    }
    return { chips: [], placeholder: "也可以继续补充你的情况" };
  }

  function parseJson(raw) {
    try {
      return JSON.parse(raw);
    } catch {
      return null;
    }
  }

  function normalizeSavedMessages(messages) {
    if (!Array.isArray(messages)) return [];
    return messages
      .map((message) => ({
        role: message && message.role === "assistant" ? "assistant" : "user",
        content: String(message && message.content ? message.content : "").trim()
      }))
      .filter((message) => message.content)
      .slice(-80);
  }

  function readStoredPayload() {
    try {
      const sessionRaw = window.sessionStorage.getItem(SESSION_KEY);
      const backupRaw = window.localStorage.getItem(BACKUP_KEY);
      const session = sessionRaw ? parseJson(sessionRaw) : null;
      const backup = backupRaw ? parseJson(backupRaw) : null;
      return session || backup;
    } catch {
      return null;
    }
  }

  function saveChatSession() {
    const payload = {
      savedAt: Date.now(),
      state: {
        stage: state.stage || localStage(),
        region: state.region || "",
        mainland: state.mainland || "",
        matter: state.matter || "",
        summary: state.summary || "",
        messages: state.messages.slice(-80)
      },
      inputDraft: String(input && input.value ? input.value : "").slice(0, 1000)
    };

    try {
      const raw = JSON.stringify(payload);
      window.sessionStorage.setItem(SESSION_KEY, raw);
      window.localStorage.setItem(BACKUP_KEY, raw);
    } catch {
      // ignore storage failures
    }
  }

  function restoreChatSession() {
    const payload = readStoredPayload();
    if (!payload || !payload.state) return false;

    const savedAt = Number(payload.savedAt || 0);
    if (savedAt && Date.now() - savedAt > STORAGE_MAX_AGE_MS) return false;

    const savedMessages = normalizeSavedMessages(payload.state.messages);
    if (!savedMessages.length) return false;

    state.stage = String(payload.state.stage || "region");
    state.region = String(payload.state.region || "");
    state.mainland = String(payload.state.mainland || "");
    state.matter = String(payload.state.matter || "");
    state.summary = String(payload.state.summary || "");
    state.messages = savedMessages;

    chatBody.innerHTML = '<div class="day-pill">今天</div>';
    savedMessages.forEach((message) => {
      addMessage(message.content, message.role === "assistant" ? "bot" : "user");
    });

    const stage = localStage();
    state.stage = stage;
    const ui = stageUi(stage);
    setChips(ui.chips);
    updatePlaceholder(ui.placeholder);
    updateAd(routeForCurrentState(), stage);

    if (payload.inputDraft) {
      input.value = String(payload.inputDraft);
      input.style.height = "auto";
      input.style.height = Math.min(input.scrollHeight, 118) + "px";
    }

    return true;
  }

  function appendSummary(text) {
    const cleaned = String(text || "").trim();
    if (!cleaned) return;

    const parts = state.summary ? state.summary.split("\n").map((line) => line.trim()).filter(Boolean) : [];
    if (!parts.includes(cleaned)) parts.push(cleaned);
    state.summary = parts.join("\n").slice(0, 2000);
  }

  function inferRegion(text) {
    if (/澳门|澳門/.test(text)) return "macau";
    if (/马来西亚|馬來西亞|Malaysia/i.test(text)) return "malaysia";
    if (/新加坡|Singapore/i.test(text)) return "singapore";
    if (/美国华人|華人|中文客户/.test(text)) return "us_chinese";
    if (/美国|美國|U\.?S\.?|United States/i.test(text)) return "us_general";
    return "other";
  }

  function inferMainland(text) {
    if (/不涉及中国内地|不涉及中國內地|只涉及当地|纯美国|純美國|美国本地|美國本地|澳门本地|澳門本地|香港本地/.test(text)) return "no";
    if (/不确定|不確定|暂时不清楚|還不清楚|需要先判断/.test(text)) return "unsure";
    if (/中国内地|中國內地|内地|內地|大陆|大陸|mainland/i.test(text)) return "yes";
    return "unsure";
  }

  function inferMatter(text) {
    if (/合同|合约|合約|合作|货款|貨款|商事|contract|breach|payment/i.test(text)) return "contract";
    if (/公司|股权|股權|经营|經營|投资|投資|shareholder|equity|company/i.test(text)) return "company";
    if (/婚姻|离婚|離婚|继承|繼承|家事|遗产|遺產|family|divorce|inheritance/i.test(text)) return "family";
    if (/授权|授權|公证|公證|认证|認證|文件|身份|notarization|authentication|document/i.test(text)) return "identity";
    return "other";
  }

  function routeForCurrentState() {
    if (state.mainland === "no") return null;
    return localRoutes[state.region] || localRoutes.other;
  }

  function routeUrl(route) {
    const source = new URLSearchParams(window.location.search).get("source") || "ask-chat";
    return route.url + "?source=" + encodeURIComponent(source);
  }

  function updateAd(route, stage) {
    const resolvedRoute = route && route.url ? route : stage === "done" ? routeForCurrentState() : null;

    if (!resolvedRoute && state.mainland === "no") {
      adTitle.textContent = "你当前的问题方向";
      adCopy.textContent = "根据你目前提供的信息，这个问题更偏当地法律事务。你可以继续补充情况，我们会继续帮你梳理。";
      adLink.textContent = "继续当前咨询";
      adLink.removeAttribute("href");
      adLink.classList.add("is-disabled");
      return;
    }

    if (!resolvedRoute) {
      adTitle.textContent = "跨境中国内地法律事务";
      adCopy.textContent = "如需进一步咨询或委托，可查看对应专题页了解服务内容与办理方式。";
      adLink.href = "/us/index_cn.html?source=ask-chat";
      adLink.textContent = "打开专题页";
      adLink.classList.remove("is-disabled");
      return;
    }

    adTitle.textContent = resolvedRoute.label || "相关专题页";
    adCopy.textContent = "你可以打开该专题页查看对应服务，并按页面指引继续办理。";
    adLink.href = routeUrl(resolvedRoute);
    adLink.textContent = "打开专题页";
    adLink.classList.remove("is-disabled");
  }

  function localStage() {
    if (!state.region) return "region";
    if (!state.mainland) return "mainland";
    if (state.mainland === "no") return "done";
    if (!state.matter) return "matter";
    if (state.summary.replace(/\s+/g, "").length < 12) return "summary";
    return "done";
  }

  function fallbackReply() {
    const stage = localStage();

    if (stage === "region") {
      return {
        stage: "region",
        answer: "你好，我是刘毅律师团队的 AI 法律助理。先用聊天方式做初步判断，你现在主要在哪个地区？",
        chips: regionChips,
        inputPlaceholder: "也可以直接输入你现在主要所在地区",
        route: null
      };
    }

    if (stage === "mainland") {
      return {
        stage: "mainland",
        answer: "这个事项是否涉及中国内地？比如对方主体、财产所在地、合同履行地或主要证据在内地。",
        chips: mainlandChips,
        inputPlaceholder: "输入是否涉及中国内地",
        route: null
      };
    }

    if (stage === "matter") {
      return {
        stage: "matter",
        answer: "大致属于哪一类事务？你先说合同合作、公司股权、婚姻继承、授权文件，或其他民商事问题都可以。",
        chips: matterChips,
        inputPlaceholder: "输入大致事务类型",
        route: null
      };
    }

    if (stage === "summary") {
      return {
        stage: "summary",
        answer: "最后用一句话补充核心情况：你在哪里、对方或财产在哪里、最想先解决什么。",
        chips: [],
        inputPlaceholder: "例如：我人在美国，对方公司在深圳，合同履行地在内地",
        route: null
      };
    }

    if (state.mainland === "no") {
      return {
        stage: "done",
        answer: "从你目前提供的信息看，这更偏当地法律事务，不是中国内地法律事项。你也可以继续补充事实，我可以再帮你细化判断。",
        chips: [],
        inputPlaceholder: "也可以继续补充你的情况",
        route: null
      };
    }

    return {
      stage: "done",
      answer: "基于目前信息，这个事项可继续按中国内地法律路径做初步分析。你可以继续补充时间线、关键证据和目标，我会继续细化判断。",
      chips: [],
      inputPlaceholder: "也可以继续补充你的情况",
      route: routeForCurrentState()
    };
  }

  function applyChoice(text, options) {
    const fromChip = options && options.fromChip;
    const value = options && options.value;

    if (!fromChip) appendSummary(text);

    if (state.stage === "region") {
      state.region = fromChip ? value : inferRegion(text);
      return;
    }
    if (state.stage === "mainland") {
      state.mainland = fromChip ? value : inferMainland(text);
      return;
    }
    if (state.stage === "matter") {
      state.matter = fromChip ? value : inferMatter(text);
    }
  }

  async function askBackend() {
    const response = await fetch(apiEndpoint(), {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        region: state.region,
        mainland: state.mainland,
        matter: state.matter,
        summary: state.summary,
        language: "zh-CN",
        messages: state.messages
      })
    });

    if (!response.ok) throw new Error("AI endpoint failed");
    return response.json();
  }

  function applyBackendState(result) {
    if (result && result.state) {
      state.region = result.state.region || state.region;
      state.mainland = result.state.mainland || state.mainland;
      state.matter = result.state.matter || state.matter;
      state.summary = result.state.summary || state.summary;
    }
    state.stage = (result && result.stage) || localStage();
  }

  function renderAssistantReply(result) {
    applyBackendState(result);
    addBot(result.answer || fallbackReply().answer);
    setChips(result.chips || []);
    updatePlaceholder(result.inputPlaceholder);
    updateAd(result.route || null, state.stage);
  }

  async function handleTurn(text, options) {
    const cleaned = String(text || "").trim();
    if (!cleaned) return;

    addUser(cleaned);
    applyChoice(cleaned, options);
    input.value = "";
    input.style.height = "auto";
    saveChatSession();

    const requestId = ++state.activeRequestId;
    setBusy(true);
    const typing = addMessage("正在整理你的情况...", "bot", { typing: true });

    try {
      const result = await askBackend();
      if (requestId !== state.activeRequestId) return;
      typing.remove();
      renderAssistantReply(result);
    } catch (error) {
      if (requestId !== state.activeRequestId) return;
      typing.remove();
      renderAssistantReply(fallbackReply());
    } finally {
      if (requestId === state.activeRequestId) {
        setBusy(false);
        input.focus();
      }
    }
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    handleTurn(input.value, { fromChip: false });
  });

  input.addEventListener("compositionstart", function () {
    isComposing = true;
  });

  input.addEventListener("compositionend", function () {
    isComposing = false;
  });

  input.addEventListener("keydown", function (event) {
    if (event.key !== "Enter" || event.shiftKey) return;
    if (event.isComposing || isComposing || event.keyCode === 229) return;
    if (input.disabled) return;
    if (!String(input.value || "").trim()) return;

    event.preventDefault();
    if (typeof form.requestSubmit === "function") {
      form.requestSubmit();
    } else {
      form.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
    }
  });

  input.addEventListener("input", function () {
    input.style.height = "auto";
    input.style.height = Math.min(input.scrollHeight, 118) + "px";
    saveChatSession();
  });

  window.addEventListener("pagehide", saveChatSession);

  if (!restoreChatSession()) {
    chatBody.innerHTML = '<div class="day-pill">今天</div>';
    renderAssistantReply({
      stage: "region",
      answer: "你好，我是刘毅律师团队的 AI 法律助理。先用聊天方式做初步判断，你现在主要在哪个地区？",
      chips: regionChips,
      inputPlaceholder: "也可以直接输入你现在主要所在地区",
      route: null,
      state: { region: "", mainland: "", matter: "", summary: "" }
    });
  }
})();
