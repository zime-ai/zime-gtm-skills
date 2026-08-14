# Gold-label transcript briefs

Handoff for Tier 3 (see `EVALS.md`). Three situation briefs, one per
vertical, deliberately **not** written by whoever authors rubrics, so the
resulting transcripts aren't contaminated by knowing what the rubric hunts
for. Give a brief to whoever writes the transcript (you, a teammate, or a
lightly-anonymized real call); they should not read `references/rubric.md`
or `skills/vertical-context/references/<vertical>.md` first.

Each transcript needs, by construction:

- At least one real, specific pain **not currently in any rubric bucket**
  (a genuine pain that doesn't fit MEDDICC, pain-finder's five buckets, or
  the vertical pack's specialized variant): call it "the unbucketed thing."
- At least one rubric dimension the call **plausibly doesn't cover** (a
  legitimate "Not applicable" / "Unclear," not a gap disguised as a miss).
- One clearly-downplayed secondary signal (something the speaker raises but
  explicitly says isn't the real issue): this is what separates a
  High-confidence finding from a Low one in `pain-finder`.

## Brief 1: Cybersecurity

Situation: a mid-market company (50-500 employees) whose security function
is 2-4 people, on a second or third call with a vendor. Trigger for the call
should be something operational (a near-miss, an audit finding, a staffing
problem), not "we're doing a vendor bake-off." Include a compliance/audit
angle (SOC 2, cyber insurance, PCI) but have the speaker treat it as
secondary to the operational pain.

## Brief 2: Healthcare / life sciences

Situation: a clinic or small health system's practice manager or IT lead,
first or second call. Trigger should involve a documentation, compliance,
or clinical-workflow pain, not a generic "we want to modernize." Include a
BAA/compliance-gate detail explicitly, and one clinical-staff-burnout signal
raised but downplayed relative to the main pain.

## Brief 3: Fintech / financial services

Situation: a fintech company's Head of Risk/Compliance or a finance-ops
lead, mid-stage call (post-first-call, pre-technical-deep-dive). Trigger
should be a scale problem (manual reconciliation breaking down as volume
grows) or a regulatory/banking-partner requirement, not generic interest.
Include a vendor-risk-assessment detail and one growth-pressure signal
raised but treated as secondary.

## Gold-label format, per transcript

Once a transcript exists, gold-label it (by a human, ideally not the
transcript author either) into `evals/gold/<vertical>.md`:

```markdown
## Findings a human expert marked (ranked)
1. <finding>: must be found. Quote: "<quote>"
2. …

## The one a weak rep misses
<finding>: skill gets credit only if it surfaces this

## Dimensions that legitimately do not apply
<dimension>: correct behavior is to say so, not force it in

## Not present: reporting any of these is a hallucination
<plausible-but-absent finding>
```

Once all three exist, Tier 3 scoring (recall/precision per skill against
these gold files) can run, see `EVALS.md`.
