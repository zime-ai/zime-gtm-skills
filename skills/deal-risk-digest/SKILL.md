---
name: deal-risk-digest
description: Reads a pipeline export (a whole book of business, not one call) and ranks deals by risk — a past-due close date paired with low probability, stage age, a blank or vague next step, and a single-threaded contact, with deal value breaking ties — citing the column values behind each call. Use when a sales manager or RevOps person wants a ranked risk view across a whole pipeline before a forecast call or pipeline review, not a single-call audit.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: csv
---

# Deal Risk Digest

You are a pipeline-risk analyst. Your goal is to give a sales manager a
ranked, evidence-backed view of which deals in a whole book of business
actually need attention.

Reads a pipeline export and ranks every deal by risk, most at-risk first.
This is a manager-facing, cross-deal digest — it writes a ranked list
across a whole book of business, it does not grade a single call. There is
no transcript mode: this is a structural export read, not a call-quality
claim. Pair it with a per-call skill (e.g. `next-step-commitment`) when a
specific flagged deal needs that deeper read.

## When to use this

- A sales manager wants a ranked view of which deals need attention before
  a pipeline review or forecast call.
- Someone is prepping a forecast call and wants to know which committed
  deals are actually shaky, not just which are big.
- RevOps wants a repeatable risk pass across an entire export rather than
  reviewing deals one at a time.

## Before you start

- Run this end to end in one pass — note an ambiguous column and move on,
  don't stop to ask.
- If the export is empty or has no usable date/probability columns at all,
  say so plainly rather than forcing a ranking out of nothing.

## How to run it

```
claude "run deal-risk-digest on ./exports/pipeline.csv"
```

**Input.** A `.csv` deal/pipeline export. If the conversation has a
connector tool that can list opportunities/deals, use it instead and treat
the returned rows exactly like CSV rows — CSV is otherwise the path.

**Column detection.** Match headers case-insensitively, ignoring
`_`/`-`/space differences, and accept the synonyms listed in
`references/rubric.md`. If a column a risk signal needs is entirely absent
from the export, skip that signal for every row — contributing zero
points, never inferred from another column — and state this once, up
front.

**Score each of the five risk signals in `references/rubric.md`** against
every row, using today's actual date for anything relative to "today."
Sum each row's points into a risk tier (High / Medium / Low).

**Evidence rule.** Every scored signal cites the column name and the
actual cell value behind it — e.g. `close_date = 2025-02-14 (past),
probability = 20%`, or `contacts = (empty)`. A signal with no cited cell
does not ship.

**Reads-well-too check.** Apply the check in `references/rubric.md` before
finalizing — a rubric that risks every deal is useless.

## Output

One markdown table, highest risk first (ties broken by larger deal value):

| Deal | Risk | Reasons | Evidence |

Then two closing lines:

- `N of M deals rated High risk`
- The single most common risk signal across them.

Nothing else — no invented risk scores beyond the point system in the
rubric, no percentages made up from nothing.

## Do not

- Don't read a call transcript — this is a structural, cross-deal export
  read, not a call-quality claim.
- Don't skip the reads-well-too check — a rubric that risks every deal is
  useless to a manager triaging a real pipeline.
- Don't invent a risk score beyond the point system in `references/rubric.md`.

## Related skills

- **`next-step-commitment`** — for a deeper, single-call read once this
  digest flags a specific deal worth investigating.
- **`prospect-pipeline-check`** / **`qualify-pipeline-check`** /
  **`evaluation-pipeline-check`** — for a stage-specific hygiene sweep
  rather than a cross-pipeline risk ranking.

## Sample data

`assets/sample-pipeline-deal-risk.csv` is a synthetic pipeline export —
run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
