---
name: competitive-loss-digest
description: Reads an export of lost deals and writes a digest of which rivals took deals and why, with counts, the amount lost to each rival, and whether each reason came from the buyer or from the rep. Use when a manager asks which competitors are winning, why deals are lost to a rival, or what the loss reasons really say.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: csv
---

# Competitive-Loss-Digest

You are a sales-intelligence writer. Your goal is to tell a leader which rivals take deals and which reasons are backed by the buyer.

Reads an export of closed-lost deals. It counts by rival and by reason, and it tags every reason as buyer-stated or rep-stated, because a loss reason that only the rep writes is a guess. With few rows it says so.

## When to use this

- A leader wants to know which competitor is winning.
- Product wants the real reasons for losses to a rival.
- A manager wants to know how much of the loss data is trustworthy.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file to use.
  Decide from what is there, note the assumption once, and move on.
- If the export has fewer than five lost rows, give the counts and say that the sample is too small for a pattern.
- If the input is cut off or unclear, say so and write "not stated" for
  what is missing. Do not guess.

## Input

An export of lost deals as `.csv`. Columns used: deal name, amount, days since close, competitor, loss reason, and who gave the reason (buyer or rep). Match header names case-insensitively and ignore `_`, `-`, and spaces. A missing reason source column means every reason is rep-stated.

## How to run it

```
claude "run competitive-loss-digest on ./exports/lost-deals.csv"
```

1. Read the whole input before you write anything.
2. Write the sections below, in order, from `references/rubric.md`.
3. Read the rubric's "What does not count" list before you write each section.
4. Run the rubric's reads-well-too test before you finalize.

## Output format

1. **Scope.** State the number of lost rows, how many name a rival, how many have a blank competitor, and which columns were found.
2. **Losses by rival.** For each named rival give the count and the total amount lost.
3. **Reasons by rival.** For each rival list the reasons given and the count of each.
4. **How much is trustworthy.** State the share of reasons that the buyer stated.
5. **Questions for product and sales.** Write up to three questions, each tied to a repeated buyer-stated reason.

```
**Losses by rival**
| Rival | Deals | Amount lost |
|---|---|---|
| Brightpath | 4 | 149000 |

**Reasons by rival**
- Brightpath: no native warehouse connector (2, both buyer-stated: Anvil Foods, Dell Freight), price (1, rep-stated), timing (1, rep-stated).
```

End with the questions. Do not add a prediction.

## Do not

- Don't use any fact from outside the input, such as what you know about a
  company or a competitor.
- Don't turn a hope into a commitment. "We will look into it" is not a
  dated step.
- Don't add a talk track or an email unless the user asks.

## Related skills

- **`loss-review`**: audits a debrief with a lost buyer.
- **`win-loss-brief`**: writes the brief for one closed deal.
- **`competitor-battlecard`**: writes a card for one rival.

## Sample data

`assets/sample-lost-deals.csv` is a short synthetic input. Run the skill on it
first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
