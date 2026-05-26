from __future__ import annotations

import os

from crewai import Agent, Crew, Process, Task

from shared.config import DEFAULT_BASE_URL, get_model, load_course_env


def configure_llm_env() -> None:
    load_course_env()
    os.environ.setdefault("OPENAI_API_BASE", os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL))
    os.environ.setdefault("OPENAI_MODEL_NAME", get_model())


def build_crew() -> Crew:
    configure_llm_env()

    researcher = Agent(
        role="Market Researcher",
        goal="Collect the most relevant facts for a short market brief.",
        backstory="You are concise and careful. You separate facts from assumptions.",
        verbose=False,
    )
    analyst = Agent(
        role="Business Analyst",
        goal="Turn research notes into actionable implications.",
        backstory="You focus on decisions, risks, and next steps.",
        verbose=False,
    )
    editor = Agent(
        role="Editor",
        goal="Produce a clear final brief for a product team.",
        backstory="You remove fluff and keep structure tight.",
        verbose=False,
    )

    research = Task(
        description="Prepare notes about practical use cases for AI agents in customer support.",
        expected_output="5 bullet points with facts or plausible assumptions clearly labeled.",
        agent=researcher,
    )
    analysis = Task(
        description="Convert the notes into product opportunities, risks, and adoption barriers.",
        expected_output="A short analysis with opportunities, risks, and barriers.",
        agent=analyst,
        context=[research],
    )
    edit = Task(
        description="Create a final market brief of no more than 250 words.",
        expected_output="A concise market brief with a title and 3 sections.",
        agent=editor,
        context=[analysis],
    )

    return Crew(
        agents=[researcher, analyst, editor],
        tasks=[research, analysis, edit],
        process=Process.sequential,
        verbose=False,
    )


if __name__ == "__main__":
    crew = build_crew()
    print(crew.kickoff())
