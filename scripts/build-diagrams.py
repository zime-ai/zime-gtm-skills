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


def frame(skin, W, H, label):
    t = TOKENS[skin]
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(label)}">',
            f'<title>{esc(label)}</title>',
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="{t["paper"]}" stroke="{t["rule"]}"/>']


def txt(x, y, s, family, size, fill, anchor="start", extra=""):
    a = "" if anchor == "start" else f' text-anchor="{anchor}"'
    return f'<text x="{x}" y="{y}"{a} font-family="{family}" font-size="{size}" fill="{fill}" {extra}>{esc(s)}</text>'


def hero(skin, skills):
    t = TOKENS[skin]
    total = len(skills)
    n_stage = sum(1 for d in skills.values() if d["dimension"] == "stage")
    n_init = sum(1 for d in skills.values() if d["dimension"] == "initiative")
    n_intel = sum(1 for d in skills.values() if d["dimension"] == "intelligence")
    W, H, M = 1200, 340, 48
    o = frame(skin, W, H, f"zime-gtm-skills: {total} Agent Skills that audit sales calls and CRM exports")
    o.append(txt(M, 66, "AGENT SKILLS FOR REVOPS AND SALES OPS", MONO, 12, t["soft"], extra='letter-spacing="2.4"'))
    o.append(txt(M, 134, "Audit sales calls and CRM exports.", SERIF, 50, t["ink"]))
    o.append(txt(M, 190, "Credit only what the buyer said.", SERIF, 50, t["muted"], extra='font-style="italic"'))
    o.append(txt(M, 232, "One file in, one evidence-cited audit out. Runs locally, no credentials, no telemetry.", SANS, 17, t["muted"]))
    o.append(f'<rect x="{M}" y="262" width="560" height="50" rx="10" fill="{t["paper2"]}" stroke="{t["rule"]}"/>')
    o.append(txt(M + 20, 293, "$", MONO, 16, t["accent"], extra='font-weight="700"'))
    o.append(txt(M + 42, 293, "/plugin marketplace add zime-ai/zime-gtm-skills", MONO, 16, t["ink"]))
    o.append(txt(W - M, 186, str(total), SERIF, 124, t["accent"], "end"))
    o.append(txt(W - M, 240, "OPEN AGENT SKILLS", MONO, 13, t["soft"], "end", 'letter-spacing="2"'))
    o.append(txt(W - M, 288, f"{n_stage} stage  |  {n_init} initiative  |  {n_intel} intelligence", MONO, 13, t["muted"], "end"))
    o.append("</svg>")
    return "\n".join(o) + "\n"


