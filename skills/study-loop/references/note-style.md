# 📝 Note Style: Chapter Reference Notes

A chapter note is what the learner rereads in six months, so it has to teach on its own, without the book and without the chat. It is built from **the source and the study session**. The learner's questions and mistakes are what make it theirs.

The study folder's note prompt (`AI Prompt - {Short} notes.md`) can override any of this.

## Contents

1. [Inputs](#inputs)
2. [Teaching order and section pattern](#teaching-order-and-section-pattern)
3. [Visual readability](#visual-readability)
4. [Writing](#writing)
5. [Commands, code, and diagrams](#commands-code-and-diagrams)
6. [Q&A and practice](#qa-and-practice)
7. [Note skeleton](#note-skeleton)
8. [Plain-Markdown format](#plain-markdown-format)
9. [Final pass](#final-pass)

---

## Inputs

Before writing, collect:
- the chapter's text, re-extracted for the pages read (only the planned pages);
- the README's **📝 Questions While Reading** rows for the chapter, each of which **must** appear twice: a summary in its section and a Q&A entry;
- the Session Log rows for the chapter: explain-back corrections, surprises, and hands-on output;
- the learner profile, for the examples.

---

## Teaching order and section pattern

Teach in this order: **simple explanation → practical example → how it works → necessary details**. Add advanced material only when the chapter or the learner needs it. Follow the source's section order unless a different order is clearly easier to learn from.

A typical section:

1. **Explain directly.** 1–3 short sentences: what it is and why we use it.
2. **Make it concrete.** One example, command, path, or configuration from the learner's world.
3. **Show the relationship.** A Mermaid diagram when it makes the idea easier to see.
4. **Explain the result.** What happens, or what to notice.

This is a pattern, not four subheadings. Start with the first useful concept after the header, with no long introduction or list of learning objectives.

Use `> 💡 **Real-World Example**` callouts for scenarios worth emphasising, but not in every section. Mark outside material `🔭 Beyond the source`, keeping it to 1–2 per section.

---

## Visual readability

- 🗂️ **Descriptive emoji headings** for the main concepts. Use `---` between major topics.
- 🪜 **Group details under their main point:** a short parent bullet with indented children (4 spaces). Keep to one level of nesting.
- 🔢 **Ordered steps for actions,** with each step's code and explanation indented under it.
- ↕️ **Generous spacing:** a blank line between paragraphs, list items, steps, and around headings, code, diagrams, tables, and callouts. Inside callouts, use a line containing only `>`.
- 😀 **Meaningful emojis as landmarks:** 📁 paths, 💻 commands, 🔎 checks, ✅ expected results, 💡 tips, ⚠️ warnings, 🔐 security. Keep them out of code and don't decorate every line.
- **Bold** short key terms. Use `inline code` for commands, flags, paths, and values.
- Use a small table plus a sentence of prose for comparisons, including only the differences that matter.

---

## Writing

- Use familiar words, active voice, and paragraphs of 1–3 sentences. Explain each idea once, and let the example or diagram carry the detail.
- Define jargon where it first appears.
- Keep warnings next to the instruction they affect, in one sentence.
- **Correct source errors silently:** write the correct version, without "the book says…".
- Explain in your own words. Don't copy passages from the source.
- **Size:** match the chapter. Usually 150–350 lines; a 5-page chapter stays small. Split a long chapter into `- Part 1`, `- Part 2` rather than growing one note past ~450 lines.
- Never claim you ran an example unless you did. Real output from the session's hands-on is welcome; label it as from the session.

---

## Commands, code, and diagrams

- **Commands:**
    - Say what we want to do.
    - Show the command.
    - Explain the flags and arguments that matter.
    - Say what to expect, and how to check it.
    - Show sample output only when reading it teaches something.
- **Code and config:** give the filename and where it runs, then explain the important lines. Use language-tagged code blocks and clear placeholders.
- **Safety:** add a `> ⚠️` line beside anything destructive, with how to undo it.
- **Diagrams:** use fenced `mermaid` blocks. Flowcharts for flows and hierarchies, `sequenceDiagram` for exchanges, `stateDiagram-v2` for lifecycles. Label arrows. Explain the takeaway in a sentence or two instead of narrating every box.
- **Calculations:** show the steps, with units.

---

## Q&A and practice

**🧪 Q&A:** one block near the end of a short note, or one per major topic group in a long one. Use 3–5 questions per block. Cover understanding, practical choices, reading output, and likely failures, and include **every** logged question for the chapter. List the questions first, then put all the answers in one collapsed callout:

```markdown
### 🧪 Q&A

**Q1:** Why does `ls /dev | grep nvme*` fail in zsh?

**Q2:** …

> [!answer]- 📋 Answers
>
> **A1:** The shell expands `nvme*` as a glob before grep runs. Nothing in the current directory matches, so zsh stops. Quote patterns meant for the program: `grep 'nvme'`.
>
> **A2:** …
```

**🔨 Hands-On Practice:** a few short, safe exercises in numbered steps, with the command indented under each step and a ✅ expected result. Reuse the session's hands-on where it worked well. Mention cleanup when needed.

---

## Note skeleton

```markdown
# {emoji} {Chapter Title}

[[{study folder}/README|{icon} {Short}]] · Ch.{N} · pp. {printed range}

📘 Merged into: [[{Topic} Handbook/{N}. {Title}|{N}. {Title}]]    ← only with the handbook module

> [!toc]- 📑 Contents
>
> - [[#{Heading 1}]]
> - …

{One or two sentences: the question this chapter answers.}

---

## {emoji} {Concept}
…

### 🧪 Q&A
## 🔨 Hands-On Practice
## 📋 Quick Reference          ← small table of the most useful commands or relationships
## 🧠 Things to Remember       ← 4–6 essential facts
## 💡 Pro Tips                 ← 3–4 practical tips, each with a reason
## 🔗 Related Topics           ← previous and next chapter, the handbook note, related notes
```

When the next chapter's note doesn't exist yet, write its name as plain code (`` `5. Introducing Files` ``). Turn it into a link once the note exists.

---

## Plain-Markdown format

Use this when the rulebook says `Format: plain Markdown`:

| Obsidian | Plain Markdown |
|---|---|
| `[[Folder/Note\|Text]]` | `[Text](Folder/Note.md)`, URL-encoding spaces as `%20` |
| `[[#Heading]]` | `[Heading](#heading-slug)` |
| `> [!answer]- 📋 Answers` | `<details><summary>📋 Answers</summary>` … `</details>`, with blank lines inside |
| `> [!toc]-` contents callout | Leave it out. GitHub shows its own outline, and headings that start with an emoji make fragile anchors |
| `> 💡 **Real-World Example**` | The same blockquote. It renders fine |
| `<progress>` bars in the README | Keep them. GitHub hides the bar but shows the `52 / 174` text next to it |

Mermaid works in both.

---

## Final pass

Before saving, check:
- every logged question is answered in its section **and** in the Q&A;
- there are no repeated explanations, padding, or "as mentioned above";
- the indentation renders, with no prose accidentally indented into a code block;
- links point to notes that exist, and Mermaid blocks are valid;
- no long passages were copied from the source.

Save the finished Markdown only, with no preamble.
