from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

try:
    from article_ops import local_article_inventory
    from topic_engine import index_state
except ImportError:
    from tools.article_ops import local_article_inventory
    from tools.topic_engine import index_state


ROOT = Path(__file__).resolve().parents[1]
LOCAL_TZ = timezone(timedelta(hours=8), name="Asia/Shanghai")
PUBLICATION_LOG_PATH = ROOT / "content-system" / "publication-log.json"
DAILY_REPORT_PATH = ROOT / "content-system" / "daily-report.json"
DAILY_REPORT_MD_PATH = ROOT / "content-system" / "daily-report.md"
DAILY_HISTORY_PATH = ROOT / "content-system" / "daily-report-history.json"
SEARCH_CONSOLE_PATH = ROOT / "dashboard" / "search-console.json"
TOPIC_ENGINE_PATH = ROOT / "dashboard" / "topic-engine.json"
TOPIC_REGISTRY_PATH = ROOT / "content-system" / "topic-registry.json"

TOPIC_LABELS = {
    "hk-inheritance": "香港继承",
    "macau": "澳门",
    "singapore": "新加坡",
    "united-states": "美国",
    "other-cross-border": "其他跨境",
}


def read_json(path: Path, fallback: Any) -> Any:
    if not path.exists():
        return fallback
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def local_date_from_timestamp(value: str | None) -> date | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return parse_date(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=LOCAL_TZ)
    return parsed.astimezone(LOCAL_TZ).date()


def preferred_title(pages: list[dict], fallback: str = "") -> str:
    priorities = {"zh-Hant": 0, "zh-Hans": 1, "en": 2}
    ordered = sorted(pages, key=lambda row: priorities.get(row.get("language"), 9))
    return str(ordered[0].get("title") if ordered else fallback).strip()


def inspection_lookup() -> tuple[dict[str, dict], dict]:
    payload = read_json(SEARCH_CONSOLE_PATH, {})
    rows = payload.get("urls", []) if isinstance(payload, dict) else []
    lookup = {
        str(row.get("url") or row.get("inspectionUrl") or "").rstrip("/"): row
        for row in rows
        if row.get("url") or row.get("inspectionUrl")
    }
    return lookup, payload if isinstance(payload, dict) else {}


def story_index_status(pages: list[dict], inspections: dict[str, dict]) -> str:
    states = []
    for page in pages:
        inspection = inspections.get(str(page.get("url") or "").rstrip("/"), {})
        indexed, explicit_nonindex, _ = index_state(inspection)
        if indexed:
            states.append("indexed")
        elif explicit_nonindex:
            states.append("not-indexed")
        else:
            states.append("unknown")
    if "indexed" in states:
        return "indexed"
    if states and all(state == "not-indexed" for state in states):
        return "not-indexed"
    return "unknown"


def publication_events_for_date(target: date) -> list[dict]:
    payload = read_json(PUBLICATION_LOG_PATH, {})
    events = payload.get("events", []) if isinstance(payload, dict) else []
    return [
        row for row in events
        if local_date_from_timestamp(row.get("deployedAt")) == target
    ]


def summarise_publications(
    inventory: list[dict],
    inspections: dict[str, dict],
    target: date,
    events: list[dict],
) -> dict:
    pages_by_story: dict[str, list[dict]] = defaultdict(list)
    for row in inventory:
        pages_by_story[row.get("story") or row.get("path")].append(row)

    metadata_stories = {
        row.get("story") or row.get("path")
        for row in inventory
        if parse_date(row.get("datePublished")) == target
    }
    event_by_story = {
        str(row.get("story") or ""): row
        for row in events
        if row.get("story")
    }
    published_stories = sorted(metadata_stories | set(event_by_story))
    published = []
    for story in published_stories:
        pages = pages_by_story.get(story, [])
        event = event_by_story.get(story, {})
        urls = sorted({row.get("url") for row in pages if row.get("url")} | set(event.get("urls", [])))
        languages = sorted({row.get("language") for row in pages if row.get("language")} | set(event.get("languages", [])))
        sources = []
        if story in metadata_stories:
            sources.append("page-metadata")
        if story in event_by_story:
            sources.append("publication-log")
        published.append(
            {
                "story": story,
                "title": preferred_title(pages, event.get("title", story)),
                "topic": pages[0].get("topic") if pages else event.get("topic", "other-cross-border"),
                "urls": urls,
                "languages": languages,
                "indexStatus": story_index_status(pages, inspections) if pages else "unknown",
                "sources": sources,
            }
        )

    updated_story_ids = {
        row.get("story") or row.get("path")
        for row in inventory
        if parse_date(row.get("dateModified")) == target
        and parse_date(row.get("datePublished")) != target
    }
    updated = [
        {
            "story": story,
            "title": preferred_title(pages_by_story[story], story),
            "topic": pages_by_story[story][0].get("topic", "other-cross-border"),
        }
        for story in sorted(updated_story_ids)
    ]

    status_counts = Counter(row["indexStatus"] for row in published)
    return {
        "date": target.isoformat(),
        "newArticleCount": len(published),
        "newLanguagePageCount": sum(len(row["urls"]) for row in published),
        "updatedArticleCount": len(updated),
        "indexed": status_counts.get("indexed", 0),
        "notIndexed": status_counts.get("not-indexed", 0),
        "indexUnknown": status_counts.get("unknown", 0),
        "articles": published,
        "updatedArticles": updated,
    }


