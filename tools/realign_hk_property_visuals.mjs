import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const topicRoot = path.join(root, "articles", "hk-mainland-property-inheritance");
const imagesRoot = path.join(topicRoot, "images");

const languages = [
  { suffix: "", imageSuffix: "", locale: "tc" },
  { suffix: "_cn", imageSuffix: "_cn", locale: "cn" },
  { suffix: "_en", imageSuffix: "_en", locale: "en" },
];

function decodeHtml(value) {
  return value
    .replaceAll("&#x27;", "'")
    .replaceAll("&#39;", "'")
    .replaceAll("&quot;", '"')
    .replaceAll("&amp;", "&");
}

function escapeXml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll('"', "&quot;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function wrapChinese(value, width = 24) {
  const chars = [...value];
  const first = chars.slice(0, width).join("");
  const remaining = chars.slice(width);
  if (!remaining.length) return [first];
  const second = remaining.length > width
    ? `${remaining.slice(0, width - 1).join("")}…`
    : remaining.join("");
  return [first, second];
}

function wrapEnglish(value, width = 46) {
  const words = value.split(/\s+/);
  const lines = [""];
  for (const word of words) {
    const candidate = lines.at(-1) ? `${lines.at(-1)} ${word}` : word;
    if (candidate.length <= width || !lines.at(-1)) {
      lines[lines.length - 1] = candidate;
    } else if (lines.length === 1) {
      lines.push(word);
    } else {
      lines[1] = `${lines[1].replace(/…$/, "")}…`;
      break;
    }
  }
  if (lines[1]?.length > width) lines[1] = `${lines[1].slice(0, width - 1).trimEnd()}…`;
  return lines.slice(0, 2);
}

function titleMarkup(title, locale) {
  const lines = locale === "en" ? wrapEnglish(title) : wrapChinese(title);
  return lines.map((line, index) => (
    `<text x="72" y="${168 + index * 48}" text-anchor="start" class="title ink">${escapeXml(line)}</text>`
  )).join("");
}

const visibleTermReplacements = [
  ["資產線索", "房產線索"],
  ["资产线索", "房产线索"],
  [">Assets<", ">Property<"],
  ["內地資產", "內地房產"],
  ["内地资产", "内地房产"],
  ["Mainland Estate", "Mainland Property"],
  ["資產清單不要只寫名", "房產清單不要只寫「"],
  ["资产清单不要只写名", "房产清单不要只写「"],
  [">稱<", ">廣州有房」<"],
  [">称<", ">广州有房」<"],
  ["遺囑用語要和實際資", "遺囑用語要和實際房"],
  ["遗嘱用语要和实际资", "遗嘱用语要和实际房"],
  ["產對照", "產對照"],
  ["产对照", "产对照"],
  ["房產、銀行和訴訟通", "房產查冊、繼承過户"],
  ["房产、银行和诉讼通", "房产查册、继承过户"],
  ["常不要混成一句", "和爭議處理分開"],
  ["常不要混成一句", "和争议处理分开"],
  ["收款安排要單獨確認", "租金或售房款要確認"],
  ["收款安排要单独确认", "租金或售房款要确认"],
  ["Do not compress", "Separate property"],
  ["property, banking…", "search, transfer and…"],
  ["receipt-of-funds…", "rent or sale proceeds…"],
  ["資產要分開，不是所", "先分清房屋狀態，不"],
  ["资产要分开，不是所", "先分清房屋状态，不"],
  ["有東西一個辦法", "是每套房都走同一路"],
  ["有东西一个办法", "是每套房都走同一路"],
  ["可先整理資產，不等", "可先整理房產，不等"],
  ["可先整理资产，不等", "可先整理房产，不等"],
  ["於可先分掉", "於可先完成轉名"],
  ["于可先分掉", "于可先完成转名"],
  ["Asset preservation", "Property records"],
  ["can begin before…", "before transfer…"],
  ["Separate the assets", "Separate each property"],
  ["into workstreams", "by title and use"],
  [">Separate the<", ">Separate each<"],
  [">assets into…<", ">property by use<"],
  ["List the assets", "List the property"],
  ["full asset picture", "full property picture"],
  ["debts and family…", "mortgage and costs…"],
];

let changed = 0;
for (const entry of fs.readdirSync(topicRoot, { withFileTypes: true })) {
  if (!entry.isFile() || !entry.name.endsWith(".html")) continue;
  if (/^(index|bank-deposits|social-security-housing-fund)(?:_cn|_en)?\.html$/.test(entry.name)) continue;
  if (/_cn\.html$|_en\.html$/.test(entry.name)) continue;

  const slug = entry.name.replace(/\.html$/, "");
  const imageDir = path.join(imagesRoot, slug);
  if (!fs.existsSync(imageDir)) continue;

  for (const language of languages) {
    const htmlPath = path.join(topicRoot, `${slug}${language.suffix}.html`);
    const html = fs.readFileSync(htmlPath, "utf8");
    const h1 = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/)?.[1]?.replace(/<[^>]+>/g, "").trim();
    if (!h1) throw new Error(`Missing h1 in ${htmlPath}`);
    const title = decodeHtml(h1);

    for (const imageName of ["01-context", "02-path", "03-checklist"]) {
      const imagePath = path.join(imageDir, `${imageName}${language.imageSuffix}.svg`);
      if (!fs.existsSync(imagePath)) continue;
      let svg = fs.readFileSync(imagePath, "utf8");
      const before = svg;
      svg = svg.replace(/aria-label="[^"]*"/, `aria-label="${escapeXml(title)}"`);
      svg = svg.replace(
        /<text x="72" y="168" text-anchor="start" class="title ink">[\s\S]*?<\/text>(?:<text x="72" y="216" text-anchor="start" class="title ink">[\s\S]*?<\/text>)?/,
        titleMarkup(title, language.locale),
      );
      for (const [from, to] of visibleTermReplacements) svg = svg.split(from).join(to);
      if (language.locale === "cn") svg = svg.replaceAll("和爭議處理分開", "和争议处理分开");
      if (svg !== before) {
        fs.writeFileSync(imagePath, svg, "utf8");
        changed += 1;
      }
    }
  }
}

console.log(`Aligned ${changed} Hong Kong property article visuals.`);
