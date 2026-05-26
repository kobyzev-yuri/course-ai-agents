from __future__ import annotations

import json
from typing import Any

from shared.config import get_client, get_model


def get_order_status(order_id: str) -> dict[str, Any]:
    """A safe mock tool: no external side effects, deterministic output."""
    orders = {
        "A-100": {"status": "paid", "delivery": "tomorrow", "risk": "low"},
        "B-200": {"status": "payment_failed", "delivery": None, "risk": "needs_human_review"},
    }
    return orders.get(order_id, {"status": "unknown", "delivery": None, "risk": "needs_human_review"})


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "Return order status, delivery estimate, and risk level for a training order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "Order identifier, for example A-100.",
                    }
                },
                "required": ["order_id"],
                "additionalProperties": False,
            },
        },
    }
]


def run(user_request: str) -> str:
    client = get_client()
    messages: list[dict[str, Any]] = [
        {
            "role": "system",
            "content": (
                "You are a support agent. Use tools when order state is needed. "
                "If risk is needs_human_review, do not promise a final resolution."
            ),
        },
        {"role": "user", "content": user_request},
    ]

    first = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",
        temperature=0.1,
    )
    assistant_message = first.choices[0].message
    messages.append(assistant_message.model_dump(exclude_none=True))

    for tool_call in assistant_message.tool_calls or []:
        if tool_call.function.name != "get_order_status":
            raise RuntimeError(f"Unexpected tool call: {tool_call.function.name}")

        args = json.loads(tool_call.function.arguments)
        tool_result = get_order_status(args["order_id"])
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(tool_result, ensure_ascii=False),
            }
        )

    final = client.chat.completions.create(
        model=get_model(),
        messages=messages,
        temperature=0.1,
    )
    return final.choices[0].message.content or ""


if __name__ == "__main__":
    print(run("Customer asks: what is happening with order B-200?"))
