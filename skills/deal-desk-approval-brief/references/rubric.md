# Deal-Desk-Approval-Brief rules

Reads one export with a discount column. It does not decide whether a discount is allowed, and it uses no policy that the export or the company context does not state. It compares each deal with the other deals in the same export.

Three rules apply to every section.

- **Cite or leave it out.** Every claim traces to a quote, a timestamp, or a column and cell. A claim with no cited source does not ship.
- **The buyer or customer must say it.** A claim that only the rep makes does not count unless the other side accepted it. Silence is not a yes.
- **Unknown stays unknown.** When the input does not say it, write "not stated". Do not fill the gap with a guess or with outside knowledge.

## Discount norm

State the median discount percent of the rows in scope and the number of rows. Compute it from the rows. If the company context states a ceiling, state that too.

## Deals above the norm

List each deal whose discount is 10 points or more above the median, or above the stated ceiling. Show amount, discount, term, approver, and competitor. Write (empty) for a blank cell. Cite the cells. Rank by discount, highest first.

## Missing for the approver

For each listed deal, name which of approver, term, and competitor is blank. Do not fill a blank from another column or from a guess.

## Open approvals

List every deal whose approval status is pending, even if it is not above the norm. Write the count if none.

## Questions for the owner

Write one question for each listed deal that an owner can answer in a sentence, tied to a missing item.

## What does not count

- A decision that a discount is allowed or not.
- A policy ceiling that the export and the company context do not state.
- A blank cell written as a value.
- A competitor that the export does not name.
- A deal listed with no cited cell.

## Reads-well-too test

Run this test in both directions before you finalize.

- An export where every discount is within 10 points of the median and every deal has an approver must produce "no deal is above the norm" and an open-approvals list. Do not invent a deal to list.
- A thin input must not get a padded output. When the input supports two items, write two. Do not invent a third to reach a count.

## Sources

The brief follows common deal-desk practice. The rules come from reviews of exports.
