(function () {
  const chatBody = document.getElementById("chatBody");
  const quickReplies = document.getElementById("quickReplies");
  const form = document.getElementById("chatForm");
  const input = document.getElementById("chatInput");

  const state = {
    stage: "region",
    region: "",
    mainland: "",
    matter: "",
    summary: ""
  };

  const labels = {
    region: {
      us_chinese: "美国华人或中文客户",
      us_general: "美国客户或英文语境客户",
      macau: "澳门",
      malaysia: "马来西亚",
      singapore: "新加坡",
      other: "其他海外地区"
    },
    mainland: {
      yes: "是，涉及中国内地",
      unsure: "不确定，需要先判断",
      no: "否，只涉及当地法律"
    },
    matter: {
      contract: "合同或商业合作",
      company: "公司、股权或经营争议",
      family: "婚姻家事或继承",
      identity: "身份、授权或文件材料",
      other: "其他中国内地民商事问题"
    }
  };

  const localRoutes = {
    us_chinese: {
      label: "美国华人中国内地法律事务入口",
      url: "/us/index_cn.html"
    },
    us_general: {
      label: "美国客户中国内地法律事务英文入口",
      url: "/us/index_us.html"
    },
    macau: {
      label: "澳門繁體客戶入口",
      url: "/am/index_tc.html"
    },
    malaysia: {
      label: "马来西亚中文客户入口",
      url: "/ml/index_cn.html"
    },
    singapore: {
      label: "新加坡中文客户入口",
      url: "/xj/index_cn.html"
    },
    other: {
      label: "美国华人中国内地法律事务入口",
      url: "/us/index_cn.html"
    }
  };

  function apiEndpoint() {
    if (window.JINGWEI_AI_API) {
      return window.JINGWEI_AI_API;
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
    row.className = "msg-row " + type + (options?.typing ? " typing" : "");

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
    return addMessage(text, "bot");
  }

  function addUser(text) {
    return addMessage(text, "user");
  }

  function setChips(items) {
    quickReplies.innerHTML = "";
    items.forEach((item) => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "reply-chip";
      button.textContent = item.label;
      button.dataset.value = item.value;
      button.addEventListener("click", () => handleQuickReply(item.value, item.label));
      quickReplies.appendChild(button);
    });
  }

  function askRegion() {
    state.stage = "region";
    input.placeholder = "也可以直接输入你所在地区";
    setChips([
      { label: "美国华人", value: "us_chinese" },
      { label: "美国客户", value: "us_general" },
      { label: "澳门", value: "macau" },
      { label: "马来西亚", value: "malaysia" },
      { label: "新加坡", value: "singapore" },
      { label: "其他海外地区", value: "other" }
    ]);
  }

  function askMainland() {
    state.stage = "mainland";
    input.placeholder = "输入是否涉及中国内地";
    addBot("这个事项是否涉及中国内地？比如对方、财产、公司、合同履行地或主要证据在中国内地。");
    setChips([
      { label: "涉及中国内地", value: "yes" },
      { label: "不确定", value: "unsure" },
      { label: "只涉及当地法律", value: "no" }
    ]);
  }

  function askMatter() {
    state.stage = "matter";
    input.placeholder = "输入事务类型";
    addBot("大致属于哪一类事务？");
    setChips([
      { label: "合同/商业合作", value: "contract" },
      { label: "公司/股权", value: "company" },
      { label: "婚姻家事/继承", value: "family" },
      { label: "身份/授权/文件", value: "identity" },
      { label: "其他民商事问题", value: "other" }
    ]);
  }

  function askSummary() {
    state.stage = "summary";
    quickReplies.innerHTML = "";
    input.placeholder = "例如：我人在美国，合同和对方主体在中国内地";
    addBot("最后用一句话说一下你的具体情况，我再给你一个初步入口。");
    input.focus();
  }

  function routeUrl(route) {
    const source = new URLSearchParams(window.location.search).get("source") || "ask-chat";
    return route.url + "?source=" + encodeURIComponent(source);
  }

  function addCta(route) {
    const lastBubble = chatBody.querySelector(".msg-row.bot:last-child .bubble");
    if (!lastBubble || !route?.url) {
      return;
    }

    const link = document.createElement("a");
    link.className = "cta-link";
    link.href = routeUrl(route);
    link.textContent = "进入推荐表单";
    lastBubble.appendChild(document.createElement("br"));
    lastBubble.appendChild(link);
    scrollToBottom();
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
        language: "zh-CN"
      })
    });

    if (!response.ok) {
      throw new Error("AI endpoint failed");
    }

    return response.json();
  }

  function fallbackResult() {
    if (state.mainland === "no") {
      return {
        answer: "这个入口主要处理中国内地法律事务。你现在选择的是只涉及当地法律，建议先确认是否存在中国内地主体、财产、合同履行地或主要证据。以上仅作初步信息整理，不构成正式法律意见。",
        route: null
      };
    }

    const route = localRoutes[state.region] || localRoutes.other;
    const matter = labels.matter[state.matter] || "中国内地民商事问题";
    return {
      answer: "你这个情况可以先按“" + matter + "”方向整理。建议先提交基本情况，由律师团队结合所在地、事务发生地、对方主体和已有材料进一步判断。以上仅作初步信息整理，不构成正式法律意见。",
      route
    };
  }

  async function finishTriage() {
    state.stage = "done";
    quickReplies.innerHTML = "";
    input.placeholder = "可以继续补充情况";

    const typing = addMessage("正在整理你的情况...", "bot", { typing: true });

    try {
      const result = await askBackend();
      typing.remove();
      addBot(result.answer || fallbackResult().answer);
      if (result.route) {
        addCta(result.route);
      }
    } catch (error) {
      const result = fallbackResult();
      typing.remove();
      addBot(result.answer);
      if (result.route) {
        addCta(result.route);
      }
    }
  }

  function inferRegion(text) {
    if (text.includes("澳门") || text.includes("澳門")) return "macau";
    if (text.includes("马来") || text.includes("馬來")) return "malaysia";
    if (text.includes("新加坡")) return "singapore";
    if (text.includes("美国") || text.includes("美國")) return "us_chinese";
    return "other";
  }

  function inferMainland(text) {
    if (text.includes("不涉及") || text.includes("当地") || text.includes("當地")) return "no";
    if (text.includes("不确定") || text.includes("不確定")) return "unsure";
    return "yes";
  }

  function inferMatter(text) {
    if (text.includes("合同") || text.includes("商业") || text.includes("商業")) return "contract";
    if (text.includes("公司") || text.includes("股权") || text.includes("股權")) return "company";
    if (text.includes("婚") || text.includes("继承") || text.includes("繼承")) return "family";
    if (text.includes("授权") || text.includes("授權") || text.includes("身份") || text.includes("文件")) return "identity";
    return "other";
  }

  function handleQuickReply(value, label) {
    addUser(label);

    if (state.stage === "region") {
      state.region = value;
      askMainland();
      return;
    }

    if (state.stage === "mainland") {
      state.mainland = value;
      if (value === "no") {
        state.matter = "other";
        state.summary = "事项只涉及当地法律";
        finishTriage();
        return;
      }
      askMatter();
      return;
    }

    if (state.stage === "matter") {
      state.matter = value;
      askSummary();
    }
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = input.value.trim();
    if (!text) {
      return;
    }

    addUser(text);
    input.value = "";

    if (state.stage === "region") {
      state.region = inferRegion(text);
      state.summary = text;
      askMainland();
      return;
    }

    if (state.stage === "mainland") {
      state.mainland = inferMainland(text);
      if (state.mainland === "no") {
        state.matter = "other";
        state.summary = [state.summary, text].filter(Boolean).join("；");
        finishTriage();
        return;
      }
      askMatter();
      return;
    }

    if (state.stage === "matter") {
      state.matter = inferMatter(text);
      state.summary = [state.summary, text].filter(Boolean).join("；");
      askSummary();
      return;
    }

    if (state.stage === "summary" || state.stage === "done") {
      state.summary = [state.summary, text].filter(Boolean).join("；");
      finishTriage();
    }
  });

  input.addEventListener("input", () => {
    input.style.height = "auto";
    input.style.height = Math.min(input.scrollHeight, 118) + "px";
  });

  chatBody.innerHTML = '<div class="day-pill">今天</div>';
  addBot("你好，我是刘毅律师团队的 AI 法律助理。我们先用聊天方式做一个初步判断。你现在主要在哪个地区？");
  askRegion();
})();