def how_it_works(skin, skills):
    t = TOKENS[skin]
    W, H, M = 1200, 430, 48
    o = frame(skin, W, H, "How a skill works: a file goes in, the rubric applies three evidence rules, an audit with a quote for every finding comes out")
    o.append(txt(M, 56, "HOW A SKILL WORKS", MONO, 12, t["soft"], extra='letter-spacing="2.4"'))
    o.append(txt(M, 100, "One file in. One evidence-cited audit out.", SERIF, 34, t["ink"]))
    gap = 70
    bw = (W - 2 * M - 2 * gap) // 3
    by, bh = 140, 220
    boxes = [
        ("INPUT", ["Call transcript", ".txt  .vtt  .json  .md", "", "CRM export", ".csv", "", "Live CRM, read-only", "through crm-export"], False),
        ("RUBRIC", ["1  The buyer must say it", "", "2  Absence is a result", "", "3  Say what does not count", "", "Each skill adds its own", "dimensions on top"], True),
        ("OUTPUT", ["Covered, Partial or Missed", "", "A quote or a cell", "for every finding", "", "One closing line,", "no recap"], False),
    ]
    for i, (name, lines, focal) in enumerate(boxes):
        x = M + i * (bw + gap)
        stroke = t["accent"] if focal else t["rule"]
        sw = 2 if focal else 1
        o.append(f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="{t["paper2"]}" stroke="{stroke}" stroke-width="{sw}"/>')
        o.append(txt(x + 24, by + 38, name, MONO, 12, t["accent"] if focal else t["ink"], extra='font-weight="600" letter-spacing="1.6"'))
        for j, ln in enumerate(lines):
            strong = ln[:1].isdigit() or ln in ("Call transcript", "CRM export", "Live CRM, read-only", "Covered, Partial or Missed", "A quote or a cell")
            o.append(txt(x + 24, by + 72 + j * 18, ln, SANS if strong else MONO, 14 if strong else 13,
                         t["ink"] if strong else t["muted"], extra='font-weight="600"' if strong else ""))
        if i < 2:
            ax = x + bw + 12
            o.append(f'<line x1="{ax}" y1="{by+bh//2}" x2="{ax+gap-30}" y2="{by+bh//2}" stroke="{t["accent"]}" stroke-width="2"/>')
            o.append(f'<path d="M{ax+gap-38} {by+bh//2-6} L{ax+gap-28} {by+bh//2} L{ax+gap-38} {by+bh//2+6}" fill="none" stroke="{t["accent"]}" stroke-width="2"/>')
    o.append(txt(M, H - 34, "Nothing leaves your machine. No telemetry, no lead capture.", SERIF, 16, t["soft"], extra='font-style="italic"'))
    o.append("</svg>")
    return "\n".join(o) + "\n"


def output_card(skin, skills):
    """Two panels: the last lines of a call on the left, the audit of it on the right."""
    t = TOKENS[skin]
    W, H, M = 1200, 520, 48
    o = frame(skin, W, H, "Sample audit: the last lines of a call, and the next-step-commitment audit that scores it a weak commitment with a quote for each element")
    o.append(txt(M, 56, "SAMPLE OUTPUT", MONO, 12, t["soft"], extra='letter-spacing="2.4"'))
    o.append(txt(M, 100, "What an audit looks like", SERIF, 34, t["ink"]))
    py, ph = 128, 330
    lx, lw = M, 440
    rx, rw = 548, W - M - 548
    for x, w in ((lx, lw), (rx, rw)):
        o.append(f'<rect x="{x}" y="{py}" width="{w}" height="{ph}" rx="10" fill="{t["paper2"]}" stroke="{t["rule"]}"/>')
        o.append(f'<line x1="{x+24}" y1="{py+52}" x2="{x+w-24}" y2="{py+52}" stroke="{t["rule"]}"/>')
    # left: the call
    o.append(txt(lx + 24, py + 34, "THE CALL", MONO, 12, t["ink"], extra='font-weight="600" letter-spacing="1.6"'))
    o.append(txt(lx + lw - 24, py + 34, "last three lines", MONO, 12, t["soft"], "end"))
    lines = [
        ("1", "Alex, rep", ["\"Great. I'll get that put together", "and send it your way.\""]),
        ("3", "Nina, buyer", ["\"Perfect, sounds good. I'll take a", "look when it comes through.\""]),
        ("2", "Alex, rep", ["\"Awesome. I'll be in touch soon", "once it's ready.\""]),
    ]
    for k, (num, who, quote) in enumerate(lines):
        y = py + 88 + k * 86
        o.append(f'<circle cx="{lx+36}" cy="{y+14}" r="11" fill="none" stroke="{t["accent"]}" stroke-width="1.5"/>')
        o.append(txt(lx + 36, y + 18, num, MONO, 12, t["accent"], "middle", 'font-weight="700"'))
        o.append(txt(lx + 62, y + 4, who.upper(), MONO, 11, t["soft"], extra='letter-spacing="1.4"'))
        for q, ln in enumerate(quote):
            o.append(txt(lx + 62, y + 28 + q * 20, ln, SANS, 15, t["ink"]))
    # the arrow between the panels
    ay = py + ph // 2
    o.append(f'<line x1="{lx+lw+10}" y1="{ay}" x2="{rx-12}" y2="{ay}" stroke="{t["accent"]}" stroke-width="2"/>')
    o.append(f'<path d="M{rx-20} {ay-6} L{rx-10} {ay} L{rx-20} {ay+6}" fill="none" stroke="{t["accent"]}" stroke-width="2"/>')
    # right: the audit
    o.append(txt(rx + 24, py + 34, "THE AUDIT", MONO, 12, t["ink"], extra='font-weight="600" letter-spacing="1.6"'))
    o.append(txt(rx + rw - 24, py + 34, "next-step-commitment", MONO, 12, t["soft"], "end"))
    o.append(txt(rx + 24, py + 98, "VERDICT", MONO, 12, t["soft"], extra='letter-spacing="2"'))
    o.append(txt(rx + 112, py + 100, "Weak commitment", SERIF, 34, t["accent"]))
    rows = [
        ("1", True, "Specific action", "PRESENT", "A named deliverable, but only the rep owns it."),
        ("2", False, "Date or concrete trigger", "MISSING", "\"Soon\" is not a date, and nothing marks when it happens."),
        ("3", False, "Two-sided ownership", "MISSING", "\"I'll take a look\" is a hope. The buyer owns no step."),
    ]
    for k, (num, ok, name, status, note) in enumerate(rows):
        y = py + 150 + k * 62
        o.append(txt(rx + 24, y + 5, num, MONO, 12, t["soft"]))
        if ok:
            o.append(f'<circle cx="{rx+58}" cy="{y}" r="6" fill="{t["ink"]}" stroke="{t["ink"]}" stroke-width="2"/>')
        else:
            o.append(f'<circle cx="{rx+58}" cy="{y}" r="6" fill="none" stroke="{t["ink"]}" stroke-width="2"/>')
        o.append(txt(rx + 78, y + 5, name, SANS, 16, t["ink"], extra='font-weight="600"'))
        o.append(txt(rx + rw - 24, y + 5, status, MONO, 12, t["soft"], "end", 'letter-spacing="1.4"'))
        o.append(txt(rx + 78, y + 28, note, SANS, 14, t["muted"]))
    o.append(txt(M, H - 28, "Every status carries a quote. A rep claim the buyer never accepted does not count.", SERIF, 16, t["soft"], extra='font-style="italic"'))
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
    out = {}
    for skin in TOKENS:
        out[f"skill-map-{skin}.svg"] = skill_map(skin, skills)
        out[f"hero-{skin}.svg"] = hero(skin, skills)
        out[f"how-it-works-{skin}.svg"] = how_it_works(skin, skills)
        out[f"sample-output-{skin}.svg"] = output_card(skin, skills)
    return out


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
