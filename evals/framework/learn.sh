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

# Ledger of already-decided amendments for this skill (applied or rejected,
# latest row per id wins) -- so LEARN doesn't re-propose what's already been
# ruled on. Absence is fine: nothing decided yet for this skill.
LEDGER="$REPO_ROOT/evals/amendments.jsonl"
DECIDED_FILE="$SCRATCH/decided-amendments.md"
python3 -c "
import json, sys
ledger, skill = sys.argv[1], sys.argv[2]
rows = []
try:
    with open(ledger) as f:
        rows = [json.loads(l) for l in f if l.strip()]
except FileNotFoundError:
    pass
latest = {}
for r in rows:
    latest.setdefault(r['id'], {}).update(r)
decided = [r for r in latest.values() if r.get('skill') == skill and r.get('status') != 'pending']
if not decided:
    print('None yet.')
else:
    for r in decided:
        print(f\"- {r['id']} ({r['status']}): {r.get('proposal', '')} -- {r.get('note', '')}\")
" "$LEDGER" "$SKILL" > "$DECIDED_FILE"

( cd "$SCRATCH" && claude -p \
  "Read every ./gaps-$SKILL-*.md file and ./feedback.md, and the skill definition at .claude/skills/$SKILL/SKILL.md plus its references/. Also read ./decided-amendments.md: proposals already applied or rejected for this skill -- do not re-propose any of them. Write ./learnings.md: a ranked list of concrete NEW fixes to the skill's SKILL.md or references, each citing the specific gaps file line or feedback.md bullet driving it. Do not edit any files -- only write learnings.md." \
  --dangerously-skip-permissions )

cp "$SCRATCH/learnings.md" "$RUN_DIR/learnings.md"
echo "-> $RUN_DIR/learnings.md"

# Seed the ledger with pending rows for whatever learnings.md just proposed,
# one line = one proposal, so amend.sh has ids to decide on. Simple line-based
# split -- good enough for a ranked markdown list, not a parser.
RECORDED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python3 -c "
import json, re, sys
learnings_path, ledger, skill, run_dir, recorded_at = sys.argv[1:6]
text = open(learnings_path).read()
# One proposal per ranked item. The isolated session renders 'a ranked list'
# as either a plain numbered list ('1. ...') or numbered headers
# ('## 1. ...') with prose/sub-bullets underneath -- seen both in practice.
# Only match a line starting with 'N.', not a bare '-' bullet: a '-' inside
# an item's body (a sub-point, not a new ranked item) would otherwise get
# split out as its own spurious proposal.
items = [re.sub(r'^#+\s*', '', l).strip() for l in text.splitlines()
         if re.match(r'^#*\s*\d+\.\s+\S', l)]
if not items:
    sys.exit(0)
existing_ids = set()
try:
    with open(ledger) as f:
        existing_ids = {json.loads(l)['id'] for l in f if l.strip()}
except FileNotFoundError:
    pass
n = 0
while f'A-{n:03d}' in existing_ids:
    n += 1
with open(ledger, 'a') as f:
    for item in items:
        while f'A-{n:03d}' in existing_ids:
            n += 1
        row = {
            'id': f'A-{n:03d}', 'skill': skill, 'source_run': run_dir,
            'proposal': item, 'status': 'pending', 'note': None,
            'recorded_at': recorded_at,
        }
        f.write(json.dumps(row) + '\n')
        existing_ids.add(row['id'])
        n += 1
print(f'-> {len(items)} pending amendment(s) added to {ledger}')
" "$SCRATCH/learnings.md" "$LEDGER" "$SKILL" "$(basename "$RUN_DIR")" "$RECORDED_AT"
