const BASE_URL = process.env.BASE_URL || "https://www.jingwei-law.com";
const API_BASE_URL = process.env.API_BASE_URL || "https://api.jingwei-law.com";
const SUBMIT_RELAY_URL = process.env.SUBMIT_RELAY_URL || "https://submit.jingwei-law.com/submit.php";
const RETRIES = Number(process.env.VERIFY_RETRIES || 4);
const RETRY_DELAY_MS = Number(process.env.VERIFY_RETRY_DELAY_MS || 7000);
const TIMEOUT_MS = Number(process.env.VERIFY_TIMEOUT_MS || 18000);

const protectedPages = [
  { label: "首页", path: "/", mustContain: "contactForm" },
  { label: "马来西亚中文", path: "/ml/index_cn.html", mustContain: "contactForm" },
  { label: "马来西亚英文", path: "/ml/index_en.html", mustContain: "contactForm" },
  { label: "新加坡中文", path: "/xj/index_cn.html", mustContain: "contactForm" },
  { label: "新加坡英文", path: "/xj/index_en.html", mustContain: "contactForm" },
  { label: "美国华人中文", path: "/us/index_cn.html", mustContain: "contactForm" },
  { label: "美国华人英文", path: "/us/index_en.html", mustContain: "contactForm" },
  { label: "美国华人繁体", path: "/us/index_tc.html", mustContain: "contactForm" },
  { label: "纯美国英文", path: "/us/index_us.html", mustContain: "contactForm" },
  { label: "纯美国中文参考", path: "/us/index_us_cn.html", mustContain: "contactForm" },
  { label: "澳门繁体", path: "/am/index_tc.html", mustContain: "contactForm" },
  { label: "澳门简体", path: "/am/index_cn.html", mustContain: "contactForm" }
];

const seoPages = [
  { label: "文章库", path: "/articles/", mustContain: "跨境中国法律事务文章库" },
  { label: "香港继承文章", path: "/articles/hk-mainland-property-inheritance/", mustContain: "香港居民继承内地房产过户" },
  { label: "香港继承专题表单页", path: "/topics/hk-mainland-property-inheritance/", mustContain: "contactForm" },
  { label: "AI 问答页", path: "/ask/?topic=hk-mainland-property-inheritance&source=verify-live&intent=general", mustContain: "routeAd" },
  { label: "站点地图", path: "/sitemap.xml", mustContain: "/topics/hk-mainland-property-inheritance/" },
  { label: "站点配置", path: "/site-config.js", mustContain: "submit.jingwei-law.com/submit.php" }
];

const backendChecks = [
  { label: "AI API 健康检查", url: `${API_BASE_URL}/healthz`, method: "GET", okStatuses: [200] },
  { label: "表单中转接口预检", url: SUBMIT_RELAY_URL, method: "OPTIONS", okStatuses: [200, 204, 405] }
];

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function absoluteUrl(path) {
  return path.startsWith("http") ? path : new URL(path, BASE_URL).toString();
}

async function fetchWithTimeout(url, options = {}) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
  try {
    return await fetch(url, { ...options, signal: controller.signal, redirect: "follow" });
  } finally {
    clearTimeout(timer);
  }
}

async function checkUrl(check) {
  const url = check.url || absoluteUrl(check.path);
  const okStatuses = check.okStatuses || [200];
  let lastError = "";

  for (let attempt = 1; attempt <= RETRIES; attempt += 1) {
    try {
      const response = await fetchWithTimeout(url, { method: check.method || "GET" });
      const statusOk = okStatuses.includes(response.status);
      const text = check.method === "OPTIONS" ? "" : await response.text();
      const bodyOk = !check.mustContain || text.includes(check.mustContain);

      if (statusOk && bodyOk) {
        return { ...check, url, status: response.status, ok: true, attempt };
      }

      lastError = `status=${response.status}${bodyOk ? "" : " missing=" + check.mustContain}`;
    } catch (error) {
      lastError = error && error.name === "AbortError" ? "timeout" : String(error && error.message ? error.message : error);
    }

    if (attempt < RETRIES) await sleep(RETRY_DELAY_MS);
  }

  return { ...check, url, ok: false, error: lastError };
}

async function main() {
  const checks = [...protectedPages, ...seoPages, ...backendChecks];
  const results = [];

  for (const check of checks) {
    const result = await checkUrl(check);
    results.push(result);
    const status = result.ok ? "OK" : "FAIL";
    const detail = result.ok ? `status=${result.status}` : result.error;
    console.log(`${status.padEnd(4)} ${check.label} ${detail} ${result.url}`);
  }

  const failures = results.filter((result) => !result.ok);
  console.log(`\nChecked ${results.length} URLs. Failures: ${failures.length}.`);

  if (failures.length) {
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
