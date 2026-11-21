<!--
Template: the note prompt. Save as `AI Prompt - {{SHORT}} notes.md` in the study folder.
Write the style from the skill's references/note-style.md into the "Style" section, keeping
only the chosen format (Obsidian or plain Markdown), so this file works even without the skill
installed. Then add source-specific rules below. Without comparison sources, rename the chapter
map's "Enrichment" column to "🔭 Beyond the source".
Delete this comment.
-->
# {{SOURCE_TITLE}} — Chapter Notes Prompt

> **Purpose:** Turn a chapter of *{{SOURCE_TITLE}}* and our study session into a clear, practical reference note.
>
> **Study process:** [[{{RULEBOOK_LINK}}|AI Prompt - {{SHORT}}]]. This file covers only how notes look.
>
> **Format:** {{FORMAT}}

---

## 🎨 Style

{{COPY OF references/note-style.md: teaching order, section pattern, visual readability, writing, commands and diagrams, Q&A and practice, skeleton, final pass. Keep only the format variant the rulebook names}}

---

## 👤 Reader

{{ROLE_ONE_LINE}} Skip the basics they already have, and explain the mechanism under what they already use.

Use their world for examples: {{BRIDGES}}.

---

## 🧷 Source-specific rules

- **Ideas to preserve** from this source: {{KEY_IDEAS_OR_MENTAL_MODELS}}.
- **Disagreements:** when sources differ, give the modern recommendation in one sentence. Add a small table only if the difference matters.
- **Out of scope:** {{TOPICS_NOT_TO_ADD}}.
- **Safety:** {{DOMAIN_SAFETY_RULES}}, e.g. a `> ⚠️` line beside destructive commands, with how to undo them.
- **Q&A focus:** {{LIKELY_CONFUSIONS}}, plus every question logged in the README's Questions While Reading table.

---

## 🗺️ Chapter map

| Ch | Title | Pages | Useful diagram | Enrichment, if needed |
|---|---|---|---|---|
| 1 | {{CH1_TITLE}} | {{CH1_PAGES}} | {{DIAGRAM_IDEA}} | {{COMPARISON_REF}} |

Diagrams are suggestions: draw one only when it makes the concept easier.

---

## 📝 Note conventions

- **Filename:** `{N}. {Chapter Title}.md`. Archive an older note as `{N}.OLD-{Title}.md` before replacing it.
- **Header:** `[[{{README_LINK}}|{{ICON}} {{SHORT}}]] · Ch.{N} · pp. {printed range}`, then one or two sentences on what the chapter answers.
- **Collapsed answers:** {{ANSWER_BLOCK_STYLE}}, e.g. `> [!answer]- 📋 Answers` in Obsidian, or `<details>` in plain Markdown.
- **Related Topics:** the previous and next chapter, plus existing related notes: {{RELATED_NOTES}}.
- **Size:** scale to the chapter, usually 150–350 lines.
