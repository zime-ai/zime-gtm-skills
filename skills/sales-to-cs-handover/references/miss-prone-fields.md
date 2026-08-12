# Miss-prone fields — detail for Step 3

Stakeholder mapping, persona mapping, open objections, and deal risk are the
four areas both a blind test and the person who does this by hand flagged as
where Claude reliably falls short when just handed transcripts. This file
holds the derivation checklist and worked examples that don't fit inline in
SKILL.md.

## Risk derivation checklist

Run against the inventoried sources every time, regardless of whether any
risk was named explicitly. Each hit gets a line in §9 with a one-clause
handling note — same format as an objection.

- Legal paper (NDA, POC charter, MSA) sent but unsigned.
- Economic buyer named but never present on any call — or not named at all.
- Only one stakeholder engaged across every call (single-threaded).
- Something Sales asked for (data, API access, a list) that hasn't arrived.
- Something the client may believe was committed but Sales explicitly
  deferred (check "What was NOT committed" — a live risk if the client's own
  words suggest they expect it anyway).
- A date discussed as needed (demo slot, discovery call) with no date set.
- Commercial terms floated but not finalized.
- A stakeholder who is new to their own company's systems/role, or newly
  arrived mid-cycle — their answers may not hold once someone more senior
  engages.

A checklist hit with zero evidence either way does not get invented — it's
a hit only when the sources actually show the condition (e.g. a call
explicitly says the NDA is unsigned, not "NDA status wasn't mentioned").
Absence of a topic is not evidence of the risk; only surface a risk from
what's *said*.

**Named-account anecdotes as evidence, not just the abstract risk** (instance
of `grounding-rules.md`'s "Specificity survives compression" rule — same
failure shape, different content: a concrete name instead of a concrete
number). When a source attaches a named-account story to a risk or
objection already derived above, carry the account name and its one-clause
outcome as the line's evidence instead of stating the risk abstractly.
Worked example (Fyno, Rohit Jain): "champion ≠ close — DCB Bank (champion
convinced, CEO overrode) and Federal Bank (deal stalled a year when the
approving authority changed, not the champion)." Guard: this only dresses up
a risk/objection the checklist already surfaced — a war story is not itself
a new §9 line, and this is never licence to import an anecdote unrelated to
an existing risk.

## Persona vocabulary — motivation vs. posture, personal vs. org-level

Both samples do this well; use them as the calibration. Copy the
*structure* (personal want, sourced to what that person said), not the
tool names or domain — "Fireflies," "manual review," "pentesting" etc.
below are what those specific stakeholders said, not defaults to reuse for
an unrelated client's tools.

| Bad (org-level want / adjective) | Good (personal want / behavioral instruction) | Source |
| --- | --- | --- |
| "Wants pipeline visibility" | "Pipeline hygiene and forecasting accuracy — his own stated top priority, from the 07/21 call" | Astra, Suraj |
| "Engaged and analytical" | "Asked a sharp comparison question re: Zime vs. directly prompting Claude/ChatGPT — answer his technical comparisons directly and thoroughly" | Astra, Sahil |
| "Wants to reduce manual work" | "Needs account health, open action items, upsell/renewal risk visibility without manual Fireflies review" | TrueFoundry, Juhi |
| "Supportive" | "Supportive but defers day-to-day to Juhi; wants business-level signals, not operational detail; decision maker on go/no-go" | TrueFoundry, Anuraag |

The test for "Motivation": could this sentence be copy-pasted onto a
*different* stakeholder at a different company without changing a word? If
yes, it's org-level, not personal — rewrite from what that specific person
said. The test for "CS posture": does it tell CS what to *do* the next time
they talk to this person? If it only describes a vibe, add the instruction.

## §8 "Marching orders for CS" — differentiation test

§8's four fields are easy to conflate the same way persona's Motivation/CS
posture are — a "focus first" item, a "first interaction" item, and a
"chase" item can all plausibly restate the same underlying fact. Test each
before placing it:

| Field | Test |
| --- | --- |
| "What CS and FDE should focus on first" | A work-item CS should prioritize — typically a Zime-owed action item (see the insight-export routing map below) |
| "Key things to do in the first client interaction" | A behavior/tone instruction specific to the *first* call, not a standing priority |
| "Key things NOT to do or say — client sensitivities" | A do-not instruction tied to a specific person or topic named in a source |
| "Open questions / Objections / Blockers … CS to chase" | A still-open question/objection Sales couldn't close — overlaps with §9 by design, per the reconciliation notes in `handover-template.md` |

## Insight-export routing map

When a pasted source is a Zime insight export (structured Call summary /
Action Items / Objections / Commitment and positive moments / Important
points, each with severity + evidence + a recording snippet URL), route
directly instead of re-deriving from raw prose:

| Export block | Template destination |
| --- | --- |
| Objections | §9, one line per objection with its evidence as the handling note. Still apply Answered ≠ closed — the export's own severity/status doesn't override that rule |
| Action Items | §7/§8 depending on owner — Zime-owed items to §8 "What CS should focus on first"; client-owed items to Open gaps as a transcript gap if still outstanding |
| Commitment and positive moments | §4 "What Sales committed to delivering" / "Key hooks that landed" |
| Important points | Route by content — stakeholder facts to §3, risk-shaped points through the risk checklist above, everything else to §10 |

The export's severity tags are a hint for which risks/objections matter most,
not a substitute for the derivation checklist — a low-severity export item
can still be the client's stated top priority in context.
