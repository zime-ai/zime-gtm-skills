#!/bin/bash
# The one command: runs the skill eval framework via promptfoo.
# See evals/framework/README.md for the full picture.
#
# Usage:
#   evals/framework/eval.sh <skill> [--case <description>] [--judges N] [--baseline] [--learn]
#
#   <skill>    e.g. sales-to-cs-handover, poc-deck
#   --case     restrict to one case description (matches evals/cases/*.yaml)
#   --judges   judge samples per case, default 3 (env EVAL_JUDGES overrides default)
#   --baseline promote this run's results.json to evals/baseline-<skill>.json
#   --learn    run the LEARN stage (learn.sh) immediately after
set -euo pipefail

PROMPTFOO_VERSION="promptfoo@0.122.0"  # pinned -- an unpinned judge/toolchain drifts, see EVALS.md. Bump deliberately: `npm view promptfoo version`

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$REPO_ROOT"

SKILL="${1:?Usage: $0 <skill> [--case X] [--judges N] [--baseline] [--learn]}"
shift
CASE=""
JUDGES="${EVAL_JUDGES:-3}"
BASELINE=""
LEARN=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --case) CASE="$2"; shift 2 ;;
    --judges) JUDGES="$2"; shift 2 ;;
    --baseline) BASELINE=1; shift ;;
    --learn) LEARN=1; shift ;;
    *) echo "Unknown arg: $1" >&2; exit 1 ;;
  esac
done

[ -d "evals/cases" ] && [ -n "$(ls -A evals/cases/*.yaml 2>/dev/null)" ] || {
  echo "No evals/cases/*.yaml found (gitignored, private -- see evals/cases.example.yaml to add your own)." >&2
  exit 1
}

TS="$(date +%Y-%m-%dT%H-%M)"
RUN_DIR="$REPO_ROOT/evals/runs/$TS"
mkdir -p "$RUN_DIR/verdicts"
export EVAL_RUN_DIR="$RUN_DIR"
export EVAL_JUDGES="$JUDGES"

FILTERS=(--filter-metadata "skill=$SKILL")
[ -n "$CASE" ] && FILTERS+=(--filter-pattern "$CASE")

npx --yes "$PROMPTFOO_VERSION" eval \
  -c evals/promptfooconfig.yaml \
  "${FILTERS[@]}" \
  -o "$RUN_DIR/results.json" -o "$RUN_DIR/results.csv"

echo ""
python3 evals/framework/summarize.py "$RUN_DIR/results.json" "$REPO_ROOT/evals/baseline-$SKILL.json"
echo ""
echo "-> $RUN_DIR/{results.json,results.csv,gaps-$SKILL-*.md}"

if [ -n "$BASELINE" ]; then
  cp "$RUN_DIR/results.json" "$REPO_ROOT/evals/baseline-$SKILL.json"
  echo "Promoted to baseline: evals/baseline-$SKILL.json"
fi

if [ -n "$LEARN" ]; then
  evals/framework/learn.sh "$SKILL" "$RUN_DIR"
fi
