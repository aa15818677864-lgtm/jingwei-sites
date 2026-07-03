from __future__ import annotations

import json
import re
from html import escape
from pathlib import Path

from opencc import OpenCC


ROOT = Path(__file__).resolve().parents[1]
TODAY = "2026-07-03"
BASE = "https://www.jingwei-law.com"
IMAGE = f"{BASE}/articles/articles-index-v24-bg.webp"
cc = OpenCC("s2hk")
cc_simplified = OpenCC("hk2s")


def esc(value: str) -> str:
    return escape(value, quote=True)


def url(path: str) -> str:
    return BASE + path


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8", newline="\n")


def remove_i18n_bits(html: str) -> str:
    html = "\n".join(
        line for line in html.splitlines() if '<link rel="alternate" hreflang="' not in line
    )
    html = re.sub(
        r'\n\s*<div class="article-lang-switch[^"]*" aria-label="[^"]+">.*?</div>\s*',
        "\n",
        html,
        flags=re.S,
    )
    return html + "\n"


def cn_from_zh_path(zh_path: str) -> str:
    if zh_path == "/articles/":
        return "/articles/index_cn.html"
    if zh_path.endswith("/"):
        return zh_path + "index_cn.html"
    return zh_path.removesuffix(".html") + "_cn.html"


def rel_to_cn(rel: str) -> str:
    path = Path(rel)
    if path.name == "index.html":
        return str(path.with_name("index_cn.html")).replace("\\", "/")
    return str(path.with_name(path.stem + "_cn.html")).replace("\\", "/")


def alternate_links(zh_path: str, cn_path: str, en_path: str) -> str:
    return (
        f'  <link rel="alternate" hreflang="zh-Hant" href="{url(zh_path)}">\n'
        f'  <link rel="alternate" hreflang="zh-Hans" href="{url(cn_path)}">\n'
        f'  <link rel="alternate" hreflang="en" href="{url(en_path)}">\n'
        f'  <link rel="alternate" hreflang="x-default" href="{url(zh_path)}">'
    )


def _legacy_switch_html(zh_path: str, en_path: str, active: str, compact: bool = False) -> str:
    label = "Language switch" if active == "en" else "語言切換"
    zh = '<span aria-current="true">繁</span>' if active == "zh" else f'<a href="{zh_path}" lang="zh-Hant">繁</a>'
    en = '<span aria-current="true">EN</span>' if active == "en" else f'<a href="{en_path}" lang="en">EN</a>'
    extra = " v25-lang-switch" if compact else ""
    return f'<div class="article-lang-switch{extra}" aria-label="{label}">{zh}{en}</div>'


def switch_html(zh_path: str, cn_path: str, en_path: str, active: str, compact: bool = False) -> str:
    label = "Language switch"
    zh = '<span aria-current="true">&#32321;</span>' if active == "zh" else f'<a href="{zh_path}" lang="zh-Hant">&#32321;</a>'
    cn = '<span aria-current="true">&#31616;</span>' if active == "cn" else f'<a href="{cn_path}" lang="zh-Hans">&#31616;</a>'
    en = '<span aria-current="true">EN</span>' if active == "en" else f'<a href="{en_path}" lang="en">EN</a>'
    extra = " v25-lang-switch" if compact else ""
    return f'<div class="article-lang-switch{extra}" aria-label="{label}">{zh}{cn}{en}</div>'


def chinese_page(rel: str, zh_path: str, cn_path: str, en_path: str, is_index: bool = False) -> None:
    html = cc.convert(read(rel))
    html = remove_i18n_bits(html)
    html = html.replace('<html lang="zh-CN">', '<html lang="zh-Hant">')
    html = html.replace('content="zh_CN"', 'content="zh_HK"')
    html = html.replace('"inLanguage": "zh-CN"', '"inLanguage": "zh-Hant"')
    html = re.sub(r'(<meta property="article:modified_time" content=")[^"]+(">)', rf"\g<1>{TODAY}\2", html)
    html = re.sub(r'("dateModified": ")[^"]+(")', rf"\g<1>{TODAY}\2", html)
    html = re.sub(r'(<link rel="canonical" href="[^"]+">)', rf"\1\n{alternate_links(zh_path, cn_path, en_path)}", html, count=1)
    if is_index:
        html = re.sub(
            r'(\s*</nav>\s*)(<a class="v25-contact")',
            rf'\1      {switch_html(zh_path, cn_path, en_path, "zh", compact=True)}\n\n      \2',
            html,
            count=1,
        )
    else:
        html = re.sub(
            r'(\s*</div>\s*)(</nav>)',
            rf'\1      {switch_html(zh_path, cn_path, en_path, "zh")}\n    \2',
            html,
            count=1,
        )
    write(rel, html)


def simplify_article_links(html: str) -> str:
    html = re.sub(
        r'((?:href|item|content)="https://www\.jingwei-law\.com/articles/hk-mainland-property-inheritance/)([a-z0-9-]+)\.html"',
        r'\1\2_cn.html"',
        html,
    )
    html = re.sub(
        r'((?:href|item|content)="https://www\.jingwei-law\.com/articles/hk-mainland-property-inheritance/)"',
        r'\1index_cn.html"',
        html,
    )
    html = re.sub(
        r'((?:href|item|content)="https://www\.jingwei-law\.com/articles/)"',
        r'\1index_cn.html"',
        html,
    )
    html = re.sub(
        r'(href="/articles/hk-mainland-property-inheritance/)([a-z0-9-]+)\.html"',
        r'\1\2_cn.html"',
        html,
    )
    html = html.replace('href="/articles/hk-mainland-property-inheritance/"', 'href="/articles/hk-mainland-property-inheritance/index_cn.html"')
    html = html.replace('href="/articles/"', 'href="/articles/index_cn.html"')
    return html


def simplified_page(src_rel: str, cn_rel: str, zh_path: str, cn_path: str, en_path: str, is_index: bool = False) -> None:
    html = cc_simplified.convert(read(src_rel))
    html = remove_i18n_bits(html)
    html = html.replace('<html lang="zh-Hant">', '<html lang="zh-Hans">')
    html = html.replace('content="zh_HK"', 'content="zh_CN"')
    html = html.replace('"inLanguage": "zh-Hant"', '"inLanguage": "zh-Hans"')
    html = re.sub(r'(<meta property="article:modified_time" content=")[^"]+(">)', rf"\g<1>{TODAY}\2", html)
    html = re.sub(r'("dateModified": ")[^"]+(")', rf"\g<1>{TODAY}\2", html)
    html = re.sub(r'(<meta property="og:url" content=")[^"]+(">)', rf"\g<1>{url(cn_path)}\2", html, count=1)
    html = re.sub(r'(<link rel="canonical" href=")[^"]+(">)', rf"\g<1>{url(cn_path)}\2\n{alternate_links(zh_path, cn_path, en_path)}", html, count=1)
    html = re.sub(r'("mainEntityOfPage": ")[^"]+(")', rf"\g<1>{url(cn_path)}\2", html)
    html = simplify_article_links(html)
    if is_index:
        html = re.sub(
            r'(\s*</nav>\s*)(<a class="v25-contact")',
            rf'\1      {switch_html(zh_path, cn_path, en_path, "cn", compact=True)}\n\n      \2',
            html,
            count=1,
        )
    else:
        html = re.sub(
            r'(\s*</div>\s*)(</nav>)',
            rf'\1      {switch_html(zh_path, cn_path, en_path, "cn")}\n    \2',
            html,
            count=1,
        )
    write(cn_rel, html)


