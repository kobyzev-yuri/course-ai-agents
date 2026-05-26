from __future__ import annotations

from .mapping import COMPANY_NAMES
from .schema import ImpactAssessment, Story

NEGATIVE = ["ban", "restrict", "cut", "delay", "probe", "lawsuit", "miss", "weak", "shortage"]
POSITIVE = ["beat", "raise", "surge", "wins", "order", "approval", "launch", "demand", "pricing power"]
STRONG = ["earnings", "guidance", "export", "ban", "major", "hyperscaler", "supply", "hbm", "pricing power"]


def classify_event(text: str) -> str:
    lowered = text.lower()
    if any(k in lowered for k in ["earnings", "guidance", "revenue", "margin"]):
        return "earnings"
    if any(k in lowered for k in ["export", "ban", "restriction", "license"]):
        return "export_control"
    if any(k in lowered for k in ["supply", "shortage", "capacity", "foundry"]):
        return "supply_chain"
    if any(k in lowered for k in ["capex", "data center spending", "ai infrastructure"]):
        return "capex"
    if any(k in lowered for k in ["launch", "product", "blackwell", "hbm", "ssd"]):
        return "product"
    if any(k in lowered for k in ["customer", "hyperscaler", "order", "contract"]):
        return "customer"
    if any(k in lowered for k in ["competitor", "amd", "intel", "samsung"]):
        return "competitor"
    if any(k in lowered for k in ["fed", "rates", "inflation", "macro"]):
        return "macro"
    if any(k in lowered for k in ["lawsuit", "probe", "regulator", "legal"]):
        return "legal"
    if any(k in lowered for k in ["price", "pricing", "spot"]):
        return "pricing"
    return "other"


def score_direction(text: str) -> str:
    lowered = text.lower()
    negative_hits = sum(1 for k in NEGATIVE if k in lowered)
    positive_hits = sum(1 for k in POSITIVE if k in lowered)
    if positive_hits > negative_hits:
        return "up"
    if negative_hits > positive_hits:
        return "down"
    return "neutral"


def score_strength(text: str) -> str:
    lowered = text.lower()
    return "strong" if any(k in lowered for k in STRONG) else "weak"


def score_horizon(event_type: str, text: str) -> str:
    lowered = text.lower()
    if event_type in {"earnings", "export_control", "legal"}:
        return "1w"
    if event_type in {"customer", "competitor", "product"}:
        return "3w"
    if event_type in {"supply_chain", "pricing"} or "cycle" in lowered:
        return "5w"
    if event_type in {"capex", "macro"}:
        return "1m"
    return "3w"


def confidence_for(story: Story, direction: str, strength: str) -> float:
    base = 0.48
    if len(story.articles) > 1:
        base += 0.12
    if direction != "neutral":
        base += 0.12
    if strength == "strong":
        base += 0.10
    if story.tickers:
        base += 0.10
    return min(round(base, 2), 0.92)


def assess_story(story: Story) -> list[ImpactAssessment]:
    text = f"{story.canonical_title}. " + " ".join(a.summary for a in story.articles)
    event_type = classify_event(text)
    direction = score_direction(text)
    strength = score_strength(text)
    horizon = score_horizon(event_type, text)
    confidence = confidence_for(story, direction, strength)
    assessments: list[ImpactAssessment] = []
    for ticker in story.tickers:
        why = (
            f"{COMPANY_NAMES[ticker]} is linked to a {event_type} story. "
            f"The rule-based scorer labels the likely news impulse as {direction}/{strength} over {horizon}."
        )
        risks = []
        if confidence < 0.7:
            risks.append("Low confidence: send to human review before using in a market note.")
        if direction == "neutral":
            risks.append("Direction is ambiguous; check price action and analyst revisions.")
        assessments.append(
            ImpactAssessment(
                ticker=ticker,
                company=COMPANY_NAMES[ticker],
                story_id=story.story_id,
                news_title=story.canonical_title,
                source=story.articles[0].source,
                event_type=event_type,
                impact_direction=direction,
                impact_strength=strength,
                horizon=horizon,
                confidence=confidence,
                evidence=story.evidence,
                why_it_matters=why,
                risks_to_call=risks,
            )
        )
    return assessments
