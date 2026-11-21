<!--
Template: the study rulebook. Save as `AI Prompt - {{SHORT}}.md` in the study folder.
Replace every {{PLACEHOLDER}}. Blocks between `<!-- module: X -->` and `<!-- /module -->`
belong to optional modules: keep the content and delete only the marker lines if the module
is on; delete the whole block if it's off, and renumber the study loop so it has no gaps.
Web sources: replace offsets and pdftotext with section URLs, estimated pages, the docs version
and the date mapped (references/sources.md). Plain Markdown: convert links with the table in
references/note-style.md. Delete this comment.
-->
# {{SOURCE_TITLE}} — Study Prompt

> **Purpose:** Study *{{SOURCE_TITLE}}* ({{AUTHORS_OR_PUBLISHER}}) one chapter at a time. Each chapter ends with a reference note.
>
> **Note style:** [[{{NOTE_PROMPT_LINK}}|AI Prompt - {{SHORT}} notes]].
>
> **Tracker:** [[{{README_LINK}}|README]], with progress, the reading plan, the session log, and questions.
>
> **Precedence:** For this folder, this prompt (study process) and the note prompt (note style) override any more general prompts.

---

## 📂 Sources

| What | Where | Role |
|---|---|---|
| **{{SOURCE_TITLE}}** | `{{SOURCE_LOCATION}}` | **Ground truth.** Chapter order, terms, and examples |
<!-- module: comparison -->
| **{{COMPARISON_TITLE}}** | `{{COMPARISON_LOCATION}}` | Enrichment only, beside the chapter it extends |
<!-- /module -->
| **Our study sessions** | The chat | The learner's explanations, confusions, and questions. Notes are built from these |
| **Official docs** | {{DOCS}} | For checking facts and "🔭 Beyond the source" examples |

- **Progress unit:** {{UNIT}} (e.g. printed pages).
- **Page offsets:**
    - {{SHORT}}: `PDF page = printed page + {{OFFSET}}`
<!-- module: comparison -->
    - {{COMPARISON_SHORT}}: `+ {{COMPARISON_OFFSET}}` (or "varies by chapter: always give the PDF page")
<!-- /module -->
- **Extracting text:** `pdftotext -layout -f <pdf first> -l <pdf last> <file> -` into a scratch directory, never into this folder. Get the outline with the study-loop skill's `scripts/pdf_outline.py`.
- **Format:** {{FORMAT}} (Obsidian, or plain Markdown).
- **Language:** notes in {{NOTE_LANGUAGE}}. Translations into {{TRANSLATION_LANGUAGE}} follow the faithful-translation rules{{DIGITS_NOTE}}.

---

## 👤 Learner profile

{{ROLE_ONE_LINE}}

- ✅ **Solid ground to build on:** {{STRENGTHS}}.
- ⚠️ **Fill the gaps under the habits:** {{GAPS}}.
- 🔗 **Bridges for examples:** {{BRIDGES}}.
- 🎯 **Goal:** {{GOAL}}. Tie each chapter to the part of the goal it unlocks.
<!-- module: practice -->
- 🔨 **Practice priority:** {{PRACTICE_SKILL}}. From {{PRACTICE_START}} on, give exercises from the README's practice track and review the learner's work.
<!-- /module -->
- 🧰 **Practice environment:** {{PRACTICE_ENV}}. Never suggest destructive commands against real data.

---

## 🔁 Study loop

📌 **Reading plan:** the README decides what to read. Its Chapters table (Plan column) marks each chapter 📖 read, ✂️ only the listed pages, 👀 skim, or ⏭️ skip<!-- module: goal-plan -->, and its **What to Learn** list adds comparison-source sections beside the chapter they extend<!-- /module -->. Don't teach skipped pages.

1. 🗺️ **Preview:** one screen. What the chapter answers, what it introduces, and what the learner already uses. **Always include a reading guide:** every section with its pages (and PDF pages) marked 📖 Read, 👀 Skim or ⏭️ Skip, with why for skim and skip. The README's current-chapter checklist uses the same marks.

2. 📖 **Read and try:** the learner reads a section or two, tries things, and reports how far they got. Update the README.

    - ❓ **Questions while reading:** a question about the text means the text wasn't clear. Answer it, then log it right away in the README's **📝 Questions While Reading** (chapter, page, question, one-line answer). In the chapter note, each logged question appears twice: a summary in its section, and an entry in the Q&A. Then it goes into the handbook, and gets ticked ✅.

    - 🧪 **Hands-on:** test examples in a scratch directory before giving them, and show real output. Say plainly when the source's example is broken or outdated.

3. 🗣️ **Explain-back:** after a chapter, the learner explains it in their own words. Correct mistakes, and ask "why" and "what would happen if" questions.

4. 🔭 **Beyond the source:** at most 1–2 outside examples per section, a few lines each. Go deeper only when asked.

5. 📝 **Note:** write the chapter note with the note prompt, from the source and the session. It must cover every logged question.

<!-- module: handbook -->
6. 📘 **Merge into the handbook (required):** right after the chapter note, merge its concepts into [[{{HANDBOOK_INDEX_LINK}}|the {{TOPIC}} Handbook]], following its prompt. A chapter isn't finished until the handbook is updated.
<!-- /module -->

7. 🔁 **Recall:** start each session with 3 questions on the previous material. First check the Session Log, and skip the recall if it's already logged. Log the answers with corrections, and add weak points to **Open Questions** to re-check.

**Depth target:** L2 (explain how it works and why) by default. L3 (use it to solve a real problem) for {{L3_CHAPTERS}}.

---

## 📝 Chapter notes

- **Naming:** `{N}. {Chapter Title}.md`. Long chapters may split into `- Part 1`, `- Part 2`.
- **Header:** `[[{{README_LINK}}|{{ICON}} {{SHORT}}]] · Ch.{N} · pp. {printed range}`, then one or two sentences on what the chapter answers.
- **Size:** usually 150–350 lines. Split rather than grow.
- Correct source errors silently. Don't reproduce long passages: explain in our own words.

---

## 📊 Progress tracking

The README holds the progress bars, current position, session log, questions while reading, and open questions.

- Update it whenever the learner reports how far they read: the plan bar, the whole-source bar, the chapter bar, section checkboxes, goal checklists, the current position, and the session log.
- `<progress value="read" max="total">` followed by the `read / total · %` text.
- The **Plan** bar counts only planned pages ({{PLANNED_TOTAL}} in total). The **Whole source** line counts all {{READABLE_TOTAL}}.
- When the learner says "always…" or "from now on…", add the rule here.