def head_common(
    *,
    lang: str,
    title: str,
    description: str,
    robots: str,
    canonical_path: str,
    zh_path: str,
    cn_path: str,
    en_path: str,
    og_type: str,
    body_extra: str = "",
) -> str:
    locale = "en_US" if lang == "en" else "zh_HK"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="{robots}">
  <meta property="og:locale" content="{locale}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="Liu Yi Lawyer Team">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{url(canonical_path)}">
  <meta property="og:image" content="{IMAGE}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{IMAGE}">
  <link rel="canonical" href="{url(canonical_path)}">
{alternate_links(zh_path, cn_path, en_path)}
  <link rel="stylesheet" href="{body_extra or '../style.css'}">'''


def json_ld(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def header_detail(zh_path: str, cn_path: str, en_path: str, active: str = "en") -> str:
    return f'''  <header class="site-header">
    <nav class="nav" aria-label="Article navigation">
      <a class="brand" href="/articles/index_en.html">
        <strong>Liu Yi Lawyer Team</strong>
        <span>Cross-border Mainland China legal matters</span>
      </a>
      <div class="nav-links">
        <a href="/articles/index_en.html" aria-current="page">Articles</a>
        <a href="/articles/hk-mainland-property-inheritance/index_en.html">Topic</a>
        <a href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-en-nav">Organise Facts</a>
        <a href="/">Main Site</a>
      </div>
      {switch_html(zh_path, cn_path, en_path, active)}
    </nav>
  </header>'''


def render_index_en() -> str:
    title = "Hong Kong Families Inheriting Mainland Property | Liu Yi Lawyer Team Articles"
    desc = "A practical article hub for Hong Kong families who need to understand the first step: the property, the heirs, the Hong Kong documents, family disagreement, timing and costs."
    zh_path = "/articles/"
    cn_path = cn_from_zh_path(zh_path)
    en_path = "/articles/index_en.html"
    item_urls = [
        ("/articles/hk-mainland-property-inheritance/index_en.html", "A Hong Kong family needs to inherit Mainland property: where should they start?"),
        ("/articles/hk-mainland-property-inheritance/documents_en.html", "Can Hong Kong death certificates or family relationship documents be used?"),
        ("/articles/hk-mainland-property-inheritance/dispute_en.html", "What if heirs disagree or refuse to cooperate?"),
        ("/articles/hk-mainland-property-inheritance/tax-cost_en.html", "How to think about tax, timing and legal costs"),
        ("/articles/am/macau-client-mainland-lawyer.html", "Macau clients instructing Mainland lawyers for Mainland legal matters"),
        ("/articles/overseas-chinese/remote-entrust-china-lawyer.html", "Overseas Chinese clients remotely instructing lawyers in Mainland China"),
        ("/articles/us/remote-china-lawyer.html", "U.S.-based clients handling Mainland China legal matters remotely"),
    ]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CollectionPage",
                "@id": url(en_path) + "#collection",
                "url": url(en_path),
                "name": "Liu Yi Lawyer Team article library",
                "description": desc,
                "inLanguage": "en",
                "isPartOf": {"@type": "WebSite", "@id": url("/") + "#website", "name": "Liu Yi Lawyer Team", "url": url("/")},
                "publisher": {"@type": "Organization", "name": "Liu Yi Lawyer Team", "url": url("/")},
                "mainEntity": {"@id": url(en_path) + "#article-list"},
            },
            {
                "@type": "BreadcrumbList",
                "@id": url(en_path) + "#breadcrumb",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": url("/")},
                    {"@type": "ListItem", "position": 2, "name": "Articles", "item": url(en_path)},
                ],
            },
            {
                "@type": "ItemList",
                "@id": url(en_path) + "#article-list",
                "name": "Cross-border Mainland China legal articles",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "url": url(p), "name": n}
                    for i, (p, n) in enumerate(item_urls)
                ],
            },
        ],
    }
    return f'''{head_common(lang="en", title=title, description=desc, robots="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1", canonical_path=en_path, zh_path=zh_path, cn_path=cn_path, en_path=en_path, og_type="website", body_extra="style.css?v=20260703-i18n")}
  <script type="application/ld+json">{json_ld(graph)}</script>
