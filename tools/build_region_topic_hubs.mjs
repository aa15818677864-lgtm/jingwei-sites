import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const updated = "2026-07-23";

const languages = {
  tc: {
    htmlLang: "zh-Hant",
    suffix: "",
    brand: "劉毅律師團隊",
    brandNote: "跨境中國法律事務文章庫",
    nav: ["香港專題", "澳門專題", "新加坡專題", "美國專題", "諮詢 AI 法律助手"],
    navLabel: "文章區主導航",
    eyebrow: "跨境法律事務專題",
    overview: "先看總覽",
    published: "已發布文章",
    questions: "常見問題",
    ask: "諮詢 AI 法律助手",
    articleHeading: "從已發布文章開始",
    empty: "這個專題仍在整理。正式文章完成研究、審閱和三語改寫後才會在這裏出現。",
    more: "展開看看接下來會整理的問題",
    nextEyebrow: "仍不確定從哪裏開始",
    nextTitle: "把所在地、事情發生地和手上文件說清楚，再判斷下一步。",
    updatedLabel: "最後整理",
  },
  cn: {
    htmlLang: "zh-Hans",
    suffix: "index_cn.html",
    brand: "刘毅律师团队",
    brandNote: "跨境中国法律事务文章库",
    nav: ["香港专题", "澳门专题", "新加坡专题", "美国专题", "咨询 AI 法律助手"],
    navLabel: "文章区主导航",
    eyebrow: "跨境法律事务专题",
    overview: "先看总览",
    published: "已发布文章",
    questions: "常见问题",
    ask: "咨询 AI 法律助手",
    articleHeading: "从已发布文章开始",
    empty: "这个专题仍在整理。正式文章完成研究、审阅和三语改写后才会在这里出现。",
    more: "展开看看接下来会整理的问题",
    nextEyebrow: "仍不确定从哪里开始",
    nextTitle: "把所在地、事情发生地和手上文件说清楚，再判断下一步。",
    updatedLabel: "最后整理",
  },
  en: {
    htmlLang: "en",
    suffix: "index_en.html",
    brand: "Liu Yi Lawyer Team",
    brandNote: "Cross-border Mainland China legal articles",
    nav: ["Hong Kong", "Macau", "Singapore", "United States", "Ask AI Legal Assistant"],
    navLabel: "Article topic navigation",
    eyebrow: "Cross-border legal topic",
    overview: "Overview",
    published: "Published articles",
    questions: "Common questions",
    ask: "Ask AI Legal Assistant",
    articleHeading: "Start with a published article",
    empty: "This topic is still being prepared. Articles appear here only after research, editorial review and human-quality multilingual rewriting are complete.",
    more: "See the questions we are preparing next",
    nextEyebrow: "Not sure where to begin",
    nextTitle: "Describe where you are, where the matter arose and which documents you have, then work out the next step.",
    updatedLabel: "Last reviewed",
  },
};

