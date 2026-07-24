#!/usr/bin/env python3
"""Maintain the 150-story regional foundation plan and its review gate."""

from __future__ import annotations

import argparse
import json
from copy import deepcopy
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PLAN = ROOT / "content-system" / "regional-foundation-150.json"
REQUIRED_REVIEW_FOCI = (
    "legal-and-regional-accuracy",
    "human-readability-and-five-reader-roles",
    "trilingual-visual-seo-and-mobile",
)
READY_STATUSES = {"ready", "published"}
ALLOWED_STATUSES = {
    "planned",
    "researching",
    "drafting",
    "reviewing",
    "visuals",
    "ready",
    "published",
    "upgrade-required",
    "paused",
}


def topic(cluster: str, slug: str, title: str) -> dict[str, str]:
    return {"cluster": cluster, "slug": slug, "title": title}


TOPICS: dict[str, list[dict[str, str]]] = {
    "MO": [
        topic("getting-started", "macau-family-mainland-property-inheritance", "澳门家属继承内地房产，第一步先分清哪两套文件"),
        topic("getting-started", "macau-client-mainland-lawyer", "人在澳门，怎样委托内地律师处理继承事务"),
        topic("getting-started", "unknown-mainland-property-city", "只知道家人在内地有房，澳门家属怎样先找城市和地址线索"),
        topic("getting-started", "habitual-residence-and-mainland-assets", "亲人在澳门离世，常居地和内地资产所在地分别影响什么"),
        topic("getting-started", "family-coordinator-first-sheet", "继承人很多，澳门家庭怎样先选一名联络人整理事实"),
        topic("documents", "macau-death-record-for-mainland-inheritance", "澳门死亡记录用于内地继承，先核对哪些内容"),
        topic("documents", "macau-kinship-certificate-scope", "澳门亲属关系证明能说明什么，不能代替什么"),
        topic("documents", "macau-heir-qualification-deed", "澳门确认继承人资格公证书，什么时候值得先办"),
        topic("documents", "portuguese-documents-translation", "澳门葡文文件交到内地前，翻译最容易漏掉什么"),
        topic("documents", "macau-mainland-name-mismatch", "澳门证件和内地房产登记姓名不一致，怎样先连成同一个人"),
        topic("will-and-administration", "macau-will-mainland-property", "澳门遗嘱写到内地房产，家属先核对哪三件事"),
        topic("will-and-administration", "macau-no-will-mainland-property", "没有遗嘱，澳门家属处理内地房产从哪里开始"),
        topic("will-and-administration", "multiple-wills-across-regions", "家里找到几份遗嘱，澳门和内地文件怎样先排时间线"),
        topic("will-and-administration", "estate-manager-role-boundary", "待分割财产管理人能做什么，哪些决定仍要继承人确认"),
        topic("will-and-administration", "undisputed-or-disputed-route", "澳门家属意见一致和有人反对，内地继承路径有什么不同"),
        topic("property", "sole-title-and-spousal-share", "内地房产只登记一人姓名，是否仍要先查配偶份额"),
        topic(
            "documents",
            "omitted-heir-after-macau-qualification-deed",
            "澳门继承人资格公证书办好后，才发现漏了一名家人怎么办",
        ),
        topic("property", "missing-property-certificate", "澳门家属找不到内地房产证，可以先从哪些线索补起"),
        topic("property", "mortgaged-mainland-property", "内地房产还有按揭，继承前先向谁确认欠款和状态"),
        topic("property", "occupied-or-sold-property", "内地房子被亲属占用或疑似出售，澳门家属先保留什么"),
        topic("property", "transfer-before-sale", "继承内地房产是先转名还是直接出售，怎样判断"),
        topic("bank-and-benefits", "macau-heirship-document-mainland-bank-checklist", "澳门确认继承资格文件拿到后，内地银行还会核对什么"),
        topic("bank-and-benefits", "unknown-mainland-bank-accounts", "不知道内地存款在哪家银行，先做哪一张线索表"),
        topic("bank-and-benefits", "joint-bank-account-after-death", "内地联名账户有人去世，余额不能只看账户姓名"),
        topic("bank-and-benefits", "social-insurance-and-housing-fund", "内地社保、公积金和单位款项，澳门家属怎样分开查询"),
        topic("company-and-equity", "mainland-company-shares", "亲人在内地公司有股权，澳门家属先查股东还是先办继承"),
        topic("company-and-equity", "deceased-legal-representative", "已故亲人是内地公司法定代表人，家属先处理哪一层问题"),
        topic("company-and-equity", "dividends-and-receivables", "内地公司尚有分红或应收款，怎样分清公司财产和遗产"),
        topic("company-and-equity", "missing-company-records", "公司资料不在家属手上，澳门继承人可先整理哪些公开线索"),
        topic("company-and-equity", "equity-inheritance-dispute", "其他股东不配合，澳门家属怎样先固定股权和沟通证据"),
        topic("remote-documents", "power-of-attorney-scope", "澳门签授权书处理内地继承，权限应写到多具体"),
        topic("remote-documents", "signing-in-macau", "人在澳门签继承文件，签字前先向内地接收方问什么"),
        topic("remote-documents", "macau-document-verification-route", "澳门文件交到内地使用，先分清核验、翻译和接收要求"),
        topic("remote-documents", "multiple-heirs-one-representative", "多名澳门继承人委托一人联络，哪些决定不能一并代替"),
        topic("remote-documents", "sending-original-documents", "澳门和内地往返寄原件，怎样先做清单和留底"),
        topic("disputes", "sibling-refuses-to-sign", "有兄弟姊妹不签字，澳门家属先判断是资料问题还是继承争议"),
        topic("disputes", "missing-or-unreachable-heir", "有继承人失联，澳门家庭不要先假设他已放弃"),
        topic("disputes", "oral-will-or-missing-original", "只听说有遗嘱却找不到原件，先保留哪些人和文件线索"),
        topic("disputes", "relative-occupies-property", "亲属长期住在内地遗产房，继承和腾退要分开看"),
        topic("disputes", "urgent-evidence-preservation", "担心房产或资料被转移，澳门家属先固定哪几类证据"),
        topic("costs-and-aftercare", "inheritance-costs-and-taxes", "澳门家属继承内地房产，费用先按哪些项目问清"),
        topic("costs-and-aftercare", "inheritance-timeline-factors", "内地房产继承要多久，真正影响时间的是哪些事情"),
        topic("costs-and-aftercare", "rent-after-death", "内地遗产房仍在收租，租金和钥匙应由谁先保管"),
        topic("costs-and-aftercare", "management-fees-and-debts", "房屋欠管理费或其他债务，继承人先查数额还是先签文件"),
        topic("costs-and-aftercare", "sale-after-inheritance-transfer", "内地房产完成继承转名后出售，还要提前准备什么"),
        topic("special-families", "minor-heir", "有未成年继承人，澳门家庭哪些决定不能只由成年人商量"),
        topic("special-families", "heir-dies-during-process", "继承手续未完又有继承人去世，家族关系怎样重新梳理"),
        topic("special-families", "renounce-mainland-inheritance", "澳门继承人想放弃内地遗产，先查清资产和债务再决定"),
        topic("special-families", "estate-debts-and-legacies", "遗产既有房产也有债务或遗赠，澳门家属怎样分层处理"),
        topic("special-families", "family-settlement-agreement", "澳门家属达成分配意见后，协议应写清哪些现实安排"),
    ],
    "SG": [
        topic("getting-started", "mainland-property-inheritance", "新加坡家庭处理内地房产继承，第一步先查什么"),
        topic("getting-started", "probate-or-letters-of-administration", "Grant of Probate 和 Letters of Administration 有什么不同"),
        topic("getting-started", "domicile-and-mainland-asset-location", "亲人在新加坡离世，住所和内地资产所在地分别影响什么"),
        topic("getting-started", "mainland-property-in-schedule-of-assets", "内地房产是否已列入新加坡 Schedule of Assets，怎样先核对"),
        topic("getting-started", "singapore-family-first-fact-sheet", "新加坡家属第一次整理内地遗产，先做哪一页事实表"),
        topic("documents", "singapore-death-certificate", "新加坡死亡证明用于内地继承，先核对姓名和签发资料"),
        topic("documents", "original-will-verification", "新加坡原始遗嘱为什么要先保管好，扫描件能说明多少"),
        topic("documents", "english-chinese-name-mismatch", "英文姓名和中文姓名不一致，怎样证明是同一个人"),
        topic("documents", "singapore-apostille-for-mainland-use", "新加坡文件交到内地前，什么时候需要 SAL Apostille"),
        topic("documents", "singapore-document-translation", "英文继承文件翻成中文，哪些姓名和日期必须逐项核对"),
        topic("property", "sole-registered-mainland-property", "内地房产只登记父母一人姓名，新加坡家属先查哪几项"),
        topic("property", "co-owned-mainland-property", "内地房产多人共有，遗产范围怎样先算清"),
        topic("property", "mortgaged-mainland-property", "内地房产仍有按揭，新加坡继承人应先取得哪些信息"),
        topic("property", "rented-mainland-property", "内地遗产房正在出租，租金和租约先由谁整理"),
        topic("property", "transfer-or-direct-sale", "新加坡家属继承内地房产，先转名还是考虑出售"),
        topic("bank-and-benefits", "known-mainland-bank-deposit", "知道内地银行账户，新加坡家属先准备什么"),
        topic("bank-and-benefits", "unknown-mainland-bank-accounts", "不知道存款在哪家内地银行，怎样先找线索"),
        topic("bank-and-benefits", "joint-mainland-bank-account", "内地联名账户有人去世，余额归属不能只看持卡人"),
        topic("bank-and-benefits", "digital-payment-clues", "只找到手机和付款记录，怎样整理内地账户线索"),
        topic("bank-and-benefits", "remitting-inherited-funds", "内地继承款汇到新加坡前，应先保存哪些来源文件"),
        topic("company-and-equity", "mainland-company-shares", "亲人在内地公司有股权，新加坡家属先查什么"),
        topic("company-and-equity", "deceased-legal-representative", "已故亲人是内地公司法定代表人，家属先分清哪两件事"),
        topic("company-and-equity", "dividends-and-receivables", "内地公司分红和个人应收款，怎样避免混在一起"),
        topic("company-and-equity", "missing-company-records", "公司章程和股东资料不齐，新加坡家属先找哪些线索"),
        topic("company-and-equity", "trust-and-mainland-property", "新加坡信托安排写到内地房产，为什么仍要先查登记状态"),
        topic("remote-documents", "singapore-power-of-attorney", "新加坡授权书处理内地继承，权限怎样写得清楚"),
        topic("remote-documents", "notarisation-and-apostille", "公证和 Apostille 不是一回事，文件顺序怎样先问清"),
        topic("remote-documents", "multiple-heirs-one-contact", "多名继承人在不同国家，怎样先统一事实和签字顺序"),
        topic("remote-documents", "remote-identity-check", "新加坡继承人不能到内地，身份核对通常先准备什么"),
        topic("remote-documents", "sending-originals-to-mainland", "把新加坡原件寄到内地前，怎样留底和记录交接"),
        topic("disputes", "heir-refuses-to-sign", "有继承人拒绝签字，先判断他反对什么"),
        topic("disputes", "will-challenge", "有人质疑新加坡遗嘱，哪些争议不能靠重复做文件解决"),
        topic("disputes", "executor-conflict", "遗嘱执行人与家属意见不一，内地资产先由谁提供资料"),
        topic("disputes", "missing-heir", "有继承人失联，新加坡家庭先固定哪些联系记录"),
        topic("disputes", "occupied-mainland-property", "内地房产被亲属占用，新加坡继承人先查权属还是先谈腾退"),
        topic("special-families", "spouse-and-children", "配偶和子女同时在世，新加坡家庭先把关系图画清"),
        topic("special-families", "blended-family", "再婚家庭处理内地遗产，前段婚姻子女资料怎样整理"),
        topic("special-families", "minor-heir", "有未成年继承人，哪些分配决定需要特别谨慎"),
        topic("special-families", "heir-dies-during-process", "继承未办完又有继承人去世，文件不能沿用到哪一步"),
        topic("special-families", "renounce-inheritance", "新加坡继承人想放弃内地遗产，先查哪些债务和资产"),
        topic("costs-and-aftercare", "inheritance-costs-and-taxes", "新加坡家庭继承内地房产，费用应按什么项目询问"),
        topic("costs-and-aftercare", "inheritance-timeline", "跨境继承要多久，哪些文件最容易拖慢进度"),
        topic("costs-and-aftercare", "estate-debts", "遗产有债务，新加坡家属不要先把房产价值当成净额"),
        topic("costs-and-aftercare", "management-fees-and-utilities", "内地遗产房欠管理费和水电费，先怎样核数"),
        topic("costs-and-aftercare", "after-transfer-sale-preparation", "完成继承转名后准备出售，哪些旧资料仍要保留"),
        topic("special-routes", "muslim-estate-and-mainland-assets", "新加坡穆斯林遗产涉及内地资产，先分清哪些程序层次"),
        topic("special-routes", "citizenship-pr-and-identity", "公民、永久居民和旧国籍记录，对内地身份核对有什么影响"),
        topic("special-routes", "overseas-assets-in-estate-schedule", "新加坡遗产清单遗漏内地资产，家属先向谁核对"),
        topic("special-routes", "old-passport-and-chinese-name", "旧护照有中文名，新证件没有，怎样建立连续身份线索"),
        topic("special-routes", "family-settlement-agreement", "新加坡家属谈好分配后，跨境家庭协议应写清什么"),
    ],
    "US": [
        topic("getting-started", "us-documents-mainland-property-inheritance", "美国文件用于内地房产继承，先分清签发机关"),
        topic("getting-started", "remote-china-lawyer", "人在美国，怎样委托内地律师处理继承事务"),
        topic("getting-started", "issuing-state-matters", "美国文件由哪个州签发，为什么会改变 Apostille 路径"),
        topic("getting-started", "domicile-and-mainland-asset-location", "亲人在美国离世，住所州和内地资产所在地分别影响什么"),
        topic("getting-started", "mainland-asset-omitted-from-probate", "美国 probate 材料没写内地资产，家属先怎样核对"),
        topic("documents", "us-death-certificate-for-mainland", "美国死亡证明交到内地前，先看州、版本和姓名"),
        topic("documents", "us-will-and-mainland-property", "美国遗嘱写到内地房产，为什么还要查登记和继承关系"),
        topic("documents", "letters-testamentary-or-administration", "Letters Testamentary 和 Letters of Administration 分别说明什么"),
        topic("documents", "state-or-federal-apostille", "州文件和联邦文件的 Apostille 不能送错机关"),
        topic("documents", "us-document-translation-and-name", "英文文件翻成中文，姓名、日期和州县信息怎样核对"),
        topic("property", "sole-registered-mainland-property", "内地房产只登记已故亲人姓名，美国家属先查哪几项"),
        topic("property", "spousal-share-before-inheritance", "房产只写一人姓名，为什么仍要先判断配偶份额"),
        topic(
            "property",
            "california-inventory-mainland-property-value",
            "加州 probate 清单涉及内地房产，先分清估值日期和逝者份额",
        ),
        topic("property", "missing-mainland-title", "美国家属找不到内地房产证，可以先从哪些资料补线索"),
        topic("property", "transfer-or-direct-sale", "继承内地房产是先转名还是考虑出售，先确认什么"),
        topic("bank-and-benefits", "known-mainland-bank-deposit", "知道内地银行和账户，美国继承人先准备什么"),
        topic("bank-and-benefits", "unknown-mainland-bank-accounts", "不知道存款在哪家内地银行，先做哪些线索核对"),
        topic("bank-and-benefits", "joint-mainland-bank-account", "内地联名账户有人去世，余额不能只凭银行卡判断"),
        topic("bank-and-benefits", "digital-account-clues", "手机、短信和邮箱里有哪些内地资产线索值得保存"),
        topic("bank-and-benefits", "remitting-inherited-funds-to-us", "内地继承款汇到美国前，应先保存哪些来源材料"),
        topic("company-and-equity", "mainland-company-shares", "亲人在内地公司持股，美国家属先查股权还是先办 probate"),
        topic("company-and-equity", "deceased-legal-representative", "已故亲人是内地公司法定代表人，继承和公司变更要分开"),
        topic("company-and-equity", "dividends-and-receivables", "内地公司分红、借款和个人应收款怎样先分类"),
        topic("company-and-equity", "missing-company-records", "股东资料不在美国家属手里，先找哪些公开和家庭线索"),
        topic("company-and-equity", "us-trust-and-mainland-property", "美国 living trust 写到内地房产，为什么不能只看信托文件"),
        topic("remote-documents", "us-power-of-attorney", "美国签授权书处理内地继承，权限怎样写得不过宽"),
        topic("remote-documents", "state-notarisation-and-apostille", "州公证和州 Apostille 怎样衔接，先问清谁接收"),
        topic("remote-documents", "federal-document-apostille", "联邦文件用于内地事务，为什么不能送州务卿办理"),
        topic("remote-documents", "multiple-heirs-one-representative", "继承人分散在不同州，怎样先统一事实和授权范围"),
        topic("remote-documents", "mailing-originals-safely", "美国原件寄到内地前，怎样留底、编号和确认收件"),
        topic("disputes", "sibling-refuses-to-sign", "有兄弟姊妹拒绝签字，美国家庭先判断争议点"),
        topic("disputes", "will-challenge", "有人质疑美国遗嘱，内地资产处理为什么要先停下来核对"),
        topic("disputes", "executor-refuses-to-cooperate", "美国遗嘱执行人不配合提供文件，家属先保留什么"),
        topic("disputes", "missing-heir", "有继承人失联，美国家庭怎样记录查找过程"),
        topic("disputes", "occupied-mainland-property", "内地遗产房被亲属占用，权属确认和腾退怎样分开"),
        topic("special-families", "spouse-and-children", "配偶和子女同时在世，美国家庭先画哪一张关系图"),
        topic("special-families", "blended-family", "再婚家庭处理内地遗产，前段婚姻子女资料怎样核对"),
        topic("special-families", "adopted-child", "有收养子女，跨境继承前先准备哪些关系文件"),
        topic("special-families", "minor-heir", "有未成年继承人，内地房产分配哪些决定要特别谨慎"),
        topic("special-families", "heir-dies-during-process", "手续未完又有继承人去世，继承链怎样重新整理"),
        topic("costs-and-aftercare", "inheritance-costs-and-taxes", "美国家庭继承内地房产，费用和税务问题怎样分开问"),
        topic("costs-and-aftercare", "inheritance-timeline", "美国到内地的继承手续要多久，哪些环节最影响时间"),
        topic("costs-and-aftercare", "estate-debts-and-mortgage", "内地房产有按揭或其他债务，美国继承人先怎样核数"),
        topic("costs-and-aftercare", "rent-after-death", "内地遗产房仍在收租，租金、押金和钥匙先由谁记录"),
        topic("costs-and-aftercare", "renounce-inheritance", "美国继承人想放弃内地遗产，先查资产和债务再签文件"),
        topic("state-examples", "new-york-death-certificate", "纽约州死亡证明用于内地继承，先核对签发和 Apostille 路径"),
        topic("state-examples", "california-death-certificate", "加州死亡证明用于内地继承，先准备哪种副本"),
        topic("state-examples", "legal-name-change-records", "美国合法改名后，旧中文姓名怎样和内地房产记录衔接"),
        topic("state-examples", "supplemental-probate-materials", "发现内地资产后，美国 probate 文件是否需要补充，先问谁"),
        topic("state-examples", "family-settlement-agreement", "美国家属谈好分配后，跨境家庭协议应写清哪些执行事项"),
    ],
}