</head>
<body class="articles-index-v25 articles-index-en">
  <main class="v25-shell">
    <header class="v25-header" aria-label="Article library navigation">
      <a class="v25-brand" href="/articles/index_en.html">
        <span class="v25-seal">L</span>
        <span>
          <strong>Liu Yi Lawyer Team</strong>
          <small>Cross-border Mainland China legal articles</small>
        </span>
      </a>
      <nav class="v25-nav" aria-label="Main navigation">
        <a href="/articles/index_en.html" aria-current="page">Articles</a>
        <a href="/articles/hk-mainland-property-inheritance/index_en.html">Topic</a>
        <a href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=articles-index-en-nav">Organise Facts</a>
        <a href="/">Main Site</a>
      </nav>
      {switch_html(zh_path, cn_path, en_path, "en", compact=True)}
      <a class="v25-contact" href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=articles-index-en-contact">Ask</a>
    </header>

    <section class="v25-hero" aria-labelledby="hero-title">
      <article class="v25-hero-main">
        <p class="v25-eyebrow">Hong Kong inheritance / Article hub</p>
        <h1 id="hero-title">Start with the question your family is stuck on now</h1>
        <p class="v25-lead">You may simply need to know whether the Mainland property can be handled, whether Hong Kong documents can be used, or what to do if a family member will not cooperate. Choose the closest situation first; you do not need to start with legal terminology.</p>
        <div class="v25-pills" aria-label="Reading priorities">
          <span>Start with the overview</span>
          <span>Choose your situation</span>
          <span>List the facts</span>
        </div>
      </article>
      <aside class="v25-hero-side" aria-label="Suggested reading order">
        <h2>Suggested Order</h2>
        <ol>
          <li>Read the overview first to see whether the problem is the property, documents, family cooperation or costs.</li>
          <li>If you already have Hong Kong documents, read the document article; if someone refuses to cooperate, read the dispute article.</li>
          <li>If records are scattered or family members live in different places, list the people, property and documents first.</li>
          <li>If you are still unsure, use the initial Q&amp;A to organise the facts for a lawyer.</li>
        </ol>
        <div class="v25-hero-actions">
          <a class="v25-primary" href="/articles/hk-mainland-property-inheritance/index_en.html">Read Overview</a>
          <a class="v25-secondary" href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=articles-index-en-hero">Organise Facts</a>
        </div>
      </aside>
    </section>

    <section class="v25-checkbar" aria-labelledby="checkbar-title">
      <div class="v25-checkbar-intro">
        <h2 id="checkbar-title">Choose what you need first</h2>
        <p>If you are not sure where to start, compare your situation with these four common questions.</p>
      </div>
      <div class="v25-check-items">
        <article><span>01</span><strong>Where To Start</strong><p>Property, documents or family cooperation</p></article>
        <article><span>02</span><strong>Hong Kong Documents</strong><p>Whether death certificates or authorisations can be used</p></article>
        <article><span>03</span><strong>Family Disagreement</strong><p>Refusal to sign, missing heirs or control of the property</p></article>
        <article><span>04</span><strong>Need Help</strong><p>Organise the facts before speaking to a lawyer</p></article>
      </div>
    </section>

    <section class="v25-content" aria-labelledby="article-index-title">
      <div class="v25-main">
        <div class="v25-section-copy">
          <h2 id="article-index-title">Hong Kong Inheritance Article Guide</h2>
          <p>Start with the article closest to your situation: documents, family disagreement, timing and costs, or simply not knowing where to begin.</p>
        </div>
        <article class="v25-pillar-card">
          <div class="v25-card-label">Overview</div>
          <div class="v25-pillar-copy">
            <h3>A Hong Kong family needs to inherit Mainland property: where should they start?</h3>
            <p>Use this first if you do not yet know where to begin. It helps you list the property, family members, documents and any disagreement.</p>
          </div>
          <a class="v25-pill-action" href="/articles/hk-mainland-property-inheritance/index_en.html">Read Overview</a>
        </article>
        <div class="v25-article-grid" aria-label="Hong Kong inheritance articles">
          <a class="v25-article-card" href="/articles/hk-mainland-property-inheritance/documents_en.html"><span class="v25-card-label v25-card-label-red">Article</span><h3>Can Hong Kong death certificates or family documents be used?</h3><p>For families who already have Hong Kong papers but do not know whether a Mainland office will accept them.</p></a>
          <a class="v25-article-card" href="/articles/hk-mainland-property-inheritance/dispute_en.html"><span class="v25-card-label v25-card-label-teal">Article</span><h3>What if heirs disagree or refuse to cooperate?</h3><p>For situations involving missing heirs, refusal to sign, will disputes or control of the asset.</p></a>
          <a class="v25-article-card" href="/articles/hk-mainland-property-inheritance/tax-cost_en.html"><span class="v25-card-label v25-card-label-red">Article</span><h3>How to think about tax, timing and legal costs</h3><p>For questions such as how long it may take and which facts may increase cost or delay.</p></a>
        </div>
        <section class="v25-other-topics" aria-labelledby="other-topics-title">
          <div class="v25-section-copy"><h2 id="other-topics-title">Other Cross-border Articles</h2><p>If your issue is not Hong Kong inheritance of Mainland assets, these articles may still help orient the next step.</p></div>
          <div class="v25-other-grid">
            <a class="v25-other-card" href="/articles/am/macau-client-mainland-lawyer.html"><strong>Macau clients handling Mainland China legal matters</strong><time datetime="2026-05-16">2026-05-16</time></a>
            <a class="v25-other-card" href="/articles/overseas-chinese/remote-entrust-china-lawyer.html"><strong>Overseas Chinese clients remotely instructing Mainland lawyers</strong><time datetime="2026-05-16">2026-05-16</time></a>
            <a class="v25-other-card" href="/articles/us/remote-china-lawyer.html"><strong>U.S.-based clients handling Mainland China legal matters</strong><time datetime="2026-05-16">2026-05-16</time></a>
          </div>
        </section>
      </div>
      <aside class="v25-side" aria-label="Topic navigation and next step">
        <section class="v25-side-card">
          <h2>What This Group Helps You Clarify</h2>
          <p>Use these article groups to decide whether to keep reading, submit basic facts, or organise the situation first.</p>
          <h3>Common Question Areas</h3>
          <ul><li>Where to start</li><li>Hong Kong documents and authorisation</li><li>Family disagreement and non-cooperation</li><li>Tax, timing and costs</li><li>Property status and next step</li></ul>
          <h3>Common Extensions</h3>
          <ul><li>Heirs spread across Hong Kong, Mainland China and overseas</li><li>Company interests, business assets and relocation compensation</li><li>Renunciation, authorisation and declaration documents</li></ul>
        </section>
        <section class="v25-side-card v25-side-actions">
          <h2>Next Step</h2>
          <div class="v25-side-buttons">
            <a class="v25-primary" href="/articles/hk-mainland-property-inheritance/index_en.html">Read Overview</a>
            <a class="v25-secondary" href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=articles-index-en-side">Organise Facts</a>
          </div>
        </section>
      </aside>
    </section>
    <section class="v25-bottom-cta" aria-label="Reading suggestion">
      <h2>Not sure which article to read first?</h2>
      <p>Prepare the city, registered owner, heir relationships, Hong Kong documents and any disagreement first, then choose the article closest to your situation.</p>
    </section>
  </main>
