from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from tools import daily_brief


class DailyBriefTests(unittest.TestCase):
    def test_publication_count_deduplicates_language_pages(self) -> None:
        inventory = [
            {
                "story": "/articles/example",
                "path": "/articles/example.html",
                "url": "https://example.com/articles/example.html",
                "title": "繁体文章",
                "language": "zh-Hant",
                "topic": "hk-inheritance",
                "datePublished": "2026-07-22",
                "dateModified": "2026-07-22",
            },
            {
                "story": "/articles/example",
                "path": "/articles/example_en.html",
                "url": "https://example.com/articles/example_en.html",
                "title": "English article",
                "language": "en",
                "topic": "hk-inheritance",
                "datePublished": "2026-07-22",
                "dateModified": "2026-07-22",
            },
        ]
        summary = daily_brief.summarise_publications(
            inventory,
            {},
            date(2026, 7, 22),
            [],
        )
        self.assertEqual(summary["newArticleCount"], 1)
        self.assertEqual(summary["newLanguagePageCount"], 2)
        self.assertEqual(summary["indexUnknown"], 1)

    def test_index_state_requires_a_known_inspection(self) -> None:
        pages = [{"url": "https://example.com/a"}]
        self.assertEqual(daily_brief.story_index_status(pages, {}), "unknown")
        self.assertEqual(
            daily_brief.story_index_status(
                pages,
                {"https://example.com/a": {"verdict": "PASS", "coverageState": "Submitted and indexed"}},
            ),
            "indexed",
        )

    def test_next_directions_are_capped_at_thirty(self) -> None:
        decisions = [
            {
                "id": f"T-{index}",
                "systemStatus": "recommended",
                "score": 70,
                "topic": "hk-inheritance",
                "clusterId": "hk-entry-process",
                "personaLabel": "香港家属协调人",
                "primaryQuery": f"问题 {index}",
                "title": f"题目 {index}",
                "reason": "通过",
            }
            for index in range(40)
        ]
        summary = daily_brief.next_directions({"decisions": decisions}, limit=30)
        self.assertEqual(summary["available"], 30)
        self.assertEqual(summary["gap"], 0)

    def test_publication_log_merges_language_pages_for_one_story(self) -> None:
        with TemporaryDirectory() as folder:
            log_path = Path(folder) / "publication-log.json"
            with patch.object(daily_brief, "PUBLICATION_LOG_PATH", log_path):
                daily_brief.record_publication(
                    "/articles/example",
                    "Example",
                    ["https://example.com/articles/example.html"],
                    ["zh-Hant"],
                    "hk-inheritance",
                    "2026-07-22T12:00:00+08:00",
                )
                daily_brief.record_publication(
                    "/articles/example",
                    "Example",
                    ["https://example.com/articles/example_en.html"],
                    ["en"],
                    "hk-inheritance",
                    "2026-07-22T12:05:00+08:00",
                )
            payload = daily_brief.read_json(log_path, {})
            self.assertEqual(len(payload["events"]), 1)
            self.assertEqual(len(payload["events"][0]["urls"]), 2)


if __name__ == "__main__":
    unittest.main()
