# zime-gtm-skills

Open-source [Claude Code Skills](https://github.com/agentskills/agentskills)
that audit sales call transcripts and CRM exports against per-motion
rubrics. Runs locally, no credentials, no data leaves your machine.

Built for RevOps engineers and sales engineers who want a structured second
opinion on call quality without wiring a live CRM connection into a
third-party tool.

## Quick start

```bash
git clone https://github.com/zime-ai/zime-gtm-skills.git
cd zime-gtm-skills
claude "run gtm-deep-discovery on skills/gtm-deep-discovery/assets/sample-transcript.txt"
```

That's a synthetic call bundled with the repo — nothing of yours required
to see real output. Expect a per-dimension audit like:

```
1. Pain & business impact — Covered
   "our lead dispatcher... spends probably 8-10 hours a week just
   chasing down exception statuses" (00:48)

2. Trigger — why now — Covered
   "we lost a mid-size account last quarter over a missed exception,
   and our board asked for a logistics-ops review this quarter" (01:30)

7. Procurement & buying path — Covered
   "anything touching our TMS goes through a security review with
   our IT director... about three weeks" (04:28)

Next steps:
- Confirm the $40k CFO threshold in writing before scoping a proposal
- Get the competing vendor's name — "felt built for a bigger company"
  is a usable wedge, worth understanding further
```

## Skills

| Skill | Audits | Input |
|---|---|---|
| `gtm-deep-discovery` | Early-stage discovery call quality — pain, trigger, decision process, budget/timeline, procurement, competition, rapport | transcript (`.txt`/`.vtt`/`.json`/`.md`) or CRM export (`.csv`) |
| `gtm-meeting-to-qualify` | Whether a deal is real — authority, budget plausibility, urgency, fit, competitive situation, concrete next step | transcript or CRM export |
| `gtm-churn-prevention` | Renewal risk — value realization, usage depth, champion strength, sentiment, service friction | transcript or CRM export |

More motions (technical discovery, demo, pilot/POC, negotiation, onboarding,
customer success, upsell/expansion) are planned — see
[CONTRIBUTING.md](CONTRIBUTING.md) if you want to help build one sooner.

## License

MIT — see [LICENSE](LICENSE).

Maintained by [Zime](https://zime.ai).
