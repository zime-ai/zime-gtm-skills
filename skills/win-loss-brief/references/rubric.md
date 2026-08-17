# Win-loss brief rubric

## Column synonyms (CSV mode)

Match headers case-insensitively, ignoring `_`/`-`/space differences.

- **Deal name**: `deal_name`, `deal`, `opportunity`, `opportunity name`,
  `account`, `account name`
- **Outcome**: `outcome`, `stage`, `deal stage`, `result`. Counts as **won**
  if the value fuzzy-matches `closed won`, `closed-won`, `won`, `closedwon`,
  or contains "won" as a whole word alongside "closed". Counts as **lost**
  if it fuzzy-matches `closed lost`, `closed-lost`, `lost`, `closedlost`, or
  contains "lost" as a whole word alongside "closed". Anything else (an
  open-pipeline stage) is out of scope — say so rather than briefing an
  open deal.
- **Close date**: `close date`, `closedate`, `won date`, `lost date`,
  `closed date`, `date closed`
- **Deal value**: `deal value`, `amount`, `opportunity value`, `deal size`,
  `contract value`
- **Reason**: `reason`, `loss reason`, `win reason`, `close reason`,
  `outcome reason`
- **Competitor**: `competitor`, `competing vendor`, `lost to`, `competitor
  name`

If a column the brief needs is entirely absent from the file, state this
once, up front, and never infer the value from another column.

## Driver categories

Every driver in section 2 of the brief is tagged with one of these five.
Reuse this vocabulary rather than inventing new category names for the
same ideas — it matches how `meddicc`'s Competition and Champion
dimensions and `negotiation-closing`'s pricing/procurement checks already
name these signals.

- **Competitive displacement** — a named competitor was chosen instead, or
  "do nothing"/incumbent status won out. Matches `meddicc`'s Competition
  dimension: what else was being evaluated, and how the deal was framed
  against it.
- **Champion strength or loss** — a champion actively sold on the rep's
  behalf (won) or went quiet, left, or was never truly present
  (lost). Matches `meddicc`'s Champion dimension.
- **Pricing/procurement friction** — pushback on price, a stalled
  approval/paper process, or a budget/contracting blocker. Matches
  `negotiation-closing`'s reaction-to-pricing and procurement-movement
  checks.
- **Timing** — the deal's timeline slipped, a trigger event passed, or the
  buying window closed/opened independent of price or competition.
- **Technical fit** — the product's capabilities matched or missed a
  stated requirement, integration, or evaluation criterion.

A single driver may brush against more than one category (e.g. a
competitor won partly on price) — tag it with the category its cited
evidence most directly supports, and name the secondary angle in the
evidence line if it's material.

## Driver confidence test

- **Clear** — the transcript states the driver plainly (the prospect names
  the reason, the competitor, or the blocker outright), or the CSV's
  `reason`/`competitor` column states it directly.
- **Tentative** — the closest thing said is a hedge, a guess, an
  unconfirmed aside, or the rep's own speculation ("might have been
  budget," "not sure if that was the real reason") — quote it exactly as
  hedged. Do not smooth a tentative driver into confident language, and do
  not drop it just because it's uncertain — cite it as uncertain.

## Evidence rule

Every driver cites either its quote and timestamp (transcript) or its
column name and cell value (CSV). A driver with no cited evidence does not
ship.

## Reads-well-too check

A deal with an unambiguous, well-evidenced outcome (a clearly-stated
competitor, a clearly-present or clearly-absent champion, explicit pricing
feedback) should come back with mostly **clear** drivers, not padded with
invented tentative ones to hit a factor count. Section 2 should have 3-5
drivers — if the evidence only supports 2, say so rather than manufacturing
a third.
