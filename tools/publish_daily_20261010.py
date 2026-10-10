"""Publish the prepared 2026-10-10 article batch without touching the divorce topic."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DRAFT_DIR = ROOT / "content-drafts" / "daily-20261010"
DATE = "2026-10-10"
BASE = "https://www.jingwei-law.com"
PROTECTED = {"lh.html", "lh-thanks.html"}


STORIES = {
    "HK-053": {
        "folder": "hong-kong-other-estate",
        "slug": "mainland-patent-application-after-death",
        "topic": {"zh-Hant": "香港家屬與內地知識產權", "zh-Hans": "香港家属与内地知识产权", "en": "Hong Kong families and Mainland intellectual property"},
        "titles": {
            "zh-Hant": "內地專利申請人離世、申請還未辦完，香港家屬先查哪一個狀態",
            "zh-Hans": "内地专利申请人离世、申请还未办完，香港家属先查哪一个状态",
            "en": "A Mainland patent applicant has died: what should a Hong Kong family check first?",
        },
        "fallback": "/articles/hong-kong-other-estate/",
    },
    "HK-054": {
        "folder": "hong-kong-other-estate",
        "slug": "mainland-unpublished-work-inheritance",
        "topic": {"zh-Hant": "香港家屬與內地著作權", "zh-Hans": "香港家属与内地著作权", "en": "Hong Kong families and Mainland copyright"},
        "titles": {
            "zh-Hant": "內地未發表作品留下稿件，香港家屬先分開發表權和收益線索",
            "zh-Hans": "内地未发表作品留下稿件，香港家属先分开发表权和收益线索",
            "en": "An unpublished Mainland work remains: separate publication questions from inheritance clues",
        },
        "fallback": "/articles/hong-kong-other-estate/",
    },
    "MO-053": {
        "folder": "am",
        "slug": "rural-contract-income-after-death",
        "topic": {"zh-Hant": "澳門家屬與內地農村資產", "zh-Hans": "澳门家属与内地农村资产", "en": "Macau families and Mainland rural assets"},
        "titles": {
            "zh-Hant": "內地農村承包收益未結，澳門繼承人先確認的是合同還是房屋",
            "zh-Hans": "内地农村承包收益未结，澳门继承人先确认的是合同还是房屋",
            "en": "Unpaid Mainland rural contract income: should a Macau heir check the contract or the building first?",
        },
        "fallback": "/articles/macau/",
    },
    "MO-054": {
        "folder": "am",
        "slug": "mainland-trademark-licence-royalty-estate",
        "topic": {"zh-Hant": "澳門家屬與內地商標收益", "zh-Hans": "澳门家属与内地商标收益", "en": "Macau families and Mainland trademark income"},
        "titles": {
            "zh-Hant": "內地商標許可費仍在收，澳門家屬先核對許可合同而不是只看流水",
            "zh-Hans": "内地商标许可费仍在收，澳门家属先核对许可合同而不是只看流水",
            "en": "Mainland trademark royalties continue: check the licence agreement before the bank statements",
        },
        "fallback": "/articles/macau/",
    },
    "SG-054": {
        "folder": "singapore",
        "slug": "mainland-domain-and-platform-store-after-death",
        "topic": {"zh-Hant": "新加坡家屬與內地數碼資產", "zh-Hans": "新加坡家属与内地数字资产", "en": "Singapore families and Mainland digital assets"},
        "titles": {
            "zh-Hant": "內地域名和電商店舖都用同一個人實名，新加坡家屬先分開帳戶和資產",
            "zh-Hans": "内地域名和电商店铺都用同一个人实名，新加坡家属先分开账户和资产",
            "en": "A Mainland domain and online shop use one identity: separate accounts from estate assets",
        },
        "fallback": "/articles/singapore/",
    },
    "SG-055": {
        "folder": "singapore",
        "slug": "mainland-collective-benefit-after-death",
        "topic": {"zh-Hant": "新加坡家屬與內地集體收益", "zh-Hans": "新加坡家属与内地集体收益", "en": "Singapore families and Mainland collective benefits"},
        "titles": {
            "zh-Hant": "新加坡家屬聽說內地村集體有分紅，先查成員身份還是先查款項",
            "zh-Hans": "新加坡家属听说内地村集体有分红，先查成员身份还是先查款项",
            "en": "A Mainland village collective may have paid a dividend: check membership and the payment record",
        },
        "fallback": "/articles/singapore/",
    },
    "US-054": {
        "folder": "us",
        "slug": "mainland-loan-guarantee-estate-claim",
        "topic": {"zh-Hant": "美國家屬與內地借款保證", "zh-Hans": "美国家属与内地借款保证", "en": "U.S. families and Mainland loan guarantees"},
        "titles": {
            "zh-Hant": "美國家屬發現逝者替內地借款人作過保證，先分清債權、債務和責任線",
            "zh-Hans": "美国家属发现逝者替内地借款人作过保证，先分清债权、债务和责任线",
            "en": "A deceased person guaranteed a Mainland loan: separate the creditor, borrower and guarantee issues",
        },
        "fallback": "/articles/united-states/",
    },
    "US-055": {
        "folder": "us",
        "slug": "mainland-copyright-income-omitted-from-probate",
        "topic": {"zh-Hant": "美國家屬與內地著作權收益", "zh-Hans": "美国家属与内地著作权收益", "en": "U.S. families and Mainland copyright income"},
        "titles": {
            "zh-Hant": "美國 probate 文件沒有寫內地著作權收益，先判斷補資料還是另起爭議",
            "zh-Hans": "美国 probate 文件没有写内地著作权收益，先判断补资料还是另起争议",
            "en": "Mainland copyright income was omitted from U.S. probate papers: what should happen next?",
        },
        "fallback": "/articles/united-states/",
    },
    "OC-001": {
        "folder": "overseas-chinese",
        "slug": "mainland-court-electronic-service",
        "topic": {"zh-Hant": "海外繼承人與內地程序", "zh-Hans": "海外继承人与内地程序", "en": "Overseas heirs and Mainland procedure"},
        "titles": {
            "zh-Hant": "海外繼承人收到內地法院電子材料，先固定送達憑證和時區",
            "zh-Hans": "海外继承人收到内地法院电子材料，先固定送达凭证和时区",
            "en": "An overseas heir receives Mainland court material electronically: preserve service evidence and time zones",
        },
        "fallback": "/articles/",
    },
    "OC-002": {
        "folder": "overseas-chinese",
        "slug": "mainland-multiheir-remittance",
        "topic": {"zh-Hant": "海外繼承人與內地遺產款項", "zh-Hans": "海外继承人与内地遗产款项", "en": "Overseas heirs and Mainland estate funds"},
        "titles": {
            "zh-Hant": "海外繼承人要把內地遺產款分給多人，先核對收款人和分配依據",
            "zh-Hans": "海外继承人要把内地遗产款分给多人，先核对收款人和分配依据",
            "en": "Several overseas heirs will receive Mainland estate funds: check recipients and the allocation basis",
        },
        "fallback": "/articles/",
    },
}


LANG_HEADINGS = {
    "zh-Hant": ["先核對這一件事", "接下來要保留的資料", "何時先停下來確認"],
    "zh-Hans": ["先核对这一件事", "接下来要保留的资料", "什么时候先停下来确认"],
    "en": ["First question to settle", "Records to preserve next", "When to pause and verify"],
}


def markdown_blocks(text: str) -> dict[str, list[str]]:
    markers = {
        "zh-Hant": "## 繁體中文草稿",
        "zh-Hans": "## 简体中文草稿",
        "en": "## English draft",
    }
    blocks: dict[str, list[str]] = {}
    for lang, marker in markers.items():
        start = text.find(marker)
        if start < 0:
            raise ValueError(f"missing language section: {marker}")
        start += len(marker)
        ends = [text.find(other, start) for other in ["## 繁體中文草稿", "## 简体中文草稿", "## English draft", "## Internal evidence note"] if text.find(other, start) >= 0]
        end = min(ends) if ends else len(text)
        raw = text[start:end]
        blocks[lang] = [p.strip() for p in re.split(r"\n\s*\n", raw.strip()) if p.strip() and not p.startswith("状态：")]
    return blocks


def strip_md(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", value)
    value = re.sub(r"[*_`#]", "", value)
    return re.sub(r"\s+", " ", value).strip()


def target_exists(path: str) -> bool:
    clean = path.split("?", 1)[0].split("#", 1)[0].lstrip("/")
    candidate = ROOT / clean
    if clean.endswith("/"):
        candidate = candidate / "index.html"
    return candidate.is_file()


def inline_html(value: str) -> str:
    escaped = html.escape(value, quote=False)
    return re.sub(
        r"\[([^\]]+)\]\((/[^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1))}</a>' if target_exists(m.group(2)) else html.escape(m.group(1)),
        escaped,
    )


def related_links(raw: str, fallback: str, lang: str) -> list[tuple[str, str]]:
    links = []
    for label, path in re.findall(r"\[([^\]]+)\]\((/[^)]+)\)", raw):
        if target_exists(path) and path not in [p for _, p in links]:
            links.append((label, path))
    if not links:
        label = {"zh-Hant": "同一專題總覽", "zh-Hans": "同一专题总览", "en": "Topic overview"}[lang]
        links.append((label, fallback))
    return links[:2]


def page_url(folder: str, slug: str, suffix: str = "") -> str:
    return f"{BASE}/articles/{folder}/{slug}{suffix}.html"


def render_page(story: dict, lang: str, paragraphs: list[str], raw_block: str) -> tuple[str, str]:
    slug = story["slug"]
    suffix = "_cn" if lang == "zh-Hans" else "_en" if lang == "en" else ""
    url = page_url(story["folder"], slug, suffix)
    title = story["titles"][lang]
    description = strip_md(paragraphs[0])[:150]
    lead = inline_html(paragraphs[0])
    heading = {"zh-Hant": "文章 / ", "zh-Hans": "文章 / ", "en": "Article / "}[lang] + story["topic"][lang]
    updated = {"zh-Hant": "最後更新", "zh-Hans": "最后更新", "en": "Updated"}[lang]
    ad_label = {"zh-Hant": "劉毅律師團隊 · 站內服務", "zh-Hans": "刘毅律师团队 · 站内服务", "en": "Liu Yi Lawyer Team · Site service"}[lang]
    ad_title = {"zh-Hant": "先把案情和文件線索整理清楚", "zh-Hans": "先把案情和文件线索整理清楚", "en": "Organise the facts and document clues first"}[lang]
    ad_desc = {"zh-Hant": "可先整理人物、文件、資產和待核對問題。", "zh-Hans": "可以先整理人物、文件、资产和待核对问题。", "en": "Start by organising the people, documents, assets and questions to verify."}[lang]
    cta = {"zh-Hant": "使用 AI 法律助手整理案情 →", "zh-Hans": "使用 AI 法律助手整理案情 →", "en": "Use the AI legal assistant to organise the facts →"}[lang]
    related_title = {"zh-Hant": "相關文章", "zh-Hans": "相关文章", "en": "Related reading"}[lang]
    sections = []
    for index, paragraph in enumerate(paragraphs[1:]):
        section_title = LANG_HEADINGS[lang][min(index, len(LANG_HEADINGS[lang]) - 1)]
        sections.append(f'<section class="hk-section-card article-prose-section"><h2>{section_title}</h2><p>{inline_html(paragraph)}</p></section>')
    links = related_links(raw_block, story["fallback"], lang)
    links_html = "".join(f'<p><a href="{html.escape(path, quote=True)}">{html.escape(label)}</a></p>' for label, path in links)
    canonical_hant = page_url(story["folder"], slug)
    canonical_hans = page_url(story["folder"], slug, "_cn")
    canonical_en = page_url(story["folder"], slug, "_en")
    jsonld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "datePublished": DATE,
        "dateModified": DATE,
        "inLanguage": lang,
        "mainEntityOfPage": url,
        "author": {"@type": "Organization", "name": "劉毅律師團隊", "url": BASE + "/"},
        "publisher": {"@type": "Organization", "name": "劉毅律師團隊"},
        "articleSection": story["topic"][lang],
        "image": [BASE + "/articles/article-library-desk-v26.jpg"],
    }
    nav_topic = {"zh-Hant": "文章庫", "zh-Hans": "文章库", "en": "Articles"}[lang]
    language_links = f'<a href="{canonical_hant}" lang="zh-Hant">繁</a><a href="{canonical_hans}" lang="zh-Hans">简</a><a href="{canonical_en}" lang="en">EN</a>'
    html_page = f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} | 劉毅律師團隊</title><meta name="description" content="{html.escape(description, quote=True)}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<link rel="canonical" href="{url}"><link rel="alternate" hreflang="zh-Hant" href="{canonical_hant}"><link rel="alternate" hreflang="zh-Hans" href="{canonical_hans}"><link rel="alternate" hreflang="en" href="{canonical_en}"><link rel="alternate" hreflang="x-default" href="{canonical_hant}">
<meta property="og:type" content="article"><meta property="og:site_name" content="劉毅律師團隊"><meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(description, quote=True)}"><meta property="og:url" content="{url}"><meta property="article:published_time" content="{DATE}"><meta property="article:modified_time" content="{DATE}">
<link rel="stylesheet" href="/articles/style.css?v=20261010-liuyi-articles"><script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script></head>
<body class="article-detail generated-article article-regional-inheritance"><header class="site-header"><nav class="nav" aria-label="Article navigation"><a class="brand" href="/articles/"><strong>劉毅律師團隊</strong><span>跨境中國法律事務</span></a><a href="/articles/">{nav_topic}</a><div class="article-lang-switch" aria-label="Language switch">{language_links}</div></nav></header>
<main><section class="article-hero"><div class="article-hero-inner"><div class="article-hero-copy"><p class="eyebrow">{html.escape(heading)}</p><h1>{html.escape(title)}</h1><p class="article-lead">{lead}</p><p class="article-last-updated">{updated}: <time datetime="{DATE}">{DATE}</time></p></div></div></section><div class="article-shell"><article class="article-main">
<a class="article-native-ad" href="/ask/gpt/?topic={html.escape(story['folder'], quote=True)}&amp;source=article-inline-ad-{slug}" aria-label="AI legal assistant"><span class="article-native-ad__media" aria-hidden="true"><img src="/articles/assets/ai-legal-assistant-native-ad-v2.webp" alt="" width="1536" height="1024" loading="lazy" decoding="async"></span><span class="article-native-ad__copy"><span class="article-native-ad__label">{ad_label}</span><strong>{ad_title}</strong><span class="article-native-ad__description">{ad_desc}</span></span><span class="article-native-ad__action">開始整理 <span aria-hidden="true">→</span></span></a>
<section class="answer-card"><h2>{'先說重點' if lang == 'zh-Hant' else '先说重点' if lang == 'zh-Hans' else 'Key point first'}</h2><p>{lead}</p></section>{''.join(sections)}<section class="topic-article-directory compact-directory"><h2>{related_title}</h2>{links_html}<p><a href="/ask/gpt/?topic={html.escape(story['folder'], quote=True)}&amp;source=article-{slug}">{cta}</a></p></section></article></div></main><footer class="site-footer">{('內容只作一般資訊參考，具體事項需由律師結合材料判斷。' if lang == 'zh-Hant' else '内容只作一般信息参考，具体事项需由律师结合材料判断。' if lang == 'zh-Hans' else 'This article is general information only; a lawyer should review the actual documents and facts.')}</footer><script src="/articles/script.js" defer></script></body></html>'''
    return url, html_page


def add_daily_section(path: Path, entries: list[tuple[str, str]], lang: str) -> None:
    content = path.read_text(encoding="utf-8")
    if lang == "zh-Hant":
        heading, label = "2026年10月10日更新", "最新文章"
    elif lang == "zh-Hans":
        heading, label = "2026年10月10日更新", "最新文章"
    else:
        heading, label = "Latest updates · 10 October 2026", "New article"
    cards = "".join(f'<a href="{html.escape(url.replace(BASE, ""), quote=True)}"><span>{label}</span><strong>{html.escape(title)}</strong><p>{html.escape(title)}</p></a>' for url, title in entries)
    section = f'<!-- DAILY_20261010_START --><section class="topic-article-directory compact-directory daily-update-20261010"><h2>{heading}</h2><div class="topic-directory-grid">{cards}</div></section><!-- DAILY_20261010_END -->\n'
    existing = re.compile(r"<!-- DAILY_20261010_START -->.*?<!-- DAILY_20261010_END -->", re.S)
    if existing.search(content):
        path.write_text(existing.sub(section.rstrip("\n"), content, count=1), encoding="utf-8")
        return
    marker = "</main>"
    if marker not in content:
        raise ValueError(f"missing main close in {path}")
    path.write_text(content.replace(marker, section + marker, 1), encoding="utf-8")


def update_sitemap(urls: list[str]) -> None:
    path = ROOT / "sitemap.xml"
    content = path.read_text(encoding="utf-8")
    existing = set(re.findall(r"<loc>([^<]+)</loc>", content))
    additions = []
    for url in urls:
        if url in existing:
            continue
        priority = "0.60" if not re.search(r"_(?:cn|en)\.html$", url) else "0.55"
        additions.append(f"  <url>\n    <loc>{url}</loc>\n    <lastmod>{DATE}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>")
    if additions:
        content = content.replace("</urlset>", "\n" + "\n".join(additions) + "\n</urlset>")
        path.write_text(content, encoding="utf-8")


def main() -> None:
    outputs: list[tuple[str, str, str, str]] = []
    for story_id, story in STORIES.items():
        draft_files = list(DRAFT_DIR.glob(f"{story_id}-*.md"))
        if len(draft_files) != 1:
            raise ValueError(f"expected one draft for {story_id}, found {len(draft_files)}")
        blocks = markdown_blocks(draft_files[0].read_text(encoding="utf-8"))
        for lang in ("zh-Hant", "zh-Hans", "en"):
            url, page = render_page(story, lang, blocks[lang], "\n\n".join(blocks[lang]))
            relative = url.replace(BASE + "/", "")
            target = ROOT / relative
            if any(part in PROTECTED for part in target.parts):
                raise RuntimeError(f"protected path refused: {target}")
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(page, encoding="utf-8")
            outputs.append((url, story["titles"][lang], story_id, lang))

    update_sitemap([url for url, _, _, _ in outputs])
    by_category: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for url, title, story_id, lang in outputs:
        story = STORIES[story_id]
        by_category.setdefault((lang, "all"), []).append((url, title))
        category = "macau" if story["folder"] == "am" else "united-states" if story["folder"] == "us" else story["folder"]
        by_category.setdefault((lang, category), []).append((url, title))

    index_targets = {
        "zh-Hant": [ROOT / "articles" / "index.html", ROOT / "articles" / "hong-kong-other-estate" / "index.html", ROOT / "articles" / "macau" / "index.html", ROOT / "articles" / "singapore" / "index.html", ROOT / "articles" / "united-states" / "index.html"],
        "zh-Hans": [ROOT / "articles" / "index_cn.html", ROOT / "articles" / "hong-kong-other-estate" / "index_cn.html", ROOT / "articles" / "macau" / "index_cn.html", ROOT / "articles" / "singapore" / "index_cn.html", ROOT / "articles" / "united-states" / "index_cn.html"],
        "en": [ROOT / "articles" / "index_en.html", ROOT / "articles" / "hong-kong-other-estate" / "index_en.html", ROOT / "articles" / "macau" / "index_en.html", ROOT / "articles" / "singapore" / "index_en.html", ROOT / "articles" / "united-states" / "index_en.html"],
    }
    for lang, paths in index_targets.items():
        for path in paths:
            if not path.exists():
                continue
            key = "all" if path.parent.name == "articles" else path.parent.name
            add_daily_section(path, by_category.get((lang, key), []), lang)
    print(f"published {len(outputs)} language pages for {len(STORIES)} stories")


if __name__ == "__main__":
    main()