</body>
</html>
'''


MODERN = {
    "index": {
        "rel": "articles/hk-mainland-property-inheritance/index_en.html",
        "zh": "/articles/hk-mainland-property-inheritance/",
        "en": "/articles/hk-mainland-property-inheritance/index_en.html",
        "robots": "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1",
        "title": "A Hong Kong Family Needs to Inherit Mainland Property: Where to Start | Liu Yi Lawyer Team",
        "description": "For Hong Kong families handling Mainland property inheritance: first list the property, heirs, Hong Kong documents and any family disagreement, then decide the next step.",
        "published": "2026-05-21",
        "reading": "Published: 2026-05-21 · Updated: 2026-07-03 · About 6 minutes",
        "eyebrow": "Article / Hong Kong inheritance / Mainland property",
        "h1": "A Hong Kong family needs to inherit Mainland property: where should they start?",
        "lead": "If a family member left property in the Mainland, Hong Kong heirs usually get stuck on three things first: where the property is, who may inherit, and whether Hong Kong documents can be used. Once those facts are clear, it is easier to decide whether the next step is document preparation, family discussion or property handling.",
        "key_title": "Start With These Points",
        "keys": [
            "Do not start with the question 'can we transfer it?' Start with the city, registered owner and property status.",
            "Hong Kong death certificates, relationship documents or authorisations may need different preparation depending on use.",
            "If someone refuses to cooperate, is missing, or the property has mortgage or seizure issues, the order of work changes.",
        ],
        "answer_title": "Start With the Practical Answer",
        "answer": "This is usually not as simple as taking Hong Kong papers to a Mainland office. A steadier start is to organise the property information, the family relationship and the documents already held. If everyone cooperates, the next issue is usually documents and sequence. If someone refuses to sign, cannot be contacted, or the property itself has mortgage, seizure or unclear registration issues, evidence and family cooperation may need to be handled first.",
        "path_title": "Answer These Four Questions First",
        "path_intro": "You do not need to prepare every document before speaking to a lawyer. Start with these four questions.",
        "path": [
            ("1. Where is the property?", "Give the city, neighbourhood if known, and whose name appears on the property records."),
            ("2. When and where did the family member pass away?", "State the date and place of death, and where the death certificate is now held."),
            ("3. Which family members may inherit?", "List the possible heirs and whether anyone objects, is missing or will not sign."),
            ("4. Is there any property problem now?", "For example mortgage, seizure, missing certificate, someone living there or rent being collected."),
        ],
        "facts_title": "A Short Message You Can Send to a Lawyer",
        "facts_text": "The property is in [city] and is registered under [name]. The deceased passed away on [date / place]. The known heirs are [names / relationship]. Existing or missing documents include [will / death certificate / relationship proof / authorisation]. The property does or does not involve [mortgage / seizure / missing certificate / registration issue].",
        "facts": [
            "If you are in Hong Kong, state whether you can travel to the Mainland or prefer remote authorisation.",
            "If Hong Kong documents already exist, state what they are and what they will be used for.",
            "If heirs disagree, identify who disagrees and what the disagreement is about.",
            "If you mainly want an estimate of time or cost, provide the city and heir situation first.",
        ],
        "sections": [
            ("Why the property location matters", "Mainland property inheritance is usually handled through the rules and registration practice of the property location. Hong Kong probate or estate administration alone does not replace Mainland property transfer procedures.", "Where heirs cooperate and documents are complete, the route can be relatively direct. Where documents or heir relationships are unclear, the matter often needs evidence work before registration."),
            ("Hong Kong documents need to match the intended use", "Death certificates, relationship documents, declarations and powers of attorney formed in Hong Kong are not automatically accepted for every Mainland step.", "The first question is not only whether the document exists, but what it will be used for, where it was formed, and which Mainland office will receive it."),
            ("If heirs disagree, the route changes", "When heirs disagree, cannot be located or refuse to sign, the focus shifts from registration paperwork to confirming rights and resolving the distribution issue.", "In those cases, correspondence, evidence preservation, negotiation or court procedures may need to be considered before transfer registration."),
            ("Tax, timing and legal costs depend on the facts", "Costs and timing cannot be judged only by the property value. They depend on the city, document readiness, number and location of heirs, property status and whether any dispute exists.", "A clear fact summary usually gives a better first estimate than asking for a fixed quote at the start."),
        ],
        "related": [
            ("Hong Kong document use in Mainland inheritance", "/articles/hk-mainland-property-inheritance/documents_en.html"),
            ("Heir disagreement or dispute", "/articles/hk-mainland-property-inheritance/dispute_en.html"),
            ("Tax, timing and cost", "/articles/hk-mainland-property-inheritance/tax-cost_en.html"),
            ("Organise facts", "/ask/gpt/?topic=hk-mainland-property-inheritance&source=article-overview-en-related"),
        ],
        "faq": [
            ("Is Mainland property inheritance handled under Hong Kong law or Mainland procedures?", "For Mainland real estate, the property location and Mainland registration procedure are usually decisive. Hong Kong estate procedures cannot by themselves replace Mainland transfer registration."),
            ("Can a Hong Kong death certificate or relationship document be used directly?", "Usually it depends on the document type, where it was formed, what it will be used for and which Mainland office will receive it."),
            ("Can the property be transferred if heirs disagree?", "If heirs disagree, someone is missing or refuses to cooperate, the matter often cannot proceed as a simple registration case. Evidence, negotiation or court confirmation may be needed first."),
            ("Can tax and timing be estimated at the start?", "A rough direction may be possible, but a reliable estimate depends on the city, document status, heir cooperation and whether the property has mortgage, seizure or other registration issues."),
        ],
        "quick_title": "Quick Check",
        "quick": ["Where is the property and who is the registered owner?", "Are all heirs known and willing to cooperate?", "Do Hong Kong documents need to be used in Mainland procedures?", "Is there a mortgage, seizure, missing certificate or dispute?"],
        "toc": [("answer", "Practical answer"), ("facts", "Four facts"), ("documents", "Document use"), ("faq", "FAQ")],
        "cta_title": "Next Step",
        "cta_text": "Start by organising the property city, registered owner, heir relationships, Hong Kong documents and any disagreement. Then decide whether to prepare documents, authorisation or dispute evidence first.",
    },
    "bank-deposits": {
        "rel": "articles/hk-mainland-property-inheritance/bank-deposits_en.html",
        "zh": "/articles/hk-mainland-property-inheritance/bank-deposits.html",
        "en": "/articles/hk-mainland-property-inheritance/bank-deposits_en.html",
        "robots": "noindex,nofollow",
        "title": "Mainland Bank Deposits, Wealth Products or Insurance Left by a Relative: What Hong Kong Families Should Check First",
        "description": "For Hong Kong families trying to locate or handle Mainland bank deposits, wealth products or insurance after a relative's death, start with account clues, heirs, product type and whether someone already controls the funds.",
        "published": "2026-07-02",
        "reading": "Published: 2026-07-02 · Draft · About 6 minutes",
        "eyebrow": "Article / Hong Kong inheritance / Bank funds and insurance",
        "h1": "Mainland bank deposits, wealth products or insurance: what Hong Kong families should check first",
        "lead": "Many families do not begin by wanting litigation. They simply need to know whether the deceased had accounts in the Mainland, whether a bank will check them, whether a small balance can be handled more simply, and what to do if cards, phones or policies are already in someone else's hands.",
        "key_title": "Start With Three Points",
        "keys": ["Do not start with 'can we take the money'; start with account clues, family relationship and who holds the documents.", "Small-deposit simplified procedures may help, but they do not remove all document requirements.", "Deposits, wealth products, insurance and securities need separate review, especially where insurance beneficiaries are named."],
        "answer_title": "The Most Practical Starting Point",
        "answer": "These cases often stall because documents and account clues do not connect. The person has passed away, the account location is unclear, banks must check identity and relationship, and relatives may not cooperate. If someone already controls the phone, bank card, password or policy documents, the matter should not be treated as a simple withdrawal.",
        "path_title": "Break the Situation Into Four Parts",
        "path_intro": "You do not need to describe the law perfectly at the beginning. These four points usually tell us what should be checked next.",
        "path": [("1. What clues do you have?", "Bank cards, passbooks, SMS alerts, wage records, app screenshots, policies and old receipts can all matter."), ("2. Can the family cooperate?", "Whether spouse, children and parents can sign or provide documents affects the route."), ("3. What kind of money is it?", "Ordinary deposits, wealth products, insurance, securities, government bonds and debts are not handled identically."), ("4. Who controls the documents or account?", "If someone holds the card, phone, password or policy original, the priority is to preserve facts and records.")],
        "facts_title": "How to Brief the Lawyer",
        "facts_text": "The relative passed away on [date / place]. Current family members include [name / relationship]. Existing clues include [bank card / passbook / wage record / SMS / policy / wealth product record]. The suspected assets include [bank deposits / wealth products / bonds / insurance / securities / receivables]. The main problem is [unknown bank / family disagreement / funds already withdrawn / phone banking inaccessible / policy original held by someone else].",
        "facts": ["If you only know the person worked in a Mainland city, write down the city, employer and wage clues.", "Photograph old bank cards, SMS notices or product receipts even if incomplete.", "If someone holds the card, phone, password or policy original, record who holds it and since when.", "If you are in Hong Kong and need remote handling, state whether you can sign authorisation documents."],
        "sections": [("The first step is usually to find where the money is", "Families are often unsure whether the deceased had accounts, which bank held them, or whether wealth products or insurance existed. Useful clues include cards, passbooks, wage cards, app screenshots, SMS alerts, transfer records, product receipts, policies, employer details and usual account-opening locations.", "If the clues only show that money may exist in the Mainland but do not point to a bank or insurer, the next question is whether the clues are enough for a targeted inquiry."), ("A small balance does not mean immediate withdrawal", "Simplified handling for small balances can reduce some procedural burden, but it is not the same as withdrawing with only a death certificate.", "Banks may still review the applicant's status, heir relationship, account scope, balance calculation, documents and whether any dispute or abnormal transaction exists."), ("Deposits, wealth products and insurance should not be mixed together", "Ordinary deposits and some wealth products may have a simpler route. Insurance must first be checked for named beneficiaries. Securities and funds may involve brokerage accounts, holdings, dividends and transfer rules.", "A responsible first answer is often to separate the products before deciding the route."), ("If someone may already have taken or controlled the funds", "Where a relative holds the bank card, phone, SMS code or policy original, others may reasonably worry about transfer or withdrawal.", "The focus then becomes transaction traces, authorisation, agency explanations and whether records can be obtained or preserved.")],
        "related": [("Mainland property inheritance overview", "/articles/hk-mainland-property-inheritance/index_en.html"), ("Hong Kong document use", "/articles/hk-mainland-property-inheritance/documents_en.html"), ("Heir disagreement", "/articles/hk-mainland-property-inheritance/dispute_en.html"), ("Tax, timing and cost", "/articles/hk-mainland-property-inheritance/tax-cost_en.html")],
        "faq": [("We only know there may be Mainland deposits. What comes first?", "Do not ask every bank at random. Organise bank cards, passbooks, SMS alerts, wage records, old receipts, app screenshots, employer details and usual account locations first."), ("If the amount is under RMB 50,000, can it always be withdrawn directly?", "No. Simplified procedures may help some cases, but banks still review identity, heirs, balance, product type and whether any dispute exists."), ("If an insurance policy names a beneficiary, is it part of the estate?", "Usually the policy wording comes first. If a beneficiary is clearly named, payment is generally handled under the policy arrangement unless the beneficiary arrangement fails or another legal issue arises."), ("What if someone may already have withdrawn the money?", "Preserve bank cards, phones, SMS records, transfer clues and who held original documents. Then consider whether transaction details can be requested and whether negotiation or dispute action is needed.")],
        "quick_title": "Where Are You Stuck?",
        "quick": ["No one knows where the money is.", "The account or policy is known, but the institution will not handle it directly.", "Family members disagree or someone holds the card, phone or policy.", "Deposits, wealth products and insurance are mixed together."],
        "toc": [("answer", "Practical starting point"), ("facts", "Four parts"), ("query", "Find the money"), ("dispute", "Possible withdrawal"), ("faq", "FAQ")],
        "cta_title": "Next Step",
        "cta_text": "Organise the bank cards, SMS, policies, wage clues, family relationship and who holds the documents before deciding whether to inquire, authorise or prepare inheritance materials.",
    },
}


LEGACY = {
    "documents": {
        "rel": "articles/hk-mainland-property-inheritance/documents_en.html",
        "zh": "/articles/hk-mainland-property-inheritance/documents.html",
        "en": "/articles/hk-mainland-property-inheritance/documents_en.html",
        "robots": "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1",
        "title": "Can Hong Kong Death Certificates or Family Documents Be Used for Mainland Inheritance?",
        "description": "For Hong Kong documents in Mainland property inheritance, first identify where the document was issued, what it will be used for and which city the property is in.",
        "published": "2026-05-22",
        "eyebrow": "Hong Kong documents · Mainland inheritance",
        "h1": "Can Hong Kong death certificates or family documents be used for Mainland inheritance?",
        "tags": ["Hong Kong documents", "Document use", "Mainland property inheritance"],
        "image": "/img/lxwm1.webp",
        "hide_image": True,
        "alt": "Hong Kong and Mainland cross-border documents for property inheritance",
        "caption": "For Mainland property inheritance, the key is not only whether a document exists, but whether it will be accepted for the specific Mainland procedure.",
        "intro": "Many Hong Kong families already have a death certificate, family relationship material, declaration or power of attorney, but do not know whether it can be used for Mainland property inheritance. Do not start only with 'can this be used directly?' First clarify where the document was issued, which city will receive it, and whether it is for property handling, authorisation or a family dispute.",
        "notice": "This article helps you classify the document issue. It is not a final checklist for a specific office; the exact route depends on the property city and document use.",
        "quick_eyebrow": "Start with document use",
        "quick_title": "The same Hong Kong document may be treated differently depending on use",
        "quick_text": "A document used to prove death, show family relationship, authorise someone or handle property may need different preparation.",
        "button": "Organise document questions",
        "sections": [
            ("Four common document groups", ["Death certificate: confirms death; the issuing place, original status and Mainland requirements matter.", "Family relationship materials: may need to connect birth, marriage, household or other records.", "Declaration or renunciation documents: usually require stricter identity and signing checks.", "Power of attorney: the scope of authorisation and document-use requirements should be checked if a Hong Kong heir cannot attend in person."]),
            ("Why documents sometimes need extra handling", "For Hong Kong documents to be used in the Mainland, the practical question is not the label of the procedure. First confirm the document type, the receiving city, the intended use and the office that will receive it."),
            ("Property matters look beyond one document", "Mainland property inheritance usually looks beyond one Hong Kong document. Death records, wills, family agreement, relationship evidence and property status may all matter together."),
            ("Information to prepare first", ["Property city and registered owner.", "Where the deceased passed away and where the death certificate is held.", "The heir list and whether anyone is in Hong Kong, the Mainland or overseas.", "Whether any will, declaration, renunciation or authorisation already exists.", "Whether the document will be used for property handling, family discussion, dispute handling or authorisation."]),
        ],
        "related": [("Overview", "/articles/hk-mainland-property-inheritance/index_en.html"), ("Heir dispute", "/articles/hk-mainland-property-inheritance/dispute_en.html"), ("Tax and timing", "/articles/hk-mainland-property-inheritance/tax-cost_en.html")],
        "cta_title": "Describe the document situation first",
        "cta_text": "If you are unsure whether a Hong Kong document can be used, organise its type, source, intended use and property location before deciding the next step.",
    },
    "dispute": {
        "rel": "articles/hk-mainland-property-inheritance/dispute_en.html",
        "zh": "/articles/hk-mainland-property-inheritance/dispute.html",
        "en": "/articles/hk-mainland-property-inheritance/dispute_en.html",
        "robots": "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1",
        "title": "Hong Kong Heirs Inheriting Mainland Property: What If Someone Refuses to Cooperate?",
        "description": "When heirs disagree, refuse to sign, are missing, or dispute a will, Mainland property inheritance often requires evidence, negotiation or court confirmation before registration.",
        "published": "2026-05-22",
        "eyebrow": "Heir dispute · Mainland property transfer",
        "h1": "Hong Kong residents inheriting Mainland property: what if heirs disagree or refuse to cooperate?",
        "tags": ["Heir dispute", "Will", "Court route"],
        "image": "/articles/hk-mainland-property-inheritance/heir-dispute-property-documents.webp",
        "alt": "Heir disagreement, documents and Mainland property handling",
        "caption": "When heirs disagree, the focus usually shifts from direct registration to confirming inheritance rights and distribution.",
        "intro": "If all heirs cooperate, the route can be relatively clear. More often, one heir is in Hong Kong, another in the Mainland, someone objects to the proposed distribution, someone cannot be contacted, or a will is challenged. In those cases, the first question is not simply whether the property can be transferred, but what kind of dispute exists.",
        "notice": "Online content only helps with initial orientation. In a dispute, preserve evidence and avoid signing unclear documents or privately disposing of property.",
        "quick_eyebrow": "Identify the dispute type",
        "quick_title": "Different disputes require different routes",
        "quick_text": "Refusal to sign, missing heirs, questioned wills and registration issues should not be handled with one template.",
        "button": "Ask about heir dispute",
        "sections": [
            ("Four common forms of non-cooperation", ["Heirs can be contacted but disagree over shares, sale or who should register the property.", "Heirs live in Hong Kong, overseas or different Mainland cities and cannot all attend signing.", "Someone is missing, refuses identity documents or will not sign renunciation or authorisation papers.", "Someone challenges the will, its scope or whether all heirs have been included."]),
            ("Why a disputed matter cannot simply proceed to registration", "Mainland registration usually needs materials proving inheritance rights and distribution. If heirs have no agreed arrangement, a registry or notary office will not resolve the substantive dispute for them. Negotiation, evidence work, lawyer correspondence or court confirmation may be needed first."),
            ("A will still needs to be checked against the property", "Where a will exists, its form, signing time, property scope, later revocation and objections from other heirs still matter. A Hong Kong will or declaration may also need to meet Mainland use requirements."),
            ("Evidence to organise first", ["Death certificate, property certificate or purchase materials.", "Identity, relationship records and contact information for all possible heirs.", "Will, declarations, renunciation documents, communications, payment or contribution records.", "The real dispute: who objects, what they object to and whether they have made a clear claim.", "Mortgage, seizure, co-owner, missing certificate or other property status issues."]),
        ],
        "related": [("Overview", "/articles/hk-mainland-property-inheritance/index_en.html"), ("Hong Kong documents", "/articles/hk-mainland-property-inheritance/documents_en.html"), ("Tax and timing", "/articles/hk-mainland-property-inheritance/tax-cost_en.html")],
        "cta_title": "Start by explaining the heirs and the dispute",
        "cta_text": "Organise the heir list, dispute focus, documents and property status before deciding whether to negotiate, supplement evidence or consider a court route.",
    },
    "tax-cost": {
        "rel": "articles/hk-mainland-property-inheritance/tax-cost_en.html",
        "zh": "/articles/hk-mainland-property-inheritance/tax-cost.html",
        "en": "/articles/hk-mainland-property-inheritance/tax-cost_en.html",
        "robots": "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1",
        "title": "Tax, Timing and Costs for Hong Kong Residents Inheriting Mainland Property",
        "description": "Tax, timing and legal costs for Hong Kong residents inheriting Mainland property depend on heir relationships, documents, property location, registration status and disputes.",
        "published": "2026-05-22",
        "eyebrow": "Tax and timing · Cost assessment",
        "h1": "Hong Kong residents inheriting Mainland property: how to think about tax, timing and costs",
        "tags": ["Tax", "Timing", "Cost assessment"],
        "image": "/img/banner1.webp",
        "alt": "Tax and timing assessment for Hong Kong residents inheriting Mainland property",
        "caption": "Tax and timing cannot be judged only by property value. Document readiness, dispute status and local requirements also matter.",
        "intro": "Clients often ask at the beginning how much it will cost and how long it will take. A rough direction may be possible, but a fixed answer is rarely reliable without the property city, heir relationship, Hong Kong documents, registration status and any dispute information.",
        "notice": "This article helps explain cost components and timing variables. It does not provide a fixed amount, fixed timetable or guaranteed outcome.",
        "quick_eyebrow": "Clarify the variables first",
        "quick_title": "Tax, timing and legal fees should be considered separately",
        "quick_text": "Tax rules, registration costs, document costs, dispute costs and lawyer assistance are different layers of the matter.",
        "button": "Ask about cost and timing",
        "sections": [
            ("Separate the main cost groups", ["Tax: whether any exemption or reduction applies depends on inheritance type and local practice.", "Registration and document costs: certificates, searches, translations or replacement documents may create costs.", "Hong Kong document costs: declarations, authorisations or other document preparation may be needed.", "Dispute costs: disagreement, will disputes or abnormal property status can increase evidence and procedure costs.", "Legal assistance: fees depend on complexity, document readiness, cross-city coordination and dispute work."]),
            ("Intestate inheritance and will-based inheritance differ", "Where statutory heirs are clear, documents are complete and no one objects, timing and cost are usually easier to assess. Wills, renunciation, gifts by will, missing heirs or objections require inheritance rights and document usability to be addressed first."),
            ("Why timing is hard to quote in one sentence", "Timing depends on the property city, registration requirements, Hong Kong document preparation, heir cooperation, mortgage, missing certificate, seizure or other title issues. One blocked step can change the schedule."),
            ("Information needed for a better estimate", ["Property city, property nature and whether there is a real estate certificate.", "Place of death and current death or relationship records.", "Whether there is a will, renunciation or statutory inheritance only.", "Number and location of heirs and whether all can sign.", "Mortgage, seizure, missing certificate or registration inconsistency."]),
        ],
        "related": [("Overview", "/articles/hk-mainland-property-inheritance/index_en.html"), ("Hong Kong documents", "/articles/hk-mainland-property-inheritance/documents_en.html"), ("Heir dispute", "/articles/hk-mainland-property-inheritance/dispute_en.html")],
        "cta_title": "Explain the cost and timing variables first",
        "cta_text": "Before asking for a fixed quote, organise the property city, heirs, Hong Kong documents and dispute status.",
    },
}


def render_modern(slug: str, data: dict) -> str:
    cn_path = cn_from_zh_path(data["zh"])
    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": data["h1"],
        "description": data["description"],
        "datePublished": data["published"],
        "dateModified": TODAY,
        "image": IMAGE,
        "inLanguage": "en",
        "author": {"@type": "Organization", "name": "Liu Yi Lawyer Team"},
        "publisher": {"@type": "Organization", "name": "Liu Yi Lawyer Team", "url": url("/")},
        "mainEntityOfPage": url(data["en"]),
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in data["faq"]
        ],
    }
    path_items = "\n".join(
        f'<article><span></span><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for title, text in data["path"]
    )
    facts = "\n".join(f"<li>{esc(x)}</li>" for x in data["facts"])
    sections = "\n".join(
        f'<article class="hk-section-card"><h2>{esc(h)}</h2><p>{esc(p1)}</p><p>{esc(p2)}</p></article>'
        for h, p1, p2 in data["sections"]
    )
    related = "\n".join(f'<a href="{href}">{esc(label)}</a>' for label, href in data["related"])
    faq = "\n".join(f'<article class="faq-card"><h3>{esc(q)}</h3><p>{esc(a)}</p></article>' for q, a in data["faq"])
    quick = "\n".join(f"<li>{esc(x)}</li>" for x in data["quick"])
    toc = "\n".join(f'<a href="#{anchor}">{esc(label)}</a>' for anchor, label in data["toc"])
    keys = "\n".join(f"<li>{esc(x)}</li>" for x in data["keys"])
    return f'''{head_common(lang="en", title=data["title"], description=data["description"], robots=data["robots"], canonical_path=data["en"], zh_path=data["zh"], cn_path=cn_path, en_path=data["en"], og_type="article")}
  <meta property="article:published_time" content="{data["published"]}">
  <meta property="article:modified_time" content="{TODAY}">
  <script type="application/ld+json">{json_ld(article_ld)}</script>
  <script type="application/ld+json">{json_ld(faq_ld)}</script>