REGION_LABELS = {"MO": "澳门", "SG": "新加坡", "US": "美国"}


PUBLISHED_SEEDS = {
    "MO-001": {
        "status": "published",
        "publishedUrl": "https://www.jingwei-law.com/articles/am/macau-family-mainland-property-inheritance.html",
    },
    "SG-001": {
        "status": "published",
        "publishedUrl": "https://www.jingwei-law.com/articles/singapore/mainland-property-inheritance.html",
    },
    "US-001": {
        "status": "published",
        "publishedUrl": "https://www.jingwei-law.com/articles/us/us-documents-mainland-property-inheritance.html",
    },
}


UPGRADE_SEEDS = {
    "MO-002": "https://www.jingwei-law.com/articles/am/macau-client-mainland-lawyer.html",
    "US-002": "https://www.jingwei-law.com/articles/us/remote-china-lawyer.html",
}


def seeded_reviews(region: str, slug: str) -> list[dict]:
    common_date = "2026-07-24T00:00:00+08:00"
    return [
        {
            "round": 1,
            "focus": REQUIRED_REVIEW_FOCI[0],
            "problemsFound": [
                "繁体正文混入简体字和不一致标点，降低澳门、香港读者的可信感。"
            ],
            "fixesApplied": [
                "逐段改回自然繁体表达，并重新核对人物、资产、文件和条件性结论。"
            ],
            "evidence": ["UTF-8 text audit", "legal fact pass against internal source notes"],
            "reviewedAt": common_date,
        },
        {
            "round": 2,
            "focus": REQUIRED_REVIEW_FOCI[1],
            "problemsFound": [
                "初稿部分段落先讲概念，读者要到后面才看到自己下一步该做什么。"
            ],
            "fixesApplied": [
                "把直接答案、事实清单和第一步行动前移，并删除重复的模板化总结。"
            ],
            "evidence": ["five-reader-role readability pass", "article_ops audit"],
            "reviewedAt": common_date,
        },
        {
            "round": 3,
            "focus": REQUIRED_REVIEW_FOCI[2],
            "problemsFound": [
                "Article JSON-LD 缺少 author.url，英文第二张流程图在窄屏出现文字重叠。"
            ],
            "fixesApplied": [
                "补齐作者与发布者网址；重排窄屏 SVG 文本；当前语言改为 aria-current 非自链接。"
            ],
            "evidence": [
                f"three-language pages for {region}/{slug}",
                "geo_hardening audit: 0 errors",
                "Playwright mobile visual pass",
                "live URL returned 200",
            ],
            "reviewedAt": common_date,
        },
    ]


