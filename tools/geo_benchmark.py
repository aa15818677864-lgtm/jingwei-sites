from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content-system"
BENCHMARK_PATH = CONTENT_DIR / "geo-benchmark.json"
RESULTS_PATH = CONTENT_DIR / "geo-benchmark-results.json"
GEO_PATH = ROOT / "dashboard" / "geo.json"


CASES = [
    {
        "id": "hk-recognise",
        "persona": "hk-family-coordinator",
        "topic": "hk-inheritance",
        "stage": "recognise",
        "queries": {
            "zh-Hant": "香港家人要繼承內地房產，第一步應該先查甚麼？",
            "zh-Hans": "香港家人要继承内地房产，第一步应该先查什么？",
            "en": "What should a Hong Kong family check first before dealing with inherited property in Mainland China?",
        },
    },
    {
        "id": "hk-locate",
        "persona": "hk-family-coordinator",
        "topic": "hk-inheritance",
        "stage": "locate",
        "queries": {
            "zh-Hant": "只知道父親在深圳留過資產，沒有賬戶號碼可以怎樣開始查？",
            "zh-Hans": "只知道父亲在深圳留过资产，没有账户号码可以怎样开始查？",
            "en": "How can a Hong Kong family start tracing a deceased parent's assets in Shenzhen without account numbers?",
        },
    },
    {
        "id": "hk-prepare",
        "persona": "hk-family-coordinator",
        "topic": "hk-inheritance",
        "stage": "prepare",
        "queries": {
            "zh-Hant": "香港死亡證明和親屬關係資料交到內地前要先核對哪些地方？",
            "zh-Hans": "香港死亡证明和亲属关系资料交到内地前要先核对哪些地方？",
            "en": "What details should be checked before Hong Kong death and family records are used for a Mainland China inheritance matter?",
        },
    },
    {
        "id": "hk-blocked",
        "persona": "hk-family-coordinator",
        "topic": "hk-inheritance",
        "stage": "blocked",
        "queries": {
            "zh-Hant": "一名繼承人不肯簽字，其他香港家屬還可以先做哪些事？",
            "zh-Hans": "一名继承人不肯签字，其他香港家属还可以先做哪些事？",
            "en": "What can the rest of a Hong Kong family do when one heir refuses to sign for a Mainland China estate?",
        },
    },
    {
        "id": "hk-act",
        "persona": "hk-family-coordinator",
        "topic": "hk-inheritance",
        "stage": "act",
        "queries": {
            "zh-Hant": "人在香港不能經常回內地，怎樣委託律師處理繼承才不容易反覆補簽？",
            "zh-Hans": "人在香港不能经常回内地，怎样委托律师处理继承才不容易反复补签？",
            "en": "How should a Hong Kong resident appoint a Mainland China lawyer for an inheritance matter without repeated signing?",
        },
    },
    {
        "id": "macau-recognise",
        "persona": "macau-owner-operator",
        "topic": "macau",
        "stage": "recognise",
        "queries": {
            "zh-Hant": "澳門居民在珠海碰到欠款和家庭資產問題，應先分開處理嗎？",
            "zh-Hans": "澳门居民在珠海碰到欠款和家庭资产问题，应先分开处理吗？",
            "en": "Should a Macau resident separate a Zhuhai business debt from a family asset issue before taking legal action?",
        },
    },
    {
        "id": "macau-locate",
        "persona": "macau-owner-operator",
        "topic": "macau",
        "stage": "locate",
        "queries": {
            "zh-Hant": "澳門公司要追內地欠款，沒有完整付款記錄時先整理甚麼？",
            "zh-Hans": "澳门公司要追内地欠款，没有完整付款记录时先整理什么？",
            "en": "What should a Macau company collect first when pursuing a Mainland China debt with incomplete payment records?",
        },
    },
    {
        "id": "macau-prepare",
        "persona": "macau-owner-operator",
        "topic": "macau",
        "stage": "prepare",
        "queries": {
            "zh-Hant": "在澳門簽的授權書交到內地使用前，要先確定用途還是先做文件手續？",
            "zh-Hans": "在澳门签的授权书交到内地使用前，要先确定用途还是先做文件手续？",
            "en": "Before a Macau power of attorney is used in Mainland China, should its exact purpose be confirmed first?",
        },
    },
    {
        "id": "macau-blocked",
        "persona": "macau-owner-operator",
        "topic": "macau",
        "stage": "blocked",
        "queries": {
            "zh-Hant": "內地欠款人失聯，澳門公司先查資產、發函還是準備起訴？",
            "zh-Hans": "内地欠款人失联，澳门公司先查资产、发函还是准备起诉？",
            "en": "If a Mainland China debtor disappears, should a Macau company trace assets, send a demand, or prepare litigation first?",
        },
    },
    {
        "id": "macau-act",
        "persona": "macau-owner-operator",
        "topic": "macau",
        "stage": "act",
        "queries": {
            "zh-Hant": "本人不能常去內地，澳門客戶委託內地律師時要先說清哪些工作範圍？",
            "zh-Hans": "本人不能常去内地，澳门客户委托内地律师时要先说清哪些工作范围？",
            "en": "What scope should a Macau client define when appointing a Mainland China lawyer for remote legal work?",
        },
    },
    {
        "id": "sg-recognise",
        "persona": "singapore-bilingual-professional",
        "topic": "singapore",
        "stage": "recognise",
        "queries": {
            "zh-Hant": "新加坡居民繼承廣州房產，一開始應先釐清哪些人和哪些資產？",
            "zh-Hans": "新加坡居民继承广州房产，一开始应先厘清哪些人和哪些资产？",
            "en": "What people and assets should a Singapore resident identify first when inheriting property in Guangzhou?",
        },
    },
    {
        "id": "sg-locate",
        "persona": "singapore-bilingual-professional",
        "topic": "singapore",
        "stage": "locate",
        "queries": {
            "zh-Hant": "家人在內地可能留有房產和公司股權，新加坡家屬怎樣先做資產線索表？",
            "zh-Hans": "家人在内地可能留有房产和公司股权，新加坡家属怎样先做资产线索表？",
            "en": "How can a Singapore family build an asset clue list for property and company interests left in Mainland China?",
        },
    },
    {
        "id": "sg-prepare",
        "persona": "singapore-bilingual-professional",
        "topic": "singapore",
        "stage": "prepare",
        "queries": {
            "zh-Hant": "英文證件姓名和內地舊中文姓名不同，辦繼承前怎樣證明是同一人？",
            "zh-Hans": "英文证件姓名和内地旧中文姓名不同，办继承前怎样证明是同一人？",
            "en": "How can an heir connect an English passport name with an older Chinese name before a Mainland China inheritance case?",
        },
    },
    {
        "id": "sg-blocked",
        "persona": "singapore-bilingual-professional",
        "topic": "singapore",
        "stage": "blocked",
        "queries": {
            "zh-Hant": "繼承人分散在新加坡、香港和內地，文件簽署順序怎樣安排？",
            "zh-Hans": "继承人分散在新加坡、香港和内地，文件签署顺序怎样安排？",
            "en": "How should documents be sequenced when heirs are spread across Singapore, Hong Kong, and Mainland China?",
        },
    },
    {
        "id": "sg-act",
        "persona": "singapore-bilingual-professional",
        "topic": "singapore",
        "stage": "act",
        "queries": {
            "zh-Hant": "從新加坡遠程委託內地律師處理房產和股權，哪些決定仍要家屬自己作？",
            "zh-Hans": "从新加坡远程委托内地律师处理房产和股权，哪些决定仍要家属自己作？",
            "en": "Which decisions must a Singapore family still make when a Mainland China lawyer handles property and shares remotely?",
        },
    },
    {
        "id": "us-recognise",
        "persona": "us-overseas-decision-maker",
        "topic": "united-states",
        "stage": "recognise",
        "queries": {
            "zh-Hant": "人在美國能不能不回內地處理父母留下的房產繼承？",
            "zh-Hans": "人在美国能不能不回内地处理父母留下的房产继承？",
            "en": "Can I deal with property inherited from my parents in Mainland China while remaining in the United States?",
        },
    },
    {
        "id": "us-locate",
        "persona": "us-overseas-decision-maker",
        "topic": "united-states",
        "stage": "locate",
        "queries": {
            "zh-Hant": "只記得父母內地房子的舊地址，住在美國的子女還能怎樣查線索？",
            "zh-Hans": "只记得父母内地房子的旧地址，住在美国的子女还能怎样查线索？",
            "en": "How can a child living in the US trace a parent's Mainland China property with only an old address?",
        },
    },
    {
        "id": "us-prepare",
        "persona": "us-overseas-decision-maker",
        "topic": "united-states",
        "stage": "prepare",
        "queries": {
            "zh-Hant": "美國簽署的授權文件要交給內地房管或法院，內容應先怎樣按用途準備？",
            "zh-Hans": "美国签署的授权文件要交给内地房管或法院，内容应先怎样按用途准备？",
            "en": "How should a US power of attorney be tailored before it is used with a Mainland China property office or court?",
        },
    },
    {
        "id": "us-blocked",
        "persona": "us-overseas-decision-maker",
        "topic": "united-states",
        "stage": "blocked",
        "queries": {
            "zh-Hant": "家人爭議內地遺產又有人收租，住在美國的繼承人先保存哪些證據？",
            "zh-Hans": "家人争议内地遗产又有人收租，住在美国的继承人先保存哪些证据？",
            "en": "What evidence should a US-based heir preserve when relatives dispute a Mainland China estate and one person collects rent?",
        },
    },
    {
        "id": "us-act",
        "persona": "us-overseas-decision-maker",
        "topic": "united-states",
        "stage": "act",
        "queries": {
            "zh-Hant": "美國華人家庭找內地訴訟律師時，第一次溝通應提供哪些資料？",
            "zh-Hans": "美国华人家庭找内地诉讼律师时，第一次沟通应提供哪些资料？",
            "en": "What should a Chinese American family provide in the first call with a Mainland China litigation lawyer?",
        },
    },
]


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build() -> dict:
    prompts = []
    for case in CASES:
        for language, query in case["queries"].items():
            prompts.append(
                {
                    "id": f'{case["id"]}-{language.lower()}',
                    "caseId": case["id"],
                    "persona": case["persona"],
                    "topic": case["topic"],
                    "stage": case["stage"],
                    "language": language,
                    "query": query,
                }
            )
    if len(prompts) != 60 or len({row["id"] for row in prompts}) != 60:
        raise ValueError("GEO benchmark must contain 60 unique prompts")
    payload = {
        "version": 1,
        "updatedAt": datetime.now(timezone.utc).date().isoformat(),
        "brand": "Liu Yi Lawyer Team",
        "cadence": {"weeklySample": 12, "monthlyFullRun": 60},
        "platforms": ["Google AI / Gemini", "ChatGPT Search", "Bing / Copilot", "Perplexity", "Claude Search"],
        "recordFields": ["runAt", "platform", "promptId", "mentioned", "cited", "citedUrl", "notes"],
        "prompts": prompts,
    }
    write_json(BENCHMARK_PATH, payload)
    return payload


