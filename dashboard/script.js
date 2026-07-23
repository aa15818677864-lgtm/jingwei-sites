(function () {
  "use strict";

  const state = {
    range: "day",
    articleFilter: "all",
    metrics: null,
    geo: null,
    liveLeads: null,
    relay: null
  };

  const byId = (id) => document.getElementById(id);
  const nodes = {
    freshness: byId("freshness"),
    consultationLabel: byId("consultationLabel"),
    consultationCount: byId("consultationCount"),
    consultationHint: byId("consultationHint"),
    publishedCount: byId("publishedCount"),
    publishedHint: byId("publishedHint"),
    indexedCount: byId("indexedCount"),
    indexedHint: byId("indexedHint"),
    pendingCount: byId("pendingCount"),
    pendingHint: byId("pendingHint"),
    sourceSummary: byId("sourceSummary"),
    lastUpdated: byId("lastUpdated"),
    trendHint: byId("trendHint"),
    activityChart: byId("activityChart"),
    queueRows: byId("queueRows"),
    queueSummary: byId("queueSummary"),
    candidateNote: byId("candidateNote"),
    articleRows: byId("articleRows"),
    articleSummary: byId("articleSummary"),
    gscClicks: byId("gscClicks"),
    gscImpressions: byId("gscImpressions"),
    gscCtr: byId("gscCtr"),
    gscPosition: byId("gscPosition"),
    topicDetail: byId("topicDetail"),
    geoDetail: byId("geoDetail"),
    sourceDetail: byId("sourceDetail")
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

  const topicLabels = {
    "hk-inheritance": "香港继承",
    macau: "澳门",
    singapore: "新加坡",
    "united-states": "美国",
    "other-cross-border": "跨境事务"
  };

  const statusLabels = {
    planned: "待写",
    "drafted-zh-Hant": "繁中初稿",
    "drafted-zh-Hans": "简中初稿",
    "model-written-en": "英文已写",
    "legal-reviewed": "已复核",
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

    const isLocalPreview = ["127.0.0.1", "localhost"].includes(window.location.hostname);
    const configuredEndpoint = isLocalPreview ? "" : (window.SITE_CONFIG?.dashboardMetricsEndpoint || "");
    const relayEndpoint = !isLocalPreview && window.SITE_CONFIG?.googleSheetsEndpoint
      ? `${window.SITE_CONFIG.googleSheetsEndpoint}?action=dashboard`
      : "";

    if (configuredEndpoint) {
      const live = await fetchJson(configuredEndpoint);
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

  function periodKey(date, range) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    return range === "month" ? `${year}-${month}` : `${year}-${month}-${day}`;
  }

  function buildPeriods(range) {
    const now = new Date();
    const count = range === "month" ? 6 : 14;
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
    const lookup = new Map(raw.map((item) => [
      String(item.period || item.date || item.month),
      Number(item.count || 0)
    ]));
    rows.forEach((row) => {
      row.value = lookup.get(row.key) || 0;
    });
    return rows;
  }

  function storyRows() {
    const stories = new Map();
    const languagePriority = { "zh-Hant": 0, "zh-Hans": 1, en: 2 };
    (state.metrics?.articles?.latest || []).forEach((article) => {
      const key = article.story || article.path;
      const current = stories.get(key);
      if (!current || (languagePriority[article.language] ?? 9) < (languagePriority[current.language] ?? 9)) {
        stories.set(key, article);
      }
    });
    return Array.from(stories.values()).sort((left, right) => {
      const rightDate = new Date(right.dateModified || right.lastmod || right.datePublished || 0).getTime();
      const leftDate = new Date(left.dateModified || left.lastmod || left.datePublished || 0).getTime();
      return rightDate - leftDate;
    });
  }

  function articleSeries(range) {
    const rows = buildPeriods(range);
    const lookup = new Map(rows.map((row) => [row.key, row]));
    storyRows().forEach((article) => {
      const date = new Date(article.datePublished || article.lastmod || article.dateModified || "");
      if (Number.isNaN(date.getTime())) return;
      const row = lookup.get(periodKey(date, range));
      if (row) row.value += 1;
    });
    return rows;
  }

  function currentPeriodPublishedCount() {
    const currentKey = periodKey(new Date(), state.range);
    return storyRows().filter((article) => {
      const date = new Date(article.datePublished || "");
      return !Number.isNaN(date.getTime()) && periodKey(date, state.range) === currentKey;
    }).length;
  }

  function renderMetrics() {
    const metrics = state.metrics;
    const consultation = consultationData();
    const consultationValue = state.range === "month" ? consultation?.month : consultation?.today;
    nodes.consultationLabel.textContent = state.range === "month" ? "本月咨询" : "今日咨询";
    nodes.consultationCount.textContent = formatCount(consultationValue);
    nodes.consultationHint.textContent = consultation
      ? "来自咨询数据表"
      : (state.relay?.service || metrics?.source?.leadRelay === "online"
        ? "表单在线，统计端点待接通"
        : "咨询统计未接通");

    nodes.publishedCount.textContent = formatCount(metrics?.articles?.uniqueTopics);
    const periodLabel = state.range === "month" ? "本月" : "今日";
    nodes.publishedHint.textContent = `${periodLabel}新增 ${formatCount(currentPeriodPublishedCount())} 篇 · ${formatCount(metrics?.articles?.totalPages)} 个语言页面`;

    const indexSummary = metrics?.indexed || {};
    nodes.indexedCount.textContent = formatCount(indexSummary.count);
    nodes.indexedHint.textContent = isFiniteNumber(indexSummary.count)
      ? "来自 Search Console"
      : `已查 ${formatCount(indexSummary.inspectedCount)} 页 · ${formatCount(indexSummary.unknownCount)} 页待确认`;

    const pending = metrics?.queue?.hkLaunch?.remaining;
    nodes.pendingCount.textContent = formatCount(pending);
    nodes.pendingHint.textContent = `${formatCount(metrics?.queue?.next?.length)} 篇已有明确题目`;

    const sitemap = metrics?.sitemap?.searchConsole;
    const indexText = isFiniteNumber(indexSummary.inspectedCount)
      ? `Search Console 已查 ${formatCount(indexSummary.inspectedCount)} 页`
      : "Search Console 待同步";
    nodes.sourceSummary.textContent = sitemap?.status
      ? `站点地图${sitemap.status} · ${indexText}`
      : "站点地图与收录数据待同步";
    nodes.lastUpdated.textContent = `更新于 ${formatTime(metrics?.generatedAt)}`;
    nodes.freshness.textContent = metrics
      ? "只显示可核对的数据，未知项保持空白"
      : "没有读取到网站运营数据";
  }

  function renderActivity() {
    const articles = articleSeries(state.range);
    const consultations = metricSeries(consultationData(), state.range);
    const values = articles.flatMap((row, index) => [row.value, consultations?.[index]?.value || 0]);
    const max = Math.max(...values, 1);
    const hasAnyData = values.some((value) => value > 0);

    nodes.trendHint.textContent = state.range === "month"
      ? `过去 6 个月 · ${consultations ? "文章与咨询" : "文章发布，咨询统计待接"}`
      : `过去 14 天 · ${consultations ? "文章与咨询" : "文章发布，咨询统计待接"}`;

    if (!hasAnyData) {
      nodes.activityChart.innerHTML = '<div class="empty-state">当前周期没有可显示的变化</div>';
      return;
    }

    nodes.activityChart.style.setProperty("--groups", articles.length);
    nodes.activityChart.innerHTML = articles.map((row, index) => {
      const consultationValue = consultations?.[index]?.value || 0;
      const articleHeight = row.value ? Math.max(5, Math.round((row.value / max) * 100)) : 2;
      const consultationHeight = consultationValue ? Math.max(5, Math.round((consultationValue / max) * 100)) : 2;
      return `
        <div class="chart-group">
          <div class="chart-bars">
            <i class="chart-bar article-bar" style="height:${articleHeight}%" title="${escapeHtml(row.label)}：文章 ${row.value}"></i>
            <i class="chart-bar consultation-bar${consultations ? "" : " is-unavailable"}" style="height:${consultationHeight}%" title="${escapeHtml(row.label)}：咨询 ${consultations ? consultationValue : "未接通"}"></i>
          </div>
          <span>${escapeHtml(row.label)}</span>
        </div>`;
    }).join("");
  }

  function renderQueue() {
    const rows = state.metrics?.queue?.next || [];
    const remaining = state.metrics?.queue?.hkLaunch?.remaining;
    nodes.queueSummary.textContent = `${formatCount(remaining)} 篇待处理`;
    nodes.queueRows.innerHTML = rows.length
      ? rows.slice(0, 6).map((row) => `
        <div class="queue-row">
          <span class="queue-id">${escapeHtml(row.id)}</span>
          <div><strong>${escapeHtml(row.title)}</strong><small>${escapeHtml(row.intent)}</small></div>
          <span class="status neutral">${escapeHtml(statusLabels[row.status] || row.status)}</span>
        </div>`).join("")
      : '<div class="empty-state">当前没有待处理文章</div>';

    const summary = state.metrics?.topicEngine?.summary || {};
    const limit = state.metrics?.topicEngine?.adaptiveAllocation?.limit;
    const gap = isFiniteNumber(limit) && isFiniteNumber(summary.eligibleCandidates)
      ? Math.max(0, Number(limit) - Number(summary.eligibleCandidates))
      : null;
    nodes.candidateNote.textContent = isFiniteNumber(summary.eligibleCandidates)
      ? `本轮可写选题 ${formatCount(summary.eligibleCandidates)}/${formatCount(limit)}${gap ? `，还需补充 ${formatCount(gap)} 个真实问题` : ""}`
      : "选题储备尚未生成";
  }

  function articleMatchesFilter(article) {
    if (state.articleFilter === "indexed") return article.indexKnown && article.indexed;
    if (state.articleFilter === "unknown") return !article.indexKnown;
    if (state.articleFilter === "issues") {
      return !article.indexable || !article.inSitemap || (article.indexKnown && !article.indexed);
    }
    return true;
  }

  function cleanTitle(value) {
    return String(value || "未命名文章").split(" | ")[0];
  }

  function renderArticles() {
    const allRows = storyRows();
    const filtered = allRows.filter(articleMatchesFilter);
    const visible = filtered.slice(0, 12);
    const totalPages = state.metrics?.articles?.totalPages;
    nodes.articleSummary.textContent = state.articleFilter === "all"
      ? `${formatCount(allRows.length)} 篇文章 · ${formatCount(totalPages)} 个语言页面 · 显示最近 12 篇`
      : `筛选出 ${formatCount(filtered.length)} 篇 · 显示最近 12 篇`;

    nodes.articleRows.innerHTML = visible.length
      ? visible.map((article) => {
        const technicalOk = article.indexable && article.inSitemap;
        const indexLabel = article.indexKnown ? (article.indexed ? "已收录" : "未收录") : "待确认";
        const indexClass = article.indexKnown ? (article.indexed ? "positive" : "warning") : "neutral";
        return `
          <tr>
            <td><a href="${escapeHtml(article.url || article.path)}">${escapeHtml(cleanTitle(article.title))}</a></td>
            <td>${escapeHtml(topicLabels[article.topic] || article.topic || "其他")}</td>
            <td>${escapeHtml(article.dateModified || article.lastmod || "--")}</td>
            <td><span class="status ${technicalOk ? "positive" : "warning"}">${technicalOk ? "正常" : "需检查"}</span></td>
            <td><span class="status ${indexClass}">${indexLabel}</span></td>
          </tr>`;
      }).join("")
      : '<tr><td colspan="5">这个筛选条件下没有文章</td></tr>';
  }

  function renderDetails() {
    const performance = state.metrics?.searchPerformance || {};
    nodes.gscClicks.textContent = formatCount(performance.clicks);
    nodes.gscImpressions.textContent = formatCount(performance.impressions);
    nodes.gscCtr.textContent = isFiniteNumber(performance.ctr) ? `${(Number(performance.ctr) * 100).toFixed(1)}%` : "--";
    nodes.gscPosition.textContent = isFiniteNumber(performance.averagePosition) ? Number(performance.averagePosition).toFixed(1) : "--";

    const summary = state.metrics?.topicEngine?.summary || {};
    const allocation = state.metrics?.topicEngine?.adaptiveAllocation || {};
    nodes.topicDetail.textContent = isFiniteNumber(summary.eligibleCandidates)
      ? `${formatCount(summary.registeredCandidates)} 个登记问题中，${formatCount(summary.eligibleCandidates)} 个达到写作门槛；本轮上限 ${formatCount(allocation.limit)} 个。`
      : "选题数据尚未生成。";

    const geoStatus = state.geo?.status || {};
    nodes.geoDetail.textContent = isFiniteNumber(geoStatus.eligiblePlatforms)
      ? `${formatCount(geoStatus.eligiblePlatforms)}/${formatCount(geoStatus.platformCount)} 个搜索抓取通道已放行；AI 引用与引流需要平台数据后才能确认。`
      : "AI 搜索技术状态尚未生成。";

    const sitemap = state.metrics?.sitemap?.searchConsole;
    const indexSummary = state.metrics?.indexed || {};
    const leadText = consultationData()
      ? "咨询统计已接通"
      : (state.relay?.service || state.metrics?.source?.leadRelay === "online" ? "咨询表单在线，统计待接" : "咨询链路待检查");
    nodes.sourceDetail.textContent = sitemap?.status
      ? `站点地图${sitemap.status}，发现 ${formatCount(sitemap.discoveredPages)} 个网址；Search Console 已检查 ${formatCount(indexSummary.inspectedCount)} 页；${leadText}。`
      : `站点地图待同步；${leadText}。`;
  }

  function render() {
    renderMetrics();
    renderActivity();
    renderQueue();
    renderArticles();
    renderDetails();
  }

  function bindControls() {
    document.querySelectorAll("[data-range]").forEach((button) => {
      button.addEventListener("click", () => {
        state.range = button.dataset.range;
        document.querySelectorAll("[data-range]").forEach((item) => {
          const active = item === button;
          item.classList.toggle("is-active", active);
          item.setAttribute("aria-pressed", String(active));
        });
        renderMetrics();
        renderActivity();
      });
    });

    document.querySelectorAll("[data-filter]").forEach((button) => {
      button.addEventListener("click", () => {
        state.articleFilter = button.dataset.filter;
        document.querySelectorAll("[data-filter]").forEach((item) => {
          const active = item === button;
          item.classList.toggle("is-active", active);
          item.setAttribute("aria-pressed", String(active));
        });
        renderArticles();
      });
    });
  }

  bindControls();
  loadData().then(render);
}());
