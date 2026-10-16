# Web-harvested ground-truth sources

Public citation registry for `evals/gt-web/` — see its `README.md` for what
qualifies and how this is used. Every row here should be independently
checkable: the URL should resolve and should actually contain the
attributed critique.

| Skill | Dimensions grounded | Author / org | URL | Published | Retrieved | Why it qualifies |
|---|---|---|---|---|---|---|
| deep-discovery | 8 Competitive landscape and 9 Rapport & engagement (2 quotes) | Rob Snyder, The Physics of Startups | https://youtu.be/9a78RWkaALM | 2026-06-12 | 2026-10-16 | Named expert, dated, real recorded call with his verbatim critique in the video transcript; customer feedback given with permission |
| deep-discovery | 1 Pain & business impact and 2 Current state & tooling (4 quote mappings) | Rob Snyder, The Physics of Startups | https://www.youtube.com/watch?v=RfOoKwP9hWE | 2026-06-12 | 2026-10-16 | Same expert and event; real call, verbatim critique |

## Second harvest pass: 2026-10-16, one expert, thin coverage

Found Rob Snyder's three public teardowns of Sliq sales calls (published
2026-06-12): https://youtu.be/3TsrrMSXIfg, https://youtu.be/9a78RWkaALM,
https://www.youtube.com/watch?v=RfOoKwP9hWE. He is a named expert. The
posts are dated. Each video has a transcript with the real call and his
critique.

Process, in four steps:

1. A harvester copied his critique sentences word for word. We then checked
   every quote against freshly downloaded captions and dropped 5 that did
   not match. 61 quotes remain.
2. A separate segmenter marked which timestamps are the call itself. We
   checked that the call-only text shares no 6-word run with any quote.
3. A separate mapper, blind to skill output, linked quotes to rubric
   dimensions only where his words are explicit.
4. Quotes stay in gitignored files. Only this registry is public.

Result: 6 quote-to-dimension links. All are for `deep-discovery`. None are
for `pain-finder`, and none come from the first video. His rubric is the
PULL framework, so most of his advice (demo length, positioning, website)
does not address these rubrics and stays unmapped. Five of the nine
`deep-discovery` dimensions have no supporting quote. This is one rater, so
it cannot check the judge. It is a smoke test, not an accuracy number. We
still need human-labeled cases (see `evals/framework/README.md` and
`calibrate.py`).

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
