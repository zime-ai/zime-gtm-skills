# Gold label: follow-up-email-drafter-demo, reference email + grounding notes

Written from `evals/illustrative/BRIEF-follow-up-email-drafter.md`'s
construction. Shape C (document-writer) — graded by claim-level diff:
does each claim's phrasing (stated fact vs. proposal) and grounding tag
match what was actually agreed on the call.

## Expected email (reference shape, wording may vary)

Subject: Following up — Brightline Goods technical deep-dive

Body, in substance:
- Recaps that today's forecasting is entirely spreadsheet-based, rebuilt
  monthly, and that seasonal spikes are where it breaks down most —
  stated as fact (heard).
- Confirms the technical deep-dive with the data team next Tuesday at
  2pm, and that a calendar invite is coming — stated as an agreed next
  step (heard).
- Raises finance involvement as a **suggestion**, not an agreed step —
  e.g. "Whenever it's useful, it might help to loop in someone from your
  finance side for the budget conversation — happy to set that up
  whenever you've got a name in mind." Must not read as already agreed.
- Does not state a specific budget-cycle date — if Q1 timing is
  mentioned at all, it's phrased as loose/tentative ("sometime in Q1"),
  never "your Q1 budget cycle" as a settled fact.

## Expected grounding notes

| Claim | Tag | Source |
|---|---|---|
| Forecasting is spreadsheet-based, rebuilt monthly | Heard | "it's entirely spreadsheet-based right now... rebuilds the forecast monthly from scratch" |
| Seasonal spikes are the main breakdown point | Heard | "Mostly around seasonal spikes — the manual model doesn't adapt fast enough" |
| Technical deep-dive, Tuesday 2pm, data team + Marcus | Heard | "Next Tuesday at 2pm works for our data lead and me." |
| Looping in finance for budget conversation | Proposed | Marcus said "let me think about who'd be right for that" — not an agreement to include anyone yet |
| Budget planning timing | Proposed / omit | "Sometime in Q1, but it's not locked yet" — not firm enough to state as a fact |

## The trap a weak run fails

Writing "I'll loop in your finance team as we discussed" or similar,
treating Marcus's "let me think about who'd be right for that" as
agreement. It's the opposite — Marcus is holding off on naming anyone.
The email must phrase this as the rep's own suggestion or leave it out
entirely, and the `Heard`/`Proposed` tag must never appear inside the
email body itself.

## Not present: reporting any of these is a hallucination

- No dollar figure, contract term, or specific budget number anywhere on
  the call.
- No named finance contact — Marcus never names anyone.
- No specific calendar date for the budget conversation beyond "sometime
  in Q1."
