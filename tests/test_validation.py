import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

def cli(script, rows, *, options=(), extra_json=None):
    with tempfile.TemporaryDirectory() as temp:
        source = Path(temp) / "input.csv"
        if isinstance(rows, list) and (not rows or isinstance(rows[0], dict)):
            fields = list(rows[0]) if rows else ["score", "language"]
            with source.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows(rows)
        args = [sys.executable, str(ROOT / "scripts" / script), str(source)]
        if extra_json is not None:
            output = Path(temp) / "outputs.json"
            output.write_text(json.dumps(extra_json), encoding="utf-8")
            args.append(str(output))
        return subprocess.run([*args, *options], text=True, capture_output=True, cwd=ROOT, timeout=10)

COLUMNS = ['general', 'factuality', 'reasoning', 'instruction', 'safety', 'tone']
SCRIPTS = ['evaluate_scores.py', 'generate_feedback_summary.py']
EVALUATE = 'evaluate_scores.py'

def row(item, value):
    return {"item_id": item, "reviewer_comment": "Check evidence", **{column: str(value) for column in COLUMNS}}

class RubricTests(unittest.TestCase):
    def test_follow_up_boundary_and_dimension_floor(self):
        good = row("good", 4)
        safety_failure = row("safety-failure", 5)
        safety_failure["safety"] = "2"
        result = cli(EVALUATE, [good, safety_failure])
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.splitlines()
        self.assertTrue(next(line for line in lines if line.startswith("good,")).endswith(",false"))
        failure = next(line for line in lines if line.startswith("safety-failure,"))
        self.assertIn(",safety,true", failure)
        self.assertEqual(float(failure.split(",")[1]), 4.5)

    def test_all_reporting_commands_reject_invalid_scores(self):
        for script in SCRIPTS:
            for score in ["", "0", "6", "100", "1.5"]:
                with self.subTest(script=script, score=score):
                    bad = row("bad", 4)
                    bad["safety"] = score
                    result = cli(script, [bad])
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("safety", result.stderr.lower())
                    self.assertNotIn("Traceback", result.stderr)

    def test_missing_dimension_is_rejected(self):
        bad = row("bad", 4)
        del bad["safety"]
        for script in SCRIPTS:
            result = cli(script, [bad])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("safety", result.stderr.lower())
            self.assertNotIn("Traceback", result.stderr)

if __name__ == "__main__":
    unittest.main()
