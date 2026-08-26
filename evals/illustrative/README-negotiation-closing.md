# Illustrative self-authored run: `negotiation-closing`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**six-dimension scorecard**, graded by per-dimension agreement plus a
planted-trap check.

## Result

Full grader output: `runs/negotiation-closing-demo-verdict.md`. Skill's
raw output: `runs/negotiation-closing-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 5/6 exact match |
| Trap (budget not re-confirmed at this proposal ≠ Covered off earlier carryover) | Passed |
| Hallucinations | 1 — a fabricated "reads-well-too" comparison call that doesn't exist in the transcript |

## Reading this honestly

The planted trap passed cleanly — the run correctly refused to credit
budget as confirmed just because it was assumed fine from an earlier call,
scoring it as unconfirmed at this specific proposal exactly as the rubric
requires. The one dimension mismatch is a stricter label than gold's
(Missed vs. gold's Partial) — defensible, not wrong, since some signal did
carry forward even if it wasn't reconfirmed. More notable: the run's
"reads-well-too" line claims it checked this transcript against "a
known-good fast-close call pattern" — no such comparison call exists
anywhere in the brief or transcript, so that line is an invented
verification step rather than a real one, even though it didn't corrupt
any of the actual dimension scoring.
