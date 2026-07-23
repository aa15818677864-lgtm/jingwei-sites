import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const articlesRoot = path.join(root, "articles");

const navigation = {
  "zh-Hant": [
    ["/articles/", "香港專題", "hong-kong"],
    ["/articles/macau/", "澳門專題", "macau"],
    ["/articles/singapore/", "新加坡專題", "singapore"],
    ["/articles/united-states/", "美國專題", "united-states"],
    ["/ask/gpt/?topic=articles&amp;source=article-nav", "諮詢 AI 法律助手", "assistant"],
  ],
  "zh-Hans": [
    ["/articles/index_cn.html", "香港专题", "hong-kong"],
    ["/articles/macau/index_cn.html", "澳门专题", "macau"],
    ["/articles/singapore/index_cn.html", "新加坡专题", "singapore"],
    ["/articles/united-states/index_cn.html", "美国专题", "united-states"],
    ["/ask/gpt/?topic=articles&amp;source=article-nav", "咨询 AI 法律助手", "assistant"],
  ],
  en: [
    ["/articles/index_en.html", "Hong Kong", "hong-kong"],
    ["/articles/macau/index_en.html", "Macau", "macau"],
    ["/articles/singapore/index_en.html", "Singapore", "singapore"],
    ["/articles/united-states/index_en.html", "United States", "united-states"],
    ["/ask/gpt/?topic=articles&amp;source=article-nav", "Ask AI Legal Assistant", "assistant"],
  ],
};

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const fullPath = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(fullPath) : [fullPath];
  });
}

function languageFor(html) {
  const match = html.match(/<html\s+lang="([^"]+)"/i);
  if (match?.[1].toLowerCase().startsWith("en")) return "en";
  if (match?.[1].toLowerCase() === "zh-hans") return "zh-Hans";
  return "zh-Hant";
}

function topicFor(relativePath) {
  const normalized = relativePath.replaceAll("\\", "/");
  if (normalized.startsWith("hk-mainland-property-inheritance/")) return "hong-kong";
  if (normalized.startsWith("am/")) return "macau";
  if (normalized.startsWith("us/")) return "united-states";
  return null;
}

let updated = 0;
for (const filePath of walk(articlesRoot)) {
  if (!filePath.endsWith(".html")) continue;
  const html = fs.readFileSync(filePath, "utf8");
  if (!html.includes('class="nav-links"')) continue;

  const relativePath = path.relative(articlesRoot, filePath);
  const language = languageFor(html);
  const currentTopic = topicFor(relativePath);
  const links = navigation[language]
    .map(([href, label, topic]) => {
      const current = topic === currentTopic ? ' aria-current="page"' : "";
      return `        <a href="${href}"${current}>${label}</a>`;
    })
    .join("\n");
  const replacement = `<div class="nav-links">\n${links}\n      </div>`;
  const next = html.replace(/<div class="nav-links">[\s\S]*?<\/div>/, replacement);
  if (next === html) throw new Error(`Could not update navigation in ${relativePath}`);
  fs.writeFileSync(filePath, next, "utf8");
  updated += 1;
}

console.log(`Updated ${updated} article navigation blocks.`);