const topics = {
  macau: {
    paths: ["/articles/macau/", "/articles/macau/index_cn.html", "/articles/macau/index_en.html"],
    names: ["澳門專題", "澳门专题", "Macau"],
    titles: [
      "人在澳門，要處理內地法律事務先從哪裏開始",
      "人在澳门，要处理内地法律事务先从哪里开始",
      "Handling a Mainland China legal matter from Macau",
    ],
    descriptions: [
      "先分清事情發生在哪裏、對方或資產在哪裏，以及手上的澳門文件能說明甚麼。把這三件事說清楚，才容易判斷要查資料、準備授權，還是先處理爭議。",
      "先分清事情发生在哪里、对方或资产在哪里，以及手上的澳门文件能说明什么。把这三件事说清楚，才容易判断要查资料、准备授权，还是先处理争议。",
      "Start by separating three things: where the matter arose, where the other party or asset is located, and what your Macau documents actually establish. That makes it easier to decide whether to investigate, prepare an authorisation or address a dispute first.",
    ],
    summaries: [
      "這裏會按委託、文件、資產和爭議四條線整理澳門居民常見的內地法律問題。",
      "这里会按委托、文件、资产和争议四条线整理澳门居民常见的内地法律问题。",
      "This topic organises common questions from Macau residents around instructions, documents, assets and disputes.",
    ],
    article: {
      href: "/articles/am/macau-client-mainland-lawyer.html",
      labels: ["委託起步", "委托起步", "Getting started"],
      titles: ["澳門客戶如何委託內地律師處理內地法律事務", "澳门客户如何委托内地律师处理内地法律事务", "How Macau clients can instruct a Mainland lawyer"],
      notes: ["繁體中文文章：先整理事實、文件和希望處理的結果。", "繁体中文文章：先整理事实、文件和希望处理的结果。", "Traditional Chinese article covering facts, documents and the outcome you need."],
    },
    questions: [
      ["澳門文件交到內地前要先核對甚麼", "澳门文件交到内地前要先核对什么", "What to check before using Macau documents in Mainland China"],
      ["人不回內地時，授權範圍怎樣寫", "人不回内地时，授权范围怎样写", "How to define an authorisation when you cannot travel"],
      ["內地房產、存款或公司資料從哪裏查", "内地房产、存款或公司资料从哪里查", "Where to begin tracing Mainland property, accounts or company records"],
      ["對方不配合時，先留哪些證據", "对方不配合时，先留哪些证据", "Which evidence to preserve when the other side will not cooperate"],
    ],
  },
  singapore: {
    paths: ["/articles/singapore/", "/articles/singapore/index_cn.html", "/articles/singapore/index_en.html"],
    names: ["新加坡專題", "新加坡专题", "Singapore"],
    titles: [
      "人在新加坡，處理內地法律事務先把三個地方說清楚",
      "人在新加坡，处理内地法律事务先把三个地方说清楚",
      "Handling a Mainland China legal matter from Singapore",
    ],
    descriptions: [
      "你人在哪裏、事情在哪裏發生、對方或資產在哪裏，往往會影響文件、溝通和處理順序。這個專題會先回答最常見的遠程委託和資料整理問題。",
      "你人在哪里、事情在哪里发生、对方或资产在哪里，往往会影响文件、沟通和处理顺序。这个专题会先回答最常见的远程委托和资料整理问题。",
      "Where you are, where the events occurred and where the other party or asset is located can change the document and communication path. This topic begins with the practical questions that arise when handling a matter remotely from Singapore.",
    ],
    summaries: [
      "正式文章正在按讀者最常問的遠程委託、身份文件、資產線索和爭議處理問題整理。",
      "正式文章正在按读者最常问的远程委托、身份文件、资产线索和争议处理问题整理。",
      "Articles are being developed around remote instructions, identity documents, asset clues and dispute handling.",
    ],
    article: null,
    questions: [
      ["第一次諮詢要先準備哪些基本事實", "第一次咨询要先准备哪些基本事实", "Which facts to prepare for a first consultation"],
      ["新加坡文件用於內地事務時先看甚麼", "新加坡文件用于内地事务时先看什么", "What to check before using Singapore documents in Mainland China"],
      ["不能回內地時，委託和簽署怎樣安排", "不能回内地时，委托和签署怎样安排", "How to arrange instructions and signing without travelling"],
      ["內地資產只有零散線索時怎樣開始查", "内地资产只有零散线索时怎样开始查", "How to start when you only have fragments of information about an asset"],
    ],
  },
  "united-states": {
    paths: ["/articles/united-states/", "/articles/united-states/index_cn.html", "/articles/united-states/index_en.html"],
    names: ["美國專題", "美国专题", "United States"],
    titles: [
      "人在美國，怎樣遠程處理內地法律事務",
      "人在美国，怎样远程处理内地法律事务",
      "Handling a Mainland China legal matter from the United States",
    ],
    descriptions: [
      "跨時區和無法到場通常不是第一個難點。先把當事人、事情發生地、資產位置和現有文件整理清楚，才知道哪些可以遠程推進，哪些需要在內地核實。",
      "跨时区和无法到场通常不是第一个难点。先把当事人、事情发生地、资产位置和现有文件整理清楚，才知道哪些可以远程推进，哪些需要在内地核实。",
      "Time zones and travel are rarely the first issue to solve. Begin by organising the people involved, where the events and assets are located, and which documents exist, then separate what can be progressed remotely from what needs checking in Mainland China.",
    ],
    summaries: [
      "這裏會整理遠程委託、身份與簽署文件、內地資產和家事爭議等常見問題。",
      "这里会整理远程委托、身份与签署文件、内地资产和家事争议等常见问题。",
      "This topic covers remote instructions, identity and signing documents, Mainland assets and family disputes.",
    ],
    article: {
      href: "/articles/us/remote-china-lawyer.html",
      labels: ["遠程委託", "远程委托", "Remote instructions"],
      titles: ["人在美國如何委託內地律師處理內地法律事務", "人在美国如何委托内地律师处理内地法律事务", "How U.S.-based clients can instruct a Mainland lawyer"],
      notes: ["簡體中文文章：先整理事實，再判斷溝通、授權和辦理順序。", "简体中文文章：先整理事实，再判断沟通、授权和办理顺序。", "Simplified Chinese article on facts, communication, authorisation and sequence."],
    },
    questions: [
      ["第一次跨時區諮詢怎樣把事情說清楚", "第一次跨时区咨询怎样把事情说清楚", "How to explain the matter clearly across time zones"],
      ["美國文件用於內地事務時先核對哪些細節", "美国文件用于内地事务时先核对哪些细节", "What to check before using U.S. documents in Mainland China"],
      ["內地房產或存款只有舊線索時怎樣查", "内地房产或存款只有旧线索时怎样查", "How to trace a Mainland property or account from old clues"],
      ["家人分散多地時，誰先整理文件和決定", "家人分散多地时，谁先整理文件和决定", "Who should organise documents and decisions when family members are dispersed"],
    ],
  },
};

