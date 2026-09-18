# LLM Rubric Evaluation Toolkit

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![Synthetic Data](https://img.shields.io/badge/Data-Synthetic-brightgreen)
![Portfolio Ready](https://img.shields.io/badge/GitHub-Portfolio%20Ready-black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Practical toolkit for scoring LLM outputs across quality, factuality, reasoning, instruction following, safety, and tone.

## Project Overview

This repository is a polished, recruiter-friendly portfolio project for `Cross-role AI Evaluation / AI Data` and adjacent micro1-style roles. It uses synthetic examples only and avoids confidential client data.

## Why This Project Exists

AI trainer and evaluator roles depend on consistent scoring, evidence-backed comments, and clear feedback loops. This repo packages that workflow into reusable templates and scripts.

## Core Features

| Feature | Portfolio value |
| --- | --- |
| Dimension-level scoring templates for common LLM evaluation work. | Shows realistic execution and documentation depth. |
| Synthetic prompt-response examples with reviewer comments. | Shows realistic execution and documentation depth. |
| Average-score and weakest-dimension summaries. | Shows realistic execution and documentation depth. |
| Rubric schema for QA consistency. | Shows realistic execution and documentation depth. |
| Feedback-summary generation for model improvement notes. | Shows realistic execution and documentation depth. |

## Sample Workflow

1. Review the synthetic dataset in `data/`.
2. Read the methodology and quality checklist in `docs/`.
3. Inspect the worked examples in `examples/`.
4. Run the Python scripts in `scripts/`.
5. Use the generated summaries as evidence for GitHub, LinkedIn Featured, or interview discussion.

## Folder Structure

```text
README.md
docs/
data/
examples/
scripts/
LICENSE
.gitignore
LINKEDIN_DESCRIPTION.md
```

## How To Run

```bash
python3 scripts/evaluate_scores.py
```

The scripts use only the Python standard library.

## Example Output

```text
Portfolio QA summary generated from synthetic data.
Rows reviewed, averages, failures, and follow-up actions are printed in the terminal.
```

## Recruiter-Facing Skills Demonstrated

- LLM evaluation
- Rubric design
- RLHF-style feedback
- AI data QA
- Python automation
- Annotation guidelines

## LinkedIn Project Description

Created an LLM rubric evaluation toolkit for scoring AI outputs across factuality, reasoning, instruction following, safety, tone, and general response quality, with synthetic datasets, feedback templates, and Python score summaries.

## Safety and Privacy Notes

- Synthetic examples only.
- No confidential client data.
- No private client names.
- No harmful jailbreak instructions.
- No deletion or modification of existing repositories.

## Verification

Run `make verify` (or `python3 -m unittest discover -s tests -v`). The
standard-library suite uses independent synthetic fixtures and command-line
checks, including malformed inputs. GitHub CI runs the same command on Python
3.11. These checks verify the reporting code; they do not measure a live model
or validate the truth of a human-assigned score.

Score-reporting commands reject missing, blank, noninteger, or out-of-range
scores with a clear error. The documented scale is 1–5; missing assessments
are data errors and are not converted into model failures.

The existing no-argument commands retain the bundled dataset. An optional CSV
path lets reviewers validate another synthetic fixture, for example
`python3 scripts/evaluate_scores.py path/to/scores.csv`.

See [repair scope and evidence](docs/verified-repair.md).