</head>
<body class="article-detail article-hk-inheritance article-en">
{header_detail(data["zh"], cn_path, data["en"])}
  <main>
    <section class="article-hero" aria-label="Article introduction">
      <div class="article-hero-inner">
        <div class="article-hero-copy">
          <p class="eyebrow">{esc(data["eyebrow"])}</p>
          <h1>{esc(data["h1"])}</h1>
          <p class="article-lead">{esc(data["lead"])}</p>
          <div class="reading-meta">{esc(data["reading"])}</div>
        </div>
        <aside class="article-key-card" aria-label="Key points">
          <h2>{esc(data["key_title"])}</h2>
          <ul class="article-key-list">{keys}</ul>
        </aside>
      </div>
    </section>
    <div class="article-shell">
      <article class="article-main">
        <section id="answer" class="answer-card"><h2>{esc(data["answer_title"])}</h2><p>{esc(data["answer"])}</p></section>
        <section id="facts" class="reading-path" aria-label="Key facts">
          <h2>{esc(data["path_title"])}</h2><p class="path-intro">{esc(data["path_intro"])}</p><div class="path-grid">{path_items}</div>
        </section>
        <section class="copy-format facts-card"><h2>{esc(data["facts_title"])}</h2><p>{esc(data["facts_text"])}</p><ul class="fact-list">{facts}</ul></section>
        <div class="hk-detail-grid">{sections}</div>
        <section class="copy-format"><h2>Related Reading</h2><div class="hk-related-links">{related}</div></section>
        <section id="faq" class="faq-section" aria-label="FAQ"><h2>FAQ</h2>{faq}</section>
      </article>
      <aside class="toc" aria-label="Article table of contents">
        <section class="quick-check"><h2>{esc(data["quick_title"])}</h2><ul>{quick}</ul></section>
        <h2>Contents</h2>{toc}
        <a class="toc-cta" href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-{slug}-en-aside">Organise facts →</a>
      </aside>
    </div>
    <section class="cta-panel"><h2>{esc(data["cta_title"])}</h2><p>{esc(data["cta_text"])}</p><a class="button" href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-{slug}-en-bottom">Organise facts →</a></section>
  </main>
  <footer class="site-footer"><div class="footer-inner">This article is for initial information only. Specific matters should be reviewed by a lawyer together with the documents.</div></footer>
  <script src="/articles/script.js" defer></script>
