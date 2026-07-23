import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const articlesRoot = path.join(root, "articles");
const propertyRoot = path.join(articlesRoot, "hk-mainland-property-inheritance");
const otherEstateRoot = path.join(articlesRoot, "hong-kong-other-estate");
const site = "https://www.jingwei-law.com";

const languageFiles = {
  tc: { suffix: "", htmlLang: "zh-Hant" },
  cn: { suffix: "_cn", htmlLang: "zh-Hans" },
  en: { suffix: "_en", htmlLang: "en" },
};

const alignment = {
  "asset-clue-list": {
    tc: ["只知道家人在內地留過房子，香港家屬怎樣整理房產線索", "不知道房產證在哪裏、地址是否改過時，先把房屋位置、登記人、舊票據和現時佔用情況列成一張可查清單。"],
    cn: ["只知道家人在内地留过房子，香港家属怎样整理房产线索", "不知道房产证在哪里、地址是否改过时，先把房屋位置、登记人、旧票据和现在的占用情况列成一张可查清单。"],
    en: ["A Relative Left Property in Mainland China: How a Hong Kong Family Can Organise the Clues", "If the title document is missing or the address may have changed, organise the location, registered owner, old receipts and current occupation into one searchable property list."],
  },
  "document-route-by-purpose": {
    tc: ["香港文件用於內地房產繼承、過户和爭議處理時，為什麼準備方式不同", "同一份香港文件交給房產登記、處理共有份額或解決繼承爭議時，接收目的不同，準備次序也會不同。"],
    cn: ["香港文件用于内地房产继承、过户和争议处理时，为什么准备方式不同", "同一份香港文件交给房产登记、处理共有份额或解决继承争议时，接收目的不同，准备顺序也会不同。"],
    en: ["Why Hong Kong Documents May Need Different Preparation for Mainland Property Transfer and Disputes", "A Hong Kong document may be used for property registration, a co-ownership issue or an inheritance dispute. The receiving purpose changes how the document should be prepared."],
  },
  documents: {
    tc: ["香港死亡證明、親屬關係文件能否用於內地房產繼承過户", "香港家屬要辦內地房產繼承過户時，先分清死亡證明、親屬關係文件、授權書和房屋資料各自要證明甚麼。"],
    cn: ["香港死亡证明、亲属关系文件能否用于内地房产继承过户", "香港家属要办内地房产继承过户时，先分清死亡证明、亲属关系文件、授权书和房屋资料各自要证明什么。"],
    en: ["Can Hong Kong Death and Family Records Be Used for Mainland Property Inheritance and Transfer?", "Before transferring inherited Mainland property, separate what the death record, family records, authorisation and property papers each need to establish."],
  },
  "executor-role-boundary": {
    tc: ["遺囑執行人能否一個人辦完內地遺產房過户", "遺囑寫了執行人，不代表他自然可以單獨查房、確認繼承份額、簽署過户文件或出售房屋。"],
    cn: ["遗嘱执行人能否一个人办完内地遗产房过户", "遗嘱写了执行人，不代表他自然可以单独查房、确认继承份额、签署过户文件或出售房屋。"],
    en: ["Can an Executor Complete a Mainland Inherited Property Transfer Alone?", "Being named executor does not automatically allow one person to trace the property, confirm inheritance shares, sign transfer papers or sell the home alone."],
  },
  "family-relationship-evidence": {
    tc: ["辦內地房產繼承過户，沒有完整親屬關係證明怎麼辦", "房屋過户卡在親屬關係時，不要只找一張所謂完整證明；先把每一段家庭關係和現有舊資料逐項對上。"],
    cn: ["办内地房产继承过户，没有完整亲属关系证明怎么办", "房屋过户卡在亲属关系时，不要只找一张所谓完整证明；先把每一段家庭关系和现有旧资料逐项对上。"],
    en: ["No Complete Family Relationship Record for a Mainland Property Transfer: What Can You Do?", "When an inherited property transfer is held up by family relationship evidence, map each relationship and match it to the older records already available."],
  },
  "family-tree-before-inheritance": {
    tc: ["內地房產繼承人很多又分散，為什麼要先畫家庭關係圖", "內地房產要轉到繼承人名下前，先把可能參與過户的人、現居地、聯絡情況和是否同意畫成一張圖。"],
    cn: ["内地房产继承人很多又分散，为什么要先画家庭关系图", "内地房产要转到继承人名下前，先把可能参与过户的人、现居地、联络情况和是否同意画成一张图。"],
    en: ["Why a Family Tree Helps When Heirs to Mainland Property Live in Different Places", "Before inherited Mainland property can be transferred, map the possible heirs, where they live, whether they can be reached and whether they agree."],
  },
  "first-call-family-facts": {
    tc: ["第一次諮詢香港家屬繼承內地房產，先準備哪五件事", "第一次說明內地房屋繼承問題時，先準備房屋位置、登記人、家屬關係、現有文件和目前卡點。"],
    cn: ["第一次咨询香港家属继承内地房产，先准备哪五件事", "第一次说明内地房屋继承问题时，先准备房屋位置、登记人、家属关系、现有文件和目前卡点。"],
    en: ["First Call About Inheriting Mainland Property: Five Things a Hong Kong Family Should Prepare", "For a first discussion, prepare the property location, registered owner, family relationships, documents already held and the point where the transfer is stuck."],
  },
  "heir-refuses-to-sign": {
    tc: ["內地遺產房過户時家人不肯簽字，先分清反對、拖延還是失聯", "有人不簽房產繼承或過户文件時，先弄清他反對繼承身份、房屋份額、轉名方案，還是只是未收到完整資料。"],
    cn: ["内地遗产房过户时家人不肯签字，先分清反对、拖延还是失联", "有人不签房产继承或过户文件时，先弄清他反对继承身份、房屋份额、转名方案，还是只是未收到完整资料。"],
    en: ["A Relative Will Not Sign a Mainland Property Transfer: Objection, Delay or No Contact?", "When someone will not sign inheritance or transfer papers, identify whether the dispute concerns heirship, the property share, the transfer plan or missing information."],
  },
  "heirs-in-multiple-regions": {
    tc: ["繼承人分散在香港、內地和海外，內地遺產房怎樣辦過户", "多人分散不同地方時，先分清誰要確認房屋份額、誰能簽文件、誰需要授權，以及是否有人明確反對轉名。"],
    cn: ["继承人分散在香港、内地和海外，内地遗产房怎样办过户", "多人分散不同地方时，先分清谁要确认房屋份额、谁能签文件、谁需要授权，以及是否有人明确反对转名。"],
    en: ["Heirs in Hong Kong, Mainland China and Overseas: How Can Inherited Property Be Transferred?", "When heirs live in several places, separate who must confirm the property shares, who can sign, who needs an authorisation and whether anyone opposes the transfer."],
  },
  "hong-kong-death-certificate-details": {
    tc: ["香港死亡證明用於內地房產繼承前，先核對姓名、日期和用途", "死亡證明交給內地房產登記或相關機構前，先核對姓名寫法、死亡日期、房屋登記資料和這次提交的用途。"],
    cn: ["香港死亡证明用于内地房产继承前，先核对姓名、日期和用途", "死亡证明交给内地房产登记或相关机构前，先核对姓名写法、死亡日期、房屋登记资料和这次提交的用途。"],
    en: ["Before Using a Hong Kong Death Certificate for Mainland Property Inheritance, Check These Details", "Before submitting the death certificate for a Mainland property matter, compare the name, date of death, property registration records and the purpose of the submission."],
  },
  "inheritance-without-will": {
    tc: ["沒有遺囑時，香港家屬繼承內地房產先確認哪些人", "沒有遺囑不等於可以直接把房屋平均轉名；先按死亡時間整理家屬範圍，再確認哪些人需要參與房產過户。"],
    cn: ["没有遗嘱时，香港家属继承内地房产先确认哪些人", "没有遗嘱不等于可以直接把房屋平均转名；先按死亡时间整理家属范围，再确认哪些人需要参与房产过户。"],
    en: ["No Will: Which Family Members Must Be Identified Before Mainland Property Can Be Transferred?", "Without a will, do not assume the property can simply be divided equally. Map the family at the date of death and identify who may need to join the transfer."],
  },
  "missing-documents": {
    tc: ["長輩離世多年、房產資料不全，香港繼承人怎樣辦內地過户", "房產證、舊地址或親屬資料不全時，先確認房屋是否仍在、登記在誰名下，以及哪些文件可以逐步補回。"],
    cn: ["长辈离世多年、房产资料不全，香港继承人怎样办内地过户", "房产证、旧地址或亲属资料不全时，先确认房屋是否仍在、登记在谁名下，以及哪些文件可以逐步补回。"],
    en: ["The Owner Died Years Ago and Property Records Are Incomplete: How Can Hong Kong Heirs Start?", "If the title document, old address or family records are incomplete, first confirm whether the property still exists, whose name is registered and which records can be rebuilt."],
  },
  "name-mismatch-across-records": {
    tc: ["辦內地房產過户時，香港證件與舊登記姓名不一致怎麼辦", "香港證件、舊户籍和房屋登記的姓名寫法不同時，先做版本對照，再確認哪一段身份關係需要補證明。"],
    cn: ["办内地房产过户时，香港证件与旧登记姓名不一致怎么办", "香港证件、旧户籍和房屋登记的姓名写法不同时，先做版本对照，再确认哪一段身份关系需要补证明。"],
    en: ["Hong Kong Identity Records and an Old Property Registration Do Not Match: What Next?", "When names differ across Hong Kong identity records, older household records and the property registration, build a version table before deciding what needs to be proved."],
  },
  "old-address-and-id-records": {
    tc: ["內地房屋地址、舊證件號碼和繁簡字不同，繼承過户怎樣核對", "舊房屋地址、證件號碼和姓名寫法已改變時，不要自行統一；先按時間整理每個版本和房屋權屬線索。"],
    cn: ["内地房屋地址、旧证件号码和繁简字不同，继承过户怎样核对", "旧房屋地址、证件号码和姓名写法已改变时，不要自行统一；先按时间整理每个版本和房屋权属线索。"],
    en: ["Old Property Addresses, Identity Numbers and Name Variants: How to Check Them for Transfer", "When an old property address, identity number or name format has changed, preserve each version and place it on a timeline with the ownership records."],
  },
  "remote-authorisation-scope": {
    tc: ["人在香港不回內地，房產繼承過户授權書要寫到多具體", "遠程辦理房屋查冊、繼承確認、過户或出售時，先列清每項任務，再決定授權範圍，避免文件寄到後才補簽。"],
    cn: ["人在香港不回内地，房产继承过户授权书要写到多具体", "远程办理房屋查册、继承确认、过户或出售时，先列清每项任务，再决定授权范围，避免文件寄到后才补签。"],
    en: ["Handling Mainland Property Inheritance From Hong Kong: How Specific Should the Authorisation Be?", "For remote property searches, inheritance confirmation, transfer or sale, list each task before defining the authority so the document does not need to be signed again."],
  },
  "renounce-inheritance": {
    tc: ["香港家屬想放棄內地房產繼承，決定前先看清三件事", "決定不要內地遺產房前，先看房屋價值和欠款、其他繼承人的安排，以及放棄後過户方案是否真的能繼續。"],
    cn: ["香港家属想放弃内地房产继承，决定前先看清三件事", "决定不要内地遗产房前，先看房屋价值和欠款、其他继承人的安排，以及放弃后过户方案是否真的能继续。"],
    en: ["Thinking of Renouncing Inherited Mainland Property? Check Three Things First", "Before giving up an inherited property, check its value and debts, the other heirs' plans and whether the proposed transfer can still proceed afterwards."],
  },
  "unreachable-heir": {
    tc: ["一名繼承人失聯，其他家人能否先辦內地遺產房過户", "有人失聯時，可以先查房屋和整理文件，但不等於可以在沒有處理其繼承份額前直接完成轉名。"],
    cn: ["一名继承人失联，其他家人能否先办内地遗产房过户", "有人失联时，可以先查房屋和整理文件，但不等于可以在没有处理其继承份额前直接完成转名。"],
    en: ["One Heir Cannot Be Found: Can the Family Start a Mainland Property Transfer?", "The family can trace the property and organise documents, but that does not mean the missing heir's possible share can be ignored when completing the transfer."],
  },
  "will-first-review": {
    tc: ["拿遺囑辦內地房產繼承前，先看版本、簽署和房屋範圍", "找到遺囑後，先確認版本和簽署線索，再核對遺囑是否真的涵蓋要過户的那套內地房屋和相應份額。"],
    cn: ["拿遗嘱办内地房产继承前，先看版本、签署和房屋范围", "找到遗嘱后，先确认版本和签署线索，再核对遗嘱是否真的涵盖要过户的那套内地房屋和相应份额。"],
    en: ["Before Using a Will for Mainland Property Inheritance, Check the Version, Signing and Property Scope", "After finding a will, verify its version and signing history, then check whether it actually covers the Mainland property and share that need to be transferred."],
  },
};

