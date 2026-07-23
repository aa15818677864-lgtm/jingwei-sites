from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

from opencc import OpenCC


ROOT = Path(__file__).resolve().parents[1]
DRAFT_ROOT = ROOT / "content-drafts" / "hk-mainland-property-inheritance-202607" / "03-drafts"
ARTICLE_ROOT = ROOT / "articles" / "hk-mainland-property-inheritance"
QUEUE_PATH = ROOT / "ARTICLE_OPERATIONS_QUEUE.json"
SITEMAP_PATH = ROOT / "sitemap.xml"
SITE = "https://www.jingwei-law.com"
SLUGS = [
    "first-call-family-facts",
    "asset-clue-list",
    "family-tree-before-inheritance",
    "hong-kong-death-certificate-details",
    "family-relationship-evidence",
    "inheritance-without-will",
    "will-first-review",
    "executor-role-boundary",
    "heirs-in-multiple-regions",
    "unreachable-heir",
    "heir-refuses-to-sign",
    "renounce-inheritance",
    "remote-authorisation-scope",
    "document-route-by-purpose",
    "name-mismatch-across-records",
    "old-address-and-id-records",
    "property-transfer-checklist",
    "mortgaged-property",
    "co-owned-property-share",
    "property-certificate-missing",
]

LOCALES = {
    "zh-Hant": {
        "suffix": "",
        "lang": "zh-Hant",
        "og": "zh_HK",
        "brand": "劉毅律師團隊",
        "subtitle": "跨境中國法律事務",
        "nav_articles": "文章",
        "nav_topic": "香港繼承",
        "nav_ask": "初步問答",
        "nav_home": "主站",
        "eyebrow": "文章 / 香港繼承",
        "key_title": "這篇先回答",
        "answer_title": "先說結論",
        "updated": "最後更新",
        "directory": "同一專題繼續閱讀",
        "toc": "文章目錄",
        "next": "下一步",
        "cta": "進入專題初步問答",
        "cta_text": "把家人關係、內地資產、已有文件和目前卡點先說清楚，再判斷應先查資料、安排文件，還是處理家人之間的分歧。",
        "disclaimer": "文章內容僅作初步信息參考，具體事項需由律師結合材料進一步判斷。",
        "figure_labels": ["情況", "次序", "清單"],
        "figure_captions": ["先把人物、資產和目前卡點放在同一張圖。", "按實際任務安排先後，不套用單一流程。", "整理諮詢前值得先找齊的資料。"],
        "prep": ["人物關係", "資產線索", "現有文件", "目前卡點"],
    },
    "zh-Hans": {
        "suffix": "_cn",
        "lang": "zh-Hans",
        "og": "zh_CN",
        "brand": "刘毅律师团队",
        "subtitle": "跨境中国法律事务",
        "nav_articles": "文章",
        "nav_topic": "香港继承",
        "nav_ask": "初步问答",
        "nav_home": "主站",
        "eyebrow": "文章 / 香港继承",
        "key_title": "这篇先回答",
        "answer_title": "先说结论",
        "updated": "最后更新",
        "directory": "同一专题继续阅读",
        "toc": "文章目录",
        "next": "下一步",
        "cta": "进入专题初步问答",
        "cta_text": "把家人关系、内地资产、已有文件和目前卡点先说清楚，再判断应先查资料、安排文件，还是处理家人之间的分歧。",
        "disclaimer": "文章内容仅作初步信息参考，具体事项需由律师结合材料进一步判断。",
        "figure_labels": ["情况", "次序", "清单"],
        "figure_captions": ["先把人物、资产和目前卡点放在同一张图。", "按实际任务安排先后，不套用单一流程。", "整理咨询前值得先找齐的资料。"],
        "prep": ["人物关系", "资产线索", "现有文件", "目前卡点"],
    },
    "en": {
        "suffix": "_en",
        "lang": "en",
        "og": "en_US",
        "brand": "Liu Yi Lawyer Team",
        "subtitle": "Cross-border Mainland China legal matters",
        "nav_articles": "Articles",
        "nav_topic": "Hong Kong inheritance",
        "nav_ask": "Initial Q&A",
        "nav_home": "Main site",
        "eyebrow": "Articles / Hong Kong inheritance",
        "key_title": "What this article answers",
        "answer_title": "The short answer",
        "updated": "Last updated",
        "directory": "Continue with this topic",
        "toc": "Contents",
        "next": "Next step",
        "cta": "Start the initial Q&A",
        "cta_text": "Set out the family relationships, known Mainland assets, available records and the immediate obstacle. That makes it easier to decide whether the next task is a search, document preparation or dispute work.",
        "disclaimer": "This article provides general information only. A lawyer must review the actual records and circumstances before advising on a particular matter.",
        "figure_labels": ["Situation", "Sequence", "Checklist"],
        "figure_captions": ["Put the people, assets and immediate obstacle in one view.", "Sequence the work around the actual task rather than a single template.", "Collect the records that will make an initial review more useful."],
        "prep": ["Family", "Assets", "Records", "Obstacle"],
    },
}


