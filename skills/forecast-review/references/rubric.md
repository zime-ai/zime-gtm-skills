# Forecast-Review rules

Reads one export that has a forecast category. It does not predict a number. It tests whether each commit deal has the evidence that a commit needs, and it shows the value at risk if the weak ones slip.

Three rules apply to every section.

- **Cite or leave it out.** Every claim traces to a quote, a timestamp, or a column and cell. A claim with no cited source does not ship.
- **The buyer or customer must say it.** A claim that only the rep makes does not count unless the other side accepted it. Silence is not a yes.
- **Unknown stays unknown.** When the input does not say it, write "not stated". Do not fill the gap with a guess or with outside knowledge.

## Forecast as stated

State the total amount for each forecast category, computed from the rows. Name the commit deals.

## Commit deals that do not hold up

For each commit deal, apply six tests. (1) Days to close is zero or more. (2) Probability is 50 or more. (3) The next step is present and names a specific action. A blank cell or a phrase such as 'follow up' or 'check in' fails. (4) The deal has more than one contact. (5) The stage is Proposal or later. (6) The amount is above zero. List a deal only when it fails at least one test. Cite the cell for each failure. Rank by amount.

## Commit that holds

State the count and the total amount of commit deals that pass every test. Do not list them.

## Value at risk

State the total amount of the commit deals that fail at least one test, and the share of the commit total. Compute it from the rows.

## Questions for the owner

Write one question for each failing deal, tied to the test it failed.

## What does not count

- A deal that fails only because a column is missing. A missing column is a data gap and is stated once.
- A guess that a deal will close or slip.
- A probability that the writer changes.
- A test that the export cannot run.
- A commit deal listed as failing with no cited cell.

## Reads-well-too test

Run this test in both directions before you finalize.

- A commit list where every deal has a future close date, a probability of 50 or more, a dated next step, more than one contact, a mid or late stage, and an amount must produce "every commit deal holds". Do not invent a failure.
- A thin input must not get a padded output. When the input supports two items, write two. Do not invent a third to reach a count.

## Sources

The tests follow common forecast-hygiene practice. The rules come from reviews of exports.
