# Zime Ignite / Sales → CS Handover Template

Canonical empty form, reconciled from two filled samples (Astra Security,
TrueFoundry). Structure only — every field below is filled from transcript
evidence per `grounding-rules.md`, never invented. Preserve this exact
markdown table shape (one-row tables, `| :---- |` separators, checkbox list)
in generated output.

```markdown
**Zime Ignite**

**Sales → CS Handover Template**

*Complete this before handing over to CS. CS will not accept the handover until all required fields are filled and all links are shared.*

| Handover by (Sales) | *{name}* | Handover date | *{DD/Mon/YYYY}* |
| :---- | :---- | :---- | :---- |

| Handover to (CS) | *{name}* | CS Owner | *{name}* |
| :---- | :---- | :---- | :---- |

| Company Drive folder | {link} |
| :---- | :---- |

| POC resources sheet - Call recordings, exit criteria, Tribal knowledge | {link} |
| :---- | :---- |

| Sales Deck | {link} |
| :---- | :---- |

|  | Handover acceptance checklist |
| :---: | :---- |

| *Sales completes the checkboxes. CS validates and accepts only when all items are confirmed. If anything is missing, POC start date is pushed — not the scope.* |
| :---- |

- [ ] NDA signed
- [ ] POC charter signed by DM
- [ ] NDA/POC charter links are updated in the onboarding tracker - Status is Done
- [ ] Day 28 silence clause acknowledged in writing
- [ ] **Client Objections** – What objections or blockers could impact POC success, and how should each be handled?
- [ ] Client initiative confirmed — specific behavior or outcome with ROI target
- [ ] Deal stage identified for POC brain
- [ ] Exit criteria of the deal stage — filled in the Google Sheet
- [ ] API access confirmed OR Sample calls to build the brain received (Sample call details sheet filled and link shared — Zime has download access, including Tribal knowledge / Existing playbooks if any)
- [ ] Playbook resources (Tribal knowledge / Existing playbooks / QBR and onboarding SOPs if any)
- [ ] Decision maker name, role, and Day 14 demo slot confirmed
- [ ] Champion name and seniority confirmed
- [ ] Company Drive folder created and shared with {current ops contacts} (add all client-related documents/sheets in the folder)
- [ ] Slack channel created and {current ops contacts} added
- [ ] What NOT to do list completed — client sensitivities documented
- [ ] At least one open question or risk flagged for CS (or explicitly confirmed as none)

| CS accepts this handover | *Yes / No — if No, list gaps below* | Acceptance date | *DD/Mon/YYYY* |
| :---- | :---- | :---- | :---- |

**Open gaps — to be resolved by Sales before CS accepts**

| {gap list, one per line} |
| :---- |

| 1 | Legal and commercial status |
| :---: | :---- |

| NDA | *{status}* | POC charter | *{status}* |
| :---- | :---- | :---- | :---- |

| Post-POC commercial terms | *{terms}* |
| :---- | :---- |

| Pilot cohort | *{size and description}* |
| :---- | :---- |

| 2 | Client context |
| :---: | :---- |

| Client name and website | *{name - url}* |
| :---- | :---- |

**What they do**

| *{description}* |
| :---- |

| Sales motion | *{motion}* | Team size | *{size}* |
| :---- | :---- | :---- | :---- |

**Team structure**

| *{structure}* |
| :---- |

| Sales tools | *{tools}* |
| :---- | :---- |

| 3 | Stakeholders |
| :---: | :---- |

| Name | Title | Role in POC | Motivation | CS posture |
| :---- | :---- | :---- | :---- | :---- |
| {row per stakeholder} |

| Day 7 discovery call slot confirmed with DM / Champion | *{status}* |
| :---- | :---- |

| Day 14 demo slot confirmed with DM | *{status}* |
| :---- | :---- |

| Who must NOT be engaged during POC and why | *{answer}* |
| :---- | :---- |

| 4 | Why Zime — what closed the POC |
| :---: | :---- |

| *Be specific. These hooks become the narrative CS uses in every client interaction.* |
| :---- |

**Primary pain**

| *{pain}* |
| :---- |

**Key hooks that landed**

| *{hooks}* |
| :---- |

**What Sales committed to delivering**

| *{commitments}* |
| :---- |

**What was NOT committed — defer to post-POC**

| *{exclusions}* |
| :---- |

| 5 | POC initiative and success criteria |
| :---: | :---- |

| Primary initiative | *{initiative}* |
| :---- | :---- |

| ROI they are targeting | *{roi}* |
| :---- | :---- |

| Deal stage the POC will focus on | *{stage}* |
| :---- | :---- |

**POC success criteria**

| *{criteria}* |
| :---- |

**Secondary use cases — post-POC only, do not pursue during POC**

| *{secondary}* |
| :---- |

| 6 | Current state — how they solve this today |
| :---: | :---- |

**How reps currently record and review calls**

| *{answer}* |
| :---- |

**How CRM is updated today**

| *{answer}* |
| :---- |

**What has been tried and failed**

| *{answer}* |
| :---- |

**Biggest gaps in current rep behavior**

| *{answer}* |
| :---- |

| 7 | Call recordings/ deal data / Sales materials and tribal knowledge |
| :---: | :---- |

| *Fill in call details in the Google Sheet and paste the link below. Ensure Zime has download access before sharing.* |
| :---- |

| Sample call details sheet | *{status/link}* |
| :---- | :---- |

| API access keys | *{status}* |
| :---- | :---- |

| 8 | Marching orders for CS |
| :---: | :---- |

**What CS and FDE should focus on first**

| *{answer}* |
| :---- |

**Key things to do in the first client interaction**

| *{answer}* |
| :---- |

**Key things NOT to do or say — client sensitivities**

| *{answer}* |
| :---- |

**Open questions / Objections / Blockers Sales could not resolve — CS to chase**

| *{list}* |
| :---- |

| 9 | Top objections? Why the deal can fail and how to handle it? |
| :---: | :---- |

| *{answer, or blank if never discussed}* |
| :---- |

| 10 | Any additional context - not covered above |
| :---: | :---- |

| *{answer}* |
| :---- |
```

## Trailing appendix — conditional, not part of the numbered template

Render **only** when transcripts evidence this level of tribal knowledge (a
call where the client explicitly walks through their own signal-detection or
triage habits, as Juhi did on the TrueFoundry calls). Omit entirely rather
than filling with `TBC` placeholders — an omitted appendix is not a gap; a
gap only exists inside the numbered template.

```markdown
**1. Upsell signals**

- {bullet per signal named in transcripts}

**2. Churn / negative signals**

- {bullet per signal named in transcripts}

**3. Types of action items**

- {bullet per category named in transcripts}
```

## Reconciliation notes

- "{current ops contacts}" was "AV and Sajan" (literal names) in both
  samples — templatized since who's on ops rotation isn't a per-deal fact
  and will go stale the moment either person's role changes; ask who's
  current before filling.
- Checklist item "Playbook resources (Tribal knowledge / Existing
  playbooks / QBR and onboarding SOPs if any)" is TrueFoundry-only in the
  samples; kept in the canonical checklist since it's a superset union, not
  a per-deal quirk.
- §9 "Top objections" was answered inline in Astra (folded into §8's Open
  questions/Objections block) and left blank in TrueFoundry. Canonical form
  keeps §9 as its own row; if transcripts only ever raise objections in the
  §8 sense, §9 may legitimately stay blank rather than restating §8 — that's
  not a gap, it just means no distinct "why this deal could fail" narrative
  was surfaced on calls.
