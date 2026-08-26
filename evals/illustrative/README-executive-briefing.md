# Illustrative self-authored run: `executive-briefing`

Same mechanism, same caveat as the rest of this batch
(`evals/illustrative/README.md`). Shape C (document-writer) — gold is a
**reference brief** (snapshot, status, risk, ask), graded by field-level
diff against the skill's own four-part structure.

## Result

Full grader output: `runs/executive-briefing-demo-verdict.md`. Skill's
raw output: `runs/executive-briefing-demo-output.md`.

| Metric | Result |
|---|---|
| Planted trap (deal value never stated — must not estimate) | Passed |
| Close date ("before end of quarter," buyer-stated) | Under-reported — headline framing says "no firm date" before the correct quote follows |
| Both risks present with citations | Passed |
| Heard ask (legal-to-legal call), all 3 elements | Passed |
| Inferred exec-to-exec proposal kept unconfirmed | Passed |
| Hallucinations | 0 |

## Reading this honestly

The trap this brief was built around — inventing or estimating a deal
value the call never states — was avoided cleanly, and the harder ask
distinction (a buyer-requested legal call correctly tagged `heard`,
versus the rep's own exec-to-exec idea correctly kept as a deferred
proposal) came through exactly right. The one real finding is on a field
the brief didn't specifically trap: the close date. The buyer states a
real target ("we're hoping to have this signed before end of quarter —
that's the internal goal we're working toward") and the skill's own
snapshot field opens with "no firm date" before quoting that line,
underselling a fact that was actually said. Not an invented date, not a
missing citation — a framing choice that reads more uncertain than the
call supports, on a skill whose whole job is reporting what the input
actually says.

## Reproducing this

```bash
mkdir -p /tmp/eb-run/.claude/skills
cp -r skills/executive-briefing /tmp/eb-run/.claude/skills/
cp evals/illustrative/transcripts/executive-briefing-demo.txt /tmp/eb-run/transcript.txt
( cd /tmp/eb-run && claude -p "run executive-briefing on ./transcript.txt" --dangerously-skip-permissions )

mkdir -p /tmp/eb-grade
cp /tmp/eb-run/<output> /tmp/eb-grade/output.md
cp evals/illustrative/transcripts/executive-briefing-demo.txt /tmp/eb-grade/transcript.txt
cp evals/illustrative/gold/executive-briefing-demo.md /tmp/eb-grade/gold.md
( cd /tmp/eb-grade && claude -p "<grading prompt, see runs/executive-briefing-demo-verdict.md>" --dangerously-skip-permissions )
```
