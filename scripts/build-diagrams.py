#!/usr/bin/env python3
"""Builds the README diagrams from the skills' own metadata, so counts never drift.

    python3 scripts/build-diagrams.py          # write docs/img/*.svg
    python3 scripts/build-diagrams.py --check  # fail if a file is stale or a color pair is too faint

Zero dependencies. Design rules (after cathrynlavery/diagram-design): semantic color
tokens, one focal accent, no shadows, a light and a dark skin, system fonts only
(GitHub shows an SVG through an image tag, and that cannot load web fonts).
"""
import glob
import html
import os
import re
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "img")

TOKENS = {
    "light": dict(paper="#fafaf8", paper2="#f0f0ec", ink="#1f2430", muted="#4a5365",
                  soft="#5b6578", rule="#d9dad4", accent="#b8431f"),
    "dark": dict(paper="#171a21", paper2="#20242d", ink="#eceae4", muted="#b7bcc7",
                 soft="#9aa2b2", rule="#2e333e", accent="#f08a59"),
}
# (foreground token, background token, minimum ratio). Text needs 4.5. The accent line also carries text, so it is held to 4.5.
PAIRS = [("ink", "paper", 4.5), ("muted", "paper", 4.5), ("soft", "paper", 4.5), ("accent", "paper", 4.5),
         ("ink", "paper2", 4.5), ("muted", "paper2", 4.5), ("soft", "paper2", 4.5), ("accent", "paper2", 4.5)]

SERIF = "Georgia, 'Times New Roman', serif"
SANS = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

# Lifecycle columns. Every stage skill must appear here, so a new skill forces a decision.
STAGES = [
    ("Prospect and qualify", ["prospect-pipeline-check", "sql-to-qualify", "meeting-to-qualify",
                              "qualify-pipeline-check", "qualify-to-poc"]),
    ("Discover", ["deep-discovery", "persona-based-discovery", "technical-discovery"]),
    ("Demo and evaluate", ["improve-demo", "evaluation-pipeline-check", "poc-pilot-pipeline-check",
                           "poc-success", "pilot-to-conversion"]),
    ("Negotiate", ["negotiation-closing", "security-legal-review", "negotiation-pipeline-check"]),
    ("Post-sale", ["won-pipeline-check", "onboarding-journey", "customer-success",
                   "upsell-expansion", "churn-prevention"]),
]
ANY_STAGE = ["first-call-rampup", "end-client-registration", "new-business-registration"]
INTEL_EXAMPLES = ["deal-risk-digest", "forecast-review", "pipeline-review", "call-prep", "win-loss-brief", "crm-export"]


def load():
    """Return {name: {dimension, initiative}} read from every SKILL.md."""
    skills = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))):
        text = open(f).read()
        get = lambda k: (re.search(r"zime:%s: (.*)" % k, text) or [None, ""])[1].strip()
        skills[f.split(os.sep)[-2]] = dict(dimension=get("dimension"), initiative=get("initiative"))
    return skills


def esc(s):
    return html.escape(s, quote=False)


