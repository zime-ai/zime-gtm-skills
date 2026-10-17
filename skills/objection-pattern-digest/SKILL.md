---
name: objection-pattern-digest
description: Reads several call transcripts and lists the objections that repeat, grouped by theme, with the number of calls, a quote from each call, whether each was resolved on the call, and what the calls that resolved it did. Use when a manager asks what objections come up most, wants an objection digest across calls, or wants to know which objections reps handle badly.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript
---

# Objection-Pattern-Digest

You are a sales-intelligence writer. Your goal is to tell a manager which objections repeat across calls and which ones the calls never resolved.

Reads many calls at once. It counts only what the calls show. It needs at least three calls in the input. Within those calls, a theme is a pattern when it appears in at least two of them. It separates a real objection from a question or a minor complaint, and it does not guess a cause.

## When to use this

- A manager wants to know the top objections across recent calls.
- Enablement wants real objection language for training.
- A leader wants to know which objections stay unresolved.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file to use.
  Decide from what is there, note the assumption once, and move on.
- If fewer than three calls are given, list the objections as observations and say that three calls are the minimum for a pattern.
- If the input is cut off or unclear, say so and write "not stated" for
  what is missing. Do not guess.

## Input

Three or more call transcripts, one file each or one file with the calls separated by a clear marker. Mark which lines the buyer spoke.

## How to run it

```
claude "run objection-pattern-digest on ./calls/"
```

1. Read the whole input before you write anything.
2. Write the sections below, in order, from `references/rubric.md`.
3. Read the rubric's "What does not count" list before you write each section.
4. Run the rubric's reads-well-too test before you finalize.

## Output format

1. **Scope.** State how many calls were read and how many contained at least one objection.
2. **Patterns.** Group objections into themes, such as price, past failure, integration, or timing.
3. **Resolved or not.** For each pattern, state in how many calls the buyer accepted an answer on the call.
4. **What worked.** For each pattern, name what the rep did in the calls where the buyer accepted the answer.
5. **One-call objections.** List objections that appear in one call only, with a quote.

```
**Patterns**
- Price (3 calls of 4). Call 1: "Your price is higher than the tool we use now." Call 3: "It is more than we budgeted."

**Resolved or not**
- Price: accepted in 1 of 3 calls (call 3, after a smaller package was offered).

**What worked**
- Price: in call 3 the rep asked "What was the budget?" and offered a smaller package.
```

End with the one objection that no call resolved. Do not add a recap.

## Do not

- Don't use any fact from outside the input, such as what you know about a
  company or a competitor.
- Don't turn a hope into a commitment. "We will look into it" is not a
  dated step.
- Don't add a talk track or an email unless the user asks.

## Related skills

- **`competitive-positioning`**: audits how a rep handled a named rival.
- **`coaching-plan`**: turns one rep's calls into a plan.
- **`competitor-battlecard`**: writes a card for one rival.

## Sample data

`assets/sample-transcript.txt` is a short synthetic input. Run the skill on it
first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
