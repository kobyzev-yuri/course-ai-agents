from __future__ import annotations

from pathlib import Path

from .dedup import cluster_stories
from .ingestion import filter_articles_for_tickers, load_jsonl
from .schema import ImpactAssessment
from .scoring import assess_story

DEFAULT_TICKERS = ["NVDA", "SNDK", "MU"]


def run_pipeline(news_path: str | Path, tickers: list[str] | None = None) -> list[ImpactAssessment]:
    selected = tickers or DEFAULT_TICKERS
    articles = load_jsonl(news_path)
    relevant = filter_articles_for_tickers(articles, selected)
    stories = cluster_stories(relevant)
    results: list[ImpactAssessment] = []
    for story in stories:
        results.extend(assessment for assessment in assess_story(story) if assessment.ticker in selected)
    return sorted(results, key=lambda item: (item.confidence, item.impact_strength == "strong"), reverse=True)
