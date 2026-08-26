# Illustrative self-authored run: `sell-the-dream`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**five-element scorecard plus a required sequencing finding**, graded by
per-element agreement and whether the violation is caught, same shape as
`sandler`'s violation check applied to Raskin's five elements instead of
the submarine's seven compartments.

## Result

Full grader output: `runs/sell-the-dream-demo-verdict.md`. Skill's raw
output: `runs/sell-the-dream-demo-output.md`.

| Metric | Result |
|---|---|
| Per-element agreement with gold | 4/5 |
| Sequencing violation (feature pitched before any of elements 1-3) caught | Yes, correct root cause |
| Hallucinations | 0 |

## Reading this honestly

The central trap this brief was built around — a call where every element
is individually present somewhere, so a run that only checks presence
would report "no violation found" — didn't fail: the sequencing violation
was caught with the right root cause (feature-first, vision backfilled
after). The one real finding is a scoring inconsistency it introduced on
its own: it marked element 4 ("Introduce Features as Magic Gifts")
`Missed` rather than `Covered`, reasoning that a feature stated without
promised-land framing isn't yet a true "magic gift." That's a real
observation about the call, but it's the *same* order problem the
sequencing section already exists to hold — gold's structure keeps
element presence and sequencing as two separate concerns precisely so a
weak run can't launder an order violation into a lower element score (or,
symmetrically, use a strong sequencing pass to paper over a genuinely
missing element). By folding the order judgment into element 4's score
and then re-flagging the same issue in the sequencing section, the output
double-counts one defect into two findings.

## Reproducing this

```bash
mkdir -p /tmp/std-run/.claude/skills
cp -r skills/sell-the-dream /tmp/std-run/.claude/skills/
cp evals/illustrative/transcripts/sell-the-dream-demo.txt /tmp/std-run/transcript.txt
( cd /tmp/std-run && claude -p "run sell-the-dream on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/std-grade
cp /tmp/std-run/<output> /tmp/std-grade/output.md
cp evals/illustrative/transcripts/sell-the-dream-demo.txt /tmp/std-grade/transcript.txt
cp evals/illustrative/gold/sell-the-dream-demo.md /tmp/std-grade/gold.md
( cd /tmp/std-grade && claude -p "<grading prompt, see runs/sell-the-dream-demo-verdict.md>" --dangerously-skip-permissions )
```
