# Illustrative self-authored run: `challenger`

Same mechanism and same caveat as the `meddicc` run
(`evals/illustrative/README.md`) — read that file's top section first if
you haven't. Short version: same author behind brief, transcript, gold,
and grading prompt; real isolation only between the skill-run process and
the grading process; **not Tier 3, not evidence of real-world accuracy.**

## Result

Full grader output: `runs/challenger-demo-verdict.md`. Skill's raw output:
`runs/challenger-demo-output.md`.

| Metric | Result |
|---|---|
| Recall (gold's ranked findings) | 4/4 |
| Hallucinations | 0 |
| Out-of-rubric finding (board-member pressure) | Full credit — surfaced twice, once flagged as an unexploited signal under the skill's own "Pitch arc" section, once as a standalone "Single biggest missed teaching opportunity" call-out, never force-fit into Teach/Tailor/Take-control |
| Per-dimension agreement | 2/3 comparable dimensions (Take control disagreed — skill called it Covered on the strength of mid-call pushback, gold called it Missed/Partial on the weak, permission-seeking close; the grader sided with gold here, since nothing in the close proposes a specific next step) |
| Gold-construction mismatch | Yes — the brief assumed a "handling resistance/negotiation" dimension the skill doesn't actually score. Flagged honestly rather than forced into the comparison: this is a gap in how well I (the same author) actually knew this skill's rubric shape going in, not a skill defect. |

## Reading this honestly

Two real signals, in tension with each other: the out-of-rubric finding
detection worked *better* here than in the `meddicc` run (full credit vs.
no credit) — the skill explicitly named the missed board-pressure
opportunity as its own section rather than absorbing it silently. But the
Take-control disagreement repeats the same pattern seen in `meddicc`: the
skill again resolved a genuinely ambiguous, soft-close moment toward more
credit than the gold read supports. One data point in each direction is
not a trend — it's two single samples from the same author.

The gold-construction mismatch is itself worth keeping visible: it's
direct evidence that "the same author already knows the rubric" isn't
even reliably true in practice — I got a dimension wrong. That cuts
against over-trusting this mechanism's grading in either direction, and
is exactly the kind of thing a real second author (human or third-party)
would have caught before the run, not after.

## Reproducing this

Same pattern as `meddicc`'s reproduction steps in `evals/illustrative/README.md`,
substituting `challenger` for `meddicc` and this directory's
`challenger-demo.*` files.
