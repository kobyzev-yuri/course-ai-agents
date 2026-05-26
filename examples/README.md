# Практические примеры курса

Все примеры запускаются из корня workspace:

```bash
conda activate py11
python course-ai-agents/examples/01_minimal_agent.py
```

## Примеры

- `01_minimal_agent.py`: минимальный агент, который превращает цель в план, действие и критерий проверки.
- `05_tool_use_agent.py`: agent loop с mock-инструментом `get_order_status`.
- `07_langgraph_support_agent.py`: LangGraph graph с классификацией тикета, routing и human gate.
- `09_crewai_market_brief.py`: CrewAI crew из researcher, analyst и editor.
- `10_crewai_flow_onboarding.py`: CrewAI Flow с детерминированным branching.

## Конфигурация

Код читает `config.env` из родительских директорий. Ключи не хранятся в примерах.

Минимальная конфигурация:

```bash
OPENAI_BASE_URL=https://api.proxyapi.ru/openai/v1
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4o-mini
```
