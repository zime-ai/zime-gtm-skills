# Illustrative self-authored run: `follow-up-email-drafter`

Same mechanism, same caveat as the rest of this batch
(`evals/illustrative/README.md`). Shape C (document-writer) — gold is a
**reference email + grounding notes**, graded by claim-level diff (stated
fact vs. proposal, and whether the internal `Heard`/`Proposed` tags leak
into the customer-facing body), not a rubric score.

## Result

Full grader output: `runs/follow-up-email-drafter-demo-verdict.md`.
Skill's raw output: `runs/follow-up-email-drafter-demo-output.md`.

| Metric | Result |
|---|---|
| Planted trap (finance loop-in stated as agreed, not proposed) | Passed |
| `Heard`/`Proposed` tags leaking into email body | None |
| Q1 budget timing stated as settled fact | Not stated — omitted |
| Hallucinations | 0 |
| Grounding notes vs. gold | Exact match, tag-for-tag |

## Reading this honestly

Clean pass, the strongest result in this batch so far. The planted trap
(Marcus's "let me think about who'd be right for that" reads as a
non-agreement, not consent to loop in finance) was correctly kept out of
the email as a stated fact and phrased as the rep's own suggestion
instead — exactly the distinction the skill's grounding rule exists to
enforce. The internal `Heard`/`Proposed` tags stayed out of the body, and
grounding notes matched gold claim-for-claim. One data point, one model,
one grader — but on the specific failure mode this brief was built to
probe (an inferred ask silently promoted to an agreed fact), this run
didn't fail it.

## Reproducing this

```bash
mkdir -p /tmp/fed-run/.claude/skills
cp -r skills/follow-up-email-drafter /tmp/fed-run/.claude/skills/
cp evals/illustrative/transcripts/follow-up-email-drafter-demo.txt /tmp/fed-run/transcript.txt
( cd /tmp/fed-run && claude -p "run follow-up-email-drafter on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/fed-grade
cp /tmp/fed-run/<output> /tmp/fed-grade/output.md
cp evals/illustrative/transcripts/follow-up-email-drafter-demo.txt /tmp/fed-grade/transcript.txt
cp evals/illustrative/gold/follow-up-email-drafter-demo.md /tmp/fed-grade/gold.md
( cd /tmp/fed-grade && claude -p "<grading prompt, see runs/follow-up-email-drafter-demo-verdict.md>" --dangerously-skip-permissions )
```
