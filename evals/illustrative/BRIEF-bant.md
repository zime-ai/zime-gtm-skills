# Brief: bant-demo transcript

Same caveat as every run in this batch. Shape A (findings-recall): gold is
a **ranked four-criterion scorecard**, graded by per-criterion agreement
and hallucination check. Different company/names than the skill's own
bundled `assets/sample-transcript.txt` to avoid re-testing a calibrated
scenario.

## Situation

First qualification call: a regional law firm ("Aldergate Legal")
evaluating a document-review platform, talking to their Director of
Operations.

## Deliberate construction

- **Budget — Covered**: buyer states a specific range — "we've got
  somewhere between $30-45K set aside for this kind of tooling this
  year."
- **Authority — the trap, should be Partial not Covered**: buyer is
  titled "Director of Operations" and speaks with confidence about the
  decision, but the only concrete statement about sign-off is "anything
  over $25K needs our managing partner's approval." A shallow run scores
  Authority Covered from the title or confident tone alone; the buyer
  themselves is not the final approver above that threshold, and this
  deal is likely to cross it.
- **Need — Covered**: buyer names a specific, quantified problem —
  associates spending "roughly 15 hours a week" manually cross-referencing
  documents, "time we could bill instead."
- **Timeline — Partial**: buyer says they'd like something "in place
  before the next big case cycle starts," without naming a specific date
  or what triggers that cycle.

## The trap a weak run fails

Scoring Authority Covered because the buyer holds a director title and
speaks confidently throughout the call, when the buyer's own words name a
$25K approval threshold this deal will likely cross, with a managing
partner as the real approver above it — should be Partial, not Covered.

## Not present: reporting any of these is a hallucination

- No specific date is named for "the next big case cycle" — no exact
  date should be invented.
- No name is given for the managing partner — no name should be
  invented.
- No competitor or alternative vendor is mentioned anywhere on the call.