@dataclass
class Article:
    title: str
    intro: list[str]
    sections: list[tuple[str, list[tuple[str, object]]]]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def paragraph_blocks(lines: list[str]) -> list[tuple[str, object]]:
    blocks: list[tuple[str, object]] = []
    paragraph: list[str] = []
    bullets: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            blocks.append(("p", " ".join(paragraph).strip()))
            paragraph.clear()

    def flush_bullets() -> None:
        if bullets:
            blocks.append(("ul", bullets.copy()))
            bullets.clear()

    for raw in lines + [""]:
        line = raw.strip()
        if line.startswith("- "):
            flush_paragraph()
            bullets.append(line[2:].strip())
        elif not line:
            flush_paragraph()
            flush_bullets()
        else:
            flush_bullets()
            paragraph.append(line)
    return blocks


def parse_markdown(text: str) -> Article:
    title = ""
    intro_lines: list[str] = []
    sections: list[tuple[str, list[tuple[str, object]]]] = []
    heading: str | None = None
    section_lines: list[str] = []

    def flush_section() -> None:
        nonlocal section_lines
        if heading is not None:
            sections.append((heading, paragraph_blocks(section_lines)))
        section_lines = []

    for raw in text.splitlines():
        if raw.startswith("# "):
            title = raw[2:].strip()
        elif raw.startswith("## "):
            flush_section()
            heading = raw[3:].strip()
        elif heading is None:
            intro_lines.append(raw)
        else:
            section_lines.append(raw)
    flush_section()
    intro = [str(value) for kind, value in paragraph_blocks(intro_lines) if kind == "p"]
    if not title or not intro or not sections:
        raise ValueError("Draft must have one H1, an opening answer and at least one H2")
    return Article(title=title, intro=intro, sections=sections)


def first_sentence(text: str, limit: int) -> str:
    sentence = re.split(r"(?<=[。！？.!?])\s*", text.strip())[0]
    if len(sentence) <= limit:
        return sentence
    return sentence[: limit - 1].rstrip("，,；;: ") + "…"


def slug_id(value: str, index: int) -> str:
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return ascii_slug or f"section-{index}"


def render_blocks(blocks: list[tuple[str, object]]) -> str:
    rows: list[str] = []
    for kind, value in blocks:
        if kind == "p":
            rows.append(f"          <p>{html.escape(str(value))}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{html.escape(str(item))}</li>" for item in value)
            rows.append(f"          <ul>{items}</ul>")
    return "\n".join(rows)


def page_path(slug: str, locale: str) -> str:
    suffix = LOCALES[locale]["suffix"]
    return f"/articles/hk-mainland-property-inheritance/{slug}{suffix}.html"


def alt_links(slug: str) -> str:
    return "\n".join(
        [
            f'  <link rel="alternate" hreflang="zh-Hant" href="{SITE}{page_path(slug, "zh-Hant")}">',
            f'  <link rel="alternate" hreflang="zh-Hans" href="{SITE}{page_path(slug, "zh-Hans")}">',
            f'  <link rel="alternate" hreflang="en" href="{SITE}{page_path(slug, "en")}">',
            f'  <link rel="alternate" hreflang="x-default" href="{SITE}{page_path(slug, "zh-Hant")}">',
        ]
    )


