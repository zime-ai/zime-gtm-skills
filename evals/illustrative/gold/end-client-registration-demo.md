# Gold label: end-client-registration-demo.csv, scored against `end-client-registration`

Computed by hand from `references/rubric.md`'s seven dimensions, against
today = 2026-08-17. This rubric is deterministic — every dimension assessment
below is a fact, not a judgment call, matching the skill's deterministic
checklist.

## Expected flagged registrations (flagged ones first)

| Registration | Dimensions Flagged | Evidence | Suggested action |
|---|---|---|---|
| REG-102 | 1 (Partner identity) | partner_contact = (empty) | Add partner contact name |
| REG-103 | 2 (End-client distinct) | end_client_name = "Northlake Partners" (same as partner_name, conflated) | Correct end-client name; this is the partner's own registration of itself |
| REG-104 | 4 (Conflict check) | conflict_check_done = "Yes - existing direct AE has an active opportunity with Echo Inc" (real conflict found) | Do not accept; direct sales owns this account |
| REG-105 | 5 (Contact + permission) | end_client_contact = "Dev Chandra", permission_confirmed = "No response yet - contact not confirmed" (permission not Yes) | Confirm contact before accepting |
| REG-106 | 3 (Engagement scope) | engagement_scope = "General support" (vague, no specific sourcing/implementation/referral credit stated) | Clarify which services partner is credited for |
| REG-107 | 4, 6 (Conflict check + commercial terms) | conflict_check_done = (empty), margin_tier = (empty) | Run conflict check; record margin tier and deal type |
| REG-108 | 7 (Registration expiry) | expiry_date = (empty) | Set registration validity window |
| REG-100 | None | All dimensions met | Accept |
| REG-101 | None | All dimensions met | Accept |
| REG-109 | None | expiry_date = "2026-08-18" (tomorrow, future-dated and present) — boundary case, but valid | Accept |

## The traps (findings a correct run must get right)

1. **REG-103: end_client_name conflated with partner_name.** The
   registration lists "Northlake Partners" as both the partner and the
   end-client entity — a clear flag for Dimension 2 (entity distinct). A
   skill that treats this as a legitimate registration, or misses the
   conflation, fails on the repo's own sample-data trap.

2. **REG-104: conflict check returned a real conflict, not a missing check.**
   The `conflict_check_done` column states the check *was* done and *found*
   an existing direct AE with an active opportunity on Echo Inc. This is not
   a Dimension 4 flag for "conflict check was not done" — the check was
   done. The flag is for "conflict exists." Flagging REG-104 correctly means
   reading the status message, not scanning for empty/Yes/No only.

3. **REG-107: multiple independent flags, not one compound flag.** This
   registration has `conflict_check_done = (empty)` *and*
   `margin_tier = (empty)`. These trigger two separate dimensions (Dimension
   4 and Dimension 6), not one "incomplete registration" bucket. A correct
   run flags both.

4. **REG-109: expiry_date is tomorrow, but valid.** The registration
   `expiry_date = "2026-08-18"` is extremely soon (one day from the
   reference date 2026-08-17), but it is present and future-dated. Dimension
   7 asks "Does the registration have a defined validity window... or is it
   open-ended with no forcing function?" This row is not open-ended; it has
   a window. It should not be flagged. The skill is not responsible for
   warning about near-expiry (that's a different concern); it only checks
   that a window exists.

5. **REG-102 vs. REG-103: two related but distinct flags on Northlake
   Partners registrations.** REG-102 flags for missing `partner_contact`
   (Dimension 1). REG-103 flags for conflated end-client name (Dimension 2).
   Both are Northlake Partners, but the flags are in different dimensions
   and require independent evidence from the CSV.

## Not present: reporting any of these is a hallucination

- A flag on REG-100, REG-101, or REG-109 (all three are clean).
- A claim that REG-104's conflict check was not done (the column states it
  was; the check revealed a conflict).
- A claim that REG-109 is flagged for near-expiry (Dimension 7 only requires
  the window to exist, not to be far in the future).
- Any other dimension being flagged on any registration than what's listed
  in the table above.
- Suggested actions that infer content not in the CSV (e.g., inventing a
  partner contact name for REG-102, or assuming a conflict exists on a
  registration without evidence from the `conflict_check_done` cell).
- A different number of flagged registrations than 7 of 10.
- A most common flag dimension different than Dimension 4 (Conflict check),
  which appears on 2 of the 7 flagged registrations (REG-104 and REG-107).

## Closing lines expected

- **"7 of 10 registrations flagged"**
- **The single most common flag dimension is Dimension 4 (Conflict check),
  appearing on 2 flagged registrations** (REG-104: conflict found; REG-107:
  conflict check not done).
