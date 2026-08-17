# Illustrative self-authored run: `won-pipeline-check`

Same mechanism and same caveat as the `deal-risk-digest`, `meddicc`, and
`challenger` runs (`evals/illustrative/README.md`) — same author behind brief,
CSV, gold, and grading prompt; real isolation only between the skill-run
process and the grading process; **not Tier 3, not evidence of real-world
accuracy.**

This is Shape B (CSV pipeline-sweep) — a deterministic, row-scored skill with
an exact handoff-data-completeness rubric (`references/rubric.md`). Because
the rubric defines six specific checks, the gold file here is a computed
fact, not a judgment call — this run has minimal room for reasonable
disagreement.

## Result

Full grader output: `runs/won-pipeline-check-demo-verdict.md`. Skill's raw
output: `runs/won-pipeline-check-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (flags + evidence, all 9 deals) | 9/9 |
| Clean-deal check (two deals marked clean per rubric) | Correct |
| Trap tests (8 constructed traps — isolated flags, false positives) | 8/8 |
| Hallucinations | 0 |
| Closing line 1 ("N of M deals flagged") | Correct (7 of 9) |
| Closing line 2 ("most common flag") | **Wrong** — output said "Orphaned record (2 occurrences)" without comparing to other flags; gold requires "ahead of each other flag at 1 of 7 each" |
| Table ranking | **Wrong** — output grouped by flag category (Orphaned first) instead of preserving CSV row order when all flagged deals are tied at 1 flag each |

## Reading this honestly

Every individual row-level score and all eight traps passed — strong evidence
the skill correctly applies its six-check rubric to each row. But the output
violated two format requirements the rubric defines: the table ranking (when
deals are tied, preserve row order, not flag-type grouping) and the
closing-line detail (which flag is most common must compare to the count on
other flags, not stand alone). The first is a sorting logic miss, the second
is an incomplete aggregate summary. One sample; treat as one data point —
row-level detection is flawless, but output formatting and summary statistics
need tightening.

## Reproducing this

Same pattern as the other illustrative runs, using
`evals/illustrative/artifacts/won-pipeline-check-demo.csv` as the input, and
pointing the skill at it as `claude -p "/won-pipeline-check ./pipeline.csv"
--dangerously-skip-permissions`. Grading scratch dir contains only the
skill's real output + the CSV + `gold/won-pipeline-check-demo.md` — never
`SKILL.md` or the brief.
