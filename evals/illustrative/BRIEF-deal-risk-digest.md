# Brief: deal-risk-digest-demo CSV

Same discipline as the transcript briefs, adapted for a CSV: decide the
row roster and each row's intended score *before* writing values into the
sheet, per `references/rubric.md`'s exact five-signal point system (a
deterministic rubric, unlike the transcript-audit skills — this lets the
gold file be exact rather than judgment-based).

Reference date for every relative date below: **2026-08-17** (the date
this brief was authored). Reproducing this run on a much later date could
shift a boundary row (e.g. Row 7's stage-age signal) across the 45-day
line — a known limitation shared with the skill's own existing
`assets/sample-pipeline-deal-risk.csv`.

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, must score Low (0 pts)**: the rubric's own
  "reads-well-too" check requires at least two such rows in any sample —
  future close, confident probability, recent stage entry, a specific
  next step, 2+ contacts.
- **Row 3 — High, maximum signal (6 pts)**: past-due + low probability
  (3), stage age (1), blank next step (1), single contact (1). The
  clearest possible High.
- **Row 4 — High, minimal boundary (exactly 3 pts)**: past-due + low
  probability only, nothing else — tests that 3 points alone crosses into
  High without needing any other signal.
- **Row 5 — trap: past close date, high probability.** The rubric is
  explicit that past-due-and-unlikely needs *both* conditions — a stale
  date with a confident probability is "stale-but-fine," not risk. Score
  should be 0 (Low). A skill that flags this High because the date alone
  looks bad fails a rule stated directly in its own rubric.
- **Row 6 — trap: low probability, future close date.** The rubric calls
  this "just early pipeline," not risk on its own. Combined with an
  incidental stage-age hit and a vague next step it should land Medium
  (2 pts) from those two signals alone — not from the probability/date
  pair.
- **Row 7 — stage age only (1 pt)**: everything else clean, isolates the
  stage-age signal.
- **Rows 8-9 — three-way point tie test**: Rows 6, 8, and 9 all land at
  exactly 2 points through different signal combinations. Deal values are
  set so the correct sort order (higher value first among equal points) is
  Row 9 (67,000) > Row 6 (51,000) > Row 8 (40,000) — the rubric's
  tiebreak rule, tested across three tied rows, not just two.
- **Row 9 also tests the empty-contacts edge case**: an empty contacts
  cell counts as single-threaded ("one name or none at all"), not as a
  missing-column skip (the column exists, this one cell is blank).

## Expected final scoring (computed by hand from the rubric, not guessed)

| Deal | Points | Tier | Value | Signals |
|---|---|---|---|---|
| Redstone Facilities Group | 6 | High | 61,000 | past-due+unlikely, stage age, blank next step, single contact |
| Milltown Cold Storage | 3 | High | 38,000 | past-due+unlikely only |
| Thistlebrook Energy | 2 | Medium | 67,000 | vague next step ("TBD"), single/empty contact |
| Bramblewood Retail | 2 | Medium | 51,000 | stage age, vague next step ("Follow up") |
| Palisade Home Services | 2 | Medium | 40,000 | blank next step, single contact |
| Northgate Utilities | 1 | Medium | 22,000 | stage age only |
| Harborline Manufacturing | 0 | Low | 72,000 | none (clean) |
| Cinderpine Analytics | 0 | Low | 45,000 | none (clean) |
| Ashworth Legal Partners | 0 | Low | 29,000 | none — trap row, past close date but 78% probability |

Closing lines: **2 of 9 deals rated High risk.** Most common signal across
the 6 flagged (High+Medium) deals: **blank/vague next step**, appearing on
4 of them (Redstone, Bramblewood, Thistlebrook, Palisade) — ahead of
stage age (3) and single-threaded contact (3).
