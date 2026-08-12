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

## Literal, not prescriptive — by design

This skill transcribes; it does not compose the confident, prescriptive
framing a human handover author sometimes adds (e.g. stating POC exit
criteria as fact when no call actually set one). That's a deliberate
choice, not an omission — never invent a fact to match a more assertive
ground-truth sample's tone.

But a bare unknown marker is not the end state either: pair it with a
one-line next-step telling CS what to go establish, phrased as an action,
not as a finding. Worked example: "No numeric exit criteria discussed —
Rohit prioritized quality over speed. CS to agree exit criteria before the
brain demo." — the first clause stays literal/sourced, the second is an
instruction, not a claim about what the transcript said.

The astra/truefoundry ground-truth samples, and any client's own GT doc,
may be more prescriptive than this on purpose (human editorial judgment
added after the fact) — a diff against them on this specific axis is not a
defect to fix.

## Fields requiring a provenance note (append after the value)

Examples below are Astra's actual filled values, shown to demonstrate the
*note style* — copy the phrasing pattern, not the domain (pentesting,
MeetGeek) or the tool names, which are specific to that deal.

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

## Citing a fact back to its source call

When a source carries a citable pointer — a raw transcript's own
`𝐙𝐢𝐦𝐞 𝐫𝐞𝐜𝐨𝐫𝐢𝐧𝐝𝐢𝐧𝐠:` URL at the call header, or an insight export's per-item
evidence URL — a fact pulled from it gets a trailing linked citation, not a
bare parenthetical:

- Raw transcript: link is the whole call's recording URL. Every fact drawn
  from that call links to the same URL — coarse (call-level, not
  timestamp-level), since that's the only pointer a raw transcript offers.
- Insight export: link is that item's own evidence URL when present, finer
  than the call-level link.
- Placement: append after the fact as a small linked marker, e.g. "...absent
  from every call since (08 Jun) \[[source](URL)\]" — the fact's own text
  stays plain, matching the word-budget rules below; the marker is not a
  second fact.
- If a fact draws on more than one source, cite the first/primary one only —
  don't stack links.
- No pointer in the source (most raw transcripts without a recording URL,
  and both existing ground-truth samples) → no citation at all. Never invent
  one.

**Fail-safe: default is no marker, not a broken one.** This is additive
formatting on top of an otherwise-complete fact — a missing or malformed
link must never take the fact down with it. Concretely:
- A URL must be copied verbatim from the source, character for character.
  Never construct, complete, or guess one from a partial ID, a call title,
  or a pattern seen on another call ("this one's probably .../recordings/N+1").
  If the copy would be uncertain, that's the same as no pointer — omit the
  marker.
- Never emit the `[source](...)` bracket/paren syntax with an empty, `TBC`,
  or placeholder URL inside it — that renders as a dead link or literal
  brackets in the doc, worse than the plain fact alone. If there's no real
  URL, skip the whole marker, not just the URL portion.
- One malformed or missing link on one fact is never a reason to withhold
  the fact itself, blank the field, or fall back to an unknown marker
  (`TBC`) — the fact still stands on its own evidence per the normal rules
  above; the citation is strictly optional decoration on top of it.
- When genuinely unsure whether something in a source is a real recording
  URL (vs. a Drive link, a Slack link, or other artifact link meant for a
  different field), treat it as not a citable pointer — false negative
  (no citation) is always the safe failure, never a false positive (linking
  to the wrong artifact).

This is new behavior beyond the astra/truefoundry ground-truth samples,
which predate this rule and carry zero citations — don't treat their
absence of links as a mismatch to fix.

## Specificity survives compression — the rule behind the two below

A general failure mode, found by tracing two separate Fyno misses back to
one cause: the skill had *found* the underlying claim in both cases (an
experience gap; a champion-doesn't-guarantee-close risk) and then, while
compressing the field to budget, kept the abstract restatement and dropped
the concrete evidence that made it checkable — a number in one case, two
named accounts in the other.

**The predicate:** before finalizing any field, check whether it still
contains the specific noun, number, date, or name the source actually gave,
or only your restatement of it. If only the restatement survived, put the
specific back — cutting connective prose from around it — before applying
any word budget. This is the general form; "Keep the number" below and
`miss-prone-fields.md`'s named-account rule are its two known instances so
far, each with category-specific handling (how to normalize a spoken number;
how to avoid importing an unrelated anecdote) that the general form alone
doesn't cover. Treat any future miss that fits this shape (a verbatim quote,
a competitor name, a job title, a specific date) as a third instance of this
same rule, not a new one-off patch.

## Numeric / dated claims

Every price, headcount, or date pulled into the doc must be traceable to a
specific call in the pasted input set. If two calls disagree (e.g. cohort
size stated differently on two dates), use the most recent value but always
name the discrepancy inline — e.g. "10 (updated from 5 on the earlier call)"
— never silently pick one. A scope or number that changed mid-cycle is
itself a signal CS should see, not noise to suppress.

**Keep the number, don't paraphrase it into a duration** (instance of the
specificity rule above). When a source states a specific quantity tied to a
claim (call/deal volume, headcount, %, ₹/$ amount, a ratio), carry the
number itself into the doc — never convert it into a qualitative or
duration-only phrase. If the speaker's own point is a contrast, keep both
sides of it. Worked example (Fyno, Rohit Jain): the transcript states
*"~1,000 calls, my team would have had 10-15"* — the field should read
"~1,000 calls vs. 10-15 for his team", not "4 years of founder-led judgment"
(the duration alone drops the concrete, quotable stat). Numbers spoken as
words ("thousand calls") are normalized to digits; add `~` when the speaker
was visibly approximating, not stating an exact count.

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

§2's "Sales motion/Team size", "Sales tools", and "Team structure" describe
the *client's* existing sales organization as stated on a call — not Zime's
proposed process or the POC's own structure. Watch for the two getting
mentioned in the same call and attributed to the wrong side.

§1's "Pilot cohort" is the client's **team headcount** running the POC (e.g.
"7 reps") — the same population as §2's Team size, not the count of
accounts/deals the POC will analyze. Both ground-truth samples fill it this
way; a field-audit re-run independently picked the accounts/deals reading on
two fresh generations, so this is stated explicitly now rather than left to
be inferred from the field's short label.

§4's "Primary pain" is easy to conflate with "Key hooks that landed" —
Primary pain is the problem stated in the client's own words/situation
(something broken or costly *before* Zime), not the capability that resolved
it; the capability belongs in "Key hooks" instead.

A field that would run over budget gets trimmed, not split across cells or
padded with connective prose. No preamble inside any field ("It appears
that…", "Based on the calls…", restating the field's own label before
answering it) — go straight to the fact. Trim connective prose first — a
stated number or a named account (see "Numeric / dated claims" above and
`miss-prone-fields.md`'s risk checklist) is the last thing cut, never the
first; those are the concrete, quotable content the budget exists to
protect room for.

## "Any additional context" (§10) and appendix

§10 takes miscellaneous evidenced detail that doesn't fit §1–§9 — travel
dates, personal context, org-chart color. Still grounded: no filler sentence
about "the team seems engaged" without a specific transcript line behind it.
The trailing appendix (Upsell/Churn/Action-item types) renders only when a
transcript contains that level of explicit tribal-knowledge walkthrough —
see `handover-template.md` for the omit-vs-include rule.
