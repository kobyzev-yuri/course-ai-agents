from __future__ import annotations

import argparse
from pathlib import Path

from .pipeline import DEFAULT_TICKERS, run_pipeline
from .reporting import to_jsonl, to_markdown


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Chip News Impact Engine training pipeline.")
    parser.add_argument("--news", default="data/sample_news.jsonl", help="Path to input JSONL news data.")
    parser.add_argument("--tickers", default=",".join(DEFAULT_TICKERS), help="Comma-separated ticker list.")
    parser.add_argument("--format", choices=["jsonl", "markdown"], default="markdown")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tickers = [ticker.strip().upper() for ticker in args.tickers.split(",") if ticker.strip()]
    results = run_pipeline(Path(args.news), tickers)
    print(to_jsonl(results) if args.format == "jsonl" else to_markdown(results))


if __name__ == "__main__":
    main()
