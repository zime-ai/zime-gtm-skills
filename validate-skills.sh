#!/bin/bash
# Zero-dependency local check for skills/*/SKILL.md frontmatter and layout.
# CI additionally runs the upstream skills-ref validator — this is the fast
# pre-PR check a contributor can run with nothing installed.
#
# Usage: ./validate-skills.sh [root-dir]   (default: current directory)
# The optional root-dir lets tests/run-checks-tests.sh point this at a
# scratch fixture instead of the real repo.

ROOT="${1:-.}"
cd "$ROOT" || { echo "No such directory: $ROOT" >&2; exit 1; }

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

SKILLS_DIR="skills"
ISSUES=0
WARNINGS=0
PASSED=0

echo "Checking private eval data stays gitignored"
echo "================================================================"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    PRIVATE_DIRS=(evals/transcripts evals/gt evals/cases evals/labels)
    for d in "${PRIVATE_DIRS[@]}"; do
        if git check-ignore -q "$d" 2>/dev/null; then
            echo -e "${GREEN}PASS${NC} $d is gitignored"
        else
            echo -e "${RED}FAIL${NC} $d is NOT gitignored — real client data could leak to the public repo. Fix .gitignore."
            ((ISSUES++))
        fi
    done
else
    echo "Not a git repository, skipping (this check needs git check-ignore)"
fi
echo ""

echo "Validating skills against the Agent Skills frontmatter contract"
echo "================================================================"
echo ""

for skill_dir in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill_dir")
    skill_file="${skill_dir}SKILL.md"
    errors=()
    warnings=()

    if [[ ! -f "$skill_file" ]]; then
        echo -e "${RED}FAIL${NC} $skill_name — missing SKILL.md"
        ((ISSUES++))
        continue
    fi

    frontmatter=$(awk '/^---$/{count++; next} count==1' "$skill_file")

    if [[ -z "$frontmatter" ]]; then
        echo -e "${RED}FAIL${NC} $skill_name — missing YAML frontmatter (---)"
        ((ISSUES++))
        continue
    fi

    name_in_file=$(echo "$frontmatter" | grep "^name:" | sed -E 's/^name:[[:space:]]*//' | tr -d ' ')
    if [[ -z "$name_in_file" ]]; then
        errors+=("missing 'name' field")
    elif [[ "$name_in_file" != "$skill_name" ]]; then
        errors+=("name mismatch: directory='$skill_name' frontmatter='$name_in_file'")
    elif ! [[ "$name_in_file" =~ ^[a-z0-9]([a-z0-9-]{0,62}[a-z0-9])?$ ]]; then
        errors+=("invalid name format: '$name_in_file'")
    fi

    description=$(echo "$frontmatter" | grep "^description:" | head -1 | sed -E 's/^description:[[:space:]]*//')
    desc_len=${#description}
    if [[ -z "$description" ]]; then
        errors+=("missing 'description' field")
    elif [[ $desc_len -lt 1 || $desc_len -gt 1024 ]]; then
        errors+=("description length invalid: $desc_len chars (must be 1-1024)")
    fi

    line_count=$(wc -l < "$skill_file" | tr -d ' ')
    if [[ $line_count -gt 500 ]]; then
        errors+=("SKILL.md is $line_count lines (must be under 500)")
    fi

    dimension=$(echo "$frontmatter" | grep "zime:dimension:" | head -1 | sed 's/.*zime:dimension: *//' | tr -d ' ')
    if [[ -z "$dimension" ]]; then
        errors+=("missing 'zime:dimension' metadata field")
    elif [[ "$dimension" != "stage" && "$dimension" != "initiative" && "$dimension" != "vertical-context" ]]; then
        errors+=("invalid zime:dimension '$dimension' (must be stage, initiative, or vertical-context)")
    fi

    evals_file="${skill_dir}evals/evals.json"
    if [[ -f "$evals_file" ]]; then
        if ! python3 -m json.tool "$evals_file" >/dev/null 2>&1; then
            errors+=("evals/evals.json does not parse as valid JSON")
        elif grep -q '"assertions"' "$evals_file"; then
            errors+=("evals/evals.json uses 'assertions' — schema requires 'expectations'")
        fi
    fi

    for sub in "$skill_dir"*/; do
        [[ -d "$sub" ]] || continue
        sub_name=$(basename "$sub")
        case "$sub_name" in
            references|scripts|assets|evals) ;;
            *) warnings+=("unexpected subdirectory '$sub_name'") ;;
        esac
    done

    if [[ ${#errors[@]} -gt 0 ]]; then
        echo -e "${RED}FAIL${NC} $skill_name"
        for e in "${errors[@]}"; do echo "   $e"; done
        ((ISSUES++))
    elif [[ ${#warnings[@]} -gt 0 ]]; then
        echo -e "${YELLOW}WARN${NC} $skill_name"
        for w in "${warnings[@]}"; do echo "   $w"; done
        ((WARNINGS++))
        ((PASSED++))
    else
        echo -e "${GREEN}PASS${NC} $skill_name"
        ((PASSED++))
    fi
done

echo ""
echo "================================================================"
echo "$PASSED passed, $WARNINGS with warnings, $ISSUES failed"

if [[ $ISSUES -gt 0 ]]; then
    exit 1
fi