def site_index_summary(inventory: list[dict], inspections: dict[str, dict]) -> dict:
    pages_by_story: dict[str, list[dict]] = defaultdict(list)
    for row in inventory:
        pages_by_story[row.get("story") or row.get("path")].append(row)
    story_states = {
        story: story_index_status(pages, inspections)
        for story, pages in pages_by_story.items()
    }
    counts = Counter(story_states.values())
    return {
        "inspectionConnected": bool(inspections),
        "totalArticles": len(story_states),
        "indexed": counts.get("indexed", 0) if inspections else None,
        "notIndexed": counts.get("not-indexed", 0) if inspections else None,
        "unknown": counts.get("unknown", 0),
        "indexedStories": sorted(story for story, state in story_states.items() if state == "indexed"),
    }


def previous_indexed_stories(history: dict, run_date: date) -> set[str] | None:
    snapshots = history.get("snapshots", []) if isinstance(history, dict) else []
    previous = [
        row for row in snapshots
        if parse_date(row.get("runDate")) and parse_date(row.get("runDate")) < run_date
    ]
    if not previous:
        return None
    latest = max(previous, key=lambda row: row.get("runDate", ""))
    if not latest.get("inspectionConnected"):
        return None
    return set(latest.get("indexedStories", []))


def next_directions(topic_engine: dict, limit: int = 30) -> dict:
    recommendations = list(topic_engine.get("recommendations", []))
    seen = {row.get("id") for row in recommendations}
    for row in topic_engine.get("decisions", []):
        if row.get("systemStatus") == "recommended" and row.get("id") not in seen:
            recommendations.append(row)
            seen.add(row.get("id"))
    rows = recommendations[:limit]

    registry = read_json(TOPIC_REGISTRY_PATH, {})
    cluster_labels = {
        row.get("id"): row.get("label", row.get("id"))
        for row in registry.get("clusters", [])
    }
    by_topic = Counter(row.get("topic") for row in rows)
    by_cluster = Counter(row.get("clusterId") for row in rows)
    cluster_rows = [
        {
            "clusterId": cluster,
            "label": cluster_labels.get(cluster, cluster),
            "count": count,
        }
        for cluster, count in by_cluster.most_common()
    ]
    compact_rows = [
        {
            "id": row.get("id"),
            "score": row.get("score"),
            "persona": row.get("personaLabel"),
            "topic": row.get("topic"),
            "topicLabel": TOPIC_LABELS.get(row.get("topic"), row.get("topic")),
            "clusterId": row.get("clusterId"),
            "query": row.get("primaryQuery"),
            "title": row.get("title"),
            "reason": row.get("reason"),
        }
        for row in rows
    ]
    return {
        "target": limit,
        "available": len(rows),
        "gap": max(0, limit - len(rows)),
        "byTopic": {topic: by_topic.get(topic, 0) for topic in TOPIC_LABELS if by_topic.get(topic)},
        "byCluster": cluster_rows,
        "items": compact_rows,
        "replenishment": topic_engine.get("replenishment", {}),
        "editorialTasks": topic_engine.get("editorialTasks", []),
        "suppressedClusters": topic_engine.get("suppressedClusters", []),
        "learningLog": topic_engine.get("learningLog", []),
    }