const legacyTitleAliases = {
  "asset-clue-list": {
    en: ["How to Build a Searchable Asset Clue List for a Relative's Mainland Estate"],
  },
};

const languageCopy = {
  tc: {
    hubTitle: "香港家屬繼承內地存款、社保等其他遺產",
    hubDescription: "這裏單獨整理不屬於房產過户專題的內地銀行存款、理財、保險、社保、公積金和相關款項問題。",
    eyebrow: "香港其他內地遺產",
    published: "已發布文章",
    ask: "諮詢 AI 法律助手",
    redirectTitle: "文章已移至香港其他內地遺產專題",
    redirectText: "這篇不是房產過户文章，已移到正確的專題。",
    nav: ["香港房產繼承", "澳門專題", "新加坡專題", "美國專題", "諮詢 AI 法律助手"],
    articles: ["親人在內地留下銀行存款、理財或保險，香港家屬先怎麼查", "香港繼承人如何領取內地社保、公積金、撫卹金和相關款項"],
  },
  cn: {
    hubTitle: "香港家属继承内地存款、社保等其他遗产",
    hubDescription: "这里单独整理不属于房产过户专题的内地银行存款、理财、保险、社保、公积金和相关款项问题。",
    eyebrow: "香港其他内地遗产",
    published: "已发布文章",
    ask: "咨询 AI 法律助手",
    redirectTitle: "文章已移至香港其他内地遗产专题",
    redirectText: "这篇不是房产过户文章，已移到正确的专题。",
    nav: ["香港房产继承", "澳门专题", "新加坡专题", "美国专题", "咨询 AI 法律助手"],
    articles: ["亲人在内地留下银行存款、理财或保险，香港家属先怎么查", "香港继承人如何领取内地社保、公积金、抚恤金和相关款项"],
  },
  en: {
    hubTitle: "Other Mainland Estate Assets for Hong Kong Families",
    hubDescription: "This separate collection covers Mainland bank accounts, investments, insurance, social security, housing fund and related payments that do not belong in the property transfer topic.",
    eyebrow: "Other Mainland estate assets",
    published: "Published articles",
    ask: "Ask AI Legal Assistant",
    redirectTitle: "This article has moved to the other Mainland estate assets topic",
    redirectText: "This is not a property transfer article, so it has been moved to the correct collection.",
    nav: ["HK Property Inheritance", "Macau", "Singapore", "United States", "Ask AI Legal Assistant"],
    articles: ["A relative left Mainland bank deposits, investments or insurance: where should a Hong Kong family start?", "How Hong Kong heirs can trace Mainland social security, housing fund and related payments"],
  },
};

