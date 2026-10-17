# Stuck-Deal-Digest rules

Reads one pipeline export. It looks only at movement: silence, time in stage, and a next step that is overdue. `deal-risk-digest` ranks risk from five flags. This skill answers a narrower question, which deals have stopped, and it uses the export's own norms to decide.

Three rules apply to every section.

- **Cite or leave it out.** Every claim traces to a quote, a timestamp, or a column and cell. A claim with no cited source does not ship.
- **The buyer or customer must say it.** A claim that only the rep makes does not count unless the other side accepted it. Silence is not a yes.
- **Unknown stays unknown.** When the input does not say it, write "not stated". Do not fill the gap with a guess or with outside knowledge.

## Scope and columns

State how many deals are in scope, which columns were found, and which signals could not be scored. A signal with no column scores nothing for every row. Never infer it from another column.

## Stuck deals, ranked

A deal is silent when days since last activity is more than twice the median of the deals in scope. It is aged when days in stage is more than one and a half times the median for its own stage, or for all deals when the stage has fewer than three rows. It has an overdue step when the next step is overdue by one day or more. Rank by the number of signals, then by amount. Cite the cells.

## What each needs

Write one question per stuck deal that a manager can ask the owner. Tie the question to the signal, for example what changed since the last activity, or who owns the next step.

## Not stuck

State the count of deals with no signal. Do not list them.

## What does not count

- A deal that is slow only because the stage is long for every deal in the export.
- A deal with a blank next step and no other signal. That is a data gap and not a stall.
- A guess about why a deal stopped. The cells show that it stopped, not why.
- A median that includes deals outside the stage in scope.

## Reads-well-too test

Run this test in both directions before you finalize.

- A healthy export, where every deal has recent activity, a normal time in stage, and no overdue step, must produce "no stuck deals". Do not rank deals to fill a list.
- A thin input must not get a padded output. When the input supports two items, write two. Do not invent a third to reach a count.

## Sources

The signals follow common pipeline-hygiene practice. The rules come from reviews of exports and calls.
