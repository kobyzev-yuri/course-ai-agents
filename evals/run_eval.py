from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from news_impact.pipeline import run_pipeline


def load_expected(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    results = [item.to_dict() for item in run_pipeline(root / "data/sample_news.jsonl")]
    expected = load_expected(root / "evals/expected_labels.jsonl")
    hits = 0
    misses = []
    for row in expected:
        match = next((item for item in results if row["ticker"] == item["ticker"] and row["story_contains"].lower() in item["news_title"].lower()), None)
        if match and match["impact_direction"] == row["impact_direction"] and match["impact_strength"] == row["impact_strength"]:
            hits += 1
        else:
            misses.append({"expected": row, "actual": match})
    score = hits / len(expected)
    print(json.dumps({"score": score, "hits": hits, "total": len(expected), "misses": misses}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if score >= 0.8 else 1)


if __name__ == "__main__":
    main()
