from __future__ import annotations

from crewai.flow.flow import Flow, listen, router, start


class OnboardingFlow(Flow):
    """A deterministic Flow example that can be extended with crews or LLM calls."""

    @start()
    def receive_customer(self) -> dict[str, str]:
        return {"customer": "Acme", "plan": "enterprise", "risk": "high"}

    @router(receive_customer)
    def choose_path(self, customer: dict[str, str]) -> str:
        if customer["plan"] == "enterprise" or customer["risk"] == "high":
            return "human_gate"
        return "self_serve"

    @listen("human_gate")
    def prepare_human_review(self) -> str:
        return "Prepare onboarding brief and ask customer success manager for approval."

    @listen("self_serve")
    def prepare_self_serve(self) -> str:
        return "Send self-serve onboarding checklist."


if __name__ == "__main__":
    flow = OnboardingFlow()
    print(flow.kickoff())
