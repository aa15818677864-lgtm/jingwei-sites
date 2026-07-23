from __future__ import annotations

import unittest
from datetime import date

from tools import topic_engine


class TopicEngineTests(unittest.TestCase):
    def test_phrase_matching_handles_chinese_and_english_spacing(self) -> None:
        self.assertTrue(
            topic_engine.phrase_matches(
                "香港人繼承內地房產有什麽手續",
                ["香港人繼承內地房產"],
            )
        )
        self.assertTrue(
            topic_engine.phrase_matches(
                "Chinese litigation lawyer for a US client",
                ["chinese litigation lawyer"],
            )
        )
        self.assertFalse(topic_engine.phrase_matches("劉毅律師", ["內地房產繼承"]))

    def test_score_reaches_gate_for_a_distinct_evidenced_question(self) -> None:
        score, breakdown = topic_engine.score_candidate(
            {
                "personaId": "persona",
                "distinctValue": True,
                "evidenceSources": ["source-a", "source-b"],
                "primaryQuery": "香港人继承内地房产要办什么手续",
            },
            {"impressions": 0, "clicks": 0},
            {},
            0,
            2,
            False,
            False,
        )
        self.assertGreaterEqual(score, 65)
        self.assertEqual(breakdown["distinctValue"], 15)

    def test_long_explicit_nonindex_retires_only_when_technical_base_is_healthy(self) -> None:
        candidate = {
            "publishedUrl": "https://www.jingwei-law.com/articles/example.html",
            "improvements": 1,
        }
        status, _, _ = topic_engine.lifecycle_status(
            candidate,
            40,
            65,
            {"impressions": 0, "clicks": 0},
            {"verdict": "FAIL", "coverageState": "Crawled - currently not indexed"},
            {"datePublished": "2026-01-01", "indexable": True},
            True,
            0,
            75,
            46,
            today=date(2026, 7, 23),
        )
        self.assertEqual(status, "retired")

        technical_status, _, _ = topic_engine.lifecycle_status(
            candidate,
            40,
            65,
            {"impressions": 0, "clicks": 0},
            {"verdict": "FAIL", "coverageState": "Crawled - currently not indexed"},
            {"datePublished": "2026-01-01", "indexable": False},
            False,
            0,
            75,
            46,
            today=date(2026, 7, 23),
        )
        self.assertEqual(technical_status, "needs-technical-fix")

    def test_unknown_inspection_never_becomes_not_indexed(self) -> None:
        indexed, explicit_nonindex, label = topic_engine.index_state({})
        self.assertFalse(indexed)
        self.assertFalse(explicit_nonindex)
        self.assertEqual(label, "unknown")

    def test_similarity_blocks_keyword_variants_but_keeps_distinct_questions(self) -> None:
        self.assertGreater(
            topic_engine.text_similarity(
                "香港人继承内地房产要什么手续",
                "香港居民继承内地房产需要哪些手续",
            ),
            0.62,
        )
        self.assertLess(
            topic_engine.text_similarity(
                "香港人继承内地房产要什么手续",
                "家人失联时怎样先保存租金和房屋记录",
            ),
            0.30,
        )

    def test_candidate_already_in_writing_is_not_recommended_again(self) -> None:
        status, action, _ = topic_engine.lifecycle_status(
            {"publishedUrl": "", "status": "researching"},
            80,
            65,
            {},
            {},
            None,
            False,
            0,
            75,
            46,
            today=date(2026, 7, 23),
        )
        self.assertEqual(status, "in-production")
        self.assertEqual(action, "继续现有写作流程")


if __name__ == "__main__":
    unittest.main()
