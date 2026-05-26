from __future__ import annotations

from .schema import ImpactAssessment


def deterministic_reviewer(items: list[ImpactAssessment]) -> list[dict]:
    reviews = []
    for item in items:
        flags = []
        if item.confidence < 0.7:
            flags.append("confidence_below_review_threshold")
        if item.impact_strength == "strong" and len(item.evidence) < 2:
            flags.append("strong_call_needs_more_evidence")
        if item.impact_direction == "neutral" and item.impact_strength == "strong":
            flags.append("neutral_strong_is_unusual")
        reviews.append({
            "ticker": item.ticker,
            "story_id": item.story_id,
            "review_status": "needs_review" if flags else "accepted_for_training_report",
            "flags": flags,
        })
    return reviews


def crewai_review_or_fallback(items: list[ImpactAssessment]) -> list[dict]:
    """Use CrewAI in the lesson if installed; keep the repo runnable without it."""
    try:
        import crewai  # noqa: F401
    except Exception:
        return deterministic_reviewer(items)
    # The actual Crew construction is deliberately a lesson exercise. The fallback
    # keeps tests deterministic and shows the expected review contract.
    return deterministic_reviewer(items)
