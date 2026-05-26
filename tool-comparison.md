# Antigravity CLI vs LangGraph vs CrewAI in this course

## Antigravity CLI (`agy`)
Используется как agentic development interface. Ученик просит агента анализировать код, предлагать diff, проектировать тесты и готовить review notes. Это рабочая среда разработки, а не production runtime.

## LangGraph
Используется как production-like orchestration: typed state, nodes, routing, checkpointing, replay, human gates. В проекте это слой `src/news_impact/langgraph_pipeline.py`.

## CrewAI
Используется как аналитическая команда для review: Semiconductor Analyst, Market Reaction Analyst, Skeptic Reviewer, Editor. В проекте это слой `src/news_impact/crewai_review.py`.

## Лучшее сочетание
`agy` помогает строить и проверять код, LangGraph исполняет pipeline, CrewAI проверяет спорные выводы как экспертная команда.
