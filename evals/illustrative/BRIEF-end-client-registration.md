# Brief: end-client-registration-demo CSV

Same discipline as the `deal-risk-digest` brief: decide the row roster and
each row's intended flags *before* writing values into the sheet, per
`references/rubric.md`'s seven dimensions (partner identity, end-client
distinct, engagement scope, conflict check, contact + permission, commercial
terms, registration expiry).

Reference date for every relative date below: **2026-08-17** (the date this
brief was authored).

## Deliberate construction (per row, decided before the sheet)

- **Rows 1-2 — clean, must pass all seven dimensions**: partner and partner
  contact both named and distinct; end client clearly named (not conflated
  with partner); scope specific (sourced the lead, technical implementation,
  etc., not vague); conflict check done and clear result stated; named
  end-client contact with confirmed permission; margin or discount tier +
  deal type recorded; expiry date future-dated and present.

- **Row 3 — partner_contact missing, single flag (Dimension 1)**: flagged
  for missing partner contact name; all other dimensions clean. Tests that
  partner identity requires *both* organization *and* person.

- **Row 4 — trap: end_client_name conflated with partner_name (Dimension
  2)**. The sample data (REG-1003) shows the partner filing a registration
  where the end-client field contains the partner's own name — a flag that
  signals the registration is unclean at the outset. This row intentionally
  repeats that pattern to confirm the skill catches it as a Dimension 2
  (entity-distinct) violation, not a partner-identity or conflict issue.

- **Row 5 — trap: conflict check done but reveals active house conflict
  (Dimension 4)**. The sample data (REG-1008) shows `conflict_check_done`
  stating "Yes - existing house AE has an active opportunity with this
  account" — a check *was* done and it *revealed* a conflict. This is not a
  missing-check flag; it's evidence of a real conflict that should block
  registration. The rubric (Dimension 4) says "Was the end client actually
  checked ... before the registration was accepted" — this row shows the
  check happened and found a problem, so it flags for the conflict finding
  itself, not for a missing check.

- **Row 6 — permission not confirmed, single flag (Dimension 5)**: the
  `permission_confirmed` column states the contact exists but says something
  like "No response yet" or "Declined" instead of "Yes". Tests that
  confirmation is explicit, not assumed.

- **Row 7 — engagement_scope vague, single flag (Dimension 3)**: the scope
  column contains something generic like "General support" or "TBD" rather
  than specific credit lines. Tests that scope must be specific enough to
  avoid later disputes.

- **Row 8 — commercial terms incomplete, single flag (Dimension 6)**: either
  margin_tier or deal_type (or both) left blank. Tests that both parts of
  commercial terms (the discount/margin *and* whether it's referral or
  resell) must be recorded.

- **Row 9 — registration expiry missing, single flag (Dimension 7)**: all
  other dimensions clean, but `expiry_date` is blank. Tests that the
  registration must have a defined validity window.

- **Row 10 — clean but boundary-condition row**: registration is valid but
  expiry_date is tomorrow (2026-08-18) — tests that an expiry_date
  technically present and future counts as passing Dimension 7, even if it's
  very soon (not the skill's job to warn about near-expiry, only whether it
  exists).

## Expected final flagging (computed from the rubric, not guessed)

| Registration | Dimensions Flagged | Evidence |
|---|---|---|
| Vestor Analytics | None | All seven dimensions met |
| Granite Solutions | None | All seven dimensions met |
| Northlake Partners | 1 (partner_contact missing) | partner_contact = (empty) |
| Northlake Partners (Echo Inc) | 2 (end_client distinct) | end_client_name = "Northlake Partners" (same as partner_name) |
| Clearline Tech | 4 (conflict found) | conflict_check_done = "Yes - existing direct opportunity with Echo Inc" |
| Watershed Equity | 5 (permission) | permission_confirmed = "No response yet" |
| Axis Capital | 3 (scope vague) | engagement_scope = "General support" |
| Pinnacle Advisory | 6 (commercial terms) | margin_tier = (empty), deal_type = (empty) |
| Meridian Group | 7 (expiry missing) | expiry_date = (empty) |
| Fieldstone Advisors | None | expiry_date = 2026-08-18 (tomorrow, but present and future) |

Closing lines expected: **"6 of 10 registrations flagged"**, and the single
most common flag dimension across the 6 flagged registrations is **Dimension
7 (missing expiry)** appearing on 2 registrations — actually, wait, let me
recount: Northlake (1x row 3), Northlake Echo (1x row 4), Clearline (1x row
5), Watershed (1x row 6), Axis (1x row 7), Pinnacle (1x row 8), Meridian
(1x row 9) — that's 7 registrations with flags, not 6. Let me adjust.

Actually, re-reading the expected output structure: the skill outputs one
markdown table with flagged registrations first. So the closing "N of M
registrations flagged" counts unique registrations that have at least one
flag, not the count of flags.

Let me recalculate: rows 3, 4, 5, 6, 7, 8, 9 all have flags = 7 flagged
registrations out of 10 total. Closing line should be "7 of 10 registrations
flagged."

The single most common flag dimension: I need to count across the 7 flagged
ones:
- Dimension 1 (partner identity): 1 (row 3)
- Dimension 2 (entity distinct): 1 (row 4)
- Dimension 3 (engagement scope): 1 (row 7)
- Dimension 4 (conflict check): 1 (row 5)
- Dimension 5 (permission): 1 (row 6)
- Dimension 6 (commercial terms): 1 (row 8)
- Dimension 7 (expiry): 1 (row 9)

They're all tied at 1 each. Hmm, that's not as interesting as the
deal-risk-digest traps which had a clear winner. Let me restructure to have
some registrations with *multiple* flags so that one dimension shows up more
frequently.

Let me revise the construction:
- Rows 1-2: clean
- Row 3: Dimensions 1 + 2 (missing partner_contact AND end_client conflated)
- Row 4: Dimension 2 only (end_client = partner_name)
- Row 5: Dimension 4 only (conflict found)
- Row 6: Dimension 5 only (permission not confirmed)
- Row 7: Dimensions 3 + 7 (vague scope AND missing expiry)
- Row 8: Dimension 6 only (missing commercial terms)
- Row 9: trap (multiple missing fields but actually a different interpretation)
- Row 10: clean + boundary

Actually, let me simplify and make it match the brief better. I'll have:
- 2 clean
- 5 rows with various single flags
- 2 rows with multiple flags (to make one dimension appear more)
- 1 trap row

Wait, that's 10 rows. Let me think about which dimensions to emphasize. Looking at the sample data, the most common issues seem to be:
- Missing end_client_contact
- Missing permission_confirmed
- Missing expiry_date

Let me revise to have multiple registrations missing expiry_date as a way to highlight that dimension:

- Rows 1-2: clean (all 7 dimensions met)
- Row 3: Dimension 1 (partner_contact missing)
- Row 4: Dimension 2 (end_client = partner_name)
- Row 5: Dimension 4 (conflict check reveals conflict)
- Row 6: Dimension 5 (permission not confirmed)
- Row 7: Dimension 3 (engagement_scope vague)
- Row 8: Dimension 6 (commercial terms missing)
- Row 9: Dimension 7 (expiry_date missing) -- first missing expiry
- Row 10: Dimension 7 (expiry_date missing) -- second missing expiry, trap: but everything else looks clean

Most common flag: Dimension 7 appears on 2 registrations (rows 9-10) while all others appear once.

Actually, I realize I should check the skill's actual output format by running it on the sample first. Let me continue with the structure and then adjust after the run.
