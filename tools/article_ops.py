from __future__ import annotations

import argparse
import json
import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from html import escape, unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://www.jingwei-law.com"
ARTICLES_ROOT = ROOT / "articles"
DRAFTS_ROOT = ROOT / "content-drafts"
QUEUE_PATH = ROOT / "ARTICLE_OPERATIONS_QUEUE.json"
METRICS_PATH = ROOT / "dashboard" / "metrics.json"
SEARCH_CONSOLE_PATH = ROOT / "dashboard" / "search-console.json"
TOPIC_ENGINE_PATH = ROOT / "dashboard" / "topic-engine.json"
CONSULTATIONS_PATH = ROOT / "dashboard" / "consultations.json"
RELAY_STATUS_PATH = ROOT / "dashboard" / "lead-relay.json"
SITEMAP_PATH = ROOT / "sitemap.xml"

I18N_SUFFIX_RE = re.compile(r"_(cn|en)\.html$")
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
ROBOTS_RE = re.compile(r'<meta\s+name=["\']robots["\']\s+content=["\']([^"\']+)', re.I)
CANONICAL_RE = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)', re.I)
DATE_PUBLISHED_RE = re.compile(r'"datePublished"\s*:\s*"([^"]+)"')
DATE_MODIFIED_RE = re.compile(r'"dateModified"\s*:\s*"([^"]+)"')


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_json(path: Path, fallback):
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback


def write_json(path: Path, data) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def html_text(value: str) -> str:
    return unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", value))).strip()


def language_from_path(path: str) -> str:
    if path.endswith("_en.html"):
        return "en"
    if path.endswith("_cn.html"):
        return "zh-Hans"
    return "zh-Hant"


def canonical_story(path: str) -> str:
    clean = path.rstrip("/")
    clean = I18N_SUFFIX_RE.sub(".html", clean)
    clean = clean.removesuffix(".html")
    if clean.endswith("/index"):
        clean = clean[:-6]
    return clean


def topic_from_path(path: str) -> str:
    if path.startswith("/articles/hk-mainland-property-inheritance"):
        return "hk-inheritance"
    if path.startswith("/articles/am/"):
        return "macau"
    if path.startswith("/articles/singapore/"):
        return "singapore"
    if path.startswith("/articles/us/"):
        return "united-states"
    return "other-cross-border"


def is_article_content_path(path: str) -> bool:
    if not path.startswith("/articles/"):
        return False
    if path == "/articles/" or re.search(r"(^|/)index(?:_cn|_en)?\.html$", path):
        return False
    return path.endswith(".html") or path.endswith("/")


def parse_sitemap() -> list[dict]:
    if not SITEMAP_PATH.exists():
        return []
    tree = ET.parse(SITEMAP_PATH)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    rows = []
    for item in tree.findall("sm:url", namespace):
        loc = (item.findtext("sm:loc", default="", namespaces=namespace) or "").strip()
        lastmod = (item.findtext("sm:lastmod", default="", namespaces=namespace) or "").strip()
        if not loc.startswith(BASE_URL):
            continue
        path = loc.removeprefix(BASE_URL)
        if is_article_content_path(path):
            rows.append({"url": loc, "path": path, "lastmod": lastmod})
    return rows


