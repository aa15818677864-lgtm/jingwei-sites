(function () {
  const chatBody = document.getElementById("chatBody");
  const quickReplies = document.getElementById("quickReplies");
  const form = document.getElementById("chatForm");
  const input = document.getElementById("chatInput");
  const submitButton = form?.querySelector("button[type='submit']");

  const state = {
    stage: "region",
    region: "",
    mainland: "",
    matter: "",
    summary: "",
    messages: [],
    activeRequestId: 0,
    lastRouteUrl: ""
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
    us_chinese: {
      label: "美国华人中文入口",
      url: "/us/index_cn.html"
    },
    us_general: {
      label: "美国客户英文入口",
      url: "/us/index_us.html"
    },
    macau: {
      label: "澳门繁体入口",
      url: "/am/index_tc.html"
    },
    malaysia: {
      label: "马来西亚中文入口",
      url: "/ml/index_cn.html"
    },
    singapore: {
      label: "新加坡中文入口",
      url: "/xj/index_cn.html"
    },
    other: {
      label: "美国华人中文入口",
      url: "/us/index_cn.html"
    }
  };

  function apiEndpoint() {
    if (window.JINGWEI_AI_API) {
      return window.JINGWEI_AI_API;
    }

    if (window.SITE_CONFIG && window.SITE_CONFIG.aiEndpoint) {
      return window.SITE_CONFIG.aiEndpoint;
    }

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
    return addMessage(text, "bot");
  }

  function addUser(text) {
    state.messages.push({ role: "user", content: text });
    return addMessage(text, "user");
  }

  function setBusy(busy) {
    if (submitButton) {
      submitButton.disabled = busy;
    }
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

  function appendSummary(text) {
    const cleaned = String(text || "").trim();
    if (!cleaned) {
      return;
    }

    const parts = state.summary
      ? state.summary.split("\n").map(function (line) { return line.trim(); }).filter(Boolean)
      : [];

    if (!parts.includes(cleaned)) {
      parts.push(cleaned);
    }

    state.summary = parts.join("\n").slice(0, 2000);
  }

  function inferRegion(text) {
    if (/澳门|澳門/.test(text)) return "macau";
    if (/马来西亚|Malaysia/i.test(text)) return "malaysia";
    if (/新加坡|Singapore/i.test(text)) return "singapore";
    if (/美国华人|华人|中文客户/.test(text)) return "us_chinese";
    if (/美国|U\.?S\.?|United States/i.test(text)) return "us_general";
    return "other";
  }

  function inferMainland(text) {
    if (/不涉及中国内地|只涉及当地|当地法律|美国本地|澳门本地|香港本地/.test(text)) return "no";
    if (/不确定|暂时不清楚|还不清楚|需要先判断/.test(text)) return "unsure";
    if (/中国内地|内地|大陆|中国法律|境内/.test(text)) return "yes";
    return "unsure";
  }

  function inferMatter(text) {
    if (/合同|合作|买卖|货款|商业/.test(text)) return "contract";
    if (/公司|股权|经营|投资|合伙/.test(text)) return "company";
    if (/婚姻|离婚|继承|家事|抚养/.test(text)) return "family";
    if (/授权|公证|认证|文件|身份|委托/.test(text)) return "identity";
    return "other";
  }

  function routeForCurrentState() {
    if (state.mainland === "no") {
      return null;
    }
    return localRoutes[state.region] || localRoutes.other;
  }

  function routeUrl(route) {
    const source = new URLSearchParams(window.location.search).get("source") || "ask-chat";
    return route.url + "?source=" + encodeURIComponent(source);
  }

  function addCta(route) {
    if (!route || !route.url) {
      return;
    }

    const normalizedUrl = routeUrl(route);
    if (state.lastRouteUrl === normalizedUrl) {
      return;
    }

    const lastBubble = chatBody.querySelector(".msg-row.bot:last-child .bubble");
    if (!lastBubble) {
      return;
    }

    const link = document.createElement("a");
    link.className = "cta-link";
    link.href = normalizedUrl;
    link.textContent = "进入推荐表单";
    lastBubble.appendChild(document.createElement("br"));
    lastBubble.appendChild(link);
    state.lastRouteUrl = normalizedUrl;
    scrollToBottom();
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
        answer: "你好，我是刘毅律师团队的 AI 法律助理。我们先像聊天一样做一个初步判断。你现在主要在哪个地区？",
        chips: regionChips,
        inputPlaceholder: "也可以直接输入你现在主要所在地区",
        route: null
      };
    }

    if (stage === "mainland") {
      return {
        stage: "mainland",
        answer: "这个事项是否涉及中国内地？比如对方、财产、公司、合同履行地或主要证据在中国内地。",
        chips: mainlandChips,
        inputPlaceholder: "输入是否涉及中国内地",
        route: null
      };
    }

    if (stage === "matter") {
      return {
        stage: "matter",
        answer: "大致属于哪一类事务？你先说合同合作、公司股权、婚姻家事、授权文件，或者其他民商事问题都可以。",
        chips: matterChips,
        inputPlaceholder: "输入大致的事务类型",
        route: null
      };
    }

    if (stage === "summary") {
      return {
        stage: "summary",
        answer: "最后用一句话说一下你的具体情况，比如你现在在哪、对方或财产在哪里、最想先解决什么问题。",
        chips: [],
        inputPlaceholder: "例如：我人在美国，对方公司和合同履行地在中国内地",
        route: null
      };
    }

    const route = routeForCurrentState();
    if (!route) {
      return {
        stage: "done",
        answer: "从你目前说的情况看，这个入口暂时不像是在处理中国内地法律事务。\n\n如果后面确认涉及中国内地主体、财产、合同履行地或主要证据，可以再回到这里继续判断。\n\n以上仅作初步信息整理，不构成正式法律意见。",
        chips: [],
        inputPlaceholder: "也可以继续补充你的情况",
        route: null
      };
    }

    return {
      stage: "done",
      answer: "你这个情况可以先按对应中国内地法律事务方向整理。\n\n建议先提交所在地区、事项发生地、对方主体、现有材料和你最想解决的问题，律师团队再结合材料判断下一步。\n\n以上仅作初步信息整理，不构成正式法律意见。",
      chips: [],
      inputPlaceholder: "也可以继续补充你的情况",
      route: route
    };
  }

  function applyChoice(text, options) {
    const fromChip = options && options.fromChip;
    const value = options && options.value;

    if (!fromChip) {
      appendSummary(text);
    }

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
      return;
    }
  }

  async function askBackend() {
    const response = await fetch(apiEndpoint(), {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        region: state.region,
        mainland: state.mainland,
        matter: state.matter,
        summary: state.summary,
        language: "zh-CN",
        messages: state.messages
      })
    });

    if (!response.ok) {
      throw new Error("AI endpoint failed");
    }

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

    if (result.route) {
      addCta(result.route);
    } else if (state.stage !== "done") {
      state.lastRouteUrl = "";
    }
  }

  async function handleTurn(text, options) {
    const cleaned = String(text || "").trim();
    if (!cleaned) {
      return;
    }

    addUser(cleaned);
    applyChoice(cleaned, options);
    input.value = "";
    input.style.height = "auto";

    const requestId = ++state.activeRequestId;
    setBusy(true);
    const typing = addMessage("正在整理你的情况...", "bot", { typing: true });

    try {
      const result = await askBackend();
      if (requestId !== state.activeRequestId) {
        return;
      }
      typing.remove();
      renderAssistantReply(result);
    } catch (error) {
      if (requestId !== state.activeRequestId) {
        return;
      }
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

  input.addEventListener("input", function () {
    input.style.height = "auto";
    input.style.height = Math.min(input.scrollHeight, 118) + "px";
  });

  chatBody.innerHTML = '<div class="day-pill">今天</div>';
  renderAssistantReply({
    stage: "region",
    answer: "你好，我是刘毅律师团队的 AI 法律助理。我们先像聊天一样做一个初步判断。你现在主要在哪个地区？",
    chips: regionChips,
    inputPlaceholder: "也可以直接输入你现在主要所在地区",
    route: null,
    state: {
      region: "",
      mainland: "",
      matter: "",
      summary: ""
    }
  });
})();
