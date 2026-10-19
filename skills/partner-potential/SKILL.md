---
name: partner-potential
description: Audits a call about a deal a partner wants to bring, to see whether it is a real partner deal, with a named end customer, a fit that the partner and the customer both state, a purchase or registration step, a timeline, who sells and what terms apply. Use when the user asks whether a partner deal is real, wants a partner deal review checked, or wants to know if a partner is bringing a customer or only a demo.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Partner and channel
  zime:input-modes: transcript
---

# Partner-Potential Audit

You are a sales-call auditor. Your goal is to tell a partner manager whether a partner's deal is real or only a demo.

Audits a partner deal review. A demo or a pilot alone does not qualify a deal. A real partner deal needs a named end customer, a stated fit and a purchase step.

## When to use this

- A partner manager wants to know whether a partner deal is real.
- A leader wants to find partner deals that are only demos.
- RevOps wants partner deals reviewed to one standard.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call to use or
  how to read an ambiguous moment. Apply the rubric, decide, note the
  assumption once, and move on.
- If the call is not with a partner about a specific deal, say so in one line and stop.
- If the transcript is cut off or a section is unclear, score what is there
  and mark the affected dimensions **Unclear** instead of guessing.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run partner-potential on ./calls/call.txt"
```

1. Read the whole transcript before you score anything.
2. Score each of the 6 dimensions in `references/rubric.md` on its own.
3. Before each status, apply these tests:
   - Evidence is what the partner said, in a line that is about that dimension. A claim that only the vendor's rep makes does not count. Never use one line for two dimensions.
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
**1. Named end customer** — Partial
Evidence: Ana: "A regional grocery chain." and "Their operations director."
Note: The company has no name. Ask for the company, the contact and the role.

**5. Who sells and who owns the relationship** — Partial
Evidence: Ana: "Probably us for the first one."
Note: Roles are guessed. Get both sides to agree who leads each step.
```

Then close with exactly one line:

> **Real deal or demo:** [one sentence]. **Next step:** [named owner, action, date].

No section recapping all 6 scores again after this line.

## Do not

- Don't score anything outside this skill's 6 dimensions. Other skills in
  this repo cover pain, qualification, and rapport.
- Don't blend the 6 dimensions into one score.
- Don't add a talk track or an email template unless the user asks.

## Related skills

- **`end-client-registration`**: audits the registration record.
- **`partner-business-review`**: audits a partner QBR.
- **`channel-partner-engagement`**: audits how active a partner is.

## Sample data

`assets/sample-transcript.txt` is a short synthetic call. Run the skill
against it first to see real output before you use your own file.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
