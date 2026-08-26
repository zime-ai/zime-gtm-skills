# Illustrative self-authored run: `deal-highlights`

Same mechanism, same caveat as the rest of this batch
(`evals/illustrative/README.md`). Shape C (document-writer) — gold is a
**reference highlights list** (6 items), graded by item recall/precision
against the skill's six categories, not a rubric score.

## Result

Full grader output: `runs/deal-highlights-demo-verdict.md`. Skill's raw
output: `runs/deal-highlights-demo-output.md`.

| Metric | Result |
|---|---|
| Gold items recalled | 6/6, all citations correct |
| Extra items beyond gold | 2 — one legit (a rep-side ROI-model commitment), one padding |
| Planted trap: dog/vacation small talk | Passed — never mentioned |
| Planted trap: Tuesday/Wednesday scheduling exchange | **Failed** — output listed it as "Commitment (both): next call set for Wednesday" |
| Hallucinations | 0 |

## Reading this honestly

Full recall and accurate citations on all six real highlights is the
strong result here. The one real finding: the skill avoided the more
obvious trap (dog-and-vacation chatter never appears) but walked straight
into the subtler one — the "does Tuesday or Wednesday work" scheduling
back-and-forth got written up as "Commitment (both)," exactly the padding
the skill's own rule forbids ("generic rapport-building, scheduling
chatter, and small talk are not highlights"). Scheduling a follow-up call
is not itself a deal commitment the way "I'll send the numbers by
Thursday" is — it has no stakes if it slips. That the skill caught the
easy small-talk trap but not the scheduling one suggests the six-category
boundary is fuzzier at the "commitment" edge than at the others.

## Reproducing this

```bash
mkdir -p /tmp/dh-run/.claude/skills
cp -r skills/deal-highlights /tmp/dh-run/.claude/skills/
cp evals/illustrative/transcripts/deal-highlights-demo.txt /tmp/dh-run/transcript.txt
( cd /tmp/dh-run && claude -p "run deal-highlights on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/dh-grade
cp /tmp/dh-run/<output> /tmp/dh-grade/output.md
cp evals/illustrative/transcripts/deal-highlights-demo.txt /tmp/dh-grade/transcript.txt
cp evals/illustrative/gold/deal-highlights-demo.md /tmp/dh-grade/gold.md
( cd /tmp/dh-grade && claude -p "<grading prompt, see runs/deal-highlights-demo-verdict.md>" --dangerously-skip-permissions )
```
