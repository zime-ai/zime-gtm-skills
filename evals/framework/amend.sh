#!/bin/bash
# Record a decision on a proposed rubric fix in evals/amendments.jsonl
# (append-only, gitignored -- latest row per id wins, no rewrite path).
# learn.sh reads this ledger so it stops re-proposing decided amendments.
#
# Usage: evals/framework/amend.sh <id> applied|rejected "<note>"
set -euo pipefail

ID="${1:?Usage: $0 <id> applied|rejected \"<note>\"}"
STATUS="${2:?Usage: $0 <id> applied|rejected \"<note>\"}"
NOTE="${3:-}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
LEDGER="$REPO_ROOT/evals/amendments.jsonl"

case "$STATUS" in
  applied|rejected) ;;
  *) echo "status must be 'applied' or 'rejected', got: $STATUS" >&2; exit 1 ;;
esac

[ -f "$LEDGER" ] || { echo "No $LEDGER yet -- nothing to amend." >&2; exit 1; }

if ! grep -q "\"id\": *\"$ID\"" "$LEDGER"; then
  echo "No amendment with id '$ID' found in $LEDGER" >&2
  exit 1
fi

RECORDED_AT="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python3 -c "
import json, sys
print(json.dumps({
    'id': sys.argv[1], 'status': sys.argv[2], 'note': sys.argv[3],
    'recorded_at': sys.argv[4],
}))
" "$ID" "$STATUS" "$NOTE" "$RECORDED_AT" >> "$LEDGER"

echo "Recorded: $ID -> $STATUS"
