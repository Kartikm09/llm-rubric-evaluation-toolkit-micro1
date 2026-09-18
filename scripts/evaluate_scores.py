"""Evaluate LLM rubric score rows."""
from __future__ import annotations

import argparse
from pathlib import Path

from score_validation import load_scored_rows, validated_scores

DATA = Path(__file__).resolve().parents[1] / "data" / "evaluation_scores.csv"
SCORE_COLUMNS = ["general", "factuality", "reasoning", "instruction", "safety", "tone"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path, nargs="?", default=DATA)
    args = parser.parse_args()
    try:
        rows = load_scored_rows(args.csv_path, SCORE_COLUMNS)
    except ValueError as error:
        parser.error(str(error))

    print("item_id,average,weakest_dimension,needs_follow_up")
    for row in rows:
        scores = validated_scores(row, SCORE_COLUMNS)
        average = sum(scores.values()) / len(scores)
        weakest = min(scores, key=scores.get)
        needs_follow_up = average < 4 or scores[weakest] <= 2
        print(f"{row['item_id']},{average:.2f},{weakest},{str(needs_follow_up).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
