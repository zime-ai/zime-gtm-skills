# Illustrative self-authored run: `negotiation-pipeline-check`

Same mechanism and same caveat as the `meddicc`/`challenger`/`deal-risk-digest`
runs (`evals/illustrative/README.md`) — same author behind brief, CSV, gold,
and grading prompt; real isolation only between the skill-run process and
the grading process; **not Tier 3, not evidence of real-world accuracy.**

This is Shape B (CSV pipeline-sweep) — testing a six-check rubric against a
synthetic negotiation-stage export. Because `negotiation-pipeline-check`'s
rubric is deterministic (check thresholds and exact median calculation), the
gold file here is a computed fact, not a judgment call — this run has much
less room for reasonable disagreement than `meddicc`/`challenger`'s transcript
audits.

## Result

Full grader output: `runs/negotiation-pipeline-check-demo-verdict.md`. Skill's
raw output: `runs/negotiation-pipeline-check-demo-output.md`.

| Metric | Result |
|---|---|
| Row-level accuracy (flag status + flag count, all 10 deals) | 10/10 |
| Ranking (8 flagged deals sorted by flag count) | Correct |
| Flag count accuracy | 10/10 |
| Most common flag (correct flag #3, correct count 3 of 8 flagged) | Correct |
| Closing line 1 ("N of M deals flagged") | Correct (8 of 10) |
| Closing line 2 ("most common flag") | Correct (discount without approval) |
| Median calculation (14% threshold for check #3) | Correct |
| Hallucinations | 0 |

**Summary: 100% accuracy — perfect match against gold across all dimensions.**

## Reading this honestly

Every row-level flag, every flag count, the ranking, median calculation, and
both closing lines were exactly right — strong evidence the skill applies its
six deterministic checks correctly across all rows and edge cases. The
boundary-condition row (Catalyst Group: discount 15% > median 14%) was
correctly flagged, confirming the median calculation and > threshold logic.
All clean rows remained clean.

This is a single sample with high accuracy on a synthetic scenario. The value
here is: (1) the mechanism works for CSV pipeline-sweeps, (2) the skill's six
checks are internally consistent with its own rubric, and (3) no hallucinations
were present. One sample; treat as one data point, not a verdict on the skill's
accuracy in production negotiations.

## Reproducing this

Same pattern as the other illustrative runs, using
`evals/illustrative/artifacts/negotiation-pipeline-check-demo.csv` as the
input instead of a transcript, and pointing the skill at it as:

```bash
claude -p "/negotiation-pipeline-check ./pipeline.csv" --dangerously-skip-permissions
```

Grading scratch dir contains only the skill's real output + the CSV +
`gold/negotiation-pipeline-check-demo.md` — never `SKILL.md`, never the brief.
