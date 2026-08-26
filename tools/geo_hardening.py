from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "articles"
SITE = "https://www.jingwei-law.com"
GEO_PATH = ROOT / "dashboard" / "geo.json"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_redirect_article(text: str) -> bool:
    return "data-article-redirect" in text


def write(path: Path, value: str) -> None:
    path.write_text(value, encoding="utf-8", newline="\n")


def public_path(path: Path) -> str:
    return "/" + path.relative_to(ROOT).as_posix()


def locale_paths(cn_path: Path) -> dict[str, str]:
    rel = public_path(cn_path)
    if rel.endswith("/index_cn.html"):
        trad = rel[: -len("index_cn.html")]
        english = rel[: -len("index_cn.html")] + "index_en.html"
    else:
        trad = rel.replace("_cn.html", ".html")
        english = rel.replace("_cn.html", "_en.html")
    return {"zh-Hant": trad, "zh-Hans": rel, "en": english, "x-default": trad}


def fix_cn_hreflang() -> int:
    count = 0
    pattern = re.compile(r'\s*<link rel="alternate" hreflang="(?:zh-Hant|zh-Hans|en|x-default)" href="[^"]+">')
    for path in sorted(ARTICLES.rglob("*_cn.html")):
        text = read(path)
        if is_redirect_article(text):
            continue
        paths = locale_paths(path)
        replacement = "\n" + "\n".join(
            f'  <link rel="alternate" hreflang="{locale}" href="{SITE}{target}">'
            for locale, target in paths.items()
        )
        text, changed = pattern.subn("", text)
        canonical = re.search(r'(<link rel="canonical" href="[^"]+">)', text)
        if not canonical:
            raise ValueError(f"No canonical link in {path}")
        insertion = canonical.group(1) + replacement
        text = text[: canonical.start()] + insertion + text[canonical.end() :]
        write(path, text)
        count += 1 if changed else 0
    return count


def add_author_urls() -> int:
    changed_files = 0
    author_pattern = re.compile(r'("author"\s*:\s*\{)([^{}]*)(\})', re.S)
    for path in sorted(ARTICLES.rglob("*.html")):
        if re.search(r"(^|/)index(?:_cn|_en)?\.html$", public_path(path)):
            continue
        text = read(path)
        if is_redirect_article(text):
            continue

        def patch_author(match: re.Match[str]) -> str:
            body = match.group(2)
            if '"url"' in body:
                return match.group(0)
            trailing = "\n    " if "\n" in body else " "
            body = body.rstrip()
            if body and not body.endswith(","):
                body += ","
            return match.group(1) + body + trailing + f'"url": "{SITE}/"' + match.group(3)

        updated, replacements = author_pattern.subn(patch_author, text, count=1)
        if replacements and updated != text:
            write(path, updated)
            changed_files += 1
    return changed_files


def robots_allows(agent: str) -> bool:
    text = read(ROOT / "robots.txt")
    groups = re.split(r"(?=User-agent:)", text, flags=re.I)
    for group in groups:
        match = re.search(r"User-agent:\s*([^\s#]+)", group, flags=re.I)
        if match and match.group(1).lower() == agent.lower():
            return not bool(re.search(r"Disallow:\s*/\s*(?:#.*)?$", group, flags=re.I | re.M))
    return True


def story_count() -> tuple[int, int]:
    pages = []
    for path in ARTICLES.rglob("*.html"):
        rel = public_path(path)
        if re.search(r"(^|/)index(?:_cn|_en)?\.html$", rel):
            continue
        if is_redirect_article(read(path)):
            continue
        pages.append(rel)
    stories = {re.sub(r"_(?:cn|en)\.html$", ".html", rel) for rel in pages}
    return len(stories), len(pages)


