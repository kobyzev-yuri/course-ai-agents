from __future__ import annotations

from .schema import Article

ALIASES = {
    "NVDA": ["nvidia", "nvda", "blackwell", "gpu", "cuda", "ai accelerator"],
    "MU": ["micron", "mu", "dram", "hbm", "memory pricing"],
    "SNDK": ["sandisk", "sndk", "nand", "flash storage", "ssd"],
}
COMPANY_NAMES = {"NVDA": "NVIDIA", "MU": "Micron", "SNDK": "SanDisk"}
SECTOR_READ_THROUGH = {
    "hbm": {"NVDA", "MU"},
    "dram": {"MU"},
    "nand": {"SNDK", "MU"},
    "gpu": {"NVDA"},
    "export controls": {"NVDA"},
    "memory pricing": {"MU", "SNDK"},
}


def map_article_tickers(article: Article) -> set[str]:
    text = article.text().lower()
    tickers: set[str] = set()
    for ticker, aliases in ALIASES.items():
        if any(alias in text for alias in aliases):
            tickers.add(ticker)
    for phrase, mapped in SECTOR_READ_THROUGH.items():
        if phrase in text:
            tickers.update(mapped)
    return tickers


def map_story_tickers(articles: list[Article]) -> set[str]:
    tickers: set[str] = set()
    for article in articles:
        tickers.update(map_article_tickers(article))
    return tickers
