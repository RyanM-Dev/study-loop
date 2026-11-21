# 📚 Sources: PDFs, Web Pages, Videos, and Offsets

## Contents

1. [Source roles](#source-roles)
2. [PDF books](#pdf-books)
3. [EPUB and other formats](#epub-and-other-formats)
4. [Web sources](#web-sources)
5. [Video courses](#video-courses)
6. [Progress units](#progress-units)

---

## Source roles

| Role | Use |
|---|---|
| **Primary** | The ground truth. Its chapter order, terms and examples lead. Progress is tracked against it |
| **Comparison** | Enrichment only: an extra detail, a better diagram, an exercise. Placed **beside** the primary chapter it extends, never as parallel "parts" |
| **The study sessions** | The learner's explanations, questions, and mistakes. Notes are built from these too |
| **Official docs** | For checking facts and "🔭 Beyond the source" examples |

When sources disagree, give the modern, correct answer in one sentence. Add a small table only if the difference matters in practice.

---

## PDF books

**Outline and offset:** run the bundled script first.

```bash
python3 scripts/pdf_outline.py book.pdf            # chapters and sections, PDF pages, offset
python3 scripts/pdf_outline.py book.pdf --depth 1  # chapters only
python3 scripts/pdf_outline.py book.pdf --json     # machine-readable
```

- It uses PyMuPDF if it's installed. Otherwise it falls back to `mutool` and `pdftotext` (poppler-utils).
- **Offset:** `PDF page = printed page + offset`. The script finds it by looking for printed page numbers in page headers and footers. Spot-check two pages yourself. Record the offset in the rulebook and the README.
- Some books (often big reference books) restart or shift the offset per chapter. Then record it **per chapter**, or give PDF pages explicitly beside every reference: `pp. 289–298 [PDF 319–328]`.

**Extracting text** for a section you're about to discuss or write up:

```bash
pdftotext -layout -f <pdf first> -l <pdf last> book.pdf - > /tmp/<scratch>/ch5.txt
```

- Put extracted text in a scratch or temp directory, never in the notes folder or the learner's repo.
- Re-extract when writing the note. Don't trust your memory of the chapter.
- **Scanned PDFs** with no text layer need OCR (`ocrmypdf`). Ask the learner before installing anything.

**Readable pages:** leave out the cover, front matter, blank pages, "other books by this publisher", and the index. Count per chapter: printed first page → printed last page, minus blanks.

**Learner page numbers:** learners often give the PDF page from their viewer. If a number looks off by the offset, ask which one they mean, or convert and say so.

---

## EPUB and other formats

- **EPUB** has no fixed pages. Convert to text or PDF if a tool exists (`pandoc book.epub -t plain`, or Calibre's `ebook-convert`). Otherwise track progress by **sections** using the EPUB's table of contents.
- **Slides or papers:** treat them as a PDF. Usually one "chapter" per paper or deck.

---

## Web sources

Documentation sites, online books, blog series, tutorials.

1. 🧭 **Map it.** Fetch the start page and its navigation or table of contents. List every chapter and section with its **URL** in the README's Chapters table. For sites with no navigation, follow "next" links, or ask the learner which pages are in scope.
2. 📏 **Size it.** Estimate each section's length from its word count: one "page" ≈ 400 words (about 1.5 minutes of reading).
    - Round per **chapter**, not per section, so a 60-word summary doesn't become a whole page. Show section sizes to the nearest half page (`~0.5 p`).
    - Keep the estimates in a collapsed table in the README (`<details>` in plain Markdown, `> [!note]-` in Obsidian): section, link, estimated pages, plan mark. Progress is counted from it.
    - A ✂️ partly planned section counts only its planned subsections.
3. 🔗 **Reference it.** In reading guides and notes, link the exact page, plus an anchor when there is one (`…/git-branching#_basic_branching`). Record the date you mapped the site, because docs change: `Mapped: 2026-11-19`.
4. 🧾 **Versions.** If the docs are versioned, record the version the learner uses (`Docs for v1.31`). Read that version's pages, not "latest".
5. 📥 **Fetching.** Use whatever web tool you have: a fetch tool, a browser, or `curl`. Keep fetched text in a scratch directory. If a page needs a login, ask the learner to paste the text or export it.

The learner may start from a single link. Find out whether it's one article or the entry point of a series, then confirm the scope with them.

---

## Video courses

- List modules and lessons with their **lengths** (from the course page or the files' metadata, e.g. `ffprobe`).
- The progress unit is **lessons** or **minutes**.
- The learner's own rough notes, or transcripts if available, take the place of the text. Notes are built from those plus the session.
- Questions while watching get logged with a **timestamp** instead of a page: `Ep 106 @ 12:30`.

---

## Progress units

| Source | Unit | Shown as |
|---|---|---|
| PDF / printed book | Printed pages | `pp. 51–53 [PDF 82–84]` |
| EPUB | Sections | `§ 5.2–5.4` |
| Web docs | Sections, or estimated pages | Section title with a link, `~3 pages` |
| Video | Lessons or minutes | `Ep 12–14 (38 min)` |

Use one unit per study, and say which one in the README's Progress section. Mixing units makes the bars meaningless.
