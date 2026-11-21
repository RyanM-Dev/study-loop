<!--
Template: the pointer file. Save as `AGENTS.md` in the folder that holds the source files (or in
the study folder). For Claude Code, also write `CLAUDE.md` containing just `@AGENTS.md`.
Use absolute paths when the folder is private and local. Use paths relative to the study
folder when the notes live in a shared or public repository, so home directories don't leak.
For web sources, replace the page-number facts with the site URL, docs version, and date
mapped. Delete this comment.
-->
# {{SOURCE_TITLE}} Study — Agent Instructions

This folder belongs to a guided study of *{{SOURCE_TITLE}}*, run with the **study-loop** skill. If the skill is installed, use it. Either way, **read these before doing anything:**

1. `{{RULEBOOK_PATH}}` is the rulebook: sources, offsets, learner profile, and the study loop.
2. `{{NOTE_PROMPT_PATH}}` is how chapter notes are written.
3. `{{README_PATH}}` is where we are now: progress, the reading plan, the session log, questions while reading, and open questions.
<!-- module: handbook -->
4. `{{HANDBOOK_PROMPT_PATH}}` is how the {{TOPIC}} Handbook is kept up to date. Every chapter is merged into it.
<!-- /module -->

## Quick facts

- **Source:** `{{SOURCE_LOCATION}}`. {{CHAPTER_COUNT}} chapters, {{READABLE_TOTAL}} readable {{UNIT}}.
- **Page numbers:** `PDF page = printed page + {{OFFSET}}`. Progress is tracked in printed pages.
- **Reading plan:** the README's Chapters table and plan decide what to read. Skipped pages aren't taught.
- **Text extraction:** into a scratch directory, never into this folder.
- **Notes:** `{{STUDY_FOLDER}}/{N}. {Chapter Title}.md`

## Every session

1. Read the README to find the current chapter and position.
2. Start with 3 recall questions on the previous material, unless the Session Log already records that recall as done. Log the answers once given.
3. When previewing a chapter, or when asked what to read, give a reading guide: each section with its pages, marked 📖 Read, 👀 Skim or ⏭️ Skip, with why for skim and skip.
4. When the learner asks about a passage, answer it and log it at once in the README's **📝 Questions While Reading**. The chapter note includes each answer, in its section and in the Q&A.
5. When the learner reports how far they read, update every progress field in the README and the session log.
6. After a chapter: explain-back, then the chapter note<!-- module: handbook -->, then the handbook merge<!-- /module -->.
