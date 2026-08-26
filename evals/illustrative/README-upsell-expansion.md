# Illustrative self-authored run: `upsell-expansion`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is an
**eight-dimension scorecard plus a go/hold close**, graded by
per-dimension agreement plus two planted-trap checks.

## Result

Full grader output: `runs/upsell-expansion-demo-verdict.md`. Skill's raw
output: `runs/upsell-expansion-demo-output.md`.

| Metric | Result |
|---|---|
| Per-dimension agreement with gold | 7/8 exact match |
| Trap 1 (account-health risk gates the read, doesn't average with 5 other Covered dims) | Passed |
| Trap 2 (personal enthusiasm ≠ champion advocacy) | Passed |
| Hallucinations | 0 — one interpretive gloss ("question dodged") flagged as a slightly stronger claim than the transcript literally supports, and an invented "reads-well-too" verification step with no basis |

## Reading this honestly

Both planted traps passed cleanly — the run correctly held the close to
"Hold" despite five of eight dimensions being Covered, refusing to let the
account-health risk average away, and it correctly refused to credit Sam's
"I'm really excited" as real champion advocacy. The one dimension mismatch
is a rubric-schema slip rather than a reasoning error: the skill's rubric
is Covered/Partial/Missed like the others in this batch, and dimension 1
came back "Partial" where gold scores it flatly "Missed" — the prose still
correctly treats the risk as unresolved and gates the close on it, so the
substance is right even though the label is softer than gold's. The run
also added an unearned "reads-well-too... sanity-checked against a
healthy-close pattern" line with no actual comparison behind it — harmless
noise, not a scoring defect.
