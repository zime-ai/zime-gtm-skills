# Brief: sandler-demo transcript

Same caveat as every run in this batch. Shape A (findings-recall): gold is
a **ranked seven-compartment scorecard plus a sequencing-violation
finding**, graded by per-compartment agreement and whether the violation
is caught, not just presence/absence of each compartment.

## Situation

Mid-stage call: a regional grocery chain ("Millbrook Market") talking to a
rep about a shift-scheduling platform. Different company, names, and
product than the skill's own bundled `assets/sample-transcript.txt` (which
uses "Harborview," "Kim," and a returns/routing-engine pitch) to avoid
re-testing a scenario the skill was already built and calibrated against
— same underlying pattern (pitch-before-pain, assumed close), different
surface details.

## Deliberate construction

- **1. Bonding & Rapport — Covered**: genuine small talk, rep matches
  buyer's tone before moving to business.
- **2. Up-Front Contract — Covered**: rep sets clear call agenda upfront
  ("I'll ask about how scheduling works today, and by the end we'll both
  know honestly whether this is worth a follow-up").
- **3. Pain — the trap, should be Missed not Covered**: buyer says "we do
  get a fair number of scheduling conflicts" but never quantifies impact,
  root cause, or urgency — then the rep pitches the auto-scheduler right
  after. A shallow run scores Pain Covered because a scheduling issue was
  mentioned; the rubric requires named cause/impact/urgency in the buyer's
  own words.
- **4. Budget — Missed**: no budget discussion anywhere; rep proceeds as
  if affordability is settled.
- **5. Decision — Partial**: buyer says "I'd check with my director
  first," naming an approver but never a process or timeline.
- **6. Fulfillment — the trap, should be Missed not Covered**: rep says
  "I think this is a great fit, let's get this moving, I'll send a
  contract this week" and buyer responds "I guess, sure" — a hesitant,
  one-sided assumption of close, not a real mutual decision. A shallow run
  scores this Covered because a next step ("send contract") was named.
- **7. Post-Sell — Missed**: call ends on "any other questions?" with no
  check for doubts or reversal risk.
- **Sequencing violation — must be flagged**: the rep pitches the
  auto-scheduler (feature territory) immediately after the vague "we do
  get a fair number of scheduling conflicts" line, before Pain was
  actually secured — a rep who jumped ahead, which the skill's own
  definition calls out as a violation distinct from any single
  compartment's score.

## The trap a weak run fails

Two traps: (1) scoring **Pain** Covered because "returns" was mentioned,
without the buyer naming cause/impact/urgency — should be Missed; (2)
scoring **Fulfillment** Covered because the rep named a next step, when
the buyer's hesitant "I guess, sure" shows no real mutual agreement —
should be Missed. Plus the sequencing violation (pitch before pain
secured) must be named as its own explicit finding, not folded into the
Pain score.

## Not present: reporting any of these is a hallucination

- No specific dollar figure is stated anywhere on the call.
- No named director or other approver beyond "my director," no name
  given.
- No competitor or alternative vendor is mentioned anywhere.
