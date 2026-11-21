# 🌐 Faithful Translation

Sometimes the learner wants a passage, a section, or a whole chapter in their own language. Persian is the case this module was written for, but the rules apply to any language.

**The main rule: a translation keeps the source's own voice.** Learners ask for a translation because they want to hear **the author**, in their language: the way the author builds an argument, tells a story, jokes, warns, and walks the reader from one idea to the next. A translation that "improves" the text by summarising, bulleting, simplifying, or modernising it has failed, even if every fact survives.

This is the opposite of the note style. Notes restructure and teach in our own words. **Translations don't restructure anything.**

## Contents

1. [What to keep](#what-to-keep)
2. [What not to do](#what-not-to-do)
3. [Faithful, not literal](#faithful-not-literal)
4. [Technical terms](#technical-terms)
5. [Persian specifics](#persian-specifics)
6. [Figures and footnotes](#figures-and-footnotes)
7. [Where translations go](#where-translations-go)
8. [Self-check](#self-check)

---

## What to keep

- 🎭 **The voice and register.** Formal stays formal, chatty stays chatty, dry humour stays dry. Keep how the author addresses the reader ("you", "we", "let's"). Keep their rhetorical questions, asides, and parenthetical remarks.
- 📖 **The storytelling.** Keep the order the author reveals things in: the setup, the example, the payoff, the "but wait" twist. If a paragraph opens with an anecdote and gets to the point at the end, so does the translation.
- 🧱 **The structure.** Every paragraph stays one paragraph, in the same order. Headings keep their level. Lists stay lists and prose stays prose. Emphasis (bold, italics) stays on the same words.
- 🖼️ **Examples and metaphors.** Translate each image so it means the same thing. If a metaphor really doesn't work in the target language, find the closest one that does, and add a translator's note giving the original.
- 🧮 **Everything literal**, untouched: code, commands, output, paths, URLs, identifiers, numbers in code, and quoted program text.
- 📏 **Length and rhythm.** Roughly match sentence length and paragraph weight. A short, punchy line stays short and punchy. A long winding sentence may be split only if the target language truly needs it, and the rhythm should survive.

---

## What not to do

- ❌ Summarise, shorten, or skip "obvious" sentences.
- ❌ Turn prose into bullet points or tables, or add headings that aren't in the source.
- ❌ Add explanations inside the text. Explanations go into clearly marked translator's notes, kept to a minimum.
- ❌ Silently correct the author. If the source is wrong or outdated, translate what it says and add a translator's note.
- ❌ Soften or sharpen the tone. Don't add politeness the author didn't use, and don't drop the author's opinions.
- ❌ Insert emojis, callouts, or note-style formatting.

**Translator's notes:** mark each one clearly and put it in a footnote at the end of the passage, never mid-paragraph: `[^t1]` → `[^t1]: یادداشت مترجم: …`.

---

## Faithful, not literal

Faithful means faithful to **meaning, voice, and structure**, not word order. A word-for-word calque (copying the source language's sentence structure) sounds foreign and can lose the voice just as surely as a summary does. Write the sentence a native writer with the author's personality would write in the target language.

- **Idioms:** use the target language's equivalent idiom, not a literal one.
- **Sentence order:** reorder within a sentence when the grammar needs it. Don't reorder across sentences.
- **Ambiguity:** keep the author's ambiguity when it's deliberate. When it's accidental, choose the most likely reading, and add a note if the choice matters.

---

## Technical terms

- **Established term:** if the target language has one that practitioners actually use, use it: «پایگاه داده».
- **Naturalised loanword:** if practitioners write the English word in the target script, do the same: «فایل»، «سرور»، «کلاینت».
- **Kept in Latin script:** only terms practitioners really write in Latin, such as `check out`, product names, and command names.
- **First use in a passage:** give the English in parentheses after the translated term, in body text, not in a heading: «سیستم فایل (filesystem)». For an acronym: «سیستم کنترل نسخه (Version Control System یا VCS)». Inside the author's own parentheses, use square brackets: «[time-stamped]». Don't gloss everyday loanwords like «فایل». After the first use, keep to one form.
- **Glossary:** keep a short `Translation Glossary.md` in the study folder, as a table of `English | Translation | Note`, with a **Conventions** line at the top (digits, punctuation, ZWNJ rules). Reuse it so the same term is translated the same way in every chapter, and add to it whenever you make a new choice.

---

## Persian specifics

- 🔤 **Letters:** use Persian «ی» and «ک», never Arabic «ي» and «ك». Keyboards and copy-paste mix them up often.
- ✍️ **Punctuation:** use Persian punctuation in Persian prose: «،» «؛» «؟» and guillemets «…» for quotations. Leave code and English terms as they are.
- 🔗 **Half-space (ZWNJ, نیم‌فاصله):** use it where Persian orthography needs it: می‌شود، فایل‌ها، کتاب‌های، خانه‌ای. Also put one between a Latin word and a Persian suffix: VCS‌ها. Don't use a full space (می شود), and don't join the parts (میشود).
- 🔢 **Digits:** ask the learner once and record it in the rulebook. The default for technical sources is **Latin digits** (1, 2, 3), so they match the code, page numbers, and output. Never change digits inside code, commands, or quoted output.
- ↔️ **Direction:** write normal Markdown paragraphs. Code blocks, commands and paths stay as code, so they render left-to-right.
    - **Start each paragraph with a Persian word.** When direction is detected automatically, a paragraph that opens with a Latin word (`RCS یک ابزار …`) renders left-to-right. Reorder the sentence slightly: «ابزار RCS …».
    - **Obsidian:** if Persian paragraphs show left-aligned, turn on the editor's right-to-left setting, or use an RTL plugin, rather than wrapping text in HTML. Markdown inside HTML blocks often doesn't render in Obsidian.
    - **GitHub:** wrap the translation in `<div dir="rtl">` … `</div>`, with blank lines inside so the Markdown still renders.
- 🎚️ **Register:** match the author. A conversational English author usually maps to a natural, standard written Persian with a conversational warmth (نوشتار معیار, not محاوره‌ای slang), unless the source itself uses slang. A formal author maps to formal Persian.
- 👤 **Addressing the reader:** keep the author's choice. "You" usually becomes «شما». Keep the inclusive «ما» ("we") where the author uses it.

---

## Figures and footnotes

- 🖼️ **Images:** keep the image URL or path exactly. Translate the alt text and the caption, and keep the figure number: «شکل 1. …».
- 📝 **Translator's notes** go at the **end of the file**, numbered `[^t1]`, `[^t2]`, … across the whole file. Keep the source's own footnotes as they are, translated, with their original numbering.

---

## Where translations go

- **File:** save each translation as its own file beside the chapter note: `{N}. {Chapter Title} - {lang}.md`, e.g. `5. Introducing Files - fa.md`. If there's no study folder yet, save it in the current folder, put the glossary beside it, and record the digit choice in the glossary's Conventions line. When a study is set up later, move both in.
- **Header:** start the file with a short header, ending in a `---` line:
    - the source, chapter, and pages (or the URL with section anchors for web sources);
    - a link to the chapter note, written as plain text if the note doesn't exist yet;
    - what was left out, if you translated only part of a section.
- **Scope:** translate **only what the learner asks for**, usually the passages they're studying. It's for their personal study.
- **Licences:**
    - Don't put translations of copyrighted books in public repositories.
    - For openly licensed sources (Creative Commons and similar), add the attribution and licence the source asks for, such as `CC BY-NC-SA 3.0, same licence for this translation`.
- **Translating notes:** if the learner asks for their **notes** (not the source) in another language, translate the note faithfully in the same way. Keep its structure, emojis, callouts and code exactly. Only the prose changes language.

---

## Self-check

1. **Save the source text** you translated into a scratch directory, in the same Markdown layout (headings, paragraphs, lists, code), and put the translation's header in it too.
2. **Run the mechanical check:**

   ```bash
   python3 scripts/check_translation.py "5. Introducing Files - fa.md" --source /tmp/<scratch>/source.md --lang fa
   ```

   It compares the block structure, code, and URLs. For Persian, it also catches Arabic «ي/ك», mixed digits, ASCII punctuation, missing half-spaces, and paragraphs that start with a Latin word. Fix everything it reports.
3. **Read** the source and the translation side by side, paragraph by paragraph:

- [ ] Same number of paragraphs, in the same order. Headings and lists match.
- [ ] Nothing summarised, skipped, or added, apart from marked translator's notes.
- [ ] The author's jokes, asides, questions and warnings are all there, in their voice.
- [ ] Code, commands, paths and output are byte-for-byte unchanged.
- [ ] Terms match the glossary. First uses show the English original.
- [ ] (Persian) Persian «ی/ک», correct ZWNJ, Persian punctuation, the agreed digits, and every paragraph starts with a Persian word.
- [ ] Read aloud, it sounds like a native writer, not a calque.
