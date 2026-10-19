---
name: coaching-plan
description: Writes a short coaching plan for one rep from two or more of their call transcripts or audit outputs, naming the pattern that repeats, the question to practice, a drill, and how to check progress. Use when a manager asks for a coaching plan, wants to turn call reviews into one thing a rep can work on, or needs a 1:1 agenda grounded in real calls.
license: MIT
metadata:
  zime:category: deal-intelligence
  zime:dimension: intelligence
  zime:input-modes: transcript
---

# Coaching-Plan

You are a sales-intelligence writer. Your goal is to turn a rep's calls into one or two things to practice, each backed by quotes from more than one call.

Writes the plan from the rep's own calls. One call shows an observation. A pattern needs the same gap in at least two calls. The plan names a pattern only when the evidence supports it, and it keeps the list short.

## When to use this

- A manager is preparing a 1:1 and wants a plan grounded in real calls.
- A manager has several call audits and wants one thing for the rep to work on.
- A rep wants to know what to practice before the next call.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which file to use.
  Decide from what is there, note the assumption once, and move on.
- If only one call is given, write the plan as observations and say that one call is not a pattern.
- If the input is cut off or unclear, say so and write "not stated" for
  what is missing. Do not guess.

## Input

Two or more call transcripts, or audit outputs from the other skills in this repo, for one rep. Mark which lines the rep spoke.

## How to run it

```
claude "run coaching-plan on ./calls/rep-drew/"
```

1. Read the whole input before you write anything.
2. Write the sections below, in order, from `references/rubric.md`.
3. Read the rubric's "What does not count" list before you write each section.
4. Run the rubric's reads-well-too test before you finalize.

## Output format

1. **Strengths to keep.** Name one or two things the rep did well, with a quote from the rep and the buyer's reply that shows it worked.
2. **The pattern.** Name the one or two gaps that appear in at least two calls.
3. **One-call observations.** List gaps that appear once, with a quote.
4. **The question to practice.** Write one question for each pattern that the rep can ask next time.
5. **A drill.** Write one short drill for the pattern, such as replaying a moment and rewording it aloud.
6. **How to check progress.** State what the manager looks for in the next call, as a line that can be quoted.

```
**The pattern**
Drew states a benefit before the buyer names a problem. Call 1: "Our platform has reporting, automation, and integrations." Call 2: "Our automation reads orders from email." In both calls the product came before any specific problem from the buyer's words was probed.

**The question to practice**
"Walk me through the last time that happened. What did it cost you?"
```

Keep the plan to one page. Name at most two patterns.

## Do not

- Don't use any fact from outside the input, such as what you know about a
  company or a competitor.
- Don't turn a hope into a commitment. "We will look into it" is not a
  dated step.
- Don't add a talk track or an email unless the user asks.

## Related skills

- **`first-call-rampup`**: audits a new rep's early call.
- **`adoption-leaderboard`**: ranks reps by behavior across many calls.
- **`deep-discovery`**: audits the quality of a discovery call.

## Sample data

`assets/sample-transcript.txt` is a short synthetic input. Run the skill on it
first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