def render_markdown(report: dict) -> str:
    yesterday = report["yesterday"]
    site_index = report["siteIndex"]
    directions = report["nextDirections"]
    lines = [
        f"# 文章日报 | {report['generatedDate']}",
        "",
        f"统计对象：{report['reportDate']}（昨天）",
        "",
        "## 昨日发布",
        "",
        f"- 新发布文章：{yesterday['newArticleCount']} 篇，{yesterday['newLanguagePageCount']} 个语言页面。",
        f"- 更新既有文章：{yesterday['updatedArticleCount']} 篇。",
    ]
    if yesterday["articles"]:
        for row in yesterday["articles"]:
            lines.append(f"- {row['title']}：{row['indexStatus']}。")
    else:
        lines.append("- 发布台账和页面日期均未发现昨日新文章。")

    lines.extend(["", "## 收录状态", ""])
    if site_index["inspectionConnected"]:
        lines.extend(
            [
                f"- 昨日文章已确认收录：{yesterday['indexed']} 篇。",
                f"- 昨日文章明确未收录：{yesterday['notIndexed']} 篇；未知：{yesterday['indexUnknown']} 篇。",
                f"- 全站已确认收录：{site_index['indexed']} / {site_index['totalArticles']} 篇。",
                f"- 自上次日报新增收录：{report['newlyIndexedCount'] if report['newlyIndexedCount'] is not None else '尚无可比较基线'}。",
            ]
        )
    else:
        lines.append("- URL Inspection 明细未接通，收录数量记为未知，不用 0 代替。")
    lines.append(f"- Search Console 数据日期：{report['sourceFreshness']['searchConsoleExportedAt'] or '未知'}。")

    lines.extend(["", "## 下一批选题", ""])
    lines.append(f"- 可确认候选：{directions['available']} / {directions['target']}；仍缺 {directions['gap']} 个合格问题。")
    if directions["byTopic"]:
        mix = "、".join(
            f"{TOPIC_LABELS.get(topic, topic)} {count} 个"
            for topic, count in directions["byTopic"].items()
        )
        lines.append(f"- 当前方向：{mix}。")
    if directions["byCluster"]:
        clusters = "、".join(
            f"{row['label']} {row['count']} 个"
            for row in directions["byCluster"][:6]
        )
        lines.append(f"- 重点问题簇：{clusters}。")

    lines.extend(["", "## 升级决定", ""])
    if directions["editorialTasks"]:
        lines.append(f"- 有 {len(directions['editorialTasks'])} 篇需要技术修复、补强或标题复核。")
    else:
        lines.append("- 当前没有需要立即补强或停止的已发布文章。")
    replenishment = directions.get("replenishment", {})
    if replenishment.get("needed"):
        lines.append(f"- 合格库存不足，需要补充 {replenishment['needed']} 个独立问题。")
    else:
        lines.append("- 合格库存达到安全线，本轮不为了凑满 30 个而补题。")
    for row in directions.get("learningLog", [])[:4]:
        lines.append(f"- {row}")
    lines.append("")
    return "\n".join(lines)


def update_history(report: dict) -> None:
    history = read_json(DAILY_HISTORY_PATH, {"version": 1, "snapshots": []})
    snapshots = history.setdefault("snapshots", [])
    snapshot = {
        "runDate": report["generatedDate"],
        "reportDate": report["reportDate"],
        "generatedAt": report["generatedAt"],
        "publishedArticles": report["yesterday"]["newArticleCount"],
        "inspectionConnected": report["siteIndex"]["inspectionConnected"],
        "indexedStories": report["siteIndex"]["indexedStories"],
    }
    snapshots = [row for row in snapshots if row.get("runDate") != snapshot["runDate"]]
    snapshots.append(snapshot)
    history["snapshots"] = sorted(snapshots, key=lambda row: row.get("runDate", ""))[-120:]
    history["updatedAt"] = report["generatedAt"]
    write_json(DAILY_HISTORY_PATH, history)


