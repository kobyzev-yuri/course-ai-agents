from __future__ import annotations

from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from shared.config import get_client, get_model


class SupportState(TypedDict):
    ticket: str
    category: str
    answer: str
    needs_human: bool


def classify_ticket(state: SupportState) -> dict[str, str]:
    text = state["ticket"].lower()
    if "refund" in text or "payment" in text:
        return {"category": "billing"}
    if "bug" in text or "error" in text:
        return {"category": "technical"}
    return {"category": "general"}


def route(state: SupportState) -> Literal["draft_answer", "human_review"]:
    return "human_review" if state["category"] == "billing" else "draft_answer"


def human_review(state: SupportState) -> dict[str, object]:
    return {
        "needs_human": True,
        "answer": "This ticket touches billing. A human specialist must approve the final response.",
    }


def draft_answer(state: SupportState) -> dict[str, object]:
    client = get_client()
    response = client.chat.completions.create(
        model=get_model(),
        messages=[
            {
                "role": "system",
                "content": "Draft a short support response. Do not invent facts. Mention the ticket category.",
            },
            {"role": "user", "content": f"Category: {state['category']}\nTicket: {state['ticket']}"},
        ],
        temperature=0.2,
    )
    return {"answer": response.choices[0].message.content or "", "needs_human": False}


def build_graph():
    builder = StateGraph(SupportState)
    builder.add_node("classify_ticket", classify_ticket)
    builder.add_node("draft_answer", draft_answer)
    builder.add_node("human_review", human_review)
    builder.add_edge(START, "classify_ticket")
    builder.add_conditional_edges(
        "classify_ticket",
        route,
        {"draft_answer": "draft_answer", "human_review": "human_review"},
    )
    builder.add_edge("draft_answer", END)
    builder.add_edge("human_review", END)
    return builder.compile()


if __name__ == "__main__":
    app = build_graph()
    result = app.invoke(
        {
            "ticket": "I see an error every time I export the report.",
            "category": "",
            "answer": "",
            "needs_human": False,
        }
    )
    print(result)
