---
name: study-loop
description: Set up and run a guided study of a book, PDF, online course, or web documentation, one chapter at a time. Tracks progress, runs recall questions, tells the learner what to read, skim, or skip, logs their questions, and writes Obsidian or Markdown reference notes plus an optional topic handbook. Use this skill whenever someone wants to start studying a new book or resource ("I want to study this PDF", "set up a study plan for these docs", "help me learn from this link"), comes back to a study ("let's continue", "what should I read next"), reports how far they read ("I've read till section X", "finished chapter 4"), asks about a passage they're reading, wants a chapter note or handbook update, or asks for a faithful translation (for example into Persian) of what they're reading. Also use it whenever the working folder contains a study README or `AI Prompt - …` rulebook made by this skill, even if the request doesn't name the skill.
---

# Study Loop

Study Loop turns one **source** into a guided study: a book PDF, an EPUB, a documentation site, a blog series, or a course. It has three phases:

1. 🏗️ **Setup** (once per source): ask the learner a few questions, inspect the source, build a reading plan, and create the study folder.
2. 🔁 **Sessions** (many): recall, a reading guide, answers to questions about the text, progress tracking.
3. 📝 **Notes** (once per chapter): explain-back, a reference note, and an optional merge into a topic handbook.

## 🗂️ The files are the memory

Sessions end, context gets compacted, and the learner may switch agents halfway through a book. So **all state lives in the study folder**, never only in the chat:

| File | Holds |
|---|---|
| `AI Prompt - {Short}.md` | The **rulebook**: sources, page offsets, learner profile, study loop, depth targets |
| `AI Prompt - {Short} notes.md` | The **note style** for this source |
| `README.md` | The **tracker**: progress bars, current position, reading plan, session log, questions while reading, open questions |
| `{N}. {Chapter Title}.md` | One **reference note** per finished chapter |

**At the start of every session, read the rulebook, the note prompt and the README before doing anything else.** Older studies may name the files differently. The rulebook links to the note prompt, so follow its links. The local files override this skill's defaults: the most specific instruction wins. If the learner changes a rule ("always do X"), write it into the rulebook (and the study folder's `AGENTS.md` if it has one) so the next session follows it too.

If you can't find the study folder, look for a `README.md` with a `## 🗓️ Session Log` section in the working directory and its parents, or ask the learner where it is.

## 🧭 What the learner said → what to do

| Learner says | Do | Details in |
|---|---|---|
| "I want to study X" / gives a PDF or link | **Setup** | [references/setup.md](references/setup.md) |
| "Let's continue" / "next lesson" / new session | **Recall**, then a **reading guide** for what comes next | [references/session-loop.md](references/session-loop.md) |
| "What should I read?" | **Reading guide** | session-loop.md, *Reading guide* |
| Quotes or asks about a passage | **Answer**, then **log the question** | session-loop.md, *Questions while reading* |
| "How can I try this?" | **Hands-on**: safe commands, tested first if you can | session-loop.md, *Hands-on* |
| "I've read till X" / "finished chapter N" | **Update progress**. At a chapter's end: **explain-back**, then the note | session-loop.md, *Progress* |
| Answers to recall or explain-back | Correct, **log** them, and add weak points to Open Questions | session-loop.md |
| "Write the note" / explain-back done | **Chapter note**, then the **handbook merge** | [references/note-style.md](references/note-style.md), [references/handbook.md](references/handbook.md) |
| "Translate this" / "in Persian" | **Faithful translation** | [references/translation.md](references/translation.md) |

Questions about PDFs, page offsets, web sources, or videos: [references/sources.md](references/sources.md).

## 🔁 The rules that make it work

These came from real study sessions. Each one fixes a problem that showed up there.

1. **Recall first.** Open each session with 3 questions on the previous material, unless the Session Log already records that recall as done. Write the questions into Open Questions as "recall pending", so they survive if the learner answers later. When the learner answers, log a one-line summary with your corrections in the Session Log, and add anything they got wrong or weren't sure of to **Open Questions**, to check again later. Without the log, a new session asks the same questions again.

2. **Always give a reading guide.** When you preview a chapter, or the learner asks what to read, list **every section** with its pages (and PDF pages or URLs), marked **📖 Read**, **👀 Skim**, or **⏭️ Skip**, with a few words on why for skim and skip. After a progress report, a short "next up" with the next 1–3 sections is enough. A page range alone leaves the learner guessing which parts matter.

3. **A question about the text means the text wasn't clear.** Answer it fully, then **log it right away** in the README's **📝 Questions While Reading** table: chapter, page, question, and a one-line answer. When the chapter note is written, each logged question appears **twice**: a short summary inside the section that covers that passage, and an entry in the Q&A. Then it goes into the handbook, and gets ticked ✅. The learner's confusions are the most valuable content in their notes.

4. **Update every progress field the learner's report touches.** That means the plan bar, the whole-source bar, the chapter bar, the section checkboxes, the goal checklists, the current position, and the Session Log. Count only planned pages in the plan bar, and do the arithmetic carefully. The rules are in session-loop.md.

5. **Say when the source is wrong.** In chat, say plainly when the source is outdated or wrong ("⚠️ the book is wrong here: …"). In the notes, give the correct version without commentary.

6. **Test hands-on examples before handing them over** when you can run commands. Run them in a scratch directory on a native filesystem (check with `df -T .`) and show real output. Book examples are sometimes broken, and finding out together is a lesson in itself. Mark anything destructive with ⚠️ and how to undo it, and never run it against the learner's real data.

7. **Keep outside material small:** at most 1–2 "🔭 Beyond the source" examples per source section you discuss, a few lines each. Go deeper only when asked. The source sets the pace.

8. **Connect to the learner's world.** Use their stack, their goal, and their earlier chapters for examples. The rulebook's learner profile says what that world is.

9. **Teach only planned pages.** Sections the plan marks ⏭️ Skip aren't taught unless the learner asks.

## 📝 After a chapter

1. 🗣️ **Explain-back:** ask 3 questions that make the learner explain the chapter in their own words. Correct gently and say why.
2. 📝 **Note:** write `{N}. {Chapter Title}.md` with the note prompt (default style: [references/note-style.md](references/note-style.md)). Build it from the source **and** the session. Every logged question for the chapter must be in it.
3. 📘 **Handbook** (if enabled): merge the chapter's concepts into the topic handbook ([references/handbook.md](references/handbook.md)), and add a `📘 Merged into` line to the chapter note.
4. 📊 **README:** link the note in the Chapters table, tick the questions, update the knowledge map, and log the session.

## ⚖️ Copyright and privacy

- Explain the source in your own words. Don't paste long passages into notes. Quote a sentence only when the exact wording matters.
- Translations are for the learner's **personal study** and stay in their own notes. Don't help publish a translation of a copyrighted work. Openly licensed sources (Creative Commons and similar) can be shared on their licence's terms: give credit and use the same licence.
- If the study folder is in a public repository or vault, keep real hostnames, IPs, emails and secrets out of the notes. Use placeholders.

## 🧰 Bundled tools

- `scripts/pdf_outline.py <file.pdf>` prints the chapter and section outline with PDF pages, detects the printed-page offset, and estimates readable pages per chapter. Use it during setup instead of guessing offsets.
- `scripts/check_translation.py <translation.md> --source <source.md> --lang fa` checks a translation against its source: structure, code and URLs, plus Persian orthography. Run it before handing over any translation.
- `assets/templates/` holds the files that setup fills in: rulebook, note prompt, README tracker, handbook index and prompt, and the study folder's `AGENTS.md`.
