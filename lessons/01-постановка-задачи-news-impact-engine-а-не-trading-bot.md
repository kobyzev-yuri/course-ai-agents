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

## Критерий перехода дальше
Переходите к следующему уроку только если команда тестов проходит, а вы можете объяснить один пример правильного label и один пример сомнительного label.