def build_report(target: date | None = None, now: datetime | None = None) -> dict:
    now = now or datetime.now(LOCAL_TZ)
    if now.tzinfo is None:
        now = now.replace(tzinfo=LOCAL_TZ)
    run_date = now.astimezone(LOCAL_TZ).date()
    target = target or (run_date - timedelta(days=1))
    inventory = local_article_inventory()
    inspections, search_console = inspection_lookup()
    events = publication_events_for_date(target)
    yesterday = summarise_publications(inventory, inspections, target, events)
    site_index = site_index_summary(inventory, inspections)
    history = read_json(DAILY_HISTORY_PATH, {"version": 1, "snapshots": []})
    previous_indexed = previous_indexed_stories(history, run_date)
    newly_indexed = (
        sorted(set(site_index["indexedStories"]) - previous_indexed)
        if site_index["inspectionConnected"] and previous_indexed is not None
        else None
    )
    topic_engine = read_json(TOPIC_ENGINE_PATH, {})
    performance = search_console.get("performance", {}) if isinstance(search_console, dict) else {}
    report = {
        "generatedAt": now.astimezone(LOCAL_TZ).isoformat(timespec="seconds"),
        "generatedDate": run_date.isoformat(),
        "reportDate": target.isoformat(),
        "timezone": "Asia/Shanghai",
        "yesterday": yesterday,
        "siteIndex": site_index,
        "newlyIndexedCount": len(newly_indexed) if newly_indexed is not None else None,
        "newlyIndexedStories": newly_indexed,
        "nextDirections": next_directions(topic_engine, limit=30),
        "sourceFreshness": {
            "searchConsoleExportedAt": search_console.get("exportedAt"),
            "searchConsoleRange": performance.get("range"),
            "urlInspectionCount": len(inspections),
            "topicEngineGeneratedAt": topic_engine.get("generatedAt"),
            "publicationLogEvents": len(events),
        },
        "caveats": [
            "Search Console performance data may lag; URL Inspection is the source for a page's known index state.",
            "Unknown index state is never counted as not indexed or indexed.",
            "Publication count is de-duplicated by article story, not by language page.",
        ],
    }
    report["markdown"] = render_markdown(report)
    return report


def write_report(target: date | None = None) -> dict:
    report = build_report(target=target)
    write_json(DAILY_REPORT_PATH, report)
    DAILY_REPORT_MD_PATH.write_text(report["markdown"], encoding="utf-8", newline="\n")
    update_history(report)
    print(report["markdown"])
    return report


def record_publication(
    story: str,
    title: str,
    urls: list[str],
    languages: list[str],
    topic: str,
    deployed_at: str | None,
) -> None:
    timestamp = deployed_at or datetime.now(LOCAL_TZ).isoformat(timespec="seconds")
    if local_date_from_timestamp(timestamp) is None:
        raise SystemExit("invalid --deployed-at timestamp")
    payload = read_json(PUBLICATION_LOG_PATH, {"version": 1, "events": []})
    events = payload.setdefault("events", [])
    event_date = local_date_from_timestamp(timestamp).isoformat()
    existing = next(
        (
            row for row in events
            if row.get("story") == story
            and local_date_from_timestamp(row.get("deployedAt")) == local_date_from_timestamp(timestamp)
        ),
        None,
    )
    if existing:
        existing["title"] = title or existing.get("title", "")
        existing["urls"] = sorted(set(existing.get("urls", [])) | set(urls))
        existing["languages"] = sorted(set(existing.get("languages", [])) | set(languages))
        existing["topic"] = topic or existing.get("topic", "")
        existing["deployedAt"] = timestamp
    else:
        events.append(
            {
                "id": f"{event_date}:{story}",
                "story": story,
                "title": title,
                "topic": topic,
                "urls": sorted(set(urls)),
                "languages": sorted(set(languages)),
                "deployedAt": timestamp,
                "source": "confirmed-live-deployment",
            }
        )
    payload["updatedAt"] = datetime.now(LOCAL_TZ).isoformat(timespec="seconds")
    write_json(PUBLICATION_LOG_PATH, payload)
    print(f"recorded publication: {story}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the daily Jingwei article operations brief")
    subparsers = parser.add_subparsers(dest="command", required=True)
    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("--date", type=date.fromisoformat)
    record_parser = subparsers.add_parser("record-publish")
    record_parser.add_argument("--story", required=True)
    record_parser.add_argument("--title", default="")
    record_parser.add_argument("--topic", default="")
    record_parser.add_argument("--url", action="append", default=[])
    record_parser.add_argument("--language", action="append", default=[])
    record_parser.add_argument("--deployed-at")
    args = parser.parse_args()

    if args.command == "report":
        write_report(args.date)
    elif args.command == "record-publish":
        record_publication(
            args.story,
            args.title,
            args.url,
            args.language,
            args.topic,
            args.deployed_at,
        )


if __name__ == "__main__":
    main()
