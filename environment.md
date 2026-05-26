# Окружение для практики

Практические примеры курса рассчитаны на conda-окружение `py11` и OpenAI-compatible API router.

## Активация

```bash
conda activate py11
```

## Конфигурация LLM

В корне workspace используется файл `config.env`. Примеры ищут его автоматически вверх по дереву директорий.

Ожидаемые переменные:

```bash
OPENAI_BASE_URL=https://api.proxyapi.ru/openai/v1
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4o-mini
```

`OPENAI_MODEL` можно заменить на любую модель, доступную через router. Если переменная не задана, примеры используют `gpt-4o-mini` как нейтральное значение по умолчанию.

## Установка зависимостей

```bash
conda activate py11
pip install -r course-ai-agents/examples/requirements.txt
```

## Запуск примеров

```bash
conda activate py11
python course-ai-agents/examples/01_minimal_agent.py
python course-ai-agents/examples/05_tool_use_agent.py
python course-ai-agents/examples/07_langgraph_support_agent.py
python course-ai-agents/examples/09_crewai_market_brief.py
```

## Правило безопасности

Не коммитьте `config.env` и не вставляйте API key в учебные материалы, prompts или ответы агента. Ключ должен оставаться только в локальной конфигурации окружения.
