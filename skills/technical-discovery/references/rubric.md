# Technical discovery rubric

This rubric has seven dimensions. They show whether a technical evaluation or proof of concept (POC) is set up to succeed, or scoped on hope.

Three rules apply to every dimension.

- **The buyer must say it.** Evidence is something the buyer said. A claim from the rep does not count. A system that the rep assumes the buyer runs does not count.
- **Absence is a result.** A dimension that the call never touched is Missed. Do not credit it because the rep seemed prepared.
- **Read the "does not count" line.** Each dimension lists the usual false positives. Read that line before you write Covered or Partial.

## 1. Current technical environment mapped

**What it is.** What is in place today: systems, integrations, data sources, and the deployment model (on-premises, cloud, hybrid). Any solution must work alongside these.

**Covered looks like:** the buyer names specific systems and describes how data or workflow moves through them today. **Partial looks like:** a system is named but not described in enough detail to scope around. **Missed looks like:** the call never sets a technical baseline. A POC scoped without a baseline is a guess.

**Does not count:** a vague phrase such as "we have a lot of legacy stuff". A list of systems that the rep read from the CRM and the buyer did not discuss.

**A strong call** asks the buyer to trace one record from where it starts to where it ends.

"We are on an older on-prem system, with a nightly batch export to a data warehouse" is Covered. "We have a bunch of legacy stuff" is Missed.

## 2. Future-state vision

**What it is.** The buyer holds a specific technical picture of what "working" looks like. The picture goes beyond business outcomes. It names the architecture, the latency, or the workflow change that the buyer imagines.

**Covered looks like:** a concrete technical target, such as "real-time sync instead of a nightly batch". **Partial looks like:** a directional wish ("faster would be nice") with no specific shape. **Missed looks like:** no future-state picture surfaces.

**Does not count:** the rep's own architecture diagram. A business outcome with no technical shape ("grow revenue").

**A strong call** asks what the buyer sees on day one after launch and how that differs from today.

## 3. POC scope clarity

**What it is.** The call discusses a POC and sets a specific, bounded scope. The scope says what is tested, over what period, against what data, and under what constraints. An open-ended "let us try it out" is the weak case.

**Covered looks like:** the buyer states what must be proven and what data the POC runs against. The buyer also names any hard limit on how it touches existing systems. **Partial looks like:** the goal is named and the boundaries (data, systems, non-negotiables) stay vague. **Missed looks like:** the POC has no defined scope.

**Does not count:** interest in "a pilot" with no boundary. A scope that only the rep wrote down.

**A strong call** asks what the POC must not touch and what data it needs on the first day.

"That we can get near-real-time data into our warehouse without touching our core scheduling system directly, that is our biggest constraint" is Covered. "Let us just see how it goes" is Missed.

## 4. Technical stakeholders identified

**What it is.** The people who will judge this technically are named and engaged. They can be architects, IT, security, or data owners. The alternative is a conversation with a business buyer only.

**Covered looks like:** a specific technical owner is named, with a stated role in judging the outcome. **Partial looks like:** a technical team is mentioned in general terms ("someone from data engineering looks at this") with no name. **Missed looks like:** no technical stakeholder is ever identified on a deal where one plainly matters.

**Does not count:** a job title with no stated role in the evaluation. A technical person who is on the call but whom the buyer does not name as an evaluator.

**A strong call** asks whether the technical owner will join the next call and what that person needs to see.

"Our data engineering lead, Priya, needs to sign off on the integration approach" is Covered. "IT probably wants to weigh in eventually" is Partial.

## 5. Success metrics for the evaluation

**What it is.** An agreed, specific bar exists for what counts as a successful technical evaluation. The buyer defines it before the work starts. The bar is a measurable threshold and not a feeling.

**Covered looks like:** a specific metric and a threshold, tied to a dataset or a time window. **Partial looks like:** a metric without a threshold, or a threshold with no way to measure it. **Missed looks like:** success is never defined in measurable terms.

**Does not count:** a benchmark that the vendor sets. "Looks good" or "feels faster".

**A strong call** asks the buyer to say what result means go and what result means stop.

"Sync latency under 15 minutes on a sample dataset over two weeks is a clear win for us" is Covered. "We just want it to feel faster" is Missed.

## 6. Resourcing for the evaluation

**What it is.** The buyer has the internal time and access to run a POC. Someone supplies test data, sets up access, and joins check-ins. Without them, the POC is likely to stall on the buyer's side.

**Covered looks like:** a named person with a stated time commitment. **Partial looks like:** the buyer says resourcing is needed but names no person and no amount of time. **Missed looks like:** nobody on the buyer's side agreed to do the work.

**Does not count:** "IT will handle it" with no name. Silence on who does the work. Readiness is not the same as a commitment.

**A strong call** asks who provides the data and who has access rights, and for how many hours a week.

## 7. Clear next technical step

**What it is.** The call ended with a specific next step, such as a scoping document, a scheduled kickoff, or named attendees. The weak case is a general "sounds interesting".

**Covered looks like:** a specific deliverable and a date, with named attendees. **Partial looks like:** a next step is agreed in principle with no date and no owner. **Missed looks like:** the call ends with no concrete follow-up.

**Does not count:** "let us reconnect sometime". A promise by the rep to look into something, with no owner and no due date.

**A strong call** ends with a proposed day, the people who must attend, and an agenda.

## Reads-well-too test

Run this test in both directions before you finalize an audit.

- A call that you know led to a well-scoped, successful POC must not come back mostly Missed. When it does, widen what counts as evidence.
- A call that never raised a dimension must not get credit for it. When a status rests on a line from a "does not count" list, remove that status.

## Sources

The dimensions follow common solution-engineering practice for scoping a technical evaluation. The evidence rules and the "strong call" lines come from reviews of recorded sales calls.