def skill_map(skin, skills):
    t = TOKENS[skin]
    stage_names = {n for n, d in skills.items() if d["dimension"] == "stage"}
    placed = {n for _, names in STAGES for n in names} | set(ANY_STAGE)
    missing = stage_names - placed
    if missing:
        sys.exit("build-diagrams.py: stage skills missing from STAGES or ANY_STAGE: " + ", ".join(sorted(missing)))
    stale = placed - set(skills)
    if stale:
        sys.exit("build-diagrams.py: STAGES names a skill that no longer exists: " + ", ".join(sorted(stale)))
    total = len(skills)
    n_stage = len(stage_names)
    initiatives = {}
    for n, d in skills.items():
        if d["dimension"] == "initiative":
            initiatives[d["initiative"]] = initiatives.get(d["initiative"], 0) + 1
    n_init = sum(initiatives.values())
    n_intel = sum(1 for d in skills.values() if d["dimension"] == "intelligence")

    W, M = 1200, 40
    col_w = (W - 2 * M) // len(STAGES)
    top = 150
    line_h = 22
    rows = max(len(names) for _, names in STAGES)
    card_y = top + 46 + rows * line_h + 34
    card_h = 190
    H = card_y + card_h + 66
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         f'aria-label="Map of {total} skills by deal stage">',
         f'<title>{total} skills by deal stage</title>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{t["paper"]}" stroke="{t["rule"]}"/>',
         f'<text x="{M}" y="54" font-family="{MONO}" font-size="12" letter-spacing="2.4" fill="{t["soft"]}">SKILL MAP</text>',
         f'<text x="{M}" y="96" font-family="{SERIF}" font-size="34" fill="{t["ink"]}">What reps skip, by deal stage</text>',
         f'<text x="{W-M}" y="96" text-anchor="end" font-family="{SERIF}" font-size="34" fill="{t["accent"]}">{total} skills</text>',
         f'<text x="{M}" y="122" font-family="{SANS}" font-size="14" fill="{t["muted"]}">'
         f'Each skill audits one thing a deal needs at that stage, and cites a quote or a cell for every finding.</text>']
    # the deal flow: one accent line with a dot at each stage
    fy = top
    o.append(f'<line x1="{M}" y1="{fy}" x2="{W-M-8}" y2="{fy}" stroke="{t["accent"]}" stroke-width="2"/>')
    o.append(f'<path d="M{W-M-10} {fy-5} L{W-M} {fy} L{W-M-10} {fy+5}" fill="none" stroke="{t["accent"]}" stroke-width="2"/>')
    for i, (label, names) in enumerate(STAGES):
        x = M + i * col_w
        o.append(f'<circle cx="{x+5}" cy="{fy}" r="5" fill="{t["paper"]}" stroke="{t["accent"]}" stroke-width="2"/>')
        o.append(f'<text x="{x}" y="{fy+30}" font-family="{MONO}" font-size="12" font-weight="600" letter-spacing="1.2" '
                 f'fill="{t["ink"]}">{esc(label.upper())}</text>')
        o.append(f'<text x="{x+col_w-18}" y="{fy+30}" text-anchor="end" font-family="{MONO}" font-size="12" '
                 f'fill="{t["soft"]}">{len(names)}</text>')
        for j, n in enumerate(names):
            o.append(f'<text x="{x}" y="{fy+56+j*line_h}" font-family="{MONO}" font-size="13" fill="{t["muted"]}">{esc(n)}</text>')
    # three cards
    gap = 20
    cw = (W - 2 * M - 2 * gap) // 3

    def card(i, eyebrow, count, lines):
        x = M + i * (cw + gap)
        o.append(f'<rect x="{x}" y="{card_y}" width="{cw}" height="{card_h}" rx="10" fill="{t["paper2"]}" stroke="{t["rule"]}"/>')
        o.append(f'<text x="{x+22}" y="{card_y+34}" font-family="{MONO}" font-size="12" font-weight="600" letter-spacing="1.2" '
                 f'fill="{t["ink"]}">{esc(eyebrow.upper())}</text>')
        o.append(f'<text x="{x+cw-22}" y="{card_y+34}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{t["soft"]}">{count}</text>')
        for j, ln in enumerate(lines):
            o.append(f'<text x="{x+22}" y="{card_y+64+j*21}" font-family="{MONO}" font-size="13" fill="{t["muted"]}">{esc(ln)}</text>')

    card(0, "Any stage and partner", f"{len(ANY_STAGE)} skills", ANY_STAGE)
    names = [f"{k} ({v})" if v > 1 else k for k, v in sorted(initiatives.items(), key=lambda kv: (-kv[1], kv[0]))]
    card(1, "Frameworks and initiatives", f"{n_init} skills", textwrap.wrap(", ".join(names), 36, break_on_hyphens=False)[:6])
    ex = [n for n in INTEL_EXAMPLES if n in skills]
    more = n_intel - len(ex)
    card(2, "Deal intelligence", f"{n_intel} skills",
         textwrap.wrap("Digests, briefs and reviews across a book of business, such as " + ", ".join(ex) +
                       f", and {more} more.", 36, break_on_hyphens=False)[:7])
    o.append(f'<text x="{M}" y="{H-26}" font-family="{SERIF}" font-style="italic" font-size="15" fill="{t["soft"]}">'
             f'The buyer has to say it. Absence is a result. {n_stage} stage skills, {n_init} initiatives, {n_intel} intelligence.</text>')
    o.append("</svg>")
    return "\n".join(o) + "\n"


def lum(hex_):
    r, g, b = (int(hex_[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def outputs():
    skills = load()
    return {f"skill-map-{skin}.svg": skill_map(skin, skills) for skin in TOKENS}


def main():
    files = outputs()
    if "--check" in sys.argv:
        bad = []
        for skin, tk in TOKENS.items():
            for fg, bg, need in PAIRS:
                r = ratio(tk[fg], tk[bg])
                if r < need:
                    bad.append(f"{skin}: {fg} on {bg} is {r:.2f}:1, needs {need}:1")
        for name, svg in files.items():
            p = os.path.join(OUT, name)
            if not os.path.exists(p) or open(p).read() != svg:
                bad.append(f"docs/img/{name} is out of date. Run: python3 scripts/build-diagrams.py")
        if bad:
            print("\n".join(bad))
            sys.exit(1)
        print(f"diagrams up to date ({len(files)} files), color contrast ok")
        return
    os.makedirs(OUT, exist_ok=True)
    for name, svg in files.items():
        open(os.path.join(OUT, name), "w").write(svg)
        print("wrote docs/img/" + name)


if __name__ == "__main__":
    main()