def local_article_inventory() -> list[dict]:
    rows = []
    for file_path in sorted(ARTICLES_ROOT.rglob("*.html")):
        relative = file_path.relative_to(ROOT).as_posix()
        if re.search(r"(^|/)index(?:_cn|_en)?\.html$", relative):
            continue

        text = file_path.read_text(encoding="utf-8", errors="ignore")
        canonical_match = CANONICAL_RE.search(text)
        canonical = canonical_match.group(1).strip() if canonical_match else f"{BASE_URL}/{relative}"
        path = canonical.removeprefix(BASE_URL) if canonical.startswith(BASE_URL) else f"/{relative}"
        title_match = TITLE_RE.search(text)
        robots_match = ROBOTS_RE.search(text)
        published_match = DATE_PUBLISHED_RE.search(text)
        modified_match = DATE_MODIFIED_RE.search(text)
        robots = robots_match.group(1).lower() if robots_match else ""
        rows.append(
            {
                "path": path,
                "file": relative,
                "url": canonical,
                "story": canonical_story(path),
                "topic": topic_from_path(path),
                "language": language_from_path(relative),
                "title": html_text(title_match.group(1)) if title_match else file_path.stem,
                "datePublished": published_match.group(1) if published_match else "",
                "dateModified": modified_match.group(1) if modified_match else "",
                "indexable": "noindex" not in robots,
                "robots": robots or "not-declared",
            }
        )
    return rows


def discover_drafts() -> list[dict]:
    if not DRAFTS_ROOT.exists():
        return []
    drafts = []
    for folder in sorted(path for path in DRAFTS_ROOT.rglob("*") if path.is_dir()):
        markers = [
            folder / "00-card.md",
            folder / "01-research.md",
            folder / "02-outline.md",
            folder / "03-draft_zh-Hant.md",
        ]
        if not any(path.exists() for path in markers):
            continue

        review_text = ""
        if (folder / "06-review.md").exists():
            review_text = (folder / "06-review.md").read_text(encoding="utf-8", errors="ignore")

        status = "source-needed"
        if (folder / "02-outline.md").exists():
            status = "outlined"
        if (folder / "03-draft_zh-Hant.md").exists():
            status = "drafted-zh-Hant"
        for candidate in [
            "needs-fix",
            "indexed",
            "published",
            "build-ready",
            "images-ready",
            "model-written-en",
            "legal-reviewed",
        ]:
            if candidate in review_text:
                status = candidate
                break

        image_count = 0
        image_dir = folder / "images"
        if image_dir.exists():
            image_count = len([path for path in image_dir.iterdir() if path.is_file()])

        drafts.append(
            {
                "slug": folder.name,
                "status": status,
                "hasTraditional": (folder / "03-draft_zh-Hant.md").exists(),
                "hasSimplified": (folder / "04-draft_zh-Hans.md").exists(),
                "hasEnglish": (folder / "05-draft_en.md").exists(),
                "imageCount": image_count,
                "path": folder.relative_to(ROOT).as_posix(),
            }
        )
    return drafts


def queue_metrics() -> dict:
    queue = read_json(QUEUE_PATH, {})
    hk_items = queue.get("hkInheritanceQueue", [])
    status_counts = Counter(item.get("status", "planned") for item in hk_items)
    starter = queue.get("starterBacklog", {})
    return {
        "updatedAt": queue.get("updatedAt"),
        "dailyCandidateAllocation": queue.get("dailyCandidateAllocation", {}),
        "hkLaunch": {
            "total": len(hk_items),
            "remaining": sum(1 for item in hk_items if item.get("status") not in {"published", "indexed"}),
            "byStatus": dict(status_counts),
        },
        "starterBacklog": {topic: len(items) for topic, items in starter.items()},
        "next": [item for item in hk_items if item.get("status") not in {"published", "indexed"}][:12],
    }


def search_console_lookup() -> tuple[dict, dict, dict]:
    data = read_json(SEARCH_CONSOLE_PATH, {})
    rows = data.get("urls") if isinstance(data, dict) else None
    lookup = {}
    if isinstance(rows, list):
        lookup = {
            row.get("url") or row.get("inspectionUrl"): row
            for row in rows
            if row.get("url") or row.get("inspectionUrl")
        }
    performance = data.get("performance", {}) if isinstance(data, dict) else {}
    sitemap_report = data.get("sitemap", {}) if isinstance(data, dict) else {}
    return lookup, performance, sitemap_report


