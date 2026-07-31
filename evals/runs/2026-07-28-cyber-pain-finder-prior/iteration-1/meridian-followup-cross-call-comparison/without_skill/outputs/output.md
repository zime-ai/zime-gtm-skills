# Meridian Freight Logistics — Cross-Call Pain Point Comparison

**Call 1:** Discovery call (Dana Okafor / Chris Vance, Director of IT Security)
**Call 2:** Follow-up call, 3 weeks later (Dana Okafor / Chris Vance / Renee Kupchak, VP Operations — new attendee)

---

## Recurring Pain Points (present in both calls, unresolved)

| Pain Point | Call 1 | Call 2 |
|---|---|---|
| **Alert fatigue / manual triage burden** | 50–80 alerts/day, only 2–3 real; analysts juggle 4 tools by hand to triage a single alert | "Hasn't gotten better, if anything it's worse" — no change in root cause |
| **Disconnected tool stack** | SentinelOne, Splunk, email gateway, AWS GuardDuty — "none of it talks to each other" | Not explicitly re-described, but it's the direct cause of the repeat multi-hour triage incident described below — still unaddressed |
| **Understaffing relative to 24/7 coverage need** | Team is "3 analysts on paper," one out on leave, effectively 2.5 covering 24/7 | Same structural gap persists and has gotten worse (see Escalated) |
| **"The tool alone should fix it" mentality from leadership** | Chris's VP: "didn't we just buy that SentinelOne thing to handle this?" | Renee independently echoes the same concern from the board's side: any ask "has to come with a story about risk reduction, not just 'we bought a tool'" |
| **Multi-hour false-positive triage events** | Named example: lateral movement alert took ~3 hours to clear (senior analyst manually cross-referencing endpoint/network/identity logs) | A near-identical event recurred ~2 weeks before this call — same pattern, same root cause, not fixed |

---

## New Pain Points (surfaced only in Call 2)

1. **Board-level accountability gap.** Renee was directly asked by the board, "how would we know if we were breached right now" — and had no good answer. This is a brand-new stakeholder-level pain that didn't exist (or wasn't visible) three weeks ago.
2. **Executive reporting demand.** The CEO now wants a one-page, plain-English (no tool-jargon) security posture summary for the next board meeting. Neither Chris nor Renee feels able to produce it credibly given the current state of triage and visibility.
3. **New stakeholder in the loop.** Renee Kupchak (VP Operations) has now been pulled into security conversations — meaning this is no longer purely an IT/security problem but an operations/leadership problem too.
4. **Explicit budget constraint framing.** Renee states the company is "not a company with a blank check" — any security spend ask must be justified with a risk-reduction narrative for the board, not just tooling purchases. This is a new, more formal procurement/budget lens that wasn't part of the conversation in Call 1.

---

## Escalated Pain Points (existed in seed form in Call 1, intensified by Call 2)

1. **Staffing attrition risk → actual attrition.**
   - *Call 1:* One analyst told Chris he's job-hunting because he's tired of "chasing ghosts." Team already thin (2.5 effective).
   - *Call 2:* That analyst (or the one who'd been on leave) returned and then resigned two weeks later. Team is now down to **2 people covering what should be 4** — a real, materialized loss, not just a risk anymore.

2. **Cyber insurance exposure → real financial cost.**
   - *Call 1:* Chris flagged that the fall renewal would likely probe MTTR and detection coverage, but downplayed it ("not really what's keeping me up at night").
   - *Call 2:* Renewal terms came back with a **~30% premium increase**, and the questionnaire specifically penalized them on "mean time to detect" and "SOC coverage hours" — the exact gaps Chris had been describing internally for a year. What was a soft, anticipated concern is now a hard dollar figure tied directly to the unresolved alert-fatigue/visibility problem.

3. **Operational frustration → leadership/board visibility.**
   - *Call 1:* The triage pain was largely contained to Chris's team and invisible to senior leadership (his VP dismissed the need for headcount).
   - *Call 2:* A repeat multi-hour triage incident reached Renee secondhand and was part of what triggered her being questioned by the board. The pain has effectively climbed the org chart from an IT annoyance to a boardroom concern.

4. **Urgency/stakes.**
   - *Call 1:* Chris's biggest fear was a hypothetical — "if that lateral movement alert HAD been real, I'm not confident we would have caught it in time."
   - *Call 2:* That fear is reinforced by a second real triage failure of the same kind, plus now a board member directly questioning breach detection capability — moving from a private "what if" to an externally-visible credibility problem.

---

## Notable Non-Escalation

- The **credential compromise near-miss from ~8 months ago** (the most serious incident referenced in Call 1) has **not recurred**. Chris explicitly confirms "not something that serious, no" when asked. The active risk driver in Call 2 is the *chronic* triage/staffing/visibility problem, not a new security event.

---

## Summary Takeaway

The core technical problem (disconnected tools causing slow, manual, exhausting triage) has not changed in three weeks — but its consequences have compounded. What began as an internal team-morale and efficiency issue has escalated into: (1) a realized staffing loss, (2) a quantified financial hit via the insurance renewal, and (3) a board-level credibility and reporting problem now involving a second executive stakeholder. The sales opportunity has shifted from "help an overworked security director" to "help two stakeholders answer to the board with a defensible risk-reduction story" — a materially higher-stakes, higher-urgency conversation than three weeks ago.