function languageFromHtml(html) {
  const match = html.match(/<html\s+lang="([^"]+)"/i);
  if (match?.[1].toLowerCase().startsWith("en")) return "en";
  if (match?.[1].toLowerCase() === "zh-hans") return "cn";
  return "tc";
}

function replaceAllLiteral(text, from, to) {
  return from && from !== to ? text.split(from).join(to) : text;
}

function decodeBasicEntities(text) {
  return text
    .replaceAll("&#x27;", "'")
    .replaceAll("&#39;", "'")
    .replaceAll("&quot;", '"')
    .replaceAll("&amp;", "&");
}

function alignTopicTerms(html, language) {
  const replacements = language === "tc" ? [
    ["文章 / 香港繼承", "香港房產繼承 / 過户與轉名"],
    ["香港繼承總覽", "香港房產繼承總覽"],
    ['"name": "香港繼承"', '"name": "香港房產繼承"'],
    ['"articleSection": "Hong Kong and Mainland inheritance"', '"articleSection": "Hong Kong heirs and Mainland property transfer"'],
    ["房產、存款、社保、公積金、股權或其他資產", "房產、共有份額、按揭、佔用和其他房屋權屬問題"],
    ["房產、銀行和訴訟通常不要混成一句", "房產查冊、繼承過户和爭議處理不要混成一句"],
    ["房產、銀行和訴訟", "房產登記、共有份額和繼承爭議"],
    ["查房、提取存款、出售房屋和分配全部款項", "查房、辦理繼承過户、處理共有份額和後續出售"],
    ["內地資產", "內地房產"],
    ["資產線索", "房產線索"],
    ["查找資產", "查找房產"],
  ] : language === "cn" ? [
    ["文章 / 香港继承", "香港房产继承 / 过户与转名"],
    ["香港继承总览", "香港房产继承总览"],
    ['"name": "香港继承"', '"name": "香港房产继承"'],
    ['"articleSection": "Hong Kong and Mainland inheritance"', '"articleSection": "Hong Kong heirs and Mainland property transfer"'],
    ["房产、存款、社保、公积金、股权或其他资产", "房产、共有份额、按揭、占用和其他房屋权属问题"],
    ["房产、银行和诉讼通常不要混成一句", "房产查册、继承过户和争议处理不要混成一句"],
    ["房产、银行和诉讼", "房产登记、共有份额和继承争议"],
    ["查房、提取存款、出售房屋和分配全部款项", "查房、办理继承过户、处理共有份额和后续出售"],
    ["内地资产", "内地房产"],
    ["资产线索", "房产线索"],
    ["查找资产", "查找房产"],
  ] : [
    ["Articles / Hong Kong inheritance", "Hong Kong property inheritance / Transfer and title change"],
    ["Hong Kong inheritance overview", "Hong Kong property inheritance overview"],
    ['"name": "Hong Kong inheritance"', '"name": "Hong Kong property inheritance"'],
    ['"articleSection": "Hong Kong and Mainland inheritance"', '"articleSection": "Hong Kong heirs and Mainland property transfer"'],
    ["property, bank and litigation", "property registration, co-ownership and inheritance disputes"],
    ["Mainland assets", "Mainland property"],
    ["asset clues", "property clues"],
    ["what Mainland property are known", "which Mainland properties are known"],
    ["tracing assets, preparing documents or addressing a disagreement", "tracing the property, preparing transfer documents or addressing a disagreement"],
  ];
  for (const [from, to] of replacements) html = replaceAllLiteral(html, from, to);
  return html;
}

