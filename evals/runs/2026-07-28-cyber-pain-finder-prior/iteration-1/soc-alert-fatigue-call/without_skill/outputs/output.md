# Pain Point Analysis: Meridian Freight Logistics (Chris Vance)

## Bottom line

Chris's real problem isn't "we need more security tools" — it's that the tools he already has don't talk to each other, and that gap is burning out his team, creating real risk exposure, and isn't visible to his own leadership. That last point matters: he doesn't have internal air cover to fix it yet. Your follow-up should give him ammunition for that internal conversation as much as it should sell the product.

## Pain Point #1 (Primary): Alert fatigue driven by tool fragmentation, not tool quality

This is the pain he came back to twice, unprompted, and it's the most quantifiable.

- Stack: SentinelOne (endpoint), Splunk (logs), a separate email security gateway, and native AWS GuardDuty for cloud — "none of it talks to each other."
- Manual correlation is the actual workflow: four browser tabs open just to triage a single alert.
- Concrete example: a lateral movement alert took his senior analyst **almost three hours** to rule out as a false positive, because he had to manually cross-reference endpoint, network, and identity provider logs by hand.
- Scale: 50–80 alerts triaged per day, of which only 2–3 are real. This kind of cross-tool manual triage event happens **multiple times a week**, not as a one-off.

**Why it matters:** This isn't a "we want a nicer dashboard" complaint — it's hours of skilled-analyst time spent per week confirming non-events, on a team that doesn't have hours to spare.

## Pain Point #2: Team capacity and retention risk

- Nominal team is Chris + 3 analysts for a 24/7 operation; actual capacity right now is Chris + 2.5 (one analyst is out on leave).
- He describes the team as "exhausted."
- One analyst has told him directly he's job-hunting because he's tired of "chasing ghosts" (his words) — i.e., burnout from chasing false positives is an active attrition risk, not a hypothetical one.

**Why it matters:** If Meridian loses another analyst, the coverage gap gets worse and the triage burden per person goes up, compounding Pain #1. This is a business-continuity/staffing risk, not just a morale issue — worth naming explicitly in your follow-up since it's a cost leadership tends to underrate until someone actually quits.

## Pain Point #3: Real risk exposure — the near miss

- Meridian had an actual phishing-based credential compromise ~8 months ago. It was contained before causing serious damage, but it was close.
- Chris's own words: if the lateral movement alert from "last Tuesday" (the 3-hour triage case) had been a real attack instead of a false positive, **he is not confident they'd have caught it in time**, given how long triage currently takes.

**Why it matters:** This connects the operational pain (slow manual triage) directly to a plausible bad outcome (missed real intrusion), and it's backed by a real prior incident, not a hypothetical. This is the strongest "cost of inaction" argument you have — use it, but handle it factually rather than as a scare tactic since he raised it candidly.

## Pain Point #4: Leadership doesn't see the problem — no internal air cover

- When Chris asked his VP for headcount, the response was "didn't we just buy that SentinelOne thing to handle this?" — leadership believes the tool purchase already solved the problem.
- Chris is currently stuck: he can see the operational and risk problem clearly, but he doesn't have a way to make it visible or credible to leadership.

**Why it matters:** This is likely the actual buying obstacle. Even if Chris is sold, he may not be able to get budget approved unless you help him build a case his VP will accept — ideally with data/metrics his leadership will find credible (see Pain #5).

## Pain Point #5 (secondary, but useful for timing/urgency): Cyber insurance renewal

- Renewal is this fall; the insurer will likely ask about MTTR and detection coverage.
- Chris was explicit that this is **not** what's keeping him up at night — the fatigue and the near miss are the real drivers. Don't lead with this; treat it as a secondary forcing function and a source of metrics leadership already expects to be asked about.

## Recommended focus for your follow-up

1. **Lead with the triage-time story** (3 hours to clear one alert, 50–80/day, 2–3 real) — it's concrete, it's his own words, and it directly maps to whatever correlation/automation capability reduces manual cross-referencing across SentinelOne, Splunk, the email gateway, and GuardDuty.
2. **Name the near-miss explicitly** as the cost of the status quo — tie faster/automated correlation to confidence in catching a real lateral movement event, referencing the phishing compromise from 8 months ago.
3. **Give him a leadership-ready narrative**, not just a product pitch. He needs something he can bring to his VP that reframes this as "the tool we bought needs a correlation layer to actually deliver on its promise," not "the tool failed." Consider offering a simple ROI/business-case framing (analyst hours saved, retention risk, insurance readiness) he can forward internally.
4. **Use the insurance renewal as a timing anchor**, not the emotional hook — position MTTR/detection-coverage improvements as a proof point that will also happen to satisfy the fall renewal conversation.
5. Be mindful of the retention thread — mention it, but don't overplay it as the primary pitch since Chris himself framed fatigue/near-miss as the core issue.
