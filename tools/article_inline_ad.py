from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
ARTICLES_ROOT = ROOT / "articles"
IMAGE_SRC = "/articles/assets/ai-legal-assistant-native-ad-v2.webp"
ARTICLE_IMAGE_URL = "https://www.jingwei-law.com/articles/article-library-desk-v26.jpg"

GRID_RE = re.compile(
    r'<section class="article-image-grid"[^>]*>.*?</section>', re.DOTALL
)
AD_RE = re.compile(r'<a class="article-native-ad"')
AD_BLOCK_RE = re.compile(
    r'<a class="article-native-ad"[^>]*>.*?</a>', re.DOTALL
)
AD_TOPIC_RE = re.compile(
    r'(<a class="article-native-ad" href="/ask/gpt/\?topic=)[^&"]+'
    r'(&amp;source=article-inline-ad-[^"]+")'
)
LANG_RE = re.compile(r'<html[^>]+lang="([^"]+)"', re.IGNORECASE)
TOPIC_RE = re.compile(r'/ask/gpt/\?topic=([^&"\s]+)')
STYLE_HREF_RE = re.compile(r'/articles/style\.css(?:\?v=\d+)?')
GRID_OVERRIDE_RE = re.compile(
    r'\s*<style>\s*\.article-regional-inheritance \.article-image-grid\{.*?</style>\s*',
    re.DOTALL,
)
ARTICLE_IMAGE_ARRAY_RE = re.compile(r'"image"\s*:\s*\[[^\]]*\]')
ARTICLE_SCHEMA_RE = re.compile(r'"@type"\s*:\s*"Article"')


COPY = {
    "zh-Hant": {
        "label": "劉毅律師團隊 · 站內服務",
        "headline": "事情很多，不妨先把問題說清楚",
        "description": "法律助手會按地區和事項，幫你整理人物、文件與資產線索，再提示下一步要補甚麼。",
        "action": "開始整理案情",
        "aria": "站內推廣：使用 AI 法律助手整理案情",
    },
    "zh-Hans": {
        "label": "刘毅律师团队 · 站内服务",
        "headline": "事情很多，不妨先把问题说清楚",
        "description": "法律助手会按地区和事项，帮你整理人物、文件与资产线索，再提示下一步要补什么。",
        "action": "开始整理案情",
        "aria": "站内推广：使用 AI 法律助手整理案情",
    },
    "en": {
        "label": "Liu Yi Lawyer Team · Internal service",
        "headline": "Too many loose ends? Start by organising the facts",
        "description": "The legal assistant sorts the people, documents and asset clues by location, then highlights what to clarify next.",
        "action": "Organise my case",
        "aria": "Internal promotion: use the AI legal assistant to organise the facts",
    },
}


def page_language(text: str) -> str:
    match = LANG_RE.search(text)
    value = match.group(1) if match else "zh-Hant"
    if value.lower().startswith("en"):
        return "en"
    if value.lower() in {"zh-hans", "zh-cn"}:
        return "zh-Hans"
    return "zh-Hant"


def page_topic(text: str, path: Path) -> str:
    relative = path.relative_to(ARTICLES_ROOT)
    first = relative.parts[0]
    directory_topic = {
        "am": "macau",
        "singapore": "singapore",
        "us": "united-states",
        "hong-kong-other-estate": "hong-kong-other-estate",
        "overseas-chinese": "overseas-chinese",
        "hk-mainland-property-inheritance": "hk-inheritance",
    }.get(first)
    if directory_topic:
        return directory_topic
    match = TOPIC_RE.search(text)
    if match:
        return html.unescape(match.group(1))
    return "articles"


def retarget_native_ad(text: str, path: Path) -> str:
    topic = page_topic(text, path)
    return AD_TOPIC_RE.sub(rf"\g<1>{topic}\g<2>", text, count=1)


def page_slug(path: Path) -> str:
    stem = path.stem
    for suffix in ("_cn", "_en"):
        if stem.endswith(suffix):
            return stem[: -len(suffix)]
    return stem


def render_inline_ad(language: str, topic: str, slug: str) -> str:
    copy = COPY[language]
    href = (
        "/ask/gpt/?topic="
        + quote(topic, safe="-")
        + "&source=article-inline-ad-"
        + quote(slug, safe="-")
    )
    return (
        f'<a class="article-native-ad" href="{html.escape(href, quote=True)}" '
        f'aria-label="{html.escape(copy["aria"], quote=True)}">'
        '<span class="article-native-ad__media" aria-hidden="true">'
        f'<img src="{IMAGE_SRC}" alt="" width="1536" height="1024" loading="lazy" decoding="async">'
        "</span>"
        '<span class="article-native-ad__copy">'
        f'<span class="article-native-ad__label">{html.escape(copy["label"])}</span>'
        f'<strong>{html.escape(copy["headline"])}</strong>'
        f'<span class="article-native-ad__description">{html.escape(copy["description"])}</span>'
        "</span>"
        f'<span class="article-native-ad__action">{html.escape(copy["action"])}'
        '<span aria-hidden="true">→</span></span>'
        "</a>"
    )


