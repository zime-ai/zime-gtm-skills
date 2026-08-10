# Negotiation pipeline check — rubric

Applies to every row in scope after the Step 3 stage filter. Each check
returns **Flagged**, **Clean**, or **Unknown (column missing)**. A flag
without a cited column + cell value does not ship.

## Column synonyms

Match case-insensitively, ignoring `_`/`-`/space differences.

| Concept | Accepted headers |
|---|---|
| Deal name | `deal`, `deal_name`, `dealname`, `opportunity`, `opportunity_name`, `name` |
| Stage | `stage`, `deal_stage`, `dealstage`, `pipeline_stage` |
| Contact role | `contact_role`, `role`, `contact_title`, `title` (one row per contact, or a semicolon-separated list of roles on the deal row) |
| Paper/contract status | `paper_status`, `contract_status`, `redline_status`, `msa_status`, `paper` |
| Discount | `discount`, `discount_pct`, `discount_percent`, `discount_%` |
| Approval | `approver`, `approval`, `discount_approver`, `discount_approval` |
| Close date | `close_date`, `expected_close`, `expected_close_date`, `closedate` |
| Original/prior close date | `original_close_date`, `orig_close_date`, `first_close_date` |
| Close plan | `close_plan`, `mutual_action_plan`, `map`, `mutual_close_plan` |
| Signer | `signer`, `signer_role`, `signatory`, `signature_contact` |

If a concept has no matching column anywhere in the export, every check
that needs it reports **Unknown (column missing)** for all in-scope rows —
say so once, up front.

## Stage match (Step 3)

Fuzzy-match the stage column against: `negotiation`, `negotiating`,
`contract`, `contract review`, `legal review`, `redlines`, `redlining`.
Case-insensitive substring match is sufficient.

## The six checks

**1. No legal or procurement contact** — Flagged if no contact on the deal
carries a role matching `legal`, `procurement`, or `finance` (substring,
case-insensitive) anywhere in the contact-role data. Cite the contact role
column and its value (or `(empty)`).

**2. Paper process not started** — Flagged if the paper/contract status
column is empty, or set to a not-started value (`not started`, `n/a`,
`none`, `pending`, `-`, `tbd`). Cite the column and value.

**3. Discount without approval** — Compute the median discount percentage
across all in-scope (negotiation-stage) rows that have a non-empty discount
value. Flagged if a row's discount is above that median **and** the
approval/approver column is empty. Cite both the discount value, the
computed median, and the empty approver cell. Never hardcode a discount
ceiling — always derive it from the export.

**4. Close date already slipped** — Flagged if (a) an original/prior close
date column exists and differs from the current close date (the date was
pushed), or (b) no such column exists but the close date is in the past
relative to today while the deal is still in negotiation. Cite the close
date value (and original close date, if present).

**5. No mutual close plan** — Flagged if the close-plan/mutual-action-plan
column is empty. Cite the column and `(empty)`.

**6. Signature path unnamed** — Flagged if no contact is marked as signer
(signer/signatory field empty, or no contact's role matches `signer`).
Cite the column and value.

## Reads-well-too check

`assets/sample-pipeline-negotiation-pipeline-check.csv` must contain at
least two deals that come back fully Clean across all six checks when run
through this rubric. A rubric that flags everything is useless — verify
this before shipping any change to the sample or the checks.
