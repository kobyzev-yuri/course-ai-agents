from __future__ import annotations

from shared.config import get_client, get_model


SYSTEM_PROMPT = """You are a compact educational AI agent.
Given a goal, produce:
1. a short plan,
2. the next action,
3. a verification criterion.
Keep the answer concise."""


def run(goal: str) -> str:
    client = get_client()
    response = client.chat.completions.create(
        model=get_model(),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": goal},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content or ""


if __name__ == "__main__":
    result = run("Prepare a 30-minute lesson about tool use in AI agents.")
    print(result)