def language_switch(slug: str, locale: str) -> str:
    links = []
    for code, label in (("zh-Hant", "繁"), ("zh-Hans", "简"), ("en", "EN")):
        if code == locale:
            links.append(f'<span aria-current="true">{label}</span>')
        else:
            links.append(f'<a href="{page_path(slug, code)}" lang="{code}">{label}</a>')
    return '<div class="article-lang-switch" aria-label="Language switch">' + "".join(links) + "</div>"


def json_ld(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")


def render_page(slug: str, locale: str, article: Article, published: str, modified: str) -> str:
    copy = LOCALES[locale]
    canonical = page_path(slug, locale)
    description = first_sentence(article.intro[0], 158 if locale == "en" else 118)
    title = article.title
    full_title = f"{title} | {copy['brand']}"
    image_suffix = copy["suffix"]
    image_paths = [
        f"/articles/hk-mainland-property-inheritance/images/{slug}/0{index}-{name}{image_suffix}.svg"
        for index, name in ((1, "context"), (2, "path"), (3, "checklist"))
    ]
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "datePublished": published,
        "dateModified": modified,
        "image": [f"{SITE}{path}" for path in image_paths],
        "inLanguage": copy["lang"],
        "articleSection": "Hong Kong and Mainland inheritance",
        "author": {"@type": "Organization", "name": copy["brand"], "url": f"{SITE}/"},
        "publisher": {"@type": "Organization", "@id": f"{SITE}/#organization", "name": copy["brand"], "url": f"{SITE}/"},
        "mainEntityOfPage": f"{SITE}{canonical}",
        "isPartOf": {"@type": "CollectionPage", "url": f"{SITE}/articles/hk-mainland-property-inheritance/"},
    }
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": copy["nav_articles"], "item": f"{SITE}/articles/"},
            {"@type": "ListItem", "position": 2, "name": copy["nav_topic"], "item": f"{SITE}/articles/hk-mainland-property-inheritance/"},
            {"@type": "ListItem", "position": 3, "name": title, "item": f"{SITE}{canonical}"},
        ],
    }
    key_items = "".join(f"<li>{html.escape(heading)}</li>" for heading, _ in article.sections[:3])
    intro_html = "\n".join(f"          <p>{html.escape(paragraph)}</p>" for paragraph in article.intro)
    section_rows: list[str] = []
    toc_rows: list[str] = [f'<a href="#answer">{html.escape(str(copy["answer_title"]))}</a>']
    for index, (heading, blocks) in enumerate(article.sections, start=1):
        section_id = slug_id(heading, index)
        section_rows.append(
            f'        <section id="{section_id}" class="hk-section-card article-prose-section">\n'
            f"          <h2>{html.escape(heading)}</h2>\n{render_blocks(blocks)}\n"
            "        </section>"
        )
        toc_rows.append(f'<a href="#{section_id}">{html.escape(heading)}</a>')
    related = related_links(slug, locale)
    figures = []
    for path, caption, label in zip(image_paths, copy["figure_captions"], copy["figure_labels"]):
        figures.append(
            f'<figure><img src="{path}" alt="{html.escape(title)} · {html.escape(str(label))}" width="1200" height="720" '
            f'loading="lazy" decoding="async"><figcaption>{html.escape(str(caption))}</figcaption></figure>'
        )
    ask_url = f"/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-{slug}"
    date_separator = ": " if locale == "en" else "："
    return f"""<!DOCTYPE html>
<html lang="{copy['lang']}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(full_title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta property="og:locale" content="{copy['og']}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="{html.escape(str(copy['brand']))}">
  <meta property="og:title" content="{html.escape(full_title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:url" content="{SITE}{canonical}">
  <meta property="og:image" content="{SITE}/articles/article-library-desk-v26.jpg">
  <meta property="og:image:alt" content="{html.escape(title)}">
  <meta property="article:published_time" content="{published}">
  <meta property="article:modified_time" content="{modified}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{html.escape(full_title)}">
  <meta name="twitter:description" content="{html.escape(description)}">
  <meta name="twitter:image" content="{SITE}/articles/article-library-desk-v26.jpg">
  <link rel="canonical" href="{SITE}{canonical}">
{alt_links(slug)}
  <link rel="stylesheet" href="../style.css?v=20260723-geo-v1">
  <script type="application/ld+json">{json_ld(article_schema)}</script>
  <script type="application/ld+json">{json_ld(breadcrumb_schema)}</script>
</head>
<body class="article-detail article-hk-inheritance generated-article">
  <header class="site-header">
    <nav class="nav" aria-label="Article navigation">
      <a class="brand" href="/articles/"><strong>{copy['brand']}</strong><span>{copy['subtitle']}</span></a>
      <div class="nav-links">
        <a href="/articles/">{copy['nav_articles']}</a>
        <a href="/articles/hk-mainland-property-inheritance/">{copy['nav_topic']}</a>
        <a href="{ask_url}">{copy['nav_ask']}</a>
        <a href="/">{copy['nav_home']}</a>
      </div>
      {language_switch(slug, locale)}
    </nav>
  </header>

  <main>
    <section class="article-hero" aria-label="Article introduction">
      <div class="article-hero-inner">
        <div class="article-hero-copy">
          <p class="eyebrow">{copy['eyebrow']}</p>
          <h1>{html.escape(title)}</h1>
          <p class="article-lead">{html.escape(description)}</p>
          <p class="article-last-updated"><time datetime="{modified}">{copy['updated']}{date_separator}{modified}</time></p>
        </div>
        <aside class="article-key-card" aria-label="Key points">
          <h2>{copy['key_title']}</h2>
          <ul class="article-key-list">{key_items}</ul>
        </aside>
      </div>
    </section>

    <div class="article-shell">
      <article class="article-main">
        <section class="article-image-grid" aria-label="Article visuals">{''.join(figures)}</section>
        <section id="answer" class="answer-card">
          <h2>{copy['answer_title']}</h2>
{intro_html}
        </section>

{chr(10).join(section_rows)}

        <section class="topic-article-directory compact-directory" aria-label="Related articles">
          <h2>{copy['directory']}</h2>
          <div class="topic-directory-grid">{related}</div>
        </section>
      </article>

      <aside class="toc" aria-label="Article contents">
        <h2>{copy['toc']}</h2>
        {''.join(toc_rows)}
        <a class="toc-cta" href="{ask_url}">{copy['cta']} →</a>
      </aside>
    </div>

    <section class="cta-panel">
      <h2>{copy['next']}</h2>
      <p>{copy['cta_text']}</p>
      <a class="button" href="{ask_url}">{copy['cta']} →</a>
    </section>
  </main>

  <footer class="site-footer"><div class="footer-inner">{copy['disclaimer']}</div></footer>
  <script src="/articles/script.js" defer></script>
</body>
</html>
"""