</body>
</html>
'''


def render_legacy(slug: str, data: dict) -> str:
    cn_path = cn_from_zh_path(data["zh"])
    article_ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": data["h1"],
        "description": data["description"],
        "datePublished": data["published"],
        "dateModified": TODAY,
        "image": url(data["image"]),
        "inLanguage": "en",
        "author": {"@type": "Organization", "name": "Liu Yi Lawyer Team"},
        "publisher": {"@type": "Organization", "name": "Liu Yi Lawyer Team", "url": url("/")},
        "mainEntityOfPage": url(data["en"]),
    }
    tags = "\n".join(f'<span class="tag">{esc(t)}</span>' for t in data["tags"])
    image_html = "" if data.get("hide_image") else f'''
      <figure class="article-visual"><img src="{data["image"]}" alt="{esc(data["alt"])}" loading="lazy" decoding="async"><figcaption>{esc(data["caption"])}</figcaption></figure>'''
    section_html = []
    for section in data["sections"]:
        h = section[0]
        body = section[1]
        if isinstance(body, list):
            section_html.append(f'<h2>{esc(h)}</h2><ul>' + "".join(f"<li>{esc(x)}</li>" for x in body) + "</ul>")
        else:
            section_html.append(f"<h2>{esc(h)}</h2><p>{esc(body)}</p>")
    related = "\n".join(f'<a href="{href}">{esc(label)}</a>' for label, href in data["related"])
    return f'''{head_common(lang="en", title=data["title"], description=data["description"], robots=data["robots"], canonical_path=data["en"], zh_path=data["zh"], cn_path=cn_path, en_path=data["en"], og_type="article")}
  <meta property="article:published_time" content="{data["published"]}">
  <meta property="article:modified_time" content="{TODAY}">
  <script type="application/ld+json">{json_ld(article_ld)}</script>
