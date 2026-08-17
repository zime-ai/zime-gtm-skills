# Gold label: champion-tracker-demo (call-1 + call-2), reference action ledger

Written from `evals/illustrative/BRIEF-champion-tracker.md`'s construction.
This is Shape C (document-writer) — the gold artifact is a **reference
version of the ledger itself**, graded by field/row diff, not a
ranked-findings list scored by recall.

## Expected action ledger

| Contact | Call | Quote | Tag | Why |
|---|---|---|---|---|
| Marisol Vance | 1 | "I want to get this in front of our finance lead sometime soon so we can start scoping what budget this would need." | Sentiment | Stated intention, not yet done |
| Marisol Vance | 2 | "I got our finance lead looped in, walked her through the numbers myself." | Action | Looped in finance lead |
| Marisol Vance | 2 | "There was actually some pushback in our ops leadership meeting last week about prioritizing a different initiative this quarter, and I pushed back on that directly." | Action | Pushed back for the deal in a room the rep wasn't in |
| Marisol Vance | 2 | "I also set up a short call between your security team and ours for Thursday." | Action | Set up security call, removed a blocker |
| Callum Reeve | 1 | "Honestly it's exactly what we need. Our inspectors are squinting at parts under bad lighting all day, this would be a huge relief." | Sentiment | Praised the product |
| Callum Reeve | 1 | "I've been telling everyone on the floor about this. People are excited." | Sentiment | Informal enthusiasm, no internal selling action described |
| Callum Reeve | 2 | "I'm just glad this is finally moving. The team keeps asking me when we're getting it." | Sentiment | Enthusiasm, no action |

## Champion read (expected)

**Marisol Vance** is the strongest, and only, champion candidate — three
Action rows in call 2, none in call 1. Callum Reeve has zero Action rows
across both calls and should not be named a champion or champion
candidate despite consistently warm language.

## Trend (expected)

**Strengthening** — Marisol had zero Action rows in call 1 (only a stated
plan, correctly tagged Sentiment) and three in call 2, all independently
verifiable actions taken between calls (finance lead briefed, internal
pushback delivered, security call scheduled).

## The trap a weak run fails

Marisol's call-1 line ("I want to get this in front of our finance lead
sometime soon") must be tagged **Sentiment**, not Action — it is a stated
intention, structurally identical to "I'll do X soon," not a completed
act. A run that tags this Action because it sounds proactive would
overstate call 1's champion strength and blunt the strengthening trend
the two calls are built to show.

## Not present: reporting any of these is a hallucination

- Callum Reeve should never appear with an Action-tagged row — nothing he
  says in either call describes him doing something internally, only
  reacting.
- No third contact exists — only Marisol Vance and Callum Reeve speak
  across both calls.
- No specific dollar figure, contract term, or named competitor appears in
  either call — none should be invented in the ledger.
- The security call is scheduled for "Thursday," not a specific calendar
  date — no date should be fabricated beyond what's stated.
