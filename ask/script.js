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
  const historyChatButton = document.getElementById("historyChat");
  const historyPopover = document.getElementById("historyPopover");
  const historyList = document.getElementById("historyList");
  const historyCloseButton = document.getElementById("historyClose");
  const clearChatButton = document.getElementById("clearChat");
  const urlParams = new URLSearchParams(window.location.search);
  const DEFAULT_TOPIC = "";
  const activeTopic = String(urlParams.get("topic") || DEFAULT_TOPIC).trim();
  const sourceParam = urlParams.get("source") || "";
  const intentParam = urlParams.get("intent") || "";
  const isGptAskRoute = /\/ask\/gpt\/?$/i.test(window.location.pathname);
  const isMinimalAskFramework = isGptAskRoute || /\/ask\/?$/i.test(window.location.pathname);
  const assistantVariant = isGptAskRoute ? "ask-gpt-openai" : "ask-deepseek-minimal";
  const modelProvider = isGptAskRoute ? "openai" : "deepseek";
  const storageSuffix = isGptAskRoute ? ".gpt" : ".simple";
  const SESSION_BASE_KEY = "jingwei.ask.simple.chat.session.v1";
  const BACKUP_BASE_KEY = "jingwei.ask.simple.chat.backup.v1";
  const ARCHIVE_BASE_KEY = "jingwei.ask.simple.chat.archive.v1";
  const VISITOR_BASE_KEY = "jingwei.ask.simple.visitor.v1";
  const SESSION_KEY = "jingwei.ask.simple.chat.session.v1" + storageSuffix;
  const BACKUP_KEY = "jingwei.ask.simple.chat.backup.v1" + storageSuffix;
  const ARCHIVE_KEY = "jingwei.ask.simple.chat.archive.v1" + storageSuffix;
  let isComposing = false;
  let attachmentRequestSerial = 0;

  const adTitle = document.getElementById("adTitle");
  const adCopy = document.getElementById("adCopy");
  const adLink = document.getElementById("adLink");
  const routeAd = document.getElementById("routeAd");
  const leadCaptureCard = document.getElementById("leadCaptureCard");
  const leadCaptureForm = document.getElementById("leadCaptureForm");
  const leadCaptureFormWrap = document.getElementById("leadCaptureFormWrap");
  const leadCaptureSuccess = document.getElementById("leadCaptureSuccess");
  const leadNameInput = document.getElementById("leadName");
  const leadRegionSelect = document.getElementById("leadRegion");
  const leadCustomCodeWrap = document.getElementById("leadCustomCodeWrap");
  const leadCustomCodeInput = document.getElementById("leadCustomCode");
  const leadPhoneInput = document.getElementById("leadPhone");
  const leadPhoneHint = document.getElementById("leadPhoneHint");
  const leadAltContactInput = document.getElementById("leadAltContact");
  const leadMatterInput = document.getElementById("leadMatter");
  const leadConsentInput = document.getElementById("leadConsent");
  const leadWebsiteInput = document.getElementById("leadWebsite");
  const leadStartedAtInput = document.getElementById("leadStartedAt");
  const leadStatus = document.getElementById("leadStatus");
  const leadSubmitButton = document.getElementById("leadSubmitButton");
  const caseEmpty = document.getElementById("caseEmpty");
  const caseContent = document.getElementById("caseContent");
  const caseGoal = document.getElementById("caseGoal");
  const caseFacts = document.getElementById("caseFacts");
  const LAST_GOOD_ENDPOINT_KEY = "jingwei.ask.simple.chat.endpoint.lastGood";
  const MAX_ATTACHMENTS = 3;
  const MAX_ATTACHMENT_BYTES = 3 * 1024 * 1024;
  const MAX_ATTACHMENT_TEXT = 2600;
  const MAX_CHAT_HISTORY_MESSAGES = 400;
  const LEAD_CAPTURE_MIN_USER_TURNS = 3;
  const PROACTIVE_DELAYS = [30000, 90000, 180000];
  const GPT_IDLE_FOLLOWUP_DELAY_MS = 60000;
  const GPT_IDLE_FOLLOWUP_COOLDOWN_MS = 10 * 60 * 1000;
  const BOTTOM_STICK_THRESHOLD = 72;
  let suppressScrollTracking = false;
  let leadCaptureSubmitted = false;

  const state = {
    sessionId: createSessionId(),
    visitorId: getOrCreateVisitorId(),
    stage: "region",
    region: "",
    mainland: "",
    matter: "",
    summary: "",
    messages: [],
    pendingAttachments: [],
    currentTurnAttachments: [],
    casePanel: null,
    casePanelPending: false,
    workflow: null,
    intake: null,
    conversion: null,
    lead: null,
    activeRequestId: 0,
    isBusy: false,
    attachmentLoadPromise: null,
    followLatest: true
  };
  let proactivePlanToken = 0;
  let proactiveTimers = [];
  let proactiveTypingRow = null;
  let lastGptIdleCareAt = 0;

  const topicPresets = {
    "hk-mainland-property-inheritance": {
      region: "hongkong",
      mainland: "yes",
      matter: "family",
      summary: "客户从香港居民继承中国内地房产过户专题进入，重点关注内地不动产继承、香港文件公证转递、继承人一致性、税费和委托办理。",
      greeting: "我先帮你理顺香港居民处理内地房产。先说房子在哪、现在要办继承还是提前安排。",
      placeholder: "直接说情况，不用写姓名",
      chips: [
        { label: "继承办理", value: "我是香港人，内地有房产，现在需要办理继承过户，想了解怎么走。" },
        { label: "提前安排", value: "我是香港人，内地有房产，目前只是想提前安排将来继承或过户。" },
        { label: "文件/家人配合", value: "我是香港人，内地房产涉及香港文件、公证转递或家人不同意，想先判断怎么处理。" }
      ]
    }
  };

  const topicStartOptions = [
    {
      title: "内地继承/过户",
      text: "房产、遗产、家人安排",
      value: "我想咨询继承或房产过户问题，先帮我判断怎么处理。"
    },
    {
      title: "合同 / 债务",
      text: "合同纠纷、货款追收",
      value: "我想咨询合同或债务追款问题，先帮我梳理风险和下一步。"
    },
    {
      title: "婚姻 / 家事",
      text: "离婚、财产、子女安排",
      value: "我想咨询婚姻家事问题，先帮我判断要补充哪些情况。"
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

  const leadRegionRules = {
    hongkong: {
      code: "+852",
      hint: "香港电话请输入 8 位数字",
      alert: "香港电话请输入 8 位数字",
      validate(value) {
        return /^\d{8}$/.test(value);
      }
    },
    mainland: {
      code: "+86",
      hint: "中国内地手机请输入 11 位数字",
      alert: "中国内地手机请输入 11 位数字",
      validate(value) {
        return /^\d{11}$/.test(value);
      }
    },
    macau: {
      code: "+853",
      hint: "澳门电话请输入 8 位数字",
      alert: "澳门电话请输入 8 位数字",
      validate(value) {
        return /^\d{8}$/.test(value);
      }
    },
    us_ca: {
      code: "+1",
      hint: "美国 / 加拿大电话请输入 10 位数字",
      alert: "美国 / 加拿大电话请输入 10 位数字",
      validate(value) {
        return /^\d{10}$/.test(value);
      }
    },
    uk: {
      code: "+44",
      hint: "英国电话请输入 9 到 11 位数字",
      alert: "英国电话请输入 9 到 11 位数字",
      validate(value) {
        return /^\d{9,11}$/.test(value);
      }
    },
    australia: {
      code: "+61",
      hint: "澳大利亚电话请输入 9 位数字",
      alert: "澳大利亚电话请输入 9 位数字",
      validate(value) {
        return /^\d{9}$/.test(value);
      }
    },
    singapore: {
      code: "+65",
      hint: "新加坡电话请输入 8 位数字",
      alert: "新加坡电话请输入 8 位数字",
      validate(value) {
        return /^\d{8}$/.test(value);
      }
    },
    malaysia: {
      code: "+60",
      hint: "马来西亚电话请输入 8 到 10 位数字",
      alert: "马来西亚电话请输入 8 到 10 位数字",
      validate(value) {
        return /^\d{8,10}$/.test(value);
      }
    },
    other: {
      code: "",
      hint: "其他地区可输入常用号码，并补充国际区号",
      alert: "请填写常用联系电话，并补充国际区号",
      validate(value, customCode) {
        return /^\d{6,20}$/.test(value) && /^\+\d{1,4}$/.test(customCode || "");
      }
    }
  };

  function apiEndpointCandidates() {
    if (window.location.hostname === "127.0.0.1" || window.location.hostname === "localhost") {
      return ["http://127.0.0.1:4100/chat-simple", "https://api.jingwei-law.com/api/chat-simple"];
    }

    const configured = [];
    configured.push("https://api.jingwei-law.com/api/chat-simple");
    configured.push("https://jingwei-vercel-ai-api.vercel.app/api/chat-simple");

    return Array.from(
      new Set(
        configured
          .map((endpoint) => String(endpoint || "").trim())
          .filter(Boolean)
      )
    );
  }

  function endpointTimeoutMs(endpoint, index) {
    if (/api\.jingwei-law\.com/i.test(endpoint)) return 45000;
    return index === 0 ? 35000 : 30000;
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
    return apiEndpointCandidates().map((endpoint) => endpoint.replace(/\/(?:chat-simple|chat)(?:\?.*)?$/i, "/extract-file"));
  }

  function leadEndpointCandidates() {
    return apiEndpointCandidates().map((endpoint) => endpoint.replace(/\/(?:chat-simple|chat)(?:\?.*)?$/i, "/lead-submit"));
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

  async function fetchChatStream(endpoint, payload, timeoutMs, handlers) {
    const controller = new AbortController();
    let timer = 0;
    let streamStarted = false;

    function refreshTimeout() {
      window.clearTimeout(timer);
      timer = window.setTimeout(function () {
        controller.abort();
      }, timeoutMs);
    }

    refreshTimeout();

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "text/event-stream"
        },
        body: JSON.stringify({ ...payload, stream: true }),
        signal: controller.signal
      });

      if (!response.ok || !response.body) throw new Error("AI stream failed");

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      let meta = null;
      let answer = "";

      while (true) {
        refreshTimeout();
        const { value, done } = await reader.read();
        buffer += decoder.decode(value || new Uint8Array(), { stream: !done }).replace(/\r\n/g, "\n").replace(/\r/g, "\n");

        let boundary = buffer.indexOf("\n\n");
        while (boundary !== -1) {
          const rawEvent = buffer.slice(0, boundary).trim();
          buffer = buffer.slice(boundary + 2);
          boundary = buffer.indexOf("\n\n");
          if (!rawEvent) continue;

          const data = rawEvent
            .split("\n")
            .filter((line) => line.startsWith("data:"))
            .map((line) => line.slice(5).trimStart())
            .join("\n")
            .trim();

          if (!data) continue;
          const event = parseJson(data);
          if (!event || typeof event !== "object") continue;
          streamStarted = true;

          if (event.type === "meta" && event.payload) {
            meta = event.payload;
            if (handlers && typeof handlers.onMeta === "function") handlers.onMeta(meta);
            continue;
          }

          if (event.type === "delta" && typeof event.content === "string" && event.content) {
            answer += event.content;
            if (handlers && typeof handlers.onDelta === "function") handlers.onDelta(event.content, answer);
            continue;
          }

          if (event.type === "done") {
            if (typeof event.answer === "string" && event.answer.trim()) answer = event.answer;
            if (event.lead && meta) meta.lead = event.lead;
            if (event.casePanel && meta) meta.casePanel = event.casePanel;
            if (handlers && typeof handlers.onDone === "function") handlers.onDone(answer);
            return { ...(meta || {}), answer, casePanel: event.casePanel || (meta && meta.casePanel) || null };
          }

          if (event.type === "error") {
            throw new Error(event.error || "AI stream failed");
          }
        }

        if (done) break;
      }

      if (!answer) throw new Error("AI stream ended without an answer");
      return { ...(meta || {}), answer };
    } catch (error) {
      if (error && typeof error === "object") error.streamStarted = streamStarted;
      throw error;
    } finally {
      window.clearTimeout(timer);
    }
  }

  async function fetchExtractJson(endpoint, payload) {
    const controller = new AbortController();
    const timer = window.setTimeout(function () {
      controller.abort();
    }, 30000);

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

  function isNearBottom() {
    if (!chatBody) return true;
    return chatBody.scrollHeight - chatBody.scrollTop - chatBody.clientHeight <= BOTTOM_STICK_THRESHOLD;
  }

  function scrollToBottom(force) {
    if (!chatBody) return;
    if (!force && !state.followLatest) return;
    suppressScrollTracking = true;
    chatBody.scrollTop = chatBody.scrollHeight;
    window.requestAnimationFrame(function () {
      suppressScrollTracking = false;
    });
  }

  function resizeInput() {
    if (!input) return;
    const styles = window.getComputedStyle(input);
    const lineHeight = parseFloat(styles.lineHeight) || 23;
    const paddingY = (parseFloat(styles.paddingTop) || 0) + (parseFloat(styles.paddingBottom) || 0);
    const borderY = (parseFloat(styles.borderTopWidth) || 0) + (parseFloat(styles.borderBottomWidth) || 0);
    const boxY = paddingY + borderY;
    const oneLineHeight = Math.ceil(lineHeight + boxY);
    const minHeight = Math.ceil(lineHeight * 2 + boxY);
    const threeLineHeight = Math.ceil(lineHeight * 3 + boxY);
    const maxHeight = Math.ceil(lineHeight * 5 + boxY);

    const previousMinHeight = input.style.minHeight;
    input.style.minHeight = "0px";
    input.style.height = "0px";
    const naturalHeight = Math.max(oneLineHeight, input.scrollHeight + borderY);
    input.style.minHeight = previousMinHeight;
    const targetHeight = naturalHeight > oneLineHeight + 2 ? Math.max(threeLineHeight, naturalHeight) : minHeight;
    input.style.height = Math.min(targetHeight, maxHeight) + "px";
    input.style.overflowY = targetHeight > maxHeight ? "auto" : "hidden";
  }

  function normalizeThinkingPayload(thinking) {
    if (!thinking) return null;
    const value = typeof thinking === "string" ? { content: thinking } : thinking;
    const content = String(value.content || "").replace(/\r\n/g, "\n").trim().slice(0, 24000);
    if (!content) return null;
    const title = String(value.title || "思考过程").trim().slice(0, 24) || "思考过程";
    const summary = String(value.summary || "已思考").trim().slice(0, 60) || "已思考";
    return { title, summary, content };
  }

  function normalizeThinkingForStorage(thinking) {
    const normalized = normalizeThinkingPayload(thinking);
    return normalized
      ? {
          title: normalized.title,
          summary: normalized.summary,
          content: normalized.content
        }
      : null;
  }

  function thinkingStepLines(content) {
    return String(content || "")
      .split("\n")
      .map((line) => line.trim())
      .filter(Boolean)
      .map((line) => line.replace(/^(?:[-*•]|\d+[.)、])\s+/, "").trim())
      .filter(Boolean)
      .slice(0, 12);
  }

  function buildThinkingBlock(thinking, openByDefault) {
    const normalized = normalizeThinkingPayload(thinking);
    if (!normalized) return null;

    const wrap = document.createElement("details");
    wrap.className = "thinking-block";
    if (openByDefault) wrap.open = true;

    const summary = document.createElement("summary");
    summary.textContent = normalized.summary || normalized.title || "已思考";
    wrap.appendChild(summary);

    const steps = thinkingStepLines(normalized.content);
    if (steps.length >= 2) {
      const list = document.createElement("ol");
      list.className = "thinking-steps";
      steps.forEach((step) => {
        const item = document.createElement("li");
        item.textContent = step;
        list.appendChild(item);
      });
      wrap.appendChild(list);
    } else {
      const text = document.createElement("p");
      text.className = "thinking-text";
      text.textContent = normalized.content;
      wrap.appendChild(text);
    }

    return wrap;
  }

  function addMessage(text, type, options) {
    const row = document.createElement("div");
    row.className = "msg-row " + type + (options && options.typing ? " typing" : "");

    const avatar = document.createElement("span");
    avatar.className = "msg-avatar";
    avatar.textContent = type === "user" ? "我" : "律";

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    if (options && options.typing) {
      bubble.classList.add("bubble--typing");

      const typingWrap = document.createElement("div");
      typingWrap.className = "typing-indicator";

      const label = document.createElement("span");
      label.className = "typing-label";
      label.textContent = String(text || "正在思考你的问题").replace(/[.。…]+$/u, "");

      const dots = document.createElement("span");
      dots.className = "typing-dots";
      dots.setAttribute("aria-hidden", "true");
      for (let index = 0; index < 3; index += 1) {
        const dot = document.createElement("i");
        dots.appendChild(dot);
      }

      typingWrap.appendChild(label);
      typingWrap.appendChild(dots);
      bubble.appendChild(typingWrap);
    } else if (type === "bot" && !(options && options.typewriter)) {
      renderBotBubble(bubble, text);
    } else {
      bubble.textContent = options && options.typewriter ? "" : text;
    }
    if (type === "user" && !/[\r\n]/.test(String(text)) && String(text).trim().length <= 12) {
      bubble.classList.add("bubble--single-line");
    }

    const content = document.createElement("div");
    content.className = "msg-content";
    content.appendChild(bubble);
    if (type === "bot" && !(options && options.typing)) {
      const thinkingBlock = buildThinkingBlock(options && options.thinking, options && options.thinkingOpen);
      if (thinkingBlock) content.appendChild(thinkingBlock);
    }

    row.appendChild(avatar);
    row.appendChild(content);
    chatBody.appendChild(row);
    scrollToBottom();
    return row;
  }

  function appendInlineRuns(node, text) {
    const content = String(text || "");
    const pattern = /\*\*([^*\n]+)\*\*/g;
    let lastIndex = 0;
    let match = pattern.exec(content);

    while (match) {
      if (match.index > lastIndex) {
        node.appendChild(document.createTextNode(content.slice(lastIndex, match.index)));
      }
      const strong = document.createElement("strong");
      strong.className = "bubble-inline-strong";
      strong.textContent = match[1];
      node.appendChild(strong);
      lastIndex = match.index + match[0].length;
      match = pattern.exec(content);
    }

    if (lastIndex < content.length) {
      node.appendChild(document.createTextNode(content.slice(lastIndex)));
    }
  }

  function isDisplayTitleLine(line, index) {
    const trimmed = String(line || "").trim();
    if (!trimmed) return false;
    if (!/[:\uff1a]$/.test(trimmed)) return false;
    if (trimmed.length < 8 || trimmed.length > 38) return false;
    if (/[\u3002\uff01\uff1f]/.test(trimmed)) return false;
    return index === 0 || trimmed.length <= 24;
  }

  function parseNumberTitleLine(line) {
    const trimmed = String(line || "").trim();
    const match = trimmed.match(/^(\d+)[.)\u3001]\s*(.+)$/);
    if (!match) return null;

    const title = match[2].trim();
    if (title.length < 4 || title.length > 36) return null;
    if (/[\u3002\uff01\uff1f\uff1b\uff1a:]/.test(title)) return null;

    return {
      marker: match[1] + ".",
      text: title
    };
  }

  function parseListLine(line) {
    const trimmed = String(line || "").trim();
    if (!trimmed) return null;

    const bulletMatch = trimmed.match(/^[-*•]\s+(.+)$/);
    if (bulletMatch) return { marker: "", text: bulletMatch[1].trim() };

    const numberedMatch = trimmed.match(/^(\d+)[.)\u3001]\s*(.+)$/);
    if (numberedMatch) {
      return { marker: numberedMatch[1] + ".", text: numberedMatch[2].trim() };
    }

    return null;
  }

  function isSectionLabelLine(line) {
    const trimmed = String(line || "").trim().replace(/[\uff1a:]$/, "");
    if (!trimmed) return false;
    if (trimmed.length < 2 || trimmed.length > 12) return false;
    if (/^[-*•]/.test(trimmed)) return false;
    if (/^\d+[.)\u3001]/.test(trimmed)) return false;
    if (/[\u3002\uff01\uff1f]/.test(trimmed)) return false;
    return true;
  }

  function renderBotBubble(bubble, text) {
    const normalized = String(text || "").replace(/\r\n/g, "\n").trim();
    bubble.textContent = "";
    if (!normalized) return;

    const fragment = document.createDocumentFragment();
    let currentList = null;

    function closeList() {
      currentList = null;
    }

    function ensureList() {
      if (!currentList) {
        currentList = document.createElement("ul");
        currentList.className = "bubble-list";
        fragment.appendChild(currentList);
      }
      return currentList;
    }

    normalized.split("\n").forEach((rawLine, index) => {
      const line = rawLine.trim();
      if (!line) {
        closeList();
        return;
      }

      if (isDisplayTitleLine(line, index)) {
        closeList();
        const heading = document.createElement("p");
        heading.className = "bubble-display-title";
        heading.textContent = line;
        fragment.appendChild(heading);
        return;
      }

      const numberTitle = parseNumberTitleLine(line);
      if (numberTitle) {
        closeList();
        const heading = document.createElement("p");
        heading.className = "bubble-number-title";
        heading.dataset.marker = numberTitle.marker;
        appendInlineRuns(heading, numberTitle.text);
        fragment.appendChild(heading);
        return;
      }

      const listItem = parseListLine(line);
      if (listItem) {
        const list = ensureList();
        const item = document.createElement("li");
        item.className = "bubble-list-item";
        if (listItem.marker) {
          item.dataset.marker = listItem.marker;
          item.classList.add("is-numbered");
        }
        appendInlineRuns(item, listItem.text);
        list.appendChild(item);
        return;
      }

      closeList();

      const inlineTitleMatch = line.match(/^([^:\uff1a\n]{2,14})[:\uff1a]\s*(.+)$/);
      if (inlineTitleMatch && !/[\u3002\uff01\uff1f]/.test(inlineTitleMatch[1])) {
        const paragraph = document.createElement("p");
        paragraph.className = "bubble-paragraph";

        const title = document.createElement("strong");
        title.className = "bubble-inline-title";
        title.textContent = inlineTitleMatch[1].trim() + "\uff1a";
        paragraph.appendChild(title);
        paragraph.appendChild(document.createTextNode(" "));
        appendInlineRuns(paragraph, inlineTitleMatch[2]);
        fragment.appendChild(paragraph);
        return;
      }

      if (isSectionLabelLine(line)) {
        const heading = document.createElement("p");
        heading.className = "bubble-section-title";
        heading.textContent = line.replace(/[\uff1a:]$/, "");
        fragment.appendChild(heading);
        return;
      }

      const paragraph = document.createElement("p");
      paragraph.className = "bubble-paragraph";
      appendInlineRuns(paragraph, line);
      fragment.appendChild(paragraph);
    });

    bubble.appendChild(fragment);
  }

  function sleep(ms) {
    return new Promise((resolve) => window.setTimeout(resolve, ms));
  }

  function typewriterProfile(text) {
    const length = String(text || "").length;
    if (length <= 180) return { chunkSize: 1, delay: 18 };
    if (length <= 340) return { chunkSize: 2, delay: 13 };
    if (length <= 560) return { chunkSize: 3, delay: 10 };
    if (length <= 900) return { chunkSize: 4, delay: 8 };
    return { chunkSize: 5, delay: 6 };
  }

  function typewriterPause(chunk) {
    const tail = String(chunk || "");
    if (!tail) return 0;
    if (/[\n\r]$/.test(tail)) return 150;
    if (/[。！？!?：:；;]$/.test(tail)) return 95;
    if (/[，、,]$/.test(tail)) return 40;
    return 0;
  }

  const streamStateByRow = new WeakMap();

  function renderProgressiveBotBubble(bubble, text) {
    const value = String(text || "");
    if (!bubble) return;
    if (value.trim()) {
      renderBotBubble(bubble, value);
    } else {
      bubble.textContent = value;
    }
  }

  function streamRevealProfile(queueLength) {
    if (queueLength > 120) return { chunkSize: 5, delay: 6 };
    if (queueLength > 72) return { chunkSize: 4, delay: 8 };
    if (queueLength > 36) return { chunkSize: 3, delay: 11 };
    if (queueLength > 16) return { chunkSize: 2, delay: 15 };
    return { chunkSize: 1, delay: 20 };
  }

  function createStreamingBotRow(requestId) {
    const row = addMessage('', 'bot', { typewriter: true });
    const bubble = row.querySelector('.bubble');
    if (bubble) bubble.textContent = '';
    row.classList.add('is-streaming', 'is-typewriting');
    streamStateByRow.set(row, {
      requestId: requestId || 0,
      pending: '',
      displayed: '',
      fullText: '',
      draining: false
    });
    return row;
  }

  function ensureStreamDrain(row) {
    const stream = streamStateByRow.get(row);
    const bubble = row && row.querySelector ? row.querySelector('.bubble') : null;
    if (!stream || !bubble || stream.draining) return;

    stream.draining = true;
    (async function () {
      if (document.hidden) {
        stream.displayed += stream.pending;
        stream.pending = '';
        renderProgressiveBotBubble(bubble, stream.displayed);
        stream.draining = false;
        scrollToBottom();
        return;
      }

      while (stream.pending.length) {
        if (stream.requestId && stream.requestId !== state.activeRequestId) {
          stream.pending = '';
          break;
        }

        const profile = streamRevealProfile(stream.pending.length);
        const chunk = stream.pending.slice(0, profile.chunkSize);
        stream.pending = stream.pending.slice(profile.chunkSize);
        stream.displayed += chunk;
        renderProgressiveBotBubble(bubble, stream.displayed);

        if (stream.displayed.length % Math.max(12, profile.chunkSize * 12) === 0 || !stream.pending.length) {
          scrollToBottom();
        }

        await sleep(profile.delay + typewriterPause(chunk));
      }

      stream.draining = false;
      if (stream.pending.length) ensureStreamDrain(row);
    })();
  }

  function queueStreamingDelta(row, chunk) {
    const stream = streamStateByRow.get(row);
    if (!stream || !chunk) return;
    stream.pending += chunk;
    stream.fullText += chunk;
    ensureStreamDrain(row);
  }

  async function waitForStreamDrain(row) {
    while (true) {
      const stream = streamStateByRow.get(row);
      if (!stream || (!stream.pending.length && !stream.draining)) return;
      await sleep(16);
    }
  }

  async function finalizeStreamingBotRow(row, text) {
    if (!row) return String(text || '');
    const stream = streamStateByRow.get(row);
    const bubble = row.querySelector('.bubble');
    if (stream && typeof text === 'string' && text) {
      stream.fullText = text;
    }

    await waitForStreamDrain(row);

    const finalText = String((stream && stream.fullText) || text || '');
    if (bubble) {
      if (finalText) renderBotBubble(bubble, finalText);
      else bubble.textContent = '';
    }
    row.classList.remove('is-streaming', 'is-typewriting');
    streamStateByRow.delete(row);
    scrollToBottom();
    return finalText;
  }

  function dropStreamingBotRow(row) {
    if (!row) return;
    streamStateByRow.delete(row);
    row.remove();
  }

  async function typeBotMessage(row, text, requestId) {
    const bubble = row.querySelector(".bubble");
    const fullText = String(text || "");
    if (!bubble || !fullText) return;

    row.classList.add("is-typewriting");
    renderProgressiveBotBubble(bubble, "");

    if (document.hidden) {
      renderBotBubble(bubble, fullText);
      row.classList.remove("is-typewriting");
      scrollToBottom();
      return;
    }

    const profile = typewriterProfile(fullText);
    const chunkSize = profile.chunkSize;
    const animatedLimit = fullText.length;

    for (let index = 0; index < animatedLimit; index += chunkSize) {
      if (requestId && requestId !== state.activeRequestId) {
        renderBotBubble(bubble, fullText);
        break;
      }
      const chunk = fullText.slice(index, index + chunkSize);
      renderProgressiveBotBubble(bubble, fullText.slice(0, index + chunkSize));
      if (index % Math.max(12, chunkSize * 10) === 0 || index + chunkSize >= animatedLimit) scrollToBottom();
      await sleep(profile.delay + typewriterPause(chunk));
    }

    renderBotBubble(bubble, fullText);
    row.classList.remove("is-typewriting");
    scrollToBottom();
  }

  function storeAssistantMessage(text, options) {
    const storedThinking = normalizeThinkingForStorage(options && options.thinking);
    state.messages.push({ role: "assistant", content: text, thinking: storedThinking });
    saveChatSession();
    return storedThinking;
  }

  async function addBot(text, options) {
    const storedThinking = storeAssistantMessage(text, options);
    const row = addMessage(text, "bot", {
      typewriter: options && options.typewriter,
      thinking: storedThinking,
      thinkingOpen: !!(options && options.thinkingOpen)
    });
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
    state.isBusy = !!busy;
    if (submitButton) submitButton.disabled = busy;
  }

  function clearProactiveTimers() {
    proactiveTimers.forEach((timer) => window.clearTimeout(timer));
    proactiveTimers = [];
  }

  function removeProactiveTypingRow() {
    if (proactiveTypingRow && proactiveTypingRow.isConnected) proactiveTypingRow.remove();
    proactiveTypingRow = null;
  }

  function cancelProactiveFollowups() {
    proactivePlanToken += 1;
    clearProactiveTimers();
    removeProactiveTypingRow();
  }

  function hasDraftReply() {
    return !!String(input && input.value ? input.value : "").trim();
  }

  function latestUserSource() {
    return state.messages
      .filter(function (message) {
        return message && message.role === "user" && String(message.content || "").trim();
      })
      .slice(-6)
      .map(function (message) {
        return String(message.content || "").trim();
      })
      .join("\n")
      .slice(0, 3200);
  }

  function proactiveDelayAt(index) {
    return PROACTIVE_DELAYS[index] || PROACTIVE_DELAYS[PROACTIVE_DELAYS.length - 1];
  }

  function normalizeProactiveFollowups(items) {
    if (!Array.isArray(items)) return [];
    return items
      .map(function (item, index) {
        const text = String(item && item.text ? item.text : "").trim();
        if (!text) return null;
        const delayMs = Number(item && item.delayMs);
        const typingLabel = String(item && item.typingLabel ? item.typingLabel : "").trim();
        return {
          text,
          delayMs: Number.isFinite(delayMs) && delayMs > 0 ? delayMs : proactiveDelayAt(index),
          typingLabel: typingLabel || "我继续帮你把关键点补齐"
        };
      })
      .filter(Boolean)
      .slice(0, 3);
  }

  function proactiveCaseType(source) {
    const text = String(source || "");
    if (/(协议|協議|条款|條款|审阅|審閱|竞业|競業|保密|知识产权|知識產權|nda|non-?compete|intellectual property|\bip\b)/i.test(text)) return "contract";
    if (hasInheritanceContext(text)) return "inheritance";
    return "";
  }

  function filterProactiveFollowupsForCase(items, source) {
    const text = String(source || "");
    const isProperty = /房产|房產|房子|房屋|不动产|不動產|过户|過戶|转名|轉名|赠与|贈與|买卖|買賣/i.test(text);
    const isDebt = hasDebtCollectionPanelContext(text);
    const noMainland = hasNoMainlandConnectionSource(text);
    return (Array.isArray(items) ? items : [])
      .filter((item) => {
        const itemText = String(item && item.text ? item.text : item || "");
        if (!itemText) return false;
        if (isProperty && /协议|協議|审阅|審閱|竞业|競業|保密|知识产权|知識產權|岗位|崗位|待签|待簽|已经签|已經簽/i.test(itemText)) return false;
        if (isDebt && /继承|繼承|遗嘱|遺囑|房产|房產|过户|過戶|竞业|競業|知识产权|知識產權|岗位|崗位/i.test(itemText)) return false;
        if (noMainland && /继承|繼承|过户|過戶|房产|房產|内地|內地|大陆|大陸/i.test(itemText)) return false;
        return true;
      })
      .slice(0, 2);
  }

  function buildInheritanceProactiveFallbacks(source) {
    const items = [];
    const text = String(source || "");
    const typingLabel = "我继续帮你把继承路径补齐";

    if (!/提前安排|提前规划|提前規劃|生前安排|还在世|還在世|人在世|仍在世|老人还在世|老人還在世|立遗嘱|立遺囑|预先安排|預先安排|赠与|贈與|买卖|買賣|继承|繼承|遗产|遺產|去世|過世|身故|死亡|办继承|辦繼承|过户|過戶/i.test(text)) {
      items.push("我顺着你刚才这条先补一个定方向的事实：现在是已经发生继承、要办过户，还是还在提前安排将来继承？");
    }
    if (!/深圳|广州|上海|北京|珠海|佛山|东莞|中山|惠州|厦门|杭州|苏州|成都|重庆|武汉|南京|天津|长沙|宁波|青岛|无锡|福州|西安|郑州|南宁|昆明|合肥|南昌|海口|三亚|沈阳|大连|太原|济南|石家庄/i.test(text)) {
      items.push("我再往下补一个最关键的事实：房子具体在哪个内地城市或区？不同城市后面的办理口径会有差别。");
    }
    if (!/登记在|登記在|名下|权属|權屬|产权证|產權證|房产证|房產證|不动产权证|不動產權證|房本|业主|業主|权利人|權利人/i.test(text)) {
      items.push("再补一个权属点我就更好往下判断：房子现在登记在谁名下，是否已有房产证或不动产权证？");
    }
    if (!/没有遗嘱|沒有遺囑|无遗嘱|無遺囑|未立遗嘱|未立遺囑|没立遗嘱|沒立遺囑|有遗嘱|有遺囑|留有遗嘱|留有遺囑|立了遗嘱|立了遺囑|已有遗嘱|已有遺囑|公证遗嘱|公證遺囑|还没确认遗嘱|還沒確認遺囑|不确定有没有遗嘱|不確定有沒有遺囑|未确认遗嘱|未確認遺囑/i.test(text)) {
      items.push("还有一个会直接影响路径的点：目前是有遗嘱、没有遗嘱，还是暂时还没确认？");
    }
    if (!/失联|失聯|联系不上|聯繫不上|不方便来内地|不方便來內地|不能来内地|不能來內地|人在海外不方便到场|人在海外不方便到場|不同意|不配合|有争议|有爭議|纠纷|糾紛|意见不一致|意見不一致|全部同意|都同意|一致同意|意见一致|意見一致|没有争议|沒有爭議|家人配合|可以配合|可配合/i.test(text)) {
      items.push("如果你方便，再补一句其他继承人的配合情况：是否都同意，有没有失联、反对，或不方便到场的人。");
    }
    if (!/死亡证|死亡證|亲属关系|親屬關係|公证|公證|认证|認證|转递|轉遞|委托|委託|授权书|授權書|遗产承办|遺產承辦|probate/i.test(text)) {
      items.push("顺手再补一句材料情况也会很有帮助：死亡证明、亲属关系证明、香港委托或公证文件，现在手上大概有哪几类？");
    }

    return items.slice(0, 3).map(function (text, index) {
      return { text, delayMs: proactiveDelayAt(index), typingLabel };
    });
  }

  function buildContractProactiveFallbacks(source) {
    const items = [];
    const text = String(source || "");
    const typingLabel = "我继续帮你把审阅重点补齐";
    const hasStage = /已经签|已經簽|已签|已簽|签了|簽了|正式生效|已经生效|已經生效|要我签|要我簽|公司让我签|公司讓我簽|公司给我签|公司給我簽|公司给了我协议|公司給了我協議|发给我签|發給我簽|offer|入职前|入職前|谈判|談判|协商|協商|修改中|修订中|修訂中|还没签|還沒簽|未签|未簽|草稿/i.test(text);
    const hasPendingSign = /要我签|要我簽|公司让我签|公司讓我簽|公司给我签|公司給我簽|公司给了我协议|公司給了我協議|发给我签|發給我簽|offer|入职前|入職前/i.test(text);
    const hasSigned = /已经签|已經簽|已签|已簽|签了|簽了|正式生效|已经生效|已經生效/i.test(text);
    const hasRole = /研发|研發|技术|技術|工程师|工程師|程序员|程序員|开发|開發|算法|产品研发|產品研發|销售|銷售|客户|客戶|商务|商務|bd|市场|市場|渠道|招商|高管|管理层|管理層|主管|总监|總監|创始人|創始人|合伙人|合夥人|经理|經理/i.test(text);
    const hasFocus = /竞业|競業|non-?compete|保密|nda|confidential|知识产权|知識產權|\bip\b|intellectual property/i.test(text);
    const hasVersionInfo = /中文|英文|中英文|中文版本|英文版本|英文版|中文为准|中文版|english version/i.test(text);

    if (!hasStage) {
      items.push("我先把审阅场景卡准一点：这几份协议现在还在谈判、已经发给你待签，还是已经签了？");
    }
    if (!hasRole) {
      items.push("再补一个会直接影响竞业判断的背景：你的岗位更偏研发、客户销售，还是管理岗？");
    }
    if (!hasFocus) {
      items.push("如果你愿意，我也可以先盯你最担心的那块：是竞业范围、保密义务，还是知识产权归属？");
    }
    if (hasPendingSign) {
      items.push("如果现在是待签阶段，再补一句：公司有没有留修改空间，还是基本要求你尽快签？");
    } else if (hasSigned) {
      items.push("如果已经签了，再补一句：你现在更担心公司后面执行条款，还是想先判断自己有哪些现实风险？");
    }
    if (!hasVersionInfo) {
      items.push("如果协议有中英文两版，也可以顺手说一下哪一版写着优先适用或作为准据版本。");
    }

    return items.slice(0, 3).map(function (text, index) {
      return { text, delayMs: proactiveDelayAt(index), typingLabel };
    });
  }

  function selectProactiveFollowups(result) {
    const source = caseDetailSource() || latestUserSource();
    const apiItems = filterProactiveFollowupsForCase(normalizeProactiveFollowups(result && result.proactiveFollowups), source);
    const caseType = proactiveCaseType(source);
    if (!caseType) return apiItems;

    const localItems =
      caseType === "inheritance"
        ? buildInheritanceProactiveFallbacks(source)
        : buildContractProactiveFallbacks(source);

    if (localItems.length) return localItems;
    return apiItems;
  }

  function canRunProactiveFollowup(planToken) {
    return (
      planToken === proactivePlanToken &&
      !state.isBusy &&
      !hasDraftReply() &&
      !state.pendingAttachments.length &&
      !hasLoadingAttachments()
    );
  }

  async function fireProactiveFollowup(item, planToken) {
    if (!item || !canRunProactiveFollowup(planToken)) return;

    proactiveTypingRow = addMessage(item.typingLabel || "我继续帮你把关键点补齐", "bot", { typing: true });
    await sleep(1100);

    if (!canRunProactiveFollowup(planToken)) {
      removeProactiveTypingRow();
      return;
    }

    removeProactiveTypingRow();
    await addBot(item.text, { typewriter: true, requestId: state.activeRequestId });
  }

  function scheduleGptIdleCare() {
    const now = Date.now();
    if (now - lastGptIdleCareAt < GPT_IDLE_FOLLOWUP_COOLDOWN_MS) return;
    const planToken = ++proactivePlanToken;
    proactiveTimers = [
      window.setTimeout(async function () {
        if (!canRunProactiveFollowup(planToken)) return;
        lastGptIdleCareAt = Date.now();
        proactiveTypingRow = addMessage("我还在这里", "bot", { typing: true });
        await sleep(800);
        if (!canRunProactiveFollowup(planToken)) {
          removeProactiveTypingRow();
          return;
        }
        removeProactiveTypingRow();
        await addBot("还在的。如果你愿意，可以继续补充情况、材料或你最想解决的一步，我接着帮你整理。", {
          typewriter: true,
          requestId: state.activeRequestId
        });
      }, GPT_IDLE_FOLLOWUP_DELAY_MS)
    ];
  }

  function scheduleProactiveFollowups(result) {
    cancelProactiveFollowups();
    if (isMinimalAskFramework) {
      scheduleGptIdleCare();
      return;
    }
    const items = selectProactiveFollowups(result);
    if (!items.length) return;

    const planToken = ++proactivePlanToken;
    proactiveTimers = items.map(function (item) {
      return window.setTimeout(function () {
        fireProactiveFollowup(item, planToken);
      }, item.delayMs);
    });
  }

  function hasLoadingAttachments() {
    return state.pendingAttachments.some((file) => file && file.loading);
  }

  async function waitForPendingAttachments() {
    const pending = state.attachmentLoadPromise;
    if (!pending) return;
    try {
      await pending;
    } catch {
      // Attachment extraction already falls back to a readable note.
    }
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

  function inferFileKind(file) {
    const name = String((file && file.name) || "").toLowerCase();
    const type = String((file && file.type) || "").toLowerCase();
    if (type.includes("pdf") || name.endsWith(".pdf")) return "pdf";
    if (type.includes("wordprocessingml") || name.endsWith(".docx")) return "docx";
    if (type.startsWith("text/") || /\.(txt|md|csv|json|log)$/i.test(name)) return "text";
    if (type.startsWith("image/") || /\.(png|jpe?g|webp|gif|bmp)$/i.test(name)) return "image";
    return "unknown";
  }

  function extensionForMime(type) {
    const value = String(type || "").toLowerCase();
    if (value.includes("png")) return "png";
    if (value.includes("jpeg") || value.includes("jpg")) return "jpg";
    if (value.includes("webp")) return "webp";
    if (value.includes("gif")) return "gif";
    if (value.includes("pdf")) return "pdf";
    if (value.includes("wordprocessingml")) return "docx";
    if (value.startsWith("text/")) return "txt";
    return "bin";
  }

  function normalizeClipboardFile(file, index) {
    if (!file) return null;
    if (file.name) return file;
    const extension = extensionForMime(file.type);
    const name = "clipboard-image-" + (index + 1) + "." + extension;
    try {
      return new File([file], name, {
        type: file.type || "",
        lastModified: file.lastModified || Date.now()
      });
    } catch {
      return file;
    }
  }

  function clipboardAttachmentFiles(clipboardData) {
    if (!clipboardData) return [];
    const items = Array.from(clipboardData.items || []);
    const files = [];

    items.forEach((item, index) => {
      if (!item || item.kind !== "file" || typeof item.getAsFile !== "function") return;
      const file = normalizeClipboardFile(item.getAsFile(), index);
      if (file && inferFileKind(file) !== "unknown") files.push(file);
    });

    if (!files.length) {
      Array.from(clipboardData.files || []).forEach((file, index) => {
        const normalized = normalizeClipboardFile(file, index);
        if (normalized && inferFileKind(normalized) !== "unknown") files.push(normalized);
      });
    }

    return files.slice(0, MAX_ATTACHMENTS);
  }

  function insertTextAtCursor(element, text) {
    const value = String(text || "");
    if (!element || !value) return;
    const start = Number.isFinite(element.selectionStart) ? element.selectionStart : element.value.length;
    const end = Number.isFinite(element.selectionEnd) ? element.selectionEnd : start;
    element.value = element.value.slice(0, start) + value + element.value.slice(end);
    const nextPosition = start + value.length;
    element.setSelectionRange(nextPosition, nextPosition);
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

    if (isGptAskRoute) {
      const parts = ["\n\n[客户上传资料]"];
      usable.forEach((file, index) => {
        parts.push(`${index + 1}. ${file.name}（${fileKindLabel(file.kind, file.type)}，${formatBytes(file.size)}）`);
      });
      parts.push("[资料已随本轮请求发送给 GPT 直接读取。]");
      return parts.join("\n");
    }

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
      if (file.loading) pill.classList.add("is-reading");

      const label = document.createElement("span");
      label.textContent = file.name;
      const meta = document.createElement("small");
      const metaParts = [fileKindLabel(file.kind, file.type), formatBytes(file.size)];
      if (file.loading) metaParts.push("\u6b63\u5728\u8bfb\u53d6");
      meta.textContent = metaParts.join(" ");
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

  async function prepareGptAttachments(selected, placeholders, requestId) {
    const batch = [];
    for (let index = 0; index < selected.length; index += 1) {
      const file = selected[index];
      const placeholder = placeholders[index];
      if (!file || !placeholder || placeholder.error) {
        batch.push(placeholder ? { ...placeholder, loading: false } : null);
        continue;
      }
      try {
        batch.push({
          ...placeholder,
          data: await readFileData(file),
          text: "",
          note: "已准备随本轮请求发送给 GPT 直接读取。",
          loading: false,
          error: false
        });
      } catch {
        batch.push({
          ...placeholder,
          text: "",
          note: "附件读取失败，请重新上传或改用文字补充。",
          loading: false,
          error: true
        });
      }
    }

    if (requestId !== attachmentRequestSerial) return;
    state.pendingAttachments = batch.filter(Boolean).slice(0, MAX_ATTACHMENTS);
    renderAttachments();
  }

  async function extractFiles(files) {
    const selected = Array.from(files || []).slice(0, MAX_ATTACHMENTS);
    if (!selected.length) return;

    const requestId = ++attachmentRequestSerial;
    const batchId = "upload-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 8);
    const placeholders = selected.map((file, index) => ({
      uploadBatchId: batchId,
      uploadKey: batchId + "-" + index,
      name: String(file.name || "\u672a\u547d\u540d\u6587\u4ef6").slice(0, 120),
      type: String(file.type || ""),
      kind: inferFileKind(file),
      size: Number(file.size || 0),
      text: "",
      note: file.size > MAX_ATTACHMENT_BYTES
        ? "\u6587\u4ef6\u8d85\u8fc7 3MB\uff0c\u672a\u8bfb\u53d6\u5185\u5bb9\u3002"
        : "\u6b63\u5728\u8bfb\u53d6\u9644\u4ef6\u5185\u5bb9\u3002",
      loading: file.size <= MAX_ATTACHMENT_BYTES,
      error: file.size > MAX_ATTACHMENT_BYTES
    }));
    state.pendingAttachments = placeholders;
    renderAttachments();

    if (isGptAskRoute) {
      const loadPromise = prepareGptAttachments(selected, placeholders, requestId);
      state.attachmentLoadPromise = loadPromise;
      await loadPromise.finally(function () {
        if (state.attachmentLoadPromise === loadPromise) {
          state.attachmentLoadPromise = null;
        }
      });
      return;
    }

    const loadPromise = (async function () {
      const readableEntries = selected
        .map((file, index) => ({ file, placeholder: placeholders[index] }))
        .filter((entry) => entry.file.size <= MAX_ATTACHMENT_BYTES);
      const payloadFiles = [];

      for (const entry of readableEntries) {
        const file = entry.file;
        payloadFiles.push({
          name: file.name,
          type: file.type,
          size: file.size,
          data: await readFileData(file),
          uploadKey: entry.placeholder.uploadKey
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
            kind: inferFileKind(file),
            size: file.size,
            text: "",
            note: "\u9644\u4ef6\u5df2\u6536\u5230\uff0c\u6682\u65f6\u65e0\u6cd5\u8bfb\u53d6\u5185\u5bb9\uff1b\u8bf7\u8865\u5145\u5173\u952e\u6587\u5b57\u3002",
            error: true,
            uploadKey: file.uploadKey
          }));
        }
      }

      if (requestId !== attachmentRequestSerial) return;

      const visibleKeys = new Set(state.pendingAttachments.map((file) => file.uploadKey).filter(Boolean));
      const extractedByKey = new Map();
      payloadFiles.forEach((file, index) => {
        const item = extracted[index] || {};
        extractedByKey.set(file.uploadKey, {
          ...item,
          uploadBatchId: batchId,
          uploadKey: file.uploadKey,
          name: item.name || file.name,
          type: item.type || file.type,
          kind: item.kind || inferFileKind(file),
          size: Number(item.size || file.size || 0),
          text: String(item.text || ""),
          note: String(item.note || ""),
          loading: false,
          error: !!item.error
        });
      });

      state.pendingAttachments = placeholders
        .map((placeholder) => {
          if (!visibleKeys.has(placeholder.uploadKey)) return null;
          if (placeholder.error) return { ...placeholder, loading: false };
          return extractedByKey.get(placeholder.uploadKey) || { ...placeholder, loading: false };
        })
        .filter(Boolean)
        .slice(0, MAX_ATTACHMENTS);
      renderAttachments();
    })();

    state.attachmentLoadPromise = loadPromise;
    await loadPromise.finally(function () {
      if (state.attachmentLoadPromise === loadPromise) {
        state.attachmentLoadPromise = null;
      }
    });
  }

  function setChips(items, promptText) {
    quickReplies.innerHTML = "";
    if (promptText) {
      quickReplies.dataset.prompt = promptText;
    } else {
      delete quickReplies.dataset.prompt;
    }
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
    label.textContent = "想咨询什么类型？";
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
    sample.innerHTML = "<strong>也可以直接输入</strong><p>例如：我人在香港，想咨询内地房产、合同债务或婚姻家事问题。</p>";
    guide.appendChild(sample);

    chatBody.appendChild(guide);
    scrollToBottom();
  }

  function stageUi(stage) {
    const hasUserTurn = state.messages.some((message) => message.role === "user");
    if (!hasUserTurn) {
      return { chips: [], prompt: "", placeholder: "直接输入你的法律问题或案情" };
    }
    const preset = topicPresets[activeTopic];
    if (preset && stage === "done") {
      return { chips: [], prompt: "", placeholder: preset.placeholder };
    }
    if (stage === "region") {
      return { chips: regionChips, prompt: "", placeholder: "也可以直接输入你现在主要所在地区" };
    }
    if (stage === "mainland") {
      return { chips: mainlandChips, prompt: "", placeholder: "输入是否涉及中国内地" };
    }
    if (stage === "matter") {
      return { chips: matterChips, prompt: "", placeholder: "输入大致事务类型" };
    }
    if (stage === "summary") {
      return { chips: [], prompt: "", placeholder: summaryPlaceholder() };
    }
    return { chips: [], prompt: "", placeholder: "也可以继续补充你的情况" };
  }

  function summaryQuestion() {
    if (activeTopic === "hk-mainland-property-inheritance") {
      return "再补充一句：房子在哪个内地城市、现在是要办继承，还是提前安排。";
    }
    if (state.region && state.mainland === "yes") {
      return "再补充一句：对方、财产或主要证据在内地哪里，最想先解决什么。";
    }
    if (state.region) {
      return "再补充一句：事项是否涉及内地、对方或财产在哪里、最想先解决什么。";
    }
    return "最后用一句话补充核心情况：你在哪里、对方或财产在哪里、最想先解决什么。";
  }

  function summaryPlaceholder() {
    if (activeTopic === "hk-mainland-property-inheritance") {
      return "例如：我人在香港，深圳有房，想提前安排";
    }
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

  function createSessionId() {
    return "ask-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 8);
  }

  function createVisitorId() {
    return "visitor-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 10);
  }

  function getOrCreateVisitorId() {
    try {
      const existing = String(window.localStorage.getItem(VISITOR_BASE_KEY) || "").trim();
      if (existing) return existing;
      const next = createVisitorId();
      window.localStorage.setItem(VISITOR_BASE_KEY, next);
      return next;
    } catch {
      return createVisitorId();
    }
  }

  function casePanelItemKey(item) {
    const variants = {
      "廣": "广",
      "東": "东",
      "臺": "台",
      "灣": "湾",
      "國": "国",
      "內": "内",
      "產": "产",
      "證": "证",
      "權": "权",
      "繼": "继",
      "過": "过",
      "戶": "户",
      "與": "与",
      "爭": "争",
      "議": "议",
      "聯": "联",
      "係": "系",
      "親": "亲",
      "屬": "属",
      "無": "无",
      "發": "发",
      "辦": "办"
    };
    return String(item || "")
      .toLowerCase()
      .replace(/\s+/g, "")
      .replace(/[，,。；;、]/g, "")
      .replace(/[廣東臺灣國內產證權繼過戶與爭議聯係親屬無發辦]/g, (char) => variants[char] || char);
  }

  function normalizeCasePanel(panel) {
    if (!panel || typeof panel !== "object") return null;
    const goal = String(panel.goal || "").trim().slice(0, 28);
    const facts = Array.isArray(panel.facts) ? panel.facts : [];
    const missing = Array.isArray(panel.missing) ? panel.missing : [];
    const cleanList = (items, limit) => {
      const cleaned = [];
      const seen = new Set();
      items.forEach((raw) => {
        const item = String(raw || "").trim().slice(0, 42);
        const key = casePanelItemKey(item);
        if (!item || seen.has(key) || cleaned.length >= limit) return;
        seen.add(key);
        cleaned.push(item);
      });
      return cleaned;
    };
    const cleanFacts = reconcileCaseFacts(cleanList(facts, 8));
    const cleanMissing = cleanList(missing, 5);
    if (!goal && !cleanFacts.length && !cleanMissing.length) return null;
    const normalized = {
      goal: goal || "整理案情",
      facts: cleanFacts,
      missing: cleanMissing,
      matterType: String(panel.matterType || "").trim().slice(0, 48)
    };
    return normalized;
  }

  function reconcileCaseFacts(facts) {
    const hasConflict = facts.some((fact) => /有争议|有爭議|不配合|不同意|反对|反對|失联|失聯/.test(fact));
    const hasStartedInheritance = facts.some((fact) => /父亲|父親|母亲|母親|去世|过世|過世|过身|過身|死亡|身故|已故|继承办理|繼承辦理|法定继承|法定繼承|无遗嘱|無遺囑|有遗嘱|有遺囑/.test(fact));
    const hasNotStarted = !hasStartedInheritance && facts.some((fact) => /未发生继承|未發生繼承|提前安排/.test(fact));
    const regionFacts = facts.filter(isRegionFactTag);
    const preferredRegion = regionFacts.length ? regionFacts[regionFacts.length - 1] : "";
    return facts.filter((fact) => {
      if (hasConflict && /继承人同意|繼承人同意|全部同意|一致同意|没有争议|沒有爭議|无争议|無爭議/.test(fact)) return false;
      if (hasStartedInheritance && /未发生继承|未發生繼承|提前安排/.test(fact)) return false;
      if (hasNotStarted && /继承办理|繼承辦理/.test(fact)) return false;
      if (isRegionFactTag(fact) && fact !== preferredRegion) return false;
      return true;
    });
  }

  function normalizeSavedMessages(messages) {
    if (!Array.isArray(messages)) return [];
    return messages
      .map((message) => ({
        role: message && message.role === "assistant" ? "assistant" : "user",
        content: String(message && message.content ? message.content : "").trim(),
        displayContent: String(message && message.displayContent ? message.displayContent : "").trim(),
        thinking: normalizeThinkingForStorage(message && message.thinking)
      }))
      .filter((message) => message.content)
      .slice(-MAX_CHAT_HISTORY_MESSAGES);
  }

  function hasSavedUserTurn(payload) {
    return normalizeSavedMessages(payload && payload.state && payload.state.messages)
      .some((message) => message.role === "user");
  }

  function buildSessionPayload() {
    return {
      id: state.sessionId || createSessionId(),
      visitorId: state.visitorId || getOrCreateVisitorId(),
      topic: activeTopic,
      savedAt: Date.now(),
      state: {
        stage: state.stage || localStage(),
        region: state.region || "",
        mainland: state.mainland || "",
        matter: state.matter || "",
        summary: state.summary || "",
        casePanel: state.casePanel || null,
        workflow: state.workflow || null,
        intake: state.intake || null,
        conversion: state.conversion || null,
        lead: state.lead || null,
        messages: state.messages.slice(-MAX_CHAT_HISTORY_MESSAGES)
      },
      inputDraft: String(input && input.value ? input.value : "").slice(0, 1000)
    };
  }

  function archiveDisplayTitle(payload) {
    const messages = normalizeSavedMessages(payload && payload.state && payload.state.messages);
    const firstUser = messages.find((message) => message.role === "user");
    const text = String((firstUser && (firstUser.displayContent || firstUser.content)) || "").replace(/\s+/g, " ").trim();
    if (text) return text.slice(0, 28);
    const goal = payload && payload.state && payload.state.casePanel && payload.state.casePanel.goal;
    return String(goal || "\u672a\u547d\u540d\u5bf9\u8bdd").slice(0, 28);
  }

  function archiveDisplaySubtitle(payload) {
    const messages = normalizeSavedMessages(payload && payload.state && payload.state.messages);
    const userCount = messages.filter((message) => message.role === "user").length;
    const savedAt = new Date(Number(payload && (payload.archivedAt || payload.savedAt)) || Date.now());
    const dateText = savedAt.toLocaleString("zh-CN", {
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit"
    });
    return `${dateText} \u00b7 ${userCount}\u8f6e\u54a8\u8be2`;
  }

  function readArchives() {
    try {
      const raw = window.localStorage.getItem(ARCHIVE_KEY) || window.localStorage.getItem(ARCHIVE_BASE_KEY);
      const parsed = parseJson(raw);
      return Array.isArray(parsed)
        ? parsed.filter((item) => storedPayloadCompatible(item) && hasSavedUserTurn(item))
        : [];
    } catch {
      return [];
    }
  }

  function writeArchives(items) {
    const cleaned = (items || []).filter((item) => storedPayloadCompatible(item) && hasSavedUserTurn(item));
    if (!cleaned.length) {
      try {
        window.localStorage.setItem(ARCHIVE_KEY, "[]");
        window.localStorage.setItem(ARCHIVE_BASE_KEY, "[]");
        return true;
      } catch {
        return false;
      }
    }
    let next = cleaned;
    while (next.length) {
      const raw = JSON.stringify(next);
      try {
        window.localStorage.setItem(ARCHIVE_KEY, raw);
        try {
          window.localStorage.setItem(ARCHIVE_BASE_KEY, raw);
        } catch {
          // The topic-specific key is enough; the base key is only a compatibility mirror.
        }
        return true;
      } catch {
        try {
          window.localStorage.removeItem(ARCHIVE_BASE_KEY);
        } catch {
          // ignore storage cleanup failures
        }
        next = next.slice(0, -1);
      }
    }
    return false;
  }

  function archiveCurrentSession(options) {
    const payload = buildSessionPayload();
    if (!hasSavedUserTurn(payload)) return false;

    const archives = readArchives();
    const existing = archives.find((item) => item && item.id === payload.id);
    const markJust = !!(options && options.markJust);
    const entry = {
      ...payload,
      id: payload.id || state.sessionId || createSessionId(),
      archivedAt: Date.now(),
      title: archiveDisplayTitle(payload),
      subtitle: archiveDisplaySubtitle(payload),
      justArchivedAt: markJust ? Date.now() : Number(existing && existing.justArchivedAt) || 0
    };
    const nextArchives = archives
      .filter((item) => item.id !== entry.id)
      .map((item) => (markJust ? { ...item, justArchivedAt: 0 } : item));
    writeArchives([entry].concat(nextArchives));
    renderHistoryList();
    return true;
  }

  function setHistoryOpen(open) {
    if (!historyPopover || !historyChatButton) return;
    historyPopover.hidden = !open;
    historyChatButton.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) renderHistoryList();
  }

  function renderHistoryList() {
    if (!historyList) return;
    const archives = readArchives();
    const currentPayload = buildSessionPayload();
    const currentId = String(state.sessionId || "");
    const currentEntry = hasSavedUserTurn(currentPayload)
      ? {
          ...currentPayload,
          id: currentId || currentPayload.id || createSessionId(),
          title: archiveDisplayTitle(currentPayload),
          subtitle: archiveDisplaySubtitle(currentPayload),
          isCurrentSession: true
        }
      : null;
    const displayArchives = currentEntry
      ? [currentEntry].concat(archives.filter((item) => String(item.id || "") !== String(currentEntry.id || "")))
      : archives;
    historyList.innerHTML = "";
    if (!displayArchives.length) {
      const empty = document.createElement("div");
      empty.className = "history-empty";
      const emptyTitle = document.createElement("strong");
      emptyTitle.textContent = "\u6682\u65e0\u5386\u53f2\u5bf9\u8bdd";
      const emptyCopy = document.createElement("span");
      emptyCopy.textContent = "\u5f00\u59cb\u54a8\u8be2\u540e\uff0c\u8fd9\u91cc\u4f1a\u4fdd\u7559\u53ef\u5207\u6362\u7684\u5bf9\u8bdd\u3002";
      empty.appendChild(emptyTitle);
      empty.appendChild(emptyCopy);
      historyList.appendChild(empty);
      return;
    }

    displayArchives.forEach((item) => {
      const isCurrent = String(item.id || "") === currentId;
      const isJust = !isCurrent && Number(item.justArchivedAt || 0) > 0;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "history-item";
      if (isCurrent) {
        button.classList.add("is-current");
        button.setAttribute("aria-current", "true");
      }
      if (isJust) button.classList.add("is-just");

      const top = document.createElement("span");
      top.className = "history-item-top";

      const statusIcon = document.createElement("span");
      statusIcon.className = "history-status-icon";
      statusIcon.setAttribute("aria-hidden", "true");

      const title = document.createElement("strong");
      title.textContent = item.title || archiveDisplayTitle(item);

      const badge = document.createElement("span");
      badge.className = "history-badge";
      if (isCurrent) {
        badge.classList.add("history-badge--current");
        badge.textContent = "\u5f53\u524d";
      } else if (isJust) {
        badge.classList.add("history-badge--just");
        badge.textContent = "\u521a\u521a";
      }

      top.appendChild(statusIcon);
      top.appendChild(title);
      if (badge.textContent) top.appendChild(badge);

      const subtitle = document.createElement("span");
      subtitle.textContent = archiveDisplaySubtitle(item);

      button.appendChild(top);
      button.appendChild(subtitle);
      button.addEventListener("click", () => {
        if (String(item.id || "") !== currentId) {
          archiveCurrentSession({ markJust: true });
        }
        applyStoredPayload(item, false);
        saveChatSession();
        renderHistoryList();
        setHistoryOpen(false);
      });
      historyList.appendChild(button);
    });
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
    const payload = buildSessionPayload();

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

  function cleanLeadPhoneNumber(value) {
    return String(value || "").replace(/[^\d]/g, "");
  }

  function normalizedLeadPhoneNumber() {
    let digits = cleanLeadPhoneNumber(leadPhoneInput && leadPhoneInput.value);
    const dialCode = leadDialCode();
    const codeDigits = dialCode.replace(/[^\d]/g, "");
    if (digits.startsWith("00" + codeDigits)) digits = digits.slice(codeDigits.length + 2);
    else if (codeDigits && digits.startsWith(codeDigits) && digits.length > codeDigits.length) {
      const withoutCode = digits.slice(codeDigits.length);
      if (leadRegionRule().validate(withoutCode, dialCode)) digits = withoutCode;
    }
    return digits;
  }

  function normalizeDialCode(value) {
    const compact = String(value || "").trim().replace(/[^\d+]/g, "");
    if (!compact) return "";
    if (compact.startsWith("+")) {
      return `+${compact.slice(1).replace(/[^\d]/g, "")}`;
    }
    return `+${compact.replace(/[^\d]/g, "")}`;
  }

  function leadRegionRule() {
    return leadRegionRules[leadRegionSelect && leadRegionSelect.value] || leadRegionRules.hongkong;
  }

  function leadDialCode() {
    const region = leadRegionSelect && leadRegionSelect.value;
    if (region === "other") {
      return normalizeDialCode(leadCustomCodeInput && leadCustomCodeInput.value);
    }
    return leadRegionRule().code || "";
  }

  function latestAssistantMessageText() {
    for (let index = state.messages.length - 1; index >= 0; index -= 1) {
      const message = state.messages[index];
      if (message && message.role === "assistant" && String(message.content || "").trim()) {
        return String(message.content || "").trim();
      }
    }
    return "";
  }

  function userTurnCount() {
    return state.messages.filter((message) => message && message.role === "user" && String(message.content || "").trim()).length;
  }

  function assistantAskedForContact(text) {
    return /(?:留下|留个|留一下|留个联系方式|留聯繫方式|留联系方式|手机号|手機號|微信|wechat|WhatsApp|whatsapp|后续跟进|後續跟進|匿名记录|匿名記錄|联系你|聯繫你)/i.test(String(text || ""));
  }

  function hasLeadContact() {
    if (!state.lead) return false;
    if (state.lead.hasContact) return true;
    return Array.isArray(state.lead.contacts) && state.lead.contacts.length > 0;
  }

  function leadRegionValueFromState() {
    if (state.region === "hongkong") return "hongkong";
    if (state.region === "macau") return "macau";
    if (state.region === "singapore") return "singapore";
    if (state.region === "malaysia") return "malaysia";
    if (state.region === "us_chinese" || state.region === "us_general") return "us_ca";
    return "hongkong";
  }

  function ensureLeadRegionSelection() {
    if (!leadRegionSelect) return;
    const current = String(leadRegionSelect.value || "").trim();
    if (current) return;
    leadRegionSelect.value = leadRegionValueFromState();
  }

  function setLeadStatus(message, isError) {
    if (!leadStatus) return;
    leadStatus.textContent = String(message || "");
    leadStatus.classList.toggle("is-error", !!isError);
    leadStatus.classList.toggle("is-success", !!message && !isError);
  }

  function updateLeadRegionUi() {
    if (!leadRegionSelect || !leadPhoneHint) return;
    const region = String(leadRegionSelect.value || "");
    const rule = leadRegionRules[region] || leadRegionRules.hongkong;
    const isOther = region === "other";
    if (leadCustomCodeWrap) leadCustomCodeWrap.hidden = !isOther;
    if (leadPhoneHint) leadPhoneHint.textContent = rule.hint;
    if (leadPhoneInput) {
      leadPhoneInput.placeholder = region === "hongkong" || region === "macau"
        ? "8 位号码"
        : region === "mainland"
          ? "11 位手机号"
          : "联系电话";
    }
    if (!isOther && leadCustomCodeInput) leadCustomCodeInput.value = "";
  }

  function leadCaptureShouldShow() {
    if (!leadCaptureCard || !leadCaptureForm) return false;
    if (leadCaptureSubmitted || hasLeadContact()) return false;
    return true;
  }

  function renderLeadCapture() {
    if (!leadCaptureCard) return;
    const showSuccess = leadCaptureSubmitted;
    const showForm = !showSuccess && leadCaptureShouldShow();

    leadCaptureCard.hidden = !showForm && !showSuccess;
    if (leadCaptureFormWrap) leadCaptureFormWrap.hidden = !showForm;
    if (leadCaptureSuccess) leadCaptureSuccess.hidden = !showSuccess;

    if (showForm) {
      ensureLeadRegionSelection();
      updateLeadRegionUi();
    }
  }

  function leadSubjectText() {
    if (state.casePanel && state.casePanel.goal) return String(state.casePanel.goal).trim().slice(0, 80);
    if (state.workflow && state.workflow.label) return String(state.workflow.label).trim().slice(0, 80);
    return "Ask 法律咨询";
  }

  function leadFactsForSubmission() {
    const intakeFacts = state.intake && Array.isArray(state.intake.collectedFacts)
      ? state.intake.collectedFacts
          .map((fact) => {
            const label = String(fact && (fact.label || fact.field) ? (fact.label || fact.field) : "").trim();
            const value = String(fact && fact.value ? fact.value : "").trim();
            if (!label || !value) return "";
            return `${label}：${value}`;
          })
          .filter(Boolean)
      : [];
    if (intakeFacts.length) return intakeFacts.slice(0, 8);
    return Array.isArray(state.casePanel && state.casePanel.facts) ? state.casePanel.facts.slice(0, 8) : [];
  }

  function leadConversationDigest() {
    const parts = [];
    const subject = leadSubjectText();
    if (subject) parts.push(`主要诉求：${subject}`);

    const facts = leadFactsForSubmission();
    if (facts.length) parts.push(`关键信息：${facts.join("；")}`);

    const appointmentMatter = String(leadMatterInput && leadMatterInput.value ? leadMatterInput.value : "")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 300);
    if (appointmentMatter) parts.push(`预约说明：${appointmentMatter}`);

    const recentUserTurns = state.messages
      .filter((message) => message && message.role === "user" && String(message.displayContent || message.content || "").trim())
      .slice(-4)
      .map((message) => String(message.displayContent || message.content || "").replace(/\s+/g, " ").trim().slice(0, 120))
      .filter(Boolean);
    if (recentUserTurns.length) parts.push(`最近补充：${recentUserTurns.join(" / ")}`);

    return parts.join("\n").slice(0, 1500);
  }

  function buildLeadSheetPayload() {
    const data = new URLSearchParams();
    const dialCode = leadDialCode();
    const phone = normalizedLeadPhoneNumber();
    const altContact = String(leadAltContactInput && leadAltContactInput.value ? leadAltContactInput.value : "").trim();
    const normalizedLeadName = String(leadNameInput && leadNameInput.value ? leadNameInput.value : "").trim() || "Ask visitor";
    const subject = leadSubjectText();
    const digest = leadConversationDigest();
    const source = sourceParam || "ask-lead-form";
    const topic = activeTopic || "ask-general";
    data.append("submitted_at", new Date().toISOString());
    data.append("site", "ask");
    data.append("language", document.documentElement.lang || "zh-CN");
    data.append("page_title", document.title);
    data.append("user_agent", navigator.userAgent || "");
    data.append("enews", "AddFeedback");
    data.append("bid", "2");
    data.append("page_url", window.location.href);
    data.append("name", normalizedLeadName);
    data.append("area_code", dialCode);
    data.append("phone", phone);
    data.append("wechat", altContact);
    data.append("inquiry_type", subject);
    data.append("message", digest);
    data.append("quhao", dialCode);
    data.append("mycall", phone);
    data.append("weixin", altContact);
    data.append("zxsx", subject);
    data.append("khly", digest);
    data.append("source", source);
    data.append("topic", topic);
    data.append("consent", leadConsentInput && leadConsentInput.checked ? "yes" : "no");
    return data;
  }

  function buildLeadSyncPayload() {
    const dialCode = leadDialCode();
    const phone = normalizedLeadPhoneNumber();
    const alt = String(leadAltContactInput && leadAltContactInput.value ? leadAltContactInput.value : "").trim();
    const name = String(leadNameInput && leadNameInput.value ? leadNameInput.value : "").trim();
    const contactPieces = [];
    if (name) contactPieces.push(`称呼：${name}`);
    if (dialCode || phone) contactPieces.push(`我的电话是 ${dialCode} ${phone}`.trim());
    if (alt) contactPieces.push(`其他联系方式：${alt}`);
    const contactMessage = contactPieces.join("，");

    return {
      ...buildChatPayload(false),
      message: contactMessage,
      latestMessage: contactMessage,
      summary: [state.summary, leadConversationDigest()].filter(Boolean).join("\n").slice(0, 2400),
      messages: state.messages.concat([{ role: "user", content: contactMessage }]).slice(-MAX_CHAT_HISTORY_MESSAGES),
      source: sourceParam || "ask-lead-form",
      pageUrl: window.location.href
    };
  }

  function buildLawyerBookingPayload() {
    const dialCode = leadDialCode();
    const phone = normalizedLeadPhoneNumber();
    const name = String(leadNameInput && leadNameInput.value ? leadNameInput.value : "").trim().slice(0, 40);
    const altContact = String(leadAltContactInput && leadAltContactInput.value ? leadAltContactInput.value : "").trim().slice(0, 120);
    const matter = String(leadMatterInput && leadMatterInput.value ? leadMatterInput.value : "").trim().slice(0, 300);
    return {
      name,
      region: String(leadRegionSelect && leadRegionSelect.value ? leadRegionSelect.value : "hongkong"),
      dialCode,
      phone,
      altContact,
      matter,
      consent: Boolean(leadConsentInput && leadConsentInput.checked),
      companyWebsite: String(leadWebsiteInput && leadWebsiteInput.value ? leadWebsiteInput.value : "").slice(0, 200),
      startedAt: Number(leadStartedAtInput && leadStartedAtInput.value ? leadStartedAtInput.value : 0),
      visitorId: state.visitorId,
      sessionId: state.sessionId,
      topic: activeTopic || "ask-general",
      originalTopic: activeTopic || "ask-general",
      source: sourceParam || "ask-lawyer-appointment",
      intent: intentParam || "lawyer-appointment",
      pageUrl: window.location.href,
      summary: leadConversationDigest(),
      messages: state.messages.slice(-40).map(function (message) {
        return {
          role: message.role,
          content: String(message.displayContent || message.content || "").slice(0, 1200)
        };
      })
    };
  }

  function leadSubmitEndpoint() {
    if (!window.SITE_CONFIG || typeof window.SITE_CONFIG.googleSheetsEndpoint !== "string") return "";
    return String(window.SITE_CONFIG.googleSheetsEndpoint || "").trim();
  }

  function isLeadCaptureTestContext() {
    const host = String(window.location.hostname || "").toLowerCase();
    if (host === "127.0.0.1" || host === "localhost") return true;
    const source = String(sourceParam || "").toLowerCase();
    return /verify-local|test|codex/.test(source);
  }

  async function submitLeadSheet() {
    if (isLeadCaptureTestContext()) return false;
    const target = leadSubmitEndpoint();
    if (!target) throw new Error("missing submit endpoint");
    const controller = new AbortController();
    const timer = window.setTimeout(function () {
      controller.abort();
    }, 4000);
    try {
      await fetch(target, {
        method: "POST",
        mode: "no-cors",
        headers: { "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8" },
        body: buildLeadSheetPayload().toString(),
        signal: controller.signal
      });
    } catch (error) {
      if (!error || error.name !== "AbortError") throw error;
    } finally {
      window.clearTimeout(timer);
    }
    return true;
  }

  async function syncLeadCaptureToBackend(timeoutOverrideMs) {
    if (isLeadCaptureTestContext()) return null;
    const payload = buildLeadSyncPayload();
    const candidates = preferredEndpointOrder(apiEndpointCandidates());
    let lastError = null;

    for (let index = 0; index < candidates.length; index += 1) {
      const endpoint = candidates[index];
      try {
        const timeoutMs = Number.isFinite(Number(timeoutOverrideMs))
          ? Math.max(2500, Math.min(Number(timeoutOverrideMs), endpointTimeoutMs(endpoint, index)))
          : endpointTimeoutMs(endpoint, index);
        const result = await fetchChatJson(endpoint, payload, timeoutMs);
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

    throw lastError || new Error("lead sync failed");
  }

  async function submitLawyerBooking() {
    if (isLeadCaptureTestContext()) {
      return { ok: true, lead: { hasContact: true, status: "conversion_ready" } };
    }

    const candidates = leadEndpointCandidates();
    let lastError = null;
    for (let index = 0; index < candidates.length; index += 1) {
      try {
        return await fetchChatJson(candidates[index], buildLawyerBookingPayload(), index === 0 ? 12000 : 10000);
      } catch (error) {
        lastError = error;
      }
    }

    // Keep appointments working while an older API deployment is still serving traffic.
    // The existing contact path persists the lead and sends the same notification email.
    try {
      const fallbackResult = await syncLeadCaptureToBackend(15000);
      if (fallbackResult && fallbackResult.lead && fallbackResult.lead.hasContact) {
        return { ok: true, lead: fallbackResult.lead };
      }
    } catch (error) {
      lastError = error;
    }

    throw lastError || new Error("booking submit failed");
  }

  function validateLeadCaptureForm() {
    const region = String(leadRegionSelect && leadRegionSelect.value ? leadRegionSelect.value : "hongkong");
    const rule = leadRegionRules[region] || leadRegionRules.hongkong;
    const phone = normalizedLeadPhoneNumber();
    const customCode = normalizeDialCode(leadCustomCodeInput && leadCustomCodeInput.value);

    if (!phone) {
      return { ok: false, message: "请填写联系电话", focus: leadPhoneInput };
    }

    if (!rule.validate(phone, customCode)) {
      if (region === "other" && !/^\+\d{1,4}$/.test(customCode || "")) {
        return { ok: false, message: "其他地区请先填写国际区号", focus: leadCustomCodeInput || leadPhoneInput };
      }
      return { ok: false, message: rule.alert, focus: leadPhoneInput };
    }

    if (!leadConsentInput || !leadConsentInput.checked) {
      return { ok: false, message: "请先勾选同意联系", focus: leadConsentInput };
    }

    return { ok: true };
  }

  async function handleLeadCaptureSubmit(event) {
    event.preventDefault();
    if (state.isBusy || !leadCaptureForm) return;

    const validation = validateLeadCaptureForm();
    if (!validation.ok) {
      setLeadStatus(validation.message, true);
      if (validation.focus && typeof validation.focus.focus === "function") validation.focus.focus();
      return;
    }

    const originalText = leadSubmitButton ? leadSubmitButton.textContent : "";
    if (leadSubmitButton) {
      leadSubmitButton.disabled = true;
      leadSubmitButton.textContent = "提交中...";
    }
    setLeadStatus("", false);

    try {
      const backendResult = await submitLawyerBooking();
      if (!backendResult || backendResult.ok !== true) throw new Error("lead submit failed");

      state.lead = backendResult && backendResult.lead
        ? backendResult.lead
        : {
            ...(state.lead || {}),
            hasContact: true
          };

      leadCaptureSubmitted = true;
      if (leadCaptureForm) leadCaptureForm.reset();
      if (leadStartedAtInput) leadStartedAtInput.value = String(Date.now());
      updateLeadRegionUi();
      saveChatSession();
      renderLeadCapture();
      setLeadStatus("预约已提交。", false);

      if (!isLeadCaptureTestContext()) {
        submitLeadSheet()
          .catch(function () {
            // The booking API is authoritative; sheet mirroring is best effort.
          });
      }
    } catch {
      setLeadStatus("提交失败，请稍后再试。", true);
    } finally {
      if (leadSubmitButton) {
        leadSubmitButton.disabled = false;
        leadSubmitButton.textContent = originalText || "提交预约";
      }
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

  function storedPayloadCompatible(payload) {
    if (!payload || !payload.state) return false;
    if (payload.topic && activeTopic && payload.topic !== activeTopic) return false;
    return true;
  }

  function applyStoredPayload(payload, restoreDraft) {
    if (!storedPayloadCompatible(payload)) return false;
    cancelProactiveFollowups();
    leadCaptureSubmitted = false;
    setLeadStatus("", false);

    const savedMessages = normalizeSavedMessages(payload.state.messages);
    if (!savedMessages.length) return false;

    state.sessionId = String(payload.id || createSessionId());
    state.visitorId = String(payload.visitorId || state.visitorId || getOrCreateVisitorId());
    state.stage = String(payload.state.stage || "region");
    state.region = String(payload.state.region || "");
    state.mainland = String(payload.state.mainland || "");
    state.matter = String(payload.state.matter || "");
    state.summary = String(payload.state.summary || "");
    state.messages = savedMessages;
    state.casePanel = normalizeCasePanel(payload.state.casePanel);
    state.workflow = payload.state.workflow || null;
    state.intake = payload.state.intake || null;
    state.conversion = payload.state.conversion || null;
    state.lead = payload.state.lead || null;
    state.casePanelPending = false;

    chatBody.innerHTML = '<div class="day-pill">今天</div>';
    savedMessages.forEach((message) => {
      addMessage(message.displayContent || message.content, message.role === "assistant" ? "bot" : "user", {
        thinking: null
      });
    });

    const stage = localStage();
    state.stage = stage;
    const ui = stageUi(stage);
    setChips(ui.chips, ui.prompt);
    updatePlaceholder(ui.placeholder);
    updateAd(routeForCurrentState(), stage);
    updateCasePanel();
    renderLeadCapture();
    if (activeTopic && !state.messages.some((message) => message.role === "user")) {
      renderStartGuide();
    }

    if (restoreDraft && payload.inputDraft) {
      input.value = String(payload.inputDraft);
      resizeInput();
    } else {
      input.value = "";
      resizeInput();
    }

    return true;
  }

  function restoreChatSession() {
    const payload = readStoredPayload();
    return applyStoredPayload(payload, true);
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
    if (/美国|美國|\bU\.?S\.?\b|United States/i.test(text)) return "us_general";
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
    if (/欠款|欠钱|欠錢|拖欠|货款|貨款|尾款|账款|賬款|追款|催款|退款|拒绝退款|拒絕退款|债权|債權|债务|債務|收不回|不付款|不给钱|不給錢/i.test(text)) return "contract";
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

  function isRegionFactTag(fact) {
    return /^(?:香港居民|当前地区：香港|香港|澳门居民|美国客户|美国华人|加拿大客户|加拿大华人|英国客户|英国华人|澳大利亚客户|澳大利亚华人|日本客户|日本华人|新加坡居民|马来西亚客户)$/.test(String(fact || "").trim());
  }

  function isPersonalRegionContext(text, index) {
    const before = text.slice(Math.max(0, index - 24), index);
    const after = text.slice(index, index + 24);
    const windowText = before + after;
    if (/(?:父亲|父親|母亲|母親|父母|祖父母|爷爷|爺爺|奶奶|外公|外婆|哥哥|姐姐|弟弟|妹妹|配偶|老婆|老公|对方|對方|公司)[^。\n，,；;：:]{0,16}$/.test(before)) return false;
    if (/(?:过身|過身|去世|過世|身故|已故|死亡)/.test(after)) return false;
    return /(?:我|本人|自己|客户|客戶|当事人|當事人|人在|目前在|现在在|現在在|身在|住在|我是|本人是|係|是香港人|是香港居民|是港人)/.test(windowText);
  }

  function regionFact(source) {
    const latest = latestRegionFact(source);
    if (latest) return latest;
    if (/(?:我|本人|自己)[^。\n，,；;：:]{0,12}(?:香港居民|香港人|港人)|(?:香港居民|香港人|港人)[^。\n，,；;：:]{0,12}(?:我|本人|自己)/i.test(source)) return "香港居民";
    if (/(?:我在香港|人在香港|目前在香港|现在在香港|現在在香港|身在香港|住在香港)/i.test(source)) return "当前地区：香港";
    if (/(?:我|本人|自己)[^。\n，,；;：:]{0,12}(?:澳门|澳門)/i.test(source)) return "澳门居民";
    if (/(?:我|本人|自己|客户|客戶|当事人|當事人)[^。\n，,；;：:]{0,12}(?:美国|美國|纽约|紐約|加州|洛杉矶|洛杉磯)/i.test(source)) return /华人|華人/.test(source) ? "美国华人" : "美国客户";
    if (/(?:我|本人|自己|客户|客戶|当事人|當事人)[^。\n，,；;：:]{0,12}(?:加拿大|温哥华|溫哥華|多伦多|多倫多)/i.test(source)) return /华人|華人/.test(source) ? "加拿大华人" : "加拿大客户";
    if (/(?:我|本人|自己|客户|客戶|当事人|當事人)[^。\n，,；;：:]{0,12}(?:英国|英國|伦敦|倫敦)/i.test(source)) return /华人|華人/.test(source) ? "英国华人" : "英国客户";
    if (/(?:我|本人|自己|客户|客戶|当事人|當事人)[^。\n，,；;：:]{0,12}(?:澳大利亚|澳大利亞|澳洲|悉尼|雪梨|墨尔本|墨爾本)/i.test(source)) return /华人|華人/.test(source) ? "澳大利亚华人" : "澳大利亚客户";
    if (/(?:我|本人|自己|客户|客戶|当事人|當事人)[^。\n，,；;：:]{0,12}(?:日本|东京|東京|大阪)/i.test(source)) return /华人|華人/.test(source) ? "日本华人" : "日本客户";
    if (/(?:我|本人|自己|客户|客戶|当事人|當事人)[^。\n，,；;：:]{0,12}新加坡/i.test(source)) return "新加坡居民";
    if (/(?:我|本人|自己|客户|客戶|当事人|當事人)[^。\n，,；;：:]{0,12}(?:马来西亚|馬來西亞)/i.test(source)) return "马来西亚客户";
    return "";
  }

  function latestRegionMatch(source) {
    const text = String(source || "");
    const patterns = [
      { code: "hongkong", label: "\u9999\u6e2f\u5c45\u6c11", regex: /(?:\u9999\u6e2f|\u6e2f\u4eba|\u9999\u6e2f\u5c45\u6c11|Hong Kong|HK)/gi },
      { code: "macau", label: "\u6fb3\u95e8\u5c45\u6c11", regex: /(?:\u6fb3\u95e8|\u6fb3\u9580|Macau|Macao)/gi },
      { code: "singapore", label: "\u65b0\u52a0\u5761\u5c45\u6c11", regex: /(?:\u65b0\u52a0\u5761|Singapore)/gi },
      { code: "malaysia", label: "\u9a6c\u6765\u897f\u4e9a\u5ba2\u6237", regex: /(?:\u9a6c\u6765\u897f\u4e9a|\u99ac\u4f86\u897f\u4e9e|Malaysia)/gi },
      { code: "us_general", label: "\u7f8e\u56fd\u5ba2\u6237", regex: /(?:\u7f8e\u56fd|\u7f8e\u570b|United States|\bU\.?S\.?\b|USA)/gi },
      { code: "canada", label: "\u52a0\u62ff\u5927\u5ba2\u6237", regex: /(?:\u52a0\u62ff\u5927|Canada)/gi },
      { code: "australia", label: "\u6fb3\u6d32\u5ba2\u6237", regex: /(?:\u6fb3\u6d32|\u6fb3\u5927\u5229\u4e9a|\u6fb3\u5927\u5229\u4e9e|Australia)/gi },
      { code: "uk", label: "\u82f1\u56fd\u5ba2\u6237", regex: /(?:\u82f1\u56fd|\u82f1\u570b|United Kingdom|UK)/gi },
      { code: "japan", label: "\u65e5\u672c\u5ba2\u6237", regex: /(?:\u65e5\u672c|Japan)/gi }
    ];
    const matches = [];
    patterns.forEach((item) => {
      item.regex.lastIndex = 0;
      let matched = item.regex.exec(text);
      while (matched) {
        if (isPersonalRegionContext(text, matched.index)) {
          matches.push({ index: matched.index, code: item.code, label: item.label });
        }
        if (!matched[0]) item.regex.lastIndex += 1;
        matched = item.regex.exec(text);
      }
    });
    if (!matches.length) return null;
    matches.sort((a, b) => a.index - b.index);
    return matches[matches.length - 1];
  }

  function latestRegionFact(source) {
    const matched = latestRegionMatch(source);
    return matched ? matched.label : "";
  }

  function latestRegionCode(source) {
    const matched = latestRegionMatch(source);
    return matched ? matched.code : "";
  }

  function hasPropertySignal(source) {
    return /(?:\u623f\u4ea7|\u623f\u7522|\u623f\u5b50|\u623f\u5c4b|\u697c|\u6a13|\u4e0d\u52a8\u4ea7|\u4e0d\u52d5\u7522|\u7269\u4e1a|\u7269\u696d|property|title)/i.test(String(source || ""));
  }

  function hasMainlandContextSignal(source) {
    return /(?:\u4e2d\u56fd\u5185\u5730|\u4e2d\u570b\u5167\u5730|\u5185\u5730|\u5167\u5730|\u5927\u9646|\u5927\u9678|mainland)/i.test(String(source || "")) || !!mainlandCityFact(source);
  }

  function hasMainlandPropertySignal(source) {
    return hasPropertySignal(source) && hasMainlandContextSignal(source);
  }

  function hasExplicitInheritanceSignal(source) {
    return /(?:\u7ee7\u627f|\u7e7c\u627f|\u9057\u4ea7|\u907a\u7522|\u9057\u5631|\u907a\u56d1|\u53bb\u4e16|\u8fc7\u4e16|\u904e\u4e16|\u6b7b\u4ea1|\u8eab\u6545|\u88ab\u7ee7\u627f\u4eba|\u88ab\u7e7c\u627f\u4eba|inheritance|estate|probate)/i.test(String(source || ""));
  }

  function hasDebtCollectionPanelContext(source) {
    return /欠款|欠钱|欠錢|拖欠|货款|貨款|尾款|账款|賬款|追款|催款|付款记录|付款記錄|收不回|拒绝退款|拒絕退款|债权|債權|债务|債務|出货|出貨|送货|送貨|对账|對賬|不付款|不给钱|不給錢|未付款|退款|invoice|payment|debt|receivable/i.test(String(source || ""));
  }

  function hasNoMainlandConnectionSource(source) {
    return /(?:没有|沒有|无|無|暂无|暫無|不涉及).{0,12}(?:内地|內地|中国内地|中國內地|大陆|大陸).{0,18}(?:财产|財產|资产|資產|房产|房產|公司|存款|关联|關聯|连接|連接)|(?:内地|內地|中国内地|中國內地|大陆|大陸).{0,18}(?:财产|財產|资产|資產|房产|房產|公司|存款|关联|關聯|连接|連接).{0,12}(?:没有|沒有|无|無|暂无|暫無|不涉及)|纯香港|純香港|香港本地/i.test(String(source || ""));
  }

  function hasLivingPropertyOverride(source) {
    const text = String(source || "");
    if (deathStatus(text) === "yes") return false;
    const latest = latestCaseSignal(
      text,
      /继承|繼承|遗产|遺產|遗嘱|遺囑|去世|过世|過世|死亡|身故|inheritance|estate|probate/i,
      /(?:不是|唔係|并非|並非).{0,8}(?:继承|繼承)|(?:没有人|沒有人|没人|冇人).{0,8}(?:去世|过世|過世|死亡|身故)|(?:没有|沒有|还没|還沒).{0,8}(?:发生死亡|發生死亡|去世|过世|過世)|生前|现在过户|現在過戶|想过户|想過戶|给孩子|給孩子|转给孩子|轉給孩子|赠与|贈與|买卖|買賣/i
    );
    return latest === "no";
  }

  function mainlandCityFact(source) {
    return firstMatch(
      source,
      /深圳|广州|廣州|中山|上海|北京|佛山|珠海|东莞|東莞|苏州|蘇州|杭州|南京|天津|重庆|重慶|武汉|武漢|成都|西安|青岛|青島|厦门|廈門/i
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
      /去世|过世|過世|死亡|身故|离世|離世|过身|過身|走了|走咗/i,
      /(?:没人|沒人|没有人|沒有人|无人|無人|没有亲人|沒有親人|没有家人|沒有家人|没有谁|沒有誰|没有任何人|沒有任何人)[^，。；、,.\n]{0,8}(?:去世|过世|過世|死亡|身故|离世|離世|过身|過身|走了|走咗)|(?:没有去世|沒有去世|没去世|沒去世|还没去世|還沒去世|尚未去世|未去世|没有发生死亡|沒有發生死亡)|(?:都|全部|全都)[^，。；、,.\n]{0,8}(?:健在|在世|还在|還在)/i
    );
  }

  function deceasedFact(source) {
    const status = deathStatus(source);
    if (status === "no") return "未发生继承";
    if (status !== "yes") return "";
    const deathWords = "(?:去世|过世|過世|死亡|身故|离世|離世|过身|過身|走了|走咗)";
    const died = (relative) => new RegExp("(?:" + relative + ")[^，。；、,.\\n]{0,12}" + deathWords + "|" + deathWords + "[^，。；、,.\\n]{0,12}(?:" + relative + ")", "i").test(source);
    if (died("父亲|父親|爸爸|我爸|爹|家父")) return "父亲去世";
    if (died("母亲|母親|妈妈|媽媽|我妈|家母")) return "母亲去世";
    if (died("爷爷|爺爺|祖父")) return "祖父去世";
    if (died("奶奶|祖母")) return "祖母去世";
    if (died("丈夫|先生|老公|妻子|太太|老婆|配偶")) return "配偶去世";
    return "继承办理";
  }

  function hasPositiveTitleInfo(source) {
    const titleWords = "房产证|房產證|不动产权证|不動產權證|产权证|產權證|屋契|契纸|契紙";
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
    const titleWords = "房产证|房產證|不动产权证|不動產權證|产权证|產權證|屋契|契纸|契紙";
    return new RegExp(
      [
        "未办证",
        "未辦證",
        "(?:" + titleWords + ")" + shortText + "(?:失去|丢失|遺失|遗失|不见|不見|找不到|只得副本|只有副本|没有正本|沒有正本)",
        "(?:正本|副本|复印件|影印本)" + shortText + "(?:" + titleWords + ")",
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
    if (deathStatus(source) === "yes") return hasExplicitInheritanceSignal(source);
    if (hasLivingPropertyOverride(source)) return false;
    return hasExplicitInheritanceSignal(source);
  }

  function hasMatterSignal(source) {
    return /合同|合约|合約|合作|货款|貨款|公司|股权|股權|投资|投資|婚姻|离婚|離婚|继承|繼承|遗产|遺產|授权|授權|委托|委託|公证|公證|认证|認證|文件|身份|纠纷|糾紛|诉讼|訴訟|律师|律師|法院|房产|房產|不动产|不動產/i.test(source);
  }

  function matterFact(source) {
    if (hasDebtCollectionPanelContext(source)) return "债权追款";
    if (hasNoMainlandConnectionSource(source) && /婚姻|离婚|離婚|divorce/i.test(source)) return "香港本地婚姻";
    const matter = inferMatter(source) || state.matter;
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
    const region = latestRegionFact(source) || regionFact(source);
    const deceased = deceasedFact(source);
    const area = propertyAreaFact(source);
    const lostStatus = lostContactStatus(source);
    const conflictStatus = disputeStatus(source);
    const isInheritance = hasInheritanceContext(source);
    const matter = matterFact(source);
    const noMainland = hasNoMainlandConnectionSource(source);
    const debtContext = hasDebtCollectionPanelContext(source);

    if (isInheritance && state.region === "hongkong" && (!region || /香港/.test(region))) facts.push("香港居民");
    else if (region) facts.push(region);
    if (!noMainland && (/中国内地|中國內地|内地|內地|大陆|大陸|mainland/i.test(source) || (state.mainland === "yes" && (hasMainlandContextSignal(source) || city || debtContext)))) facts.push("涉及中国内地");
    if (debtContext) facts.push("债权追款");
    else if (hasMainlandPropertySignal(source)) facts.push("内地房产事项");
    else if (matter) facts.push(matter);
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
    if (hasMainlandPropertySignal(source) && /(?:登记|登記|名下|名字).{0,12}(?:我|本人|自己|一人)|(?:我|本人|自己|一人).{0,12}(?:名下|名字)/i.test(source)) facts.push("本人名下");
    if (hasMainlandPropertySignal(source) && /婚后|婚後|婚内|婚內/i.test(source)) facts.push("婚后取得");
    if (hasMainlandPropertySignal(source) && /(?:配偶|老婆|老公|太太|妻子|丈夫).{0,12}(?:不同意|不配合|反对|反對)|(?:不同意|不配合|反对|反對).{0,12}(?:配偶|老婆|老公|太太|妻子|丈夫)/i.test(source)) facts.push("配偶不同意");
    else if (hasMainlandPropertySignal(source) && /(?:配偶|老婆|老公|太太|妻子|丈夫).{0,12}(?:同意|配合)|(?:同意|配合).{0,12}(?:配偶|老婆|老公|太太|妻子|丈夫)/i.test(source)) facts.push("配偶配合");
    if (/屋契|契纸|契紙|正本|副本|复印件|影印本/i.test(source) && hasUnclearTitleInfo(source)) facts.push("权属文件待核");
    if (/掉空|空置|破落|荒废|荒廢|没有跟进|沒有跟進|长期未处理|長期未處理/i.test(source)) facts.push("长期未处理");
    if (isInheritance && /死亡证明|死亡證明|亲属关系|親屬關係|香港文件|公证|公證|转递|轉遞|委托书|委託書/i.test(source)) facts.push("提到文件材料");
    if (/委托|委託|代办|代辦|回不去|不到内地|不到內地/i.test(source)) facts.push("想委托办理");
    if (isInheritance && /卖房|賣房|卖掉|賣掉|出售|转卖|轉賣/i.test(source)) facts.push("继承后出售");
    return Array.from(new Set(facts)).slice(0, 8);
  }

  function caseGoalText(source) {
    const city = mainlandCityFact(source);
    const property = city ? city + "房产" : "内地房产";
    if (hasNoMainlandConnectionSource(source) && /婚姻|离婚|離婚|divorce/i.test(source)) return "香港本地婚姻咨询";
    if (hasDebtCollectionPanelContext(source)) return city ? city + "追款事项" : "整理债权追款事项";
    if (!hasInheritanceContext(source)) {
      if (hasMainlandPropertySignal(source)) return "整理内地房产事项";
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
    const hasTitle = hasUnclearTitleInfo(source) || hasPositiveTitleInfo(source) || /房产证|房產證|不动产权证|不動產權證|产权证|產權證|屋契|契纸|契紙/i.test(source);
    const hasDocuments = /死亡证明|死亡證明|亲属关系|親屬關係|香港文件|公证|公證|转递|轉遞/i.test(source);
    const hasTitleDocIssue = /屋契|契纸|契紙|正本|副本|复印件|影印本/i.test(source) && hasUnclearTitleInfo(source);
    const hasRegion = !!(latestRegionFact(source) || regionFact(source) || state.region);
    const noMainland = hasNoMainlandConnectionSource(source);

    if (noMainland && /婚姻|离婚|離婚|divorce/i.test(source)) {
      return ["如后续涉及内地财产、公司或文件，再补充这些连接点"];
    }

    if (hasDebtCollectionPanelContext(source)) {
      if (!hasCity) items.push("对方或资产线索所在的内地城市");
      if (!/公司全称|主体|营业执照|營業執照|统一社会信用代码|統一社會信用代碼/i.test(source)) items.push("对方主体名称或公司信息");
      if (!/合同|订单|訂單|发票|發票|对账|對賬|付款|转账|轉賬|送货|送貨|交付|聊天|催款/i.test(source)) items.push("合同、付款交付和催款证据");
      return Array.from(new Set(items)).slice(0, 4);
    }

    if (!isInheritance) {
      if (hasMainlandPropertySignal(source)) {
        if (!hasRegion) items.push("客户目前所在地区或身份");
        if (!hasCity) items.push("房产具体在哪个内地城市");
        items.push("现在最想办的是过户、继承、出售，还是家庭安排");
        if (!hasTitle) items.push("房产登记在谁名下，是否已有房产证/不动产权证");
        return Array.from(new Set(items)).slice(0, 5);
      }
      if (!hasRegion) items.push("客户目前所在地区或身份");
      if (!noMainland && !state.mainland && !hasMainlandContext) items.push("事项是否涉及中国内地");
      if (!state.matter || (state.matter === "other" && !hasMatterSignal(source))) items.push("大致属于哪类法律事务");
      if (!noMainland && (state.mainland === "yes" || hasMainlandContext)) items.push("对方、财产或证据在内地哪里");
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
    if (!hasDeceased) {
      items.push("现在是要办理继承，还是提前安排");
      if (!hasTitle) items.push("房产登记在谁名下，是否已有房产证/不动产权证");
      items.push("相关家人或可能继承人是否知情、有无争议");
      return Array.from(new Set(items)).slice(0, 5);
    }
    items.push("配偶、父母、子女和全部继承人范围");
    if (!hasWill) items.push("是否有遗嘱或遗产分配文件");
    if (!hasAgreement) {
      items.push(lostStatus === "no" ? "继承人是否全部同意，有无不配合" : "继承人是否全部同意，有无失联或不配合");
    }
    if (hasTitleDocIssue) {
      items.push("登记查册结果和证号");
      items.push("副本内容是否完整");
    } else if (!hasTitle) items.push("房产证/不动产权证是否已有");
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
    const fallbackText = [
      fallback.goal || "",
      ...(fallback.facts || []),
      ...(fallback.missing || [])
    ].join("\n");
    const fallbackIsNewerInheritance = /父亲|父親|母亲|母親|去世|过世|過世|过身|過身|死亡|身故|已故|继承|繼承|无遗嘱|無遺囑|有遗嘱|有遺囑/.test(fallbackText) && !/未发生继承|未發生繼承|提前安排/.test(fallbackText);
    const fallbackIsLivingProperty = /未发生继承|未發生繼承|生前|赠与|贈與|买卖|買賣|过户|過戶/.test(fallbackText) && !/去世|过世|過世|过身|過身|死亡|身故|已故/.test(fallbackText);
    const preferFallback = fallbackIsNewerInheritance || fallbackIsLivingProperty;
    return normalizeCasePanel({
      goal: preferFallback ? fallback.goal : (primary.goal || fallback.goal),
      facts: [...(fallback.facts || []), ...(primary.facts || [])],
      missing: preferFallback ? fallback.missing : ((primary.missing && primary.missing.length) ? primary.missing : fallback.missing)
    });
  }

  function resolvedCasePanel() {
    if (isMinimalAskFramework) return state.casePanel || null;
    const source = caseDetailSource() || userCaseSource();
    const localPanel = buildLocalCasePanel(source);
    return mergeCasePanels(state.casePanel, localPanel);
  }

  function pendingCasePanel(panel) {
    const base = panel || {};
    const facts = Array.isArray(base.facts) ? base.facts.slice() : [];
    const missing = Array.isArray(base.missing) ? base.missing.slice() : [];
    if (!facts.length) facts.push("AI正在核对");
    if (!missing.includes("根据你刚补充的内容更新案情要点")) {
      missing.unshift("根据你刚补充的内容更新案情要点");
    }
    return normalizeCasePanel({
      goal: base.goal || "正在整理",
      facts,
      missing,
      matterType: base.matterType || ""
    });
  }

  function updateCasePanel() {
    if (!caseEmpty || !caseContent || !caseGoal || !caseFacts) return;
    const hasUserTurn = state.messages.some((message) => message.role === "user");

    if (!hasUserTurn) {
      caseEmpty.hidden = false;
      caseContent.hidden = true;
      return;
    }

    const basePanel = resolvedCasePanel();
    const panel = state.casePanelPending ? pendingCasePanel(basePanel) : basePanel;

    if (!panel) {
      caseEmpty.hidden = false;
      caseContent.hidden = true;
      return;
    }

    caseEmpty.hidden = true;
    caseContent.hidden = false;

    const workflowLabel = state.workflow && state.workflow.label ? state.workflow.label : "";
    const statusLabels = {
      intake: "\u6536\u6848\u4e2d",
      plan_ready: "\u53ef\u51fa\u65b9\u6848",
      plan_given: "\u5df2\u7ed9\u521d\u6b65\u65b9\u6848",
      conversion_ready: "\u5df2\u5efa\u8bae\u5f8b\u5e08\u56e2\u961f\u8ddf\u8fdb",
      done: "\u5df2\u521d\u6b65\u5224\u65ad"
    };
    const statusText = statusLabels[state.stage] || statusLabels[panel.stage] || "\u6b63\u5728\u6574\u7406";
    caseGoal.textContent = workflowLabel ? `${workflowLabel} · ${statusText}` : (panel.goal || statusText);

    caseFacts.innerHTML = "";
    if (isMinimalAskFramework) {
      caseGoal.textContent = panel.goal || "整理法律问题";
    }
    const intakeFacts = state.intake && Array.isArray(state.intake.collectedFacts)
      ? state.intake.collectedFacts.map((fact) => `${fact.label || fact.field}\uff1a${fact.value || "\u5df2\u6536\u96c6"}`)
      : [];
    const facts = intakeFacts.length ? intakeFacts : (Array.isArray(panel.facts) ? panel.facts : []);
    (facts.length ? facts : ["已开始整理"]).forEach((fact) => {
      const tag = document.createElement("span");
      tag.className = "case-tag";
      tag.textContent = fact;
      caseFacts.appendChild(tag);
    });

  }

  function routeForCurrentState() {
    if (state.mainland === "no") return null;
    return localRoutes[state.region] || localRoutes.other;
  }

  function inheritanceFallbackReply() {
    if (activeTopic !== "hk-mainland-property-inheritance") return null;
    const source = userCaseSource();
    const city = mainlandCityFact(source);
    const hasTitle = hasPositiveTitleInfo(source) || hasUnclearTitleInfo(source) || /登记|登記|名下|房产证|房產證|不动产权证|不動產權證|产权证|產權證|屋契|契纸|契紙/i.test(source);
    const hasWill = /遗嘱|遺囑|遗产分配|遺產分配|遗赠|遺贈|认证|認證|承办|承辦|probate/i.test(source);
    const hasHeirInfo = /继承人|繼承人|兄弟|姐妹|姊妹|配偶|父母|子女|儿子|兒子|女儿|女兒|同意|反对|反對|争议|爭議|不配合|失联|失聯/i.test(source);
    const hasDocumentUse = /公证|公證|转递|轉遞|正本|副本|文件在手|材料在手|证明|證明/i.test(source);
    const items = [];

    if (!city) items.push("房子具体在哪个内地城市或区");
    if (!hasTitle) items.push("房子现在登记在谁名下，是否有房产证/不动产权证");
    if (hasWill) items.push("香港遗嘱认证文件是否明确写到这套房，正本是否在手");
    else items.push("是否有遗嘱、遗产分配或放弃继承文件");
    if (!hasHeirInfo) items.push("配偶、父母、子女或其他继承人是否都同意");
    if (!hasDocumentUse) items.push("香港死亡证明、亲属关系证明或委托文件是否已准备");

    const intro = city
      ? `我已记下：${city}房产。先不用你整理复杂资料，知道就答，不知道就写不知道：`
      : "先不用你整理复杂资料。这类问题先看几个具体点，知道就答，不知道就写不知道：";

    return {
      answer: [intro, ...items.slice(0, 4).map((item, index) => `${index + 1}. ${item}`)].join("\n"),
      chips: city ? ["登记在谁名下", "遗嘱文件在手", "其他继承人同意"] : ["广州房产", "深圳房产", "遗嘱文件在手"],
      inputPlaceholder: "知道多少说多少，不知道就写不知道"
    };
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
    const conversion = state.conversion || {};
    const resolvedRoute = route && route.url ? route : stage === "done" ? routeForCurrentState() : null;
    const hasUserTurn = state.messages.some((message) => message.role === "user");
    const shouldShow = hasUserTurn && conversion.show === true && !!(conversion.ctaUrl || (resolvedRoute && resolvedRoute.url));

    if (routeAd) {
      routeAd.hidden = !shouldShow;
      routeAd.setAttribute("aria-hidden", shouldShow ? "false" : "true");
    }
    if (chatMain) {
      chatMain.classList.toggle("has-ad", shouldShow);
    }

    if (!shouldShow) {
      return;
    }

    adTitle.textContent = conversion.ctaTitle || (resolvedRoute && resolvedRoute.label) || "\u9700\u8981\u5f8b\u5e08\u8fdb\u4e00\u6b65\u770b\uff1f";
    adCopy.textContent = conversion.ctaCopy || "\u4f60\u5df2\u7ecf\u8865\u5145\u5230\u53ef\u4ee5\u521d\u6b65\u5224\u65ad\u7684\u7a0b\u5ea6\uff0c\u53ef\u4ee5\u8ba9\u5f8b\u5e08\u56e2\u961f\u7ee7\u7eed\u770b\u3002";
    adLink.href = conversion.ctaUrl || routeUrl(resolvedRoute);
    adLink.textContent = conversion.ctaLabel || "\u8ba9\u5f8b\u5e08\u56e2\u961f\u7ee7\u7eed\u5224\u65ad";
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
    state.stage = "done";
    chatBody.innerHTML = '<div class="day-pill">今天</div>';
    return renderAssistantReply({
      stage: "done",
      answer: "你好，我是刘毅律师团队的 AI 法律助手。你可以直接输入法律问题或案情，我会先帮你做基础分析、整理关键事实和下一步思路。",
      chips: [],
      inputPlaceholder: "直接输入你的法律问题或案情",
      route: null,
      state: {
        region: state.region,
        mainland: state.mainland,
        matter: state.matter,
        summary: state.summary
      }
    });
  }

  function fallbackReply() {
    return {
      stage: "done",
      answer: "刚才这句没有完整接上。你可以再发一次核心事实，或继续补充案情，我会接着帮你整理。",
      chips: [],
      inputPlaceholder: "直接输入你的法律问题或案情",
      route: null
    };

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
      answer: "暂时没能连接 AI。你可以稍后重试，或继续补充事实，我会重新整理。",
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
      const latestRegion = latestRegionCode(text);
      if (latestRegion && latestRegion !== "other") state.region = latestRegion;
      if (inferredMainland && inferredMainland !== "unsure") state.mainland = inferredMainland;
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

  function buildChatPayload(streamMode) {
    return {
      sessionId: state.sessionId,
      visitorId: state.visitorId || getOrCreateVisitorId(),
      topic: activeTopic || "",
      region: state.region,
      mainland: state.mainland,
      matter: state.matter,
      summary: state.summary,
      language: "zh-CN",
      source: sourceParam,
      intent: intentParam,
      pageUrl: window.location.href,
      assistantVariant,
      modelProvider,
      messages: state.messages.slice(-MAX_CHAT_HISTORY_MESSAGES),
      attachments: isGptAskRoute ? state.currentTurnAttachments.slice(0, MAX_ATTACHMENTS) : [],
      stream: !!streamMode
    };
  }

  async function askBackend() {
    const payload = buildChatPayload(false);
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

  async function askBackendStream(handlers) {
    const payload = buildChatPayload(true);
    const candidates = preferredEndpointOrder(apiEndpointCandidates());
    let lastError = null;

    for (let index = 0; index < candidates.length; index += 1) {
      const endpoint = candidates[index];
      try {
        const result = await fetchChatStream(endpoint, payload, endpointTimeoutMs(endpoint, index), handlers);
        try {
          window.sessionStorage.setItem(LAST_GOOD_ENDPOINT_KEY, endpoint);
        } catch {
          // ignore storage failures
        }
        return result;
      } catch (error) {
        if (error && error.streamStarted) throw error;
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
    state.workflow = result && result.workflow ? result.workflow : state.workflow;
    state.intake = result && result.intake ? result.intake : state.intake;
    state.conversion = result && result.conversion ? result.conversion : null;
    state.lead = result && result.lead ? result.lead : state.lead;
    state.stage = (result && result.stage) || localStage();
  }

  function applyReplyUiState(result) {
    applyBackendState(result);
    if (isMinimalAskFramework) {
      state.workflow = null;
      state.intake = null;
      state.casePanel = normalizeCasePanel(result && result.casePanel) || state.casePanel;
    } else {
      state.casePanel = mergeCasePanels(
        normalizeCasePanel(result && result.casePanel),
        buildLocalCasePanel(caseDetailSource() || userCaseSource())
      );
    }
    state.casePanelPending = false;
    setChips(result.chips || [], result.chipsPrompt || "");
    updatePlaceholder(result.inputPlaceholder);
    updateAd(result.route || null, state.stage);
    updateCasePanel();
    renderLeadCapture();
  }

  async function renderAssistantReply(result, options) {
    applyReplyUiState(result);
    const row = await addBot(result.answer || fallbackReply().answer, {
      ...(options || {}),
      thinking: null,
      thinkingOpen: false
    });
    scheduleProactiveFollowups(result);
    return row;
  }

  async function renderStreamedAssistantReply(row, result, options) {
    const answer = await finalizeStreamingBotRow(row, result.answer || fallbackReply().answer);
    applyReplyUiState(result);
    storeAssistantMessage(answer, {
      thinking: options && options.thinking,
      thinkingOpen: !!(options && options.thinkingOpen)
    });
    scheduleProactiveFollowups(result);
    return row;
  }

  async function handleTurn(text, options) {
    if (state.isBusy) return;
    cancelProactiveFollowups();
    const cleaned = String(text || "").trim();
    if (!cleaned && !state.pendingAttachments.length) return;
    if (hasLoadingAttachments()) {
      setBusy(true);
      await waitForPendingAttachments();
    }
    const attachments = state.pendingAttachments.slice();
    if (!cleaned && !attachments.length) {
      setBusy(false);
      return;
    }
    const userText = cleaned || "\u6211\u4e0a\u4f20\u4e86\u8d44\u6599\uff0c\u8bf7\u5148\u5e2e\u6211\u770b\u91cd\u70b9\u3002";
    const fullText = userText + attachmentMessage(attachments);
    const displayText = userText + attachmentDisplay(attachments);
    state.currentTurnAttachments = isGptAskRoute
      ? attachments
          .filter((file) => file && !file.error && file.data)
          .map((file) => ({
            name: file.name,
            type: file.type,
            kind: file.kind,
            size: file.size,
            data: file.data
          }))
      : [];

    state.followLatest = true;
    removeStartGuide();
    setChips([], "");
    addUser(fullText, displayText);
    applyChoice(userText, options);
    input.value = "";
    resizeInput();
    state.pendingAttachments = [];
    renderAttachments();
    saveChatSession();

    const requestId = ++state.activeRequestId;
    setBusy(true);
    const typing = addMessage("\u6b63\u5728\u601d\u8003\u4f60\u7684\u95ee\u9898...", "bot", { typing: true });
    try {
      const result = await askBackendStream({});
      if (requestId !== state.activeRequestId) return;
      if (typing.isConnected) typing.remove();
      await renderAssistantReply(result, { typewriter: true, requestId });
    } catch (error) {
      if (requestId !== state.activeRequestId) return;
      if (typing.isConnected) typing.remove();
      if (!error || error.streamStarted !== true) {
        try {
          const result = await askBackend();
          if (requestId !== state.activeRequestId) return;
          await renderAssistantReply(result, { typewriter: true, requestId });
          return;
        } catch {
          // ignore fallback request errors
        }
      }
      await renderAssistantReply(fallbackReply(), { typewriter: true, requestId });
    } finally {
      state.currentTurnAttachments = [];
      if (requestId === state.activeRequestId) {
        setBusy(false);
      }
    }
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (state.isBusy) return;
    state.followLatest = true;
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
    if (state.isBusy) {
      event.preventDefault();
      return;
    }
    if (!String(input.value || "").trim() && !state.pendingAttachments.length) return;

    event.preventDefault();
    if (typeof form.requestSubmit === "function") {
      form.requestSubmit();
    } else {
      form.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
    }
  });

  input.addEventListener("input", function () {
    if (String(input.value || "").trim()) cancelProactiveFollowups();
    resizeInput();
    saveChatSession();
  });

  input.addEventListener("paste", function (event) {
    const files = clipboardAttachmentFiles(event.clipboardData);
    if (!files.length) return;

    cancelProactiveFollowups();
    const pastedText = event.clipboardData && typeof event.clipboardData.getData === "function"
      ? event.clipboardData.getData("text/plain")
      : "";
    event.preventDefault();
    insertTextAtCursor(input, pastedText);
    resizeInput();
    saveChatSession();
    extractFiles(files);
  });

  if (attachButton && attachmentInput) {
    attachButton.addEventListener("click", function () {
      cancelProactiveFollowups();
      if (typeof attachmentInput.showPicker === "function") {
        try {
          attachmentInput.showPicker();
          return;
        } catch {
          // Fall back to click() when showPicker is not available for this input.
        }
      }
      attachmentInput.click();
    });

    attachmentInput.addEventListener("change", async function () {
      cancelProactiveFollowups();
      await extractFiles(attachmentInput.files);
      attachmentInput.value = "";
    });
  }

  if (clearChatButton) {
    clearChatButton.addEventListener("click", function () {
      cancelProactiveFollowups();
      archiveCurrentSession();
      state.activeRequestId += 1;
      state.sessionId = createSessionId();
      state.stage = "region";
      state.region = "";
      state.mainland = "";
      state.matter = "";
      state.summary = "";
      state.messages = [];
      state.pendingAttachments = [];
      state.currentTurnAttachments = [];
      state.casePanel = null;
      state.casePanelPending = false;
      state.workflow = null;
      state.intake = null;
      state.conversion = null;
      state.lead = null;
      state.attachmentLoadPromise = null;
      state.followLatest = true;
      lastGptIdleCareAt = 0;
      leadCaptureSubmitted = false;
      input.value = "";
      resizeInput();
      clearStoredSession();
      setBusy(false);
      renderAttachments();
      renderInitialChat();
      renderHistoryList();
    });
  }

  if (historyChatButton) {
    historyChatButton.addEventListener("click", function (event) {
      event.stopPropagation();
      setHistoryOpen(historyPopover ? historyPopover.hidden : true);
    });
  }

  if (historyCloseButton) {
    historyCloseButton.addEventListener("click", function () {
      setHistoryOpen(false);
    });
  }

  document.addEventListener("click", function (event) {
    if (!historyPopover || historyPopover.hidden) return;
    if (historyPopover.contains(event.target) || (historyChatButton && historyChatButton.contains(event.target))) return;
    setHistoryOpen(false);
  });

  if (chatBody) {
    chatBody.addEventListener("scroll", function () {
      if (suppressScrollTracking) return;
      state.followLatest = isNearBottom();
    }, { passive: true });
  }

  if (leadRegionSelect) {
    leadRegionSelect.value = leadRegionValueFromState();
    leadRegionSelect.addEventListener("change", function () {
      updateLeadRegionUi();
      setLeadStatus("", false);
    });
  }

  if (leadCustomCodeInput) {
    leadCustomCodeInput.addEventListener("input", function () {
      if (leadRegionSelect && leadRegionSelect.value === "other") {
        setLeadStatus("", false);
      }
    });
  }

  if (leadPhoneInput) {
    leadPhoneInput.addEventListener("input", function () {
      setLeadStatus("", false);
    });
  }

  if (leadCaptureForm) {
    leadCaptureForm.addEventListener("submit", handleLeadCaptureSubmit);
  }

  if (leadStartedAtInput && !leadStartedAtInput.value) {
    leadStartedAtInput.value = String(Date.now());
  }

  updateLeadRegionUi();

  window.addEventListener("pagehide", saveChatSession);

  if (!restoreChatSession()) {
    renderInitialChat();
  }
  resizeInput();
  renderHistoryList();
  renderLeadCapture();
})();