def index_state(row: dict) -> tuple[bool, bool, str]:
    verdict = str(row.get("verdict") or "").strip()
    coverage = str(row.get("coverageState") or "").strip()
    combined = f"{verdict} {coverage}".casefold()
    if not combined.strip() or combined.strip() in {"unknown", "neutral"}:
        return False, False, "unknown"
    explicit_nonindex_markers = (
        "not indexed",
        "not on google",
        "未编入索引",
        "未建立索引",
        "尚未收录",
    )
    if any(marker in combined for marker in explicit_nonindex_markers):
        return False, True, coverage or verdict
    indexed = verdict.upper() == "PASS" or (
        "indexed" in combined and "not indexed" not in combined
    ) or "已编入索引" in combined or "已建立索引" in combined
    return indexed, not indexed, coverage or verdict


def fetch_json(url: str) -> dict | None:
    if not url:
        return None
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "LiuYiArticleOps/1.0"})
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.loads(response.read().decode("utf-8"))
        return payload if isinstance(payload, dict) else None
    except (OSError, ValueError, json.JSONDecodeError):
        return None


def consultation_metrics() -> tuple[dict | None, str, dict]:
    local = read_json(CONSULTATIONS_PATH, None)
    if isinstance(local, dict):
        return local.get("consultation") or local, "dashboard/consultations.json", local

    endpoint = os.environ.get("JINGWEI_DASHBOARD_ENDPOINT", "").strip()
    remote = fetch_json(endpoint) if endpoint else None
    if isinstance(remote, dict) and isinstance(remote.get("consultation"), dict):
        return remote["consultation"], endpoint, remote
    return None, "not-connected", remote or {}