const titleMaps = { tc: [], cn: [], en: [] };
for (const [slug, copy] of Object.entries(alignment)) {
  for (const [language, config] of Object.entries(languageFiles)) {
    const filePath = path.join(propertyRoot, `${slug}${config.suffix}.html`);
    let html = fs.readFileSync(filePath, "utf8");
    const oldTitle = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/)?.[1]?.replace(/<[^>]+>/g, "").trim();
    const oldDescription = html.match(/<meta\s+name="description"\s+content="([^"]*)"/i)?.[1];
    if (!oldTitle || oldDescription === undefined) throw new Error(`Missing title or description in ${filePath}`);
    const [newTitle, newDescription] = copy[language];
    titleMaps[language].push([oldTitle, newTitle]);
    html = replaceAllLiteral(html, oldTitle, newTitle);
    html = replaceAllLiteral(html, decodeBasicEntities(oldTitle), newTitle);
    for (const alias of legacyTitleAliases[slug]?.[language] || []) {
      html = replaceAllLiteral(html, alias, newTitle);
    }
    html = replaceAllLiteral(html, oldDescription, newDescription);
    html = alignTopicTerms(html, language);
    fs.writeFileSync(filePath, html, "utf8");
  }
}

const publicHtmlFiles = [
  ...fs.readdirSync(propertyRoot).filter((name) => name.endsWith(".html")).map((name) => path.join(propertyRoot, name)),
  path.join(articlesRoot, "index.html"),
  path.join(articlesRoot, "index_cn.html"),
  path.join(articlesRoot, "index_en.html"),
];
for (const filePath of publicHtmlFiles) {
  let html = fs.readFileSync(filePath, "utf8");
  const language = languageFromHtml(html);
  for (const [from, to] of titleMaps[language]) {
    html = replaceAllLiteral(html, from, to);
    html = replaceAllLiteral(html, decodeBasicEntities(from), to);
  }
  if (!/bank-deposits|social-security-housing-fund/.test(path.basename(filePath))) {
    html = alignTopicTerms(html, language);
  }
  fs.writeFileSync(filePath, html, "utf8");
}

