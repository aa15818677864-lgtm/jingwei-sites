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

    def test_launch_twenty_have_three_complete_language_pages(self) -> None:
        topic = ARTICLES / "hk-mainland-property-inheritance"
        for slug in NEW_SLUGS:
            for suffix in ("", "_cn", "_en"):
                path = topic / f"{slug}{suffix}.html"
                self.assertTrue(path.exists(), str(path.relative_to(ROOT)))
                text = path.read_text(encoding="utf-8")
                self.assertEqual(3, len(re.findall(r"<figure\b", text)), str(path.relative_to(ROOT)))
                self.assertEqual(1, text.count('class="article-last-updated"'), str(path.relative_to(ROOT)))
                self.assertIn('hreflang="zh-Hant"', text)
                self.assertIn('hreflang="zh-Hans"', text)
                self.assertIn('hreflang="en"', text)
                self.assertIn('hreflang="x-default"', text)

    def test_public_brand_and_article_count(self) -> None:
        indexes = [ARTICLES / "index.html", ARTICLES / "index_cn.html", ARTICLES / "index_en.html"]
        expected = ["28 篇已發佈", "28 篇已发布", "28 articles"]
        for path, label in zip(indexes, expected):
            text = path.read_text(encoding="utf-8")
            self.assertIn(label, text)
            self.assertNotIn("228", text)
        dashboard = (ROOT / "dashboard" / "index.html").read_text(encoding="utf-8")
        self.assertIn("Liu Yi Lawyer Team", dashboard)
        self.assertNotIn("Jingwei Content Operations", dashboard)
        public_text = dashboard + "\n" + "\n".join(path.read_text(encoding="utf-8") for path in html_files())
        self.assertNotIn("静为", public_text)
        self.assertNotRegex(public_text, r"中华人民共和国|中華人民共和國|gov\.cn")


if __name__ == "__main__":
    unittest.main()
