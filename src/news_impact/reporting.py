from __future__ import annotations

import json
from .schema import ImpactAssessment


def to_jsonl(items: list[ImpactAssessment]) -> str:
    return "\n".join(json.dumps(item.to_dict(), ensure_ascii=False) for item in items)


def to_markdown(items: list[ImpactAssessment]) -> str:
    lines = ["# Chip News Impact Report", "", "Not investment advice. Educational news-intelligence output.", ""]
    for item in items:
        lines.append(f"## {item.ticker}: {item.impact_direction}/{item.impact_strength} over {item.horizon}")
        lines.append(f"- News: {item.news_title}")
        lines.append(f"- Event: {item.event_type}")
        lines.append(f"- Confidence: {item.confidence}")
        lines.append(f"- Why it matters: {item.why_it_matters}")
        lines.append("- Evidence:")
        for evidence in item.evidence:
            lines.append(f"  - {evidence}")
        if item.risks_to_call:
            lines.append("- Risks:")
            for risk in item.risks_to_call:
                lines.append(f"  - {risk}")
        lines.append("")
    return "\n".join(lines)
