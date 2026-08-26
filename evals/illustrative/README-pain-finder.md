# Illustrative self-authored run: `pain-finder`

Same mechanism, same caveat as every other run in this repo
(`evals/illustrative/README.md`). Shape A (findings-recall) — gold is a
**ranked pain-point list with confidence tags**, graded by recall,
confidence calibration, and whether a downplayed or thin pain is handled
per the skill's own rules.

## Result

Full grader output: `runs/pain-finder-demo-verdict.md`. Skill's raw
output: `runs/pain-finder-demo-output.md`.

| Metric | Result |
|---|---|
| Gold pains recalled, correct order | 4/4 |
| Trap 1 (explicitly downplayed guest-complaints pain stays `Low`) | Passed |
| Trap 2 (thin onboarding pain reported, ranked last, not dropped) | Passed |
| Hallucinations | 0 |

## Reading this honestly

Clean pass on both traps this brief was built around. The guest-complaint
pain — a topic that reads as compelling on its face ("guest complaints")
— stayed at Low confidence with an explicit downplayed-by-the-buyer flag,
instead of getting inflated because the category sounds important. The
single vague onboarding remark stayed in the list, ranked last, instead
of getting dropped for being too thin to justify a slot. The skill did
relabel gold's category names (e.g. "Risk exposure" instead of
"Customer/guest experience," "Cost/headcount pressure" instead of
"Financial") — a defensible restructuring since the evidence quotes,
confidence tiers, and ranking order all matched exactly; the category
taxonomy itself isn't fixed by the rubric the way the confidence
calibration is.

## Reproducing this

```bash
mkdir -p /tmp/pf-run/.claude/skills
cp -r skills/pain-finder /tmp/pf-run/.claude/skills/
cp evals/illustrative/transcripts/pain-finder-demo.txt /tmp/pf-run/transcript.txt
( cd /tmp/pf-run && claude -p "run pain-finder on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/pf-grade
cp /tmp/pf-run/<output> /tmp/pf-grade/output.md
cp evals/illustrative/transcripts/pain-finder-demo.txt /tmp/pf-grade/transcript.txt
cp evals/illustrative/gold/pain-finder-demo.md /tmp/pf-grade/gold.md
( cd /tmp/pf-grade && claude -p "<grading prompt, see runs/pain-finder-demo-verdict.md>" --dangerously-skip-permissions )
```
