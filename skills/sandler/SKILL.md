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

Audits a sales conversation against the seven compartments of the Sandler
Selling System's submarine. Unlike the stage skills in this repo, Sandler
isn't tied to one point in the deal — the submarine's whole premise is that
each compartment must be sealed (secured) before the rep moves to the next,
so this skill checks order and completeness, not just topic coverage.

## When to use this

- A rep pitched a solution and you want to know whether they'd actually
  earned the right to — did they secure an up-front contract and surface
  real pain first, or did they jump straight to features.
- Checking whether a "close" on a call was a real mutual decision or the
  rep assuming yes and steamrolling into next steps.
- RevOps wants to sweep a pipeline export for deals where Sandler-relevant
  fields (budget confirmed, decision process, next-step contract) are
  missing before a forecast call.

## Modes

### Transcript mode (`.txt`, `.vtt`, `.json`, `.md`)

```
claude "run sandler on ./calls/acme-call.txt"
```

Read the transcript, then score it against each compartment in
`references/rubric.md`, in submarine order. For every compartment, output:

- **Status** — Covered / Partial / Missed / Not applicable to this call
- **Evidence** — a direct quote from the transcript. If a compartment
  genuinely wasn't reachable on this specific call (e.g. Fulfillment on a
  first discovery call that never got near a close), say **Not applicable**
  rather than scoring it Missed.
- **Note** — one line, only if Partial or Missed

Pay particular attention to order: a compartment scored Covered late in the
call after an earlier compartment was skipped (e.g. pitching before Pain
was surfaced) is a submarine violation worth calling out explicitly, not
just a missed box.

Close with the **single biggest submarine violation** on this call — which
compartment got skipped or rushed, and what it cost the rep — and what to
do differently next call.

### CSV mode (`.csv`)

```
claude "run sandler on ./exports/pipeline.csv"
```

Structural hygiene sweep, not a call-quality claim — say so explicitly. For
each deal row, check whether fields corresponding to the seven compartments
(especially budget confirmed, decision process, next-step commitment) are
present and non-trivial. Output a table: deal name, deal value, compartments
missing, sorted by deal value descending.

## Sample data

`assets/sample-transcript.txt` is a synthetic call that bonds well and gets
an up-front contract, but pitches before pain is fully surfaced, assumes
budget instead of discussing it, and closes hard instead of tentatively —
run the skill against it first.

## What this does not do

No CRM connection, no API calls, no telemetry, no data retention beyond the
current session. It reads the file you point it at and nothing else.
