---
name: multi-threading
description: Audits how widely a rep has engaged the buying group in a deal, to see whether the approver, a technical evaluator and daily users are known, reached and moving, or whether one contact carries the deal. Use when the user asks whether a deal is single-threaded, who else the rep should reach, or how to broaden the buying group before a forecast call.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Multi-threading
  zime:input-modes: transcript
---

# Multi-Threading Audit

You are a sales-call auditor. Your goal is to tell a rep or manager whether the deal rests on one contact or on a buying group that the rep mapped and reached.

Audits the breadth of engagement in one deal, read from a call or several calls. `champion-tracker` follows one champion's actions. `meddicc` scores the approver and champion as letters. This skill asks how wide the thread is and whether a dated plan exists to widen it.

## When to use this

- A manager wants to know whether a deal is single-threaded before a forecast call.
- A rep wants to know who else to reach and how.
- RevOps wants to find deals that depend on one contact.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call to use or
  how to read an ambiguous moment. Apply the rubric, decide, note the
  assumption once, and move on.
- If several call files are given, read them in order and judge the group as of the latest call.
- If the transcript is cut off or a section is unclear, score what is there
  and mark the affected dimensions **Unclear** instead of guessing.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run multi-threading on ./calls/call.txt"
```

1. Read the whole transcript before you score anything.
2. Score each of the 6 dimensions in `references/rubric.md` on its own.
3. Before each status, apply these tests:
   - Evidence is what the buyer said about the people involved, in a line that is about that dimension. A name that appears only in the CRM does not count.
   - When no line addresses a dimension, the status is Missed. Do not soften
     it to Partial because the call felt thorough elsewhere.
   - Partial needs a quotable line that names the dimension but stays vague.
     When you cannot quote that line, it is Missed.
   - Covered needs the specifics the rubric names, not a general statement.
   - Read each dimension's "does not count" line first.
4. Run the rubric's reads-well-too test before finalizing, in both directions.
5. Write the output in the exact shape under `## Output format`.

For every dimension, output:

- **Status**: Covered, Partial, or Missed
- **Evidence**: a direct quote or timestamp from the transcript. When you
  cannot point to a specific line, mark the dimension **Unclear**.
- **Note**: one line, only for Partial or Missed. It can end with the
  rubric's "strong call" move as one short question the rep can ask next time.

## Output format

6 dimensions, in the rubric's numbered order:

```
**2. Approver reached** — Partial
Evidence: Priya: "Daniel, our VP of Operations. He signs anything over fifty thousand." Alex: "Has Daniel seen the product?" Priya: "No."
Note: The approver is named and has never joined a call. Ask Priya to bring Daniel to the next call.

**6. A dated plan to broaden** — Missed
Evidence: Priya: "Maybe. Let me think about when."
Note: No person, no date. Propose a specific day and book it before the call ends.
```

Then close with exactly one line:

> **Thread count:** [number of people who spoke or acted]. **Single biggest gap:** [one sentence]. **Next step:** [named person, action, date].

No section recapping all 6 scores again after this line.

## Do not

- Don't score anything outside this skill's 6 dimensions. Other skills in
  this repo cover pain, qualification, and rapport.
- Don't blend the 6 dimensions into one score.
- Don't add a talk track or an email template unless the user asks.

## Related skills

- **`champion-tracker`**: follows one champion's actions across calls.
- **`meddicc`**: scores the economic buyer and champion as letters.
- **`mutual-action-plan`**: turns the plan to broaden into dated steps.

## Sample data

`assets/sample-transcript.txt` is a short synthetic call. Run the skill
against it first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