function articleAnchor(html, href) {
  const escaped = href.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  return html.match(new RegExp(`<a[^>]*href="${escaped}"[^>]*>[\\s\\S]*?<\\/a>`))?.[0] || "";
}

for (const [language, config] of Object.entries(languageFiles)) {
  const indexName = language === "tc" ? "index.html" : `index_${language}.html`;
  const indexPath = path.join(articlesRoot, indexName);
  let html = fs.readFileSync(indexPath, "utf8");
  const suffix = config.suffix;
  const base = "/articles/hk-mainland-property-inheritance/";
  const bankHref = `${base}bank-deposits${suffix}.html`;
  const socialHref = `${base}social-security-housing-fund${suffix}.html`;
  const transferHref = `${base}property-transfer-checklist${suffix}.html`;
  const certificateHref = `${base}property-certificate-missing${suffix}.html`;
  const bankBlock = articleAnchor(html, bankHref);
  const socialBlock = articleAnchor(html, socialHref);
  const transferBlock = articleAnchor(html, transferHref);
  const certificateBlock = articleAnchor(html, certificateHref);
  if (bankBlock && socialBlock && transferBlock && certificateBlock) {
    html = html.replace(transferBlock, "").replace(certificateBlock, "");
    html = html.replace(bankBlock, transferBlock).replace(socialBlock, certificateBlock);
  }
  for (const [slug, copy] of Object.entries(alignment)) {
    const href = `${base}${slug}${suffix}.html`;
    const block = articleAnchor(html, href);
    if (!block) continue;
    const [title, description] = copy[language];
    const nextBlock = block
      .replace(/(<strong>)[\s\S]*?(<\/strong>)/, `$1${title}$2`)
      .replace(/(<h3>)[\s\S]*?(<\/h3>)/, `$1${title}$2`)
      .replace(/(<p>)[\s\S]*?(<\/p>)/, `$1${description}$2`);
    html = html.replace(block, nextBlock);
  }
  html = html.replace(/(<summary>[^<]*<span>)20(\s*(?:篇|articles)<\/span><\/summary>)/, "$118$2");
  fs.writeFileSync(indexPath, html, "utf8");
}

