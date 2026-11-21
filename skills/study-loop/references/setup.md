# 🏗️ Setup: Starting a New Source

Setup runs once per source. At the end, the learner has a study folder with a rulebook, a note prompt, and a README tracker, and knows exactly what to read first.

## Contents

1. [Ask in one batch](#1-ask-in-one-batch)
2. [Inspect the source](#2-inspect-the-source)
3. [Build the reading plan](#3-build-the-reading-plan)
4. [Write the files](#4-write-the-files)
5. [Hand over](#5-hand-over)

---

## 1. Ask in one batch

Ask everything at once rather than one question per turn. Skip anything the learner already told you or you can find out yourself, such as page counts or the folder that holds the PDF. Offer a sensible default for each question, so the learner can just say "defaults".

**🧱 Always ask:**

1. 📚 **Primary source.** A file path (PDF, EPUB) or a link (documentation site, online book, course page, playlist). This is the **ground truth**: its order and terms lead.
2. 📁 **Where the notes go.** A folder in an Obsidian vault, or any folder. The default is `<vault>/<Topic>/<Source Title>/`.
3. 🖋️ **Note format.** Obsidian (the default: wikilinks, `> [!answer]-` callouts, Mermaid) or plain Markdown that renders on GitHub.
4. 👤 **Learner profile.**
    - What they do and what they already know well. These are the bridges for examples.
    - What they *use* but don't really understand. These are the gaps to fill.
    - Where earlier notes live, if any, so you can check what's already covered.
5. 🎯 **Goal.** Why this source: a course they're taking, a job, an exam, a project, or general depth. The goal decides what's worth reading.
6. 🌐 **Language.** The language for notes and chat. Whether they'll want translations of passages, and into which language.

**🧩 Ask about optional modules.** Offer each with a one-line explanation. Turn on only what the learner wants:

| Module | What it adds | Ask for |
|---|---|---|
| 📖 **Comparison sources** | Other books or docs used only for **enrichment**, beside the chapter they extend | Paths or links. You'll find their offsets yourself |
| 🎯 **Goal-driven plan** | Each chapter marked read, ✂️ only some pages, or skip, based on the goal and what the learner knows. Includes a knowledge map | The goal's syllabus (a link, a folder of notes, or a list) and how far they've got |
| 📘 **Topic handbook** | One unified, beginner-to-advanced reference for the topic that every chapter (and later sources) merges into | The topic name, and whether a handbook already exists |
| 🔨 **Practice track** | A ladder of hands-on exercises for a skill the learner wants to practise (scripting, SQL, …) | Which skill, and where they can practise safely |

---

## 2. Inspect the source

Do this yourself; don't ask the learner. Details per source type are in [sources.md](sources.md).

- 📄 **PDF:** run `python3 scripts/pdf_outline.py <file.pdf>`. It prints chapters and sections with PDF pages, the **printed-page offset**, and readable pages per chapter. Spot-check the offset on two pages.
- 🌐 **Web source:** fetch the table of contents or navigation page, and list every chapter and section with its URL. Choose a **progress unit**: sections, or estimated reading minutes for long pages.
- 🎬 **Video course:** list modules and lessons with their lengths. The unit is lessons or minutes.
- 📖 **Comparison sources:** find each one's offset. If it varies by chapter, record it per chapter.

Count **readable** pages per chapter, without blank pages, ads, and "other books" pages. Progress is tracked in printed pages, because those are what the learner sees.

---

## 3. Build the reading plan

**Without a goal-driven plan:** every chapter is 📖 Read. Still mark sections that are obviously optional (installation for another OS, a crash course in something they know) as 👀 Skim.

**With a goal-driven plan:**

1. 🔎 **Find what the learner already knows.** Use their profile and earlier notes. If they have a notes folder, skim its titles and headings. Don't re-teach what's already solid.
2. 🎯 **Find what the goal needs.** Go through the syllabus, module by module, and list what each module relies on.
3. ⚖️ **Mark every chapter:**
    - 📖 **Read all**: the goal needs it, and it's new.
    - ✂️ **Only pages X–Y**: part is new, part is known.
    - 👀 **Skim**: known, but worth a glance for details.
    - ⏭️ **Skip**: known well, or not needed for the goal. Give the reason in **Don't Read**.
4. 📚 **Place comparison-source sections beside the chapter they extend**, with exact pages and PDF pages. Use them only where they add something the primary source lacks.
5. 🗺️ **Draw the knowledge map:** a Mermaid `mindmap` of what the goal needs, each leaf marked ✅ known, 🟡 known a little, or 📖 to learn.
6. 🪜 **Stage the plan** when the goal has phases ("before module X"). The learner reads what the next phase needs first.

**Plan edge cases:**

- 🧭 **Stages may reorder chapters.** The Chapters table keeps the source's order, with a Stage column. "Current chapter" and "current position" follow the **plan's** order: the next unread item of the current stage.
- ❔ **No syllabus given?** Plan for a typical version of the goal (e.g. "a usual Git + CI module"). List what you assumed in **Open Questions**, and revise the plan once the learner shares the real one.
- 🔨 **Practice skill = the source's topic?** Don't repeat the reading list in the practice track. Map each rung to the sections it practises instead.

Assign a **depth target** per chapter:
- **L2**: explain how it works and why. The default.
- **L3**: use it to debug or solve a real problem.
- **L4**: teach it to others.

---

## 4. Write the files

Fill the templates in `assets/templates/`. Replace every `{{PLACEHOLDER}}`, and delete sections for modules that are off, along with their table-of-contents entries. Don't leave empty sections behind.

| Template | Becomes | Notes |
|---|---|---|
| `rulebook.md` | `AI Prompt - {Short}.md` | `{Short}` is a short name for the source, such as `SDGL` or `Pro Git` |
| `note-prompt.md` | `AI Prompt - {Short} notes.md` | Points to the style in [note-style.md](note-style.md). Copy that style into the file so it works without the skill. Add source-specific rules |
| `README.md` | `README.md` | The tracker. Fill the Chapters table from step 2 and the plan from step 3 |
| `handbook-prompt.md`, `handbook-index.md` | `<Topic> Handbook/AI Prompt - <Topic> Handbook.md` and `0. <Topic> Handbook.md` | Only with the handbook module. If a handbook already exists, extend its curriculum instead of making a new one |
| `AGENTS.md` | `AGENTS.md` in the folder that holds the source files (or the study folder) | Tells any agent opened there where the rules live. For Claude Code, also write a `CLAUDE.md` containing `@AGENTS.md` |

**Naming:**
- Prompt files are named `AI Prompt - {name}.md` and sit **beside the notes they govern**. If the learner's notes already use another naming scheme, follow theirs.
- Chapter notes are `{N}. {Chapter Title}.md`. Use the source's own chapter titles, and drop characters that aren't allowed in filenames.

**Adapting the templates:**

- 🖋️ **Plain Markdown:** convert every wikilink and callout with the table in [note-style.md](note-style.md#plain-markdown-format), including in the README and the prompts, and drop the Contents callouts. GitHub has its own outline, and emoji headings make fragile anchors.
- 🌐 **Web sources:** replace PDF offsets and `pdftotext` with section URLs, estimated pages, the docs version, and the date mapped. Add the per-section estimates table ([sources.md](sources.md#web-sources)).
- 🧩 **Modules off:** delete their blocks and Contents entries, and renumber lists so there are no gaps.
- 📖 **Glossary:** create `Translation Glossary.md` at the first translation, not during setup.

---

## 5. Hand over

Finish with a short message:

1. 📁 **What you created:** a list of the files.
2. 🗺️ **The plan in one screen:** the chapters table with its marks, and the first stage.
3. 📖 **The first reading guide:** the first chapter's sections, marked 📖 / 👀 / ⏭️, with pages, PDF pages, or URLs.
4. 🧪 **Something to try** while reading, if the topic is hands-on.

Log the setup as session 0 in the Session Log.
