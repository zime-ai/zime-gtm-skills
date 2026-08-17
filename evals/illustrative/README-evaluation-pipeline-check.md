# Illustrative self-authored run: `evaluation-pipeline-check`

Same mechanism and same caveat as the other runs in `evals/illustrative/README.md`
— same author behind brief, CSV, gold, and grading prompt; real isolation only
between the skill-run process and the grading process; **not Tier 3, not evidence
of real-world accuracy.**

This is Shape B (CSV pipeline-sweep) applied to technical evaluations. Because
`evaluation-pipeline-check`'s rubric is deterministic (exact six checks with
median thresholds), the gold file here is a computed fact, not a judgment call.

## Result

Full grader output: `runs/evaluation-pipeline-check-demo-verdict.md`. Skill's raw
output: `runs/evaluation-pipeline-check-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (flag count + evidence, all 8 deals) | 8/8 |
| Ranking / ordering (flagged deals sorted by flag count, ties stable) | Correct |
| Traps passed (3 constructed: grouped medians, below-median security skip, above-median clean state) | 3/3 |
| Hallucinations | 0 |
| Closing line 1 ("N of M deals in Evaluation flagged") | Correct (6 of 8) |
| Closing line 2 ("most common flag") | Correct (stalled on 4 of 6 flagged) |

## Reading this honestly

Every row-level score, every evidence citation (including the nuanced grouped
median logic for check 4), and the ranking were exactly right. All three traps
passed: the skill correctly grouped deals by value to compute separate
`days_in_stage` medians, correctly skipped the security-review check for
below-median deals, and correctly didn't flag Acme despite "In Progress"
status. The closing line on flag counts and the signal distribution (stalled
as the most common) were both exact.

This is the strongest possible single-sample result — a clean 100% with no
hedging room. One sample; treat as one data point, not a verdict. The skill
applied a complex, multi-step deterministic rubric without error on synthetic
data; real-world performance depends on real pipeline exports.

## Reproducing this

Same pattern as the other illustrative runs, using
`evals/illustrative/artifacts/evaluation-pipeline-check-demo.csv` as the input
instead of a transcript, and running:

```bash
claude "run evaluation-pipeline-check on ./evaluation-pipeline-check-demo.csv" --dangerously-skip-permissions
```

Grading scratch dir contains only the skill's real output + the CSV +
`gold/evaluation-pipeline-check-demo.md` — never `SKILL.md` or `BRIEF.md`, to
isolate the grading process from the expectation-setting process.