def build_metrics() -> dict:
    sitemap_rows = parse_sitemap()
    sitemap_by_url = {row["url"]: row for row in sitemap_rows}
    inventory = local_article_inventory()
    drafts = discover_drafts()
    queue = queue_metrics()
    topic_engine = read_json(TOPIC_ENGINE_PATH, {})
    adaptive_allocation = topic_engine.get("adaptiveAllocation", {}) if isinstance(topic_engine, dict) else {}
    if adaptive_allocation:
        queue["dailyCandidateAllocation"] = {
            "total": adaptive_allocation.get("selected", 0),
            **adaptive_allocation.get("byTopic", {}),
        }
    gsc, performance, sitemap_report = search_console_lookup()
    consultation, consultation_source, consultation_payload = consultation_metrics()
    relay_status = read_json(RELAY_STATUS_PATH, {})

    latest = []
    indexed_count = 0
    explicit_nonindex_count = 0
    inspected_count = 0
    for row in inventory:
        gsc_row = gsc.get(row["url"], {})
        indexed, explicit_nonindex, verdict = index_state(gsc_row)
        index_known = indexed or explicit_nonindex
        if row["indexable"] and index_known:
            inspected_count += 1
            if indexed:
                indexed_count += 1
            elif explicit_nonindex:
                explicit_nonindex_count += 1
        latest.append(
            {
                **row,
                "inSitemap": row["url"] in sitemap_by_url,
                "lastmod": sitemap_by_url.get(row["url"], {}).get("lastmod") or row["dateModified"],
                "indexed": indexed,
                "indexKnown": index_known,
                "indexVerdict": verdict,
                "coverageState": gsc_row.get("coverageState", ""),
                "lastCrawlTime": gsc_row.get("lastCrawlTime", ""),
            }
        )

    latest.sort(key=lambda item: (item.get("lastmod", ""), item.get("path", "")), reverse=True)
    indexable = [row for row in inventory if row["indexable"]]
    in_sitemap = [row for row in inventory if row["url"] in sitemap_by_url]
    unique_stories = sorted({row["story"] for row in inventory})
    by_language = Counter(row["language"] for row in inventory)
    by_topic = Counter(row["topic"] for row in inventory)
    ready_statuses = {"legal-reviewed", "model-written-en", "images-ready", "build-ready"}
    ready = [draft for draft in drafts if draft["status"] in ready_statuses]
    relay_online = (
        consultation_payload.get("service") == "jingwei-form-relay"
        or relay_status.get("service") == "jingwei-form-relay"
    )
    gsc_connected = bool(gsc)
    unknown_index_count = max(0, len(indexable) - inspected_count)
    complete_index_coverage = bool(indexable) and inspected_count == len(indexable)

    return {
        "generatedAt": now_iso(),
        "source": {
            "sitemap": "sitemap.xml",
            "searchConsole": "dashboard/search-console.json" if gsc_connected else "not-connected",
            "searchConsolePerformance": "dashboard/search-console.json" if performance else "not-connected",
            "topicEngine": "dashboard/topic-engine.json" if topic_engine else "not-generated",
            "consultations": consultation_source,
            "leadRelay": "online" if relay_online else "unknown",
            "emailMode": consultation_payload.get("mail_mode") or relay_status.get("mail_mode", "not-reported"),
        },
        "consultation": consultation,
        "sitemap": {
            "localUrlCount": len(sitemap_rows),
            "searchConsole": sitemap_report or None,
        },
        "articles": {
            "totalPages": len(inventory),
            "uniqueTopics": len(unique_stories),
            "indexablePages": len(indexable),
            "sitemapPages": len(in_sitemap),
            "unsitemappedPages": len(inventory) - len(in_sitemap),
            "byLanguage": dict(by_language),
            "byTopic": dict(by_topic),
            "latest": latest,
        },
        "drafts": {"total": len(drafts), "ready": len(ready), "items": drafts},
        "queue": queue,
        "topicEngine": topic_engine,
        "indexed": {
            "count": indexed_count if complete_index_coverage else None,
            "confirmedCount": indexed_count if gsc_connected else None,
            "confirmedNotIndexedCount": explicit_nonindex_count if gsc_connected else None,
            "inspectedCount": inspected_count if gsc_connected else None,
            "unknownCount": unknown_index_count if gsc_connected else None,
            "pending": explicit_nonindex_count if gsc_connected else None,
            "source": "Search Console URL Inspection" if gsc_connected else "not connected",
        },
        "searchPerformance": performance,
        "leadChain": {
            "steps": ["Article CTA", "AI initial Q&A", "Lead form", "Form relay", "Lead sheet", "Email notification"],
            "topicField": "configured-in-source",
            "aggregateEndpoint": consultation_source,
        },
        "compliance": {
            "mode": "human-first",
            "autoPublish": False,
            "dailyCandidateLimit": 30,
            "dailyPublishPolicy": "publish only after every quality gate passes",
            "googlePolicyCheckedAt": "2026-07-22",
            "notes": [
                "30 means candidate slots, not a forced daily publication count.",
                "Use truthful publication and modification dates only.",
                "Do not create thin pages for minor query variations.",
                "Use Search Console data for index monitoring; do not scrape Google results.",
            ],
        },
    }


def write_dashboard() -> None:
    metrics = build_metrics()
    write_json(METRICS_PATH, metrics)
    print(f"wrote {METRICS_PATH.relative_to(ROOT)}")
    print("article pages:", metrics["articles"]["totalPages"])
    print("indexable:", metrics["articles"]["indexablePages"])
    print("in sitemap:", metrics["articles"]["sitemapPages"])
    print("draft packages:", metrics["drafts"]["total"])
    print("HK queue remaining:", metrics["queue"]["hkLaunch"]["remaining"])


