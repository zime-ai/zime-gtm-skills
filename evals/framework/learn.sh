#!/bin/bash
# LEARN stage: isolated session over gaps-<skill>-*.md + your feedback.md +
# the skill's own SKILL.md/references only -- no transcript, no generated
# output. Writes ranked, gap-cited fixes to learnings.md. Never edits the
# skill -- you apply what's useful by hand.
#
# Usage: evals/framework/learn.sh <skill> <run-dir>
set -euo pipefail

SKILL="${1:?Usage: $0 <skill> <run-dir>}"
RUN_DIR="${2:?Usage: $0 <skill> <run-dir>}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

FEEDBACK="$RUN_DIR/feedback.md"
if [ ! -f "$FEEDBACK" ]; then
  cat > "$FEEDBACK" <<'EOF'
<!-- Your notes. Empty sections are ignored by the LEARN stage -- not treated as approval. -->

## What the output got wrong

## What it invented (not in the transcript, not in ground truth)

## What a human would have written instead

## What the rubric (SKILL.md) should have said
EOF
  echo "Seeded $FEEDBACK -- edit it, then re-run this command to fold your notes in."
fi

shopt -s nullglob
GAPS_FILES=("$RUN_DIR"/gaps-"$SKILL"-*.md)
if [ "${#GAPS_FILES[@]}" -eq 0 ]; then
  echo "No gaps-$SKILL-*.md in $RUN_DIR -- run eval.sh $SKILL first." >&2
  exit 1
fi

SCRATCH="/tmp/skill-eval-$SKILL-learn"
rm -rf "$SCRATCH"
mkdir -p "$SCRATCH/.claude/skills"
cp -r "$REPO_ROOT/skills/$SKILL" "$SCRATCH/.claude/skills/"
cp "${GAPS_FILES[@]}" "$SCRATCH/"
cp "$FEEDBACK" "$SCRATCH/feedback.md"

( cd "$SCRATCH" && claude -p \
  "Read every ./gaps-$SKILL-*.md file and ./feedback.md, and the skill definition at .claude/skills/$SKILL/SKILL.md plus its references/. Write ./learnings.md: a ranked list of concrete fixes to the skill's SKILL.md or references, each citing the specific gaps file line or feedback.md bullet driving it. Do not edit any files -- only write learnings.md." \
  --dangerously-skip-permissions )

cp "$SCRATCH/learnings.md" "$RUN_DIR/learnings.md"
echo "-> $RUN_DIR/learnings.md"