</head>
<body class="article-detail-legacy article-hk-inheritance article-en">
{header_detail(data["zh"], cn_path, data["en"])}
  <main class="article-shell">
    <article class="article-main">
      <p class="eyebrow">{esc(data["eyebrow"])}</p>
      <h1>{esc(data["h1"])}</h1>
      <div class="meta"><span>Published: {data["published"]}</span>{tags}</div>
{image_html}
      <p>{esc(data["intro"])}</p>
      <div class="notice">{esc(data["notice"])}</div>
      <section class="quick-judge"><div><p class="eyebrow">{esc(data["quick_eyebrow"])}</p><h2>{esc(data["quick_title"])}</h2><p>{esc(data["quick_text"])}</p></div><div class="quick-actions"><a class="button" href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-{slug}-en-top">{esc(data["button"])}</a><a class="button-secondary" href="/topics/hk-mainland-property-inheritance/?source=article-{slug}-en-top">Submit Basic Facts</a></div></section>
      {''.join(section_html)}
      <div class="inline-cta"><strong>Not sure yet?</strong><span>Prepare the city, documents, heirs and the immediate issue first.</span><a href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-{slug}-en-inline">Organise facts first</a></div>
      <div class="related-box"><h2>Related Reading</h2>{related}</div>
      <div class="cta-panel"><h2>{esc(data["cta_title"])}</h2><p>{esc(data["cta_text"])}</p><div class="actions"><a class="button" href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-{slug}-en-bottom">Organise facts first</a><a class="button-secondary" href="/topics/hk-mainland-property-inheritance/?source=article-{slug}-en-bottom">Submit Basic Facts</a></div></div>
    </article>
    <aside class="toc" aria-label="Article table of contents"><h2>Contents</h2><a href="/articles/hk-mainland-property-inheritance/index_en.html">Overview</a><a href="/articles/hk-mainland-property-inheritance/documents_en.html">Documents</a><a href="/articles/hk-mainland-property-inheritance/dispute_en.html">Disputes</a><a href="/articles/hk-mainland-property-inheritance/tax-cost_en.html">Costs</a><a href="/ask/gpt/?topic=hk-mainland-property-inheritance&amp;source=article-{slug}-en-toc">Organise facts</a></aside>
  </main>
  <footer class="site-footer"><div class="footer-inner">© 2026 Liu Yi Lawyer Team. This article is for initial information only. Specific matters should be reviewed by a lawyer together with the documents.</div></footer>
  <script src="/articles/script.js" defer></script>
</body>
</html>
'''


def patch_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    for loc in [
        "https://www.jingwei-law.com/articles/index_cn.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/index_cn.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/documents_cn.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/dispute_cn.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/tax-cost_cn.html",
        "https://www.jingwei-law.com/articles/index_en.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/index_en.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/documents_en.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/dispute_en.html",
        "https://www.jingwei-law.com/articles/hk-mainland-property-inheritance/tax-cost_en.html",
    ]:
        if loc not in text:
            block = f'''  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.55</priority>
  </url>
