# Gold label: prospect-pipeline-check-demo.csv, scored against `prospect-pipeline-check`

Computed by hand from `references/rubric.md`'s six engagement-gate checks, against
today = 2026-08-17. The rubric is deterministic — every flag below is a fact, not
a judgment call, based on the exact column values and the computed median created_date
age (25.5 days, so 1.5x = 38.25 days threshold).

## Expected flagged table (flagged deals first, most flags first; then clean rows)

| Deal | Flags | Evidence | Suggested action |
|---|---|---|---|
| StaleVenture Corp | 5 | aged+no-activity (created_date=2026-05-15, 94 days old, last_activity=2026-05-16 same day), no-two-way-engagement (prospect_replied=No, meetings_held=0, no inbound), no-meeting-held (meetings_held=0), single-contact-unresponsive (contacts="David Foster" single, prospect_replied=No), close-date-past (close_date=2026-08-10) | Remove from pipeline |
| NoEngagementVenture | 3 | no-two-way-engagement (prospect_replied=No, meetings_held=0), no-meeting-held (meetings_held=0), aged+no-activity (created_date=2026-07-05, 43 days, last_activity=2026-07-06 same day) | Investigate or close |
| CrossStateServices | 1 | close-date-past (close_date=2026-08-10, but deal is actively engaged: prospect_replied=Yes, meeting held) | Follow up immediately despite past close date |
| AgedOnceActive | 1 | aged+no-activity (created_date=2026-06-19, 59 days old, last_activity=2026-06-20 same day) | Activate or close |
| PlaceholderDeal LLC | 1 | placeholder-deal (deal_value empty — no estimated value assigned) | Estimate deal value |
| TechStartup Inc | 0 | none | no action |
| RetailBrand Ltd | 0 | none | no action |
| SingleReply Inc | 0 | none (single contact Elena Reyes but prospect_replied=Yes — single-contact-unresponsive does NOT fire) | no action |

Closing lines expected: **"5 of 8 deals in Prospect pipeline flagged"** and **"aged with no activity"** is
the single most common flag (appears on StaleVenture, AgedOnceActive, and NoEngagementVenture = 3 of 5 flagged).

## The traps (findings a correct run must get right)

1. **CrossStateServices: close date is past, but deal must NOT be flagged on engagement.** 
   close_date=2026-08-10 is before today, BUT prospect_replied=Yes and there is a completed
   meeting. The deal has real two-way engagement. It should flag ONLY on "close-date-past",
   not on any of the six engagement checks. A run that flags this on "no engagement" or "single-threaded"
   misunderstands the rubric.

2. **SingleReply Inc: single contact, but has replied.** contacts="Elena Reyes" (single), but
   prospect_replied=Yes. Per rubric, "single-threaded + unresponsive" requires BOTH conditions:
   single contact AND no reply. This contact did reply. Must NOT be flagged on
   "single-contact-unresponsive". A run that flags this is the single most important trap
   in this sheet.

3. **AgedOnceActive is flagged ONLY on aged+no-activity, not engagement.** created_date=2026-06-19
   (59 days, past 1.5x median of 25.5), last_activity=2026-06-20 (1 day after, indicating
   no subsequent engagement). However, this deal HAS a completed meeting (meetings_held=1)
   and two contacts, so it should NOT flag on "no-two-way-engagement" or "no-meeting-held"
   or "single-contact". It flags only on "aged+no-activity". A run that flags this on
   engagement checks has misapplied the aged-check boundary or the engagement logic.

4. **PlaceholderDeal LLC has empty deal_value.** The placeholder check flags on:
   value is empty/zero OR round-number value repeated across same rep. This row has empty
   value (no deal size estimated), so it flags. But the deal itself has good engagement
   (two contacts, reply, meeting), so the reads-well-too check should NOT override the
   placeholder flag — a deal with no estimated value is genuinely incomplete, not
   falsely flagged.

5. **The aged+no-activity boundary (1.5x median) is at exactly 38.25 days.** StaleVenture
   (94 days) and NoEngagementVenture (43 days) both clearly exceed it. AgedOnceActive
   (59 days) is well past it. The threshold must be computed per-run, not hardcoded
   — if a run hardcodes 45 days or 60 days, all three will misfire.

## Not present: reporting any of these is a hallucination

- Any flag on TechStartup, RetailBrand, or SingleReply (all three are clean).
- A flag on CrossStateServices other than "close-date-past" (engagement is real).
- A flag on AgedOnceActive for "no-meeting-held" or "no-two-way-engagement" (it has
  a meeting and 2 contacts).
- A claim that any column was missing from the export — every column used by the rubric
  is present in this sheet.
- Any inferred or guessed contact name, meeting outcome, or date not present in the CSV.
- A seventh check type, or a flag name not listed in the rubric's six checks.
