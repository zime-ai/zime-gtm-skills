# Deal risk digest rubric

Five risk signals, each worth points, summed into a risk tier. This ranks
deals against each other for a manager skimming a whole pipeline — it does
not claim to know why a rep hasn't updated a field.

## Column synonyms

Match headers case-insensitively, ignoring `_`/`-`/space differences.

- **Deal name**: `deal name`, `deal`, `opportunity`, `opportunity name`
- **Deal value**: `deal value`, `amount`, `opportunity value`, `deal size`
- **Stage**: `stage`, `deal stage`, `dealstage`, `opportunity stage`
- **Close date**: `close date`, `expected close`, `closedate`
- **Probability**: `probability`, `win probability`, `forecast
  probability`
- **Stage entered date**: `stage entered date`, `stage entry date`,
  `entered stage`, `stage start date`. If instead the export already has a
  precomputed **days in stage** column (`days in stage`, `time in stage`,
  `stage age`, `days in current stage`), use its value directly rather than
  computing from a date.
- **Next step**: `next step`, `next steps`, `next action`
- **Contacts**: `contacts`, `stakeholders`, `champions`, `buying
  committee`, `contacts involved`. Names are separated by `;` or `,`.

If a column a signal depends on is entirely absent from the export, that
signal contributes zero points for every row — state this once, up front,
and never infer the value from another column.

## 1. Past-due and unlikely — 3 points

Triggered if the close date is today or earlier **and** probability is
below 50%. This is the strongest signal: a deal that's already blown past
its committed close date while the rep still isn't confident in it.
Neither condition alone triggers this — a past-due date with high
probability is a stale-but-fine field; a low probability with a future
close date is just early pipeline. Evidence cites both cells, e.g.
`close_date = 2025-02-14 (past), probability = 20%`.

## 2. Stage age — 1 point

Triggered if the deal has sat in its current stage for more than 45 days
(computed against today if only a stage-entered date is present).
Evidence: `stage_entered_date = 2025-05-01 (103 days in stage)` or
`days_in_stage = 103`.

## 3. Blank or vague next step — 1 point

Triggered if the next-step field is empty, or matches a vague-phrase
pattern: "follow up", "followup", "check in", "checking in", "circle
back", "touch base", "keep in touch", "keeping warm", "tbd", "n/a",
"none", "pending". Evidence: `next_step = (empty)` or `next_step =
"follow up"`.

## 4. Single-threaded contact — 1 point

Triggered if the contacts field lists one name or none at all. Evidence:
`contacts = "Greg Malone"` or `contacts = (empty)`.

## 5. Deal value — tiebreak only, not a point

Not scored on its own. When two or more deals tie on total points, the
larger deal_value ranks first — a bigger deal surfaces above a smaller
one when the risk read is otherwise comparable.

## Risk tiers

- **High**: 3+ points
- **Medium**: 1-2 points
- **Low**: 0 points

## Reads-well-too check

A deal with a future close date, a confident probability, a recent stage
entry, a specific next step, and more than one contact should come back
Low/0 points across the board — not picked apart for phrasing or minor
formatting differences in otherwise complete fields. The sample data must
contain at least two such deals, and running this skill against it must
score them Low. If a healthy-looking deal is coming back scored, the
rubric is being applied too strictly — loosen it before finalizing.
