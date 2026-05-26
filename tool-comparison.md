# Сравнительная карта: Antigravity vs LangGraph vs CrewAI

## Antigravity

Лучше всего подходит для агентной разработки и практического выполнения задач в рабочей среде: код, терминал, браузер, артефакты, параллельные агенты.

Используйте Antigravity, когда нужно:

- делегировать coding или QA задачу агенту;
- наблюдать за несколькими агентами в разных рабочих областях;
- получать проверяемые артефакты: screenshots, walkthroughs, logs, test results;
- быстро провести agentic development loop от задачи до проверки.

## LangGraph

Лучше всего подходит для production workflow, где нужны явное состояние, ветвления, checkpointing, resume и human-in-the-loop.

Используйте LangGraph, когда нужно:

- контролировать граф выполнения;
- сохранять и возобновлять состояние;
- встраивать approval gates;
- дебажить долгие агентные процессы;
- строить надежные support, operations или backend agents.

## CrewAI

Лучше всего подходит для быстрых multi-agent прототипов и сценариев, где задача естественно раскладывается на роли.

Используйте CrewAI, когда нужно:

- быстро собрать команду researcher/analyst/editor/reviewer;
- показать collaborative intelligence;
- построить sequential или hierarchical workflow;
- совместить автономные crews с более управляемыми flows.

## Быстрое правило выбора

- Нужна рабочая среда для агентной разработки и проверки: **Antigravity**.
- Нужен надежный stateful workflow с контролем: **LangGraph**.
- Нужен быстрый role-based multi-agent прототип: **CrewAI**.
- Нужна production-система: часто комбинируйте подходы, например Antigravity для разработки, LangGraph для runtime, CrewAI для автономных экспертных подзадач.
