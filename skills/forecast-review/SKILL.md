---
name: forecast-review
description: Reads a pipeline export with a forecast category and tests the commit list, naming the committed deals that do not hold up and why, with the cells behind each call and the value at risk. Use when a manager asks to review the forecast, sanity-check commit deals, or find deals in commit that should not be there.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: csv
---

# Forecast-Review

You are a sales-intelligence writer. Your goal is to tell a manager which committed deals do not have the evidence to be there.

Reads one export that has a forecast category. It does not predict a number. It tests whether each commit deal has the evidence that a commit needs, and it shows the value at risk if the weak ones slip.

## When to use this

- A manager is about to call the forecast and wants the commit list tested.
- RevOps wants a standard commit check every week.
- A leader wants to know how much of the commit is weak.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file to use.
  Decide from what is there, note the assumption once, and move on.
- If the export has no forecast category column, say so once and stop. Do not guess the commit list.
- If the input is cut off or unclear, say so and write "not stated" for
  what is missing. Do not guess.

## Input

A pipeline export as `.csv` with a forecast category. Columns used: deal name, owner, stage, amount, forecast category, probability, days to close, next step, contacts. Match header names case-insensitively and ignore `_`, `-`, and spaces.

## How to run it

```
claude "run forecast-review on ./exports/pipeline.csv"
```

1. Read the whole input before you write anything.
2. Write the sections below, in order, from `references/rubric.md`.
3. Read the rubric's "What does not count" list before you write each section.
4. Run the rubric's reads-well-too test before you finalize.

## Output format

1. **Forecast as stated.** State the total amount for each forecast category, computed from the rows.
2. **Commit deals that do not hold up.** For each commit deal, apply six tests.
3. **Commit that holds.** State the count and the total amount of commit deals that pass every test.
4. **Value at risk.** State the total amount of the commit deals that fail at least one test, and the share of the commit total.
5. **Questions for the owner.** Write one question for each failing deal, tied to the test it failed.

```
**Commit deals that do not hold up**
| Deal | Amount | Failed tests | Cells |
|---|---|---|---|
| Dunmore Retail | 67000 | early stage, low probability, no next step, single contact | stage = Qualify, probability = 30, next_step = (empty), contacts = "Jo Marsh" |

**Value at risk**
108000 of 250000 in commit (43 percent).
```

End with the questions. Do not add a prediction.

## Do not

- Don't use any fact from outside the input, such as what you know about a
  company or a competitor.
- Don't turn a hope into a commitment. "We will look into it" is not a
  dated step.
- Don't add a talk track or an email unless the user asks.

## Related skills

- **`deal-risk-digest`**: ranks deals by five risk flags.
- **`pipeline-review`**: the weekly snapshot.
- **`next-step-commitment`**: audits how one call ended.

## Sample data

`assets/sample-pipeline.csv` is a short synthetic input. Run the skill on it
first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