def related_links(slug: str, locale: str) -> str:
    position = SLUGS.index(slug)
    nearby = [SLUGS[(position - 1) % len(SLUGS)], SLUGS[(position + 1) % len(SLUGS)]]
    paths = [
        ("/articles/hk-mainland-property-inheritance/", {"zh-Hant": "香港繼承總覽", "zh-Hans": "香港继承总览", "en": "Hong Kong inheritance overview"}[locale]),
        (page_path(nearby[0], locale), title_for(nearby[0], locale)),
        (page_path(nearby[1], locale), title_for(nearby[1], locale)),
        ({"zh-Hant": "/articles/hk-mainland-property-inheritance/documents.html", "zh-Hans": "/articles/hk-mainland-property-inheritance/documents_cn.html", "en": "/articles/hk-mainland-property-inheritance/documents_en.html"}[locale], {"zh-Hant": "香港文件怎樣按用途準備", "zh-Hans": "香港文件怎样按用途准备", "en": "Preparing Hong Kong records for a Mainland matter"}[locale]),
    ]
    return "".join(f'<a href="{path}">{html.escape(label)}</a>' for path, label in paths)


_ARTICLE_CACHE: dict[tuple[str, str], Article] = {}


def draft_path(slug: str, locale: str) -> Path:
    filename = {"zh-Hant": "03-draft_zh-Hant.md", "zh-Hans": "04-draft_zh-Hans.md", "en": "05-draft_en.md"}[locale]
    return DRAFT_ROOT / slug / filename