for (const filePath of fs.readdirSync(propertyRoot).filter((name) => name.endsWith(".html")).map((name) => path.join(propertyRoot, name))) {
  let html = fs.readFileSync(filePath, "utf8");
  if (html.includes("data-article-redirect")) continue;
  const language = languageFromHtml(html);
  const suffix = languageFiles[language].suffix;
  for (const [slug, copy] of Object.entries(alignment)) {
    const href = `/articles/hk-mainland-property-inheritance/${slug}${suffix}.html`;
    const escaped = href.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const linkPattern = new RegExp(`(<a[^>]*href="${escaped}"[^>]*>)([^<]*)(<\\/a>)`, "g");
    html = html.replace(linkPattern, `$1${copy[language][0]}$3`);
  }
  fs.writeFileSync(filePath, html, "utf8");
}

fs.mkdirSync(otherEstateRoot, { recursive: true });
const movedSlugs = ["bank-deposits", "social-security-housing-fund"];
for (const slug of movedSlugs) {
  for (const [language, config] of Object.entries(languageFiles)) {
    const fileName = `${slug}${config.suffix}.html`;
    const oldPath = path.join(propertyRoot, fileName);
    const newPath = path.join(otherEstateRoot, fileName);
    let source = fs.existsSync(newPath) ? fs.readFileSync(newPath, "utf8") : fs.readFileSync(oldPath, "utf8");
    const oldArticlePath = `/articles/hk-mainland-property-inheritance/${slug}`;
    const newArticlePath = `/articles/hong-kong-other-estate/${slug}`;
    source = source.split(oldArticlePath).join(newArticlePath);
    source = source.split("topic=hk-mainland-property-inheritance").join("topic=hong-kong-other-estate");
    source = source.replace(/<a href="\/articles\/" aria-current="page">/, '<a href="/articles/">');
    source = source.replace(/article-hk-inheritance/g, "article-hk-other-estate");
    source = source.replaceAll(`${site}/articles/hk-mainland-property-inheritance/\"`, `${site}/articles/hong-kong-other-estate/\"`);
    source = source.replaceAll('"articleSection": "Hong Kong and Mainland inheritance"', '"articleSection": "Hong Kong families and other Mainland estate assets"');
    source = source.replaceAll('"name": "香港繼承"', '"name": "香港其他內地遺產"');
    source = source.replaceAll('"name": "香港继承"', '"name": "香港其他内地遗产"');
    source = source.replaceAll('"name": "Hong Kong inheritance"', '"name": "Other Mainland estate assets"');
    fs.writeFileSync(newPath, source, "utf8");

    const copy = languageCopy[language];
    const newUrl = `${newArticlePath}${config.suffix}.html`;
    const redirect = `<!doctype html>\n<html lang="${config.htmlLang}" data-article-redirect>\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>${copy.redirectTitle}</title>\n  <meta name="robots" content="noindex,follow">\n  <link rel="canonical" href="${site}${newUrl}">\n  <meta http-equiv="refresh" content="0; url=${newUrl}">\n</head>\n<body>\n  <p>${copy.redirectText} <a href="${newUrl}">${copy.redirectTitle}</a></p>\n</body>\n</html>\n`;
    fs.writeFileSync(oldPath, redirect, "utf8");
  }
}

