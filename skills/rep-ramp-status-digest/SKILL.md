---
name: rep-ramp-status-digest
description: Reads a new rep's calls over several weeks and writes a ramp status by technique (opening, questioning, pain, trigger, pitch, rapport), marking each as improving, flat, regressing, or not enough evidence, with a quote from each call. Use when a manager asks how a new rep is ramping, wants a ramp status for a 1:1, or wants to know whether coaching is working.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript
---

# Rep-Ramp-Status-Digest

You are a sales-intelligence writer. Your goal is to tell a manager whether a new rep is improving at each early-call technique, with the calls to prove it.

Reads one rep's calls in time order. It states a trend only when at least two calls show the technique, and it counts a technique as improved only when the buyer's replies show it worked. It uses the six techniques that `first-call-rampup` audits.

## When to use this

- A manager wants a ramp status before a 1:1.
- A manager wants to know whether last month's coaching changed the calls.
- A leader wants a ramp view for a new hire.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file to use.
  Decide from what is there, note the assumption once, and move on.
- If fewer than two calls are given, write the status as observations and say that two calls are the minimum for a trend.
- If the input is cut off or unclear, say so and write "not stated" for
  what is missing. Do not guess.

## Input

Two or more call transcripts for one rep, oldest first, each labeled with its week or date. Mark which lines the rep spoke.

## How to run it

```
claude "run rep-ramp-status-digest on ./calls/rep-riley/"
```

1. Read the whole input before you write anything.
2. Write the sections below, in order, from `references/rubric.md`.
3. Read the rubric's "What does not count" list before you write each section.
4. Run the rubric's reads-well-too test before you finalize.

## Output format

1. **Scope.** State the rep, the number of calls, and the weeks that they cover.
2. **Status by technique.** For each of the six techniques (opening, open-ended questioning, pain and priority, trigger, pitch clarity, rapport) give a status: improving, flat, regressing, or not enough evidence.
3. **What changed.** Name the one or two changes between the first and the latest call that the quotes show.
4. **Next focus.** Name the one technique with the most room to improve and the question to practice.
5. **Not yet judged.** List the techniques that have not been shown in enough calls to judge.

```
**Status by technique**
- Opening: improving. Week 1 had no agenda. Week 3: "Today I would like to hear how you schedule crews, then show a bit, then agree on next steps." Buyer: "Sure."
- Pain and priority: improving. Week 1: "Do you have scheduling problems?" Buyer: "Not really." Week 5: "Walk me through the last time a schedule went wrong." Buyer: "...about 1,200 dollars."
```

End with the next focus. Do not add a summary paragraph.

## Do not

- Don't use any fact from outside the input, such as what you know about a
  company or a competitor.
- Don't turn a hope into a commitment. "We will look into it" is not a
  dated step.
- Don't add a talk track or an email unless the user asks.

## Related skills

- **`first-call-rampup`**: audits one early call against six techniques.
- **`coaching-plan`**: turns calls into one thing to practice.
- **`adoption-leaderboard`**: ranks reps by behavior across many calls.

## Sample data

`assets/sample-transcript.txt` is a short synthetic input. Run the skill on it
first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
