from __future__ import annotations

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from news_impact.schema import ImpactAssessment


class SchemaTests(unittest.TestCase):
    def test_assessment_validates_labels(self):
        item = ImpactAssessment(
            ticker="NVDA",
            company="NVIDIA",
            story_id="s1",
            news_title="NVIDIA beats guidance",
            source="Example",
            event_type="earnings",
            impact_direction="up",
            impact_strength="strong",
            horizon="1w",
            confidence=0.8,
            evidence=["Example: NVIDIA beats guidance"],
            why_it_matters="Earnings surprise changes near-term expectations.",
        )
        self.assertEqual(item.to_dict()["ticker"], "NVDA")

    def test_invalid_ticker_fails(self):
        item = ImpactAssessment(
            ticker="ABC",
            company="Bad",
            story_id="s1",
            news_title="Bad",
            source="Example",
            event_type="other",
            impact_direction="neutral",
            impact_strength="weak",
            horizon="3w",
            confidence=0.5,
            evidence=["x"],
            why_it_matters="x",
        )
        with self.assertRaises(ValueError):
            item.validate()


if __name__ == "__main__":
    unittest.main()
