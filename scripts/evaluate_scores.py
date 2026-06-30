"""Evaluate LLM rubric score rows."""
from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "evaluation_scores.csv"
SCORE_COLUMNS = ["general", "factuality", "reasoning", "instruction", "safety", "tone"]

with DATA.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

print("item_id,average,weakest_dimension,needs_follow_up")
for row in rows:
    scores = {column: int(row[column]) for column in SCORE_COLUMNS}
    average = sum(scores.values()) / len(scores)
    weakest = min(scores, key=scores.get)
    needs_follow_up = average < 4 or scores[weakest] <= 2
    print(f"{row['item_id']},{average:.2f},{weakest},{str(needs_follow_up).lower()}")
