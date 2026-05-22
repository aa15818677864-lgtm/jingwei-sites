(function () {
  const chatBody = document.getElementById("chatBody");
  const chatMain = document.querySelector(".chat-main");
  const quickReplies = document.getElementById("quickReplies");
  const form = document.getElementById("chatForm");
  const input = document.getElementById("chatInput");
  const submitButton = form?.querySelector("button[type='submit']");
  const urlParams = new URLSearchParams(window.location.search);
  const activeTopic = urlParams.get("topic") || "";
  const sourceParam = urlParams.get("source") || "";
  const intentParam = urlParams.get("intent") || "";
  const storageSuffix = activeTopic ? "." + activeTopic.replace(/[^a-z0-9_-]/gi, "") : "";
  const SESSION_BASE_KEY = "jingwei.ask.chat.session.v1";
  const BACKUP_BASE_KEY = "jingwei.ask.chat.backup.v1";
  const SESSION_KEY = "jingwei.ask.chat.session.v1" + storageSuffix;
  const BACKUP_KEY = "jingwei.ask.chat.backup.v1" + storageSuffix;
  const STORAGE_MAX_AGE_MS = 1000 * 60 * 60 * 24 * 3;
  let isComposing = false;

  const adTitle = document.getElementById("adTitle");
  const adCopy = document.getElementById("adCopy");
  const adLink = document.getElementById("adLink");
  const routeAd = document.getElementById("routeAd");
  const LAST_GOOD_ENDPOINT_KEY = "jingwei.ask.chat.endpoint.lastGood";

  const state = {
    stage: "region",
    region: "",
    mainland: "",
    matter: "",
    summary: "",
    messages: [],
    activeRequestId: 0
  };

  const topicPresets = {
    "hk-mainland-property-inheritance": {
      region: "hongkong",
      mainland: "yes",
      matter: "family",
      summary: "客户从香港居民继承中国内地房产过户专题进入，重点关注内地不动产继承、香港文件公证转递、继承人一致性、税费和委托办理。",
      greeting: "你好，这里先按“香港居民继承中国内地房产/物业过户”来做初步判断。你可以直接说：房子在哪个内地城市、登记在谁名下、被继承人是否已去世、有没有遗嘱或继承人争议。",
      placeholder: "例如：父亲在深圳有房，香港去世，有两个子女，想问怎么过户",
      chips: [
        { label: "深圳房产继承", value: "我想咨询香港居民继承深圳房产过户" },
        { label: "香港文件能否用", value: "香港死亡证明和亲属关系证明能不能直接拿到内地用？" },
        { label: "继承人不同意", value: "继承人之间不同意，内地房产还能过户吗？" },
        { label: "费用和周期", value: "香港居民继承内地房产大概费用和周期怎么判断？" }
      ]
    }
  };

  const regionChips = [
    { label: "香港", value: "hongkong" },
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
    hongkong: { label: "香港继承内地房产咨询入口", url: "/topics/hk-mainland-property-inheritance/" },
    us_chinese: { label: "美国华人中文入口", url: "/us/index_cn.html" },
    us_general: { label: "美国客户英文入口", url: "/us/index_us.html" },
    macau: { label: "澳门繁体入口", url: "/am/index_tc.html" },
    malaysia: { label: "马来西亚中文入口", url: "/ml/index_cn.html" },
    singapore: { label: "新加坡中文入口", url: "/xj/index_cn.html" },
    other: { label: "美国华人中文入口", url: "/us/index_cn.html" }
  };

  function apiEndpointCandidates() {
    if (window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost") {
      return ["http://127.0.0.1:4100/chat"];
    }

    const configured = [];
    if (window.JINGWEI_AI_API) configured.push(window.JINGWEI_AI_API);
    if (window.SITE_CONFIG) {
      if (Array.isArray(window.SITE_CONFIG.aiEndpoints)) {
        window.SITE_CONFIG.aiEndpoints.forEach((endpoint) => configured.push(endpoint));
      }
      if (window.SITE_CONFIG.aiEndpoint) configured.push(window.SITE_CONFIG.aiEndpoint);
    }

    configured.push("https://jingwei-vercel-ai-api.vercel.app/chat");

    return Array.from(
      new Set(
        configured
          .map((endpoint) => String(endpoint || "").trim())
          .filter(Boolean)
      )
    );
  }

  function endpointTimeoutMs(endpoint, index) {
    if (/api\.jingwei-law\.com/i.test(endpoint)) return 13000;
    return index === 0 ? 12000 : 9000;
  }

  function preferredEndpointOrder(candidates) {
    let lastGood = "";
    try {
      lastGood = window.sessionStorage.getItem(LAST_GOOD_ENDPOINT_KEY) || "";
    } catch {
      lastGood = "";
    }

    if (!lastGood || !candidates.includes(lastGood)) return candidates.slice();
    return [lastGood].concat(candidates.filter((endpoint) => endpoint !== lastGood));
  }

  async function fetchChatJson(endpoint, payload, timeoutMs) {
    const controller = new AbortController();
    const timer = window.setTimeout(function () {
      controller.abort();
    }, timeoutMs);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        signal: controller.signal
      });

      if (!response.ok) throw new Error("AI endpoint failed");
      return response.json();
    } finally {
      window.clearTimeout(timer);
    }
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
    bubble.textContent = options && options.typewriter ? "" : text;

    row.appendChild(avatar);
    row.appendChild(bubble);
    chatBody.appendChild(row);
    scrollToBottom();
    return row;
  }

  function sleep(ms) {
    return new Promise((resolve) => window.setTimeout(resolve, ms));
  }

  async function typeBotMessage(row, text, requestId) {
    const bubble = row.querySelector(".bubble");
    const fullText = String(text || "");
    if (!bubble || !fullText) return;

    row.classList.add("is-typewriting");
    bubble.textContent = "";

    for (let index = 0; index < fullText.length; index += 1) {
      if (requestId && requestId !== state.activeRequestId) {
        bubble.textContent = fullText;
        break;
      }
      bubble.textContent += fullText[index];
      if (index % 4 === 0 || index === fullText.length - 1) scrollToBottom();
      await sleep(index < 220 ? 18 : 7);
    }

    bubble.textContent = fullText;
    row.classList.remove("is-typewriting");
    scrollToBottom();
  }

  async function addBot(text, options) {
    state.messages.push({ role: "assistant", content: text });
    saveChatSession();
    const row = addMessage(text, "bot", { typewriter: options && options.typewriter });
    if (options && options.typewriter) {
      await typeBotMessage(row, text, options.requestId);
    }
    return row;
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
    const preset = topicPresets[activeTopic];
    if (preset && stage === "done") {
      return { chips: preset.chips || [], placeholder: preset.placeholder };
    }
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
      if (session || backup) return session || backup;

      const genericSessionRaw = window.sessionStorage.getItem(SESSION_BASE_KEY);
      const genericBackupRaw = window.localStorage.getItem(BACKUP_BASE_KEY);
      const genericSession = genericSessionRaw ? parseJson(genericSessionRaw) : null;
      const genericBackup = genericBackupRaw ? parseJson(genericBackupRaw) : null;
      if (activeTopic) {
        const generic = genericSession || genericBackup;
        return generic && generic.topic === activeTopic ? generic : null;
      }
      if (genericSession || genericBackup) return genericSession || genericBackup;

      let newest = null;
      for (let index = 0; index < window.localStorage.length; index += 1) {
        const key = window.localStorage.key(index);
        if (!key || !key.startsWith(BACKUP_BASE_KEY + ".")) continue;
        const payload = parseJson(window.localStorage.getItem(key));
        if (!payload || !payload.savedAt) continue;
        if (!newest || Number(payload.savedAt) > Number(newest.savedAt || 0)) newest = payload;
      }
      return newest;
    } catch {
      return null;
    }
  }

  function saveChatSession() {
    const payload = {
      topic: activeTopic,
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
      window.sessionStorage.setItem(SESSION_BASE_KEY, raw);
      window.localStorage.setItem(BACKUP_BASE_KEY, raw);
    } catch {
      // ignore storage failures
    }
  }

  function restoreChatSession() {
    const payload = readStoredPayload();
    if (!payload || !payload.state) return false;

    const preset = topicPresets[activeTopic];
    if (preset) {
      const savedState = payload.state || {};
      const mismatchedTopic = payload.topic && payload.topic !== activeTopic;
      const mismatchedRegion = savedState.region && savedState.region !== preset.region;
      const mismatchedMainland = savedState.mainland && savedState.mainland !== preset.mainland;
      const mismatchedMatter = savedState.matter && savedState.matter !== preset.matter;
      if (mismatchedTopic || mismatchedRegion || mismatchedMainland || mismatchedMatter) return false;
    }

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
    if (/香港|港人|香港居民|Hong Kong|HK/i.test(text)) return "hongkong";
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
    if (
      /(深圳|广州|上海|北京|佛山|珠海|东莞|苏州|杭州|南京|天津|重庆|武汉|成都|西安|青岛|厦门|shenzhen|guangzhou|shanghai|beijing)/i.test(
        text
      ) &&
      /(房产|房產|楼房|樓房|不动产|不動產|物业|物業|开发商|開發商|交房|收楼|办证|辦證|产证|產證|过户|過戶|合同|纠纷|公司|资产|證據|证据|property|developer|title|mortgage|contract)/i.test(
        text
      )
    ) {
      return "yes";
    }
    return "unsure";
  }

  function inferMatter(text) {
    if (/继承|繼承|遗产|遺產|遗嘱|遺囑|家事|family|inheritance|estate/i.test(text)) return "family";
    if (
      /合同|合约|合約|合作|货款|貨款|商事|购房|購房|买房|買房|房产|房產|楼房|樓房|不动产|不動產|物业|物業|开发商|開發商|交房|收楼|办证|辦證|产证|產證|过户|過戶|产权|產權|按揭|房款|contract|breach|payment|property|developer|title|handover|mortgage/i.test(
        text
      )
    )
      return "contract";
    if (/公司|股权|股權|经营|經營|投资|投資|shareholder|equity|company/i.test(text)) return "company";
    if (/婚姻|离婚|離婚|family|divorce/i.test(text)) return "family";
    if (/授权|授權|公证|公證|认证|認證|文件|身份|notarization|authentication|document/i.test(text)) return "identity";
    return "other";
  }

  function routeForCurrentState() {
    if (state.mainland === "no") return null;
    return localRoutes[state.region] || localRoutes.other;
  }

  function routeUrl(route) {
    const target = new URL(route.url, window.location.origin);
    target.searchParams.set("source", "ask-recommendation");
    if (sourceParam) target.searchParams.set("from", sourceParam);
    if (activeTopic) target.searchParams.set("topic", activeTopic);
    if (intentParam) target.searchParams.set("intent", intentParam);
    return target.pathname + target.search + target.hash;
  }

  function updateAd(route, stage) {
    const resolvedRoute = route && route.url ? route : stage === "done" ? routeForCurrentState() : null;
    const hasUserTurn = state.messages.some((message) => message.role === "user");
    const shouldShow = stage === "done" && hasUserTurn && !!(resolvedRoute && resolvedRoute.url);

    if (routeAd) {
      routeAd.hidden = !shouldShow;
      routeAd.setAttribute("aria-hidden", shouldShow ? "false" : "true");
    }
    if (chatMain) {
      chatMain.classList.toggle("has-ad", shouldShow);
    }

    if (!shouldShow || !resolvedRoute) {
      return;
    }

    adTitle.textContent = resolvedRoute.label || "相关专题页";
    adCopy.textContent = "如果想让律师团队进一步联系，可以打开专题页提交基本情况。";
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

  function applyTopicPreset() {
    const preset = topicPresets[activeTopic];
    if (!preset) return null;

    state.region = preset.region || state.region;
    state.mainland = preset.mainland || state.mainland;
    state.matter = preset.matter || state.matter;
    state.summary = preset.summary || state.summary;
    state.stage = localStage();
    return preset;
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

    if (fromChip && activeTopic && !["region", "mainland", "matter"].includes(state.stage)) {
      appendSummary(value || text);
      return;
    }
    if (!fromChip) appendSummary(text);
    if (!fromChip) {
      const inferredMainland = inferMainland(text);
      if (inferredMainland && inferredMainland !== "unsure" && !state.mainland) state.mainland = inferredMainland;
      const inferredMatter = inferMatter(text);
      if (inferredMatter && !state.matter) state.matter = inferredMatter;
    }

    if (state.stage === "region") {
      if (fromChip) {
        state.region = value;
      } else {
        const inferredRegion = inferRegion(text);
        state.region = inferredRegion === "other" ? "" : inferredRegion;
      }
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
    const payload = {
      topic: activeTopic || "",
      region: state.region,
      mainland: state.mainland,
      matter: state.matter,
      summary: state.summary,
      language: "zh-CN",
      source: sourceParam,
      intent: intentParam,
      pageUrl: window.location.href,
      messages: state.messages
    };

    const candidates = preferredEndpointOrder(apiEndpointCandidates());
    let lastError = null;

    for (let index = 0; index < candidates.length; index += 1) {
      const endpoint = candidates[index];
      try {
        const result = await fetchChatJson(endpoint, payload, endpointTimeoutMs(endpoint, index));
        try {
          window.sessionStorage.setItem(LAST_GOOD_ENDPOINT_KEY, endpoint);
        } catch {
          // ignore storage failures
        }
        return result;
      } catch (error) {
        lastError = error;
      }
    }

    throw lastError || new Error("AI endpoint failed");
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

  async function renderAssistantReply(result, options) {
    applyBackendState(result);
    setChips(result.chips || []);
    updatePlaceholder(result.inputPlaceholder);
    updateAd(result.route || null, state.stage);
    await addBot(result.answer || fallbackReply().answer, options);
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
      await renderAssistantReply(result, { typewriter: true, requestId });
    } catch (error) {
      if (requestId !== state.activeRequestId) return;
      typing.remove();
      await renderAssistantReply(fallbackReply(), { typewriter: true, requestId });
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
    const preset = applyTopicPreset();
    chatBody.innerHTML = '<div class="day-pill">今天</div>';
    renderAssistantReply({
      stage: preset ? "done" : "region",
      answer: preset ? preset.greeting : "你好，我是刘毅律师团队的 AI 法律助理。先用聊天方式做初步判断，你现在主要在哪个地区？",
      chips: preset ? preset.chips : regionChips,
      inputPlaceholder: preset ? preset.placeholder : "也可以直接输入你现在主要所在地区",
      route: null,
      state: {
        region: state.region,
        mainland: state.mainland,
        matter: state.matter,
        summary: state.summary
      }
    });
  }
})();