def article_for(slug: str, locale: str) -> Article:
    key = (slug, locale)
    if key not in _ARTICLE_CACHE:
        _ARTICLE_CACHE[key] = parse_markdown(read(draft_path(slug, locale)))
    return _ARTICLE_CACHE[key]


def title_for(slug: str, locale: str) -> str:
    return article_for(slug, locale).title


def wrap_text(value: str, width: int, max_lines: int = 2) -> list[str]:
    value = value.strip()
    if not value:
        return [""]
    if " " in value:
        words = value.split()
        lines: list[str] = []
        line = ""
        for word in words:
            candidate = f"{line} {word}".strip()
            if line and len(candidate) > width:
                lines.append(line)
                line = word
            else:
                line = candidate
        if line:
            lines.append(line)
    else:
        lines = [value[index : index + width] for index in range(0, len(value), width)]
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(1, width - 1)].rstrip() + "…"
    return lines


def svg_text(lines: list[str], x: int, y: int, css_class: str, line_height: int, anchor: str = "start") -> str:
    return "".join(
        f'<text x="{x}" y="{y + index * line_height}" text-anchor="{anchor}" class="{css_class}">{xml_escape(line)}</text>'
        for index, line in enumerate(lines)
    )


def visual_svg(article: Article, locale: str, variant: int) -> str:
    copy = LOCALES[locale]
    title_lines = wrap_text(article.title, 22 if locale != "en" else 42, 2)
    section_labels = [heading for heading, _ in article.sections[:4]]
    while len(section_labels) < 4:
        section_labels.append(str(copy["prep"][len(section_labels)]))
    short_sections = [wrap_text(value, 9 if locale != "en" else 18, 2) for value in section_labels]
    common = """<style>
      .bg{fill:#f3f6f8}.panel{fill:#fff;stroke:#d7dfe8;stroke-width:2}.ink{fill:#142033}.muted{fill:#52647a}.red{fill:#a30d23}.gold{fill:#d39b31}.teal{fill:#16736b}.blue{fill:#315f86}
      .kicker{font:700 22px -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;letter-spacing:0}.title{font:760 39px -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;letter-spacing:0}.label{font:700 24px -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;letter-spacing:0}.small{font:600 20px -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;letter-spacing:0}.num{font:760 22px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:0}
    </style>"""
    header = (
        '<rect class="bg" width="1200" height="720"/><rect class="panel" x="36" y="36" width="1128" height="648" rx="8"/>'
        f'<rect class="red" x="72" y="72" width="112" height="7"/>{svg_text([str(copy["figure_labels"][variant - 1])], 72, 116, "kicker red", 28)}'
        f'{svg_text(title_lines, 72, 168, "title ink", 48)}'
    )
    if variant == 1:
        colors = ("red", "teal", "blue")
        cards = []
        for index in range(3):
            x = 72 + index * 354
            cards.append(
                f'<rect class="panel" x="{x}" y="306" width="318" height="290" rx="8"/>'
                f'<circle class="{colors[index]}" cx="{x + 44}" cy="354" r="16"/>'
                f'{svg_text(short_sections[index], x + 30, 416, "label ink", 34)}'
                f'<rect class="{colors[index]}" opacity=".12" x="{x + 30}" y="502" width="258" height="54" rx="6"/>'
            )
        body = "".join(cards)
    elif variant == 2:
        colors = ("red", "gold", "teal", "blue")
        cards = ['<line x1="140" y1="420" x2="1060" y2="420" stroke="#ced8e2" stroke-width="6"/>']
        for index in range(4):
            x = 140 + index * 306
            cards.append(
                f'<circle class="{colors[index]}" cx="{x}" cy="420" r="34"/><text class="num" x="{x}" y="428" text-anchor="middle" fill="#fff">{index + 1}</text>'
                f'{svg_text(short_sections[index], x, 500, "small ink", 29, "middle")}'
            )
        body = "".join(cards)
    else:
        colors = ("red", "gold", "teal", "blue")
        cards = []
        for index, label in enumerate(copy["prep"]):
            row = index % 2
            col = index // 2
            x = 72 + col * 534
            y = 320 + row * 132
            cards.append(
                f'<rect class="panel" x="{x}" y="{y}" width="498" height="102" rx="8"/>'
                f'<rect class="{colors[index]}" x="{x + 28}" y="{y + 32}" width="38" height="38" rx="6"/>'
                f'<path d="M{x + 38} {y + 51} l8 8 14 -18" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
                f'{svg_text([str(label)], x + 90, y + 63, "label ink", 30)}'
            )
        body = "".join(cards)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720" role="img" aria-label="{xml_escape(article.title)}">{common}{header}{body}</svg>\n'


