"""Generate concise feedback themes from rubric scores."""
from __future__ import annotations

import argparse
from collections import Counter
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

    weakest_counts = Counter()
    for row in rows:
        scores = validated_scores(row, SCORE_COLUMNS)
        weakest_counts[min(scores, key=scores.get)] += 1

    print("Weakest dimensions")
    print("------------------")
    for dimension, count in weakest_counts.most_common():
        print(f"- {dimension}: {count}")
    print("Reviewer comments:")
    for row in rows:
        print(f"- {row['item_id']}: {row['reviewer_comment']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
