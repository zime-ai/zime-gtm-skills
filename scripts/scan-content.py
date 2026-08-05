#!/usr/bin/env python3
"""Content-level guard over every tracked file, four rules, one pass.

Where validate-skills.sh checks directories are gitignored, this checks the
*content* actually committed doesn't leak or carry an attack payload. Run:

    python3 scripts/scan-content.py           # all rules, current directory
    python3 scripts/scan-content.py --rule no-home-paths
    python3 scripts/scan-content.py /path/to/fixture   # scan a different root

Exit 0 if clean, 1 if any rule (other than the skipped no-client-names,
see below) found something.
"""

import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

# Extensions worth scanning as text. Binary assets (.pptx, .png, .svg, ...)
# are never text-scanned -- matches validate-skills.sh's own scope.
TEXT_EXTENSIONS = {
    ".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh", ".js", ".ts",
    ".csv", ".mjs", ".cjs",
}

# --- rule: no-home-paths ----------------------------------------------------
# ECC's validate-no-personal-paths.js rule, ported: flag a real absolute
# home directory path, allow the placeholder forms docs use.
HOME_PATH_RE = re.compile(
    r"(/Users/([A-Za-z0-9_.-]+)|C:\\Users\\([A-Za-z0-9_.-]+))", re.IGNORECASE
)
HOME_PATH_ALLOWLIST = {"you", "example", "yourname", "your-username", "user"}


def find_home_paths(path, text):
    findings = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for m in HOME_PATH_RE.finditer(line):
            user = (m.group(2) or m.group(3) or "").lower()
            if user in HOME_PATH_ALLOWLIST:
                continue
            findings.append((lineno, m.group(0)))
    return findings


# --- rule: no-client-names --------------------------------------------------
# The denylist is itself gitignored (real client/person names), so this rule
# can only run locally / pre-push -- it prints SKIP and passes on CI and on
# forks, where the denylist file doesn't exist. The mechanical CI-side
# backstop for the leak this rule targets is validate-skills.sh's
# git-check-ignore assertion over the private data directories.
def find_client_names(path, text, denylist):
    findings = []
    lowered = text.lower()
    for name in denylist:
        needle = name.lower()
        if needle in lowered:
            for lineno, line in enumerate(text.splitlines(), start=1):
                if needle in line.lower():
                    findings.append((lineno, name))
    return findings


# --- rule: no-injection -----------------------------------------------------
# A SKILL.md is executable instruction text installed into other people's
# agents, not inert docs -- scope this rule to skill bodies only.
INJECTION_PATTERNS = [
    re.compile(r"ignore (all |any )?(previous|prior|above) instructions", re.IGNORECASE),
    re.compile(r"disregard (all |any )?(previous|prior|above)", re.IGNORECASE),
    re.compile(r"\b(curl|wget)\b[^\n|]*\|\s*(bash|sh|zsh)\b"),
    re.compile(r"\bcat\s+~?/?\.(ssh|aws|env)\b"),
    re.compile(r"\bcat\s+.*\.env\b"),
    re.compile(r"/etc/(passwd|shadow)\b"),
]


def find_injection(path, text):
    findings = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for pat in INJECTION_PATTERNS:
            if pat.search(line):
                findings.append((lineno, pat.pattern))
    return findings


# --- rule: no-hidden-unicode ------------------------------------------------
ZERO_WIDTH = {"\u200b", "\u200c", "\u200d", "\ufeff"}
BIDI_OVERRIDE = {chr(c) for c in range(0x202A, 0x202F)} | {
    chr(c) for c in range(0x2066, 0x206A)
}


def find_hidden_unicode(path, text):
    findings = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for ch in line:
            if ch in ZERO_WIDTH:
                findings.append((lineno, f"zero-width char U+{ord(ch):04X}"))
            elif ch in BIDI_OVERRIDE:
                findings.append((lineno, f"bidi override U+{ord(ch):04X}"))
            elif unicodedata.name(ch, "").startswith(("CYRILLIC", "GREEK")):
                # Only flag a lookalike mixed into otherwise-ASCII text --
                # a vertical-context reference legitimately discussing
                # Cyrillic script wouldn't be all-ASCII around it.
                if any(c.isascii() and c.isalpha() for c in line):
                    findings.append((lineno, f"non-Latin lookalike char {ch!r}"))
    return findings


def tracked_files(repo_root):
    out = subprocess.run(
        ["git", "ls-files"], cwd=repo_root, capture_output=True, text=True, check=True
    )
    return [repo_root / p for p in out.stdout.splitlines() if p]


def load_denylist(repo_root):
    denylist_path = repo_root / ".private" / "client-denylist.txt"
    if not denylist_path.exists():
        return None
    return [
        line.strip()
        for line in denylist_path.read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root", nargs="?", default=".",
        help="Repo root to scan (default: current directory). "
             "Lets tests/run-checks-tests.sh point this at a scratch fixture.",
    )
    parser.add_argument(
        "--rule",
        choices=["no-home-paths", "no-client-names", "no-injection", "no-hidden-unicode"],
        help="Run only this rule (default: all).",
    )
    args = parser.parse_args()
    repo_root = Path(args.root).resolve()
    rules = [args.rule] if args.rule else [
        "no-home-paths", "no-client-names", "no-injection", "no-hidden-unicode",
    ]

    denylist = load_denylist(repo_root)
    if "no-client-names" in rules and denylist is None:
        print("[no-client-names] SKIP: .private/client-denylist.txt not present "
              "(expected -- it's gitignored; add it locally to run this rule)")

    issues = 0
    for path in tracked_files(repo_root):
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        rel = path.relative_to(repo_root)

        if "no-home-paths" in rules:
            for lineno, match in find_home_paths(path, text):
                print(f"[no-home-paths] {rel}:{lineno}: {match}")
                issues += 1

        if "no-client-names" in rules and denylist is not None:
            for lineno, name in find_client_names(path, text, denylist):
                print(f"[no-client-names] {rel}:{lineno}: contains denylisted name '{name}'")
                issues += 1

        if "no-injection" in rules and "skills/" in str(rel).replace("\\", "/"):
            for lineno, pattern in find_injection(path, text):
                print(f"[no-injection] {rel}:{lineno}: matches injection pattern /{pattern}/")
                issues += 1

        if "no-hidden-unicode" in rules:
            for lineno, detail in find_hidden_unicode(path, text):
                print(f"[no-hidden-unicode] {rel}:{lineno}: {detail}")
                issues += 1

    print()
    if issues:
        print(f"{issues} issue(s) found")
        sys.exit(1)
    print("Clean")


if __name__ == "__main__":
    main()
