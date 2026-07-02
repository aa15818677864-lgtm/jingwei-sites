import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const site = "https://www.jingwei-law.com/";
const skipDirs = new Set([".git", ".github", "_root_site_preview", "preview", "webfonts", "webp_images_package", "node_modules"]);
const auditAll = process.argv.includes("--all");
const defaultPublicDirs = ["articles", "topics"];

function walk(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isDirectory()) {
      if (!skipDirs.has(entry.name)) walk(path.join(dir, entry.name), out);
      continue;
    }
    if (entry.name.endsWith(".html")) out.push(path.join(dir, entry.name));
  }
  return out;
}

function strip(html = "") {
  return html.replace(/<[^>]*>/g, "").replace(/\s+/g, " ").trim();
}

function attr(html, selectorName, attrName = "name") {
  const patterns = [
    new RegExp(`<meta\\s+${attrName}=["']${selectorName}["']\\s+content=["']([^"']*)["']`, "i"),
    new RegExp(`<meta\\s+content=["']([^"']*)["']\\s+${attrName}=["']${selectorName}["']`, "i"),
  ];
  for (const pattern of patterns) {
    const match = html.match(pattern);
    if (match) return match[1].trim();
  }
  return "";
}

function canonicalFromRel(rel) {
  let url = rel.replace(/\\/g, "/");
  if (url.endsWith("/index.html")) url = url.slice(0, -"index.html".length);
  return new URL(url, site).href;
}

const sitemapPath = path.join(root, "sitemap.xml");
const sitemap = fs.existsSync(sitemapPath) ? fs.readFileSync(sitemapPath, "utf8") : "";
const sitemapUrls = new Set([...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]));

const publicFiles = (auditAll ? walk(root) : defaultPublicDirs.flatMap((dir) => walk(path.join(root, dir))))
  .map((file) => path.relative(root, file))
  .filter((rel) => !rel.startsWith("tools/"));

const issues = [];
const canonicals = new Map();

for (const rel of publicFiles) {
  const file = path.join(root, rel);
  const html = fs.readFileSync(file, "utf8");
  const title = strip((html.match(/<title[^>]*>([\s\S]*?)<\/title>/i) || [])[1]);
  const description = attr(html, "description");
  const canonical = (html.match(/<link\s+rel=["']canonical["']\s+href=["']([^"']*)["']/i) || html.match(/<link\s+href=["']([^"']*)["']\s+rel=["']canonical["']/i) || [])[1] || "";
  const h1 = strip((html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i) || [])[1]);
  const robots = attr(html, "robots");
  const ogTitle = attr(html, "og:title", "property");
  const ogDescription = attr(html, "og:description", "property");
  const ogUrl = attr(html, "og:url", "property");
  const ogType = attr(html, "og:type", "property");
  const ogImage = attr(html, "og:image", "property");
  const twitterCard = attr(html, "twitter:card");
  const twitterTitle = attr(html, "twitter:title");
  const twitterDescription = attr(html, "twitter:description");
  const noindex = /<meta\s+name=["']robots["'][^>]*content=["'][^"']*noindex/i.test(html);
  const jsonBlocks = [...html.matchAll(/<script\s+type=["']application\/ld\+json["'][^>]*>([\s\S]*?)<\/script>/gi)];
  const jsonLdTypes = [];

  if (!title) issues.push(`${rel}: missing <title>`);
  if (!description) issues.push(`${rel}: missing meta description`);
  if (!canonical) issues.push(`${rel}: missing canonical`);
  if (!h1) issues.push(`${rel}: missing h1`);
  if (!robots) issues.push(`${rel}: missing meta robots`);
  if (!ogTitle) issues.push(`${rel}: missing og:title`);
  if (!ogDescription) issues.push(`${rel}: missing og:description`);
  if (!ogUrl) issues.push(`${rel}: missing og:url`);
  if (!ogType) issues.push(`${rel}: missing og:type`);
  if (!ogImage) issues.push(`${rel}: missing og:image`);
  if (!twitterCard) issues.push(`${rel}: missing twitter:card`);
  if (!twitterTitle) issues.push(`${rel}: missing twitter:title`);
  if (!twitterDescription) issues.push(`${rel}: missing twitter:description`);
  if (noindex) issues.push(`${rel}: has noindex`);
  if (canonical && ogUrl && canonical !== ogUrl) issues.push(`${rel}: canonical and og:url do not match`);
  if (description && ogDescription && description !== ogDescription) issues.push(`${rel}: description and og:description do not match`);

  for (const [idx, block] of jsonBlocks.entries()) {
    try {
      const parsed = JSON.parse(block[1]);
      if (Array.isArray(parsed?.["@graph"])) {
        for (const item of parsed["@graph"]) {
          if (item?.["@type"]) jsonLdTypes.push(item["@type"]);
        }
      } else if (parsed?.["@type"]) {
        jsonLdTypes.push(parsed["@type"]);
      }
    } catch (error) {
      issues.push(`${rel}: invalid JSON-LD #${idx + 1}: ${error.message}`);
    }
  }

  if (rel === "articles/index.html") {
    for (const requiredType of ["CollectionPage", "ItemList", "BreadcrumbList"]) {
      if (!jsonLdTypes.includes(requiredType)) issues.push(`${rel}: missing JSON-LD type ${requiredType}`);
    }
  } else if (rel.startsWith("articles/")) {
    for (const requiredType of ["Article", "BreadcrumbList"]) {
      if (!jsonLdTypes.includes(requiredType)) issues.push(`${rel}: missing JSON-LD type ${requiredType}`);
    }
  } else if (rel.startsWith("topics/")) {
    for (const requiredType of ["LegalService", "BreadcrumbList"]) {
      if (!jsonLdTypes.includes(requiredType)) issues.push(`${rel}: missing JSON-LD type ${requiredType}`);
    }
  }

  if (canonical) {
    if (canonicals.has(canonical)) issues.push(`${rel}: duplicate canonical also used by ${canonicals.get(canonical)}`);
    canonicals.set(canonical, rel);
    if (!sitemapUrls.has(canonical) && !rel.startsWith("google")) issues.push(`${rel}: canonical missing from sitemap (${canonical})`);
  } else {
    const expected = canonicalFromRel(rel);
    if (!sitemapUrls.has(expected)) issues.push(`${rel}: expected URL missing from sitemap (${expected})`);
  }
}

if (issues.length) {
  console.log(`SEO audit found ${issues.length} issue(s):`);
  for (const issue of issues) console.log(`- ${issue}`);
  process.exitCode = 1;
} else {
  console.log(`SEO audit passed: ${publicFiles.length} HTML file(s), ${sitemapUrls.size} sitemap URL(s).`);
}