const navPaths = [
  ["/articles/", "/articles/index_cn.html", "/articles/index_en.html"],
  topics.macau.paths,
  topics.singapore.paths,
  topics["united-states"].paths,
];

function languageIndex(code) {
  return code === "tc" ? 0 : code === "cn" ? 1 : 2;
}

function languageSwitch(topic, activeCode) {
  return ["tc", "cn", "en"]
    .map((code, index) => {
      const label = code === "tc" ? "&#32321;" : code === "cn" ? "&#31616;" : "EN";
      if (code === activeCode) return `<span aria-current="true">${label}</span>`;
      return `<a href="${topic.paths[index]}" lang="${languages[code].htmlLang}">${label}</a>`;
    })
    .join("");
}

function render(topicKey, topic, code) {
  const lang = languages[code];
  const index = languageIndex(code);
  const pageUrl = `https://www.jingwei-law.com${topic.paths[index]}`;
  const canonical = pageUrl;
  const askHref = `/ask/gpt/?topic=${topicKey}&amp;source=article-topic-hub`;
  const nav = navPaths
    .map((paths, navIndex) => {
      const current = navIndex === indexForTopic(topicKey) ? ' aria-current="page"' : "";
      return `<a href="${paths[index]}"${current}>${lang.nav[navIndex]}</a>`;
    })
    .concat(`<a href="/ask/gpt/?topic=articles&amp;source=article-topic-nav">${lang.nav[4]}</a>`)
    .join("\n        ");
  const articleMarkup = topic.article
    ? `<div class="hub-article-list hub-article-list-short">
          <a href="${topic.article.href}">
            <span>${topic.article.labels[index]}</span>
            <strong>${topic.article.titles[index]}</strong>
            <small>${topic.article.notes[index]}</small>
          </a>
        </div>`
    : `<div class="hub-empty">${lang.empty}</div>`;
  const upcoming = topic.questions.map((question) => `<span>${question[index]}</span>`).join("\n          ");
  const schema = JSON.stringify({
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    name: topic.titles[index],
    description: topic.descriptions[index],
    url: pageUrl,
    inLanguage: lang.htmlLang,
    isPartOf: { "@type": "WebSite", name: lang.brand, url: "https://www.jingwei-law.com/articles/" },
    dateModified: updated,
  });

  return `<!doctype html>
<html lang="${lang.htmlLang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${topic.titles[index]} | ${lang.brand}</title>
  <meta name="description" content="${topic.descriptions[index]}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <link rel="canonical" href="${canonical}">
  <link rel="alternate" hreflang="zh-Hant" href="https://www.jingwei-law.com${topic.paths[0]}">
  <link rel="alternate" hreflang="zh-Hans" href="https://www.jingwei-law.com${topic.paths[1]}">
  <link rel="alternate" hreflang="en" href="https://www.jingwei-law.com${topic.paths[2]}">
  <link rel="alternate" hreflang="x-default" href="https://www.jingwei-law.com${topic.paths[0]}">
  <link rel="stylesheet" href="/articles/style.css">
  <script type="application/ld+json">${schema}</script>
</head>
<body class="articles-hub-v26">
  <header class="hub-header">
    <a class="hub-brand" href="${navPaths[0][index]}">
      <span class="hub-seal">${code === "en" ? "L" : "劉"}</span>
      <span><strong>${lang.brand}</strong><small>${lang.brandNote}</small></span>
    </a>
    <nav class="hub-nav" aria-label="${lang.navLabel}">
        ${nav}
    </nav>
    <div class="article-lang-switch" aria-label="Language switch">${languageSwitch(topic, code)}</div>
  </header>
  <main>
    <section class="hub-hero" id="overview" aria-labelledby="topic-title">
      <img src="/articles/articles-index-v24-bg.webp" alt="" width="1800" height="1200">
      <div class="hub-hero-copy">
        <p>${lang.eyebrow} / ${topic.names[index]}</p>
        <h1 id="topic-title">${topic.titles[index]}</h1>
        <span>${topic.descriptions[index]}</span>
        <time datetime="${updated}">${lang.updatedLabel}：${updated}</time>
      </div>
    </section>

    <nav class="hub-topic-nav" aria-label="${topic.names[index]}">
      <a href="#overview"><strong>${lang.overview}</strong><span>${topic.summaries[index]}</span></a>
      <a href="#published"><strong>${lang.published}</strong><span>${topic.article ? topic.article.titles[index] : lang.empty}</span></a>
      <a href="#questions"><strong>${lang.questions}</strong><span>${topic.questions[0][index]}</span></a>
      <a href="${askHref}"><strong>${lang.ask}</strong><span>${lang.nextTitle}</span></a>
    </nav>

    <section class="hub-topic-section" id="published" aria-labelledby="published-title">
      <div class="hub-topic-intro">
        <p>${topic.names[index]}</p>
        <h2 id="published-title">${lang.articleHeading}</h2>
        <span>${topic.summaries[index]}</span>
        <a href="${askHref}">${lang.ask}</a>
      </div>
      ${articleMarkup}
    </section>

    <details class="hub-more" id="questions">
      <summary>${lang.more}</summary>
      <div class="hub-upcoming">
          ${upcoming}
      </div>
    </details>

    <section class="hub-next-step">
      <div><p>${lang.nextEyebrow}</p><h2>${lang.nextTitle}</h2></div>
      <a href="${askHref}">${lang.ask}</a>
    </section>
  </main>
</body>
</html>
`;
}

function indexForTopic(topicKey) {
  return topicKey === "macau" ? 1 : topicKey === "singapore" ? 2 : 3;
}

for (const [topicKey, topic] of Object.entries(topics)) {
  const directory = path.join(root, "articles", topicKey);
  fs.mkdirSync(directory, { recursive: true });
  for (const code of ["tc", "cn", "en"]) {
    const fileName = languages[code].suffix || "index.html";
    fs.writeFileSync(path.join(directory, fileName), render(topicKey, topic, code), "utf8");
  }
}

console.log("Built 9 regional topic hub pages.");