def audit() -> int:
    metrics = build_metrics()
    issues = []
    for row in metrics["articles"]["latest"]:
        file_path = ROOT / row["file"]
        raw = file_path.read_text(encoding="utf-8", errors="ignore")
        if not row["indexable"]:
            issues.append(f"NOINDEX {row['file']}")
        if not row["inSitemap"]:
            issues.append(f"NOT_IN_SITEMAP {row['file']}")
        if not row["datePublished"]:
            issues.append(f"MISSING_DATE_PUBLISHED {row['file']}")
        if not row["dateModified"]:
            issues.append(f"MISSING_DATE_MODIFIED {row['file']}")

        visible_dates = re.findall(r"最後更新|最后更新|Last updated", raw)
        if len(visible_dates) != 1:
            issues.append(f"VISIBLE_DATE_COUNT_{len(visible_dates)} {row['file']}")

        ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', raw, re.I))
        for anchor in re.findall(r'href=["\']#([^"\']+)["\']', raw, re.I):
            if anchor not in ids:
                issues.append(f"BROKEN_ANCHOR #{anchor} {row['file']}")

        for href in re.findall(r'href=["\']([^"\']+)["\']', raw, re.I):
            local_href = unescape(href).split("#", 1)[0].split("?", 1)[0]
            if not local_href.startswith("/articles/"):
                continue
            target = ROOT / local_href.lstrip("/")
            if local_href.endswith("/"):
                target = target / "index.html"
            if not target.exists():
                issues.append(f"BROKEN_ARTICLE_LINK {local_href} {row['file']}")

        image_sources = re.findall(
            r'src=["\'](/articles/[^"\']+/images/[^"\']+\.svg)["\']',
            raw,
            re.I,
        )
        if len(image_sources) != 3:
            issues.append(f"ARTICLE_IMAGE_COUNT_{len(image_sources)} {row['file']}")
        for source in image_sources:
            if not (ROOT / source.lstrip("/")).exists():
                issues.append(f"MISSING_ARTICLE_IMAGE {source} {row['file']}")

        if re.search(r"gov\.cn|《中华人民共和国|中华人民共和国[^\n<]{0,40}(?:法|条例|办法)", raw):
            issues.append(f"CLIENT_PAGE_FORMAL_STATE_REFERENCE {row['file']}")
    for issue in issues:
        print(issue)
    print(f"audit issues: {len(issues)}")
    return 1 if issues else 0


def queue_next(limit: int) -> None:
    queue = read_json(QUEUE_PATH, {})
    items = [
        item
        for item in queue.get("hkInheritanceQueue", [])
        if item.get("status") not in {"published", "indexed"}
    ][:limit]
    print(json.dumps(items, ensure_ascii=False, indent=2))


def find_queue_item(slug: str) -> dict | None:
    queue = read_json(QUEUE_PATH, {})
    return next((item for item in queue.get("hkInheritanceQueue", []) if item.get("slug") == slug), None)


def split_title(title: str, max_chars: int = 17) -> tuple[str, str]:
    if len(title) <= max_chars:
        return title, ""
    split_at = max(title.rfind("，", 0, max_chars + 4), title.rfind("：", 0, max_chars + 4))
    if split_at < 6:
        split_at = max_chars
    return title[: split_at + (1 if title[split_at:split_at + 1] in "，：" else 0)], title[split_at + (1 if title[split_at:split_at + 1] in "，：" else 0):]


