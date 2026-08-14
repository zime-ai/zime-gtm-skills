# Illustrative self-authored run: `meddicc`

**Read this before the numbers below.** The brief, transcript, gold label,
and the grading prompt were all written by the same Claude session (this
one) that also holds `meddicc`'s general rubric shape in memory from
having helped build this repo. That is exactly the self-eval bias
`EVALS.md` warns about. **This is not Tier 3. It is not a substitute for
`evals/gt/` (human-labeled) or `evals/gt-web/` (third-party-sourced,
currently zero qualifying sources — see `evals/SCORECARD.md`).** It
demonstrates the mechanism — brief-first construction, isolated real skill
run, independent grading — not the repo's real-world accuracy.

## What actually was, and wasn't, isolated

- The **brief** (`../BRIEF.md`) was written first, deciding what the
  transcript would deliberately contain (an out-of-rubric pain, a
  legitimately-N/A dimension, a downplayed signal) before the transcript
  itself, matching `evals/gold/BRIEFS.md`'s own discipline. It was not
  written blind to MEDDICC's shape — full blinding isn't possible for the
  same author who's worked on this skill.
- The **skill run** was genuinely isolated: a scratch dir containing only
  `.claude/skills/meddicc/` and the transcript, invoked as a fresh
  `claude -p "/meddicc ./transcript.txt" --dangerously-skip-permissions`
  process — no gold file, no brief, no repo root present.
- The **grading** was a second, separate `claude -p` process in its own
  scratch dir containing only `output.md`, `transcript.txt`, and `gold.md`
  — never `SKILL.md`, the brief, or this conversation's context. This part
  is real process isolation, not simulated.
- What is **not** isolated: the same model family (and, for the brief/gold
  authorship, literally the same conversation) sits behind the transcript
  author, the gold labeler, and ultimately the grader's training. Process
  separation is not author separation.

## Result

Full grader output: `runs/meddicc-demo-verdict.md`. Skill's raw output:
`runs/meddicc-demo-output.md`.

| Metric | Result |
|---|---|
| Recall (gold's ranked findings) | 4/4 |
| Hallucinations (gold's "not present" traps) | 0 outright; 1 soft overstatement flagged (implied IT/COO steps were "named" when Dana only guessed) |
| Out-of-rubric finding (succession/retirement risk) | No credit — folded silently into "Identify pain — Covered" instead of flagged as outside MEDDICC's seven letters |
| Legitimately-N/A dimension (Competition) | Wrong — skill forced "Covered" instead of "Not applicable," exactly the failure mode the gold label named in advance |
| Per-dimension agreement | 4/7 (Decision process, Champion, and Competition all disagreed — in each case the skill's verdict was more confident than the transcript supports) |

## Reading this honestly

The one real, if narrow, signal here: on a call constructed to have three
specific ambiguous spots (a forced-N/A trap, an enthusiasm-vs-action
champion trap, a "steps guessed vs. steps named" trap), the skill's real
run landed on the more confident, less accurate side of all three. That's
a genuine, if single-sample, data point about failure direction — the
skill leans toward resolving ambiguity rather than reporting it as
ambiguous. It is not evidence about `meddicc`'s accuracy in general: one
transcript, one grader, one model family throughout.

## Reproducing this

```bash
# 1. Run the skill in isolation (same pattern as evals/framework/run_skill.sh)
mkdir -p /tmp/meddicc-run/.claude/skills
cp -r skills/meddicc /tmp/meddicc-run/.claude/skills/
cp evals/illustrative/transcripts/meddicc-demo.txt /tmp/meddicc-run/transcript.txt
( cd /tmp/meddicc-run && claude -p "/meddicc ./transcript.txt" --dangerously-skip-permissions )

# 2. Grade in a separate isolated dir -- never expose SKILL.md to this process
mkdir -p /tmp/meddicc-grade
cp /tmp/meddicc-run/<output> /tmp/meddicc-grade/output.md
cp evals/illustrative/transcripts/meddicc-demo.txt /tmp/meddicc-grade/transcript.txt
cp evals/illustrative/gold/meddicc-demo.md /tmp/meddicc-grade/gold.md
( cd /tmp/meddicc-grade && claude -p "<grading prompt, see runs/meddicc-demo-verdict.md's own framing>" --dangerously-skip-permissions )
```
