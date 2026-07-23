from __future__ import annotations

import argparse
import csv
import json
import math
import re
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PERSONAS_PATH = ROOT / "content-system" / "personas.json"
REGISTRY_PATH = ROOT / "content-system" / "topic-registry.json"
SEARCH_CONSOLE_PATH = ROOT / "dashboard" / "search-console.json"
CONSULTATIONS_PATH = ROOT / "dashboard" / "consultations.json"
METRICS_PATH = ROOT / "dashboard" / "metrics.json"
SNAPSHOT_PATH = ROOT / "dashboard" / "topic-engine.json"

TOPIC_LABELS = {
    "hk-inheritance": "香港继承",
    "macau": "澳门",
    "singapore": "新加坡",
    "united-states": "美国",
}

STATUS_ACTIONS = {
    "recommended": "进入资料研究",
    "in-production": "继续现有写作流程",
    "published-observe": "继续观察",
    "indexed-learning": "保留并学习",
    "title-review": "检查标题和开头",
    "improve-once": "做一次实质补强",
    "needs-technical-fix": "先修技术问题",
    "hold": "暂停同类扩写",
    "retired": "停止该搜索模式",
    "reconsider": "出现新信号，人工复核",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def today_iso() -> str:
    return date.today().isoformat()


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


def normalise(value: str) -> str:
    return re.sub(r"[^0-9a-z\u3400-\u9fff]+", "", str(value).casefold())


def phrase_matches(query: str, phrases: list[str]) -> bool:
    query_key = normalise(query)
    if not query_key:
        return False
    for phrase in phrases:
        phrase_key = normalise(phrase)
        if len(phrase_key) >= 4 and (phrase_key in query_key or query_key in phrase_key):
            return True
    return False


def text_similarity(left: str, right: str) -> float:
    left_key = normalise(left)
    right_key = normalise(right)
    if not left_key or not right_key:
        return 0.0
    if left_key == right_key:
        return 1.0

    def grams(value: str) -> set[str]:
        if len(value) < 2:
            return {value}
        return {value[index : index + 2] for index in range(len(value) - 1)}

    left_grams = grams(left_key)
    right_grams = grams(right_key)
    jaccard = len(left_grams & right_grams) / max(1, len(left_grams | right_grams))
    sequence = SequenceMatcher(None, left_key, right_key).ratio()
    return max(jaccard, sequence)


def parse_iso_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(str(value)[:10])
    except ValueError:
        return None


def age_in_days(value: str | None, today: date | None = None) -> int | None:
    parsed = parse_iso_date(value)
    if not parsed:
        return None
    return max(0, ((today or date.today()) - parsed).days)


def safe_number(value: Any, default: float = 0) -> float:
    if value is None or value == "":
        return default
    try:
        text = str(value).strip().replace(",", "").replace("%", "")
        number = float(text)
        if "%" in str(value):
            number /= 100
        return number
    except (TypeError, ValueError):
        return default


def load_inventory() -> tuple[dict[str, dict], set[str]]:
    try:
        from article_ops import local_article_inventory, parse_sitemap
    except ImportError:
        return {}, set()
    inventory = {row["url"].rstrip("/"): row for row in local_article_inventory()}
    sitemap_urls = {row["url"].rstrip("/") for row in parse_sitemap()}
    return inventory, sitemap_urls


def consultation_by_topic() -> dict[str, int]:
    payload = read_json(CONSULTATIONS_PATH, {})
    if not payload:
        payload = read_json(METRICS_PATH, {}).get("consultation") or {}
    consultation = payload.get("consultation", payload) if isinstance(payload, dict) else {}
    rows = consultation.get("by_topic", []) if isinstance(consultation, dict) else []
    result: dict[str, int] = {}
    if isinstance(rows, dict):
        rows = [{"key": key, "count": value} for key, value in rows.items()]
    for row in rows if isinstance(rows, list) else []:
        key = str(row.get("key") or row.get("topic") or "").strip()
        if key:
            result[key] = int(safe_number(row.get("count")))
    return result


def index_state(row: dict) -> tuple[bool, bool, str]:
    verdict = str(row.get("verdict") or "").strip()
    coverage = str(row.get("coverageState") or "").strip()
    combined = f"{verdict} {coverage}".casefold()
    if not combined.strip() or combined.strip() in {"unknown", "neutral"}:
        return False, False, "unknown"
    if "not indexed" in combined or "未编入索引" in combined or "未建立索引" in combined:
        return False, True, coverage or verdict
    indexed = verdict.upper() == "PASS" or (
        "indexed" in combined and "not indexed" not in combined
    ) or "已编入索引" in combined or "已建立索引" in combined
    return indexed, not indexed, coverage or verdict


def search_console_sources() -> tuple[list[dict], dict[str, dict], dict[str, dict], dict]:
    payload = read_json(SEARCH_CONSOLE_PATH, {})
    performance = payload.get("performance", {}) if isinstance(payload, dict) else {}
    queries = performance.get("topQueries", []) if isinstance(performance, dict) else []
    page_rows = performance.get("topPages", []) if isinstance(performance, dict) else []
    inspections = payload.get("urls", []) if isinstance(payload, dict) else []
    pages = {
        str(row.get("url") or row.get("page") or "").rstrip("/"): row
        for row in page_rows
        if row.get("url") or row.get("page")
    }
    inspection_lookup = {
        str(row.get("url") or row.get("inspectionUrl") or "").rstrip("/"): row
        for row in inspections
        if row.get("url") or row.get("inspectionUrl")
    }
    return queries, pages, inspection_lookup, payload


def query_signal(candidate: dict, query_rows: list[dict]) -> dict:
    matches = []
    phrases = candidate.get("matchPhrases", [])
    for row in query_rows:
        query = str(row.get("query") or "")
        if phrase_matches(query, phrases):
            matches.append(row)
    return {
        "matches": len(matches),
        "impressions": int(sum(safe_number(row.get("impressions")) for row in matches)),
        "clicks": int(sum(safe_number(row.get("clicks")) for row in matches)),
    }


def score_candidate(
    candidate: dict,
    query: dict,
    page: dict,
    lead_count: int,
    minimum_sources: int,
    long_nonindex: bool,
    cluster_suppressed: bool,
) -> tuple[int, dict[str, int]]:
    breakdown = {
        "personaFit": 24 if candidate.get("personaId") else 0,
        "distinctValue": 15 if candidate.get("distinctValue") else -25,
        "evidenceReady": 15 if len(candidate.get("evidenceSources", [])) >= minimum_sources else 5,
        "naturalQuestion": 11 if len(normalise(candidate.get("primaryQuery", ""))) >= 8 else 4,
        "observedQuery": min(15, query["impressions"] + query["clicks"] * 4),
        "pagePerformance": min(
            12,
            int(math.ceil(math.log2(safe_number(page.get("impressions")) + 1)) * 2)
            + int(safe_number(page.get("clicks"))) * 3,
        ),
        "consultation": min(10, max(0, lead_count) * 3),
        "longNonIndex": -25 if long_nonindex else 0,
        "clusterPause": -50 if cluster_suppressed else 0,
    }
    return max(0, min(100, sum(breakdown.values()))), breakdown


def lifecycle_status(
    candidate: dict,
    score: int,
    threshold: int,
    page: dict,
    inspection: dict,
    inventory: dict | None,
    in_sitemap: bool,
    lead_count: int,
    retirement_day: int,
    improvement_day: int,
    today: date | None = None,
) -> tuple[str, str, str]:
    published_url = str(candidate.get("publishedUrl") or "").rstrip("/")
    impressions = int(safe_number(page.get("impressions")))
    clicks = int(safe_number(page.get("clicks")))
    indexed, explicit_nonindex, index_label = index_state(inspection)
    published_age = age_in_days((inventory or {}).get("datePublished"), today=today)
    technical_healthy = bool(inventory and inventory.get("indexable") and in_sitemap)
    previous_retired = candidate.get("systemStatus") == "retired" or candidate.get("status") == "retired"

    if not published_url:
        editorial_status = str(candidate.get("status") or "candidate")
        if editorial_status not in {"candidate", "planned"}:
            return "in-production", STATUS_ACTIONS["in-production"], f"已进入 {editorial_status} 阶段"
        if candidate.get("clusterSuppressed"):
            return "hold", STATUS_ACTIONS["hold"], "同一问题簇近期已有两篇长期无信号页面"
        if score >= threshold:
            return "recommended", STATUS_ACTIONS["recommended"], "人物需求清楚，问题独立，资料来源达到门槛"
        return "hold", STATUS_ACTIONS["hold"], "当前信号不足，先不扩写"

    if inventory and (not inventory.get("indexable") or not in_sitemap):
        return "needs-technical-fix", STATUS_ACTIONS["needs-technical-fix"], "页面存在索引权限或 sitemap 问题"

    if previous_retired and (impressions > 0 or clicks > 0 or lead_count > 0):
        return "reconsider", STATUS_ACTIONS["reconsider"], "暂停后出现展示、点击或咨询信号"

    if indexed:
        ctr = clicks / impressions if impressions else None
        if impressions >= 20 and ctr is not None and ctr < 0.02:
            return "title-review", STATUS_ACTIONS["title-review"], "页面有展示但点击率偏低"
        if published_age is not None and published_age >= 60 and impressions == 0 and lead_count == 0:
            return "hold", STATUS_ACTIONS["hold"], "已收录但长期没有展示或咨询，暂停相近选题"
        return "indexed-learning", STATUS_ACTIONS["indexed-learning"], f"已收录；{index_label}"

    if explicit_nonindex and technical_healthy and published_age is not None:
        if published_age >= retirement_day and impressions == 0 and clicks == 0 and lead_count == 0:
            return "retired", STATUS_ACTIONS["retired"], f"明确未收录已满 {retirement_day} 天，且无展示、点击和咨询"
        if published_age >= improvement_day and int(candidate.get("improvements") or 0) < 1:
            return "improve-once", STATUS_ACTIONS["improve-once"], "技术基础正常，进入一次内容实质补强窗口"

    if inspection:
        return "published-observe", STATUS_ACTIONS["published-observe"], f"继续观察；{index_label}"
    return "published-observe", STATUS_ACTIONS["published-observe"], "尚无 URL 检查数据，不能把未知当作未收录"


def retired_patterns(registry: dict, decisions: list[dict], today: date) -> tuple[list[dict], set[str]]:
    existing = list(registry.get("retiredPatterns", []))
    by_candidate = {row.get("candidateId"): row for row in existing}
    for decision in decisions:
        if decision["systemStatus"] != "retired":
            continue
        row = by_candidate.get(decision["id"])
        if not row:
            row = {
                "candidateId": decision["id"],
                "clusterId": decision["clusterId"],
                "query": decision["primaryQuery"],
                "retiredAt": today.isoformat(),
                "reason": decision["reason"],
            }
            existing.append(row)
            by_candidate[decision["id"]] = row

    recent = Counter()
    for row in existing:
        retired_at = parse_iso_date(row.get("retiredAt"))
        if retired_at and (today - retired_at).days <= 180:
            recent[row.get("clusterId")] += 1
    suppressed = {cluster for cluster, count in recent.items() if cluster and count >= 2}
    return existing, suppressed


def allocate(decisions: list[dict], limit: int, threshold: int) -> tuple[list[dict], dict[str, int]]:
    eligible = [
        row for row in decisions
        if row["systemStatus"] == "recommended" and row["score"] >= threshold
    ]
    eligible.sort(
        key=lambda row: (
            row["score"],
            row["signals"]["queryImpressions"],
            row["signals"]["pageImpressions"],
        ),
        reverse=True,
    )
    selected: list[dict] = []
    selected_ids: set[str] = set()

    for topic in TOPIC_LABELS:
        first = next((row for row in eligible if row["topic"] == topic), None)
        if first and len(selected) < limit:
            selected.append(first)
            selected_ids.add(first["id"])

    for row in eligible:
        if len(selected) >= limit:
            break
        if row["id"] not in selected_ids:
            selected.append(row)
            selected_ids.add(row["id"])

    allocation = Counter(row["topic"] for row in selected)
    return selected, {topic: allocation.get(topic, 0) for topic in TOPIC_LABELS}


def build_snapshot(today: date | None = None) -> tuple[dict, dict]:
    today = today or date.today()
    personas_payload = read_json(PERSONAS_PATH, {})
    registry = read_json(REGISTRY_PATH, {})
    settings = registry.get("settings", {})
    personas = {row["id"]: row for row in personas_payload.get("personas", [])}
    query_rows, page_lookup, inspection_lookup, gsc_payload = search_console_sources()
    inventory_lookup, sitemap_urls = load_inventory()
    leads = consultation_by_topic()
    minimum_sources = int(settings.get("minimumEvidenceSources", 2))
    threshold = int(settings.get("recommendationThreshold", 65))
    retirement_day = int(settings.get("retirementReviewDay", 75))
    improvement_day = int(settings.get("improvementReviewDay", 46))

    first_pass = []
    for candidate in registry.get("candidates", []):
        persona = personas.get(candidate.get("personaId"), {})
        topic = persona.get("topic") or candidate.get("topic") or "other"
        url = str(candidate.get("publishedUrl") or "").rstrip("/")
        page = page_lookup.get(url, {})
        inspection = inspection_lookup.get(url, {})
        inventory = inventory_lookup.get(url)
        in_sitemap = url in sitemap_urls if url else False
        query = query_signal(candidate, query_rows)
        indexed, explicit_nonindex, _ = index_state(inspection)
        published_age = age_in_days((inventory or {}).get("datePublished"), today=today)
        long_nonindex = bool(
            explicit_nonindex
            and published_age is not None
            and published_age >= retirement_day
            and safe_number(page.get("impressions")) == 0
            and leads.get(topic, 0) == 0
        )
        score, breakdown = score_candidate(
            candidate,
            query,
            page,
            leads.get(topic, 0),
            minimum_sources,
            long_nonindex,
            False,
        )
        status, action, reason = lifecycle_status(
            candidate,
            score,
            threshold,
            page,
            inspection,
            inventory,
            in_sitemap,
            leads.get(topic, 0),
            retirement_day,
            improvement_day,
            today=today,
        )
        first_pass.append(
            {
                "id": candidate.get("id"),
                "personaId": candidate.get("personaId"),
                "personaLabel": persona.get("label", "未分类人物"),
                "topic": topic,
                "topicLabel": TOPIC_LABELS.get(topic, topic),
                "clusterId": candidate.get("clusterId"),
                "title": candidate.get("title"),
                "primaryQuery": candidate.get("primaryQuery"),
                "surfaceIntent": candidate.get("surfaceIntent"),
                "deepIntent": candidate.get("deepIntent"),
                "contextIntent": candidate.get("contextIntent"),
                "publishedUrl": url,
                "score": score,
                "scoreBreakdown": breakdown,
                "systemStatus": status,
                "action": action,
                "reason": reason,
                "signals": {
                    "queryMatches": query["matches"],
                    "queryImpressions": query["impressions"],
                    "queryClicks": query["clicks"],
                    "pageImpressions": int(safe_number(page.get("impressions"))),
                    "pageClicks": int(safe_number(page.get("clicks"))),
                    "consultations": int(leads.get(topic, 0)),
                    "indexed": indexed,
                    "inspectionKnown": bool(inspection),
                    "publishedAgeDays": published_age,
                },
            }
        )

    patterns, suppressed_clusters = retired_patterns(registry, first_pass, today)
    decisions = []
    candidate_lookup = {row.get("id"): row for row in registry.get("candidates", [])}
    for decision in first_pass:
        candidate = candidate_lookup.get(decision["id"], {})
        if decision["clusterId"] in suppressed_clusters and not decision["publishedUrl"]:
            candidate["clusterSuppressed"] = True
            score, breakdown = score_candidate(
                candidate,
                {
                    "impressions": decision["signals"]["queryImpressions"],
                    "clicks": decision["signals"]["queryClicks"],
                },
                {
                    "impressions": decision["signals"]["pageImpressions"],
                    "clicks": decision["signals"]["pageClicks"],
                },
                decision["signals"]["consultations"],
                minimum_sources,
                False,
                True,
            )
            decision["score"] = score
            decision["scoreBreakdown"] = breakdown
            decision["systemStatus"] = "hold"
            decision["action"] = STATUS_ACTIONS["hold"]
            decision["reason"] = "同一问题簇近期已有两篇长期无信号页面"
        decisions.append(decision)

    selected, allocation = allocate(
        decisions,
        int(settings.get("dailyCandidateLimit", 30)),
        threshold,
    )
    task_rows = [
        row for row in decisions
        if row["systemStatus"] in {"needs-technical-fix", "improve-once", "title-review", "reconsider"}
    ]
    task_rows.sort(key=lambda row: (row["score"], row["signals"]["pageImpressions"]), reverse=True)

    persona_rows = []
    for persona in personas.values():
        rows = [row for row in decisions if row["personaId"] == persona["id"]]
        observed = sum(row["signals"]["queryMatches"] for row in rows)
        persona_rows.append(
            {
                "id": persona["id"],
                "topic": persona["topic"],
                "label": persona["label"],
                "name": persona["name"],
                "age": persona["age"],
                "identity": persona["identity"],
                "situation": persona["situation"],
                "psychology": persona.get("psychology", []),
                "searchExample": persona.get("searchJourney", [{}])[0].get("example", ""),
                "observedQueryMatches": observed,
                "recommended": sum(row["systemStatus"] == "recommended" for row in rows),
                "highestScore": max((row["score"] for row in rows), default=0),
            }
        )

    replenishment = settings.get("replenishment", {})
    minimum_backlog = int(replenishment.get("minimumEligibleBacklog", 12))
    minimum_per_persona = int(replenishment.get("minimumPerPersona", 3))
    eligible_by_persona = Counter(row["personaId"] for row in selected)
    replenish_personas = [
        {
            "personaId": persona["id"],
            "label": persona["label"],
            "current": eligible_by_persona.get(persona["id"], 0),
            "needed": max(0, minimum_per_persona - eligible_by_persona.get(persona["id"], 0)),
        }
        for persona in personas.values()
        if eligible_by_persona.get(persona["id"], 0) < minimum_per_persona
    ]
    total_replenishment_needed = max(
        max(0, minimum_backlog - len(selected)),
        sum(row["needed"] for row in replenish_personas),
    )

    exported_at = gsc_payload.get("exportedAt") if isinstance(gsc_payload, dict) else None
    inspection_count = len(inspection_lookup)
    matched_queries = sum(row["signals"]["queryMatches"] for row in decisions)
    learning_log = [
        f"Search Console 当前有 {len(query_rows)} 条查询样本，其中 {matched_queries} 次命中已登记的问题模式。",
        (
            f"已接入 {inspection_count} 条 URL 检查记录，可执行收录生命周期判断。"
            if inspection_count
            else "目前没有 URL 检查明细，系统只观察展示数据，不把未知写成未收录。"
        ),
        (
            f"本轮有 {len(selected)} 个选题达到研究门槛，分配由真实信号和评分产生。"
            if selected
            else "本轮没有选题达到研究门槛，不为了数量强行扩写。"
        ),
    ]
    if suppressed_clusters:
        learning_log.append(f"{len(suppressed_clusters)} 个问题簇进入 90 天暂停期。")
    if total_replenishment_needed:
        learning_log.append(f"合格选题库存不足，需要从人物搜索阶段补充 {total_replenishment_needed} 个独立问题。")
    else:
        learning_log.append("合格选题库存达到安全线，本轮不需要补题。")

    snapshot = {
        "generatedAt": now_iso(),
        "model": "persona-search-feedback-v1",
        "source": {
            "personas": "content-system/personas.json",
            "registry": "content-system/topic-registry.json",
            "searchConsole": "dashboard/search-console.json" if gsc_payload else "not-connected",
            "searchConsoleExportedAt": exported_at,
            "urlInspectionCount": inspection_count,
            "consultations": "dashboard/consultations.json" if CONSULTATIONS_PATH.exists() else "not-connected",
        },
        "summary": {
            "personas": len(persona_rows),
            "registeredCandidates": len(decisions),
            "eligibleCandidates": len(selected),
            "publishedUnderObservation": sum(bool(row["publishedUrl"]) for row in decisions),
            "actionRequired": len(task_rows),
            "retiredPatterns": len(patterns),
            "suppressedClusters": len(suppressed_clusters),
            "nextFeedbackReview": (today + timedelta(days=7)).isoformat(),
        },
        "adaptiveAllocation": {
            "limit": int(settings.get("dailyCandidateLimit", 30)),
            "selected": len(selected),
            "byTopic": allocation,
            "method": "每个有合格选题的角色先保留一个位置，其余按评分、真实查询、页面表现和咨询信号排序。",
        },
        "replenishment": {
            "needed": total_replenishment_needed,
            "minimumEligibleBacklog": minimum_backlog,
            "minimumPerPersona": minimum_per_persona,
            "maxProposalsPerPersonaPerRun": int(replenishment.get("maxProposalsPerPersonaPerRun", 2)),
            "personas": replenish_personas,
            "rule": "仅在合格库存不足时补题；每个新题必须来自人物搜索阶段、通过相似度检查并有两类资料。",
        },
        "personas": persona_rows,
        "recommendations": selected[:12],
        "editorialTasks": task_rows[:12],
        "decisions": sorted(decisions, key=lambda row: row["score"], reverse=True),
        "feedbackRules": [
            {"window": "0-45 天", "action": "检查可抓取、sitemap 和内容质量，只观察收录。"},
            {"window": "46-74 天", "action": "技术正常但明确未收录时，只做一次有实质新增的补强。"},
            {"window": "75 天以上", "action": "明确未收录且无展示、点击、咨询时，停止该搜索模式。"},
            {"window": "任何时间", "action": "有展示但点击弱时改标题和开头；有咨询时提高同类问题优先级。"},
        ],
        "suppressedClusters": sorted(suppressed_clusters),
        "learningLog": learning_log,
    }

    for candidate in registry.get("candidates", []):
        decision = next((row for row in decisions if row["id"] == candidate.get("id")), None)
        if not decision:
            continue
        candidate["systemStatus"] = decision["systemStatus"]
        candidate["score"] = decision["score"]
        candidate["lastEvaluatedAt"] = today.isoformat()
        if decision["systemStatus"] == "retired" and not candidate.get("retiredAt"):
            candidate["retiredAt"] = today.isoformat()
    registry["updatedAt"] = today.isoformat()
    registry["retiredPatterns"] = patterns
    registry["learningLog"] = learning_log
    return snapshot, registry


def refresh() -> dict:
    snapshot, registry = build_snapshot()
    write_json(REGISTRY_PATH, registry)
    write_json(SNAPSHOT_PATH, snapshot)
    print(f"wrote {SNAPSHOT_PATH.relative_to(ROOT)}")
    print("personas:", snapshot["summary"]["personas"])
    print("eligible candidates:", snapshot["summary"]["eligibleCandidates"])
    print("action required:", snapshot["summary"]["actionRequired"])
    return snapshot


def print_report(snapshot: dict) -> None:
    summary = snapshot.get("summary", {})
    print("Topic engine", snapshot.get("model"))
    print("Registered:", summary.get("registeredCandidates"))
    print("Eligible:", summary.get("eligibleCandidates"))
    print("Actions:", summary.get("actionRequired"))
    print("Retired patterns:", summary.get("retiredPatterns"))
    for row in snapshot.get("recommendations", []):
        print(f"{row['score']:>3}  {row['id']}  {row['primaryQuery']}")


def read_csv_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def first_value(row: dict, names: list[str]) -> Any:
    lowered = {str(key).strip().casefold(): value for key, value in row.items()}
    for name in names:
        if name.casefold() in lowered:
            return lowered[name.casefold()]
    return ""


def convert_gsc_csv(path: Path, kind: str) -> list[dict]:
    rows = []
    for raw in read_csv_rows(path):
        key = first_value(
            raw,
            ["query", "top queries", "热门查询", "查询"] if kind == "query"
            else ["page", "url", "top pages", "网页", "页面"],
        )
        if not key:
            continue
        item = {
            "query" if kind == "query" else "url": str(key).strip(),
            "clicks": int(safe_number(first_value(raw, ["clicks", "点击次数", "点击"]))),
            "impressions": int(safe_number(first_value(raw, ["impressions", "展示次数", "展示"]))),
        }
        ctr = first_value(raw, ["ctr", "点击率"])
        position = first_value(raw, ["position", "平均排名", "排名"])
        if ctr != "":
            item["ctr"] = safe_number(ctr)
        if position != "":
            item["position"] = safe_number(position)
        rows.append(item)
    return rows


def ingest_gsc(queries_path: Path | None, pages_path: Path | None) -> None:
    payload = read_json(SEARCH_CONSOLE_PATH, {})
    if not isinstance(payload, dict):
        payload = {}
    performance = payload.setdefault("performance", {})
    if queries_path:
        performance["topQueries"] = convert_gsc_csv(queries_path, "query")
    if pages_path:
        performance["topPages"] = convert_gsc_csv(pages_path, "page")
    payload["exportedAt"] = today_iso()
    payload["source"] = "Google Search Console CSV export imported by tools/topic_engine.py"
    payload.setdefault("urls", [])
    write_json(SEARCH_CONSOLE_PATH, payload)
    print(f"updated {SEARCH_CONSOLE_PATH.relative_to(ROOT)}")


def ingest_inspections(path: Path) -> None:
    incoming = read_json(path, [])
    if isinstance(incoming, dict):
        incoming = incoming.get("urls") or incoming.get("rows") or [incoming]
    payload = read_json(SEARCH_CONSOLE_PATH, {})
    existing = payload.get("urls", []) if isinstance(payload, dict) else []
    lookup = {
        str(row.get("url") or row.get("inspectionUrl") or "").rstrip("/"): row
        for row in existing
        if row.get("url") or row.get("inspectionUrl")
    }
    for raw in incoming if isinstance(incoming, list) else []:
        result = raw.get("inspectionResult", raw) if isinstance(raw, dict) else {}
        status = result.get("indexStatusResult", result) if isinstance(result, dict) else {}
        url = str(
            status.get("inspectionUrl")
            or status.get("url")
            or raw.get("inspectionUrl")
            or raw.get("url")
            or ""
        ).rstrip("/")
        if not url:
            continue
        lookup[url] = {
            "url": url,
            "verdict": status.get("verdict", "unknown"),
            "coverageState": status.get("coverageState", ""),
            "lastCrawlTime": status.get("lastCrawlTime", ""),
            "googleCanonical": status.get("googleCanonical", ""),
            "userCanonical": status.get("userCanonical", ""),
            "inspectedAt": today_iso(),
        }
    if not isinstance(payload, dict):
        payload = {}
    payload["urls"] = sorted(lookup.values(), key=lambda row: row["url"])
    write_json(SEARCH_CONSOLE_PATH, payload)
    print(f"updated {len(lookup)} URL inspection records")


def next_candidate_id(topic: str, candidates: list[dict]) -> str:
    prefixes = {
        "hk-inheritance": "TE-HK",
        "macau": "TE-MO",
        "singapore": "TE-SG",
        "united-states": "TE-US",
    }
    prefix = prefixes.get(topic, "TE-XX")
    numbers = []
    for row in candidates:
        match = re.fullmatch(rf"{re.escape(prefix)}-(\d+)", str(row.get("id") or ""))
        if match:
            numbers.append(int(match.group(1)))
    return f"{prefix}-{max(numbers, default=0) + 1:03d}"


def ingest_proposals(path: Path) -> dict:
    incoming = read_json(path, [])
    if isinstance(incoming, dict):
        incoming = incoming.get("candidates", [])
    if not isinstance(incoming, list):
        raise SystemExit("proposal file must be a JSON list or contain a candidates list")

    personas_payload = read_json(PERSONAS_PATH, {})
    registry = read_json(REGISTRY_PATH, {})
    personas = {row["id"]: row for row in personas_payload.get("personas", [])}
    clusters = {row["id"]: row for row in registry.get("clusters", [])}
    candidates = registry.setdefault("candidates", [])
    settings = registry.get("settings", {})
    replenishment = settings.get("replenishment", {})
    threshold = float(replenishment.get("similarityThreshold", 0.62))
    minimum_sources = int(settings.get("minimumEvidenceSources", 2))
    max_per_persona = int(replenishment.get("maxProposalsPerPersonaPerRun", 2))
    per_persona = Counter()
    accepted = []
    rejected = []

    required = [
        "personaId",
        "clusterId",
        "title",
        "primaryQuery",
        "surfaceIntent",
        "deepIntent",
        "contextIntent",
    ]
    for proposal in incoming:
        if not isinstance(proposal, dict):
            rejected.append({"title": "", "reason": "proposal is not an object"})
            continue
        missing = [key for key in required if not str(proposal.get(key) or "").strip()]
        persona = personas.get(proposal.get("personaId"))
        cluster = clusters.get(proposal.get("clusterId"))
        title = str(proposal.get("title") or "").strip()
        if missing:
            rejected.append({"title": title, "reason": f"missing fields: {', '.join(missing)}"})
            continue
        if not persona:
            rejected.append({"title": title, "reason": "unknown persona"})
            continue
        if not cluster or cluster.get("topic") != persona.get("topic"):
            rejected.append({"title": title, "reason": "cluster does not belong to the persona topic"})
            continue
        if per_persona[persona["id"]] >= max_per_persona:
            rejected.append({"title": title, "reason": "persona proposal limit reached for this run"})
            continue
        evidence = proposal.get("evidenceSources", [])
        if not isinstance(evidence, list) or len([row for row in evidence if str(row).strip()]) < minimum_sources:
            rejected.append({"title": title, "reason": f"fewer than {minimum_sources} evidence sources"})
            continue
        if proposal.get("distinctValue") is not True:
            rejected.append({"title": title, "reason": "distinctValue must be true after comparison with existing pages"})
            continue
        phrases = proposal.get("matchPhrases", [])
        if not isinstance(phrases, list) or not any(len(normalise(row)) >= 4 for row in phrases):
            rejected.append({"title": title, "reason": "no usable match phrase"})
            continue

        closest = None
        closest_score = 0.0
        for existing in candidates:
            similarity = max(
                text_similarity(proposal["primaryQuery"], existing.get("primaryQuery", "")),
                text_similarity(title, existing.get("title", "")),
            )
            if similarity > closest_score:
                closest_score = similarity
                closest = existing
        if closest_score >= threshold:
            rejected.append(
                {
                    "title": title,
                    "reason": f"too similar to {closest.get('id')} ({closest_score:.2f})",
                }
            )
            continue

        candidate = {
            "id": next_candidate_id(persona["topic"], candidates),
            "personaId": persona["id"],
            "clusterId": cluster["id"],
            "title": title,
            "primaryQuery": str(proposal["primaryQuery"]).strip(),
            "matchPhrases": [str(row).strip() for row in phrases if str(row).strip()],
            "surfaceIntent": str(proposal["surfaceIntent"]).strip(),
            "deepIntent": str(proposal["deepIntent"]).strip(),
            "contextIntent": str(proposal["contextIntent"]).strip(),
            "evidenceSources": [str(row).strip() for row in evidence if str(row).strip()],
            "distinctValue": True,
            "publishedUrl": "",
            "status": "candidate",
            "improvements": 0,
            "createdAt": today_iso(),
        }
        candidates.append(candidate)
        per_persona[persona["id"]] += 1
        accepted.append({"id": candidate["id"], "title": candidate["title"]})

    registry["updatedAt"] = today_iso()
    write_json(REGISTRY_PATH, registry)
    result = {"accepted": accepted, "rejected": rejected}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Jingwei persona-led adaptive article topic engine")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("refresh")
    subparsers.add_parser("report")
    next_parser = subparsers.add_parser("next")
    next_parser.add_argument("--limit", type=int, default=12)
    gsc_parser = subparsers.add_parser("ingest-gsc")
    gsc_parser.add_argument("--queries", type=Path)
    gsc_parser.add_argument("--pages", type=Path)
    inspection_parser = subparsers.add_parser("ingest-inspections")
    inspection_parser.add_argument("file", type=Path)
    proposal_parser = subparsers.add_parser("propose")
    proposal_parser.add_argument("file", type=Path)
    args = parser.parse_args()

    if args.command == "refresh":
        refresh()
    elif args.command == "report":
        snapshot = read_json(SNAPSHOT_PATH, {}) or refresh()
        print_report(snapshot)
    elif args.command == "next":
        snapshot = read_json(SNAPSHOT_PATH, {}) or refresh()
        print(json.dumps(snapshot.get("recommendations", [])[: args.limit], ensure_ascii=False, indent=2))
    elif args.command == "ingest-gsc":
        if not args.queries and not args.pages:
            parser.error("ingest-gsc requires --queries or --pages")
        ingest_gsc(args.queries, args.pages)
        refresh()
    elif args.command == "ingest-inspections":
        ingest_inspections(args.file)
        refresh()
    elif args.command == "propose":
        ingest_proposals(args.file)
        refresh()


if __name__ == "__main__":
    main()