def write_geo_dashboard() -> None:
    stories, pages = story_count()
    platforms = [
        {
            "id": "google",
            "name": "Google AI / Gemini",
            "discoveryBot": "Googlebot",
            "discoveryAllowed": robots_allows("Googlebot"),
            "trainingBot": "Google-Extended",
            "trainingAllowed": robots_allows("Google-Extended"),
            "measurement": "Search Console",
            "citationCount": None,
            "referralSessions": None,
        },
        {
            "id": "chatgpt",
            "name": "ChatGPT Search",
            "discoveryBot": "OAI-SearchBot",
            "discoveryAllowed": robots_allows("OAI-SearchBot"),
            "trainingBot": "GPTBot",
            "trainingAllowed": robots_allows("GPTBot"),
            "measurement": "utm_source=chatgpt.com",
            "citationCount": None,
            "referralSessions": None,
        },
        {
            "id": "bing",
            "name": "Bing / Copilot",
            "discoveryBot": "Bingbot",
            "discoveryAllowed": robots_allows("Bingbot"),
            "trainingBot": "separate Microsoft controls",
            "trainingAllowed": None,
            "measurement": "Bing Webmaster AI Performance",
            "citationCount": None,
            "referralSessions": None,
        },
        {
            "id": "perplexity",
            "name": "Perplexity",
            "discoveryBot": "PerplexityBot",
            "discoveryAllowed": robots_allows("PerplexityBot"),
            "trainingBot": "not used by PerplexityBot",
            "trainingAllowed": None,
            "measurement": "referral + verified crawler logs",
            "citationCount": None,
            "referralSessions": None,
        },
        {
            "id": "claude",
            "name": "Claude Search",
            "discoveryBot": "Claude-SearchBot",
            "discoveryAllowed": robots_allows("Claude-SearchBot"),
            "trainingBot": "ClaudeBot",
            "trainingAllowed": robots_allows("ClaudeBot"),
            "measurement": "referral + crawler logs",
            "citationCount": None,
            "referralSessions": None,
        },
    ]
    payload = {
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": {
            "eligiblePlatforms": sum(bool(row["discoveryAllowed"]) for row in platforms),
            "platformCount": len(platforms),
            "articleStories": stories,
            "languagePages": pages,
            "sitemap": "connected",
            "indexNow": "key-ready",
        },
        "platforms": platforms,
        "dataSources": {
            "serverCrawlerLogs": "not-connected",
            "aiReferralAnalytics": "not-connected",
            "bingAiPerformance": "not-connected",
            "promptBenchmark": "not-run",
        },
        "benchmark": {
            "promptCount": 60,
            "languages": ["zh-Hant", "zh-Hans", "en"],
            "cadence": "weekly sample / monthly full run",
            "lastRun": None,
            "mentionRate": None,
            "citationRate": None,
        },
        "notes": [
            "Crawler access is read from robots.txt.",
            "Citation and referral values remain blank until an official source is connected.",
            "Search access and model-training access are configured separately.",
        ],
    }
    write(GEO_PATH, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def audit() -> list[str]:
    issues: list[str] = []
    expected_agents = ["Googlebot", "Bingbot", "OAI-SearchBot", "PerplexityBot", "Claude-SearchBot"]
    for agent in expected_agents:
        if not robots_allows(agent):
            issues.append(f"DISCOVERY_BOT_BLOCKED {agent}")
    for path in sorted(ARTICLES.rglob("*_cn.html")):
        text = read(path)
        if is_redirect_article(text):
            continue
        expected = locale_paths(path)
        found = dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="' + re.escape(SITE) + r'([^"]+)">', text))
        for locale, target in expected.items():
            if found.get(locale) != target:
                issues.append(f"BAD_HREFLANG {locale} {public_path(path)}")
    for path in sorted(ARTICLES.rglob("*.html")):
        rel = public_path(path)
        if re.search(r"(^|/)index(?:_cn|_en)?\.html$", rel):
            continue
        text = read(path)
        if is_redirect_article(text):
            continue
        article_match = re.search(r'"@type"\s*:\s*"Article".*?"author"\s*:\s*\{(.*?)\}', text, re.S)
        if not article_match or '"url"' not in article_match.group(1):
            issues.append(f"AUTHOR_URL_MISSING {rel}")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply and verify GEO technical foundations for the article library")
    parser.add_argument("command", choices=("fix", "audit", "dashboard"), nargs="?", default="fix")
    args = parser.parse_args()
    if args.command == "fix":
        fixed_hreflang = fix_cn_hreflang()
        author_files = add_author_urls()
        write_geo_dashboard()
        issues = audit()
        print(f"hreflang files checked: {fixed_hreflang}")
        print(f"author URLs added: {author_files}")
        print(f"GEO audit issues: {len(issues)}")
        for issue in issues:
            print(issue)
        raise SystemExit(1 if issues else 0)
    if args.command == "dashboard":
        write_geo_dashboard()
        print(f"wrote {GEO_PATH.relative_to(ROOT)}")
        return
    issues = audit()
    for issue in issues:
        print(issue)
    print(f"GEO audit issues: {len(issues)}")
    raise SystemExit(1 if issues else 0)


if __name__ == "__main__":
    main()
