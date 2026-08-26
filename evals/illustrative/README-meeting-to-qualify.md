# Illustrative self-authored run: `meeting-to-qualify`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is an
**eight-dimension scorecard plus a go/no-go close**, graded by
per-dimension agreement plus a planted-trap check.

## Result

Full grader output: `runs/meeting-to-qualify-demo-verdict.md`. Skill's raw
output: `runs/meeting-to-qualify-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold (incl. close verdict) | 9/9 exact match |
| Trap (don't infer buying authority from a "VP" title alone) | Passed |
| Hallucinations | 0 confirmed (some quote fragments unverifiable — no transcript in the grading dir) |

## Reading this honestly

Full clean pass — every dimension label and the final close call ("Needs
one more call") matched gold exactly. The planted trap — a VP title paired
with an explicit disclaimer of real sign-off authority — was handled
correctly: the run scored buying authority Partial from what Taylor
actually said about the procurement committee, not from the seniority the
title implies. The grader flagged that some of the run's quotes run
longer than gold's trimmed excerpts, which it couldn't verify verbatim
since the transcript wasn't copied into its grading directory — checked
directly against the source transcript here, the fuller quotes are all
genuine, just less truncated than gold's phrasing.
