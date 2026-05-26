# Examples

Старые игрушечные примеры удалены. Рабочий пример теперь сам проект:

```bash
python -m news_impact.cli --news data/sample_news.jsonl --format markdown
python -m news_impact.cli --news data/sample_news.jsonl --format jsonl
python evals/run_eval.py
```

Optional agent layers:

- `src/news_impact/langgraph_pipeline.py` показывает, как завернуть pipeline в LangGraph StateGraph.
- `src/news_impact/crewai_review.py` задает contract для CrewAI reviewer crew и deterministic fallback.
