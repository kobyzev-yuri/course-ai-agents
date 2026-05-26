# Финальная защита: Chip News Impact Engine

## Задача
Запустить систему по `NVDA`, `SNDK`, `MU` и показать ranked report новостей с direction, strength, horizon, confidence и evidence.

## Обязательные команды

```bash
python -m news_impact.cli --news data/sample_news.jsonl --format markdown
python -m news_impact.cli --news data/sample_news.jsonl --format jsonl
python -m unittest discover -s tests
python evals/run_eval.py
```

## Что показать на защите
- Один `up/strong` пример и evidence.
- Один `down/strong` пример и evidence.
- Один спорный или low-confidence пример.
- Где в архитектуре нужен human review.
- Почему это news intelligence, а не trading recommendation.
- Как `agy` помогал строить или проверять систему.
- Где LangGraph полезнее простого script pipeline.
- Где CrewAI reviewer crew полезнее одного LLM prompt.

## Rubric: 100 баллов
- Product boundary and financial safety: 15.
- Data schema and labels: 15.
- Ingestion, dedup, mapping: 15.
- Impact and horizon scoring: 15.
- LangGraph architecture and reliability: 15.
- CrewAI review and skeptic checks: 10.
- Evals, tests, reproducibility: 15.

## Non-advice disclaimer
Система используется только для обучения архитектуре AI-агентов и финансовой news intelligence. Она не является инвестиционной рекомендацией, торговым сигналом или заменой профессионального анализа.
