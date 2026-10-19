# Territory-Summary rules

Reads one account export. Every figure comes from the rows. It does not set quotas, rebalance territories, or predict results.

Three rules apply to every section.

- **Cite or leave it out.** Every claim traces to a quote, a timestamp, or a column and cell. A claim with no cited source does not ship.
- **The buyer or customer must say it.** A claim that only the rep makes does not count unless the other side accepted it. Silence is not a yes.
- **Unknown stays unknown.** When the input does not say it, write "not stated". Do not fill the gap with a guess or with outside knowledge.

## Coverage by territory

For each territory, state the number of accounts, the number of open deals, and the total open amount. Compute them from the rows.

## Concentration

For each territory, state the share of its open amount that sits in its largest account. Flag a territory when that share is more than two thirds. Cite the cells.

## Accounts gone quiet

List each account whose days since last activity is more than 45. Show territory, owner, open deals, and the days. Say whether it has an open deal. Rank by days.

## What it does not show

State once that the export holds no quota, win history, or account potential, so the summary does not say whether a territory is fair.

## Questions for the territory owner

Write one question for each flagged territory and each quiet account that an owner can answer in a sentence.

## What does not count

- A statement that a territory is fair, unfair, or needs rebalancing.
- A quota or target that the export does not hold.
- A share computed from a guess.
- A quiet account listed with no cited cell.
- A territory inferred from an owner name.

## Reads-well-too test

Run this test in both directions before you finalize.

- An export where no territory has a largest account above two thirds and no account is quiet must produce "no concentration and no quiet account". Do not invent one.
- A thin input must not get a padded output. When the input supports two items, write two. Do not invent a third to reach a count.

## Sources

The summary follows common territory-review practice. The rules come from reviews of exports.
