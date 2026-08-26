# Brief: meddpicc-demo transcript

Same caveat as every run in `evals/illustrative/`: same-author brief, gold,
and grading prompt — not Tier 3, not third-party evidence. Shape A
(findings-recall): gold is a **ranked eight-letter scorecard**, graded by
per-letter agreement and hallucination check, same shape as
`meddicc`/`challenger`.

## Situation

Late-stage call: a manufacturing company ("Ferro Systems") three weeks
past a verbal yes on a quality-control platform, talking through what's
left before signature.

## Deliberate construction — one letter per trap where possible

- **Metrics — Covered**: buyer states the platform needs to cut inspection
  rework by "at least 15%" to justify the spend internally.
- **Economic buyer — Covered**: buyer names their VP Ops as the final
  signer, "she's already seen the numbers and is fine with it."
- **Decision criteria — Partial**: buyer mentions integration with their
  existing MES system matters but never says what "good enough" looks
  like technically.
- **Decision process — Covered**: buyer walks through the internal
  approval steps (VP Ops sign-off, then a rubber-stamp from finance).
- **Paper process — the trap, should be Partial not Covered**: buyer says
  "legal's going to look at it, I just don't know how long that usually
  takes with our team" — a legal function is named but no signer, no
  security review, no procurement timeline is confirmed. A shallow run
  scores this Covered because "legal" was mentioned; the rubric requires
  more than naming the function.
- **Identify pain — Covered**: buyer names the specific rework-cost pain
  quantified under Metrics.
- **Champion — the trap, should be Missed not Covered**: buyer's
  colleague (an Ops Manager, Dana) is described only as enthusiastic —
  "Dana's been raving about this to anyone who'll listen" — but never
  shown doing anything: no internal selling, no stakeholder looped in, no
  objection handled internally. A shallow run scores Champion Covered
  from the enthusiasm alone; the rubric explicitly requires action, not
  sentiment.
- **Competition — Missed**: no competitor or alternative (including
  status quo) is discussed anywhere on the call.

## The trap a weak run fails

Two traps stacked: (1) scoring **Paper process** Covered because "legal"
was named, when no signer/timeline/security review was confirmed — should
be Partial; (2) scoring **Champion** Covered from Dana's enthusiasm alone,
when nothing shows Dana doing something internally — should be Missed.

## Not present: reporting any of these is a hallucination

- No specific dollar figure for the deal is stated anywhere on the call.
- No named legal or procurement contact — only "legal" as a function.
- No competitor name appears anywhere.
