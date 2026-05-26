# Курс: AI-агенты, архитектура и применение

Практический курс из 15 уроков о том, как проектировать AI-агентов для coding, research, customer support, QA automation и business workflows. Курс использует три опорных инструмента:

- **Google Antigravity** — среда для агентной разработки, постановки задач, параллельных агентов и проверки через editor/terminal/browser/artifacts loop.
- **LangGraph** — фреймворк для управляемых stateful-агентов, графов, checkpointing, human-in-the-loop и production workflow.
- **CrewAI** — фреймворк для быстрых multi-agent прототипов через роли, задачи, crews и flows.

## Для кого курс

Курс рассчитан на разработчиков, тимлидов, product/automation engineers и технических специалистов, которые уже понимают основы LLM, но хотят перейти от “чат с моделью” к надежным агентным системам.

## Результат обучения

После курса слушатель сможет:

- отличать агентный workflow от обычного LLM-промпта;
- проектировать агента через цель, состояние, инструменты, проверки и права;
- выбирать между Antigravity, LangGraph и CrewAI под конкретный сценарий;
- строить single-agent и multi-agent архитектуры;
- добавлять human-in-the-loop, checkpointing, evals, observability и security controls;
- защищать архитектуру агентной системы на финальном проекте.

## Формат урока

Каждый урок начинается с обязательной подготовки окружения: `conda activate py11`, установка нужных пакетов и проверка `config.env`. Это делает практику воспроизводимой и сразу связывает теорию с runnable-примерами.

## Структура

1. [Что такое AI-агент и чем он отличается от чатбота](lessons/01-agent-vs-chatbot.md)
2. [Анатомия агента: модель, инструкции, инструменты, память, среда](lessons/02-agent-anatomy.md)
3. [Antigravity как практическая среда агентной работы](lessons/03-antigravity-workspace.md)
4. [Промпт как спецификация задачи для агента](lessons/04-prompt-as-specification.md)
5. [Tool use: как агент безопасно действует во внешнем мире](lessons/05-tool-use.md)
6. [Память и состояние: от контекста диалога к управляемому workflow](lessons/06-memory-and-state.md)
7. [LangGraph: агент как граф состояний](lessons/07-langgraph-state-graphs.md)
8. [Надежность: checkpointing, retries, resume и human-in-the-loop](lessons/08-reliability-hitl.md)
9. [CrewAI: ролевые команды агентов](lessons/09-crewai-crews.md)
10. [CrewAI Flows и управляемая оркестрация](lessons/10-crewai-flows.md)
11. [Multi-agent архитектуры: параллельность, делегирование, конфликт результатов](lessons/11-multi-agent-architectures.md)
12. [Проверка результата: evals, тесты, артефакты и критики](lessons/12-evals-and-verification.md)
13. [Безопасность и контроль: права, секреты, sandbox, audit trail](lessons/13-security-and-control.md)
14. [Production-подход: observability, стоимость, latency, качество](lessons/14-production-observability.md)
15. [Финальный проект: спроектировать агентную систему под реальную задачу](lessons/15-final-project.md)

## Дополнительные материалы

- [Окружение для практики](environment.md)
- [Шаблон урока](lesson-template.md)
- [Все мини-тесты с ответами](assessments/quizzes-with-answers.md)
- [Финальный проект и критерии оценки](projects/final-project.md)
- [Сравнительная карта инструментов](tool-comparison.md)

## Практические примеры

Примеры находятся в `examples/` и используют `config.env` из корня workspace:

- `01_minimal_agent.py` — минимальный агент с планом, действием и критерием проверки.
- `05_tool_use_agent.py` — безопасный mock tool call без внешних побочных эффектов.
- `07_langgraph_support_agent.py` — LangGraph workflow с routing и human gate.
- `09_crewai_market_brief.py` — CrewAI команда researcher/analyst/editor.
- `10_crewai_flow_onboarding.py` — CrewAI Flow с детерминированным ветвлением.
# course-ai-agents
