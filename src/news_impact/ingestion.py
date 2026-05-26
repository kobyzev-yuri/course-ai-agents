from __future__ import annotations

import json
from pathlib import Path

from .schema import Article


def load_jsonl(path: str | Path) -> list[Article]:
    articles: list[Article] = []
    with Path(path).open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            articles.append(Article(**row))
    return articles


def filter_articles_for_tickers(articles: list[Article], tickers: list[str]) -> list[Article]:
    aliases = {
        "NVDA": ["nvda", "nvidia", "gpu", "blackwell", "cuda"],
        "MU": ["mu", "micron", "dram", "hbm", "memory"],
        "SNDK": ["sndk", "sandisk", "nand", "flash storage", "ssd"],
    }
    needles = [needle for ticker in tickers for needle in aliases.get(ticker, [ticker.lower()])]
    return [article for article in articles if any(needle in article.text().lower() for needle in needles)]
