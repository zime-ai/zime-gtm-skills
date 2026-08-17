# Illustrative self-authored run: `qualify-pipeline-check`

Same mechanism and same caveat as the other illustrative runs
(`evals/illustrative/README.md`) — same author behind brief, CSV, gold, and
grading prompt; real isolation only between the skill-run process and the
grading process; **not Tier 3, not evidence of real-world accuracy.**

This is Shape B (CSV pipeline-sweep) — adapted from the `deal-risk-digest`
pattern but for a flag-based (rather than scored) rubric. Because
`qualify-pipeline-check`'s rubric is an exact six-flag system
(`references/rubric.md`), the gold file here is a computed fact, not a
judgment call — this run has much less room for reasonable disagreement than
the transcript-audit skills' do.

## Result

Full grader output: `runs/qualify-pipeline-check-demo-verdict.md`. Skill's raw
output: `runs/qualify-pipeline-check-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (flag count, all 10 deals) | 10/10 |
| Flag type accuracy (correct flags cited, evidence tied to CSV cells) | 10/10 |
| Traps passed (5 constructed traps — 6-flag case, budget-amount OR logic, close-date comparisons, clean rows, sort order) | 5/5 |
| Hallucinations | 0 |
| Closing line 1 ("N of M deals flagged") | Correct (7 of 10) |
| Closing line 2 ("most common flag") | Correct ("close date sooner than procurement timeline" appearing 3 times) |

## Reading this honestly

Every row-level flag count, every trap, and the ranking were exactly right.
The skill's output also included an extra "Suggested action" column and an
intro line stating the scope — neither required by the rubric, but both
improve clarity without inventing facts. This is a single sample on a
deterministic rubric; treat as one data point showing the skill applies the
six-flag system correctly per-row and computes aggregate statistics (most
common flag count) accurately. No hedge, no ambiguity resolution issues — the
skill simply did the thing it's supposed to do.

## Reproducing this

Same pattern as the other illustrative runs, using
`evals/illustrative/artifacts/qualify-pipeline-check-demo.csv` as the input
instead of a transcript, and pointing the skill at it as
`claude -p "/qualify-pipeline-check ./pipeline.csv" --dangerously-skip-permissions`.
Grading scratch dir contains only the skill's real output + the CSV +
`gold/qualify-pipeline-check-demo.md` — never `SKILL.md`.
