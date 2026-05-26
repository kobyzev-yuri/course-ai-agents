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
agy --print --sandbox --add-dir "$(pwd)" "Summarize the repository and suggest the next safe step."
agy --prompt-interactive --add-dir "$(pwd)" "Help me extend the eval dataset. Ask before editing."
agy --continue
```

Запускайте `agy` из корня репозитория и оставляйте `--add-dir "$(pwd)"` в учебных командах. Этот флаг явно подключает текущую директорию как workspace; если его убрать, `agy` может сообщить, что активный workspace не настроен, и предложить работать в scratch.

## Советы ученику по запуску `agy`

Рекомендуемый read-only вариант для уроков:

```bash
agy --print --sandbox --add-dir "$(pwd)" "Inspect this repository and summarize the goal, constraints, and first safe next step. Do not modify repository files."
```

Если нужно, чтобы ответ появился только в терминале, без дополнительных markdown-артефактов в служебной директории `agy`, добавьте это явно в prompt:

```bash
agy --print --sandbox --add-dir "$(pwd)" "Inspect this repository and summarize the goal, constraints, and first safe next step. Do not modify repository files and do not create external artifacts; print the answer directly in the terminal."
```

Для живого диалога используйте интерактивный режим, но просите агента согласовывать изменения до записи файлов:

```bash
agy --prompt-interactive --add-dir "$(pwd)" "Help me inspect the next lesson. Ask before editing files."
```

Если `agy` отвечает про другой проект, предлагает создать новый workspace или пишет план для незнакомого приложения, остановитесь и проверьте три вещи:
- команда запущена из корня `course-ai-agents`;
- в команде есть `--add-dir "$(pwd)"`;
- ответ агента упоминает `Chip News Impact Engine`, `NVDA`, `SNDK`, `MU` или файлы `src/news_impact/`.

Не принимайте план агента автоматически. Для каждого ответа проверьте, что он сохраняет границу non-investment-advice, не раскрывает `config.env`, опирается на evidence и предлагает тесты или evals вместо уверенных неподтвержденных выводов.

Не используйте `--dangerously-skip-permissions` в учебной работе, кроме отдельной sandbox-only демонстрации с пустым тестовым проектом.
