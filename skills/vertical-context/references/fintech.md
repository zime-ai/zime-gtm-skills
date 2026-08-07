# Fintech / financial services vertical pack

**Unreviewed** — see `SKILL.md`'s "Status: unreviewed" note.

## Typical buyer titles / who signs

Head of Risk or Head of Compliance frequently co-owns the decision
alongside a VP Engineering/Product for anything touching the product
surface; CFO or Controller for finance-ops tooling. A security review by a
CISO or vCISO is common even when they aren't the primary buyer.

## Compliance / regulatory drivers

SOC 2 Type II (often a hard prerequisite before a vendor is even
considered), PCI-DSS if touching card data, state money-transmitter
licensing, and — depending on the product — banking-partner due-diligence
requirements that can add a slow, multi-week vendor-review process
regardless of deal size.

## Specialized pain categories (variant of the generic five buckets)

1. **Regulatory / compliance pressure** — a licensing requirement, an
   examiner finding, a banking-partner requirement is driving the timeline
2. **Risk exposure** — fraud, reconciliation errors, manual reviews that
   introduce error at scale
3. **Operational friction** — manual reconciliation, spreadsheet-based
   processes handling real money movement
4. **Growth / scale pressure** — a process that worked at lower transaction
   volume breaking down as volume grows
5. **Leadership / board pressure** — a board or examiner question is driving
   urgency, not just an internal initiative

## Domain vocabulary

Reconciliation, chargeback, KYC/AML, money transmitter license, banking
partner, examiner, SOC 2, vendor risk assessment, PCI-DSS, settlement.

## Procurement shape

Vendor risk assessment is close to universal here even for small deals —
expect a security questionnaire and possibly a banking-partner sign-off
before a contract is signed, independent of the buyer's own enthusiasm.

## Disqualifying signal

The prospect has no vendor-risk or security-review process at all despite
handling real money movement — either a very early-stage company (real
opportunity, different urgency profile) or a red flag on their own
regulatory posture worth probing rather than assuming is fine.
