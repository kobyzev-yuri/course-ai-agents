from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Literal

Ticker = Literal["NVDA", "SNDK", "MU"]
EventType = Literal[
    "earnings",
    "export_control",
    "supply_chain",
    "capex",
    "product",
    "customer",
    "competitor",
    "macro",
    "legal",
    "pricing",
    "other",
]
ImpactDirection = Literal["up", "down", "neutral"]
ImpactStrength = Literal["weak", "strong"]
Horizon = Literal["1w", "3w", "5w", "1m"]

VALID_TICKERS = {"NVDA", "SNDK", "MU"}
VALID_EVENT_TYPES = {
    "earnings", "export_control", "supply_chain", "capex", "product",
    "customer", "competitor", "macro", "legal", "pricing", "other",
}
VALID_DIRECTIONS = {"up", "down", "neutral"}
VALID_STRENGTHS = {"weak", "strong"}
VALID_HORIZONS = {"1w", "3w", "5w", "1m"}


@dataclass(frozen=True)
class Article:
    id: str
    title: str
    source: str
    published_at: str
    url: str
    summary: str

    def text(self) -> str:
        return f"{self.title}. {self.summary}"


@dataclass(frozen=True)
class Story:
    story_id: str
    canonical_title: str
    articles: list[Article]
    tickers: list[str]

    @property
    def evidence(self) -> list[str]:
        return [f"{a.source}: {a.title}" for a in self.articles[:3]]


@dataclass(frozen=True)
class ImpactAssessment:
    ticker: str
    company: str
    story_id: str
    news_title: str
    source: str
    event_type: str
    impact_direction: str
    impact_strength: str
    horizon: str
    confidence: float
    evidence: list[str]
    why_it_matters: str
    risks_to_call: list[str] = field(default_factory=list)

    def validate(self) -> None:
        if self.ticker not in VALID_TICKERS:
            raise ValueError(f"unsupported ticker: {self.ticker}")
        if self.event_type not in VALID_EVENT_TYPES:
            raise ValueError(f"unsupported event_type: {self.event_type}")
        if self.impact_direction not in VALID_DIRECTIONS:
            raise ValueError(f"unsupported impact_direction: {self.impact_direction}")
        if self.impact_strength not in VALID_STRENGTHS:
            raise ValueError(f"unsupported impact_strength: {self.impact_strength}")
        if self.horizon not in VALID_HORIZONS:
            raise ValueError(f"unsupported horizon: {self.horizon}")
        if not 0 <= self.confidence <= 1:
            raise ValueError("confidence must be between 0 and 1")
        if not self.evidence:
            raise ValueError("at least one evidence item is required")

    def to_dict(self) -> dict:
        self.validate()
        return asdict(self)
