from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AskNavigationTests(unittest.TestCase):
    def test_topic_link_opens_article_hub(self) -> None:
        for path in (ROOT / "ask" / "index.html", ROOT / "ask" / "gpt" / "index.html"):
            text = path.read_text(encoding="utf-8")
            links = re.findall(r'<a class="home-link" href="([^"]+)"[^>]*>([^<]+)</a>', text)
            self.assertEqual([("/articles/", "专题")], links, str(path.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main()
