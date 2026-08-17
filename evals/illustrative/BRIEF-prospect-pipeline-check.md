# Brief: prospect-pipeline-check-demo CSV

Same discipline as the deal-risk-digest brief: decide the row roster and each
row's intended flag status *before* writing values into the sheet, per
`references/rubric.md`'s six engagement-gate checks (deterministic, unlike
transcript audits — every flag is a fact, not a judgment call).

Reference date for every relative date below: **2026-08-17** (the date
this brief was authored). Reproducing this run on a different date could
shift boundary rows (e.g. Row 5's aged-with-no-activity signal) — a known
limitation shared with the skill's own existing `assets/sample-pipeline-prospect-pipeline-check.csv`.

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, must flag zero times**: responsive prospects with
  replies, meetings held, multiple contacts, future close dates. The
  rubric's "reads-well-too" check requires at least two such rows.
- **Row 3 — High flags, maximum signal (5 flags total)**: very old deal
  (94 days, 1.5x the median ~62 days), activity only at creation,
  single unresponsive contact, no meeting, no reply, close date past.
  Tests that a deal can stack multiple independent check failures.
- **Row 4 — trap: close date past but deal is recent and engaged**. Close
  date is 2026-08-10 (past), but deal was created on 2026-08-01, has a
  completed meeting, and prospect replied. Per the rubric, only the close
  date itself is past — the deal is actively engaged. Should flag ONLY on
  "close date in past", not on engagement checks.
- **Row 5 — aged with no activity, boundary case**. Created date is
  2026-06-14 (64 days ago, just past 1.5x median of 62), last activity
  2026-06-15 (one day after), rest of row is clean. Should flag ONLY on
  "aged with no activity", testing the 1.5x boundary applies correctly.
- **Row 6 — trap: single contact, but has replied**. Single contact (Elena
  Reyes) but prospect_replied = Yes. Per rubric, single-threaded + UNresponsive
  requires both: single contact AND no reply. This contact did reply. Should
  flag ONLY on engagement checks if any; single-contact-unresponsive must NOT
  fire.
- **Row 7 — placeholder deal value (round number)**: value is 50000 (a
  round-number placeholder), same rep (Alice Johnson) as rows 1 and 3 who
  also carry 50000. However, rows 1 and 3 are distinct accounts with real
  engagement, not same-account duplicates — Row 7 is the true placeholder
  (same rep, same value, different fake prospect). Should flag on
  "placeholder deal".
- **Row 8 — no two-way engagement (compound trap)**. No reply, no
  meetings, two contacts but neither responded. Should flag on "no
  two-way engagement" and possibly "aged with no activity" if old enough.
  Created 2026-07-05 (43 days, within range), last activity 2026-07-06
  — near creation, so DOES age-flag. Tests stacked flags from different roots.

## Expected final flagging (computed by hand from the rubric, not guessed)

| Deal | Flags | Reasons |
|---|---|---|
| TechStartup Inc | 0 (Clean) | Multiple contacts, replies, meeting held, recent, future close |
| RetailBrand Ltd | 0 (Clean) | Multiple contacts, replies, meetings held, recent, future close |
| StaleVenture Corp | 5 (Flagged) | aged+no-activity, no-two-way-engagement, no-meeting-held, single-contact-unresponsive, close-date-past |
| CrossStateServices | 1 (Flagged) | close-date-past only (trap: close date past but deal is actively engaged) |
| AgedOnceActive | 1 (Flagged) | aged+no-activity only (created 59 days ago, activity within 1 day, just past 1.5x median threshold) |
| SingleReply Inc | 0 (Clean) | Single contact but HAS replied — single-contact-unresponsive does NOT fire (trap) |
| PlaceholderDeal LLC | 1 (Flagged) | placeholder-deal (deal value is empty) |
| NoEngagementVenture | 3 (Flagged) | no-two-way-engagement, no-meeting-held, aged+no-activity |

Closing lines expected: **"5 of 8 deals in Prospect pipeline flagged"** and the
single most common flag across the 5 flagged deals is **"aged with no activity"**
(appears on StaleVenture, AgedOnceActive, NoEngagementVenture = 3 of 5 flagged).
