from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


DEFAULT_MODEL = "gpt-4o-mini"
DEFAULT_BASE_URL = "https://api.proxyapi.ru/openai/v1"


def load_course_env() -> None:
    """Load config.env from the workspace tree without exposing secrets."""
    current = Path(__file__).resolve()
    for parent in current.parents:
        candidate = parent / "config.env"
        if candidate.exists():
            load_dotenv(candidate, override=False)
            return


def get_model() -> str:
    load_course_env()
    return os.getenv("OPENAI_MODEL", DEFAULT_MODEL)


def get_client() -> OpenAI:
    load_course_env()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to config.env before running LLM examples.")

    return OpenAI(
        api_key=api_key,
        base_url=os.getenv("OPENAI_BASE_URL", DEFAULT_BASE_URL),
    )
