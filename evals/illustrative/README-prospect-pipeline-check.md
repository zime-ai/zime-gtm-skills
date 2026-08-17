# Illustrative self-authored run: `prospect-pipeline-check`

Same mechanism and same caveat as the `meddicc`/`challenger` runs
(`evals/illustrative/README.md`) — same author behind brief, CSV, gold, and
grading prompt; real isolation only between the skill-run process and the
grading process; **not Tier 3, not evidence of real-world accuracy.**

This is Shape B (CSV pipeline-sweep) — prospect-stage engagement audit, with
six deterministic checks per row. Because `prospect-pipeline-check`'s rubric
is exact (six binary checks per row), the gold file here is computed fact,
not judgment — every flag is verifiable from the CSV directly.

## Result

Full grader output: `runs/prospect-pipeline-check-demo-verdict.md`. Skill's raw
output: `runs/prospect-pipeline-check-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (all 8 deals, flags present/absent) | 8/8 |
| Flag type correctness (only the six rubric checks used) | Correct |
| Ranking / tiebreak (flagged deals first, count descending) | Correct (cosmetic swap in count=1 tie, no impact) |
| Traps passed (5 constructed traps — close-date vs engagement, single-but-replied, aged-at-boundary, placeholder despite engagement, hardcoded threshold test) | 5/5 |
| Hallucinations | 0 |
| Closing line 1 ("N of M deals flagged") | Correct (5 of 8) |
| Closing line 2 ("most common flag") | Correct ("Aged with no activity", 3 of 5 flagged deals) |

## Reading this honestly

All eight row-level flags matched gold exactly, all five constructed traps
were handled correctly, and the ranking was right (only a cosmetic order swap
in a two-way count=1 tie). Zero hallucinations. Both closing lines matched
exactly — a strong signal the skill applies its engagement-gate rubric
correctly per-row and computes aggregate stats accurately across rows. One
sample; treat as one data point.

## Reproducing this

Same pattern as the other illustrative runs, using
`evals/illustrative/artifacts/prospect-pipeline-check-demo.csv` as the input
instead of a transcript, and pointing the skill at it as
`claude -p "/prospect-pipeline-check ./pipeline.csv" --dangerously-skip-permissions`.
Grading scratch dir contains only the skill's real output + the CSV +
`gold/prospect-pipeline-check-demo.md` — never `SKILL.md` or the brief.
