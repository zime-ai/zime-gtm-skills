# Brief: mutual-action-plan-demo transcript

Same caveat as every other run in this batch (`evals/illustrative/README.md`):
same-author brief/gold/grading, not Tier 3. This is Shape C
(document-writer) — gold is a **reference milestone plan**, graded by
row-by-row diff against the skill's own three-part test (action, date,
two-sided owner), not by findings recall.

## Situation

One late-stage call: a mid-market logistics company ("Harrow Freight")
buying a route-optimization platform, talking to their VP Ops.

## Deliberate construction

- **Milestone 1 (full `heard`)**: rep and VP agree the rep will send a
  security questionnaire by Friday, VP names her IT lead (Priya Okafor) as
  the one who'll complete it. Action + date + two-sided owner, all stated
  — must tag `heard`.
- **Milestone 2 (the trap — looks concrete, is actually `inferred`)**: VP
  says "I'll get budget sign-off moving" — a specific action, but **no
  date and no named owner on her side beyond herself, and she never says
  when**. A shallow run tags this `heard` because it sounds like a real
  commitment; the three-part test requires a date or concrete trigger,
  which this line never has ("moving" is not a trigger).
- **Milestone 3 (`inferred`, correctly missing an element)**: rep proposes
  a demo for the wider team "sometime next month" — vague date, no named
  prospect-side owner — must tag `inferred`, naming the missing date
  precision and owner.
- **Milestone 4 (`heard`)**: contract redlines — VP commits to looping in
  procurement (names "our procurement lead, Sam") by "end of next week,"
  rep commits to sending the redlined MSA by Wednesday. Both sides,
  specific dates — `heard`.

## The trap a weak run fails

Milestone 2 ("I'll get budget sign-off moving") must be tagged
`inferred`, not `heard` — it has a named action and an implicit owner
(the VP herself) but no date or checkable trigger. Tagging it `heard`
overstates how locked-down the plan actually is.

## Not present: reporting any of these is a hallucination

- No specific dollar figure or contract term is stated anywhere on the
  call — none should appear in the plan.
- No third buyer-side contact beyond the VP, Priya Okafor, and Sam (named
  only as procurement lead, no surname given) — no other name should
  appear.
- The plan should not be all-`inferred` — two milestones (1 and 4) are
  genuinely `heard`, so the all-inferred call-out does not apply here.