def apply_results() -> dict:
    benchmark = build()
    geo = json.loads(GEO_PATH.read_text(encoding="utf-8"))
    if not RESULTS_PATH.exists():
        print(f"No results yet: {RESULTS_PATH.relative_to(ROOT)}")
        return geo
    payload = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    results = payload.get("results", []) if isinstance(payload, dict) else []
    valid_ids = {row["id"] for row in benchmark["prompts"]}
    rows = [row for row in results if row.get("promptId") in valid_ids and row.get("platform")]
    if not rows:
        print("No valid benchmark results yet")
        return geo

    latest = {}
    for row in rows:
        key = (row["platform"], row["promptId"])
        if key not in latest or str(row.get("runAt", "")) > str(latest[key].get("runAt", "")):
            latest[key] = row
    rows = list(latest.values())
    geo["benchmark"]["lastRun"] = max((row.get("runAt") for row in rows if row.get("runAt")), default=None)
    geo["benchmark"]["mentionRate"] = round(sum(bool(row.get("mentioned")) for row in rows) / len(rows), 4)
    geo["benchmark"]["citationRate"] = round(sum(bool(row.get("cited")) for row in rows) / len(rows), 4)
    geo["dataSources"]["promptBenchmark"] = "connected"
    for platform in geo.get("platforms", []):
        matched = [row for row in rows if row.get("platform") == platform.get("name")]
        platform["citationCount"] = sum(bool(row.get("cited")) for row in matched) if matched else None
    write_json(GEO_PATH, geo)
    return geo


def main() -> None:
    parser = argparse.ArgumentParser(description="Build and aggregate the 60-prompt GEO benchmark")
    parser.add_argument("command", choices=("build", "report", "validate"), nargs="?", default="build")
    args = parser.parse_args()
    if args.command == "report":
        geo = apply_results()
        print(json.dumps(geo.get("benchmark", {}), ensure_ascii=False))
        return
    payload = build()
    print(f'wrote {BENCHMARK_PATH.relative_to(ROOT)} with {len(payload["prompts"])} prompts')


if __name__ == "__main__":
    main()
