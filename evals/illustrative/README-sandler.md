# Illustrative self-authored run: `sandler`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**ranked seven-compartment scorecard plus a sequencing-violation
finding**, graded by per-compartment agreement and whether the violation
is explicitly named, same shape as `meddicc`/`challenger`.

Transcript uses a different company, names, and product than the skill's
own bundled `assets/sample-transcript.txt` (Millbrook Market / scheduling,
vs. the skill's Harborview / returns) to avoid re-testing a scenario the
skill was already built and calibrated against.

## Result

Full grader output: `runs/sandler-demo-verdict.md`. Skill's raw output:
`runs/sandler-demo-output.md`.

| Metric | Result |
|---|---|
| Per-compartment agreement with gold | 7/7 exact match |
| Trap 1 (Pain — should be `Missed`, not `Covered`) | Passed |
| Trap 2 (Fulfillment — should be `Missed`, not `Covered`) | Passed |
| Sequencing violation (pitch before pain secured) named explicitly | Yes |
| Hallucinations | 0 |

## Reading this honestly

Full clean pass — the strongest result in this batch so far. Both
compartments this brief specifically built as traps (a symptom-only "we
get a fair number of scheduling conflicts" line that must not read as
secured Pain, and a hedged "I guess, sure" that must not read as a real
Fulfillment agreement) landed exactly on gold's reasoning, not just the
right label. The sequencing violation — the failure mode this skill
exists to catch that a plain checklist audit would miss — was named
explicitly and tied to the correct compartment, in substance nearly
identical to the gold reference. One transcript, one grader, one model
throughout, but on the process-order distinction that's Sandler's whole
premise (as opposed to BANT/MEDDICC's independent-checklist scoring),
this run didn't just avoid the obvious failures, it reasoned through them
correctly.

## Reproducing this

```bash
mkdir -p /tmp/sandler-run/.claude/skills
cp -r skills/sandler /tmp/sandler-run/.claude/skills/
cp evals/illustrative/transcripts/sandler-demo.txt /tmp/sandler-run/transcript.txt
( cd /tmp/sandler-run && claude -p "run sandler on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/sandler-grade
cp /tmp/sandler-run/<output> /tmp/sandler-grade/output.md
cp evals/illustrative/transcripts/sandler-demo.txt /tmp/sandler-grade/transcript.txt
cp evals/illustrative/gold/sandler-demo.md /tmp/sandler-grade/gold.md
( cd /tmp/sandler-grade && claude -p "<grading prompt, see runs/sandler-demo-verdict.md>" --dangerously-skip-permissions )
```
