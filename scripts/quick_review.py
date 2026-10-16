#!/usr/bin/env python3
"""Quick review for a changed skill. This repo holds skills, not app code, so the
review is short: cheap deterministic checks first, then one Haiku read of the diff.

Usage: python3 scripts/quick_review.py <skill>
Exit 0 with "OK", or exit 1 with one line per problem, each ending in a fix.
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals/synth"))


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout


def bank_terms():
    """Details that only make sense inside one test transcript. They must not leak into a skill."""
    import importlib
    terms = set()
    for p in (ROOT / "evals/synth/banks").glob("*.py"):
        if p.stem != "__init__":
            for spec in importlib.import_module(f"banks.{p.stem}").BANKS.values():
                terms.update(t.strip() for ts in spec["leak_terms"].values() for t in ts)
                terms.update(w.strip() for w, _ in spec["header"][:0])
    terms.update(["Harbor Retail", "Lumen Desk", "Marcus Lee", "Meridian Health", "Brightline", "Elena Ruiz",
                  "Zendesk", "Freshdesk", "Workday", "Priya Nair", "Amara Okafor"])
    # keep only specific details (numbers, names). Common words like 'queue' would block honest rules.
    return {t for t in terms if len(t) > 3 and (any(c.isdigit() for c in t) or t[0].isupper())} - {"January", "November", "VP of", "HIPAA"}


def main():
    skill = sys.argv[1]
    d = ROOT / "skills" / skill
    text = (d / "SKILL.md").read_text()
    problems = []
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        problems.append("SKILL.md has no frontmatter block. Restore the original frontmatter.")
    else:
        fm = m[1]
        if not re.search(rf"(?m)^name:\s*{re.escape(skill)}\s*$", fm):
            problems.append(f"frontmatter name must equal {skill}. Restore it.")
        if not re.search(r"(?m)^description:\s*\S", fm):
            problems.append("frontmatter description is empty. Restore it.")
    for ref in set(re.findall(r"`(references/[\w./-]+)`", text)):
        if not (d / ref).exists():
            problems.append(f"SKILL.md points at {ref}, which does not exist. Remove the pointer or restore the file.")
    diff = git("diff", "HEAD", "--", f"skills/{skill}")
    added = "\n".join(l[1:] for l in diff.split("\n") if l.startswith("+") and not l.startswith("+++"))
    leaked = sorted(t for t in bank_terms() if t.lower() in added.lower())
    if leaked:
        problems.append(f"added text names test-transcript details {leaked[:4]}. Rewrite the rule without them.")
    if re.search(r"(?i)co-authored|generated with|anthropic\.com|🤖", added):
        problems.append("added text contains an attribution line. Remove it.")
    if not problems and added.strip():
        prompt = ("You review a diff to one sales-call-audit skill (a markdown instruction file for an AI agent). "
                  "Block only for: (1) an instruction that contradicts another instruction in the file, "
                  "(2) text that leaks customer data or tells the agent to do something unsafe, "
                  "(3) a rule that only makes sense for one specific test call (a hard-coded company, person or number), "
                  "(4) formatting that would stop the skill from loading. Anything else is fine, including style. "
                  "Reply with exactly 'OK' or 'BLOCK: <one-line fix>'.\n\nFull file:\n" + text + "\n\nDiff:\n" + diff)
        out = subprocess.run(["claude", "-p", prompt, "--model", "claude-haiku-5-5", "--setting-sources", "project"],
                             cwd=ROOT, capture_output=True, text=True, timeout=300).stdout.strip()
        if not out.startswith("OK"):
            problems.append(out.splitlines()[0] if out else "reviewer returned nothing. Re-run the review.")
    print("\n".join(problems) if problems else "OK")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