def ensure_simplified_drafts() -> None:
    converter = OpenCC("t2s")
    for slug in SLUGS:
        source = draft_path(slug, "zh-Hant")
        target = draft_path(slug, "zh-Hans")
        write(target, converter.convert(read(source)))


def existing_publish_date(path: Path, fallback: str) -> str:
    if not path.exists():
        return fallback
    match = re.search(r'<meta property="article:published_time" content="([0-9-]+)">', read(path))
    return match.group(1) if match else fallback


def build_pages(run_date: str) -> None:
    ensure_simplified_drafts()
    for slug in SLUGS:
        for locale in LOCALES:
            if not draft_path(slug, locale).exists():
                raise FileNotFoundError(f"Missing {locale} draft for {slug}")
            article = article_for(slug, locale)
            suffix = LOCALES[locale]["suffix"]
            output = ARTICLE_ROOT / f"{slug}{suffix}.html"
            published = existing_publish_date(output, run_date)
            write(output, render_page(slug, locale, article, published, run_date))
            image_dir = ARTICLE_ROOT / "images" / slug
            image_dir.mkdir(parents=True, exist_ok=True)
            for variant, name in ((1, "context"), (2, "path"), (3, "checklist")):
                write(image_dir / f"0{variant}-{name}{suffix}.svg", visual_svg(article, locale, variant))


def generated_cards(locale: str) -> str:
    tag = {"zh-Hant": "新文章", "zh-Hans": "新文章", "en": "New"}[locale]
    rows = []
    for slug in SLUGS:
        article = article_for(slug, locale)
        summary = first_sentence(article.intro[0], 70 if locale != "en" else 112)
        rows.append(
            f'        <a href="{page_path(slug, locale)}"><span>{tag}</span><strong>{html.escape(article.title)}</strong>'
            f'<small>{html.escape(summary)}</small></a>'
        )
    return "\n".join(rows)


def replace_marker(text: str, start: str, end: str, content: str, insertion_pattern: str) -> str:
    block = f"{start}\n{content}\n{end}"
    if start in text and end in text:
        return re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block, text, flags=re.S)
    match = re.search(insertion_pattern, text, flags=re.S)
    if not match:
        raise ValueError(f"Could not find insertion point for {start}")
    return text[: match.start(1)] + block + "\n" + text[match.start(1) :]


def patch_article_indexes() -> None:
    settings = {
        "zh-Hant": (
            ROOT / "articles" / "index.html",
            r'(<a href="#hong-kong"><strong>香港繼承</strong><span>)\d+ 篇已發佈',
            r'\g<1>28 篇已發佈',
        ),
        "zh-Hans": (
            ROOT / "articles" / "index_cn.html",
            r'(<a href="#hong-kong"><strong>香港继承</strong><span>)\d+ 篇已发布',
            r'\g<1>28 篇已发布',
        ),
        "en": (
            ROOT / "articles" / "index_en.html",
            r'(<a href="#hong-kong"><strong>Hong Kong inheritance</strong><span>)\d+ articles',
            r'\g<1>28 articles',
        ),
    }
    for locale, (path, count_pattern, count_replacement) in settings.items():
        text, count = re.subn(count_pattern, count_replacement, read(path), count=1)
        if count != 1:
            raise ValueError(f"Could not update Hong Kong article count in {path}")
        cards = generated_cards(locale)
        text = replace_marker(
            text,
            "        <!-- HK_LAUNCH_20_START -->",
            "        <!-- HK_LAUNCH_20_END -->",
            cards,
            r'(?P<one>\s*</div>\s*</section>\s*<section id="macau")',
        )
        write(path, text)


