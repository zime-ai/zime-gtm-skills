# Illustrative self-authored run: `churn-prevention`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is an
**eight-dimension scorecard plus a low/medium/high risk close**, graded by
per-dimension agreement plus a planted-trap check.

## Result

Full grader output: `runs/churn-prevention-demo-verdict.md`. Skill's raw
output: `runs/churn-prevention-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 6/8 exact match |
| Risk-level close | High / High — match |
| Trap (a polite, uneventful-sounding call must not read as low-risk) | Passed |
| Hallucinations | 0 |

## Reading this honestly

The core trap this brief was built to test passed cleanly and decisively —
the run landed on **High** risk and explicitly named the surface-politeness
pattern as camouflage ("'we're good here' reads as surface politeness, not
health"), rather than letting the calm tone soften the read. But two of
eight dimensions drifted softer than gold in a way that echoes the same
instinct the trap is designed to catch: sentiment was scored Missed
instead of gold's Covered (gold wants the flat, unelaborated tone itself
credited as evidence; the run instead scored it on whether the CSM flagged
it, missing its own observation that the pattern was "unflagged" as
grounds to credit the dimension), and champion strength was scored Partial
instead of gold's Missed (hedging on a signal the rubric says should be
read at face value, not softened because Alex framed it as "nothing
serious"). So the headline verdict is exactly right, but the dimension-level
scoring shows a residual pull toward the leniency the brief exists to
guard against, even while the top-line conclusion held firm.
