# Gold label: pain-finder-demo, reference ranked pain list

Written from `evals/illustrative/BRIEF-pain-finder.md`'s construction.
Shape A (findings-recall) — graded by recall, confidence calibration, and
whether the downplayed/thin pains are handled per the skill's own rules.

## Expected pain list (most business-critical first)

1. **Category**: Operational friction. **Confidence**: High. "we're
   scrambling every single Saturday, it's the same fire drill every
   week... short-staffed, rooms falling behind, managers pulled in to
   cover shifts." Recurring, named cause, explicit ongoing impact,
   returned to at the end as "the one that actually keeps coming up."
2. **Category**: Financial. **Confidence**: Medium. "overtime's creeping
   up... noticeable on the P&L" — real cost signal, but no specific
   figure, "not sure exactly by how much."
3. **Category**: Customer/guest experience. **Confidence**: **Low, not
   Medium/High (trap)** — "a couple times... but honestly it's not a big
   deal, we handle it fine... not something I lose sleep over." Must stay
   Low and be flagged in Notes as explicitly downplayed by the buyer, not
   upgraded because "guest complaints" sounds compelling.
4. **Category**: Operational friction (onboarding). **Confidence**: Low
   — **must still appear, ranked last, not dropped**. "onboarding new
   staff is annoying sometimes, but that's true everywhere... not really
   specific to us" — single vague mention, no elaboration.

## Expected Notes section

- Pain 3 (guest complaints) is explicitly downplayed by the buyer — flag
  this, don't let the topic's inherent appeal upgrade its confidence.
- Pain 4 (onboarding) is Low confidence and thin, reported last per the
  skill's own rule against dropping Low-confidence pains.

## The trap a weak run fails

Two traps: upgrading the explicitly-downplayed guest-complaints pain to
Medium/High because the topic sounds compelling (must stay Low, flagged
as downplayed); and dropping the thin onboarding remark entirely instead
of reporting it last at Low confidence.

## Not present: reporting any of these is a hallucination

- No dollar figure for overtime costs — only "creeping up... noticeable
  on the P&L."
- No specific count of guest complaints beyond "a couple times."
- No competitor or alternative vendor mentioned anywhere.
