<!--
Template: the study tracker. Save as `README.md` in the study folder.
Replace every {{PLACEHOLDER}}. Keep a module's block (deleting only its marker lines) when the
module is on; delete the whole block, and its Contents entry, when it's off.
Web sources: replace page numbers and PDF columns with section links and estimated pages
(see references/sources.md). Plain Markdown: convert wikilinks and callouts with the table
in references/note-style.md, and drop the Contents callout. List ⏭️ sections in the
current-chapter checklist without a checkbox. Delete this comment.
-->
# {{ICON}} {{SOURCE_TITLE}}

> {{AUTHORS_OR_PUBLISHER}} · {{CHAPTER_COUNT}} chapters
>
> Studied one chapter at a time. Rules: [[{{RULEBOOK_LINK}}|AI Prompt - {{SHORT}}]] · Note style: [[{{NOTE_PROMPT_LINK}}|AI Prompt - {{SHORT}} notes]]
<!-- module: handbook -->
>
> 📘 **Unified notes:** every concept studied here is merged into the [[{{HANDBOOK_INDEX_LINK}}|{{TOPIC}} Handbook]].
<!-- /module -->
>
> 🎯 **Why this source:** {{GOAL}}

> [!toc]- 📑 Contents
>
> - [[#📊 Progress|📊 Progress]]
> - [[#📖 Current Chapter|📖 Current Chapter]]
> - [[#🗂️ Chapters|🗂️ Chapters]]
<!-- module: goal-plan -->
> - [[#🧭 Knowledge Map|🧭 Knowledge Map]]
> - [[#✅ What You Already Know|✅ What You Already Know]]
> - [[#📖 What to Learn|📖 What to Learn]]
<!-- /module -->
<!-- module: practice -->
> - [[#🔨 Practice Track|🔨 Practice Track]]
<!-- /module -->
<!-- module: goal-plan -->
> - [[#⏭️ Don't Read|⏭️ Don't Read]]
<!-- /module -->
> - [[#📚 Sources and Page Numbers|📚 Sources and Page Numbers]]
> - [[#🗓️ Session Log|🗓️ Session Log]]
> - [[#📝 Questions While Reading|📝 Questions While Reading]]
> - [[#❓ Open Questions|❓ Open Questions]]

---

## 📊 Progress

**Plan:** <progress value="0" max="{{PLANNED_TOTAL}}"></progress> `0 / {{PLANNED_TOTAL}} planned {{UNIT}} · 0%`

**Whole source:** `0 / {{READABLE_TOTAL}} {{UNIT}} · 0%`{{PLAN_SKIPS_NOTE}}

**📍 Current position:** Ch.1, start ({{FIRST_PAGE_REF}})

---

## 📖 Current Chapter

**Ch.1 {{CH1_TITLE}}** · {{CH1_PLAN_MARK}}

<progress value="0" max="{{CH1_PLANNED}}"></progress> `0 / {{CH1_PLANNED}} planned {{UNIT}}`

**Marks:** 📖 Read · 👀 Skim · ⏭️ Skip. Pages are printed pages, with the PDF page in brackets.

- [ ] 📖 {{SECTION}}: p. {{PAGE}} [PDF {{PDF_PAGE}}]
    - [ ] 📖 {{SUBSECTION}}: p. {{PAGE}}
- [ ] 👀 {{SECTION}}: pp. {{PAGES}}. {{WHY_SKIM}}

---

## 🗂️ Chapters

Pages are **printed** pages: add {{OFFSET}} for the PDF page. Progress counts only **planned** {{UNIT}}.

**Plan:** 📖 read · ✂️ only the listed pages · 👀 skim · ⏭️ skip<!-- module: goal-plan --> (reasons in [[#⏭️ Don't Read|Don't Read]])<!-- /module -->

| # | Chapter | Pages | Plan | Progress | Note |
|---|---|---|---|---|---|
| 1 | {{CH1_TITLE}} | {{CH1_PAGES}} | 📖 All | <progress value="0" max="{{CH1_PLANNED}}"></progress> 0/{{CH1_PLANNED}} | |

<!-- module: goal-plan -->
---

## 🧭 Knowledge Map

What {{GOAL_SHORT}} needs from this topic, and where you stand on each part.

**Legend:** ✅ you know it · 🟡 you know a little · 📖 to learn (see [[#📖 What to Learn|What to Learn]])

```mermaid
mindmap
  root(({{TOPIC}} for {{GOAL_SHORT}}))
    {{AREA}}
      ✅ {{KNOWN}}
      🟡 {{PARTIAL}}
      📖 {{TO_LEARN}}
```

---

## ✅ What You Already Know

| Area | What you know | From |
|---|---|---|
| {{AREA}} | {{WHAT}} | {{SOURCE_NOTE_LINK}} |

**🟡 You know a little:**

- {{PARTIAL_TOPIC}}: {{WHERE_FROM}}

---

## 📖 What to Learn

Work from top to bottom. {{SHORT}} is the spine, and comparison-source items sit beside the chapter they extend.

### 🅰️ Stage A: {{STAGE_A_NAME}}

- [ ] **{{SHORT}} Ch.{{N}} {{TITLE}}** · pp. {{PAGES}}
    - {{WHY_IT_MATTERS_FOR_GOAL}}
    - [ ] 🔭 {{COMPARISON_SHORT}} Ch.{{N}} *{{SECTION}}* · pp. {{PAGES}} [PDF {{PDF_PAGES}}]: {{WHAT_IT_ADDS}}

### 🅱️ Stage B: {{STAGE_B_NAME}}

- [ ] {{ITEM}}
<!-- /module -->

<!-- module: practice -->
---

## 🔨 Practice Track

{{PRACTICE_INTRO}} Read in this order, then work through the ladder.

### 📚 Read

1. [ ] **{{SHORT}} Ch.{{N}}** · pp. {{PAGES}}: {{WHAT}}

### 🪜 Practice ladder

Practise in {{PRACTICE_ENV}}.

| # | Exercise | You practise | Goal link |
|---|---|---|---|
| 1 | {{EXERCISE}} | {{SKILLS}} | {{LINK_TO_GOAL}} |
<!-- /module -->

<!-- module: goal-plan -->
---

## ⏭️ Don't Read

- **{{SHORT}}:**
    - Ch.{{N}}: {{REASON}}
<!-- /module -->

---

## 📚 Sources and Page Numbers

| Short | Source | Location | PDF page |
|---|---|---|---|
| **{{SHORT}}** | *{{SOURCE_TITLE}}* | `{{SOURCE_LOCATION}}` | printed + {{OFFSET}} |
<!-- module: comparison -->
| **{{COMPARISON_SHORT}}** | *{{COMPARISON_TITLE}}* | `{{COMPARISON_LOCATION}}` | printed + {{COMPARISON_OFFSET}} |
<!-- /module -->

---

## 🗓️ Session Log

| # | Date | Covered | Next |
|---|---|---|---|
| 0 | {{TODAY}} | Set up the study: sources, plan, tracker | Ch.1 preview, then read from {{FIRST_PAGE_REF}} |

---

## 📝 Questions While Reading

Questions you asked about the text. Each one goes into the chapter note (in its section and in the Q&A)<!-- module: handbook --> and into the handbook<!-- /module -->. Then it gets ticked.

| ✓ | Ch. | Page | Question | Short answer |
|---|---|---|---|---|

---

## ❓ Open Questions

Questions to answer in a later session or chapter, and recall points to check again.

- _(none yet)_
