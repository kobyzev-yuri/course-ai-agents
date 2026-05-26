from __future__ import annotations

import re
from collections import defaultdict

from .mapping import map_story_tickers
from .schema import Article, Story

_STOPWORDS = {"the", "a", "an", "to", "of", "and", "for", "on", "in", "with", "as", "after"}


def normalize_title(title: str) -> str:
    words = re.findall(r"[a-z0-9]+", title.lower())
    return " ".join(word for word in words if word not in _STOPWORDS)


def story_key(article: Article) -> str:
    normalized = normalize_title(article.title)
    return "-".join(normalized.split()[:8]) or article.id


def cluster_stories(articles: list[Article]) -> list[Story]:
    groups: dict[str, list[Article]] = defaultdict(list)
    for article in articles:
        groups[story_key(article)].append(article)

    stories: list[Story] = []
    for key, grouped in groups.items():
        canonical = grouped[0].title
        tickers = sorted(map_story_tickers(grouped))
        stories.append(Story(story_id=key, canonical_title=canonical, articles=grouped, tickers=tickers))
    return stories
