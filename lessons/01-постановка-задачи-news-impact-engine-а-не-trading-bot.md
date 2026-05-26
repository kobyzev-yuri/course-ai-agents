# Урок 1. Постановка задачи: news impact engine, а не trading bot

## Роль в сквозном проекте
Этот урок добавляет один слой к Chip News Impact Engine. Курс не прыгает между абстрактными темами: каждый шаг улучшает систему поиска и оценки новостей по `NVDA`, `SNDK`, `MU`.

## Цель урока
Сформулировать продукт, границы ответственности и JSON-контракт результата.

## Входное состояние проекта
Файлы, которые ученик должен открыть перед занятием: `README.md, data/sample_news.jsonl`.

## Подготовка окружения

```bash
conda activate py11
pip install -e . --no-deps
python --version
python -m news_impact.cli --news data/sample_news.jsonl --format markdown
```

Если урок требует агентной разработки, используйте `agy` в sandbox-режиме и не включайте `--dangerously-skip-permissions`.

## Agentic задание через agy

Сначала используйте `agy` как навигатор по проекту:

```bash
agy --print --sandbox --add-dir "$(pwd)" "Audit lesson 1 for a beginner. Explain what the project already does by tracing data/sample_news.jsonl through src/news_impact/cli.py and run_pipeline into the structured output. Identify the product boundary between news-intelligence labels and trading advice. Name one wording or behavior that could confuse a student into reading the output as a trading signal. Do not modify files."
```

Здесь `agy` нужен не для того, чтобы сказать "начните с первого урока". Первый урок и так является точкой входа. Ценность задания в другом: агент должен быстро проверить, как ученик понял границу продукта, и связать абстрактное описание с реальным потоком данных в коде.

Ожидаемый ответ агента:
- показывает путь `data/sample_news.jsonl` -> `src/news_impact/cli.py` -> `run_pipeline` -> structured output;
- объясняет, что `up/down/neutral`, `strength`, `horizon` и `confidence` являются news-intelligence labels, а не командой покупать или продавать;
- называет места, где формулировки, например "impulse" или "market note", могут быть прочитаны слишком близко к trading-сигналу;
- предлагает первый безопасный шаг: ручной разбор одного результата и проверка его evidence, а не изменение модели или подключение внешних API.

Смысл задания не в том, чтобы слепо принять ответ агента, а в том, чтобы сравнить его аудит с текущим кодом, тестами и ограничениями курса.

Затем используйте `agy` уже как coding assistant. Задача должна быть маленькой, проверяемой и связанной с границей продукта:

```bash
agy --prompt-interactive --add-dir "$(pwd)" "Help me add one regression test or minimal wording fix that protects the lesson 1 boundary: the report must read as news intelligence, not trading advice. Inspect reporting.py, scoring.py, and tests. Propose the diff first, explain which test should fail before the change, and ask before editing files."
```

Хороший результат такого запуска — не большой рефакторинг, а один понятный patch: например, тест на disclaimer в markdown-отчете, проверка отсутствия слов вроде `buy`, `sell`, `trading signal`, или замена фразы, которая звучит как торговая рекомендация. После любого изменения ученик обязан запустить:

```bash
python -m unittest discover -s tests
python evals/run_eval.py
```

## Разбор руками
1. Найдите в коде место, где реализуется тема урока.
2. Запишите, какие данные входят в шаг и какие выходят.
3. Отметьте, где возможны ложноположительные выводы.
4. Сформулируйте, какую проверку можно автоматизировать.

## Практика
- Запустите CLI report и сохраните один пример результата в заметки.
- Измените одну учебную новость в `data/sample_news.jsonl` локально и предскажите, как изменится label.
- Верните изменение и запустите тесты.

```bash
python -m unittest discover -s tests
python evals/run_eval.py
```

## Ожидаемый результат
Ученик объясняет, почему система не дает инвестиционный совет.

## Мини-тест
1. Какой вход получает этот слой системы?
2. Какой выход обязан быть структурированным?
3. Где нужен human review или skeptic review?
4. Какая ошибка в этом уроке опаснее всего для аналитика?

## Ответы для самопроверки
1. Вход — учебный JSONL-файл `data/sample_news.jsonl` с новостями и список целевых тикеров `NVDA`, `SNDK`, `MU`. Через CLI этот вход попадает в `run_pipeline`, где новости загружаются, фильтруются, группируются в stories и передаются в scoring.
2. Выход — `ImpactAssessment`: ticker, company, story/news metadata, `event_type`, `impact_direction`, `impact_strength`, `horizon`, `confidence`, `evidence`, `why_it_matters`, `risks_to_call`. Эти поля нужны как structured output, чтобы результат можно было тестировать и сравнивать в evals.
3. Human review нужен для low-confidence, neutral/ambiguous, спорных read-through случаев и любых strong labels, где evidence слабее вывода. Skeptic review должен искать альтернативные объяснения, дубликаты, неверный ticker mapping и слишком уверенную формулировку.
4. Самая опасная ошибка — превратить news-intelligence label в инвестиционную рекомендацию: например, прочитать `up/strong over 3w` как команду покупать, игнорируя evidence, confidence, ограничения выборки и disclaimer. Вторая близкая ошибка — выдать эвристический label без проверяемого evidence.

## Критерий перехода дальше
Переходите к следующему уроку только если команда тестов проходит, а вы можете объяснить один пример правильного label и один пример сомнительного label.
