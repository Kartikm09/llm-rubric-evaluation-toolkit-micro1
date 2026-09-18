"""Validate documented reviewer score domains before reporting results."""
import csv
from pathlib import Path


def validated_scores(row: dict[str, str], columns: list[str]) -> dict[str, int]:
    scores = {}
    for column in columns:
        try:
            value = int(row.get(column, ""))
        except (ValueError, TypeError):
            raise ValueError(f"{column} must be an integer from 1 to 5") from None
        if not 1 <= value <= 5:
            raise ValueError(f"{column} must be an integer from 1 to 5")
        scores[column] = value
    return scores


def load_scored_rows(path: Path, columns: list[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for number, row in enumerate(rows, start=2):
        try:
            validated_scores(row, columns)
        except ValueError as error:
            raise ValueError(f"CSV row {number}: {error}") from None
    return rows
