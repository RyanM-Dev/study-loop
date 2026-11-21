# 📘 The Topic Handbook (optional module)

Chapter notes are a record of **one source**. The handbook is **one unified reference for the whole topic**. It merges every concept the learner has studied, from every source (books, courses, docs, their own project notes), into numbered notes ordered from beginner to advanced.

Use it when the learner studies a topic from more than one source, or plans to. A second book on the same topic then merges into the same handbook instead of starting over.

## Contents

1. [Structure](#structure)
2. [Creating a handbook](#creating-a-handbook)
3. [Merging a chapter](#merging-a-chapter)
4. [Handbook note template](#handbook-note-template)
5. [References table](#references-table)

---

## Structure

```text
<Topic> Handbook/
├── 0. <Topic> Handbook.md            ← index: parts, notes, status, sources, last updated
├── AI Prompt - <Topic> Handbook.md   ← this module's rules plus the fixed curriculum
├── 1. <First Note>.md
└── …
```

- 🔢 **The curriculum is fixed.** Notes are numbered by learning order, and **numbers never change**. A new concept goes into the note it belongs to, as a new section. Never renumber.
- ✅ **Only studied concepts get content.** A curriculum entry the learner hasn't studied stays in the index as 📖 *planned*, with no file.
- 🧭 **Beginner → advanced.** Each note builds only on the notes before it.

---

## Creating a handbook

Do this during setup, or the first time a chapter gets merged:

1. 🗂️ **Draft the curriculum.** 15–25 notes, grouped into 3–6 parts, from the primary source's chapters, the goal's syllabus, and what the learner already knows. Name notes by **concept**, not by source chapter ("Streams, Pipes, and Redirection", not "Chapter 11").
2. 🧭 **Add placement rules** for the unclear cases ("`awk` and `sed` → 5, pipes stay in 4").
3. 📝 **Write the handbook prompt** from `assets/templates/handbook-prompt.md` and the index from `handbook-index.md`.
4. 📥 **Seed it with what the learner already studied**, if they have earlier notes on the topic. Merge those into the matching notes, marked ✅ studied.

---

## Merging a chapter

Run this after every chapter note, and after any comparison-source section the plan lists:

1. 🔎 **List the chapter's new concepts**, including the logged questions and their answers.
2. 🗂️ **Find each concept's handbook note** with the curriculum and placement rules.
3. ✍️ **Merge:**
    - **The note exists:** add the material to the right section, in learning order. Keep **one explanation per concept**: take the clearest one, and add only the details the other sources have. Update Q&A, Quick Reference and Things to Remember only where the new material changes them.
    - **The note is still planned:** create it from the template. Pull in related material the learner already studied elsewhere.
4. 📚 **Update the References table:** add the source, or change its status to ✅ studied.
5. 🔁 **Fix pointers elsewhere.** Other handbook notes may have a "🔜 Later: … in Ch.N" line or a 📖 planned row for this chapter. Update them.
6. 🧭 **Update the index:** the note's status, "merged from", and the **Last updated** line with today's date.
7. 🗺️ **Update the study README's knowledge map:** 🟡 or 📖 → ✅.
8. 📘 **Add the pointer** to the chapter note: `📘 Merged into [[…]]`.
9. ✅ **Check** that links resolve, Mermaid renders, and ⬅️ ➡️ navigation is right on the neighbours of any new note.

**Merging rules:**
- 🧹 When sources disagree, give the modern, correct answer, without commentary.
- 🧪 Keep the learner's real examples, and the confusions from study sessions.
- 🔜 At most one "🔜 Later" line per section for a topic not yet studied. Never teach what hasn't been studied.
- 📏 Keep notes to roughly 250–450 lines. Past ~600, split a section into `{N}a. …` rather than renumbering.

---

## Handbook note template

```markdown
# {emoji} {Title}

[[<Topic> Handbook/0. <Topic> Handbook|{icon} <Topic> Handbook]] · Part {n}: {part} · ⬅️ [[{N-1}. …]] · ➡️ [[{N+1}. …]]

{One or two sentences: what this note answers.}

> [!toc]- 📑 Contents
> …

…merged sections, beginner → advanced…

### 🧪 Q&A
## 🔨 Hands-On Practice
### 📋 Quick Reference
### 🧠 Things to Remember
### 💡 Pro Tips
### 🔗 Related Topics
## 📚 References
```

The ⬅️ ➡️ links point to the previous and next notes that **exist**, skipping planned numbers that have no file yet. The style is the same as chapter notes ([note-style.md](note-style.md)).

---

## References table

Every handbook note ends with a table listing **every** source for its concepts, studied or not:

```markdown
| Source | Where | Status |
|---|---|---|
| 📝 Chapter note: [[…/4. Using Shell History\|4. Using Shell History]] | whole note | ✅ studied |
| 📕 Primary Ch.4 | pp. 45–49 | ✅ studied |
| 📕 Primary Ch.10 | pp. 115–125 | 📖 planned · 🔁 env vars are here · 🆕 config layers → here |
| 📗 Comparison Ch.7 | pp. 272–279 [PDF 288–295] | 🔭 optional |
```

- **Status:**
    - ✅ studied
    - 📖 planned in the reading plan
    - 🔭 optional extra reading
    - ⏭️ skipped on purpose
- **Every 📖 planned row carries a hint:**
    - 🔁 what the note already covers from other sources;
    - 🆕 what's new, and → which note it will go into.
- When a row becomes ✅, drop its hint: the content is in the note now.
- Give printed pages, with the PDF page in brackets for comparison sources.
