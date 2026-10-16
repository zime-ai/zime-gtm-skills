#!/usr/bin/env python3
"""Build planted-fact test cases for the deep-discovery skill.

The answer key is true by construction, not by anyone's opinion: each call is
assembled from modules, one per rubric dimension, at a known level (full,
partial, absent). Twin cases remove exactly one module, so the skill's status
for that dimension must change and nothing else may.

Dimension 9 (rapport) is not planted. Rapport is a property of the whole call,
so a module cannot set it cleanly.

Writes transcripts to evals/transcripts/, keys to evals/gt-synth/, and cases to
evals/cases/deep-discovery-synth.yaml. All three folders are gitignored. Run
`python3 evals/synth/deep_discovery.py` from the repo root to rebuild them.
"""
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "evals"

DIMS = {
    1: "1. Pain & business impact",
    2: "2. Current state & tooling",
    3: "3. Trigger",
    4: "4. Desired outcome",
    5: "5. Decision process",
    6: "6. Budget",
    7: "7. Procurement",
    8: "8. Competitive landscape",
}

# level -> list of (speaker, line). An empty list means the dimension never comes up.
MODULES = {
    1: {
        "full": [("Rep", "What is the biggest problem on your side right now?"),
                 ("Buyer", "Late first replies. Our support leads spend about 12 hours a week chasing tickets that sit unassigned, and anything waiting over four hours ties to roughly 6% of our monthly churn."),
                 ("Rep", "Is that number from your own reporting?"),
                 ("Buyer", "Yes, finance pulled it last quarter, and it comes up in every review.")],
        "partial": [("Rep", "What is the biggest problem on your side right now?"),
                    ("Buyer", "Late first replies are a problem for us."),
                    ("Rep", "Okay, noted.")],
        "absent": [("Buyer", "We are always looking to improve how the team works.")],
    },
    2: {
        "full": [("Rep", "How do tickets get assigned today?"),
                 ("Buyer", "They land in one shared Zendesk queue. Two leads read it every morning, tag each ticket by product line, and drag it to an agent. Overnight tickets wait until 8 a.m.")],
        "partial": [("Rep", "How do tickets get assigned today?"),
                    ("Buyer", "We handle it with some internal tools.")],
        "absent": [],
    },
    3: {
        "full": [("Rep", "Why look at this now?"),
                 ("Buyer", "We launch in two new countries on March 1, and ticket volume will roughly double.")],
        "partial": [("Rep", "Why look at this now?"),
                    ("Buyer", "We would like to get something in place soon.")],
        "absent": [],
    },
    4: {
        "full": [("Rep", "What would a good result look like?"),
                 ("Buyer", "First replies under one hour for 90% of tickets, and the leads out of the morning sorting job.")],
        "partial": [("Rep", "What would a good result look like?"),
                    ("Buyer", "We just want it to be easier for the team.")],
        "absent": [],
    },
    5: {
        "full": [("Rep", "Who else would be involved in a decision like this?"),
                 ("Buyer", "Priya Nair, our VP of Customer Experience, signs off on anything over 20 thousand. Ken from IT reviews integrations. I would bring it to her after a demo.")],
        "partial": [("Rep", "Who else would be involved in a decision like this?"),
                    ("Buyer", "My team would need to weigh in on this.")],
        "absent": [],
    },
    6: {
        "full": [("Rep", "How are you thinking about budget and timing?"),
                 ("Buyer", "We set aside 40 to 50 thousand for this year, already approved in the plan, and we need to decide by the end of January.")],
        "partial": [("Rep", "How are you thinking about timing?"),
                    ("Buyer", "We want to decide by the end of January.")],
        "absent": [],
    },
    7: {
        "full": [("Rep", "Anything on your side before a new vendor can start?"),
                 ("Buyer", "Anything new goes through a security review with our infosec team, which takes about three weeks, and legal has to sign the data processing agreement.")],
        "partial": [("Rep", "Anything on your side before a new vendor can start?"),
                    ("Buyer", "There is a procurement process we would have to go through.")],
        "absent": [],
    },
    8: {
        "full": [("Rep", "Are you looking at anything else?"),
                 ("Buyer", "We looked at the routing built into Freshdesk. It is the default if nothing else works, but its rules do not handle language, which is our gap.")],
        "partial": [("Rep", "Are you looking at anything else?"),
                    ("Buyer", "We are looking at a couple of options.")],
        "absent": [],
    },
}

OPEN = [("Rep", "Thanks for making time, Marcus. I will keep this to a conversation about how your team works."),
        ("Buyer", "Sounds good. I run support operations at Harbor Retail, about 60 agents across three shifts.")]
CLOSE = [("Rep", "I will send a short summary and we can pick a time to continue."),
         ("Buyer", "Works for me, thanks.")]

EXPECT = {"full": "Covered", "partial": "Partial", "absent": "Missed or Unclear"}


def render(levels):
    lines = list(OPEN)
    for d in DIMS:
        lines += MODULES[d][levels[d]]
    lines += CLOSE
    out = ["Discovery call: Harbor Retail x Lumen Desk",
           "Participants: Marcus Lee (Director of Support Operations, Harbor Retail), Dana Cole (AE, Lumen Desk)",
           "[Synthetic transcript for evaluation only. No real company or person]", ""]
    t = 1
    for who, text in lines:
        out.append(f"{t // 60:02d}:{t % 60:02d} {who}: {text}\n")
        t += 14 + len(text) // 9
    return "\n".join(out)


def key(levels):
    out = ["# Planted-fact answer key, true by construction (evals/synth/deep_discovery.py)",
           "# Dimension 9 (rapport) is not planted and is not keyed.", ""]
    for d, name in DIMS.items():
        lvl = levels[d]
        out.append(f"## {name}")
        out.append(f"Expected status: {EXPECT[lvl]}")
        buyer = " ".join(t for w, t in MODULES[d][lvl] if w == "Buyer")
        out.append(f'Planted evidence: "{buyer}"' if lvl != "absent" and buyer else
                   "Planted evidence: none. Nothing in the call addresses this dimension.")
        out.append("")
    return "\n".join(out)


def cases():
    full = {d: "full" for d in DIMS}
    yield "synth-dd-all-full", "happy-path", dict(full)
    yield "synth-dd-all-partial", "ambiguous", {d: "partial" for d in DIMS}
    yield "synth-dd-all-absent", "missing-context", {d: "absent" for d in DIMS}
    for d in DIMS:
        yield f"synth-dd-twin-no-{d}", "missing-context", {**full, d: "absent"}
    rng = random.Random(7)
    for i in range(1, 7):
        yield f"synth-dd-mixed-{i}", "ambiguous", {d: rng.choice(["full", "partial", "absent"]) for d in DIMS}


def main():
    for sub in ("transcripts", "gt-synth", "cases"):
        (ROOT / sub).mkdir(exist_ok=True)
    yml = []
    for name, tier, levels in cases():
        (ROOT / "transcripts" / f"{name}.txt").write_text(render(levels))
        (ROOT / "gt-synth" / f"{name}--deep-discovery.md").write_text(key(levels))
        yml.append(f"""- description: {name}
  vars:
    skill: deep-discovery
    transcript: {name}
    gt: {name}--deep-discovery.md
    gt_dir: gt-synth
  metadata:
    skill: deep-discovery
    tier: {tier}
  assert:
    - type: python
      value: file://framework/judge.py
""")
    (ROOT / "cases" / "deep-discovery-synth.yaml").write_text("\n".join(yml))
    print(f"wrote {len(yml)} cases")


if __name__ == "__main__":
    main()