def topic_directory(locale: str) -> str:
    copy = LOCALES[locale]
    intro = {
        "zh-Hant": "按人物、文件、房產和家人協作問題繼續閱讀。每篇只處理一個具體卡點。",
        "zh-Hans": "按人物、文件、房产和家人协作问题继续阅读。每篇只处理一个具体卡点。",
        "en": "Continue by family, records, property or coordination issue. Each article addresses one practical obstacle.",
    }[locale]
    links = "".join(
        f'<a href="{page_path(slug, locale)}"><strong>{html.escape(title_for(slug, locale))}</strong></a>' for slug in SLUGS
    )
    return (
        f'        <section id="article-directory" class="topic-article-directory">\n'
        f"          <h2>{copy['directory']}</h2><p>{intro}</p>\n"
        f'          <div class="topic-directory-grid">{links}</div>\n'
        "        </section>"
    )


def patch_topic_indexes() -> None:
    settings = {
        "zh-Hant": ARTICLE_ROOT / "index.html",
        "zh-Hans": ARTICLE_ROOT / "index_cn.html",
        "en": ARTICLE_ROOT / "index_en.html",
    }
    for locale, path in settings.items():
        text = read(path)
        text = replace_marker(
            text,
            "        <!-- TOPIC_DIRECTORY_START -->",
            "        <!-- TOPIC_DIRECTORY_END -->",
            topic_directory(locale),
            r"(?P<one>\s*</article>)",
        )
        write(path, text)


def patch_sitemap(run_date: str) -> None:
    rows = []
    for slug in SLUGS:
        for locale in LOCALES:
            rows.append(
                "  <url>\n"
                f"    <loc>{SITE}{page_path(slug, locale)}</loc>\n"
                f"    <lastmod>{run_date}</lastmod>\n"
                "    <changefreq>monthly</changefreq>\n"
                "    <priority>0.55</priority>\n"
                "  </url>"
            )
    start = "  <!-- HK_LAUNCH_20_START -->"
    end = "  <!-- HK_LAUNCH_20_END -->"
    text = read(SITEMAP_PATH)
    block = start + "\n" + "\n".join(rows) + "\n" + end
    if start in text and end in text:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block, text, flags=re.S)
    else:
        text = text.replace("</urlset>", block + "\n</urlset>")
    text = re.sub(
        r"(<loc>https://www\.jingwei-law\.com/articles(?:/hk-mainland-property-inheritance)?/</loc>\s*<lastmod>)[^<]+",
        rf"\g<1>{run_date}",
        text,
    )
    write(SITEMAP_PATH, text)


def patch_queue(run_date: str) -> None:
    text = read(QUEUE_PATH)
    text = re.sub(r'("updatedAt"\s*:\s*")[^"]+("\s*,)', rf"\g<1>{run_date}\2", text, count=1)
    for slug in SLUGS:
        pattern = rf'({{"id":"HK-\d+","slug":"{re.escape(slug)}".*?"status":")[^"]+("}})'
        text, count = re.subn(pattern, r'\1published\2', text)
        if count != 1:
            raise ValueError(f"Queue item not found for {slug}")
    write(QUEUE_PATH, text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish the first 20 reviewed Hong Kong inheritance draft packages")
    parser.add_argument("--date", default=date.today().isoformat(), help="truthful publication/review date in YYYY-MM-DD")
    args = parser.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        raise SystemExit("--date must use YYYY-MM-DD")
    build_pages(args.date)
    patch_article_indexes()
    patch_topic_indexes()
    patch_sitemap(args.date)
    patch_queue(args.date)
    print(f"built {len(SLUGS)} stories / {len(SLUGS) * len(LOCALES)} language pages")


if __name__ == "__main__":
    main()
