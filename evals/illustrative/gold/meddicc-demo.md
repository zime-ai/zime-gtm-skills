# Gold label: meddicc-demo.txt, scored against `meddicc`

Written from `evals/illustrative/BRIEF.md`'s construction, independent of
running the skill. Per-dimension read, then the Tier-3 template from
`EVALS.md`.

## Per-dimension expected read

| Dimension | Expected status | Why |
|---|---|---|
| Metrics | Covered | 89% actual vs. 95% contracted on-time rate, $40,000 penalty this quarter, target of 97%+ — specific and quoted |
| Economic buyer | Partial | Dana can approve up to $50k herself; anything above needs COO sign-off, untested — no confirmed path for a larger deal |
| Decision criteria | Missed / Partial | Only loose criterion stated: "does it stop this from happening again" (reduce dispatcher error, get above 97%) — no named evaluation criteria, no weighting |
| Decision process | Missed | No pilot process, no named steps; Dana explicitly says she doesn't know what the process would look like and hasn't talked to IT yet |
| Identify pain | Covered | SLA miss, dollar penalty, CEO got a direct call — specific, consequential, clearly stated |
| Champion | Partial, not Covered | Enthusiastic language ("this could actually fix our biggest headache") but zero internal action taken or committed to on this call — no offer to loop in IT or COO proactively, explicitly says she hasn't figured out sequencing |
| Competition | Not applicable | Dana states directly this is not a vendor search ("Just you, for now... I don't have the bandwidth to also go run a bake-off") |

## Findings a human expert marked (ranked)

1. Champion is enthusiastic language without action — must be found, and
   must not be scored Covered just because the sentiment is positive.
   Quote: "This could actually fix our biggest headache." paired with "I
   haven't figured out yet how I'd even bring this to the COO."
2. Economic buyer is unresolved above $50k — must be found. Quote:
   "Anything past that technically needs CFO or COO sign-off — I haven't
   actually run a deal like that past our COO before."
3. Decision process is genuinely undefined, not just unstated by the rep's
   question — Dana says she doesn't know. Quote: "I haven't done a vendor
   pilot for something like this before, so honestly I don't know what
   our process would look like."
4. Metrics are strong and specific — must be found and credited fully.
   Quote: "That's about $40,000 we're paying back this quarter."

## The one a weak rep misses

The succession/knowledge-transfer risk (two senior dispatchers retiring,
no one wants to learn the manual process, "It's not written down
anywhere") is a real, load-bearing pain Dana states is bigger to her than
the SLA penalty ("I lose sleep over that more than the Brightside penalty,
if I'm honest") — but it doesn't map to any MEDDICC letter. A skill that
force-fits it under Metrics or Pain and reports it as if MEDDICC had
scored it gets no credit; a skill that surfaces it as a real, out-of-rubric
finding (the way `pain-finder` is designed to, not `meddicc`) gets full
credit for noticing it at all, and should say plainly it falls outside
this rubric's seven letters rather than silently absorbing it into Pain
without flagging the mismatch.

## Dimensions that legitimately do not apply

Competition: Dana states directly there is no competitive process. Correct
behavior is "Not applicable," not an assumed "Missed" (which would imply a
competitor should have been surfaced and wasn't) or a fabricated
competitor mention.

## Not present: reporting any of these is a hallucination

- Any named competitor product or vendor (none was mentioned — a
  hallucination trap given how often "Competition" prompts a model to
  infer one).
- A confirmed COO conversation or timeline for one (explicitly not yet
  scheduled or planned).
- A specific decision-criteria list or weighting (never stated).
- IT's actual involvement or a security/pilot process (Dana says she
  hasn't talked to IT yet — reporting IT as "engaged" or a pilot as
  "planned" would be fabricated).
- A stated headcount/budget dollar figure beyond the $50,000 approval
  threshold (no other number was given).