def new_record(region: str, index: int, item: dict[str, str]) -> dict:
    story_id = f"{region}-{index:03d}"
    record = {
        "id": story_id,
        "region": region,
        "regionLabel": REGION_LABELS[region],
        "position": index,
        "cluster": item["cluster"],
        "slug": item["slug"],
        "title": item["title"],
        "status": "planned",
        "publishedUrl": "",
        "research": [],
        "reviews": [],
        "languages": {"zh-Hant": "pending", "zh-Hans": "pending", "en": "pending"},
        "visuals": {"nativeAd": "pending"},
        "seo": {"canonical": "pending", "hreflang": "pending", "articleJsonLd": "pending", "sitemap": "pending"},
    }
    if story_id in PUBLISHED_SEEDS:
        record.update(PUBLISHED_SEEDS[story_id])
        record["research"] = [
            {"type": "regional-official", "status": "verified"},
            {"type": "mainland-receiving-route", "status": "verified"},
        ]
        record["reviews"] = seeded_reviews(region, item["slug"])
        record["languages"] = {"zh-Hant": "published", "zh-Hans": "published", "en": "published"}
        record["visuals"] = {"nativeAd": "published"}
        record["seo"] = {"canonical": "pass", "hreflang": "pass", "articleJsonLd": "pass", "sitemap": "pass"}
    elif story_id in UPGRADE_SEEDS:
        record["status"] = "upgrade-required"
        record["publishedUrl"] = UPGRADE_SEEDS[story_id]
    return record


