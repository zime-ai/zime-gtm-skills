#!/usr/bin/env python3
"""
Post-PR check: scans the diff a PR actually introduced (base...head) for
the operator's own git identity (name/email) or a real home-directory
path. Run right after a PR opens, not before -- a PR is already public
once `gh pr create` returns, so this surfaces a leak immediately rather
than pretending a pre-push gate could still stop it.

Deliberately diff-scoped, not tree-scoped: scan-content.py's
no-home-paths rule already guards the whole tracked tree pre-push (see
AGENTS.md's rule registry); this adds the one thing no pattern-based rule
watches for -- the operator's own name/email showing up in prose, in the
lines a PR actually added.

Usage: python3 scripts/check-pr-diff-identity.py <base-ref> <head-ref> [root-dir]
root-dir defaults to the current directory; tests/run-checks-tests.sh
passes a scratch fixture there.
Exit 0 if clean, 1 if something was found.
"""
import os
import re
import subprocess
import sys

# Same regex/allowlist as scan-content.py's no-home-paths rule, duplicated
# rather than imported -- that script's filename isn't a valid module name
# and this stays a zero-dependency, standalone script like its siblings.
HOME_PATH_RE = re.compile(
    r"(/Users/([A-Za-z0-9_.-]+)|C:\\Users\\([A-Za-z0-9_.-]+))", re.IGNORECASE
)
HOME_PATH_ALLOWLIST = {"you", "example", "yourname", "your-username", "user"}


def git_config(key):
    try:
        return subprocess.run(
            ["git", "config", key], capture_output=True, text=True, check=True
        ).stdout.strip()
    except subprocess.CalledProcessError:
        return ""


def diff_added_lines(base, head):
    """Yield (file, added_line_text) for every added line in base...head."""
    out = subprocess.run(
        ["git", "diff", f"{base}...{head}", "--"],
        capture_output=True, text=True, check=True,
    ).stdout
    current_file = None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[len("+++ b/"):]
        elif line.startswith("+++ /dev/null"):
            current_file = None
        elif line.startswith("+") and not line.startswith("+++"):
            yield current_file or "?", line[1:]


def main():
    if len(sys.argv) not in (3, 4):
        print("Usage: check-pr-diff-identity.py <base-ref> <head-ref> [root-dir]", file=sys.stderr)
        sys.exit(2)
    base, head = sys.argv[1], sys.argv[2]
    if len(sys.argv) == 4:
        os.chdir(sys.argv[3])

    name = git_config("user.name")
    email = git_config("user.email")

    issues = 0
    for file, text in diff_added_lines(base, head):
        low = text.lower()
        if name and name.lower() in low:
            print(f"[operator-name] {file}: {text.strip()}")
            issues += 1
        if email and email.lower() in low:
            print(f"[operator-email] {file}: {text.strip()}")
            issues += 1
        for m in HOME_PATH_RE.finditer(text):
            user = (m.group(2) or m.group(3) or "").lower()
            if user in HOME_PATH_ALLOWLIST:
                continue
            print(f"[home-path] {file}: {text.strip()}")
            issues += 1

    print()
    if issues:
        print(f"{issues} issue(s) found in the PR diff -- review immediately, it's already public.")
        sys.exit(1)
    print("Clean: no operator identity or home path found in the PR diff.")


if __name__ == "__main__":
    main()
