#!/bin/bash
# Zero-dependency check that README.md agrees with skills/*. Run from the
# repo root. Catches the failure mode where a skill lands (or is removed)
# and one of the README's several count/table surfaces isn't updated —
# see MAINTAINING.md's "Landing a skill on main".
#
# Deliberately does not generate the README table: the "Audits" column is
# hand-written prose, not derivable from frontmatter. This only reports
# drift.
#
# Usage: ./scripts/check-docs-sync.sh [root-dir]   (default: current directory)
# The optional root-dir lets tests/run-checks-tests.sh point this at a
# scratch fixture instead of the real repo.

ROOT="${1:-.}"
cd "$ROOT" || { echo "No such directory: $ROOT" >&2; exit 1; }

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

SKILLS_DIR="skills"
README="README.md"
ISSUES=0

echo "Checking README.md against skills/*"
echo "================================================================"
echo ""

actual_count=$(ls -d "$SKILLS_DIR"/*/ 2>/dev/null | wc -l | tr -d ' ')

# --- 1. Skill count agreement, all four README surfaces ------------------

check_count() {
    local label="$1" pattern="$2"
    local matches
    matches=$(grep -oE "$pattern" "$README")
    if [[ -z "$matches" ]]; then
        echo -e "${RED}FAIL${NC} count anchor not found: $label"
        echo "   pattern '$pattern' matched nothing — README wording changed;"
        echo "   update scripts/check-docs-sync.sh to match."
        ((ISSUES++))
        return
    fi
    while IFS= read -r m; do
        n=$(grep -oE '[0-9]+' <<< "$m" | head -1)
        if [[ "$n" != "$actual_count" ]]; then
            echo -e "${RED}FAIL${NC} $label says $n, but $actual_count skill dirs exist"
            ((ISSUES++))
        fi
    done <<< "$matches"
}

check_count "badge"                     'skills-[0-9]+-blue'
check_count "opening paragraph"         'here\. [0-9]+ \[Agent Skills\]'
check_count "How these fit together"    '[0-9]+ skills: [0-9]+ stage motions'
check_count "Available skills summary"  '<summary>[0-9]+ skills across'

# --- 2/3. SKILLS:START..END table vs. actual skill dirs -------------------

table_block=$(awk '/<!-- SKILLS:START -->/{f=1;next}/<!-- SKILLS:END -->/{f=0}f' "$README")
table_skills=$(grep -oE '\[[a-z0-9-]+\]\(skills/[a-z0-9-]+/\)' <<< "$table_block" \
    | sed -E 's/\[([a-z0-9-]+)\].*/\1/' | sort -u)
actual_skills=$(ls -d "$SKILLS_DIR"/*/ 2>/dev/null | xargs -n1 basename | sort)

comm -23 <(echo "$actual_skills") <(echo "$table_skills") | while read -r s; do
    [[ -z "$s" ]] && continue
    echo -e "${RED}FAIL${NC} $s exists in skills/ but has no row in the Available skills table"
done
missing=$(comm -23 <(echo "$actual_skills") <(echo "$table_skills") | grep -c .)
((ISSUES += missing))

comm -13 <(echo "$actual_skills") <(echo "$table_skills") | while read -r s; do
    [[ -z "$s" ]] && continue
    echo -e "${RED}FAIL${NC} $s has a table row but no matching skills/ directory"
done
orphans=$(comm -13 <(echo "$actual_skills") <(echo "$table_skills") | grep -c .)
((ISSUES += orphans))

# --- 4. Grouping in Available skills table matches frontmatter category --

# macOS ships bash 3.2 (no associative arrays) — a case statement instead.
expected_section_for() {
    case "$1" in
        new-business)     echo "New business" ;;
        post-sale)        echo "Post-sale" ;;
        cross-stage)      echo "Initiative (cross-stage)" ;;
        cross-cutting)    echo "Vertical context" ;;
        deal-intelligence) echo "Deal intelligence" ;;
    esac
}

current_section=""
while IFS= read -r line; do
    if [[ "$line" =~ ^\*\*(.+)\*\*$ ]]; then
        current_section="${BASH_REMATCH[1]}"
    elif [[ "$line" =~ \[([a-z0-9-]+)\]\(skills/[a-z0-9-]+/\) ]]; then
        skill="${BASH_REMATCH[1]}"
        frontmatter=$(awk '/^---$/{c++;next} c==1' "${SKILLS_DIR}/${skill}/SKILL.md" 2>/dev/null)
        category=$(grep "zime:category:" <<< "$frontmatter" | sed 's/.*zime:category: *//' | tr -d ' ')
        expected="$(expected_section_for "$category")"
        if [[ -n "$expected" && "$current_section" != "$expected"* ]]; then
            echo -e "${RED}FAIL${NC} $skill listed under '$current_section', but zime:category=$category expects '$expected'"
            ((ISSUES++))
        fi
    fi
done <<< "$table_block"

# --- 5. Stage/initiative sub-counts, README's closing line ---------------
# "All N stage motions are covered; the initiative set is K skills today."
# The badge/opening/how-these-fit-together/summary anchors above only check
# the total; this is the one line that checks the stage-vs-initiative split.

stage_actual=0
initiative_actual=0
for d in "$SKILLS_DIR"/*/; do
    frontmatter=$(awk '/^---$/{c++;next} c==1' "${d}SKILL.md" 2>/dev/null)
    dimension=$(grep "zime:dimension:" <<< "$frontmatter" | sed 's/.*zime:dimension: *//' | tr -d ' ')
    case "$dimension" in
        stage)      ((stage_actual++)) ;;
        initiative) ((initiative_actual++)) ;;
    esac
