from __future__ import annotations

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from news_impact.crewai_review import deterministic_reviewer
from news_impact.pipeline import run_pipeline


class ReviewTests(unittest.TestCase):
    def test_review_contract(self):
        root = Path(__file__).resolve().parents[1]
        reviews = deterministic_reviewer(run_pipeline(root / "data/sample_news.jsonl"))
        self.assertTrue(reviews)
        self.assertIn("review_status", reviews[0])


if __name__ == "__main__":
    unittest.main()
