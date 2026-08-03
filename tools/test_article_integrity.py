from __future__ import annotations

import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "articles"
SITE = "https://www.jingwei-law.com"
NEW_SLUGS = [
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
CORE_PROPERTY_SLUGS = [
    "ancestral-home-homestead",
    "dispute",
    "documents",
    "missing-documents",
    "tax-cost",
]
BATCH_20260803 = {
    "demolition-compensation": "hk-mainland-property-inheritance",
    "joint-or-nominee-bank-account": "hong-kong-other-estate",
    "securities-and-funds": "hong-kong-other-estate",
    "insurance-beneficiary-or-estate": "hong-kong-other-estate",
    "employer-and-unpaid-benefits": "hong-kong-other-estate",
    "vehicle-inheritance": "hong-kong-other-estate",
    "estate-debts-before-distribution": "hong-kong-other-estate",
    "funeral-and-management-expenses": "hong-kong-other-estate",
    "property-sold-before-settlement": "hk-mainland-property-inheritance",
    "family-settlement-writing": "hong-kong-other-estate",
}
CASE_BATCH_20260803 = {
    "minor-heir": "hong-kong-other-estate",
    "elderly-or-incapable-heir": "hong-kong-other-estate",
    "remarriage-and-stepfamily": "hong-kong-other-estate",
    "adoption-and-family-records": "hong-kong-other-estate",
    "predeceased-heir": "hong-kong-other-estate",
    "multiple-deaths-in-one-family": "hong-kong-other-estate",
    "preserve-evidence-before-dispute": "hong-kong-other-estate",
    "small-deposit-multiple-products": "hong-kong-other-estate",
    "loan-receivable-after-death": "hong-kong-other-estate",
    "company-property-vs-shareholder-estate": "hong-kong-other-estate",
}
ROUND1_20260804 = {
    "first-family-meeting-agenda": "hong-kong-other-estate",
    "reconstruct-estate-income-and-withdrawals": "hong-kong-other-estate",
}
ROUND2_20260804 = {
    "different-institutions-different-files": "hong-kong-other-estate",
    "hong-kong-and-mainland-workstreams": "hong-kong-other-estate",
}
ROUND3_20260804 = {
    "individual-business-after-operator-death": "hong-kong-other-estate",
    "partnership-interest-after-partner-death": "hong-kong-other-estate",
}
BATCH_PROPERTY_SLUGS = [
    slug for slug, folder in BATCH_20260803.items() if folder == "hk-mainland-property-inheritance"
]
PROPERTY_SLUGS = sorted(set(NEW_SLUGS + CORE_PROPERTY_SLUGS + BATCH_PROPERTY_SLUGS))


def html_files() -> list[Path]:
    return sorted(ARTICLES.rglob("*.html"))


def local_target(value: str) -> Path | None:
    if not value or value.startswith(("#", "mailto:", "tel:", "javascript:")):
        return None
    parts = urlsplit(value)
    if parts.scheme and parts.netloc not in {"www.jingwei-law.com", "jingwei-law.com"}:
        return None
    path = unquote(parts.path)
    if not path.startswith("/"):
        return None
    candidate = ROOT / path.lstrip("/")
    if path.endswith("/"):
        candidate /= "index.html"
    return candidate


class ArticleIntegrityTests(unittest.TestCase):
    def test_sitemap_and_json_ld_are_valid(self) -> None:
        ET.parse(ROOT / "sitemap.xml")
        for path in html_files():
            text = path.read_text(encoding="utf-8")
            blocks = re.findall(
                r'<script\s+type="application/ld\+json">(.*?)</script>',
                text,
                flags=re.S,
            )
            for block in blocks:
                try:
                    json.loads(block)
                except json.JSONDecodeError as error:
                    self.fail(f"Invalid JSON-LD in {path.relative_to(ROOT)}: {error}")

    def test_same_site_links_and_images_exist(self) -> None:
        missing = []
        for path in html_files():
            text = path.read_text(encoding="utf-8")
            for attr, value in re.findall(r'\b(href|src)="([^"]+)"', text):
                target = local_target(value)
                if target is not None and not target.exists():
                    missing.append(f"{path.relative_to(ROOT)} {attr}={value}")
        self.assertEqual([], missing, "Missing same-site references:\n" + "\n".join(missing[:30]))

    def test_launch_twenty_have_complete_language_pages_and_one_native_ad(self) -> None:
        topic = ARTICLES / "hk-mainland-property-inheritance"
        for slug in NEW_SLUGS:
            for suffix in ("", "_cn", "_en"):
                path = topic / f"{slug}{suffix}.html"
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                self.assertEqual(0, len(re.findall(r"<figure\b", text)), str(path.relative_to(ROOT)))
                self.assertEqual(1, text.count('class="article-native-ad"'), str(path.relative_to(ROOT)))
                self.assertIn('/articles/assets/ai-legal-assistant-native-ad-v2.webp', text)
                self.assertIn('/ask/gpt/?topic=', text)
                self.assertIn('source=article-inline-ad-', text)
                self.assertEqual(1, text.count('class="article-last-updated"'), str(path.relative_to(ROOT)))
                self.assertIn('hreflang="zh-Hant"', text)
                self.assertIn('hreflang="zh-Hans"', text)
                self.assertIn('hreflang="en"', text)
                self.assertIn('hreflang="x-default"', text)

    def test_20260803_batch_has_complete_language_pages_and_metadata(self) -> None:
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        for slug, folder in BATCH_20260803.items():
            for suffix, language in (("", "zh-Hant"), ("_cn", "zh-Hans"), ("_en", "en")):
                path = ARTICLES / folder / f"{slug}{suffix}.html"
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                public_path = f"/articles/{folder}/{slug}{suffix}.html"
                self.assertIn(f'<html lang="{language}">', text)
                self.assertEqual(0, len(re.findall(r"<figure\b", text)), str(path.relative_to(ROOT)))
                self.assertEqual(1, text.count('class="article-native-ad"'), str(path.relative_to(ROOT)))
                self.assertEqual(1, text.count('/articles/assets/ai-legal-assistant-native-ad-v2.webp'))
                self.assertIn(f'<link rel="canonical" href="{SITE}{public_path}">', text)
                self.assertIn('"@type": "Article"', text)
                self.assertIn('"datePublished": "2026-08-03"', text)
                self.assertIn('"dateModified": "2026-08-03"', text)
                self.assertIn(public_path, sitemap)
                self.assertGreaterEqual(text.count("article-prose-section"), 5)
                self.assertGreaterEqual(text.count('<a href="/articles/'), 6)

    def test_20260803_case_batch_has_case_structure_and_complete_metadata(self) -> None:
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        titles = set()
        for slug, folder in CASE_BATCH_20260803.items():
            for suffix, language in (("", "zh-Hant"), ("_cn", "zh-Hans"), ("_en", "en")):
                path = ARTICLES / folder / f"{slug}{suffix}.html"
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                public_path = f"/articles/{folder}/{slug}{suffix}.html"
                self.assertIn(f'<html lang="{language}">', text)
                self.assertEqual(1, text.count('class="article-native-ad"'))
                self.assertEqual(1, text.count('/articles/assets/ai-legal-assistant-native-ad-v2.webp'))
                self.assertEqual(1, text.count('class="hk-section-card article-prose-section case-file-card"'))
                self.assertGreaterEqual(text.count("article-prose-section"), 7)
                self.assertGreaterEqual(text.count("<p>"), 14)
                self.assertGreaterEqual(text.count('<a href="/articles/'), 6)
                self.assertIn(f'<link rel="canonical" href="{SITE}{public_path}">', text)
                self.assertIn('hreflang="zh-Hant"', text)
                self.assertIn('hreflang="zh-Hans"', text)
                self.assertIn('hreflang="en"', text)
                self.assertIn('hreflang="x-default"', text)
                self.assertIn('"@type": "Article"', text)
                self.assertIn('"datePublished": "2026-08-03"', text)
                self.assertIn('"dateModified": "2026-08-03"', text)
                self.assertIn(public_path, sitemap)
                self.assertNotRegex(text, r'<a[^>]+href="https?://')
                title = re.search(r"<h1>(.*?)</h1>", text, flags=re.S)
                self.assertIsNotNone(title)
                heading = re.sub(r"<[^>]+>", "", title.group(1)).strip()
                self.assertNotIn(heading, titles)
                titles.add(heading)

    def test_20260804_round1_has_answer_first_case_structure_and_metadata(self) -> None:
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        for slug, folder in ROUND1_20260804.items():
            for suffix, language in (("", "zh-Hant"), ("_cn", "zh-Hans"), ("_en", "en")):
                path = ARTICLES / folder / f"{slug}{suffix}.html"
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                public_path = f"/articles/{folder}/{slug}{suffix}.html"
                self.assertIn(f'<html lang="{language}">', text)
                self.assertLess(text.index('id="answer"'), text.index('id="case"'))
                self.assertEqual(1, text.count('class="article-native-ad"'))
                self.assertEqual(1, text.count('/articles/assets/ai-legal-assistant-native-ad-v2.webp'))
                self.assertEqual(1, text.count('class="hk-section-card article-prose-section case-file-card"'))
                self.assertGreaterEqual(text.count("article-prose-section"), 9)
                self.assertGreaterEqual(text.count("<p>"), 17)
                self.assertGreaterEqual(text.count('<a href="/articles/'), 7)
                self.assertIn(f'<link rel="canonical" href="{SITE}{public_path}">', text)
                self.assertIn('hreflang="zh-Hant"', text)
                self.assertIn('hreflang="zh-Hans"', text)
                self.assertIn('hreflang="en"', text)
                self.assertIn('hreflang="x-default"', text)
                self.assertIn('"@type": "Article"', text)
                self.assertIn('"datePublished": "2026-08-04"', text)
                self.assertIn('"dateModified": "2026-08-04"', text)
                self.assertIn(public_path, sitemap)
                self.assertNotRegex(text, r'<a[^>]+href="https?://')
        for filename in ("index.html", "index_cn.html", "index_en.html"):
            index = (ARTICLES / filename).read_text(encoding="utf-8")
            for slug in ROUND1_20260804:
                self.assertIn(f"/{slug}", index)

    def test_20260804_round2_has_answer_first_case_structure_and_metadata(self) -> None:
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        for slug, folder in ROUND2_20260804.items():
            for suffix, language in (("", "zh-Hant"), ("_cn", "zh-Hans"), ("_en", "en")):
                path = ARTICLES / folder / f"{slug}{suffix}.html"
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                public_path = f"/articles/{folder}/{slug}{suffix}.html"
                self.assertIn(f'<html lang="{language}">', text)
                self.assertLess(text.index('id="answer"'), text.index('id="case"'))
                self.assertEqual(1, text.count('class="article-native-ad"'))
                self.assertEqual(1, text.count('/articles/assets/ai-legal-assistant-native-ad-v2.webp'))
                self.assertEqual(1, text.count('class="hk-section-card article-prose-section case-file-card"'))
                self.assertGreaterEqual(text.count("article-prose-section"), 9)
                self.assertGreaterEqual(text.count("<p>"), 17)
                self.assertGreaterEqual(text.count('<a href="/articles/'), 7)
                self.assertIn(f'<link rel="canonical" href="{SITE}{public_path}">', text)
                self.assertIn('hreflang="zh-Hant"', text)
                self.assertIn('hreflang="zh-Hans"', text)
                self.assertIn('hreflang="en"', text)
                self.assertIn('hreflang="x-default"', text)
                self.assertIn('"@type": "Article"', text)
                self.assertIn('"datePublished": "2026-08-04"', text)
                self.assertIn('"dateModified": "2026-08-04"', text)
                self.assertIn(public_path, sitemap)
                self.assertNotRegex(text, r'<a[^>]+href="https?://')
        for filename in ("index.html", "index_cn.html", "index_en.html"):
            index = (ARTICLES / filename).read_text(encoding="utf-8")
            for slug in ROUND2_20260804:
                self.assertIn(f"/{slug}", index)

    def test_20260804_round3_has_answer_first_case_structure_and_metadata(self) -> None:
        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        for slug, folder in ROUND3_20260804.items():
            for suffix, language in (("", "zh-Hant"), ("_cn", "zh-Hans"), ("_en", "en")):
                path = ARTICLES / folder / f"{slug}{suffix}.html"
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                public_path = f"/articles/{folder}/{slug}{suffix}.html"
                self.assertIn(f'<html lang="{language}">', text)
                self.assertLess(text.index('id="answer"'), text.index('id="case"'))
                self.assertEqual(1, text.count('class="article-native-ad"'))
                self.assertEqual(1, text.count('/articles/assets/ai-legal-assistant-native-ad-v2.webp'))
                self.assertEqual(1, text.count('class="hk-section-card article-prose-section case-file-card"'))
                self.assertGreaterEqual(text.count("article-prose-section"), 9)
                self.assertGreaterEqual(text.count("<p>"), 17)
                self.assertGreaterEqual(text.count('<a href="/articles/'), 7)
                self.assertIn(f'<link rel="canonical" href="{SITE}{public_path}">', text)
                self.assertIn('hreflang="zh-Hant"', text)
                self.assertIn('hreflang="zh-Hans"', text)
                self.assertIn('hreflang="en"', text)
                self.assertIn('hreflang="x-default"', text)
                self.assertIn('"@type": "Article"', text)
                self.assertIn('"datePublished": "2026-08-04"', text)
                self.assertIn('"dateModified": "2026-08-04"', text)
                self.assertIn(public_path, sitemap)
                self.assertNotRegex(text, r'<a[^>]+href="https?://')
        for filename in ("index.html", "index_cn.html", "index_en.html"):
            index = (ARTICLES / filename).read_text(encoding="utf-8")
            for slug in ROUND3_20260804:
                self.assertIn(f"/{slug}", index)

    def test_every_article_has_exactly_one_internal_native_ad(self) -> None:
        checked = 0
        for path in html_files():
            text = path.read_text(encoding="utf-8")
            if 'data-article-redirect' in text:
                continue
            if 'property="og:type" content="article"' not in text:
                continue
            checked += 1
            self.assertNotIn('class="article-image-grid"', text, str(path.relative_to(ROOT)))
            self.assertEqual(1, text.count('class="article-native-ad"'), str(path.relative_to(ROOT)))
            self.assertEqual(
                1,
                text.count('/articles/assets/ai-legal-assistant-native-ad-v2.webp'),
                str(path.relative_to(ROOT)),
            )
            self.assertIn('source=article-inline-ad-', text)
            self.assertNotRegex(text, r'"image"\s*:\s*\[[^\]]*/images/')
        self.assertGreaterEqual(checked, 140)

    def test_public_brand_and_article_count(self) -> None:
        indexes = [ARTICLES / "index.html", ARTICLES / "index_cn.html", ARTICLES / "index_en.html"]
        for path in indexes:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("228", text)
            for slug in NEW_SLUGS:
                self.assertIn(f"/{slug}", text, f"{slug} missing from {path.name}")
            for slug in BATCH_20260803:
                self.assertIn(f"/{slug}", text, f"{slug} missing from {path.name}")
            for slug in CASE_BATCH_20260803:
                self.assertIn(f"/{slug}", text, f"{slug} missing from {path.name}")
        dashboard = (ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
        self.assertIn("Liu Yi Lawyer Team", dashboard)
        self.assertNotIn("Jingwei Content Operations", dashboard)
        public_text = dashboard + "\n" + "\n".join(path.read_text(encoding="utf-8") for path in html_files())
        self.assertNotIn("静为", public_text)
        self.assertNotRegex(public_text, r"中华人民共和国|中華人民共和國|gov\.cn")

    def test_dashboard_keeps_daily_operations_simple(self) -> None:
        dashboard = (ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
        script = (ROOT / "dashboard" / "script.js").read_text(encoding="utf-8")
        for required in ("运营概览", "已发布文章", "已确认收录", "待发布", "最近变化", "下一步", "文章状态", "详细数据"):
            self.assertIn(required, dashboard)
        for removed in ("四个固定客户角色", "动态选题分配", "本轮推荐选题", "收录反馈规则", "系统本轮学到什么", "咨询链路", "发布门槛"):
            self.assertNotIn(removed, dashboard)
        for required_id in ("activityChart", "queueRows", "articleRows", "topicDetail", "geoDetail", "sourceDetail"):
            self.assertIn(f'id="{required_id}"', dashboard)
            self.assertIn(f'byId("{required_id}")', script)
        self.assertIn('data-range="day"', dashboard)
        self.assertIn('data-range="month"', dashboard)
        self.assertIn('data-filter="unknown"', dashboard)
        self.assertIn('data-filter="issues"', dashboard)

    def test_article_indexes_keep_restored_design_and_human_copy(self) -> None:
        traditional = (ARTICLES / "index.html").read_text(encoding="utf-8")
        simplified = (ARTICLES / "index_cn.html").read_text(encoding="utf-8")
        english = (ARTICLES / "index_en.html").read_text(encoding="utf-8")
        self.assertIn('class="articles-index-v24"', traditional)
        self.assertIn('class="articles-index-v25"', simplified)
        self.assertIn('class="articles-index-v25 articles-index-en"', english)
        combined = "\n".join((traditional, simplified, english))
        for rejected in (
            "articles-hub-v26",
            "先按自己的情況找文章",
            "先找到你现在卡住的是哪一类继承问题",
            "新文章",
            "Suggested Order",
            "What This Group Helps You Clarify",
            "Organise Facts",
        ):
            self.assertNotIn(rejected, combined)

    def test_article_topic_navigation_is_consistent(self) -> None:
        topic_paths = (
            "/articles/macau/",
            "/articles/singapore/",
            "/articles/united-states/",
        )
        for path in html_files():
            text = path.read_text(encoding="utf-8")
            if 'class="nav-links"' not in text:
                continue
            for topic_path in topic_paths:
                self.assertIn(topic_path, text, f"{topic_path} missing from {path.relative_to(ROOT)}")
            self.assertNotIn('href="/">主站</a>', text, str(path.relative_to(ROOT)))
            self.assertNotIn('href="/">Main Site</a>', text, str(path.relative_to(ROOT)))
            self.assertNotIn(">說明情況</a>", text, str(path.relative_to(ROOT)))
            self.assertNotIn(">说明情况</a>", text, str(path.relative_to(ROOT)))

    def test_region_topic_hubs_have_three_languages_and_hreflang(self) -> None:
        for directory in ("macau", "singapore", "united-states"):
            variants = (
                ("index.html", 'class="articles-index-v24 topic-collection"', 'class="v24-article-more"'),
                ("index_cn.html", 'class="articles-index-v25 topic-collection"', 'class="v25-article-more"'),
                (
                    "index_en.html",
                    'class="articles-index-v25 articles-index-en topic-collection"',
                    'class="v25-article-more"',
                ),
            )
            for filename, body_class, more_class in variants:
                path = ARTICLES / directory / filename
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                self.assertIn(body_class, text)
                self.assertIn(more_class, text)
                self.assertNotIn('class="articles-hub-v26"', text)
                self.assertIn('hreflang="zh-Hant"', text)
                self.assertIn('hreflang="zh-Hans"', text)
                self.assertIn('hreflang="en"', text)
                self.assertIn('hreflang="x-default"', text)

    def test_hong_kong_index_uses_expandable_article_directory(self) -> None:
        traditional = (ARTICLES / "index.html").read_text(encoding="utf-8")
        simplified = (ARTICLES / "index_cn.html").read_text(encoding="utf-8")
        english = (ARTICLES / "index_en.html").read_text(encoding="utf-8")
        self.assertIn('class="v24-article-more"', traditional)
        self.assertIn('class="v25-article-more"', simplified)
        self.assertIn('class="v25-article-more"', english)
        for text in (traditional, simplified, english):
            self.assertIn("/articles/macau/", text)
            self.assertIn("/articles/singapore/", text)
            self.assertIn("/articles/united-states/", text)

    def test_hong_kong_property_hub_directory_stays_outside_fact_grid(self) -> None:
        topic = ARTICLES / "hk-mainland-property-inheritance"
        for filename in ("index.html", "index_cn.html", "index_en.html"):
            path = topic / filename
            text = path.read_text(encoding="utf-8")
            facts_start = text.index('<section id="facts"')
            facts_end = text.index("</section>", facts_start)
            directory_start = text.index("<!-- TOPIC_DIRECTORY_START -->")
            self.assertLess(facts_end, directory_start, str(path.relative_to(ROOT)))

    def test_hong_kong_property_topic_excludes_non_property_estate_articles(self) -> None:
        topic = ARTICLES / "hk-mainland-property-inheritance"
        indexes = [topic / "index.html", topic / "index_cn.html", topic / "index_en.html"]
        for path in indexes:
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("bank-deposits", text, str(path.relative_to(ROOT)))
            self.assertNotIn("social-security-housing-fund", text, str(path.relative_to(ROOT)))

        other_topic = ARTICLES / "hong-kong-other-estate"
        for filename in ("index.html", "index_cn.html", "index_en.html"):
            path = other_topic / filename
            self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
            text = path.read_text(encoding="utf-8")
            self.assertIn("bank-deposits", text)
            self.assertIn("social-security-housing-fund", text)

        for slug in ("bank-deposits", "social-security-housing-fund"):
            for suffix in ("", "_cn", "_en"):
                path = topic / f"{slug}{suffix}.html"
                text = path.read_text(encoding="utf-8")
                self.assertIn("data-article-redirect", text)
                self.assertIn('content="noindex,follow"', text)
                self.assertIn(f"/articles/hong-kong-other-estate/{slug}{suffix}.html", text)

    def test_hong_kong_property_articles_stay_on_property_intent(self) -> None:
        topic = ARTICLES / "hk-mainland-property-inheritance"
        rejected = (
            "銀行存款",
            "银行存款",
            "社保公積金",
            "社保公积金",
            "公司股權",
            "公司股权",
            "銀行線索",
            "银行线索",
            "bank account",
            "bank clues",
            "employment-related payments",
            "company interests",
            "property, banking",
        )
        for slug in PROPERTY_SLUGS:
            for suffix in ("", "_cn", "_en"):
                path = topic / f"{slug}{suffix}.html"
                text = path.read_text(encoding="utf-8")
                h1 = re.search(r"<h1>(.*?)</h1>", text, flags=re.S)
                self.assertIsNotNone(h1, str(path.relative_to(ROOT)))
                heading = re.sub(r"<[^>]+>", "", h1.group(1))
                if suffix == "_en":
                    self.assertRegex(heading.lower(), r"property|home|house")
                else:
                    self.assertRegex(heading, r"房|物業|物业")
                for phrase in rejected:
                    self.assertNotIn(phrase, text.lower(), f"{phrase} in {path.relative_to(ROOT)}")

    def test_hong_kong_property_visuals_do_not_use_generic_estate_labels(self) -> None:
        images = ARTICLES / "hk-mainland-property-inheritance" / "images"
        rejected = (
            "\u8cc7\u7522",
            "\u8d44\u4ea7",
            "\u9280\u884c",
            "\u94f6\u884c",
            "\u793e\u4fdd",
            "\u516c\u7a4d\u91d1",
            "\u516c\u79ef\u91d1",
            "\u80a1\u6b0a",
            "\u80a1\u6743",
            "mainland estate",
            "banking",
            ">assets<",
            " asset ",
            " assets ",
        )
        for path in images.rglob("*.svg"):
            text = path.read_text(encoding="utf-8").lower()
            for phrase in rejected:
                self.assertNotIn(phrase, text, f"{phrase} in {path.relative_to(ROOT)}")

    def test_hong_kong_property_navigation_and_sitemap_are_precise(self) -> None:
        labels = {
            "index.html": "香港房產繼承",
            "index_cn.html": "香港房产继承",
            "index_en.html": "HK Property Inheritance",
        }
        for filename, label in labels.items():
            text = (ARTICLES / filename).read_text(encoding="utf-8")
            self.assertIn(label, text)

        sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
        self.assertNotIn("/articles/hk-mainland-property-inheritance/bank-deposits", sitemap)
        self.assertNotIn("/articles/hk-mainland-property-inheritance/social-security-housing-fund", sitemap)
        self.assertIn("/articles/hong-kong-other-estate/", sitemap)
        self.assertIn("/articles/hong-kong-other-estate/bank-deposits", sitemap)
        self.assertIn("/articles/hong-kong-other-estate/social-security-housing-fund", sitemap)

    def test_launch_twenty_do_not_use_old_batch_template_labels(self) -> None:
        topic = ARTICLES / "hk-mainland-property-inheritance"
        rejected = (
            "這篇先回答",
            "这篇先回答",
            "先說結論",
            "先说结论",
            "進入專題初步問答",
            "进入专题初步问答",
            "Initial Q&A",
        )
        for slug in NEW_SLUGS:
            for suffix in ("", "_cn", "_en"):
                path = topic / f"{slug}{suffix}.html"
                text = path.read_text(encoding="utf-8")
                for phrase in rejected:
                    self.assertNotIn(phrase, text, f"{phrase} in {path.relative_to(ROOT)}")

    def test_hong_kong_articles_do_not_show_internal_ai_labels(self) -> None:
        topic = ARTICLES / "hk-mainland-property-inheritance"
        rejected = (
            "初步問答",
            "初步问答",
            "AI 初步",
            "Organise Facts",
            "Initial Q&A",
        )
        for path in topic.glob("*.html"):
            text = path.read_text(encoding="utf-8")
            for phrase in rejected:
                self.assertNotIn(phrase, text, f"{phrase} in {path.relative_to(ROOT)}")


if __name__ == "__main__":
    unittest.main()
