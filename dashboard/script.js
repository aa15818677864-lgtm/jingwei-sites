(function () {
  "use strict";

  const state = {
    range: "day",
    metrics: null,
    geo: null,
    liveLeads: null,
    relay: null
  };

  const byId = (id) => document.getElementById(id);
  const nodes = {
    consultationLabel: byId("consultationLabel"),
    consultationCount: byId("consultationCount"),
    consultationHint: byId("consultationHint"),
    publishedCount: byId("publishedCount"),
    publishedHint: byId("publishedHint"),
    indexedCount: byId("indexedCount"),
    indexedHint: byId("indexedHint"),
    topicReadyCount: byId("topicReadyCount"),
    topicReadyHint: byId("topicReadyHint"),
    articleSource: byId("articleSource"),
    leadSource: byId("leadSource"),
    indexSource: byId("indexSource"),
    lastUpdated: byId("lastUpdated"),
    geoCoverageBadge: byId("geoCoverageBadge"),
    geoCrawlerCount: byId("geoCrawlerCount"),
    geoCrawlerHint: byId("geoCrawlerHint"),
    geoCitationCount: byId("geoCitationCount"),
    geoReferralCount: byId("geoReferralCount"),
    geoBenchmarkCount: byId("geoBenchmarkCount"),
    geoBenchmarkHint: byId("geoBenchmarkHint"),
    geoPlatformRows: byId("geoPlatformRows"),
    geoSourceNote: byId("geoSourceNote"),
    personaRows: byId("personaRows"),
    topicRows: byId("topicRows"),
    topicMethod: byId("topicMethod"),
    candidateLimitBadge: byId("candidateLimitBadge"),
    recommendationRows: byId("recommendationRows"),
    recommendationSummary: byId("recommendationSummary"),
    feedbackRules: byId("feedbackRules"),
    feedbackSummary: byId("feedbackSummary"),
    learningLog: byId("learningLog"),
    consultationChart: byId("consultationChart"),
    consultationTrendHint: byId("consultationTrendHint"),
    articleChart: byId("articleChart"),
    articleTrendHint: byId("articleTrendHint"),
    gscClicks: byId("gscClicks"),
    gscImpressions: byId("gscImpressions"),
    gscCtr: byId("gscCtr"),
    gscPosition: byId("gscPosition"),
    queueRows: byId("queueRows"),
    queueSummary: byId("queueSummary"),
    leadChain: byId("leadChain"),
    leadBreakdown: byId("leadBreakdown"),
    policyList: byId("policyList"),
    articleRows: byId("articleRows"),
    articleAuditSummary: byId("articleAuditSummary")
  };

  const dayFormatter = new Intl.DateTimeFormat("zh-CN", { month: "2-digit", day: "2-digit" });
  const monthFormatter = new Intl.DateTimeFormat("zh-CN", { year: "2-digit", month: "2-digit" });
  const timeFormatter = new Intl.DateTimeFormat("zh-CN", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });

  const topicMeta = {
    "hk-inheritance": { label: "香港继承", note: "家属、文件与内地资产", color: "#a30d23" },
    singapore: { label: "新加坡", note: "双语文件与远程办理", color: "#19756f" },
    macau: { label: "澳门", note: "家庭资产与企业纠纷", color: "#9b6a08" },
    "united-states": { label: "美国", note: "跨时区委托与争议", color: "#1473e6" }
  };

  const depthLabels = {
    entry: "入门",
    intermediate: "进阶",
    advanced: "深入"
  };

  const statusLabels = {
    planned: "待写",
    "drafted-zh-Hant": "繁中初稿",
    "drafted-zh-Hans": "简中初稿",
    "model-written-en": "英文已写",
    "legal-reviewed": "法律复核完成",
    "images-ready": "配图完成",
    "build-ready": "待发布",
    published: "已发布"
  };

  function escapeHtml(value) {
    return String(value ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function isFiniteNumber(value) {
    return value !== null && value !== undefined && value !== "" && Number.isFinite(Number(value));
  }

  function formatCount(value) {
    return isFiniteNumber(value) ? Number(value).toLocaleString("zh-CN") : "--";
  }

  function formatTime(value) {
    if (!value) return "--";
    const date = new Date(value);
    return Number.isNaN(date.getTime()) ? String(value) : timeFormatter.format(date);
  }

  function sameOrigin(path) {
    return new URL(path, window.location.origin).href;
  }

  async function fetchJson(url) {
    if (!url) return null;
    try {
      const response = await fetch(url, { cache: "no-store" });
      if (!response.ok) return null;
      return await response.json();
    } catch (error) {
      return null;
    }
  }

  async function loadData() {
    [state.metrics, state.geo] = await Promise.all([
      fetchJson(sameOrigin("/dashboard/metrics.json")),
      fetchJson(sameOrigin("/dashboard/geo.json"))
    ]);

    const configured = window.SITE_CONFIG?.dashboardMetricsEndpoint || "";
    const relayEndpoint = window.SITE_CONFIG?.googleSheetsEndpoint
      ? `${window.SITE_CONFIG.googleSheetsEndpoint}?action=dashboard`
      : "";

    if (configured) {
      const live = await fetchJson(configured);
      if (live?.consultation) state.liveLeads = live;
    }

    if (!state.liveLeads && relayEndpoint) {
      const relay = await fetchJson(relayEndpoint);
      if (relay?.consultation) state.liveLeads = relay;
      if (relay?.service) state.relay = relay;
    }
  }

  function consultationData() {
    return state.liveLeads?.consultation || state.metrics?.consultation || null;
  }

  function sumKnown(rows, key) {
    const values = rows.map((row) => row?.[key]).filter(isFiniteNumber).map(Number);
    return values.length ? values.reduce((sum, value) => sum + value, 0) : null;
  }

  function renderGeo() {
    const geo = state.geo;
    if (!geo) {
      nodes.geoCoverageBadge.textContent = "数据未生成";
      nodes.geoCrawlerHint.textContent = "等待 GEO 技术检查";
      nodes.geoPlatformRows.innerHTML = '<div class="empty-state geo-empty">没有读取到 GEO 状态</div>';
      nodes.geoSourceNote.textContent = "引用与引流数据未接通。";
      return;
    }

    const platforms = Array.isArray(geo.platforms) ? geo.platforms : [];
    const eligible = geo.status?.eligiblePlatforms;
    const total = geo.status?.platformCount;
    const citations = sumKnown(platforms, "citationCount");
    const referrals = sumKnown(platforms, "referralSessions");
    nodes.geoCoverageBadge.textContent = isFiniteNumber(eligible) && isFiniteNumber(total)
      ? `${eligible}/${total} 搜索通道可用`
      : "状态未知";
    nodes.geoCrawlerCount.textContent = isFiniteNumber(eligible) && isFiniteNumber(total) ? `${eligible}/${total}` : "--";
    nodes.geoCrawlerHint.textContent = "搜索访问与训练访问分别控制";
    nodes.geoCitationCount.textContent = formatCount(citations);
    nodes.geoReferralCount.textContent = formatCount(referrals);
    nodes.geoBenchmarkCount.textContent = formatCount(geo.benchmark?.promptCount);
    nodes.geoBenchmarkHint.textContent = geo.benchmark?.lastRun
      ? `最近测试 ${formatTime(geo.benchmark.lastRun)}`
      : "每周抽样、每月完整测试";

    nodes.geoPlatformRows.innerHTML = platforms.length
      ? platforms.map((platform) => {
        const training = platform.trainingAllowed === false
          ? "训练关闭"
          : (platform.trainingAllowed === true ? "训练允许" : "另行控制");
        return `
          <div class="geo-platform-row">
            <div><strong>${escapeHtml(platform.name)}</strong><span>${escapeHtml(platform.discoveryBot)}</span></div>
            <span class="status ${platform.discoveryAllowed ? "" : "is-error"}">${platform.discoveryAllowed ? "搜索抓取已允许" : "搜索抓取受阻"}</span>
            <span class="geo-training">${escapeHtml(training)}</span>
            <small>${escapeHtml(platform.measurement || "待接数据源")}</small>
          </div>`;
      }).join("")
      : '<div class="empty-state geo-empty">没有平台配置</div>';

    const missingSources = Object.values(geo.dataSources || {}).filter((value) => value !== "connected").length;
    nodes.geoSourceNote.textContent = missingSources
      ? "抓取资格来自站点配置；AI 引用、引流和基准结果仍待接入官方或可核验数据源。"
      : "GEO 数据源已接通。";
  }

  function periodKey(date, range) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    return range === "month" ? `${year}-${month}` : `${year}-${month}-${day}`;
  }

  function buildPeriods(range) {
    const now = new Date();
    const count = range === "month" ? 12 : 14;
    const rows = [];
    for (let index = count - 1; index >= 0; index -= 1) {
      const date = new Date(now);
      if (range === "month") date.setMonth(now.getMonth() - index, 1);
      else date.setDate(now.getDate() - index);
      rows.push({
        key: periodKey(date, range),
        label: range === "month" ? monthFormatter.format(date) : dayFormatter.format(date),
        value: 0
      });
    }
    return rows;
  }

  function metricSeries(source, range) {
    const raw = source?.series?.[range];
    if (!Array.isArray(raw)) return null;
    const rows = buildPeriods(range);
    const lookup = new Map(raw.map((item) => [String(item.period || item.date || item.month), Number(item.count || 0)]));
    rows.forEach((row) => {
      row.value = lookup.get(row.key) || 0;
    });
    return rows;
  }

  function articleSeries(range) {
    const rows = buildPeriods(range);
    const lookup = new Map(rows.map((row) => [row.key, row]));
    const seen = new Set();
    (state.metrics?.articles?.latest || []).forEach((article) => {
      const date = new Date(article.lastmod || article.dateModified || "");
      if (Number.isNaN(date.getTime())) return;
      const uniqueKey = `${article.story}|${periodKey(date, range)}`;
      if (seen.has(uniqueKey)) return;
      seen.add(uniqueKey);
      const row = lookup.get(periodKey(date, range));
      if (row) row.value += 1;
    });
    return rows;
  }

  function renderBars(node, rows, emptyText) {
    node.innerHTML = "";
    if (!rows || !rows.length || rows.every((row) => !row.value)) {
      node.style.setProperty("--bars", 1);
      node.innerHTML = `<div class="empty-state">${escapeHtml(emptyText)}</div>`;
      return;
    }

    const max = Math.max(...rows.map((row) => row.value), 1);
    node.style.setProperty("--bars", rows.length);
    rows.forEach((row) => {
      const bar = document.createElement("div");
      bar.className = row.value ? "bar" : "bar is-muted";
      bar.style.height = `${Math.max(4, Math.round((row.value / max) * 100))}%`;
      bar.title = `${row.label}: ${row.value}`;
      const label = document.createElement("span");
      label.textContent = row.label;
      bar.appendChild(label);
      node.appendChild(bar);
    });
  }

  function uniqueStoryCounts() {
    const stories = new Map();
    (state.metrics?.articles?.latest || []).forEach((article) => {
      const key = article.story || article.path;
      if (!stories.has(key)) stories.set(key, article.topic);
    });
    return Array.from(stories.values()).reduce((counts, topic) => {
      counts[topic] = (counts[topic] || 0) + 1;
      return counts;
    }, {});
  }

  function renderMetrics() {
    const consultation = consultationData();
    const consultationValue = state.range === "month" ? consultation?.month : consultation?.today;
    nodes.consultationLabel.textContent = state.range === "month" ? "本月咨询" : "今日咨询";
    nodes.consultationCount.textContent = formatCount(consultationValue);
    nodes.consultationHint.textContent = consultation
      ? "来自咨询数据表"
      : (state.relay?.service || state.metrics?.source?.leadRelay === "online"
        ? "表单在线，统计端点待接通"
        : "咨询统计未接通");

    nodes.publishedCount.textContent = formatCount(state.metrics?.articles?.uniqueTopics);
    nodes.publishedHint.textContent = `${formatCount(state.metrics?.articles?.totalPages)} 个语言页面`;

    const indexSummary = state.metrics?.indexed || {};
    const indexed = indexSummary.count;
    nodes.indexedCount.textContent = formatCount(indexed);
    nodes.indexedHint.textContent = isFiniteNumber(indexed)
      ? "来自 Search Console"
      : (isFiniteNumber(indexSummary.inspectedCount) && Number(indexSummary.inspectedCount) > 0
        ? `已确认 ${formatCount(indexSummary.confirmedCount)} · 已检查 ${formatCount(indexSummary.inspectedCount)} · ${formatCount(indexSummary.unknownCount)} 未知`
        : "Search Console 未接通");

    const topicSummary = state.metrics?.topicEngine?.summary || {};
    nodes.topicReadyCount.textContent = formatCount(topicSummary.eligibleCandidates);
    nodes.topicReadyHint.textContent = isFiniteNumber(topicSummary.eligibleCandidates)
      ? `${formatCount(topicSummary.registeredCandidates)} 个登记问题中筛出`
      : "选题引擎尚未生成";

    const sitemapReport = state.metrics?.sitemap?.searchConsole;
    nodes.articleSource.textContent = sitemapReport?.status && isFiniteNumber(sitemapReport.discoveredPages)
      ? `sitemap ${sitemapReport.status} · ${formatCount(sitemapReport.discoveredPages)} 个网址`
      : (state.metrics ? "本地页面 + sitemap" : "未读取");
    nodes.leadSource.textContent = consultation
      ? "真实咨询统计"
      : (state.relay?.service || state.metrics?.source?.leadRelay === "online" ? "表单在线 / 统计待接" : "未接通");
    nodes.indexSource.textContent = state.metrics?.source?.searchConsole === "not-connected"
      ? "未接通"
      : `Search Console · 已检查 ${formatCount(indexSummary.inspectedCount)} 页`;
    nodes.lastUpdated.textContent = formatTime(state.metrics?.generatedAt);

    const performance = state.metrics?.searchPerformance || {};
    nodes.gscClicks.textContent = formatCount(performance.clicks);
    nodes.gscImpressions.textContent = formatCount(performance.impressions);
    nodes.gscCtr.textContent = isFiniteNumber(performance.ctr) ? `${(Number(performance.ctr) * 100).toFixed(1)}%` : "--";
    nodes.gscPosition.textContent = isFiniteNumber(performance.averagePosition) ? Number(performance.averagePosition).toFixed(1) : "--";
  }

  function renderPersonas() {
    const rows = state.metrics?.topicEngine?.personas || [];
    nodes.personaRows.innerHTML = rows.length
      ? rows.map((row) => `
        <article class="persona-row">
          <div class="persona-name">
            <span>${escapeHtml(row.name)} · ${escapeHtml(row.age)} 岁</span>
            <strong>${escapeHtml(row.label)}</strong>
          </div>
          <p>${escapeHtml(row.situation)}</p>
          <div class="persona-search">
            <span>会这样搜</span>
            <strong>${escapeHtml(row.searchExample)}</strong>
          </div>
          <div class="persona-signal">
            <strong>${formatCount(row.highestScore)}</strong>
            <span>最高分 · ${formatCount(row.observedQueryMatches)} 次真实匹配</span>
          </div>
        </article>`).join("")
      : '<div class="empty-state persona-empty">人物画像尚未生成</div>';
  }

  function renderTopics() {
    const engine = state.metrics?.topicEngine || {};
    const allocation = engine.adaptiveAllocation?.byTopic || {};
    const starter = state.metrics?.queue?.starterBacklog || {};
    const storyCounts = uniqueStoryCounts();
    const topicKeys = ["hk-inheritance", "singapore", "macau", "united-states"];

    nodes.topicMethod.textContent = engine.adaptiveAllocation?.method || "等待人物、搜索和反馈数据。";
    nodes.candidateLimitBadge.textContent = `${formatCount(engine.adaptiveAllocation?.selected)} / ${formatCount(engine.adaptiveAllocation?.limit)}`;

    nodes.topicRows.innerHTML = topicKeys.map((topic) => {
      const meta = topicMeta[topic];
      const slots = Number(allocation[topic] || 0);
      const published = Number(storyCounts[topic] || 0);
      const backlog = topic === "hk-inheritance"
        ? Number(state.metrics?.queue?.hkLaunch?.remaining || 0)
        : Number(starter[topic] || 0);
      const denominator = Math.max(published + backlog, 1);
      const progress = Math.min(100, Math.round((published / denominator) * 100));
      return `
        <div class="topic-row" style="--topic-color:${meta.color}">
          <div class="topic-name"><strong>${meta.label}</strong><small>${meta.note}</small></div>
          <div class="progress-track" aria-label="${meta.label}进度"><span style="width:${progress}%"></span></div>
          <div class="topic-value">${published} 已发</div>
          <div class="topic-status">本轮 ${slots} 个</div>
        </div>`;
    }).join("");
  }

  function renderRecommendations() {
    const engine = state.metrics?.topicEngine || {};
    const rows = engine.recommendations || [];
    nodes.recommendationSummary.textContent = `${formatCount(engine.summary?.eligibleCandidates)} 个达到门槛`;
    nodes.recommendationRows.innerHTML = rows.length
      ? rows.map((row) => `
        <tr>
          <td><strong class="score-value">${formatCount(row.score)}</strong></td>
          <td>${escapeHtml(row.personaLabel)}</td>
          <td><span class="query-text">${escapeHtml(row.primaryQuery)}</span></td>
          <td>${escapeHtml(row.deepIntent)}</td>
          <td><span class="status is-pending">${escapeHtml(row.action)}</span></td>
        </tr>`).join("")
      : '<tr><td colspan="5">本轮没有达到门槛的选题，不为了数量强行扩写。</td></tr>';
  }

  function renderFeedback() {
    const engine = state.metrics?.topicEngine || {};
    const rules = engine.feedbackRules || [];
    nodes.feedbackSummary.textContent = `${formatCount(engine.summary?.retiredPatterns)} 个已停模式`;
    nodes.feedbackRules.innerHTML = rules.length
      ? rules.map((row) => `
        <div class="feedback-row">
          <strong>${escapeHtml(row.window)}</strong>
          <p>${escapeHtml(row.action)}</p>
        </div>`).join("")
      : '<div class="empty-state">反馈规则尚未生成</div>';

    const learning = engine.learningLog || [];
    nodes.learningLog.innerHTML = learning.length
      ? learning.map((row) => `<li>${escapeHtml(row)}</li>`).join("")
      : '<li>等待 Search Console 和咨询数据。</li>';
  }

  function renderTrends() {
    const consultation = consultationData();
    const consultationRows = metricSeries(consultation, state.range);
    renderBars(nodes.consultationChart, consultationRows, "咨询统计端点接通后显示");
    nodes.consultationTrendHint.textContent = consultationRows
      ? (state.range === "month" ? "过去 12 个月真实咨询" : "过去 14 天真实咨询")
      : "当前不推测咨询数量";

    renderBars(nodes.articleChart, articleSeries(state.range), "本周期没有文章更新");
    nodes.articleTrendHint.textContent = state.range === "month" ? "过去 12 个月文章更新" : "过去 14 天文章更新";
  }

  function renderQueue() {
    const rows = state.metrics?.queue?.next || [];
    nodes.queueSummary.textContent = `${formatCount(state.metrics?.queue?.hkLaunch?.remaining)} 篇待发布`;
    nodes.queueRows.innerHTML = rows.length
      ? rows.map((row) => `
        <tr>
          <td>${escapeHtml(row.id)}</td>
          <td>${escapeHtml(row.title)}</td>
          <td>${escapeHtml(row.intent)}</td>
          <td>${escapeHtml(depthLabels[row.depth] || row.depth)}</td>
          <td><span class="status is-pending">${escapeHtml(statusLabels[row.status] || row.status)}</span></td>
        </tr>`).join("")
      : '<tr><td colspan="5">当前队列为空</td></tr>';
  }

  function renderLeadChain() {
    const steps = state.metrics?.leadChain?.steps || ["文章入口", "AI 初步问答", "电话表单", "表单中继", "咨询表格", "邮件通知"];
    const labels = {
      "Article CTA": "文章入口",
      "AI initial Q&A": "AI 初步问答",
      "Lead form": "电话表单",
      "Form relay": "表单中继",
      "Lead sheet": "咨询表格",
      "Email notification": "邮件通知"
    };
    nodes.leadChain.innerHTML = steps.map((step) => `<li>${escapeHtml(labels[step] || step)}</li>`).join("");

    const consultation = consultationData();
    const byTopic = Array.isArray(consultation?.by_topic) ? consultation.by_topic : [];
    nodes.leadBreakdown.innerHTML = byTopic.length
      ? byTopic.slice(0, 6).map((item) => `<div class="breakdown-row"><span>${escapeHtml(item.key)}</span><strong>${formatCount(item.count)}</strong></div>`).join("")
      : '<div class="breakdown-row"><span>专题来源统计</span><strong>待端点接通</strong></div>';
  }

  function renderPolicy() {
    const fallback = [
      "每天 30 个是候选位，不是强制发布量。",
      "只显示真实发布或最后更新时间，不回填历史假日期。",
      "每篇都要有人类可读的判断路径和三张解释性图片。",
      "英文由大模型按英文读者习惯重写，不逐句硬翻。",
      "收录状态只取 Search Console，不抓取 Google 搜索结果。"
    ];
    const notes = state.metrics?.compliance?.notes;
    const rows = Array.isArray(notes) && notes.length ? notes : fallback;
    const translated = {
      "30 means candidate slots, not a forced daily publication count.": fallback[0],
      "Use truthful publication and modification dates only.": fallback[1],
      "Do not create thin pages for minor query variations.": "不为细小关键词变体批量制作低价值页面。",
      "Use Search Console data for index monitoring; do not scrape Google results.": fallback[4]
    };
    nodes.policyList.innerHTML = rows.map((row) => `<li>${escapeHtml(translated[row] || row)}</li>`).join("");
  }

  function languageLabel(language) {
    if (language === "en") return "EN";
    if (language === "zh-Hans") return "简";
    return "繁";
  }

  function seoStatus(article) {
    if (!article.indexable) return { label: "noindex", className: "is-error" };
    if (!article.inSitemap) return { label: "未进 sitemap", className: "is-pending" };
    return { label: "可抓取", className: "" };
  }

  function renderArticles() {
    const rows = [...(state.metrics?.articles?.latest || [])].sort(
      (left, right) => Number(right.indexKnown === true) - Number(left.indexKnown === true)
    );
    const bad = rows.filter((row) => !row.indexable || !row.inSitemap).length;
    nodes.articleAuditSummary.textContent = bad ? `${bad} needs fix` : "SEO base passed";
    nodes.articleRows.innerHTML = rows.length
      ? rows.slice(0, 30).map((article) => {
        const seo = seoStatus(article);
        const topic = topicMeta[article.topic]?.label || "其他";
        const indexKnown = article.indexKnown === true;
        const indexLabel = indexKnown ? (article.indexed ? "已收录" : "未收录") : "未知";
        const indexClass = indexKnown ? (article.indexed ? "" : "is-pending") : "is-unknown";
        return `
          <tr>
            <td>${escapeHtml(article.title)}</td>
            <td>${escapeHtml(topic)}</td>
            <td>${languageLabel(article.language)}</td>
            <td>${escapeHtml(article.lastmod || article.dateModified || "--")}</td>
            <td><span class="status ${seo.className}">${seo.label}</span></td>
            <td><span class="status ${indexClass}">${indexLabel}</span></td>
          </tr>`;
      }).join("")
      : '<tr><td colspan="6">没有读取到文章页面</td></tr>';
  }

  function render() {
    renderMetrics();
    renderGeo();
    renderPersonas();
    renderTopics();
    renderRecommendations();
    renderFeedback();
    renderTrends();
    renderQueue();
    renderLeadChain();
    renderPolicy();
    renderArticles();
  }

  function bindRangeSwitch() {
    document.querySelectorAll("[data-range]").forEach((button) => {
      button.addEventListener("click", () => {
        state.range = button.dataset.range || "day";
        document.querySelectorAll("[data-range]").forEach((item) => {
          item.classList.toggle("is-active", item === button);
          item.setAttribute("aria-pressed", item === button ? "true" : "false");
        });
        render();
      });
    });
  }

  async function init() {
    bindRangeSwitch();
    await loadData();
    render();
  }

  init();
})();