def normalize_article_schema_image(text: str) -> str:
    if '"@type":"Article"' not in text and '"@type": "Article"' not in text:
        return text
    return ARTICLE_IMAGE_ARRAY_RE.sub(
        '"image":["' + ARTICLE_IMAGE_URL + '"]', text, count=1
    )


def migrate_page(path: Path, *, write: bool) -> tuple[bool, str]:
    text = path.read_text(encoding="utf-8")
    grids = GRID_RE.findall(text)
    ads = AD_RE.findall(text)
    if not grids:
        if ads:
            if len(ads) != 1:
                raise RuntimeError(
                    f"Unexpected native ad count in {path.relative_to(ROOT)}: {len(ads)}"
                )
            replacement = render_inline_ad(
                page_language(text), page_topic(text, path), page_slug(path)
            )
            updated, count = AD_BLOCK_RE.subn(replacement, text, count=1)
            if count != 1:
                raise RuntimeError(
                    f"Could not refresh native ad: {path.relative_to(ROOT)}"
                )
            updated = normalize_article_schema_image(updated)
            updated = retarget_native_ad(updated, path)
            updated = STYLE_HREF_RE.sub("/articles/style.css?v=29", updated)
            if write and updated != text:
                path.write_text(updated, encoding="utf-8")
            return updated != text, page_language(text)
        return False, "not-an-article-grid-page"
    if len(grids) != 1 or ads:
        raise RuntimeError(
            f"Unexpected ad/grid count in {path.relative_to(ROOT)}: "
            f"grids={len(grids)}, ads={len(ads)}"
        )
    language = page_language(text)
    replacement = render_inline_ad(language, page_topic(text, path), page_slug(path))
    updated, count = GRID_RE.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"Could not replace image grid: {path.relative_to(ROOT)}")
    updated = GRID_OVERRIDE_RE.sub("\n", updated)
    updated = STYLE_HREF_RE.sub("/articles/style.css?v=29", updated)
    updated = normalize_article_schema_image(updated)
    updated = retarget_native_ad(updated, path)
    if write:
        path.write_text(updated, encoding="utf-8")
    return True, language


def article_pages() -> list[Path]:
    return sorted(ARTICLES_ROOT.rglob("*.html"))


def migrate(*, write: bool) -> int:
    changed = 0
    languages: dict[str, int] = {}
    for path in article_pages():
        did_change, reason = migrate_page(path, write=write)
        if did_change:
            changed += 1
            languages[reason] = languages.get(reason, 0) + 1
    mode = "migrated" if write else "would migrate"
    print(f"{mode}: {changed} article pages")
    for language, count in sorted(languages.items()):
        print(f"  {language}: {count}")
    return changed


def audit() -> int:
    errors: list[str] = []
    article_count = 0
    for path in article_pages():
        text = path.read_text(encoding="utf-8")
        if 'data-article-redirect' in text or "topic-collection" in text:
            continue
        is_article = bool(ARTICLE_SCHEMA_RE.search(text))
        if not is_article and "article-native-ad" not in text and "article-image-grid" not in text:
            continue
        if "article-image-grid" in text:
            errors.append(f"legacy image grid: {path.relative_to(ROOT)}")
            continue
        if "article-native-ad" not in text:
            errors.append(f"missing native ad: {path.relative_to(ROOT)}")
            continue
        article_count += 1
        if len(AD_RE.findall(text)) != 1:
            errors.append(f"native ad count is not 1: {path.relative_to(ROOT)}")
        if text.count(IMAGE_SRC) != 1:
            errors.append(
                f"native ad image count is not 1: {path.relative_to(ROOT)}"
            )
        if "/ask/gpt/?topic=" not in text or "source=article-inline-ad-" not in text:
            errors.append(f"native ad destination missing: {path.relative_to(ROOT)}")
        expected_topic = page_topic(text, path)
        if f'/ask/gpt/?topic={expected_topic}&amp;source=article-inline-ad-' not in text:
            errors.append(
                f"native ad topic mismatch: {path.relative_to(ROOT)} "
                f"(expected {expected_topic})"
            )
        if re.search(r'"image"\s*:\s*\[[^\]]*/images/', text):
            errors.append(f"legacy article schema images: {path.relative_to(ROOT)}")
    if not (ROOT / IMAGE_SRC.lstrip("/")).exists():
        errors.append(f"shared native ad asset missing: {IMAGE_SRC}")
    print(f"article native ad audit: {article_count} article pages, {len(errors)} errors")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("preview", "migrate", "audit"))
    args = parser.parse_args()
    if args.command == "preview":
        migrate(write=False)
        return 0
    if args.command == "migrate":
        migrate(write=True)
        return 0
    return audit()


if __name__ == "__main__":
    raise SystemExit(main())
