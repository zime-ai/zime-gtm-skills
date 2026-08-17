# Illustrative self-authored run: `end-client-registration`

Same mechanism and same caveat as the `meddicc`/`deal-risk-digest` runs
(`evals/illustrative/README.md`) — same author behind brief, CSV, gold, and
grading prompt; real isolation only between the skill-run process and the
grading process; **not Tier 3, not evidence of real-world accuracy.**

This is Shape B (CSV row-sweep) — a deterministic, completeness-check skill
rather than a risk-scoring skill. Because `end-client-registration`'s rubric
is a checklist of seven dimensions, the gold file here is a computed fact,
not a judgment call — similar to `deal-risk-digest`.

## Result

Full grader output: `runs/end-client-registration-demo-verdict.md`. Skill's
raw output: `runs/end-client-registration-demo-output.md`.

| Metric | Result |
|---|---|
| Registration-level accuracy (10 registrations) | 8/10 |
| Trap handling (5 constructed traps) | 3/5 passed |
| False negatives | 1 (REG-106: vague scope "General support" not flagged) |
| False positives | 1 (REG-109: near-expiry flagged despite being valid per rubric) |
| Hallucinations (claims not in CSV) | 1 explicit (near-expiry concern) |
| Closing line 1 ("N of M flagged") | Correct numerically (7 of 10) but wrong set — swapped REG-106 for REG-109 |
| Closing line 2 (most common dimension) | **Wrong** — output bucketed four distinct rubric dimensions into "missing required field" bucket; correct answer is Dimension 4 (Conflict check), 2 registrations |

## Reading this honestly

The skill's real output got 8 of 10 registrations' individual decisions right,
identified the correct evidence for each, and produced plausible suggested
actions. But it made two opposing mistakes on adjacent rows (missed a vague
scope on REG-106, over-flagged a valid-but-soon-expiring registration on
REG-109 as needing "renewal decision now"), and at the summary level,
collapsed the rubric's seven distinct dimensions into one meta-category
("missing required field") for the closing "most common dimension" claim,
which is methodologically wrong and contradicts how the rubric itself is
structured.

This is narrower than `meddicc`/`challenger`'s pattern (ambiguity bias) or
`deal-risk-digest`'s pattern (counting error in post-hoc summary). It's two
localized misinterpretations (one on the interpretation of "vague" scope, one
on expiry-date interpretation as needing near-term renewal flag) plus one
aggregation method that doesn't match the rubric's framing. One sample; treat
as one data point about dimension interpretation, not a verdict on the skill.

## Reproducing this

Same pattern as the other illustrative runs, using
`evals/illustrative/artifacts/end-client-registration-demo.csv` as the input:

```bash
# 1. Run the skill in isolation
mkdir -p /tmp/end-client-registration-run/.claude/skills
cp -r skills/end-client-registration /tmp/end-client-registration-run/.claude/skills/
cp evals/illustrative/artifacts/end-client-registration-demo.csv /tmp/end-client-registration-run/
( cd /tmp/end-client-registration-run && claude -p "/end-client-registration ./end-client-registration-demo.csv" --dangerously-skip-permissions )

# 2. Grade in a separate isolated dir — never expose SKILL.md
mkdir -p /tmp/end-client-registration-grade
cp /tmp/end-client-registration-run/<output.md> /tmp/end-client-registration-grade/output.md
cp evals/illustrative/artifacts/end-client-registration-demo.csv /tmp/end-client-registration-grade/
cp evals/illustrative/gold/end-client-registration-demo.md /tmp/end-client-registration-grade/gold.md
( cd /tmp/end-client-registration-grade && claude -p "<grading prompt>" --dangerously-skip-permissions )
```

The grading prompt compares the skill's output against the gold label
row-by-row, checks the five named traps, and audits the closing summary
lines. See `runs/end-client-registration-demo-verdict.md` for the full prompt
used and the detailed findings.
