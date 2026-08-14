# Brief: meddicc-demo transcript

Written before the transcript, per `evals/gold/BRIEFS.md`'s own discipline
(persona/situation first, rubric second) — see `evals/illustrative/README.md`
for the honesty caveat this doesn't fully satisfy (same author holds
MEDDICC's general shape in memory already; this is best-effort blinding,
not real blinding).

## Situation

Mid-market logistics company ("Fernway Freight," fictional), ~300
employees. Second call between an AE and the VP of Operations, after a
first call where the AE demoed a route-optimization / dispatch platform.
Trigger for this call: the VP's team missed an on-time-delivery SLA with a
large retail customer last month, and leadership is now paying attention.

## Deliberate construction (by rubric dimension, decided before writing)

- **Real pain outside any MEDDICC bucket**: the VP mentions, almost in
  passing, that half their dispatchers are close to retirement and nobody
  junior wants to learn the current paper-based routing process — a
  knowledge-transfer/succession risk, not a metric, not economic buyer,
  not decision criteria. MEDDICC has no bucket for "we're about to lose
  institutional knowledge."
- **Dimension that legitimately doesn't apply**: Competition. This is a
  second call after an inbound trigger; the VP has not mentioned evaluating
  anyone else, and nothing in the call implies a competitive process
  exists yet. Correct behavior is "Not applicable," not a forced guess.
- **Downplayed secondary signal**: the VP mentions budget almost as an
  aside — "we'd probably have to fight for headcount-adjacent budget, but
  if this pays for itself it's an easier conversation" — then immediately
  pivots back to the SLA miss. A weak read stops at "budget mentioned,
  Covered"; a stronger read notices this is a soft, unconfirmed budget
  signal the VP is actively downplaying relative to the operational pain.
- **Champion signal, ambiguous on purpose**: the VP says enthusiastic
  things ("this could actually fix our biggest headache") but takes no
  internal action on-call — no offer to loop in ops leadership, no
  mention of championing internally. A shallow read might call this
  Covered; the correct read (per `champion-tracker`'s own already-shipped
  distinction between sentiment and action) is Partial at best.
- **Metrics**: given cleanly — the SLA miss, a specific dollar penalty
  clause, and the target on-time percentage — should be an easy Covered.
- **Economic buyer**: ambiguous. The VP believes they can approve this
  under $50k but says anything larger needs the COO's sign-off, which
  hasn't been tested. Partial, not Covered.
- **Decision process / decision criteria**: thin. No named steps, no
  named evaluation criteria beyond "does it stop this from happening
  again." Missed or Partial, not Covered.