function otherEstateHub(language) {
  const config = languageFiles[language];
  const copy = languageCopy[language];
  const index = language === "tc" ? 0 : language === "cn" ? 1 : 2;
  const paths = ["/articles/hong-kong-other-estate/", "/articles/hong-kong-other-estate/index_cn.html", "/articles/hong-kong-other-estate/index_en.html"];
  const navPaths = [
    ["/articles/", "/articles/index_cn.html", "/articles/index_en.html"],
    ["/articles/macau/", "/articles/macau/index_cn.html", "/articles/macau/index_en.html"],
    ["/articles/singapore/", "/articles/singapore/index_cn.html", "/articles/singapore/index_en.html"],
    ["/articles/united-states/", "/articles/united-states/index_cn.html", "/articles/united-states/index_en.html"],
  ];
  const languageSwitch = ["tc", "cn", "en"].map((code, itemIndex) => {
    const label = code === "tc" ? "&#32321;" : code === "cn" ? "&#31616;" : "EN";
    return code === language ? `<span aria-current="true">${label}</span>` : `<a href="${paths[itemIndex]}" lang="${languageFiles[code].htmlLang}">${label}</a>`;
  }).join("");
  const nav = navPaths.map((pathSet, itemIndex) => `<a href="${pathSet[index]}">${copy.nav[itemIndex]}</a>`).concat(`<a href="/ask/gpt/?topic=hong-kong-other-estate&amp;source=other-estate-nav">${copy.nav[4]}</a>`).join("\n        ");
  const suffix = config.suffix;
  const articleLinks = movedSlugs.map((slug, itemIndex) => `<a href="/articles/hong-kong-other-estate/${slug}${suffix}.html"><span>${itemIndex + 1 < 10 ? "0" : ""}${itemIndex + 1}</span><strong>${copy.articles[itemIndex]}</strong><small>${copy.hubDescription}</small></a>`).join("\n          ");
  const canonical = `${site}${paths[index]}`;
  const schema = JSON.stringify({ "@context": "https://schema.org", "@type": "CollectionPage", name: copy.hubTitle, description: copy.hubDescription, url: canonical, inLanguage: config.htmlLang, dateModified: "2026-07-23" });
  return `<!doctype html>\n<html lang="${config.htmlLang}">\n<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1">\n  <title>${copy.hubTitle} | ${language === "en" ? "Liu Yi Lawyer Team" : language === "cn" ? "刘毅律师团队" : "劉毅律師團隊"}</title>\n  <meta name="description" content="${copy.hubDescription}">\n  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">\n  <link rel="canonical" href="${canonical}">\n  <link rel="alternate" hreflang="zh-Hant" href="${site}${paths[0]}">\n  <link rel="alternate" hreflang="zh-Hans" href="${site}${paths[1]}">\n  <link rel="alternate" hreflang="en" href="${site}${paths[2]}">\n  <link rel="alternate" hreflang="x-default" href="${site}${paths[0]}">\n  <link rel="stylesheet" href="/articles/style.css">\n  <script type="application/ld+json">${schema}</script>\n</head>\n<body class="articles-hub-v26">\n  <header class="hub-header">\n    <a class="hub-brand" href="${navPaths[0][index]}"><span class="hub-seal">${language === "en" ? "L" : "劉"}</span><span><strong>${language === "en" ? "Liu Yi Lawyer Team" : language === "cn" ? "刘毅律师团队" : "劉毅律師團隊"}</strong><small>${copy.eyebrow}</small></span></a>\n    <nav class="hub-nav" aria-label="${copy.eyebrow}">\n        ${nav}\n    </nav>\n    <div class="article-lang-switch" aria-label="Language switch">${languageSwitch}</div>\n  </header>\n  <main>\n    <section class="hub-hero" aria-labelledby="topic-title"><img src="/articles/articles-index-v24-bg.webp" alt="" width="1800" height="1200"><div class="hub-hero-copy"><p>${copy.eyebrow}</p><h1 id="topic-title">${copy.hubTitle}</h1><span>${copy.hubDescription}</span><time datetime="2026-07-23">2026-07-23</time></div></section>\n    <section class="hub-topic-section" aria-labelledby="published-title"><div class="hub-topic-intro"><p>${copy.eyebrow}</p><h2 id="published-title">${copy.published}</h2><span>${copy.hubDescription}</span><a href="/ask/gpt/?topic=hong-kong-other-estate&amp;source=other-estate-hub">${copy.ask}</a></div><div class="hub-article-list hub-article-list-short">\n          ${articleLinks}\n        </div></section>\n  </main>\n</body>\n</html>\n`;
}

