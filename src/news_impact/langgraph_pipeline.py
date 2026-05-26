from __future__ import annotations

from typing import TypedDict

from .dedup import cluster_stories
from .ingestion import filter_articles_for_tickers, load_jsonl
from .pipeline import DEFAULT_TICKERS, run_pipeline
from .scoring import assess_story


class NewsImpactState(TypedDict):
    news_path: str
    tickers: list[str]
    articles: list[object]
    stories: list[object]
    assessments: list[object]
    needs_human_review: bool


def build_langgraph_pipeline():
    """Build the optional LangGraph runtime, with a deterministic fallback for unavailable deps."""
    try:
        from langgraph.graph import END, START, StateGraph
    except Exception:
        return None

    def ingest(state: NewsImpactState) -> dict:
        articles = filter_articles_for_tickers(load_jsonl(state["news_path"]), state.get("tickers") or DEFAULT_TICKERS)
        return {"articles": articles}

    def dedup(state: NewsImpactState) -> dict:
        return {"stories": cluster_stories(state["articles"])}

    def score(state: NewsImpactState) -> dict:
        assessments = []
        for story in state["stories"]:
            assessments.extend(assess_story(story))
        needs_review = any(item.confidence < 0.7 and item.impact_strength == "strong" for item in assessments)
        return {"assessments": assessments, "needs_human_review": needs_review}

    builder = StateGraph(NewsImpactState)
    builder.add_node("ingest", ingest)
    builder.add_node("dedup", dedup)
    builder.add_node("score", score)
    builder.add_edge(START, "ingest")
    builder.add_edge("ingest", "dedup")
    builder.add_edge("dedup", "score")
    builder.add_edge("score", END)
    return builder.compile()


def run_langgraph_or_fallback(news_path: str, tickers: list[str] | None = None):
    app = build_langgraph_pipeline()
    selected = tickers or DEFAULT_TICKERS
    if app is None:
        return run_pipeline(news_path, selected)
    state = app.invoke({"news_path": news_path, "tickers": selected, "articles": [], "stories": [], "assessments": [], "needs_human_review": False})
    return state["assessments"]
