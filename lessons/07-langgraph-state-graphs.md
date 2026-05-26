# Урок 7. LangGraph: агент как граф состояний

## Цель
Научиться мыслить агентный workflow как граф узлов, переходов и условий.

## Ключевые понятия
StateGraph, nodes, edges, conditional routing, START, END, subgraph.

## Подготовка окружения

Перед уроком активируйте окружение и установите LangGraph:

```bash
conda activate py11
pip install openai python-dotenv langgraph
```

Проверьте `config.env` с `OPENAI_BASE_URL=https://api.proxyapi.ru/openai/v1` и `OPENAI_API_KEY`. Затем убедитесь, что пример импортируется без ошибок: `python -m py_compile course-ai-agents/examples/07_langgraph_support_agent.py`.

## Теория: 10-15 минут

- LangGraph делает поток выполнения явным: каждый node отвечает за один шаг, а edges описывают порядок или условия перехода.
- Графовая модель полезна там, где важны предсказуемость, дебаг, контроль ветвлений и повторяемость.
- Узлы могут быть LLM-вызовами, обычными Python-функциями, tool calls или подграфами.

## Яркий пример
Support-agent: classify_ticket -> route_to_billing_or_tech -> retrieve_context -> draft_response -> quality_check -> END.

## Практика: 15-25 минут

- Нарисуйте graph для возврата товара в интернет-магазине.
- Добавьте conditional edge для “нужна ли ручная эскалация”.

## Практический запуск

Запустите LangGraph-пример support-agent:

```bash
conda activate py11
python course-ai-agents/examples/07_langgraph_support_agent.py
```

Найдите в коде узлы `classify_ticket`, `draft_answer`, `human_review` и объясните, почему routing вынесен в отдельную функцию.

## Мини-тест
1. Что такое node в LangGraph?
   - A. Шаг выполнения, читающий и обновляющий state
   - B. Имя модели
   - C. Папка проекта
2. Зачем conditional routing?
   - A. Чтобы выбирать следующий шаг по state
   - B. Чтобы всегда идти линейно
   - C. Чтобы удалить проверки
3. Когда граф лучше свободного агента?
   - A. Когда нужны контроль и воспроизводимость
   - B. Когда цель неизвестна
   - C. Когда нет требований

## Ответы
1. A — Шаг выполнения, читающий и обновляющий state
2. A — Чтобы выбирать следующий шаг по state
3. A — Когда нужны контроль и воспроизводимость

## Домашнее задание
Сделать диаграмму LangGraph-агента для выбранной бизнес-задачи.

## Критерий готовности
Слушатель может объяснить архитектурное решение урока, применить его к новому сценарию и назвать минимум один риск неправильного применения.
