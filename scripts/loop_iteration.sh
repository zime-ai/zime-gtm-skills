#!/usr/bin/env bash
# One iteration of the improvement loop. Run by launchd weekly, or by hand.
# The agent only edits skill files. This script runs the referee, does all git work, and logs.
set -uo pipefail
CFG="$HOME/.config/gtm-loop"
REPO="$CFG/repo"   # the loop works in its own clone, never in a working copy a person is editing
STATE="$REPO/evals/loop/state"
mkdir -p "$CFG"
if [ ! -d "$REPO/.git" ]; then
  GH_TOKEN="$(cat "$CFG/gh.token" 2>/dev/null || cat "$HOME/.config/gh-gtm/token")" \
    gh repo clone zime-ai/zime-gtm-skills "$REPO" >/dev/null 2>&1 || { echo "clone failed"; exit 1; }
fi
mkdir -p "$STATE"
log() { printf '%s\t%s\n' "$(date +%Y-%m-%dT%H:%M)" "$*" >> "$STATE/results.tsv"; }
escalate() {
  printf '%s %s\n' "$(date +%Y-%m-%dT%H:%M)" "$*" >> "$STATE/escalations.md"
  osascript -e "display notification \"$*\" with title \"GTM skills loop needs you\"" 2>/dev/null || true
  log "ESCALATE	$*"; exit 1
}
[ -e "$CFG/STOP" ] && { echo "kill switch set"; exit 0; }
mkdir "$CFG/lock" 2>/dev/null || { echo "another iteration is running"; exit 0; }
trap 'rmdir "$CFG/lock"' EXIT

cd "$REPO" || exit 1
export GH_TOKEN="$(cat "$CFG/gh.token" 2>/dev/null || cat "$HOME/.config/gh-gtm/token")"
git fetch -q origin || escalate "git fetch failed"
git checkout -q -B loop/work origin/dev || escalate "cannot reset to origin/dev"
[ -s evals/loop/baseline.json ] || escalate "no baseline: run scripts/referee.py deep-discovery --baseline"
SKILL=deep-discovery   # one target for now. The referee only knows skills that have a planted bank.

PROMPT="$(cat evals/loop/PROGRAM.md)

Target skill: $SKILL
Baseline scores: $(cat evals/loop/baseline.json)
Dev-bank cells the current skill gets wrong (case, dimension): $(python3 -c "import json;print(json.load(open('evals/loop/baseline.json'))['$SKILL'].get('A_failed','unknown'))")
Edit only skills/$SKILL/. Write your hypothesis to evals/loop/state/hypothesis.txt, then stop."
rm -f "$STATE/hypothesis.txt"
perl -e 'alarm shift; exec @ARGV' 1500 claude -p "$PROMPT" --model claude-sonnet-5-5 \
  --setting-sources project --permission-mode acceptEdits \
  --allowedTools Read Edit Write Glob Grep --disallowedTools Bash WebFetch WebSearch \
  > "$STATE/author.log" 2>&1 || escalate "author step failed or timed out, see state/author.log"
HYP="$(tr '\n' ' ' < "$STATE/hypothesis.txt" 2>/dev/null)"
[ -n "$HYP" ] || { git checkout -q -- skills/; log "SKIP	no hypothesis written"; exit 0; }
git diff --quiet -- "skills/$SKILL" && { log "SKIP	no change made: $HYP"; exit 0; }

VERDICT="$(python3 scripts/referee.py "$SKILL" 2>&1 | tee "$STATE/referee.log" | tail -1)"
NOW="$(python3 -c "import json;d=json.load(open('evals/loop/state/last_run.json'));print(d['B']['exact'],d['A']['exact'],d['skill_lines'])" 2>/dev/null)"
case "$VERDICT" in
  ACCEPT*)
    BR="loop/$SKILL-$(date +%Y%m%d-%H%M)"
    python3 - "$SKILL" <<'PY'
import json, sys
s = sys.argv[1]
b = json.load(open("evals/loop/baseline.json")); l = json.load(open("evals/loop/state/last_run.json"))
b[s] = {k: l[k] for k in ("A", "B", "skill_lines", "A_failed")}
json.dump(b, open("evals/loop/baseline.json", "w"), indent=1)
PY
    git checkout -q -b "$BR" && git add -u skills evals/loop/baseline.json && \
    git commit -q -m "feat($SKILL): $HYP" -m "Referee ACCEPT on held-out and dev banks. Scores: $NOW (held-out exact, dev exact, skill lines)." && \
    git push -q -u origin "$BR" && \
    PR="$(gh pr create --repo zime-ai/zime-gtm-skills --base dev --head "$BR" --title "feat($SKILL): $HYP" \
      --body "Automated improvement loop. The referee accepted this change on a held-out planted-fact bank and a dev bank. Hypothesis: $HYP" 2>&1 | tail -1)" && \
    gh pr merge "$PR" --repo zime-ai/zime-gtm-skills --auto --squash >/dev/null 2>&1
    log "ACCEPT	$NOW	$HYP	$PR" ;;
  REJECT*)
    git checkout -q -- skills/
    printf '%s\t%s\t%s\t%s\n' "$(date +%Y-%m-%d)" "$SKILL" "$HYP" "$VERDICT" >> "$STATE/rejects.tsv"
    log "REJECT	$NOW	$HYP	$VERDICT" ;;
  *)
    git checkout -q -- skills/
    escalate "referee said: $VERDICT" ;;
esac
