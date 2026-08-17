# Brief: qualify-pipeline-check-demo CSV

Same discipline as deal-risk-digest: decide the row roster and each row's
intended flag set *before* writing values into the sheet, per
`references/rubric.md`'s exact six-flag system (a deterministic rubric
unlike the transcript-audit skills).

Reference date for every relative date below: **2026-08-17** (the date
this brief was authored). The procurement-timeline check compares close dates
against stated timelines per row, so this date matters only for sanity-checking
whether a timeline/close pair makes logical sense on the reference date.

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, must flag 0 checks**: all six fields present and
  credible (named buyer with role, specific pain, budget or deal value,
  close date at or after procurement timeline, clear next step, filled
  qualification score). Tests the rubric's reads-well-too requirement.
- **Row 3 — all six checks flagged**: empty on all six dimensions (no
  buyer, no pain, no budget+amount, no close_date, no next_step with
  status Active, no meddicc_score). The worst case.
- **Row 4 — trap: has deal value (amount) but no explicit budget field**.
  The rubric says budget signal flags only if *both* budget and amount are
  empty. This row should NOT flag on budget (flag #3) because amount=55000
  stands in. Tests that flag #3 understands the OR logic correctly.
- **Row 5 — trap: has pain and procurement timeline, but close date is
  sooner than timeline**. Should flag only on close-date/timeline mismatch
  (flag #4), not on pain itself. Tests that flag #4 is about the procurement
  cycle, not the presence of a timeline column.
- **Row 6 — no economic buyer (flag #1 only)**: buyer_name and buyer_role
  are both empty. Everything else clean.
- **Row 7 — no stated pain (flag #2 only)**: pain field is empty. Everything
  else clean.
- **Row 8 — close date sooner than procurement timeline (flag #4 only)**:
  close_date=2026-08-25 is before procurement_timeline=2026-09-15. Everything
  else clean. Tests the timeline comparison logic.
- **Row 9 — no next step while actively worked (flag #5 only)**:
  next_step is empty but status=Active. Should flag because Qualify-stage
  active deals must have a next step. Everything else clean.
- **Row 10 — no qualification record (flag #6 only)**: meddicc_score is empty.
  Everything else clean. Tests that the qualification-framework check applies
  only when the column exists and is empty on this row.

## Expected final flag counts (computed by hand from the rubric, not guessed)

| Deal | Flags | Flag numbers | Evidence |
|---|---|---|---|
| Tech Innovations Inc | 0 | none | clean |
| Global Logistics Solutions | 0 | none | clean |
| Phantom Startup | 6 | 1,2,3,4,5,6 | no buyer, no pain, no budget+amount, close_date 2026-08-20 before procurement_timeline 2026-09-15, no next_step, no meddicc_score |
| Strategic Partners Ltd | 0 | none | has amount (55000) so flag #3 does not trigger |
| Future Forward Consulting | 1 | 4 | close_date 2026-09-15 before procurement_timeline 2026-10-01 |
| Horizon Development Corp | 1 | 1 | buyer_name and buyer_role both empty |
| Nexus Technologies | 1 | 2 | pain field empty |
| Rapid Deployment Systems | 1 | 4 | close_date 2026-08-25 before procurement_timeline 2026-09-15 |
| Velocity Analytics Group | 1 | 5 | next_step empty while status=Active |
| Enterprise Solutions Partners | 1 | 6 | meddicc_score empty |

Closing lines expected: **7 of 10 deals in Qualify pipeline flagged.** The
single most common flag across the 7 flagged deals is **flag #4 (close date
inside procurement cycle)**, appearing on 3 of them (Phantom Startup, Future
Forward Consulting, Rapid Deployment Systems).
