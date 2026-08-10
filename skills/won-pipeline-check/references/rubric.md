# Won pipeline check rubric

Six flags, applied to every row whose stage fuzzy-matches "Won pipeline".
This is hygiene at the funnel exit, not a post-sale health read —
`onboarding-journey` and `customer-success` audit what happens after the
handoff; this rubric only asks whether the handoff has the data to happen.

## Stage match

Rows count as in scope if their stage column value is (case-insensitively)
`closed won`, `closed-won`, `won`, `closedwon`, or contains "won" as a
whole word alongside "closed". Anything else is out of scope, including
open Closed Lost or open-pipeline stages.

## Column synonyms

Match headers case-insensitively, ignoring `_`/`-`/space differences.

- **Stage**: `stage`, `deal stage`, `dealstage`, `opportunity stage`
- **Owner / CS owner**: `cs owner`, `post-sale owner`, `onboarding owner`,
  `csm`, `success owner`, `handoff owner`
- **Deal owner** (for the "no owner at all" half of check 6): `owner`,
  `deal owner`, `account owner`, `rep`, `sales owner`
- **Kickoff / start date**: `kickoff date`, `onboarding date`, `start date`,
  `kickoff`, `onboarding start`
- **Created date**: `created date`, `create date`, `deal created`,
  `created on`
- **Won date**: `won date`, `date won`, `closed won date`
- **Close date**: `close date`, `expected close`, `closedate`
- **Deal value**: `deal value`, `amount`, `opportunity value`, `deal size`
- **Contract value**: `contract value`, `signed value`, `final value`,
  `acv`, `tcv`
- **Contract term**: `contract term`, `term length`, `term`, `contract
  length`
- **Value reason** (why contract value differs from deal value):
  `value reason`, `variance reason`, `discount reason`, `reason`
- **Contract reference**: `contract id`, `order form id`, `order form`,
  `contract link`, `signed contract`, `agreement id`
- **Probability / forecast category**: `probability`, `forecast category`,
  `forecast`, `win probability`

If a column a check depends on is entirely absent from the export, that
check reports **Unknown (column missing)** for every row — state this once,
up front, and never infer the value from another column.

## 1. No CS or onboarding owner

Flagged if the CS/onboarding-owner field is empty or missing for a
closed-won row. Evidence: `cs_owner = (empty)`.

## 2. No onboarding or kickoff date

Flagged if the kickoff/start-date field is empty on a deal marked
closed-won. Evidence: `kickoff_date = (empty)`.

## 3. No signed value or term

Flagged if the contract value or contract term/length field is empty, OR
the contract value differs from the deal value with no value-reason field
populated. Evidence cites whichever cell(s) triggered it, e.g.
`contract_value = (empty)` or `contract_value = 42000, deal_value = 50000,
value_reason = (empty)`.

## 4. Date inconsistency

Flagged if any of: won date is before the deal's own created date, won date
is in the future (after today), or close date and won date disagree (and
both are present). Evidence cites the two conflicting cells, e.g.
`won_date = 2025-01-05, created_date = 2025-03-01`.

## 5. No signed-contract reference

Flagged if the contract/order-form ID or link field is empty. Evidence:
`contract_id = (empty)`.

## 6. Orphaned record

Flagged if there is no deal owner at all, OR the row's stage is Closed Won
while its probability/forecast-category column still holds an open-pipeline
value (e.g. a probability under 100%, or a forecast category like
"Pipeline", "Best Case", "Commit" rather than "Closed" / "Won"). Evidence
cites the conflicting cell, e.g. `probability = 60%` on a Closed Won row.

## Reads-well-too check

A won deal with a real owner, a kickoff date, a filled-in contract value
and term, consistent dates, a contract reference, and a forecast category
that reads "Closed"/"Won" should come back Clean across the board — not
picked apart for phrasing or minor formatting differences in otherwise
complete fields. The sample data must contain at least two such deals, and
running this skill against it must return them Clean. If a healthy-looking
deal is coming back flagged, the check is being applied too strictly —
loosen it before finalizing.
