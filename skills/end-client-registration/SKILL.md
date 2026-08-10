---
name: end-client-registration
description: Audits a partner/reseller's end-client deal registration for completeness — partner identity, end-client entity kept distinct from the partner, engagement scope, conflict check against the direct pipeline, confirmed permission to engage the end-client contact, commercial terms, and an expiry window. Use when reviewing a channel/partner deal registration export or a partner registration-review call, before accepting the registration into the partner pipeline. Distinct from `new-business-registration` (sibling skill), which audits a direct new-logo opportunity with no partner involved.
license: MIT
metadata:
  zime:category: new-business
  zime:dimension: stage
  zime:stage: registration
  zime:input-modes: csv,transcript
---

# End-Client Registration Audit

Audits whether a partner's end-client deal registration is complete and
clean enough to accept into the partner program's pipeline — not whether
the underlying deal itself is any good. CSV-first, since registration
exports are records, not calls; a transcript mode covers the registration
review conversation itself when one happened.

**No canonical framework caveat.** Deal/channel registration has no
canonical public framework the way BANT or MEDDPICC do. The checks in
`references/rubric.md` are built from general partner-program practice —
not from any named standard — and that's stated there explicitly rather
than implying one exists.

## When to use this

- A channel manager is reviewing a batch of incoming partner registrations
  before approving them into the pipeline.
- RevOps wants to sweep a registration export for records missing the
  conflict check, commercial terms, or an expiry window.
- A partner registration-review call just happened and someone wants a
  structured read on what was actually confirmed versus assumed.

## Modes

### CSV mode (`.csv`) — primary

```
claude "run end-client-registration on ./exports/registrations.csv"
```

For each registration row, check it against every dimension in
`references/rubric.md`. Match columns case-insensitively, ignoring
`_`/`-`/space differences (e.g. `partner_name`/`Partner Name`,
`end_client_name`/`End Client`, `conflict_check_done`/`Conflict Check`,
`margin_tier`/`Discount Tier`, `expiry_date`/`Protection End Date`). If a
column a check needs is entirely absent from the export, that check reports
**Unknown (column missing)** for every row rather than guessing.

Output one markdown table, flagged registrations first, ordered by most
flags first:

| Registration | Flags | Evidence | Suggested action |

Every flag cites the column name and the actual cell value that triggered
it (e.g. `conflict_check_done = (empty)` or `end_client_name = partner
name repeated`). A flag with no cited cell does not ship.

Close with two lines:

- `N of M registrations flagged`
- The single most common flag across the flagged registrations

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run end-client-registration on ./calls/registration-review.txt"
```

Read the transcript of a partner registration-review call, then score it
against each dimension in `references/rubric.md`. For every dimension:

- **Status** — Covered / Partial / Missed
- **Evidence** — a direct quote from the transcript, or mark **Unclear**
  rather than guess
- **Note** — one line, only if Partial or Missed

Close with a single **Approve / Approve pending the listed follow-ups / Do
not approve yet** call, and the one thing that would change your answer.

## Sample data

`assets/sample-registrations.csv` is a synthetic registration export with 8
rows — several deliberately triggering flags (a conflated partner/end-client
entity, a missing conflict check, an unconfirmed contact, missing
commercial terms, no expiry, a real conflict with an existing house
opportunity) and at least one genuinely clean registration. Run against it
first. `assets/sample-transcript.txt` is a synthetic partner
registration-review call for transcript mode.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file(s) you point it at and nothing else.
