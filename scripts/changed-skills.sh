#!/usr/bin/env bash
# Lists the skill directories a change touched and tags each one, so a review
# (or CI) looks at the delta and not at every skill.
#   new      SKILL.md added
#   rubric   a dimension heading or a Covered/Partial/Missed/does-not-count
#            line changed in the skill's files
#   wording  anything else
# Usage: scripts/changed-skills.sh [base-ref]   (default: origin/dev)
# Output: one "<skill><TAB><tag>" line per changed skill. No model calls.
set -euo pipefail
BASE="${1:-origin/dev}"
cd "$(git rev-parse --show-toplevel)"
MB="$(git merge-base "$BASE" HEAD)"   # diff against the working tree too, so it works before a commit

git diff --name-status "$MB" -- skills/ | while read -r status path _; do
  case "$path" in skills/*/*) ;; *) continue ;; esac
  name="${path#skills/}"; name="${name%%/*}"
  if [ "$status" = A ] && [ "${path##*/}" = SKILL.md ]; then echo "$name new"; continue; fi
  if git diff -U0 "$MB" -- "$path" | grep -E '^[+-](## |.*(Covered|Partial|Missed|[Dd]oes not count))' >/dev/null; then
    echo "$name rubric"
  else
    echo "$name wording"
  fi
done | sort -u | awk -F' ' '
  { rank = ($2=="new")?3:($2=="rubric")?2:1
    if (rank > best[$1]) { best[$1]=rank; tag[$1]=$2 } }
  END { for (n in best) printf "%s\t%s\n", n, tag[n] }' | sort
