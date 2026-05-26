# Окружение курса

Основной интерфейс практики: Antigravity CLI `agy`.

```bash
conda activate py11
agy --version
agy --help
```

Базовые зависимости:

```bash
pip install -r requirements.txt
```

Если `langgraph` или `crewai` временно недоступны из сети, базовый прототип все равно запускается: LangGraph и CrewAI слои имеют deterministic fallback для учебных тестов.

Локальный `config.env` находится на уровень выше репозитория или в рабочей директории. Не коммитьте секреты.

```bash
OPENAI_BASE_URL=https://api.proxyapi.ru/openai/v1
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-4o-mini
```

Безопасные режимы `agy` для курса:

```bash
agy --print --sandbox "Summarize the repository and suggest the next safe step."
agy --prompt-interactive "Help me extend the eval dataset. Ask before editing."
agy --continue
```

Не используйте `--dangerously-skip-permissions` в учебной работе, кроме отдельной sandbox-only демонстрации с пустым тестовым проектом.
