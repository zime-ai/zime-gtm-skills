#!/bin/bash
# promptfoo `exec:` provider — stage 1 (RUN) of the eval framework.
# Isolated: builds a scratch dir containing ONLY the skill under test + its
# transcript (no ground truth, no other skills, no repo CLAUDE.md), invokes
# it via the literal slash command (works whether or not the skill allows
# model auto-invocation), and prints its text output to stdout as the
# promptfoo `output` value.
#
# Contract (promptfoo custom script provider): argv = prompt, options-json,
# context-json. We ignore the rendered prompt text — the skill+transcript to
# run comes from context.vars, set per test case in evals/cases/*.yaml.
set -euo pipefail

CONTEXT="$3"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

SKILL=$(echo "$CONTEXT" | jq -r '.vars.skill')
TRANSCRIPT=$(echo "$CONTEXT" | jq -r '.vars.transcript')
CASE=$(echo "$CONTEXT" | jq -r '.test.description // "case"')

SKILL_DIR="$REPO_ROOT/skills/$SKILL"
TRANSCRIPT_FILE="$REPO_ROOT/evals/transcripts/$TRANSCRIPT.txt"
[ -d "$SKILL_DIR" ] || { echo "No such skill: skills/$SKILL" >&2; exit 1; }
[ -f "$TRANSCRIPT_FILE" ] || { echo "No such transcript: evals/transcripts/$TRANSCRIPT.txt" >&2; exit 1; }

RUN_DIR="${EVAL_RUN_DIR:-$REPO_ROOT/evals/runs/adhoc}"
OUT_DIR="$RUN_DIR/output/$SKILL/$CASE"
mkdir -p "$OUT_DIR" "$RUN_DIR"

SCRATCH="/tmp/skill-eval-$SKILL-$CASE-run"
rm -rf "$SCRATCH"
mkdir -p "$SCRATCH/.claude/skills"
cp -r "$SKILL_DIR" "$SCRATCH/.claude/skills/"
cp "$TRANSCRIPT_FILE" "$SCRATCH/transcript.txt"

( cd "$SCRATCH" && claude -p "/$SKILL ./transcript.txt" --dangerously-skip-permissions ) \
  > "$RUN_DIR/log-$SKILL-$CASE-run.log" 2>&1 || true

find "$SCRATCH" -maxdepth 1 -type f ! -name transcript.txt -exec cp {} "$OUT_DIR/" \;

# Judge (judge.py) reads $EVAL_RUN_DIR/output/$SKILL/$CASE/ directly for
# binary artifacts (.docx/.pptx); stdout here only needs the text content
# promptfoo's assertion pipeline passes along as `output`.
shopt -s nullglob
TEXT_FILES=("$OUT_DIR"/*.md "$OUT_DIR"/*.txt "$OUT_DIR"/*.json)
if [ "${#TEXT_FILES[@]}" -eq 0 ]; then
  echo "(no text output produced -- see $OUT_DIR)"
else
  cat "${TEXT_FILES[@]}"
fi
