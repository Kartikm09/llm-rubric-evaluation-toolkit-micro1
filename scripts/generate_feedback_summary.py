"""Generate concise feedback themes from rubric scores."""
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "evaluation_scores.csv"
SCORE_COLUMNS = ["general", "factuality", "reasoning", "instruction", "safety", "tone"]

with DATA.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

weakest_counts = Counter()
for row in rows:
    scores = {column: int(row[column]) for column in SCORE_COLUMNS}
    weakest_counts[min(scores, key=scores.get)] += 1

print("Weakest dimensions")
print("------------------")
for dimension, count in weakest_counts.most_common():
    print(f"- {dimension}: {count}")
print("Reviewer comments:")
for row in rows:
    print(f"- {row['item_id']}: {row['reviewer_comment']}")
