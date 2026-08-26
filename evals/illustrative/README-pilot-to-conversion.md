# Illustrative self-authored run: `pilot-to-conversion`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is an
**eight-dimension scorecard plus an on-track/at-risk/stalled close**,
graded by per-dimension agreement plus a planted-trap check.

## Result

Full grader output: `runs/pilot-to-conversion-demo-verdict.md`. Skill's raw
output: `runs/pilot-to-conversion-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold (incl. close) | 8/8 exact match |
| Trap (rep optimism ≠ a named conversion date/owner) | Passed |
| Hallucinations | 0 — extra quotes checked directly against the transcript, all verbatim |

## Reading this honestly

Full clean pass, the strongest result in this batch. Every dimension
matched gold, including the deliberately open call on user engagement
(the brief allows either Covered or Partial as long as the usage decline
is flagged — the run chose Partial-leaning-Missed and flagged it
explicitly, which is the more useful read). The planted trap — closing on
plain optimism with no named date or owner for conversion — was caught
exactly as intended, with the run explicitly naming "rep optimism, not a
plan" as the reason for scoring it Missed rather than crediting the
positive tone. The run's evidence was, if anything, more precisely sourced
than gold's own quotes.