def svg_card(title: str, kicker: str, steps: list[str], accent: str, layout: str) -> str:
    first, second = split_title(title)
    title_markup = f'<text x="88" y="164" class="title">{escape(first)}</text>'
    if second:
        title_markup += f'<text x="88" y="220" class="title">{escape(second)}</text>'
    start_y = 320 if second else 286
    rows = []
    for index, step in enumerate(steps[:4], 1):
        y = start_y + (index - 1) * 84
        rows.append(f'<circle cx="112" cy="{y}" r="23" class="step"/><text x="112" y="{y + 9}" text-anchor="middle" class="number">{index}</text><text x="158" y="{y + 10}" class="body">{escape(step)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-label="{escape(title)}">
  <style>.bg{{fill:#f3f6fa}}.panel{{fill:#fff;stroke:#d8e0ea;stroke-width:2}}.kicker{{fill:{accent};font:700 25px -apple-system,BlinkMacSystemFont,"PingFang TC","Microsoft JhengHei",sans-serif}}.title{{fill:#142033;font:760 46px -apple-system,BlinkMacSystemFont,"PingFang TC","Microsoft JhengHei",sans-serif}}.body{{fill:#2a3a4f;font:600 28px -apple-system,BlinkMacSystemFont,"PingFang TC","Microsoft JhengHei",sans-serif}}.step{{fill:{accent};opacity:.13}}.number{{fill:{accent};font:760 22px -apple-system,BlinkMacSystemFont,sans-serif}}.line{{stroke:{accent};stroke-width:8;stroke-linecap:round;opacity:.22}}</style>
  <rect class="bg" width="1200" height="720"/><rect class="panel" x="42" y="42" width="1116" height="636" rx="18"/><line class="line" x1="88" y1="92" x2="260" y2="92"/><text x="88" y="126" class="kicker">{escape(kicker)} · {escape(layout)}</text>{title_markup}{''.join(rows)}
</svg>'''


def make_images(slug: str) -> None:
    item = find_queue_item(slug)
    if not item:
        raise SystemExit(f"unknown queue slug: {slug}")
    folder = DRAFTS_ROOT / "hk-mainland-property-inheritance-202607" / "03-drafts" / slug
    images = folder / "images"
    images.mkdir(parents=True, exist_ok=True)
    title = item["title"]
    intent = item.get("intent", "跨境繼承")
    specs = [
        ("01-scene.svg", "先釐清情況", ["家人與所在地", "資產和控制人", "現有文件", "目前卡點"], "#a30d23", "場景"),
        ("02-flow.svg", "再決定路徑", ["核對事實", "補關鍵缺口", "安排簽字授權", "再進入辦理"], "#006f6a", "流程"),
        ("03-checklist.svg", "諮詢前清單", ["時間線", "人物關係", "資產線索", "最想解決的問題"], "#1d5f9b", "清單"),
    ]
    for filename, kicker, steps, accent, layout in specs:
        (images / filename).write_text(
            svg_card(title, f"{intent} · {kicker}", steps, accent, layout),
            encoding="utf-8",
            newline="\n",
        )
    (folder / "07-image-plan.md").write_text(
        "# 三圖方案\n\n"
        "- `01-scene.svg`：把客户當下的人物、資產和卡點放在同一張圖。\n"
        "- `02-flow.svg`：用四步説明先後順序，不承諾固定結果。\n"
        "- `03-checklist.svg`：讓讀者按圖整理諮詢資料。\n\n"
        "圖片只解釋文章內容，不放政府標誌、法條截圖或誤導性結果承諾。\n",
        encoding="utf-8",
        newline="\n",
    )
    print("wrote three-image set for", slug)


PUBLISHED_VISUALS = {
    "index": ("#a30d23", "home"),
    "documents": ("#176b68", "documents"),
    "dispute": ("#9b3f4d", "dispute"),
    "tax-cost": ("#9a6715", "calendar"),
    "bank-deposits": ("#315f8f", "bank"),
    "social-security-housing-fund": ("#4b6d3c", "benefits"),
    "missing-documents": ("#76558f", "archive"),
    "ancestral-home-homestead": ("#8a5138", "ancestral"),
}

ADDITIONAL_PUBLISHED_VISUALS = {
    "am/images/macau-client-mainland-lawyer": ("#9a6715", "documents"),
    "us/images/remote-china-lawyer": ("#315f8f", "remote"),
    "overseas-chinese/images/remote-entrust-china-lawyer": ("#176b68", "world"),
}


PUBLISHED_ICON_MARKUP = {
    "home": '<path d="M28 105 110 38l82 67v92H28z"/><path d="M76 197v-58h68v58"/><circle cx="46" cy="42" r="20"/><circle cx="174" cy="42" r="20"/>',
    "documents": '<rect x="32" y="24" width="130" height="172" rx="12"/><path d="M64 67h66M64 99h66M64 131h42"/><rect x="105" y="92" width="82" height="98" rx="10"/><path d="m127 142 16 16 27-34"/>',
    "dispute": '<circle cx="58" cy="61" r="28"/><circle cx="162" cy="61" r="28"/><path d="M18 184v-34c0-30 18-48 40-48s40 18 40 48v34M122 184v-34c0-30 18-48 40-48s40 18 40 48v34M103 36v150"/>',
    "calendar": '<rect x="24" y="42" width="172" height="148" rx="14"/><path d="M24 84h172M66 22v40M154 22v40"/><circle cx="77" cy="126" r="22"/><path d="M77 115v22M67 126h20"/><path d="M122 123h44M122 151h44"/>',
    "bank": '<path d="m22 82 88-54 88 54zM38 94h144M46 94v78M86 94v78M134 94v78M174 94v78M26 174h168v22H26z"/><circle cx="174" cy="54" r="28"/><path d="m194 74 20 20"/>',
    "benefits": '<rect x="26" y="30" width="168" height="166" rx="14"/><path d="M26 82h168M82 82v114M138 82v114"/><circle cx="54" cy="56" r="12"/><path d="m112 50 10 10 18-22M150 124h24M150 154h24M42 124h24M42 154h24"/>',
    "archive": '<path d="M24 68h72l18 20h82v106H24z"/><path d="M44 68V38h124v50"/><rect x="78" y="105" width="74" height="74" rx="8" stroke-dasharray="10 10"/><path d="M95 129h40M95 151h26"/>',
    "ancestral": '<path d="m20 102 90-72 90 72M36 98v98h148V98M74 196v-62h72v62"/><path d="M12 216h196M24 235h172M45 254h130"/><circle cx="58" cy="62" r="18"/><circle cx="164" cy="62" r="18"/>',
    "remote": '<rect x="20" y="42" width="180" height="118" rx="12"/><path d="M8 184h204M62 184l12-24h72l12 24"/><circle cx="110" cy="84" r="22"/><path d="M72 142c6-25 20-38 38-38s32 13 38 38"/><rect x="146" y="116" width="58" height="78" rx="8"/><path d="M159 139h32M159 160h24"/>',
    "world": '<circle cx="104" cy="106" r="78"/><path d="M26 106h156M104 28c26 24 40 49 40 78s-14 54-40 78M104 28c-26 24-40 49-40 78s14 54 40 78M38 68h132M38 144h132"/><path d="M150 188h58v-58M208 130l-69 69"/>',
}


def published_svg(accent: str, icon: str, variant: int) -> str:
    icon_markup = PUBLISHED_ICON_MARKUP[icon]
    common = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" aria-hidden="true">
  <rect width="1200" height="720" fill="#f3f6fa"/><rect x="42" y="42" width="1116" height="636" rx="18" fill="#fff" stroke="#d8e0ea" stroke-width="2"/>
  <path d="M82 94h176" stroke="{accent}" stroke-width="9" stroke-linecap="round" opacity=".75"/>'''
    if variant == 1:
        body = f'''
  <circle cx="330" cy="360" r="184" fill="{accent}" opacity=".09"/>
  <g transform="translate(218 242)" fill="none" stroke="#172338" stroke-width="11" stroke-linecap="round" stroke-linejoin="round">{icon_markup}</g>
  <g fill="#fff" stroke="#d8e0ea" stroke-width="3"><rect x="640" y="188" width="400" height="92" rx="16"/><rect x="640" y="314" width="400" height="92" rx="16"/><rect x="640" y="440" width="400" height="92" rx="16"/></g>
  <g fill="{accent}"><circle cx="692" cy="234" r="17"/><circle cx="692" cy="360" r="17"/><circle cx="692" cy="486" r="17"/></g>
  <g stroke="#9aa8b8" stroke-width="10" stroke-linecap="round"><path d="M738 224h226M738 248h152"/><path d="M738 350h248M738 374h178"/><path d="M738 476h210M738 500h252"/></g>'''
    elif variant == 2:
        body = f'''
  <path d="M196 360h808" stroke="#b9c5d2" stroke-width="12" stroke-linecap="round"/>
  <g fill="#fff" stroke="{accent}" stroke-width="10"><circle cx="224" cy="360" r="68"/><circle cx="474" cy="360" r="68"/><circle cx="724" cy="360" r="68"/><circle cx="974" cy="360" r="68"/></g>
  <g fill="none" stroke="#172338" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"><path d="m194 362 22 22 43-53"/><path d="M444 332h60v60h-60zM460 315h28"/><path d="M694 342h60M694 365h46M694 388h54"/><path d="m944 362 22 22 43-53"/></g>
  <g fill="{accent}" opacity=".12"><circle cx="224" cy="360" r="45"/><circle cx="974" cy="360" r="45"/></g>'''
    else:
        body = f'''
  <rect x="188" y="148" width="470" height="430" rx="22" fill="#fff" stroke="#d8e0ea" stroke-width="4"/>
  <rect x="316" y="118" width="214" height="74" rx="20" fill="{accent}" opacity=".14" stroke="{accent}" stroke-width="4"/>
  <g fill="none" stroke="{accent}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"><path d="m248 270 20 20 38-48M248 374l20 20 38-48M248 478l20 20 38-48"/></g>
  <g stroke="#9aa8b8" stroke-width="12" stroke-linecap="round"><path d="M348 258h240M348 292h170M348 362h220M348 396h192M348 466h248M348 500h154"/></g>
  <circle cx="882" cy="360" r="172" fill="{accent}" opacity=".09"/>
  <g transform="translate(770 242)" fill="none" stroke="#172338" stroke-width="11" stroke-linecap="round" stroke-linejoin="round">{icon_markup}</g>'''
    return common + body + "\n</svg>\n"


def make_published_images() -> None:
    root = ARTICLES_ROOT / "hk-mainland-property-inheritance" / "images"
    for slug, (accent, icon) in PUBLISHED_VISUALS.items():
        folder = root / slug
        folder.mkdir(parents=True, exist_ok=True)
        for variant, filename in enumerate(("01-context.svg", "02-path.svg", "03-checklist.svg"), 1):
            (folder / filename).write_text(
                published_svg(accent, icon, variant),
                encoding="utf-8",
                newline="\n",
            )
    for relative_folder, (accent, icon) in ADDITIONAL_PUBLISHED_VISUALS.items():
        folder = ARTICLES_ROOT / relative_folder
        folder.mkdir(parents=True, exist_ok=True)
        for variant, filename in enumerate(("01-context.svg", "02-path.svg", "03-checklist.svg"), 1):
            (folder / filename).write_text(
                published_svg(accent, icon, variant),
                encoding="utf-8",
                newline="\n",
            )
    total = (len(PUBLISHED_VISUALS) + len(ADDITIONAL_PUBLISHED_VISUALS)) * 3
    print(f"wrote {total} published article visuals")


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("dashboard")
    subparsers.add_parser("audit")
    next_parser = subparsers.add_parser("next")
    next_parser.add_argument("--limit", type=int, default=10)
    image_parser = subparsers.add_parser("images")
    image_parser.add_argument("--slug", required=True)
    subparsers.add_parser("published-images")
    args = parser.parse_args()

    if args.command == "dashboard":
        write_dashboard()
    elif args.command == "audit":
        raise SystemExit(audit())
    elif args.command == "next":
        queue_next(args.limit)
    elif args.command == "images":
        make_images(args.slug)
    elif args.command == "published-images":
        make_published_images()


if __name__ == "__main__":
    main()
