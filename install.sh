#!/usr/bin/env bash
# Install the study-loop skill for your coding agents.
#
#   ./install.sh                     # Claude Code (~/.claude/skills) + shared ~/.agents/skills
#   ./install.sh --agent grok        # add one agent's own folder (repeatable)
#   ./install.sh --all               # every known agent folder
#   ./install.sh --dir ~/my/skills   # a custom skills folder (repeatable)
#   ./install.sh --project           # this project only: ./.claude/skills and ./.agents/skills
#   ./install.sh --copy              # copy instead of symlink (default: symlink, so `git pull` updates it)
#   ./install.sh --uninstall         # remove it from the same places
#   ./install.sh --dry-run           # show what would happen
set -euo pipefail

NAME="study-loop"
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skills/$NAME"

# agent -> skills folder (user level)
agent_dir() {
    case "$1" in
        claude)   echo "$HOME/.claude/skills" ;;   # Claude Code (Grok also reads this folder)
        agents)   echo "$HOME/.agents/skills" ;;   # shared Agent Skills folder: Codex, Gemini CLI, Copilot, Cursor, OpenCode, Amp, ...
        codex)    echo "$HOME/.codex/skills" ;;    # older Codex versions
        gemini)   echo "$HOME/.gemini/skills" ;;
        copilot)  echo "$HOME/.copilot/skills" ;;
        cursor)   echo "$HOME/.cursor/skills" ;;
        grok)     echo "$HOME/.grok/skills" ;;
        *) return 1 ;;
    esac
}
ALL_AGENTS=(claude agents codex gemini copilot cursor grok)

usage() { sed -n '2,13p' "$0" | sed 's/^# \{0,1\}//'; }

mode=link; action=install; dry=0; project=0
targets=(); explicit=0

while [[ $# -gt 0 ]]; do
    case "$1" in
        --agent)     shift; d="$(agent_dir "${1:-}")" || { echo "Unknown agent: ${1:-}. Known: ${ALL_AGENTS[*]}" >&2; exit 2; }
                     targets+=("$d"); explicit=1 ;;
        --all)       for a in "${ALL_AGENTS[@]}"; do targets+=("$(agent_dir "$a")"); done; explicit=1 ;;
        --dir)       shift; targets+=("${1:?--dir needs a path}"); explicit=1 ;;
        --project)   project=1 ;;
        --copy)      mode=copy ;;
        --uninstall) action=uninstall ;;
        --dry-run)   dry=1 ;;
        -h|--help)   usage; exit 0 ;;
        *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
    esac
    shift
done

[[ -f "$SRC/SKILL.md" ]] || { echo "Can't find $SRC/SKILL.md. Run this from the repo." >&2; exit 1; }

if [[ $project -eq 1 ]]; then
    targets=("$PWD/.claude/skills" "$PWD/.agents/skills")
elif [[ $explicit -eq 0 ]]; then
    targets=("$(agent_dir claude)" "$(agent_dir agents)")
fi

run() { if [[ $dry -eq 1 ]]; then echo "  [dry-run] $*"; else "$@"; fi; }

# de-duplicate while keeping order (no associative arrays: macOS ships bash 3.2)
seen="|"
for dir in "${targets[@]}"; do
    dir="${dir/#\~/$HOME}"
    [[ "$seen" == *"|$dir|"* ]] && continue
    seen="$seen$dir|"
    dest="$dir/$NAME"

    if [[ $action == uninstall ]]; then
        if [[ -L "$dest" || -e "$dest" ]]; then
            run rm -rf "$dest"; echo "🗑️  removed  $dest"
        fi
        continue
    fi

    run mkdir -p "$dir"
    if [[ -L "$dest" || -e "$dest" ]]; then
        if [[ -L "$dest" && "$(readlink -f "$dest")" == "$(readlink -f "$SRC")" ]]; then
            echo "✅ already linked  $dest"; continue
        fi
        run rm -rf "$dest"
    fi
    if [[ $mode == copy ]]; then
        run cp -R "$SRC" "$dest"; echo "📦 copied   $dest"
    else
        run ln -s "$SRC" "$dest"; echo "🔗 linked   $dest -> $SRC"
    fi
done

if [[ $action == install ]]; then
    echo
    echo "Done. Restart your agent, then say e.g.: \"I want to study <book.pdf or link>\"."
    [[ $mode == link ]] && echo "Update later with: git -C \"$REPO_DIR\" pull"
fi
