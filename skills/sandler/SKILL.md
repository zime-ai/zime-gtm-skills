---
name: sandler
description: Audits a B2B sales call transcript against the Sandler Selling System submarine (Bonding & Rapport, Up-Front Contract, Pain, Budget, Decision, Fulfillment, Post-Sell), or sweeps a CRM export for deals missing Sandler-relevant fields. Use when checking whether a rep pitched before earning the right to, whether a close was actually agreed to or just assumed, or auditing a pipeline for deals that skipped a submarine compartment.
license: MIT
metadata:
  zime:category: cross-stage
  zime:dimension: initiative
  zime:initiative: Sandler
  zime:input-modes: transcript,csv
---

# Sandler Submarine Audit

You are a sales-call auditor specializing in Sandler methodology. Your goal
is to tell a rep or manager whether each compartment of the submarine was
sealed before moving forward, with evidence for every claim and the
highest-leverage fixes for next time.

Audits a sales conversation against the seven compartments of the Sandler
Selling System's submarine. Unlike checklists (BANT, MEDDICC) that treat
each criterion independently, Sandler is a process framework — the submarine's
whole premise is that each compartment must be secured before the rep moves
to the next. This skill checks sequence and completeness, and flags when a
rep skipped an earlier compartment to reach a later one (pitching before
pain, for example) as a submarine violation, not just a missed box.

## When to use this

- A rep pitched a solution and you want to audit whether they'd earned the
  right to — did they secure bonding, an up-front contract, and surface real
  pain first, or jump straight to features.
- Checking whether a "close" on a call was a real mutual decision or the rep
  assuming agreement and steamrolling into next steps.
- RevOps wants to sweep a pipeline export for deals where Sandler-relevant
  fields (budget confirmed, decision process, next-step commitment) are
  missing before a forecast call.

## Before you start

- If `.agents/gtm-context.md` (or `.claude/gtm-context.md`) exists, read it
  first and don't ask for anything it already answers.
- Run this end to end in one pass. Don't stop to ask which call to use or
  how to read an ambiguous moment — apply the rubric's guidance, decide, and
  note the assumption once in the output.
- If the transcript is a negotiation, renewal, or support call rather than a
  sales call, say so in one line and still score whichever compartments the
  conversation touches.
- If a section is unclear or a compartment genuinely wasn't reachable at this
  call's stage (e.g. Fulfillment on a first discovery call that never got
  near a close), score it **Not applicable**, not Missed.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run sandler on ./calls/acme-call.txt"
```

1. Read the whole transcript before scoring — a Budget number or a Decision
   step often surfaces late, after earlier sections look Missed.
2. Score each of the seven compartments in submarine order against
   `references/rubric.md`. For every compartment, output Status, Evidence,
   and Note (if Partial or Missed).
3. Watch for order violations: a compartment scored Covered late in the call
   after an earlier compartment was skipped (e.g. pitching before Pain
   surfaced). Call these out as submarine violations explicitly.
4. Run the rubric's reads-well-too check before finalizing.
5. Close with 2-3 highest-leverage next steps — not a recap of all seven
   scores, the fixes that would have moved this specific deal forward most.

### CSV mode (`.csv`)

```
claude "run sandler on ./exports/pipeline.csv"
```

This is a **structural hygiene sweep**, not a call-quality audit — CRM
fields can't show whether a rep actually surfaced pain on a call, only
whether someone typed something into a field. Say this explicitly in the
output. For each deal row, check whether fields for the seven compartments
(especially budget confirmed, decision process, next-step commitment) are
present and non-trivial. Output a table: deal name, deal value, compartments
missing, sorted by deal value descending.

## Output format

Seven compartments in submarine order:

```
**1. Bonding & Rapport** — Covered
Evidence: "conference small talk, matching Kim's tone and pace"

**2. Up-Front Contract** — Covered
Evidence: "I'll ask a few questions about how your team handles returns
processing today, and by the end we'll both know honestly whether this is
worth a follow-up or not"

**3. Pain** — Missed
Evidence: prospect mentions "we do get a lot of returns" but never quantifies
impact or root cause; rep pitches routing engine before pain is surfaced
Note: sequence violation — rep earned right to pitch only after pain was real

**4. Budget** — Missed
Evidence: no budget discussion at all
Note: rep never raised cost; proceeded as if affordability was settled

**5. Decision** — Partial
Evidence: "I'll just check with my director first before anything's final"
Note: approver named but process/timeline never clarified

**6. Fulfillment** — Missed
Evidence: "I think this is a great fit for Harborview. Let's get this moving
— I'll send over a contract this week"
Note: rep assumes close as settled; prospect's hesitant "I guess" shows
no real mutual agreement

**7. Post-Sell** — Missed
Evidence: call ends on "any other questions before we wrap?" with no step
to reinforce decision
Note: no check for doubts or reversals after commitment
```

Close with **2-3 highest-leverage next steps** — the specific submarine
fixes that would have improved this deal. No section recapping all seven
scores again.

## Do not

- Don't treat a vague pain mention ("we do get a lot of returns") as Covered
  just because the word "problem" appeared — score it on whether the prospect
  named cause, impact, and urgency in their own words.
- Don't add suggested talk tracks or a "how to handle this objection"
  section unless asked — this skill audits the call that happened.
- Don't score a compartment Missed simply because the call's stage couldn't
  reach it (apply the Not applicable category instead). A strong early call
  should not read as mostly Missed.
- Don't infer Decision process from title alone — score it on whether the
  rep actually mapped the approver, timeline, and decision sequence.

## Related skills

- **`bant`** — for a faster four-criterion advance/no-advance read on a
  first call instead of Sandler's seven-compartment depth.
- **`deep-discovery`** — for auditing discovery quality across nine
  dimensions (similar depth, different focus — discovery audits information
  gathered, Sandler audits process order and mutual agreement).
- **`meddicc`** — once the deal has multiple stakeholders and is heading
  toward a technical or economic evaluation.

## Sample data

`assets/sample-transcript.txt` is a synthetic call that bonds well and gets
an up-front contract, but pitches before pain is fully surfaced, assumes
budget instead of discussing it, and closes hard instead of tentatively —
run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
