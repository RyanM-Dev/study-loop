# 📚 study-loop

**A skill for AI coding agents that turns a book, a PDF, a course, or a documentation site into a guided study,** with reading plans, recall questions, progress tracking, and reference notes that are actually yours.

Works with **Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor, Grok**, and any agent that reads [Agent Skills](https://agentskills.io) (`SKILL.md`).

```text
You:   I want to study ~/Books/linux-guide.pdf. I'm a Go developer heading into Kubernetes.
Agent: (asks a few setup questions, maps the book, builds a plan, creates the study folder)
       📖 Ch.1: read pp. 1–12 · 👀 skim pp. 13–15 (you know this) · ⏭️ skip pp. 16–20 (installing on macOS)

You:   "A symbolic link may appear as: versions/latest -> bin/app-3.1". How do I try this?
Agent: (runs it in a scratch folder first: the book's example is broken, and here's why…)
       Logged in Questions While Reading → it will be in your Ch.5 note.

You:   I've read till "Hard links".
Agent: Plan 54/174 (31%) · Ch.5 5/14 · position p. 62 · session logged.
```

---

## ✨ What it does

| | |
|---|---|
| 🏗️ **Setup** | Asks about your sources, your background, and your goal. Maps the source: chapters, sections, PDF page offsets, readable pages. Builds a reading plan and creates a study folder |
| 🧭 **Reading guides** | Every preview lists each section as **📖 Read / 👀 Skim / ⏭️ Skip**, with pages and the reason |
| 🔁 **Recall** | Each session opens with 3 questions on last time. Answers and weak points are logged, so nothing gets asked twice and nothing weak gets forgotten |
| ❓ **Questions while reading** | A question about the text means the text wasn't clear. Each one is answered, logged, and later written into the chapter note **and** its Q&A |
| 🧪 **Hands-on** | "How can I try this?" gets safe commands, tested in a scratch folder first, with real output |
| 📊 **Progress** | Plan bar, chapter bars, checkboxes, current position, and a session log, all in a `README.md` you can open in Obsidian or on GitHub |
| 📝 **Reference notes** | One note per chapter, written from the source *and* your session: diagrams, examples from your world, Q&A, practice, and a quick reference |
| 📘 **Topic handbook** *(optional)* | One unified beginner-to-advanced reference that every chapter, and every later source on the topic, merges into |
| 🎯 **Goal-driven plan** *(optional)* | Maps chapters to a goal (a course, a job, an exam) and skips what you already know |
| 📖 **Comparison sources** *(optional)* | Other books or docs used only for enrichment, placed beside the chapter they extend |
| 🔨 **Practice track** *(optional)* | A ladder of hands-on exercises for a skill you want to drill |
| 🌐 **Faithful translation** | Translates passages, for example into **Persian**, keeping the author's voice, storytelling, and structure: no summarising, no bulleting |

**Sources:** PDF books (with page-offset detection), EPUB, documentation sites and online books (by link), blog series, and video courses.

**Notes:** Obsidian by default (wikilinks, callouts, Mermaid), or plain Markdown that renders on GitHub.

---

## 🚀 Install

### Option 1: clone and run the installer (Linux, macOS, WSL)

```bash
git clone https://github.com/RyanM-Dev/study-loop.git ~/.local/share/study-loop
~/.local/share/study-loop/install.sh
```

This symlinks the skill into `~/.claude/skills/` (Claude Code; Grok reads it too) and `~/.agents/skills/` (the shared folder read by Codex, Gemini CLI, Copilot, Cursor, OpenCode and others). Update it any time with `git -C ~/.local/share/study-loop pull`.

| Command | Does |
|---|---|
| `./install.sh --agent grok` | Also install into one agent's own folder: `claude`, `agents`, `codex`, `gemini`, `copilot`, `cursor`, `grok` (repeatable) |
| `./install.sh --all` | Install into every folder above |
| `./install.sh --dir PATH` | Install into any skills folder |
| `./install.sh --project` | Only for the current project (`./.claude/skills`, `./.agents/skills`) |
| `./install.sh --copy` | Copy instead of symlink |
| `./install.sh --uninstall` | Remove it again (combine with the same flags) |
| `./install.sh --dry-run` | Show what it would do |

### Option 2: the `skills` CLI (any OS, many agents)

```bash
npx skills add RyanM-Dev/study-loop -g
```

### Option 3: Claude Code plugin

```text
/plugin marketplace add RyanM-Dev/study-loop
/plugin install study-loop@study-loop
```

### Option 4: by hand

Copy `skills/study-loop/` into your agent's skills folder, so that you end up with `…/skills/study-loop/SKILL.md`.

> 💡 Agents load skills at startup. Restart your agent after installing.

---

## 🧑‍🎓 Usage

Just talk to your agent. You don't need any commands, though in Claude Code and Grok `/study-loop` works too.

| Say | It will |
|---|---|
| "I want to study `~/Books/ddia.pdf`" / "help me learn from https://git-scm.com/book" | Run **setup** |
| "Let's continue" / "next lesson" | Ask **recall** questions, then give a **reading guide** |
| "What should I read next?" | Give a **reading guide** |
| Paste a passage + "explain" / "how can I try this?" | **Answer**, **log** it, and give **hands-on** steps |
| "I've read till section X" / "finished chapter 4" | **Update progress**. At the end of a chapter: **explain-back**, then the **note** |
| "Write the note for chapter 4" | Write the **chapter note** (and merge it into the **handbook**) |
| "Translate this section into Persian" | Do a **faithful translation** |
| "From now on, always …" | Save the rule into the study's rulebook |

### 📁 What setup creates

```text
<your notes>/<Topic>/<Source Title>/
├── AI Prompt - <Short>.md          ← rulebook: sources, offsets, your profile, the study loop
├── AI Prompt - <Short> notes.md    ← how notes look (editable per source)
├── README.md                       ← tracker: progress, plan, session log, questions
├── 1. <Chapter Title>.md           ← one note per finished chapter
└── …
<your notes>/<Topic>/<Topic> Handbook/   (optional)
├── 0. <Topic> Handbook.md
└── AI Prompt - <Topic> Handbook.md
<folder with the PDF>/AGENTS.md  (+ CLAUDE.md)   ← points any agent at the rules
```

**All state lives in these files,** so you can switch agents, or come back after a month, and pick up exactly where you left off. The files in your study folder override the skill's defaults, so tune them as you like.

---

## 🗂️ Repository layout

```text
skills/study-loop/
├── SKILL.md                    ← entry point: modes and core rules
├── references/
│   ├── setup.md                ← the setup interview, inspecting sources, building the plan
│   ├── session-loop.md         ← recall, reading guides, questions, hands-on, progress, explain-back
│   ├── note-style.md           ← how reference notes are written (Obsidian and plain Markdown)
│   ├── handbook.md             ← the unified topic handbook
│   ├── sources.md              ← PDFs, offsets, EPUB, web docs, video courses
│   └── translation.md          ← faithful translation (Persian specifics included)
├── assets/templates/           ← rulebook, note prompt, README tracker, handbook, AGENTS.md
└── scripts/pdf_outline.py      ← PDF outline + printed-page offset + readable pages
install.sh                      ← multi-agent installer
.claude-plugin/                 ← Claude Code plugin + marketplace manifest
```

**Optional tools** it uses when present: PyMuPDF (`pip install pymupdf`) or poppler-utils (`pdftotext`, `pdfinfo`) plus `mutool` for PDFs. `pandoc` helps with EPUB.

---

## ⚖️ A note on copyright

The skill explains sources in its own words and keeps quotes short. Translations are for your **personal study**: please don't publish translations of copyrighted books.

## 📄 License

MIT