def build_plan(existing: dict | None = None) -> dict:
    existing_by_id = {story["id"]: story for story in (existing or {}).get("stories", [])}
    stories = []
    for region, items in TOPICS.items():
        for index, item in enumerate(items, start=1):
            base = new_record(region, index, item)
            old = existing_by_id.get(base["id"])
            if old:
                preserved = deepcopy(old)
                preserved.update({key: base[key] for key in ("region", "regionLabel", "position", "cluster", "slug", "title")})
                base = preserved
            stories.append(base)
    return {
        "schemaVersion": 1,
        "objective": "澳门、新加坡、美国各50篇基础文章；每篇三轮实质审稿后才可发布。",
        "updatedAt": date.today().isoformat(),
        "reviewGate": {
            "minimumRounds": 3,
            "requiredFoci": list(REQUIRED_REVIEW_FOCI),
            "rule": "每轮必须记录真实问题、实际修改和验证证据；不得用“无问题”占位。",
        },
        "stories": stories,
    }


def load_plan(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_plan(path: Path, plan: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def review_errors(story: dict) -> list[str]:
    errors = []
    reviews = story.get("reviews", [])
    if story.get("status") not in READY_STATUSES:
        return errors
    if len(reviews) != 3:
        return [f"{story['id']}: ready/published requires exactly 3 reviews"]
    for expected_round, expected_focus in enumerate(REQUIRED_REVIEW_FOCI, start=1):
        review = reviews[expected_round - 1]
        if review.get("round") != expected_round:
            errors.append(f"{story['id']}: review {expected_round} has wrong round number")
        if review.get("focus") != expected_focus:
            errors.append(f"{story['id']}: review {expected_round} has wrong focus")
        for field in ("problemsFound", "fixesApplied", "evidence"):
            values = review.get(field, [])
            if not values or not all(str(value).strip() for value in values):
                errors.append(f"{story['id']}: review {expected_round} needs non-empty {field}")
        if not review.get("reviewedAt"):
            errors.append(f"{story['id']}: review {expected_round} needs reviewedAt")
    return errors


def audit(plan: dict) -> list[str]:
    errors = []
    stories = plan.get("stories", [])
    if len(stories) != 150:
        errors.append(f"plan has {len(stories)} stories; expected 150")
    ids = [story.get("id") for story in stories]
    if len(set(ids)) != len(ids):
        errors.append("story ids are not unique")
    for region in TOPICS:
        regional = [story for story in stories if story.get("region") == region]
        if len(regional) != 50:
            errors.append(f"{region} has {len(regional)} stories; expected 50")
        expected_ids = [f"{region}-{index:03d}" for index in range(1, 51)]
        if [story.get("id") for story in regional] != expected_ids:
            errors.append(f"{region} ids or ordering are not continuous")
    titles = [story.get("title", "").strip() for story in stories]
    if len(set(titles)) != len(titles):
        errors.append("story titles are not unique")
    region_slugs = [(story.get("region"), story.get("slug")) for story in stories]
    if len(set(region_slugs)) != len(region_slugs):
        errors.append("story slugs are not unique inside a region")
    for story in stories:
        if story.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{story.get('id')}: invalid status {story.get('status')}")
        errors.extend(review_errors(story))
        if story.get("status") == "published":
            if not story.get("publishedUrl"):
                errors.append(f"{story['id']}: published story is missing publishedUrl")
            if any(value != "published" for value in story.get("languages", {}).values()):
                errors.append(f"{story['id']}: published story is missing a language page")
            if any(value != "published" for value in story.get("visuals", {}).values()):
                errors.append(f"{story['id']}: published story is missing a visual")
            if any(value != "pass" for value in story.get("seo", {}).values()):
                errors.append(f"{story['id']}: published story has an incomplete SEO gate")
    for region in TOPICS:
        regional = [story for story in stories if story.get("region") == region]
        for left_index, left in enumerate(regional):
            for right in regional[left_index + 1 :]:
                similarity = SequenceMatcher(None, left["title"], right["title"]).ratio()
                if similarity >= 0.88:
                    errors.append(
                        f"{region}: near-duplicate titles {left['id']} and {right['id']} ({similarity:.2f})"
                    )
    return errors


def summary(plan: dict) -> str:
    lines = ["Regional foundation 150"]
    for region in TOPICS:
        stories = [story for story in plan["stories"] if story["region"] == region]
        counts = {status: sum(story["status"] == status for story in stories) for status in sorted(ALLOWED_STATUSES)}
        active_counts = ", ".join(f"{status}={count}" for status, count in counts.items() if count)
        complete = counts.get("published", 0)
        lines.append(f"{region} {REGION_LABELS[region]}: {complete}/50 published; {active_counts}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("bootstrap", "audit", "summary"))
    parser.add_argument("--plan", type=Path, default=DEFAULT_PLAN)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "bootstrap":
        existing = load_plan(args.plan) if args.plan.exists() else None
        plan = build_plan(existing)
        errors = audit(plan)
        if errors:
            print("\n".join(errors))
            return 1
        write_plan(args.plan, plan)
        print(summary(plan))
        print(f"Wrote {args.plan}")
        return 0
    if not args.plan.exists():
        print(f"Missing plan: {args.plan}")
        return 1
    plan = load_plan(args.plan)
    if args.command == "summary":
        print(summary(plan))
        return 0
    errors = audit(plan)
    if errors:
        print("\n".join(errors))
        return 1
    print("Regional foundation audit: 0 errors")
    print(summary(plan))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
