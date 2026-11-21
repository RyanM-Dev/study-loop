<!--
Template: the handbook prompt. Save as `<Topic> Handbook/AI Prompt - {{TOPIC}} Handbook.md`.
Fill in the curriculum and placement rules. Delete this comment.
-->
# {{TOPIC}} Handbook — Maintenance and Note Prompt

> **Purpose:** Keep **one unified {{TOPIC}} reference** in this folder. It merges every {{TOPIC}} concept the learner has studied, from any source, into numbered notes ordered from beginner to advanced.
>
> **Style:** the same as the chapter notes: [[{{NOTE_PROMPT_LINK}}|AI Prompt - {{SHORT}} notes]].

---

## 🎯 What the Handbook Is

- 📘 **The one place to learn and review {{TOPIC}}.** Source notes stay where they are, as records of each source. The handbook is the merged, cleaned-up version.
- ✅ **Only studied concepts get content.** A topic not studied yet stays in the index as 📖 *planned*, with no note.
- 🧭 **Beginner → advanced.** The order is fixed in [[{{HANDBOOK_INDEX_LINK}}|the index]]. Every note builds only on the notes before it.

---

## 🗂️ Fixed Curriculum

Numbers never change. A new topic goes into the existing note it belongs to, as a new section, or into its reserved number. Never renumber.

| # | Note | Part |
|---|---|---|
| 1 | {{NOTE_TITLE}} | {{PART_EMOJI}} {{PART_NAME}} |

**Where a concept goes when it's unclear:**

- {{CONCEPT}} → **{{N}}**. {{RELATED_CONCEPT}} stays in **{{M}}**.

---

## 📝 Note Template and Rules

Follow the study-loop skill's `references/handbook.md`: note template, References table with status hints, merging rules, and the update workflow. In short:

1. 🔎 List the new concepts, including logged questions.
2. 🗂️ Find each concept's note with the curriculum above.
3. ✍️ Merge: one explanation per concept, in learning order. Create planned notes from the template.
4. 📚 Update the References table, then fix "🔜 Later" lines and 📖 planned rows elsewhere.
5. 🧭 Update the index status, "merged from", and **Last updated**.
6. 🗺️ Update the study README's knowledge map.
7. 📘 Add a `📘 Merged into` line to the source note.
8. ✅ Check links, Mermaid, and ⬅️ ➡️ navigation.

Size: roughly 250–450 lines per note. Past ~600, split into `{N}a. …`.
