# 🔁 Sessions: The Study Loop

A session is a sitting: the learner reads a section or two, asks questions, and reports how far they got. A chapter usually takes 1–3 sessions.

## Contents

1. [Session start](#1-session-start)
2. [Reading guide](#2-reading-guide)
3. [Questions while reading](#3-questions-while-reading)
4. [Hands-on](#4-hands-on)
5. [Progress](#5-progress)
6. [Explain-back](#6-explain-back)
7. [Logging formats](#7-logging-formats)

---

## 1. Session start

1. 📂 **Read** the rulebook, the note prompt, and the README. Find the **current position** and the last Session Log row.
2. 🔁 **Recall:** ask 3 questions on the material read last time, unless the Session Log already records that recall as done.
    - Make them **apply** the idea, not repeat it: "your script fails with X; why, and how do you check?" beats "what is X?".
    - Include any **Open Questions** marked to re-check.
    - **Write the questions down** in Open Questions as `🔁 Recall pending (asked {date}): 1. … 2. … 3. …`. If the learner doesn't answer this session, the next session asks the same ones. Remove the item once the answers are logged.
3. 🗺️ **Preview**, when a new chapter starts. Keep it to one screen:
    - the question the chapter answers;
    - the commands, terms or ideas it introduces, and which ones the learner already uses;
    - why it matters for their goal;
    - the **reading guide**;
    - one small thing to try while reading.

If the learner jumps straight in with a question, answer it first, then add the recall questions at the end of your reply.

**When recall answers arrive:** say what's right, correct what isn't (and why), then log it in the Session Log. Add each wrong or unsure point to **Open Questions** with "🔁 re-check at next recall".

---

## 2. Reading guide

Give a **full** guide every time you preview a chapter, and whenever the learner asks what to read. After a progress report, a short **next up** is enough: the next 1–3 sections, with the same marks and pages. Take both from the README plan.

A full guide lists every section of the stretch to read:

```markdown
| Mark | Pages | Section | Why |
|---|---|---|---|
| 📖 Read | 51–52 [PDF 82–83] | Plaintext vs. binary files | What decides whether a file runs |
| 👀 Skim | 54–58 [PDF 85–89] | `ls`, `cd`, `cp`, `mv`, `rm` | You use these daily. Glance at `ls -l` columns only |
| ⏭️ Skip | 71–78 [PDF 102–109] | nano and Vim basics | Covered in your Vim notes |
```

- 📖 **Read**: counted in the plan. 👀 **Skim**: not counted. ⏭️ **Skip**: not read, so not counted.
- For web sources, use section titles with links instead of pages.
- End with what comes after the chapter: any comparison-source add-ons, or the practice track's next step.

Mirror the same marks in the README's **Current Chapter** checklist, so the tracker and the guide agree.

---

## 3. Questions while reading

When the learner quotes a passage or asks about the text, the text didn't work for them.

1. 💬 **Answer it fully.** Start from the idea, then a concrete example in their world. Correct the source if it's wrong.
2. 📝 **Log it right away** in the README's **📝 Questions While Reading** table, before the session can end:

   ```markdown
   | ⬜ | 5 | 61 | How do I try the symlink example? | `ln -s TARGET LINK`; a relative target resolves from the link's directory, so the book's example is broken … |
   ```

   - **Page:** the page where the passage is.
   - **Short answer:** 1–3 specific sentences, enough to write the note from, including any source errors you found. The full explanation lives in your reply. The row is a reminder of it, not a copy.
3. 🔗 **Follow-ups go into the same row.** If the learner asks "so it's because…?", add that detail to the existing row instead of a new one.
4. ✅ **Later, when the chapter note is written,** each row's answer appears in the matching section and in the Q&A. The handbook merge carries it over. Then change ⬜ to ✅.

A question you can't answer yet, or one for a later chapter, goes to **❓ Open Questions** instead.

---

## 4. Hands-on

When the learner asks "how can I try this?", or the topic is practical:

1. 🧪 **Pick a safe playground:** a scratch directory such as `~/<source>-lab/ch5`, a VM, or a container. Never the learner's real data or production servers.
    - Check the filesystem first with `df -T .`. Experiments with permissions, links, or inodes give misleading results on NTFS, exFAT, or FUSE mounts, which are common on dual-boot machines. Use a native Linux folder such as `/tmp` or the home directory instead.
2. ▶️ **Run it yourself first** if you can run commands. Show the **real output**. If the source's example doesn't work, show that and explain why. That's often the best lesson in the session.
3. 📋 **Give numbered steps:** what we're doing, the command, the output to expect, and what it shows.
4. ⚠️ **Mark destructive commands** (`rm -r`, `dd of=`, `mkfs`, `chmod -R`, editing system config) with a warning and how to undo them. Prefer read-only exploration.
5. 🧹 **End with cleanup** when the steps created something.

When the learner pastes output that surprises them, explain what happened step by step. The surprise usually points to a concept from an earlier chapter. Name it.

---

## 5. Progress

When the learner says how far they read, update **all** of these in the README:

| Field | How |
|---|---|
| **Plan bar** | Planned pages read so far ÷ total planned pages. Count 📖 and ✂️ pages only, never 👀 skimmed or ⏭️ skipped pages |
| **Whole-source bar** | All pages the learner went through, read or skimmed, ÷ total readable pages |
| **Chapter bar** | Planned pages read in this chapter ÷ planned pages in it |
| **Chapters table** | That chapter's `<progress>` and `read/total` |
| **Section checkboxes** | Tick every section finished. A parent line stands for its own intro text, so tick it once that's read; its children are ticked separately. If the learner's report splits a combined line ("Hard links · The `file` command"), split it into two lines |
| **Goal checklists** | Tick **What to Learn** and **Practice track** items that are now done |
| **Knowledge map** | 📖 → 🟡 once the topic is read. 🟡 → ✅ once explain-back for it went well |
| **Current position** | Chapter, section, and page where they'll start next time |
| **Session Log** | One new row (see below) |

**Counting rules:**
- "Read till section X" means every page **before** X's first page is done.
- A page counts once **everything planned on it** has been read. If a page is shared with a section the learner hasn't reached yet, count it when they finish that section.
- If the report is ambiguous (they mention one of two sections on the same line or page), count conservatively and ask in one line.
- Round percentages to whole numbers.

Use the README's existing bar format. In a new README, write `<progress value="52" max="174"></progress> \`52 / 174 planned pages · 30%\``.

When the chapter is **finished**, go to explain-back.

---

## 6. Explain-back

When a chapter is done, ask 3 questions that make the learner explain its core ideas **in their own words**. Prefer "why" and "what would happen if" questions. Each one should check a different main idea.

When the answers arrive:

1. ✅ **Say what's right**, specifically.
2. 🔧 **Correct what's wrong or missing.** Give the reason and a small example. Explain any surprise they had during the chapter.
3. 📝 **Log** the explain-back in the Session Log.
4. ✍️ **Write the chapter note** ([note-style.md](note-style.md)). The learner's confusions from explain-back join the Q&A.
5. 📘 **Merge into the handbook**, if enabled ([handbook.md](handbook.md)).
6. 📊 **Update the README:** the note link in the Chapters table, ✅ on its questions, the knowledge map, the new current chapter checklist with 📖 / 👀 / ⏭️ marks, and the Session Log.

---

## 7. Logging formats

**Session Log row:**

```markdown
| 7 | 2026-11-19 | Skimmed pp. 54–59, read p. 60. Questions (logged): block devices, symlinks (book's example broken). Recall on pp. 51–54 asked, not answered yet | Recall on pp. 51–54, then 📖 read from p. 61 |
```

- **Columns:** number, date, what was covered (reading, questions, recall and explain-back results with corrections, rule changes), and what's next.
- Use **today's actual date**. Start a **new row for each new day**, or when the learner says it's a new session. Later work on the same day goes into that day's row, and its **Next** column is updated.
- Keep **Covered** to about 3 sentences. Name the questions; their answers live in the Questions While Reading table.

**Open Questions item:**

```markdown
- 🔁 Re-check at next recall: which setting makes a leading-space command skip history? (You were unsure in session 5.)
```

**Rule changes:** when the learner says "always…" or "from now on…", write the rule into the rulebook's study loop and into the study folder's `AGENTS.md`, if there is one. Then confirm it in one line.
