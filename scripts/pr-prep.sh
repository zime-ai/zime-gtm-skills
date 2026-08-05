#!/usr/bin/env bash
# ponytail: prints commands, never runs them. Claude must never push or run
# gh (hard rule, see MAINTAINING.md) -- this script is the enforcement
# mechanism, not just advice. Adapted from the workspace's zime-worktree
# skill's pr-prep.sh, scoped down to this repo's single-repo / single-target
# layout (no per-repo BASE table, no dev-mage overlay backstop) and with
# ./validate-skills.sh added as a real gate before the PR is prepped.
set -euo pipefail

usage() {
  echo "Usage: $0 <worktree-path> <pr-title>"
  echo "  worktree-path   path to the feature worktree (has its own git HEAD)"
  echo "  pr-title        PR title, e.g. \"Add sql-to-qualify skill\""
  exit 1
}

[ $# -ge 2 ] || usage
WT="$1"; TITLE="$2"
BASE="main"

[ -d "$WT/.git" ] || [ -f "$WT/.git" ] || { echo "Not a worktree: $WT"; exit 1; }
cd "$WT"

BRANCH="$(git rev-parse --abbrev-ref HEAD)"

echo "Branch: $BRANCH"
echo "Base: $BASE"
echo

# Hard rule 1: no Claude co-author trailer on HEAD.
if git log -1 --format='%B' | grep -qi 'Co-Authored-By:.*Claude'; then
  echo "BLOCKED: HEAD commit carries a 'Co-Authored-By: Claude' trailer."
  echo "This must never ship. Fix with:"
  echo "  git commit --amend  # edit the message, drop the trailer line"
  exit 1
fi
echo "OK: no Claude co-author trailer on HEAD."

# Hard rule 1b: commit author should be the user's real identity, not Claude.
AUTHOR="$(git log -1 --format='%an <%ae>')"
echo "Commit author: $AUTHOR"
if echo "$AUTHOR" | grep -qi 'claude'; then
  echo "BLOCKED: commit author looks like Claude, not the user. Fix with:"
  echo "  git commit --amend --reset-author --no-edit"
  exit 1
fi

# Gate: structural validation must pass before a PR gets prepped.
echo
echo "Running ./validate-skills.sh..."
if ! ./validate-skills.sh; then
  echo
  echo "BLOCKED: ./validate-skills.sh failed. Fix the reported skill(s) first."
  exit 1
fi

echo
echo "Diff vs base (origin/$BASE):"
git diff "origin/$BASE" --stat 2>/dev/null || echo "  (couldn't diff against origin/$BASE -- check manually)"

REPO_ROOT="$(dirname "$(git rev-parse --path-format=absolute --git-common-dir)")"
PR_BODY_FILE="$REPO_ROOT/.tmp/pr-description-${BRANCH//\//-}.txt"

if [ ! -f "$PR_BODY_FILE" ]; then
  mkdir -p "$(dirname "$PR_BODY_FILE")"
  cat > "$PR_BODY_FILE" <<'EOF'
## Summary

<!-- one-liner: the change in plain, simple terms -->

<!-- then 1-3 bullets: what changed and why -->

## Checklist

- [ ] `name` in SKILL.md frontmatter matches the directory exactly
- [ ] `description` states both what and when
- [ ] SKILL.md under 500 lines
- [ ] ./validate-skills.sh passes
- [ ] No internal Zime checklist question text introduced (see MAINTAINING.md)
- [ ] Disclosed if AI-assisted (see CONTRIBUTING.md)
EOF
  echo
  echo "Wrote a PR body template to: $PR_BODY_FILE (fill in before using it)"
else
  echo
  echo "PR body file already exists, left untouched: $PR_BODY_FILE"
fi

PUSH_SCRIPT="$REPO_ROOT/.tmp/push-pr-${BRANCH//\//-}.sh"
cat > "$PUSH_SCRIPT" <<EOF
#!/usr/bin/env bash
set -euo pipefail
cd "$WT"
git push -u origin $BRANCH
gh pr create --base $BASE --title "$TITLE" --body-file "$PR_BODY_FILE"
EOF
chmod +x "$PUSH_SCRIPT"

echo
echo "================================================================"
echo "Claude never runs this. Run it yourself:"
echo "================================================================"
echo "$PUSH_SCRIPT"