done

closing_line=$(grep -oE 'All [0-9]+ stage motions are covered; the initiative set is [0-9]+ skills' "$README")
if [[ -z "$closing_line" ]]; then
    echo -e "${RED}FAIL${NC} count anchor not found: stage/initiative closing line"
    echo "   README wording changed; update scripts/check-docs-sync.sh to match."
    ((ISSUES++))
else
    stage_said=$(grep -oE 'All [0-9]+' <<< "$closing_line" | grep -oE '[0-9]+')
    initiative_said=$(grep -oE 'is [0-9]+ skills' <<< "$closing_line" | grep -oE '[0-9]+')
    [[ "$stage_said" != "$stage_actual" ]] && {
        echo -e "${RED}FAIL${NC} closing line says $stage_said stage motions, but $stage_actual skill dirs are zime:dimension: stage"
        ((ISSUES++))
    }
    [[ "$initiative_said" != "$initiative_actual" ]] && {
        echo -e "${RED}FAIL${NC} closing line says $initiative_said initiative skills, but $initiative_actual skill dirs are zime:dimension: initiative"
        ((ISSUES++))
    }
fi

# --- 6. ROADMAP.md agreement (roadmap-in-sync) ----------------------------
# Every shipped skill must be checked off; no checked box may name a
# directory that doesn't exist.

ROADMAP="ROADMAP.md"
if [[ ! -f "$ROADMAP" ]]; then
    echo -e "${RED}FAIL${NC} ROADMAP.md not found"
    ((ISSUES++))
else
    roadmap_checked=$(grep -oE '^- \[x\] [a-z0-9-]+' "$ROADMAP" | sed -E 's/^- \[x\] //' | sort -u)

    comm -23 <(echo "$actual_skills") <(echo "$roadmap_checked") | while read -r s; do
        [[ -z "$s" ]] && continue
        echo -e "${RED}FAIL${NC} $s exists in skills/ but has no checked box in ROADMAP.md"
    done
    roadmap_missing=$(comm -23 <(echo "$actual_skills") <(echo "$roadmap_checked") | grep -c .)
    ((ISSUES += roadmap_missing))

    comm -13 <(echo "$actual_skills") <(echo "$roadmap_checked") | while read -r s; do
        [[ -z "$s" ]] && continue
        echo -e "${RED}FAIL${NC} ROADMAP.md checks off $s but no matching skills/ directory exists"
    done
    roadmap_orphans=$(comm -13 <(echo "$actual_skills") <(echo "$roadmap_checked") | grep -c .)
    ((ISSUES += roadmap_orphans))
fi

echo ""
echo "================================================================"
if [[ $ISSUES -gt 0 ]]; then
    echo -e "${RED}$ISSUES issue(s)${NC} — README.md is out of sync with skills/"
    exit 1
else
    echo -e "${GREEN}README.md matches skills/${NC} ($actual_count skills)"
fi
