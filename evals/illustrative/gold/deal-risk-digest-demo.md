# Gold label: deal-risk-digest-demo.csv, scored against `deal-risk-digest`

Computed by hand from `references/rubric.md`'s exact point system and
`evals/illustrative/BRIEF-deal-risk-digest.md`'s construction, against
today = 2026-08-17. This rubric is deterministic — every cell below is a
fact, not a judgment call, unlike the transcript-audit gold files.

## Expected ranked table (highest risk first, ties broken by deal value)

| Rank | Deal | Points | Tier | Value | Signals (evidence) |
|---|---|---|---|---|---|
| 1 | Redstone Facilities Group | 6 | High | 61,000 | close_date=2026-06-01 (past), probability=30% (past-due+unlikely); stage_entered_date=2026-04-01 (~138 days, stage age); next_step=(empty) (blank); contacts="Owen Falk" (single) |
| 2 | Milltown Cold Storage | 3 | High | 38,000 | close_date=2026-07-01 (past), probability=35% (past-due+unlikely only) |
| 3 | Thistlebrook Energy | 2 | Medium | 67,000 | next_step="TBD" (vague); contacts=(empty) (single-threaded — no contact at all) |
| 4 | Bramblewood Retail | 2 | Medium | 51,000 | stage_entered_date=2026-07-01 (~47 days, stage age); next_step="Follow up" (vague) |
| 5 | Palisade Home Services | 2 | Medium | 40,000 | next_step=(empty) (blank); contacts="Rosalind Kemp" (single) |
| 6 | Northgate Utilities | 1 | Medium | 22,000 | stage_entered_date=2026-06-01 (~77 days, stage age) |
| 7 | Harborline Manufacturing | 0 | Low | 72,000 | none |
| 8 | Cinderpine Analytics | 0 | Low | 45,000 | none |
| 9 | Ashworth Legal Partners | 0 | Low | 29,000 | none — close_date=2026-05-15 is past, but probability=78% so past-due+unlikely does NOT trigger |

Closing lines expected: **"2 of 9 deals rated High risk"**, and the single
most common signal across the 6 High+Medium deals is **blank/vague next
step** (4 of 6: Redstone, Bramblewood, Thistlebrook, Palisade) — ahead of
stage age (3: Redstone, Bramblewood, Northgate) and single-threaded
contact (3: Redstone, Palisade, Thistlebrook).

## The traps (findings a correct run must get right)

1. **Ashworth must NOT be flagged High or Medium from its past close
   date alone.** `probability=78%` means the past-due-and-unlikely signal
   requires *both* conditions and doesn't fire — the rubric calls this
   "stale-but-fine." Flagging Ashworth on date alone is the single most
   important trap in this sheet.
2. **Bramblewood's low probability (22%) + future close date must NOT
   trigger past-due-and-unlikely** — the rubric calls this "just early
   pipeline." Its 2 points must come only from stage age + vague next
   step, not from the probability/date pair.
3. **Thistlebrook's empty contacts cell counts as single-threaded**, not
   as a missing-column skip — the `contacts` column exists and has data
   in other rows, so an empty cell in one row is a real "no contact
   listed" signal, not grounds to skip the whole signal.
4. **The three-way 2-point tie (Thistlebrook, Bramblewood, Palisade)**
   must sort by deal value descending: 67,000 > 51,000 > 40,000.
5. **Milltown must reach High at exactly 3 points** with no other signal
   present — confirms the boundary (High = 3+) is applied correctly, not
   requiring a second signal to "confirm" it.

## Not present: reporting any of these is a hallucination

- Any risk signal on Harborline, Cinderpine, or Ashworth beyond what's
  listed (all three are clean/trap rows scoring 0).
- A sixth risk signal, or a different point value for any signal, than
  what `references/rubric.md` defines (3 / 1 / 1 / 1, tiebreak-only for
  value).
- Any inferred contact name, next-step content, or date not present in
  the CSV cell.
- A claim that any column was missing from the export — every column
  used by the rubric is present in this sheet.