for (const language of Object.keys(languageFiles)) {
  const fileName = language === "tc" ? "index.html" : `index_${language}.html`;
  fs.writeFileSync(path.join(otherEstateRoot, fileName), otherEstateHub(language), "utf8");
}

let sitemap = fs.readFileSync(path.join(root, "sitemap.xml"), "utf8");
for (const slug of movedSlugs) {
  sitemap = sitemap.split(`${site}/articles/hk-mainland-property-inheritance/${slug}`).join(`${site}/articles/hong-kong-other-estate/${slug}`);
}
if (!sitemap.includes(`${site}/articles/hong-kong-other-estate/</loc>`)) {
  const insertion = `  <url>\n    <loc>${site}/articles/hong-kong-other-estate/</loc>\n    <lastmod>2026-07-23</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.5</priority>\n  </url>\n  <url>\n    <loc>${site}/articles/hong-kong-other-estate/index_cn.html</loc>\n    <lastmod>2026-07-23</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.4</priority>\n  </url>\n  <url>\n    <loc>${site}/articles/hong-kong-other-estate/index_en.html</loc>\n    <lastmod>2026-07-23</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.4</priority>\n  </url>\n`;
  sitemap = sitemap.replace("</urlset>", `${insertion}</urlset>`);
}
fs.writeFileSync(path.join(root, "sitemap.xml"), sitemap, "utf8");

console.log(`Aligned ${Object.keys(alignment).length * 3} property article pages and moved 6 non-property language pages.`);