'''
            text = text.replace("</urlset>", block + "</urlset>")
    text = re.sub(r"(<loc>https://www\.jingwei-law\.com/articles(?:/|/hk-mainland-property-inheritance/(?:|documents\.html|dispute\.html|tax-cost\.html))</loc>\n\s*<lastmod>)[^<]+", rf"\g<1>{TODAY}", text)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    chinese_page("articles/index.html", "/articles/", cn_from_zh_path("/articles/"), "/articles/index_en.html", is_index=True)
    simplified_page("articles/index.html", "articles/index_cn.html", "/articles/", cn_from_zh_path("/articles/"), "/articles/index_en.html", is_index=True)
    for rel, zh, en in [
        ("articles/hk-mainland-property-inheritance/index.html", "/articles/hk-mainland-property-inheritance/", "/articles/hk-mainland-property-inheritance/index_en.html"),
        ("articles/hk-mainland-property-inheritance/documents.html", "/articles/hk-mainland-property-inheritance/documents.html", "/articles/hk-mainland-property-inheritance/documents_en.html"),
        ("articles/hk-mainland-property-inheritance/dispute.html", "/articles/hk-mainland-property-inheritance/dispute.html", "/articles/hk-mainland-property-inheritance/dispute_en.html"),
        ("articles/hk-mainland-property-inheritance/tax-cost.html", "/articles/hk-mainland-property-inheritance/tax-cost.html", "/articles/hk-mainland-property-inheritance/tax-cost_en.html"),
        ("articles/hk-mainland-property-inheritance/bank-deposits.html", "/articles/hk-mainland-property-inheritance/bank-deposits.html", "/articles/hk-mainland-property-inheritance/bank-deposits_en.html"),
        ("articles/hk-mainland-property-inheritance/social-security-housing-fund.html", "/articles/hk-mainland-property-inheritance/social-security-housing-fund.html", "/articles/hk-mainland-property-inheritance/social-security-housing-fund_en.html"),
        ("articles/hk-mainland-property-inheritance/missing-documents.html", "/articles/hk-mainland-property-inheritance/missing-documents.html", "/articles/hk-mainland-property-inheritance/missing-documents_en.html"),
        ("articles/hk-mainland-property-inheritance/ancestral-home-homestead.html", "/articles/hk-mainland-property-inheritance/ancestral-home-homestead.html", "/articles/hk-mainland-property-inheritance/ancestral-home-homestead_en.html"),
    ]:
        cn = cn_from_zh_path(zh)
        chinese_page(rel, zh, cn, en)
        simplified_page(rel, rel_to_cn(rel), zh, cn, en)

    write("articles/index_en.html", render_index_en())
    for slug, data in MODERN.items():
        write(data["rel"], render_modern(slug, data))
    for slug, data in LEGACY.items():
        write(data["rel"], render_legacy(slug, data))

    # Draft English mirrors: use the same reader-first article template and keep noindex.
    for slug in ["social-security-housing-fund", "missing-documents", "ancestral-home-homestead"]:
        src = {
            "social-security-housing-fund": ("Social Security, Housing Fund and Related Benefits for Hong Kong Heirs", "Hong Kong heirs handling Mainland social insurance balances, housing fund, funeral subsidies or pensions should first identify the city, employer, account clues and whether any amounts were already claimed."),
            "missing-documents": ("What If the Deceased Passed Away Years Ago and Mainland Inheritance Documents Are Incomplete?", "For older Mainland inheritance matters, Hong Kong heirs should rebuild the chain of death records, heirs, asset clues and current possession before deciding the next step."),
            "ancestral-home-homestead": ("Ancestral Homes, Homestead Houses and Historic Mainland Properties: What Hong Kong Heirs Should Check First", "Hong Kong heirs dealing with ancestral homes, homestead houses or historic Mainland properties should first identify land nature, title source, possession, relocation status and available records."),
        }[slug]
        base = MODERN["bank-deposits"].copy()
        base.update({
            "rel": f"articles/hk-mainland-property-inheritance/{slug}_en.html",
            "zh": f"/articles/hk-mainland-property-inheritance/{slug}.html",
            "en": f"/articles/hk-mainland-property-inheritance/{slug}_en.html",
            "title": src[0] + " | Liu Yi Lawyer Team",
            "description": src[1],
            "h1": src[0],
            "lead": src[1],
            "eyebrow": "Article / Hong Kong inheritance / Draft",
            "reading": "Published: 2026-07-02 · Draft · About 6 minutes",
            "keys": ["Identify the asset or benefit type before choosing a procedure.", "Organise the family relationship, document gaps and who currently controls the records.", "If someone already occupies, manages or has claimed the asset, preserve facts before taking the next step."],
            "answer_title": "Start With the Missing Facts",
            "answer": "For this type of matter, the first task is usually not to ask for a fixed answer. It is to identify what facts are missing, which institution or asset is involved, who can cooperate, and whether anyone already controls the documents, account, house or benefit.",
            "path_title": "Clarify Four Layers First",
            "path_intro": "These four layers normally decide whether the next step is document preparation, inquiry, authorisation or dispute handling.",
            "path": [("1. What asset or benefit is involved?", "Property, funds, benefits, old housing rights and compensation may follow different routes."), ("2. What documents still exist?", "Keep copies of identity records, old certificates, account clues, employer records and family papers."), ("3. Who are the heirs?", "List all relevant family members, including those who have passed away earlier or live overseas."), ("4. Who controls the asset now?", "Occupation, rent collection, account access or document possession may change the handling order.")],
            "facts_title": "How to Brief the Lawyer",
            "facts_text": "The deceased passed away in [year / place]. Known heirs are [names / relationship / location]. Existing records include [death record / property or account clues / employer or benefit records / old family papers]. The current problem is [missing documents / someone controls the asset / family disagreement / unclear institution].",
            "facts": ["Do not only say that documents are missing; list what still exists.", "If heirs are spread across Hong Kong, the Mainland and overseas, state who can be contacted.", "If someone controls keys, documents, rent, accounts or benefits, state this early.", "If remote handling is needed from Hong Kong, state whether authorisation documents can be signed."],
            "sections": [("Why the first step is fact reconstruction", "Older and more complex matters often fail because the fact chain is broken, not because there is no possible route.", "The practical first step is to rebuild the timeline, family relationship, asset clue and current control situation."), ("Documents and assets should be separated", "A missing death record, missing relationship proof and missing title or account clue are different problems.", "Treating them as one general document problem can lead to the wrong preparation path."), ("Control or possession changes the route", "If someone occupies a house, collects rent, holds original records or has already claimed money, the matter is no longer only about supplementing documents.", "Evidence preservation and dispute assessment may need to run together with document work."), ("Prepare a concise fact summary", "A short summary of who passed away, who the heirs are, what asset is involved and what is missing is often more useful than a long general question.", "This allows the next step to be matched to the real bottleneck.")],
            "faq": [("Does missing documentation mean nothing can be done?", "Not necessarily. The real question is which layer is missing: death record, heir relationship, asset clue or current control."), ("What should Hong Kong heirs prepare first?", "Prepare a list of existing documents, family members, asset clues and anyone who currently holds records or controls the asset."), ("What if family members disagree?", "Then the matter may need evidence preservation, negotiation or dispute handling before a simple application can proceed."), ("Can this be handled remotely?", "Some steps may be prepared remotely, but authorisation and document-use requirements should be checked early.")],
        })
        write(base["rel"], render_modern(slug, base))

    patch_sitemap()


if __name__ == "__main__":
    main()
