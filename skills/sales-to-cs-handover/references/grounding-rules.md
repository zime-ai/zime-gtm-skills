# Grounding rules

Per-field evidence test and unknown marker. If a field has no matching row
here, default rule applies: no transcript evidence → `TBC` and a line in Open
gaps.

## Unknown markers — pick the one that names *why* it's unknown, never a bare blank

| Marker | Use when |
| --- | --- |
| `TBC` | To be confirmed — evidence exists but isn't firm yet, or field is simply unaddressed |
| `TBD` | To be decided — a decision hasn't been made yet (e.g. commercial terms pending negotiation) |
| `TBA` | To be assigned/added — an artifact or person is expected but not yet named/shared |
| "requested, not yet received" | Sales explicitly asked for something on a call and it hasn't arrived |
| "requested, not yet granted" | Access/permission was asked for, response pending |
| "yet to engage" | A named stakeholder hasn't appeared in any call yet |
| "not yet scheduled" | A date/slot was discussed as needed but no date set |

Never leave a field silently blank with no marker — that reads as "checked
and found nothing" instead of "not covered." Never invent a marker not in
this list without asking; consistency matters more than expressiveness here.

## Fields requiring a provenance note (append after the value)

| Field | Note required | Example |
| --- | --- | --- |
| "What they do" (§2) | Source only from the pasted transcripts. If no transcript states it, use `TBC` — never web search or prior knowledge to fill it. The one sample exception (Astra's public-info note) reflects a manual step the AE took outside this skill's scope, not a sourcing path this skill should take on its own. | Astra: "...continuous penetration testing... *Note: from public information, not from either call.*" — that note-style is what to reuse only if the user explicitly supplies outside research as a pasted source; the skill itself never goes looking for it. |
| "ROI they are targeting" (§5) | If citing Zime's own benchmark numbers rather than a client-stated target, label them explicitly as Zime's general claims, not the client's commitment. | Astra: "...these are Zime's general claims, not commitments Astra has made or agreed to." |
| Any artifact/link field (Drive folder, Sales Deck, POC resources sheet, NDA, POC charter, API access) | If discussed on a call but not delivered, use "requested, not yet received/granted" rather than `TBC` — names the actual state. | Astra: "MeetGeek API access — requested, not yet granted" |

## Fields that are always human-only — never fill from transcripts, never ask the user, always flag

Handover by (Sales), Handover to (CS), CS Owner, Handover date, Company Drive
folder link, POC resources sheet link, Sales Deck link, Acceptance date, CS
accepts this handover (Yes/No).

Render each as `TBC` inline and list under Open gaps grouped separately from
transcript-gap fields (see SKILL.md step 5). These are process artifacts
Sales creates outside any call — no amount of transcript reading fills them,
and per standing decision the skill doesn't interactively ask for them either.

## Acceptance checklist — how the skill proposes each checkbox

Checked (`- [x] ~~text~~`) only when a transcript directly evidences the
underlying fact — e.g. "Champion name and seniority confirmed" checks if a
transcript names a champion and their role. Left unchecked with a short
trailing reason otherwise, matching the samples' own style:

- `- [ ] NDA signed - pending acknowledgement`
- `- [ ] Slack channel - requested, not yet created`

Never check a box based on assumption that a normal deal would have this by
now. Checklist items about artifacts/process (NDA signed, Drive folder
created, Slack channel created) are almost always unchecked from transcripts
alone, since transcripts record conversations, not paperwork state — that's
expected, not a skill failure.

## Numeric / dated claims

Every price, headcount, or date pulled into the doc must be traceable to a
specific call in the pasted input set. If two calls disagree (e.g. cohort
size stated differently on two dates), use the most recent value but always
name the discrepancy inline — e.g. "10 (updated from 5 on the earlier call)"
— never silently pick one. A scope or number that changed mid-cycle is
itself a signal CS should see, not noise to suppress.

## §9 objections — answered is not closed

An objection raised on a call and answered by Sales stays in §9 as live,
with the answer given as its handling line — it does not get dropped for
having been addressed once. Only an objection the client explicitly
withdrew, in their own words, is left out. Reasoning: a client raising
something once (a comparison question, a pricing pushback, a scope worry)
signals it matters to them regardless of how well Sales handled it in the
moment — CS should expect it to resurface. Full derivation checklist for
this and for deal risk (the template has no separate risk field; both live
in §9) is in `miss-prone-fields.md`.

## Word budgets — density matches the samples, not a report

| Field shape | Budget | Example |
| --- | --- | --- |
| One-line field (NDA status, pilot cohort, sales motion) | ~5–30 words | "7 reps" / "$99/user/month - TBD after negotiation" |
| Narrative block (Primary pain, Key hooks, What CS should focus on first) | ~35–60 words | Astra's "Primary pain" cell is 27 words; TrueFoundry's is 34 |
| Stakeholder table cell (Motivation, CS posture) | ~8–25 words | See `miss-prone-fields.md` persona table |

A field that would run over budget gets trimmed, not split across cells or
padded with connective prose. No preamble inside any field ("It appears
that…", "Based on the calls…", restating the field's own label before
answering it) — go straight to the fact.

## "Any additional context" (§10) and appendix

§10 takes miscellaneous evidenced detail that doesn't fit §1–§9 — travel
dates, personal context, org-chart color. Still grounded: no filler sentence
about "the team seems engaged" without a specific transcript line behind it.
The trailing appendix (Upsell/Churn/Action-item types) renders only when a
transcript contains that level of explicit tribal-knowledge walkthrough —
see `handover-template.md` for the omit-vs-include rule.
