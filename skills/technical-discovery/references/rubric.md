# Technical discovery rubric

Seven dimensions for whether a technical evaluation or POC is set up to
succeed, rather than scoped on hope.

## 1. Current technical environment mapped

**What it is.** What's actually in place today — systems, integrations,
data sources, deployment model (on-prem, cloud, hybrid) — that any solution
would need to work alongside.

**Covered looks like:** the prospect names specific systems and describes
how data or workflow currently moves through them. **Partial looks like:**
a system is named but not described in enough detail to scope around.
**Missed looks like:** the call never establishes a technical baseline at
all — a POC scoped without this is guessing.

"We're on an older on-prem system, with a nightly batch export to a data
warehouse" is Covered; "we have a bunch of legacy stuff" is Missed.

## 2. Future-state vision

**What it is.** Whether the prospect has a specific technical picture of
what "working" looks like — not just business outcomes, but the kind of
architecture, latency, or workflow change they're picturing.

**Covered looks like:** a concrete technical target ("real-time sync
instead of a nightly batch"). **Partial looks like:** a directional wish
("faster would be nice") without a specific shape. **Missed looks like:**
no future-state picture surfaces at all.

## 3. POC scope clarity

**What it is.** If a POC is being discussed, whether there's a specific,
bounded scope — what's being tested, over what period, against what data
and constraints — versus an open-ended "let's try it out."

**Covered looks like:** the prospect states what must be proven, what data
it runs against, and any hard constraint on how it can touch existing
systems. **Partial looks like:** the goal is named but the boundaries
(data, systems, non-negotiables) stay vague. **Missed looks like:** the POC
has no defined scope at all.

"That we can get near-real-time data into our warehouse without touching
our core scheduling system directly — that's our biggest constraint" is
Covered; "let's just see how it goes" is Missed.

## 4. Technical stakeholders identified

**What it is.** Whether the people who'll actually evaluate this
technically — architects, IT, security, data owners — are named and
looped in, or this is still only a conversation with a business buyer.

**Covered looks like:** a specific technical owner is named, with a stated
role in evaluating the outcome. **Partial looks like:** a technical team is
referenced generically ("someone from data eng would look at this")
without a name. **Missed looks like:** no technical stakeholder is ever
identified on a deal where one plainly matters.

"Our data engineering lead, Priya, would need to sign off on the
integration approach" is Covered; "IT will probably want to weigh in
eventually" is Partial.

## 5. Success metrics for the evaluation

**What it is.** Whether there's an agreed, specific bar for what counts as
a successful technical evaluation, defined before it starts rather than
argued about after — a measurable threshold, not a feeling.

**Covered looks like:** a specific metric and threshold, tied to a dataset
or time window. **Partial looks like:** a metric is named without a
threshold, or a threshold without a way to measure it. **Missed looks
like:** success is never defined in measurable terms.

"Sync latency under 15 minutes on a sample dataset over two weeks, that's
a clear win for us" is Covered; "we'd just want it to feel faster" is
Missed.

## 6. Resourcing for the evaluation

**What it is.** Whether the prospect has the internal time and access
needed to actually run a POC — someone to provide test data, configure
access, show up to check-ins — or this is likely to stall on their side.

**Covered looks like:** a named person with a stated time commitment.
**Partial looks like:** resourcing is acknowledged as needed but not
committed to a specific person or amount of time. **Missed looks like:**
no one on the prospect's side is confirmed to actually do the work.

## 7. Clear next technical step

**What it is.** Whether the call ended with a specific next step — a
scoping document, a scheduled kickoff, named attendees — or just a general
"sounds interesting."

**Covered looks like:** a specific deliverable and date, with named
attendees. **Partial looks like:** a next step is agreed in principle
without a date or owner. **Missed looks like:** the call ends with no
concrete follow-up at all.

## Reads-well-too check

Sanity-check against a call you know led to a well-scoped, successful POC.
If it still comes back mostly Missed, loosen the read before reporting.
