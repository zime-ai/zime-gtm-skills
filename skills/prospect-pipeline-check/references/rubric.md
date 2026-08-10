# Prospect pipeline check rubric

Six flags, built for one question only: has a human on the prospect side
engaged with this deal at all. This is the earliest gate in the deal
lifecycle — it never asks about budget, buyer, or pain. A deal can pass
every check here and still fail `qualify-pipeline-check`'s later, deeper
pass.

## Column synonyms

Match headers case-insensitively, ignoring `_`/`-`/space differences.
Accepted synonyms per concept:

- **Stage** — `stage`, `deal_stage`, `dealstage`, `pipeline_stage`
- **Deal / opportunity name** — `deal`, `deal_name`, `opportunity`, `opportunity_name`, `name`
- **Owner** — `owner`, `deal_owner`, `rep`, `sales_rep`
- **Created date** — `created_date`, `created`, `create_date`, `date_created`
- **Last activity date** — `last_activity_date`, `last_activity`, `last_touch`, `last_engagement_date`
- **Close date** — `close_date`, `expected_close`, `expected_close_date`, `target_close`
- **Deal value / amount** — `amount`, `value`, `deal_value`, `deal_amount`
- **Contacts / contact count** — `contacts`, `contact_count`, `num_contacts`, `stakeholders`
- **Meetings held** — `meetings_held`, `meetings`, `meeting_count`
- **Meeting outcome** — `meeting_outcome`, `meeting_status`, `last_meeting_status`
- **Inbound/reply activity** — `replied`, `inbound_activity`, `prospect_replied`, `last_inbound_date`

If a column a check needs is absent, that check reports **Unknown (column
missing)** for every row — state this once up front, never infer the value
from another column.

## 1. No two-way engagement

Flagged if there is no logged reply, meeting, or inbound activity from the
prospect side — only rep-side outbound activity recorded. Uses the
inbound/reply activity and meetings columns together; if both are absent,
report Unknown.

## 2. No meeting held

Flagged if the meetings-held count is zero, or every logged meeting's
outcome is no-show or cancelled. A single completed meeting, regardless of
outcome content, clears this check.

## 3. Single-threaded and unresponsive

Flagged if the contact count is exactly one **and** that contact has no
recorded response (no reply, no inbound activity). A single contact who has
replied does not trigger this — single-threaded alone isn't the problem,
unresponsive is.

## 4. Aged with no activity

Compute the median created-date age (in days, from today) across all
in-scope prospect-stage rows. Flagged if a row's created-date age is
meaningfully older than that median (more than 1.5x it) **and** the
last-activity date is at or within a few days of the created date — i.e.
the deal has sat since creation with nothing happening.

## 5. Placeholder deal

Flagged if deal value is empty or zero, or if the value is a round-number
placeholder (e.g. `10000`, `50000`, `100000`) that repeats across several
other rows owned by the same rep — a sign the number was typed to satisfy a
required field, not estimated.

## 6. Close date already in the past

Flagged if the close date is before today's date while the deal still sits
in prospect stage.

## Reads-well-too check

A deal with a genuinely responsive prospect — logged replies, a completed
meeting, more than one engaged contact — should come back Clean across all
six checks. If a deal like that still gets flagged, the rubric is reading
too strictly; loosen it before finalizing. The sample data in `assets/`
must contain at least two such deals, and running this skill against it
must return them Clean.
