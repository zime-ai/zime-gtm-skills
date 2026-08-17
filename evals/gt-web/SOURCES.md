# Web-harvested ground-truth sources

Public citation registry for `evals/gt-web/` — see its `README.md` for what
qualifies and how this is used. Every row here should be independently
checkable: the URL should resolve and should actually contain the
attributed critique.

| Skill | Dimensions grounded | Author / org | URL | Published | Retrieved | Why it qualifies |
|---|---|---|---|---|---|---|
| _(none — first harvest pass found no qualifying source, see below)_ | | | | | | |

## First harvest pass: 2026-08-14, zero qualifying sources

Searched for publicly published, transcript-attached, named-expert call
critiques mapping to `meddicc`, `challenger`, `sandler`, `bant`, `faint`,
`deep-discovery`, `pain-finder`. Result, honestly:

- **30MPC (30 Minutes to President's Club) cold-call teardowns** — real
  calls, named critics (Armand Farrokh, Nick Cegelski, guest experts), but
  audio/video only. No published transcript of either the call or the
  critique was found, so there's no text to extract a quote from or point
  a skill at as a transcript input.
- **Gong Labs / Chris Orlob-style content** — real call data underlies it,
  but published as aggregate statistics ("519,000 calls show...") or
  isolated tactic examples, never a single call's full transcript with a
  critique of that specific call. Doesn't fit the "one transcript, one
  critique" shape this mechanism needs.
- **Gong Research's "Call Playbook" dataset** (`gong-io/call-playbook`,
  paper: Rotman et al., "Distilling Examples into Task Instructions,"
  arXiv:2606.15641, 2026) — the closest real match: real anonymized
  enterprise call excerpts, human-labeled for Business Goals, Decision
  Criteria, Decision Makers, Decision Making Process, and Pain Points,
  which map cleanly onto `meddicc`'s and `pain-finder`'s rubric dimensions.
  **Rejected**: the dataset itself is gated (requires signing in and
  agreeing to share contact info) and licensed "Gong License (proprietary)"
  per its Hugging Face page, not an open license. Using gated, proprietary
  third-party data without going through that agreement — something this
  pass is explicitly not supposed to need a human for — isn't appropriate
  here, and reproducing even a few of its examples would still be
  republishing another company's gated content. Named here for the record,
  not used.
- **Discovery-call "breakdown with commentary" YouTube content** — mostly
  either scripted/mock calls (coaching/consulting niches, not B2B SaaS) or
  general technique videos, not a real B2B call + named-expert critique
  pair.

Net: the scope decision made with the user going in — "this is scarce,
probably 5-15 usable sources, not one per skill" — undershot even that
floor on this pass. No skill has a Tier 0/3 number from `evals/gt-web/`
yet. See `evals/SCORECARD.md` for what this means for reported coverage,
and re-run this search periodically — new call-coaching content publishes
transcripts occasionally (e.g. Substack/blog teardown posts), it's a
timing gap, not a structural dead end.
