from __future__ import annotations

import unittest

from tools import article_ops


class ArticleOpsTests(unittest.TestCase):
    def test_not_indexed_is_not_counted_as_indexed(self) -> None:
        indexed, explicit_nonindex, label = article_ops.index_state(
            {"verdict": "NEUTRAL", "coverageState": "已发现 - 尚未编入索引"}
        )
        self.assertFalse(indexed)
        self.assertTrue(explicit_nonindex)
        self.assertEqual(label, "已发现 - 尚未编入索引")

    def test_unknown_inspection_stays_unknown(self) -> None:
        indexed, explicit_nonindex, label = article_ops.index_state({})
        self.assertFalse(indexed)
        self.assertFalse(explicit_nonindex)
        self.assertEqual(label, "unknown")

    def test_english_not_on_google_is_explicit_nonindex(self) -> None:
        indexed, explicit_nonindex, _ = article_ops.index_state(
            {"coverageState": "URL is not on Google"}
        )
        self.assertFalse(indexed)
        self.assertTrue(explicit_nonindex)

    def test_pass_is_counted_as_indexed(self) -> None:
        indexed, explicit_nonindex, label = article_ops.index_state(
            {"verdict": "PASS", "coverageState": "Submitted and indexed"}
        )
        self.assertTrue(indexed)
        self.assertFalse(explicit_nonindex)
        self.assertEqual(label, "Submitted and indexed")


if __name__ == "__main__":
    unittest.main()
