(function () {
  const chatBody = document.getElementById("chatBody");
  const chatMain = document.querySelector(".chat-main");
  const quickReplies = document.getElementById("quickReplies");
  const form = document.getElementById("chatForm");
  const input = document.getElementById("chatInput");
  const submitButton = form?.querySelector("button[type='submit']");
  const attachButton = document.getElementById("attachButton");
  const attachmentInput = document.getElementById("attachmentInput");
  const attachmentList = document.getElementById("attachmentList");
  const clearChatButton = document.getElementById("clearChat");
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
  const caseEmpty = document.getElementById("caseEmpty");
  const caseContent = document.getElementById("caseContent");
  const caseGoal = document.getElementById("caseGoal");
  const caseFacts = document.getElementById("caseFacts");
  const caseMissing = document.getElementById("caseMissing");
  const LAST_GOOD_ENDPOINT_KEY = "jingwei.ask.chat.endpoint.lastGood";
  const MAX_ATTACHMENTS = 3;
  const MAX_ATTACHMENT_BYTES = 3 * 1024 * 1024;
  const MAX_ATTACHMENT_TEXT = 2600;

  const state = {
    stage: "region",
    region: "",
    mainland: "",
    matter: "",
    summary: "",
    messages: [],
    pendingAttachments: [],
    casePanel: null,
    casePanelPending: false,
    activeRequestId: 0
  };

  const topicPresets = {
    "hk-mainland-property-inheritance": {
      region: "hongkong",
      mainland: "yes",
      matter: "family",
      summary: "客户从香港居民继承中国内地房产过户专题进入，重点关注内地不动产继承、香港文件公证转递、继承人一致性、税费和委托办理。",
      greeting: "我先帮你理顺继承过户。直接说房产城市、谁去世、继承人情况。",
      placeholder: "直接说情况，不用写姓名",
      chips: [
        { label: "深圳房产继承", value: "我想咨询香港居民继承深圳房产过户" },
        { label: "继承人不同意", value: "继承人之间不同意，内地房产还能过户吗？" },
        { label: "香港文件能否用", value: "香港死亡证明和亲属关系证明能不能直接拿到内地用？" }
      ]
    }
  };

  const topicStartOptions = [
    {
      title: "怎么继承过户",
      text: "内地房产，亲人已去世",
      value: "亲人在香港去世，名下有中国内地房产，想先了解继承过户怎么走。"
    },
    {
      title: "香港文件怎么用",
      text: "死亡证明、亲属关系、委托书",
      value: "想问香港死亡证明、亲属关系或委托书，怎么拿到内地使用。"
    },
    {
      title: "有人不同意/联系不上",
      text: "争议、失联、不配合",
      value: "继承人有人不同意、失联或不配合，想问内地房产还能不能处理。"
    }
  ];

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

  function extractEndpointCandidates() {
    return apiEndpointCandidates().map((endpoint) => endpoint.replace(/\/chat(?:\?.*)?$/i, "/extract-file"));
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

  async function fetchExtractJson(endpoint, payload) {
    const controller = new AbortController();
    const timer = window.setTimeout(function () {
      controller.abort();
    }, 18000);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
        signal: controller.signal
      });
      if (!response.ok) throw new Error("File extraction failed");
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

  function addUser(text, displayText) {
    state.messages.push({ role: "user", content: text, displayContent: displayText || text });
    saveChatSession();
    return addMessage(displayText || text, "user");
  }

  function setBusy(busy) {
    if (submitButton) submitButton.disabled = busy;
    if (attachButton) attachButton.disabled = busy;
    input.disabled = busy;
  }

  function isSystemShortcut(event) {
    return event.ctrlKey || event.metaKey || event.altKey;
  }

  function formatBytes(bytes) {
    const size = Number(bytes || 0);
    if (size >= 1024 * 1024) return (size / 1024 / 1024).toFixed(1) + "MB";
    if (size >= 1024) return Math.round(size / 1024) + "KB";
    return size + "B";
  }

  function fileKindLabel(kind, type) {
    if (kind === "pdf") return "PDF";
    if (kind === "docx") return "Word";
    if (kind === "image" || /^image\//i.test(type || "")) return "图片";
    if (kind === "text") return "文本";
    return "附件";
  }

  function readFileData(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(String(reader.result || ""));
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
  }

  function attachmentMessage(attachments) {
    const usable = (attachments || []).slice(0, MAX_ATTACHMENTS);
    if (!usable.length) return "";

    const parts = ["\n\n[客户上传资料]"];
    usable.forEach((file, index) => {
      const text = String(file.text || "").trim().slice(0, MAX_ATTACHMENT_TEXT);
      parts.push(`${index + 1}. ${file.name}（${fileKindLabel(file.kind, file.type)}，${formatBytes(file.size)}）`);
      if (text) {
        parts.push("可读取文字摘录：");
        parts.push(text);
      }
      if (file.note) parts.push("读取说明：" + file.note);
    });
    parts.push("[请结合客户文字和上述附件内容判断；若附件是图片或扫描件且没有可读取文字，请追问客户补充图片上的关键内容，不要假装已经看清图片。]");
    return parts.join("\n");
  }

  function attachmentDisplay(attachments) {
    const names = (attachments || []).map((file) => file.name).filter(Boolean);
    return names.length ? "\n\n已上传资料：" + names.join("、") : "";
  }

  function renderAttachments() {
    if (!attachmentList) return;
    attachmentList.innerHTML = "";
    if (!state.pendingAttachments.length) {
      attachmentList.hidden = true;
      return;
    }

    state.pendingAttachments.forEach((file, index) => {
      const pill = document.createElement("span");
      pill.className = "attachment-pill" + (file.error ? " is-error" : "");

      const label = document.createElement("span");
      label.textContent = file.name;
      const meta = document.createElement("small");
      meta.textContent = fileKindLabel(file.kind, file.type) + " " + formatBytes(file.size);
      const remove = document.createElement("button");
      remove.type = "button";
      remove.textContent = "×";
      remove.setAttribute("aria-label", "移除 " + file.name);
      remove.addEventListener("click", () => {
        state.pendingAttachments.splice(index, 1);
        renderAttachments();
      });

      pill.appendChild(label);
      pill.appendChild(meta);
      pill.appendChild(remove);
      attachmentList.appendChild(pill);
    });
    attachmentList.hidden = false;
  }

  async function extractFiles(files) {
    const selected = Array.from(files || []).slice(0, MAX_ATTACHMENTS);
    if (!selected.length) return;

    const tooLarge = selected.filter((file) => file.size > MAX_ATTACHMENT_BYTES).map((file) => ({
      name: file.name,
      type: file.type,
      kind: "",
      size: file.size,
      text: "",
      note: "文件超过 3MB，未读取内容。",
      error: true
    }));
    const readable = selected.filter((file) => file.size <= MAX_ATTACHMENT_BYTES);
    const payloadFiles = [];

    for (const file of readable) {
      payloadFiles.push({
        name: file.name,
        type: file.type,
        size: file.size,
        data: await readFileData(file)
      });
    }

    let extracted = [];
    if (payloadFiles.length) {
      const endpoints = extractEndpointCandidates();
      for (let index = 0; index < endpoints.length; index += 1) {
        try {
          const result = await fetchExtractJson(endpoints[index], { files: payloadFiles });
          extracted = Array.isArray(result.attachments) ? result.attachments : [];
          break;
        } catch {
          extracted = [];
        }
      }
      if (!extracted.length) {
        extracted = payloadFiles.map((file) => ({
          name: file.name,
          type: file.type,
          kind: /^image\//i.test(file.type || "") ? "image" : "unknown",
          size: file.size,
          text: "",
          note: "暂时无法读取附件内容，请补充关键文字。",
          error: true
        }));
      }
    }

    state.pendingAttachments = extracted.concat(tooLarge).slice(0, MAX_ATTACHMENTS);
    renderAttachments();
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

  function removeStartGuide() {
    const guide = document.getElementById("startGuide");
    if (guide) guide.remove();
  }

  function renderStartGuide() {
    if (!activeTopic || document.getElementById("startGuide")) return;

    const guide = document.createElement("div");
    guide.className = "start-guide";
    guide.id = "startGuide";

    const label = document.createElement("p");
    label.className = "start-label";
    label.textContent = "先问哪件事？";
    guide.appendChild(label);

    const optionsWrap = document.createElement("div");
    optionsWrap.className = "start-options";

    topicStartOptions.forEach((item, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "start-card" + (index === 0 ? " is-active" : "");
      button.dataset.value = item.value;

      const title = document.createElement("strong");
      title.textContent = item.title;
      const text = document.createElement("span");
      text.textContent = item.text;

      button.appendChild(title);
      button.appendChild(text);
      button.addEventListener("click", function () {
        handleTurn(item.value, { fromChip: true, value: item.value });
      });

      optionsWrap.appendChild(button);
    });

    guide.appendChild(optionsWrap);

    const sample = document.createElement("div");
    sample.className = "sample-prompt";
    sample.innerHTML = "<strong>可以直接套一句</strong><p>父亲在深圳有房，香港去世，想继承过户。</p>";
    guide.appendChild(sample);

    chatBody.appendChild(guide);
    scrollToBottom();
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
      return { chips: [], placeholder: summaryPlaceholder() };
    }
    return { chips: [], placeholder: "也可以继续补充你的情况" };
  }

  function summaryQuestion() {
    if (state.region && state.mainland === "yes") {
      return "再补充一句：对方、财产或主要证据在内地哪里，最想先解决什么。";
    }
    if (state.region) {
      return "再补充一句：事项是否涉及内地、对方或财产在哪里、最想先解决什么。";
    }
    return "最后用一句话补充核心情况：你在哪里、对方或财产在哪里、最想先解决什么。";
  }

  function summaryPlaceholder() {
    if (state.region && state.mainland === "yes") {
      return "例如：对方公司在深圳，合同履行地在内地，想追回货款";
    }
    if (state.region) {
      return "例如：对方公司在深圳，想先判断能不能起诉";
    }
    return "例如：我人在美国，对方公司在深圳，合同履行地在内地";
  }

  function parseJson(raw) {
    try {
      return JSON.parse(raw);
    } catch {
      return null;
    }
  }

  function normalizeCasePanel(panel) {
    if (!panel || typeof panel !== "object") return null;
    const goal = String(panel.goal || "").trim().slice(0, 28);
    const facts = Array.isArray(panel.facts) ? panel.facts : [];
    const missing = Array.isArray(panel.missing) ? panel.missing : [];
    const cleanList = (items, limit) => Array.from(new Set(items
      .map((item) => String(item || "").trim())
      .filter(Boolean)
      .map((item) => item.slice(0, 42)))).slice(0, limit);
    const cleanFacts = cleanList(facts, 8);
    const cleanMissing = cleanList(missing, 5);
    if (!goal && !cleanFacts.length && !cleanMissing.length) return null;
    const normalized = {
      goal: goal || "整理案情",
      facts: cleanFacts,
      missing: cleanMissing
    };
    return normalized;
  }

  function normalizeSavedMessages(messages) {
    if (!Array.isArray(messages)) return [];
    return messages
      .map((message) => ({
        role: message && message.role === "assistant" ? "assistant" : "user",
        content: String(message && message.content ? message.content : "").trim(),
        displayContent: String(message && message.displayContent ? message.displayContent : "").trim()
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
        casePanel: state.casePanel || null,
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

  function clearStoredSession() {
    try {
      window.sessionStorage.removeItem(SESSION_KEY);
      window.localStorage.removeItem(BACKUP_KEY);
      window.sessionStorage.removeItem(SESSION_BASE_KEY);
      window.localStorage.removeItem(BACKUP_BASE_KEY);
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
    state.casePanel = normalizeCasePanel(payload.state.casePanel);
    state.casePanelPending = false;

    chatBody.innerHTML = '<div class="day-pill">今天</div>';
    savedMessages.forEach((message) => {
      addMessage(message.displayContent || message.content, message.role === "assistant" ? "bot" : "user");
    });

    const stage = localStage();
    state.stage = stage;
    const ui = stageUi(stage);
    setChips(ui.chips);
    updatePlaceholder(ui.placeholder);
    updateAd(routeForCurrentState(), stage);
    updateCasePanel();
    if (activeTopic && !state.messages.some((message) => message.role === "user")) {
      renderStartGuide();
    }

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

  function isRoutingOnlyLine(line) {
    const value = String(line || "").trim();
    if (!value) return true;
    if (/^(我在|人在|目前在|现在在|現在在|身在|住在)?(香港|澳门|澳門|新加坡|马来西亚|馬來西亞|美国|美國|美国华人|美國華人)$/.test(value)) return true;
    if (/^(涉及中国内地|涉及中國內地|不涉及中国内地|不涉及中國內地|暂时不确定|暫時不確定|不确定|不確定|只涉及当地法律|只涉及本地法律)$/.test(value)) return true;
    if (/^(合同\/商业合作|合同\/商業合作|公司\/股权|公司\/股權|婚姻家事\/继承|婚姻家事\/繼承|身份\/授权\/文件|身份\/授權\/文件|其他民商事问题|其他民商事問題)$/.test(value)) return true;
    return false;
  }

  function caseDetailSource() {
    return userCaseSource()
      .split("\n")
      .map((line) => line.trim())
      .filter((line) => line && !isRoutingOnlyLine(line))
      .join("\n");
  }

  function hasCaseDetails() {
    return caseDetailSource().replace(/\s+/g, "").length >= 8;
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
    return "";
  }

  function firstMatch(text, pattern) {
    const matched = String(text || "").match(pattern);
    return matched ? matched[0] : "";
  }

  function regexMatches(text, pattern) {
    const flags = pattern.flags.includes("g") ? pattern.flags : pattern.flags + "g";
    const regex = new RegExp(pattern.source, flags);
    const matches = [];
    let matched = regex.exec(String(text || ""));
    while (matched) {
      matches.push({
        index: matched.index,
        end: matched.index + matched[0].length
      });
      if (!matched[0]) regex.lastIndex += 1;
      matched = regex.exec(String(text || ""));
    }
    return matches;
  }

  function insideSpan(index, spans) {
    return spans.some((span) => index >= span.index && index < span.end);
  }

  function latestCaseSignal(source, positivePattern, negativePattern) {
    const negativeSpans = regexMatches(source, negativePattern);
    const events = negativeSpans.map((span) => ({
      index: span.index,
      end: span.end,
      value: "no"
    }));

    regexMatches(source, positivePattern).forEach((span) => {
      if (!insideSpan(span.index, negativeSpans)) {
        events.push({
          index: span.index,
          end: span.end,
          value: "yes"
        });
      }
    });

    if (!events.length) return "";
    events.sort((a, b) => a.index - b.index || a.end - b.end);
    return events[events.length - 1].value;
  }

  function userCaseSource() {
    const presetSummary = String((topicPresets[activeTopic] && topicPresets[activeTopic].summary) || "");
    const parts = [];
    state.messages
      .filter((message) => message.role === "user")
      .map((message) => message.content)
      .forEach((content) => parts.push(content));

    String(state.summary || "")
      .split("\n")
      .map((line) => line.trim())
      .filter((line) => line && line !== presetSummary)
      .forEach((line) => parts.push(line));

    return Array.from(new Set(parts.map((part) => String(part || "").trim()).filter(Boolean))).join("\n");
  }

  function regionFact(source) {
    if (/香港居民|香港人|港人/i.test(source)) return "香港居民";
    if (/我在香港|人在香港|目前在香港|现在在香港|現在在香港|身在香港|住在香港/i.test(source)) return "当前地区：香港";
    if (/香港/i.test(source)) return "香港";
    if (/澳门|澳門/i.test(source)) return "澳门居民";
    if (/美国|美國|纽约|紐約|加州|洛杉矶|洛杉磯/i.test(source)) return /华人|華人/.test(source) ? "美国华人" : "美国客户";
    if (/加拿大|温哥华|溫哥華|多伦多|多倫多/i.test(source)) return /华人|華人/.test(source) ? "加拿大华人" : "加拿大客户";
    if (/英国|英國|伦敦|倫敦/i.test(source)) return /华人|華人/.test(source) ? "英国华人" : "英国客户";
    if (/澳大利亚|澳大利亞|澳洲|悉尼|雪梨|墨尔本|墨爾本/i.test(source)) return /华人|華人/.test(source) ? "澳大利亚华人" : "澳大利亚客户";
    if (/日本|东京|東京|大阪/i.test(source)) return /华人|華人/.test(source) ? "日本华人" : "日本客户";
    if (/新加坡/i.test(source)) return "新加坡居民";
    if (/马来西亚|馬來西亞/i.test(source)) return "马来西亚客户";
    return "";
  }

  function mainlandCityFact(source) {
    return firstMatch(
      source,
      /深圳|广州|廣州|上海|北京|佛山|珠海|东莞|東莞|苏州|蘇州|杭州|南京|天津|重庆|重慶|武汉|武漢|成都|西安|青岛|青島|厦门|廈門/i
    );
  }

  function propertyAreaFact(source) {
    const pattern = /(\d{1,4}(?:\.\d{1,2})?)\s*(?:平方米|平方|平米|平|㎡|m2|m²)/gi;
    let matched = pattern.exec(String(source || ""));
    let area = "";
    while (matched) {
      area = matched[1].replace(/\.0+$/, "");
      matched = pattern.exec(String(source || ""));
    }
    return area ? "面积约" + area + "平" : "";
  }

  function deathStatus(source) {
    return latestCaseSignal(
      source,
      /去世|过世|過世|死亡|身故|离世|離世|过身|過身/i,
      /(?:没人|沒人|没有人|沒有人|无人|無人|没有亲人|沒有親人|没有家人|沒有家人|没有谁|沒有誰|没有任何人|沒有任何人)[^，。；、,.\n]{0,8}(?:去世|过世|過世|死亡|身故|离世|離世|过身|過身)|(?:没有去世|沒有去世|没去世|沒去世|还没去世|還沒去世|尚未去世|未去世|没有发生死亡|沒有發生死亡)|(?:都|全部|全都)[^，。；、,.\n]{0,8}(?:健在|在世|还在|還在)/i
    );
  }

  function deceasedFact(source) {
    const status = deathStatus(source);
    if (status === "no") return "无人去世";
    if (status !== "yes") return "";
    if (/父亲|父親|爸爸|爹/i.test(source)) return "父亲去世";
    if (/母亲|母親|妈妈|媽媽/i.test(source)) return "母亲去世";
    if (/爷爷|爺爺|祖父/i.test(source)) return "祖父去世";
    if (/奶奶|祖母/i.test(source)) return "祖母去世";
    if (/丈夫|先生|老公/i.test(source)) return "配偶去世";
    if (/妻子|太太|老婆/i.test(source)) return "配偶去世";
    return "亲人已去世";
  }

  function hasPositiveTitleInfo(source) {
    const titleWords = "房产证|房產證|不动产权证|不動產權證|产权证|產權證";
    return new RegExp(
      [
        "(?:已有|已經有|已经有|有)\\s*(?:" + titleWords + ")",
        "(?:拿到|取得|可提供|可以提供)[^\\n，。；、,.]{0,6}(?:" + titleWords + ")",
        "(?:" + titleWords + ")(?:已经有|已經有|已有|在手|齐全|齊全|可以提供|可提供)"
      ].join("|"),
      "i"
    ).test(source);
  }

  function hasUnclearTitleInfo(source) {
    const shortText = "[^\\n，。；、,.]{0,8}";
    const titleWords = "房产证|房產證|不动产权证|不動產權證|产权证|產權證";
    return new RegExp(
      [
        "未办证",
        "未辦證",
        "没办" + shortText + "证",
        "沒辦" + shortText + "證",
        "没有" + shortText + "(?:" + titleWords + ")",
        "沒有" + shortText + "(?:" + titleWords + ")",
        "不清楚" + shortText + "(?:" + titleWords + ")",
        "不确定" + shortText + "(?:" + titleWords + ")",
        "不知道" + shortText + "(?:" + titleWords + ")",
        "是否有" + shortText + "(?:" + titleWords + ")",
        "有没有" + shortText + "(?:" + titleWords + ")",
        "有沒有" + shortText + "(?:" + titleWords + ")"
      ].join("|"),
      "i"
    ).test(source);
  }

  function lostContactStatus(source) {
    return latestCaseSignal(
      source,
      /失联|失聯|联系不上|聯繫不上|联络不上|聯絡不上|找不到人/i,
      /(?:没有|沒有|无|無|暂无|暫無|不存在|没人|沒人|没有人|沒有人)[^，。；、,.\n]{0,10}(?:失联|失聯|联系不上|聯繫不上|联络不上|聯絡不上|找不到人)|(?:都|全部|全都)[^，。；、,.\n]{0,8}(?:联系得上|聯繫得上|能联系|能聯繫|可联系|可聯繫)/i
    );
  }

  function disputeStatus(source) {
    return latestCaseSignal(
      source,
      /不同意|不配合|争议|爭議|纠纷|糾紛|反对|反對/i,
      /(?:没有|沒有|无|無|暂无|暫無|不存在)[^，。；、,.\n]{0,10}(?:争议|爭議|纠纷|糾紛|不配合|不同意|反对|反對)|(?:都|全部|全都|一致)[^，。；、,.\n]{0,8}(?:同意|配合)/i
    );
  }

  function agreementConfirmed(source) {
    return /都同意|全部同意|全都同意|一致同意|都配合|全部配合|没有争议|沒有爭議|无争议|無爭議/i.test(source);
  }

  function hasCaseConflict(source) {
    return lostContactStatus(source) === "yes" || disputeStatus(source) === "yes";
  }

  function hasInheritanceContext(source) {
    if (activeTopic === "hk-mainland-property-inheritance") return true;
    return /继承|繼承|遗产|遺產|遗嘱|遺囑|法定继承|法定繼承|过世|過世|去世|死亡|身故|继承人|繼承人/i.test(source);
  }

  function hasMatterSignal(source) {
    return /合同|合约|合約|合作|货款|貨款|公司|股权|股權|投资|投資|婚姻|离婚|離婚|继承|繼承|遗产|遺產|授权|授權|委托|委託|公证|公證|认证|認證|文件|身份|纠纷|糾紛|诉讼|訴訟|律师|律師|法院|房产|房產|不动产|不動產/i.test(source);
  }

  function matterFact(source) {
    const matter = state.matter || inferMatter(source);
    if (matter === "contract") return "合同/商业合作";
    if (matter === "company") return "公司/股权";
    if (matter === "family") return "婚姻家事/继承";
    if (matter === "identity") return "身份/授权/文件";
    if (matter === "other" && hasMatterSignal(source)) return "其他民商事问题";
    return "";
  }

  function collectCaseFacts(source) {
    const facts = [];
    const city = mainlandCityFact(source);
    const region = regionFact(source);
    const deceased = deceasedFact(source);
    const area = propertyAreaFact(source);
    const lostStatus = lostContactStatus(source);
    const conflictStatus = disputeStatus(source);
    const isInheritance = hasInheritanceContext(source);
    const matter = matterFact(source);

    if (region) facts.push(region);
    if (/中国内地|中國內地|内地|內地|大陆|大陸|mainland/i.test(source) || state.mainland === "yes") facts.push("涉及中国内地");
    if (matter) facts.push(matter);
    if (city) facts.push(isInheritance || /房产|房產|楼房|樓房|不动产|不動產|物业|物業/i.test(source) ? city + "房产" : city);
    if (area) facts.push(area);
    if (isInheritance && deceased) facts.push(deceased);
    if (isInheritance && /没有遗嘱|沒有遺囑|无遗嘱|無遺囑|没遗嘱|沒遺囑/i.test(source)) facts.push("无遗嘱");
    else if (isInheritance && /有遗嘱|有遺囑|留了遗嘱|留了遺囑|遗嘱|遺囑/i.test(source)) facts.push("有遗嘱");
    if (isInheritance && (agreementConfirmed(source) || conflictStatus === "no")) facts.push("继承人同意");
    if (isInheritance && conflictStatus === "yes") facts.push("有争议/不配合");
    if (isInheritance && lostStatus === "yes") facts.push("有继承人失联");
    else if (isInheritance && lostStatus === "no") facts.push("没有失联");
    if (isInheritance && /放弃继承|放棄繼承|放弃份额|放棄份額/i.test(source)) facts.push("有人放弃继承");
    if ((isInheritance || /房产|房產|不动产|不動產/.test(source)) && hasUnclearTitleInfo(source)) facts.push("房产证未确认");
    else if ((isInheritance || /房产|房產|不动产|不動產/.test(source)) && hasPositiveTitleInfo(source)) facts.push("已有产权证");
    else if ((isInheritance || /房产|房產|不动产|不動產/.test(source)) && /房产证|房產證|不动产权证|不動產權證|产权证|產權證/i.test(source)) facts.push("提到产权证");
    if (isInheritance && /死亡证明|死亡證明|亲属关系|親屬關係|香港文件|公证|公證|转递|轉遞|委托书|委託書/i.test(source)) facts.push("提到文件材料");
    if (/委托|委託|代办|代辦|回不去|不到内地|不到內地/i.test(source)) facts.push("想委托办理");
    if (isInheritance && /卖房|賣房|卖掉|賣掉|出售|转卖|轉賣/i.test(source)) facts.push("继承后出售");
    return Array.from(new Set(facts)).slice(0, 8);
  }

  function caseGoalText(source) {
    const city = mainlandCityFact(source);
    const property = city ? city + "房产" : "内地房产";
    if (!hasInheritanceContext(source)) {
      const matter = matterFact(source);
      if (matter) return "整理" + matter + "问题";
      if (state.mainland === "yes" || /中国内地|中國內地|内地|內地|大陆|大陸/i.test(source)) return "整理内地法律事项";
      return "等待补充";
    }
    if (deathStatus(source) === "no") return "确认" + property + "安排";
    if (/卖房|賣房|卖掉|賣掉|出售|转卖|轉賣/i.test(source)) return "继承后出售" + property;
    if (hasCaseConflict(source)) return "处理" + property + "继承问题";
    if (/文件|死亡证明|死亡證明|亲属关系|親屬關係|公证|公證|转递|轉遞/i.test(source)) return "确认香港文件能否用于内地";
    if (/继承|繼承|过户|過戶|楼盘|樓盤|房产|房產|不动产|不動產/i.test(source)) return "继承" + property;
    return "整理跨境继承事项";
  }

  function caseMissingItems(source) {
    const items = [];
    const hasCity = !!mainlandCityFact(source);
    const hasMainlandContext = /中国内地|中國內地|内地|內地|大陆|大陸|国内|國內|深圳|广州|廣州|上海|北京|佛山|珠海|东莞|東莞|房产|房產|不动产|不動產/i.test(source);
    const isInheritance = hasInheritanceContext(source);
    const death = deathStatus(source);
    const hasDeceased = death === "yes";
    const hasWill = /遗嘱|遺囑/i.test(source);
    const lostStatus = lostContactStatus(source);
    const conflictStatus = disputeStatus(source);
    const hasAgreement = agreementConfirmed(source) || conflictStatus || lostStatus === "yes";
    const hasTitle = hasUnclearTitleInfo(source) || hasPositiveTitleInfo(source) || /房产证|房產證|不动产权证|不動產權證|产权证|產權證/i.test(source);
    const hasDocuments = /死亡证明|死亡證明|亲属关系|親屬關係|香港文件|公证|公證|转递|轉遞/i.test(source);
    const hasRegion = !!regionFact(source);

    if (!isInheritance) {
      if (!hasRegion) items.push("客户目前所在地区或身份");
      if (!state.mainland && !hasMainlandContext) items.push("事项是否涉及中国内地");
      if (!state.matter || (state.matter === "other" && !hasMatterSignal(source))) items.push("大致属于哪类法律事务");
      if (state.mainland === "yes" || hasMainlandContext) items.push("对方、财产或证据在内地哪里");
      items.push("最想先解决什么");
      return Array.from(new Set(items)).slice(0, 5);
    }
    if (!hasRegion) items.push("客户是否为香港居民或其他境外身份");
    if (!hasCity) items.push("房产具体在哪个内地城市");
    if (death === "no") {
      items.push("想办理赠与/买卖过户、遗嘱安排，还是提前了解将来继承");
      if (!hasTitle) items.push("房产登记在谁名下，是否已有房产证/不动产权证");
      return Array.from(new Set(items)).slice(0, 5);
    }
    if (!hasDeceased) items.push("谁去世了，与客户是什么关系");
    items.push("配偶、父母、子女和全部继承人范围");
    if (!hasWill) items.push("是否有遗嘱或遗产分配文件");
    if (!hasAgreement) {
      items.push(lostStatus === "no" ? "继承人是否全部同意，有无不配合" : "继承人是否全部同意，有无失联或不配合");
    }
    if (!hasTitle) items.push("房产证/不动产权证是否已有");
    if (!hasDocuments) items.push("香港死亡证明、亲属关系证明是否已准备");
    if (hasDocuments && !/公证|公證|转递|轉遞/i.test(source)) items.push("香港文件是否已公证转递");

    return Array.from(new Set(items)).slice(0, 5);
  }

  function buildLocalCasePanel(source) {
    const facts = collectCaseFacts(source);
    const missing = caseMissingItems(source);
    if (!facts.length && !missing.length) return null;
    const hasMatter = /继承|繼承|过户|過戶|楼盘|樓盤|房产|房產|不动产|不動產|中国内地|中國內地|内地|內地|大陆|大陸|合同|公司|股权|股權|婚姻|离婚|離婚|授权|授權|文件|公证|公證|纠纷|糾紛/i.test(source);
    return normalizeCasePanel({
      goal: hasMatter ? caseGoalText(source) : "等待补充",
      facts,
      missing
    });
  }

  function mergeCasePanels(primary, fallback) {
    if (!primary) return fallback;
    if (!fallback) return primary;
    return normalizeCasePanel({
      goal: primary.goal || fallback.goal,
      facts: [...(fallback.facts || []), ...(primary.facts || [])],
      missing: (primary.missing && primary.missing.length) ? primary.missing : fallback.missing
    });
  }

  function updateCasePanel() {
    if (!caseEmpty || !caseContent || !caseGoal || !caseFacts || !caseMissing) return;
    const source = userCaseSource();
    const hasUserTurn = state.messages.some((message) => message.role === "user");

    if (!hasUserTurn || !source) {
      caseEmpty.hidden = false;
      caseContent.hidden = true;
      return;
    }

    caseEmpty.hidden = true;
    caseContent.hidden = false;
    const localPanel = buildLocalCasePanel(source);
    const panel = state.casePanelPending
      ? localPanel || {
          goal: "正在整理",
          facts: ["AI正在核对"],
          missing: ["根据你刚补充的内容更新案情要点"]
        }
      : mergeCasePanels(state.casePanel, localPanel);

    if (!panel) {
      caseGoal.textContent = "等待补充";
      caseFacts.innerHTML = "";
      const tag = document.createElement("span");
      tag.className = "case-tag";
      tag.textContent = "等待AI判断";
      caseFacts.appendChild(tag);
      caseMissing.innerHTML = "";
      const li = document.createElement("li");
      li.textContent = "继续说你的情况，我会重新整理右侧要点";
      caseMissing.appendChild(li);
      return;
    }

    caseGoal.textContent = panel.goal || "整理案情";

    caseFacts.innerHTML = "";
    const facts = Array.isArray(panel.facts) ? panel.facts : [];
    (facts.length ? facts : ["已开始整理"]).forEach((fact) => {
      const tag = document.createElement("span");
      tag.className = "case-tag";
      tag.textContent = fact;
      caseFacts.appendChild(tag);
    });

    caseMissing.innerHTML = "";
    const missing = Array.isArray(panel.missing) ? panel.missing : [];
    missing.forEach((item) => {
      const li = document.createElement("li");
      li.textContent = item;
      caseMissing.appendChild(li);
    });
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

    adTitle.textContent = resolvedRoute.label || "需要律师进一步看？";
    adCopy.textContent = "有争议、文件缺失、继承人失联或准备出售时，可以让律师团队继续判断。";
    adLink.href = routeUrl(resolvedRoute);
    adLink.textContent = "查看专题入口";
    adLink.classList.remove("is-disabled");
  }

  function localStage() {
    if (!state.region) return "region";
    if (!state.mainland) return "mainland";
    if (state.mainland === "no") return "done";
    if (!state.matter) return "matter";
    if (!hasCaseDetails()) return "summary";
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

  function renderInitialChat() {
    const preset = applyTopicPreset();
    chatBody.innerHTML = '<div class="day-pill">今天</div>';
    return renderAssistantReply({
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
    }).then(function () {
      if (preset) renderStartGuide();
    });
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
        answer: summaryQuestion(),
        chips: [],
        inputPlaceholder: summaryPlaceholder(),
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
    state.casePanel = normalizeCasePanel(result && result.casePanel);
    state.casePanelPending = false;
    setChips(result.chips || []);
    updatePlaceholder(result.inputPlaceholder);
    updateAd(result.route || null, state.stage);
    updateCasePanel();
    await addBot(result.answer || fallbackReply().answer, options);
  }

  async function handleTurn(text, options) {
    const cleaned = String(text || "").trim();
    const attachments = state.pendingAttachments.slice();
    if (!cleaned && !attachments.length) return;
    const userText = cleaned || "我上传了资料，请先帮我看重点。";
    const fullText = userText + attachmentMessage(attachments);
    const displayText = userText + attachmentDisplay(attachments);

    removeStartGuide();
    addUser(fullText, displayText);
    applyChoice(userText, options);
    state.casePanel = null;
    state.casePanelPending = true;
    updateCasePanel();
    input.value = "";
    input.style.height = "auto";
    state.pendingAttachments = [];
    renderAttachments();
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
    if (isSystemShortcut(event)) return;
    if (event.key !== "Enter" || event.shiftKey) return;
    if (event.isComposing || isComposing || event.keyCode === 229) return;
    if (input.disabled) return;
    if (!String(input.value || "").trim() && !state.pendingAttachments.length) return;

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

  if (attachButton && attachmentInput) {
    attachButton.addEventListener("click", function () {
      attachmentInput.click();
    });

    attachmentInput.addEventListener("change", async function () {
      await extractFiles(attachmentInput.files);
      attachmentInput.value = "";
    });
  }

  if (clearChatButton) {
    clearChatButton.addEventListener("click", function () {
      state.activeRequestId += 1;
      state.stage = "region";
      state.region = "";
      state.mainland = "";
      state.matter = "";
      state.summary = "";
      state.messages = [];
      state.pendingAttachments = [];
      state.casePanel = null;
      state.casePanelPending = false;
      input.value = "";
      input.style.height = "auto";
      clearStoredSession();
      setBusy(false);
      renderAttachments();
      renderInitialChat();
    });
  }

  window.addEventListener("pagehide", saveChatSession);

  if (!restoreChatSession()) {
    renderInitialChat();
  }
})();
