# Executive briefing rubric

## Column synonyms (CSV mode)

Match headers case-insensitively, ignoring `_`/`-`/space differences.

- **Deal name**: `deal name`, `deal`, `opportunity`, `opportunity name`,
  `account`, `account name`
- **Stage**: `stage`, `deal stage`, `dealstage`, `opportunity stage`
- **Deal value**: `deal value`, `amount`, `opportunity value`, `deal size`,
  `contract value`
- **Close date**: `close date`, `closedate`, `expected close`
- **Next step**: `next step`, `next steps`, `next action`
- **Contacts**: `contacts`, `stakeholders`, `champions`, `buying
  committee`, `contacts involved`. Names are separated by `;` or `,`.

If a column the brief needs is entirely absent from the file, state this
once, up front, and never infer the value from another column or from a
similar-looking deal.

## Deal snapshot: unstated value or close date

If the deal value or close date is genuinely never stated — not in the
transcript, not in a CSV column, not filled by combining both — the
snapshot says so explicitly (e.g. "deal value: not stated in the call or
the export"). Do not estimate one from deal size language ("a
six-figure deal"), from stage, or from a similar deal. A vague spoken
figure ("a six-figure deal") is not the same as a stated value — quote it
as a hedge, don't convert it into a number.

## What counts as a risk (section 3)

A risk earns a line only if it's specific to this deal and cited — a named
blocker, a named competitor still in play, a stakeholder change, a stalled
approval step. Generic risk language ("could always change their mind",
"budget could get cut") without a specific cited trigger does not ship.
1-3 risks typical; if the call or row genuinely surfaces none, say the deal
looks clean rather than padding to a count.

## The ask: heard vs. inferred

Reuses `mutual-action-plan`'s three-part test for what makes a commitment
real — the ask in this brief is that same test applied to a single
next-step, not a different standard.

1. **Specific action** — not "follow up," a named thing.
2. **Date or concrete trigger** — a calendar date, or an event with an
   obvious, checkable occurrence. "Soon" or "at some point" fails this
   element.
3. **Two-sided ownership** — someone on the account owns something too,
   not just the rep.

- **`heard`** — all three elements were actually stated on the call, or
  the CSV row itself carries all three (a `next_step` cell naming a
  specific action, plus a date/trigger and a two-sided owner from that
  same row or another column). Quote or cite it.
- **`inferred`** — the ask is reasonable given what was discussed, but one
  or more of the three elements wasn't actually stated or agreed — it's
  the rep's own proposal. Quote the closest thing said (or cite the
  closest column), name what's missing, and label it plainly as the rep's
  proposal, not a confirmed commitment.

A bare `next_step` cell (a phrase with no date and no named counterpart
owner) fails elements 2 and/or 3 on its own — tag it `inferred` and name
what the column doesn't say, the same as an under-specified spoken ask.

## Reads-well-too check

A deal with an unambiguous snapshot (value and close date both plainly
stated), no specific cited risk, and a clearly agreed next step should
come back with a clean snapshot, "risks: none surfaced," and a `heard` ask
— not picked apart for a risk or downgraded to `inferred` that isn't
actually there.
