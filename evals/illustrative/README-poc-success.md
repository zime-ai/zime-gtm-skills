# Illustrative self-authored run: `poc-success`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**seven-dimension scorecard plus a pass/fail/inconclusive close**, graded
by per-dimension agreement plus a planted-trap check.

## Result

Full grader output: `runs/poc-success-demo-verdict.md`. Skill's raw output:
`runs/poc-success-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold (incl. close) | 7/8 exact match |
| Trap (champion's secondhand confidence ≠ economic-buyer sign-off) | Passed |
| Hallucinations | 0 — the one quote the grader flagged as unverifiable is genuine, checked directly against the transcript |

## Reading this honestly

The planted trap is the one thing this brief was built to test, and it
passed cleanly: the run correctly scored sponsor sign-off Missed because
the champion was speaking for the VP rather than the VP confirming
anything herself, and it landed on the correct **inconclusive** overall
close for that exact reason. One dimension diverged from gold —
commercial next step, which gold reads as Covered (owner plus a
date-anchored trigger tied to the SOC 2 close) and the run scored Partial
because no hard date attaches to the redline itself. That's a stricter,
defensible read rather than a rubric violation, not a scoring error. The
grader also flagged a quote ("I'll want that in writing") as unconfirmed
since no transcript was in its grading directory — checked against the
actual transcript here, it's a genuine line from the call.
