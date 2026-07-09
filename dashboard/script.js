(function () {
  const state = {
    range: "day",
    articles: [],
    metrics: null,
    relayOnline: false
  };

  const nodes = {
    consultationCount: document.getElementById("consultationCount"),
    consultationHint: document.getElementById("consultationHint"),
    publishedCount: document.getElementById("publishedCount"),
    publishedHint: document.getElementById("publishedHint"),
    indexedCount: document.getElementById("indexedCount"),
    indexedHint: document.getElementById("indexedHint"),
    dataStatus: document.getElementById("dataStatus"),
    dataHint: document.getElementById("dataHint"),
    consultationChart: document.getElementById("consultationChart"),
    articleChart: document.getElementById("articleChart"),
    consultationTrendHint: document.getElementById("consultationTrendHint"),
    articleTrendHint: document.getElementById("articleTrendHint"),
    articleRows: document.getElementById("articleRows"),
    lastUpdated: document.getElementById("lastUpdated")
  };

  const dayFormatter = new Intl.DateTimeFormat("zh-CN", { month: "2-digit", day: "2-digit" });
  const monthFormatter = new Intl.DateTimeFormat("zh-CN", { year: "2-digit", month: "2-digit" });
  const fullFormatter = new Intl.DateTimeFormat("zh-CN", {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit"
  });

  function sameOrigin(path) {
    return new URL(path, window.location.origin).href;
  }

  function articleLanguage(pathname) {
    if (/_en\.html$/.test(pathname)) return "EN";
    if (/_cn\.html$/.test(pathname)) return "简";
    return "繁";
  }

  function isArticlePage(url) {
    const parsed = new URL(url);
    const path = parsed.pathname;
    if (!path.startsWith("/articles/")) return false;
    if (path === "/articles/") return false;
    if (/\/index(?:_cn|_en)?\.html$/.test(path)) return false;
    if (path.endsWith("/")) return false;
    return path.endsWith(".html");
  }

  function articleTitleFromUrl(url) {
    const path = new URL(url).pathname;
    const file = path.split("/").pop() || path;
    return file
      .replace(/_cn\.html$|_en\.html$|\.html$/g, "")
      .split("-")
      .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
      .join(" ");
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
    const periods = [];
    for (let index = count - 1; index >= 0; index -= 1) {
      const date = new Date(now);
      if (range === "month") {
        date.setMonth(now.getMonth() - index, 1);
      } else {
        date.setDate(now.getDate() - index);
      }
      periods.push({
        key: periodKey(date, range),
        label: range === "month" ? monthFormatter.format(date) : dayFormatter.format(date),
        value: 0
      });
    }
    return periods;
  }

  function renderBars(node, rows, emptyText) {
    node.innerHTML = "";
    if (!rows || !rows.length || rows.every((row) => !row.value)) {
      const empty = document.createElement("div");
      empty.className = "empty-state";
      empty.textContent = emptyText;
      node.style.setProperty("--bars", 1);
      node.appendChild(empty);
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

  async function loadSitemap() {
    const response = await fetch(sameOrigin("/sitemap.xml"), { cache: "no-store" });
    if (!response.ok) throw new Error("sitemap unavailable");
    const xml = await response.text();
    const doc = new DOMParser().parseFromString(xml, "application/xml");
    return Array.from(doc.querySelectorAll("url")).map((entry) => {
      const loc = entry.querySelector("loc")?.textContent?.trim() || "";
      const lastmod = entry.querySelector("lastmod")?.textContent?.trim() || "";
      return { loc, lastmod };
    }).filter((entry) => entry.loc && isArticlePage(entry.loc));
  }

  async function loadMetrics() {
    const configured = window.SITE_CONFIG?.dashboardMetricsEndpoint;
    const sheetEndpoint = window.SITE_CONFIG?.googleSheetsEndpoint
      ? `${window.SITE_CONFIG.googleSheetsEndpoint}?action=dashboard`
      : "";
    const candidates = [configured, sameOrigin("/dashboard/metrics.json"), sheetEndpoint]
      .filter(Boolean);

    for (const endpoint of candidates) {
      try {
        const response = await fetch(endpoint, { cache: "no-store" });
        if (!response.ok) continue;
        const data = await response.json();
        if (data?.consultation || data?.indexed) return data;
        if (data?.ok && data?.service) state.relayOnline = true;
      } catch (error) {
        // Try the next source. Some endpoints are intentionally private.
      }
    }
    return null;
  }

  function seriesFromArticles(range) {
    const rows = buildPeriods(range);
    const lookup = new Map(rows.map((row) => [row.key, row]));
    state.articles.forEach((article) => {
      const date = new Date(article.lastmod || "");
      if (Number.isNaN(date.getTime())) return;
      const row = lookup.get(periodKey(date, range));
      if (row) row.value += 1;
    });
    return rows;
  }

  function seriesFromMetric(name, range) {
    const source = state.metrics?.[name]?.series?.[range];
    if (!Array.isArray(source)) return null;
    const rows = buildPeriods(range);
    const lookup = new Map(source.map((row) => [String(row.period || row.date || row.month), Number(row.count || 0)]));
    rows.forEach((row) => {
      row.value = lookup.get(row.key) || 0;
    });
    return rows;
  }

  function renderMetrics() {
    const rangeLabel = state.range === "month" ? "本月" : "今日";
    const consultation = state.metrics?.consultation || null;
    const indexed = state.metrics?.indexed || null;
    const consultationValue = state.range === "month" ? consultation?.month : consultation?.today;

    nodes.consultationCount.textContent = Number.isFinite(Number(consultationValue))
      ? Number(consultationValue).toLocaleString("zh-CN")
      : "--";
    nodes.consultationHint.textContent = consultation
      ? `${rangeLabel}真实咨询`
      : (state.relayOnline ? "提交服务在线，统计未开放" : "统计接口未接入");

    nodes.publishedCount.textContent = state.articles.length.toLocaleString("zh-CN");
    nodes.publishedHint.textContent = "来自 sitemap.xml";

    nodes.indexedCount.textContent = Number.isFinite(Number(indexed?.count))
      ? Number(indexed.count).toLocaleString("zh-CN")
      : "--";
    nodes.indexedHint.textContent = indexed ? "来自收录数据源" : "Search Console 未接入";

    const connectedCount = [state.articles.length > 0, Boolean(consultation), Boolean(indexed)].filter(Boolean).length;
    nodes.dataStatus.textContent = `${connectedCount}/3`;
    nodes.dataHint.textContent = connectedCount === 3 ? "全部数据源已连接" : "部分数据源待接入";

    nodes.lastUpdated.textContent = fullFormatter.format(new Date());
  }

  function renderCharts() {
    const articleRows = seriesFromArticles(state.range);
    renderBars(nodes.articleChart, articleRows, "近期没有文章更新");
    nodes.articleTrendHint.textContent = state.range === "month"
      ? "过去 12 个月 sitemap 更新"
      : "过去 14 天 sitemap 更新";

    const consultationRows = seriesFromMetric("consultation", state.range);
    renderBars(nodes.consultationChart, consultationRows, "咨询统计接口未接入");
    nodes.consultationTrendHint.textContent = consultationRows
      ? (state.range === "month" ? "过去 12 个月咨询" : "过去 14 天咨询")
      : "等待咨询统计接口";
  }

  function renderTable() {
    const rows = state.articles
      .slice()
      .sort((a, b) => String(b.lastmod).localeCompare(String(a.lastmod)))
      .slice(0, 10);

    nodes.articleRows.innerHTML = "";
    if (!rows.length) {
      nodes.articleRows.innerHTML = '<tr><td colspan="4">没有读到文章页面</td></tr>';
      return;
    }

    rows.forEach((row) => {
      const url = new URL(row.loc);
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${articleTitleFromUrl(row.loc)}</td>
        <td>${articleLanguage(url.pathname)}</td>
        <td>${row.lastmod || "--"}</td>
        <td><span class="status-dot">已发布</span></td>
      `;
      nodes.articleRows.appendChild(tr);
    });
  }

  function render() {
    renderMetrics();
    renderCharts();
    renderTable();
  }

  function bindRangeSwitch() {
    document.querySelectorAll("[data-range]").forEach((button) => {
      button.addEventListener("click", () => {
        state.range = button.dataset.range || "day";
        document.querySelectorAll("[data-range]").forEach((item) => {
          item.classList.toggle("is-active", item === button);
        });
        render();
      });
    });
  }

  async function init() {
    bindRangeSwitch();
    try {
      const [articles, metrics] = await Promise.all([loadSitemap(), loadMetrics()]);
      state.articles = articles;
      state.metrics = metrics;
    } catch (error) {
      nodes.dataStatus.textContent = "异常";
      nodes.dataHint.textContent = "数据读取失败";
    }
    render();
  }

  init();
})();
