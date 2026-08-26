# Brief: pain-finder-demo transcript

Same caveat as every run in this batch. Shape A (findings-recall): gold is
a **ranked pain-point list with confidence tags**, graded by recall,
confidence-calibration, and whether a downplayed pain gets silently
upgraded.

## Situation

One call: a mid-market hospitality company ("Brindle Hotels") talking to
a rep about a housekeeping-scheduling tool.

## Deliberate construction

- **Pain 1, High confidence, Operational friction**: buyer says
  housekeeping is short-staffed on weekends specifically, "we're
  scrambling every single Saturday, it's the same fire drill every week."
- **Pain 2, Medium confidence, Financial**: buyer mentions overtime costs
  are "creeping up, not sure exactly by how much, but it's noticeable on
  the P&L."
- **Pain 3, the trap — explicitly downplayed, must stay Low, not get
  silently upgraded**: buyer mentions guest complaints about room
  readiness "a couple times, but honestly it's not a big deal, we handle
  it fine when it happens." A shallow run upgrades this to Medium or High
  because "guest complaints" sounds compelling — the buyer's own framing
  explicitly downplays it, and the skill's rule forbids upgrading a pain
  the prospect explicitly downplayed just because it fits a better
  category.
- **Pain 4, Low confidence, must still be reported, not dropped**: buyer
  makes a single passing remark about onboarding new staff being
  "annoying sometimes" — vague, single mention, no elaboration. A shallow
  run drops this entirely for being too thin; the skill's rule requires
  reporting even Low-confidence pains, ranked last.

## The trap a weak run fails

Two traps: (1) upgrading the explicitly-downplayed guest-complaints pain
("it's not a big deal, we handle it fine") to Medium/High because the
topic sounds compelling — must stay Low and be labeled as downplayed in
the Notes section; (2) dropping the thin onboarding remark entirely
instead of reporting it, ranked last, at Low confidence.

## Not present: reporting any of these is a hallucination

- No specific dollar figure for overtime costs is stated — only "creeping
  up... noticeable on the P&L."
- No specific number of guest complaints is given, only "a couple times."
- No competitor or alternative vendor is mentioned anywhere.
