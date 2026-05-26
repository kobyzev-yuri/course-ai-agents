from __future__ import annotations

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from news_impact.pipeline import run_pipeline


class PipelineTests(unittest.TestCase):
    def test_pipeline_returns_chip_tickers(self):
        root = Path(__file__).resolve().parents[1]
        results = run_pipeline(root / "data/sample_news.jsonl")
        tickers = {item.ticker for item in results}
        self.assertTrue({"NVDA", "MU", "SNDK"}.issubset(tickers))

    def test_export_controls_score_down_strong(self):
        root = Path(__file__).resolve().parents[1]
        results = run_pipeline(root / "data/sample_news.jsonl", ["NVDA"])
        export = [item for item in results if "export" in item.news_title.lower()][0]
        self.assertEqual(export.impact_direction, "down")
        self.assertEqual(export.impact_strength, "strong")
        self.assertEqual(export.horizon, "1w")


if __name__ == "__main__":
    unittest.main()
