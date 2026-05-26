# News Impact Agents: курс по агентным системам на реальном проекте

Это практический инженерный курс, в котором ученик строит **Chip News Impact Engine**: систему поиска и оценки новостей, влияющих на акции компаний-производителей чипов: `NVDA`, `SNDK`, `MU`.

Курс больше не является набором разрозненных тем. Все 15 уроков последовательно добавляют один слой к одному продукту.

## Что делает система

Для каждой важной новости система возвращает structured output:

```json
{
  "ticker": "NVDA",
  "company": "NVIDIA",
  "event_type": "export_control",
  "impact_direction": "down",
  "impact_strength": "strong",
  "horizon": "1w",
  "confidence": 0.82,
  "evidence": ["source: title"],
  "why_it_matters": "...",
  "risks_to_call": ["..."]
}
```

Это **не trading bot** и не инвестиционный совет. Это учебная news-intelligence система для изучения архитектуры AI-агентов.

## Инструменты курса

- **Antigravity CLI (`agy`)**: agentic development loop. Ученик поручает агенту анализировать код, проектировать diff, тесты и evals.
- **LangGraph**: controlled runtime pipeline: state, nodes, routing, checkpointing, human review.
- **CrewAI**: analyst-review crew: semiconductor analyst, market reaction analyst, skeptic reviewer, editor.

## Быстрый запуск

```bash
conda activate py11
python -m news_impact.cli --news data/sample_news.jsonl --format markdown
python -m unittest discover -s tests
python evals/run_eval.py
```

## Структура репозитория

- `src/news_impact/` — runnable-прототип Chip News Impact Engine.
- `data/sample_news.jsonl` — учебный набор chip-market новостей.
- `evals/` — expected labels и eval runner.
- `tests/` — unit tests для schema, pipeline, review contract.
- `lessons/` — 15 последовательных уроков.
- `agy-prompts/` — prompts для Antigravity CLI по каждому уроку.
- `projects/final-project.md` — финальная защита.
- `environment.md` — окружение, `agy`, `config.env`, безопасные режимы.

## Последовательность уроков

1. [Постановка задачи: news impact engine, а не trading bot](lessons/01-постановка-задачи-news-impact-engine-а-не-trading-bot.md)
2. [Схема данных и labels](lessons/02-схема-данных-и-labels.md)
3. [Baseline LLM classifier](lessons/03-baseline-llm-classifier.md)
4. [News ingestion](lessons/04-news-ingestion.md)
5. [Dedup и story clustering](lessons/05-dedup-и-story-clustering.md)
6. [Entity и ticker mapping](lessons/06-entity-и-ticker-mapping.md)
7. [Event classification](lessons/07-event-classification.md)
8. [Impact scoring](lessons/08-impact-scoring.md)
9. [Horizon scoring](lessons/09-horizon-scoring.md)
10. [LangGraph pipeline](lessons/10-langgraph-pipeline.md)
11. [LangGraph reliability](lessons/11-langgraph-reliability.md)
12. [CrewAI analyst crew](lessons/12-crewai-analyst-crew.md)
13. [Verifier и eval dataset](lessons/13-verifier-и-eval-dataset.md)
14. [Report/UI/API](lessons/14-report-ui-api.md)
15. [Финальная защита](lessons/15-финальная-защита.md)

## Работа с agy

```bash
agy --version
agy --print --sandbox --add-dir "$(pwd)" "Inspect the repository and suggest the next safe step."
agy --continue
```

Запускайте команды из корня репозитория. Флаг `--add-dir "$(pwd)"` явно добавляет текущий проект в workspace `agy`; без него CLI может стартовать в scratch-директории и не увидеть файлы курса.

Подробные варианты запуска, включая read-only prompt без внешних артефактов и признаки неправильного workspace, описаны в `environment.md`.

Каждый урок содержит свой `agy` prompt и ручной разбор. Ответ агента нельзя принимать автоматически: ученик обязан проверить код, tests, evals и финансовые ограничения.

## Ограничение ответственности

Курс предназначен для обучения архитектуре AI-агентов. Выводы системы не являются финансовой рекомендацией, торговым сигналом или прогнозом доходности.
