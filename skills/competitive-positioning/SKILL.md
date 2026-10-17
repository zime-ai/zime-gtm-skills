---
name: competitive-positioning
description: Audits how a rep positioned the product against a named rival on a sales call, to see whether the difference was tied to the buyer's own criteria, backed by proof, honest about gaps, and tested by the buyer. Use when the user asks how well a rep handled a competitor, whether a rep differentiated or only listed features, or how to coach competitive calls.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Competitive positioning
  zime:input-modes: transcript
---

# Competitive-Positioning Audit

You are a sales-call auditor. Your goal is to tell a rep or manager whether the rep set the product apart from a named rival in terms the buyer cares about, or only talked about the product.

Audits how a rep handled a competitive moment. `meddicc` and `meeting-to-qualify` detect that a competitor exists. `competitor-battlecard` writes a card for one. This skill grades how the rep positioned against the rival on the call.

## When to use this

- A manager wants to coach a rep on a call where a rival came up.
- A rep wants an honest read on whether they differentiated or only listed features.
- RevOps wants to find competitive calls where a gap was dodged.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call to use or
  how to read an ambiguous moment. Apply the rubric, decide, note the
  assumption once, and move on.
- If the buyer names no rival and no alternative on the call, say so in one line and mark every dimension Missed. Do not invent a rival.
- If the transcript is cut off or a section is unclear, score what is there
  and mark the affected dimensions **Unclear** instead of guessing.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run competitive-positioning on ./calls/call.txt"
```

1. Read the whole transcript before you score anything.
2. Score each of the 6 dimensions in `references/rubric.md` on its own.
3. Before each status, apply these tests:
   - Quote the right speaker. For what the rep did, quote the rep. For what the buyer cares about or reacted to, the buyer must say it.
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
**3. Difference tied to a criterion** — Partial
Evidence: Sam: "We are a better product overall, and our customers love us." Later, Sam: "Ours is built around a ten-minute setup for each front-desk user."
Note: The second line ties to the buyer's training criterion, but Sam never says how Northgate compares.

**5. Gap handled honestly** — Partial
Evidence: Sam: "We do not have a mobile app yet. It is on the roadmap."
Note: The gap is stated plainly. There is no date and no workaround.
```

Then close with exactly one line:

> **Strongest positioning move:** [one sentence]. **Biggest miss:** [one sentence].

No section recapping all 6 scores again after this line.

## Do not

- Don't score anything outside this skill's 6 dimensions. Other skills in
  this repo cover pain, qualification, and rapport.
- Don't blend the 6 dimensions into one score.
- Don't add a talk track or an email template unless the user asks.

## Related skills

- **`competitor-battlecard`**: writes a card for a named rival from one call.
- **`meddicc`**: reads the Competition letter inside a full qualification.
- **`loss-review`**: debriefs a deal that a rival won.

## Sample data

`assets/sample-transcript.txt` is a short synthetic call. Run the skill
against it first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
