#!/usr/bin/env bash
# Static security scan (NVIDIA SkillSpector, no model calls) over skills.
#   scripts/skillspector-gate.sh all           every skill
#   scripts/skillspector-gate.sh <base-ref>    only skills changed since <base-ref>
# High or critical findings fail the run. Medium and low print as warnings.
# Reviewed false positives live in .skillspector-baseline.yaml, with a reason each.
# Needs the `skillspector` command on PATH (CI installs a pinned commit).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
MODE="${1:-all}"
SKILLS_DIR="${SKILLS_DIR:-skills}"   # override to test against a scratch directory
command -v skillspector >/dev/null || { echo "skillspector is not installed" >&2; exit 2; }

if [ "$MODE" = all ]; then names="$(ls "$SKILLS_DIR")"; else names="$(scripts/changed-skills.sh "$MODE" | cut -f1)"; fi
[ -n "$names" ] || { echo "no changed skills to scan"; exit 0; }

out="$(mktemp)"; fail=0
for n in $names; do
  [ -d "$SKILLS_DIR/$n" ] || continue   # skill was deleted
  skillspector scan "$SKILLS_DIR/$n" --no-llm --format json --baseline .skillspector-baseline.yaml --output "$out" >/dev/null 2>&1 || true
  verdict="$(python3 - "$out" <<'P'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception:
    print("ERROR no report"); sys.exit()
sev = d["risk_assessment"]["max_issue_severity"]
ids = ",".join(sorted({i["id"] for i in d["issues"]}))
if not d["execution_successful"]: print("ERROR scan did not finish")
elif sev in ("HIGH", "CRITICAL"): print(f"FAIL {sev} {ids}")
elif sev == "NONE": print("OK")
else: print(f"WARN {sev} {ids}")
P
)"
  echo "$n: $verdict"
  case "$verdict" in FAIL*|ERROR*) fail=1 ;; esac
done
rm -f "$out"
exit "$fail"
