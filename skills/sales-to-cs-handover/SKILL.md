---
name: sales-to-cs-handover
description: Fills the fixed Zime Ignite Sales-to-CS handover template from pasted call transcripts, flagging every field it can't fill.
disable-model-invocation: true
---

This skill **transcribes** evidence into a fixed form — the Zime Ignite
Sales → CS Handover Template (`references/handover-template.md`). It does
not compose a handover from what a typical deal looks like. Every filled
field traces to a specific call in the pasted input; every field without
evidence gets the template's own unknown marker (`TBC`/`TBD`/`TBA`/etc, see
`references/grounding-rules.md`) and a line in Open gaps. Transcribe, don't
compose.

**Density matches the samples, not a report.** Every filled field is a
fragment, not a paragraph — see the word budgets in `grounding-rules.md`.
No preamble ("It appears that…"), no restating the field label, no field
split across cells to say more. This applies at every step below, not just
at generation time.

## Step 1 — Inventory the pasted sources

Read only what the user pasted or named for this handover. For each source,
record: label, date, participants named, and **type** — raw transcript, or a
Zime insight export (recognizable by structured Objections / Action Items /
Commitment blocks with severity and evidence). The type matters for Step 3.
If a source has no explicit date, use the literal `undated` — never guess a
date from file order.

**Done when:** every source has a row with a date (or `undated`) and a type,
and the count is reported back to the user.

## Step 2 — Fill the template field by field

Open `references/handover-template.md` and `references/grounding-rules.md`
side by side. Walk the template top to bottom, not source by source — a
field-by-field pass catches missing fields that a source-by-source pass
would miss. For each field:

1. Search the inventoried sources for evidence.
2. If found, fill it and note which source(s) it came from (informal tracking
   for your own accuracy — the output doc itself does not carry citations,
   matching both samples).
3. If not found, apply the correct unknown marker from `grounding-rules.md`.
   Never fill from web search, prior knowledge, or a "reasonable for this
   kind of company" guess, even if the result would read plausibly — a
   plausible-sounding fabrication is worse than a visible gap, since CS
   trusts it without checking. Never a blank with no marker either.
4. If the field requires a provenance note (What they do; ROI they are
   targeting) apply it per `grounding-rules.md`.

**Done when:** every field in the template has either evidenced content or
an unknown marker — none silently blank.

## Step 3 — Close the four miss-prone areas

These four are where filling opportunistically (Step 2) reliably falls
short, confirmed independently by both a blind test run and the person who
does this by hand today. Run all four explicitly, every time. Full detail
in `references/miss-prone-fields.md`; the rules themselves:

- **Roster pass** — before finalizing §3, list every human named anywhere in
  any source, including people mentioned but never present on a call. Each
  one gets a §3 row or is explicitly excluded with a reason.
- **Role completeness** — Champion, Decision maker, and Economic buyer each
  either name a person or read as explicitly unidentified (`yet to engage`,
  `TBC`). An absent economic buyer is a finding for Open gaps, not an empty
  cell that looks skipped.
- **Persona, not adjective** — Motivation is the *personal* want, traceable
  to something that person specifically said or asked (not the org's stated
  goal restated per-person). CS posture is an instruction to CS about how to
  handle that person, not a mood adjective. Worked examples in
  `miss-prone-fields.md`.
- **Answered ≠ closed** — an objection raised and answered on a call stays
  live in §9 with a handling line, on the assumption it resurfaces. Only an
  objection the client explicitly withdrew is dropped. If a source is a Zime
  insight export, route its pre-classified Objections block here directly
  per the routing map in `miss-prone-fields.md` rather than re-deriving it.
- **Risk derivation** — §9 also takes deal risk, since the template has no
  dedicated field for it. Run the standing checklist in
  `miss-prone-fields.md` (unsigned paper, unengaged economic buyer,
  single-threaded champion, unmet asks, assumed-but-deferred commitments,
  undated milestones, unfinalized commercials, a stakeholder new to their
  own systems) against the sources; every hit gets a line with a handling
  note, same as an objection.

**Done when:** every named human is placed or excluded, all three roles are
resolved or marked unidentified, every stakeholder's motivation/posture pair
is personal/behavioral (not org-level/adjective), and §9 holds every
answered-but-live objection plus every risk-checklist hit.

## Step 4 — Propose the acceptance checklist

For each of the 16 checklist items, check it only if a source directly
evidences the underlying fact. Otherwise leave unchecked with a short
trailing reason (`- [ ] Slack channel - requested, not yet created`), per
`grounding-rules.md`. Process/artifact items (NDA signed, Drive folder
created) are almost always unchecked from transcripts alone — that's
expected, not a failure to flag.

**Done when:** all 16 items are marked, and every unchecked item carries a
reason.

## Step 5 — Assemble Open gaps

Two groups, kept separate since the fix differs:

- **Human-only fields** (Handover by/to, CS Owner, dates, Drive folder,
  Sales Deck, POC resources sheet link, Acceptance fields) — these are
  never filled from transcripts and never asked for interactively; list
  them here every time.
- **Transcript gaps** — any content field left at an unknown marker because
  no source covered it, including an unidentified role from Step 3.

**Done when:** every `TBC`/`TBD`/`TBA`/etc marker in the filled doc has a
matching line in one of the two groups.

## Step 6 — Ask, only if genuinely uncertain

Inference from the sources is the goal, not a fallback to avoid. Only when a
Step 3 area is both unresolved *and* load-bearing (a champion with no named
decision maker; an objection with no clear handling angle; a risk with no
evidence either way) ask the user directly — up to 5 questions, confined to
stakeholders, persona, objections, and risks. Never ask to pad a field that
should just read as a gap; never ask outside these four areas. Fold answers
in; anything skipped stays a flagged gap.

**Done when:** either zero questions were needed, or up to 5 were asked and
resolved answers are folded back into §3/§9 before generation.

## Step 7 — Render appendix decision

Check whether any source contains an explicit tribal-knowledge walkthrough
(a stakeholder explicitly naming their own signal-detection habits, e.g.
"here's how I spot an upsell"). If yes, fill the trailing appendix
(Upsell signals / Churn signals / Types of action items) from that source
only. If no, omit the appendix entirely — no `TBC` placeholders for it.

**Done when:** appendix is either fully evidenced or absent, never partially
filled with markers.

## Step 8 — Emit markdown, then render docx

Write the filled markdown to
`<Client name> - Sales to CS Handover - <YYYY-MM-DD>.md` in the current
directory, matching `handover-template.md`'s formatting exactly. Then
delegate to the `document-skills:docx` skill using `references/docx-layout.md`
to render the `.docx` sibling file.

**Done when:** both files exist, and the chat response is the gap summary
below — nothing else.

## Gap summary to the user

The entire chat-side response after generation. Never echo or re-describe
the generated doc's content — that duplication is where most of the
verbosity complaints come from; the doc itself is the deliverable. State:
file paths, human-only gaps (always present), transcript gaps (if any),
whether the appendix was included, and how many follow-up questions (if any)
were asked in Step 6.
