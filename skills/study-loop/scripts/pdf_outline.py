#!/usr/bin/env python3
"""Print a PDF's outline with PDF and printed pages, the printed-page offset,
and readable pages per chapter. Used by the study-loop skill during setup.

    python3 pdf_outline.py book.pdf             # full outline
    python3 pdf_outline.py book.pdf --depth 1   # chapters only
    python3 pdf_outline.py book.pdf --json      # machine-readable

Backends: PyMuPDF (`pip install pymupdf`) if available, otherwise `mutool` for
the outline and `pdftotext` (poppler-utils) for page text.
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import shutil
import subprocess
import sys

BLANK_CHARS = 80  # pages with less text than this count as blank / not readable


# ---------- backends ----------

def load_fitz(path):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    doc = fitz.open(path)
    toc = [(lvl, title.strip(), page) for lvl, title, page in doc.get_toc(simple=True)]
    return {
        "page_count": doc.page_count,
        "toc": toc,
        "text": lambda p: doc[p - 1].get_text() if 1 <= p <= doc.page_count else "",
    }


def load_cli(path):
    if not shutil.which("pdftotext"):
        sys.exit("Need PyMuPDF (pip install pymupdf) or poppler-utils (pdftotext).")
    page_count = 0
    if shutil.which("pdfinfo"):
        info = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
        m = re.search(r"^Pages:\s+(\d+)", info, re.M)
        page_count = int(m.group(1)) if m else 0
    toc = []
    named = False
    if shutil.which("mutool"):
        out = subprocess.run(["mutool", "show", path, "outline"],
                             capture_output=True, text=True).stdout
        for line in out.splitlines():
            m = re.match(r'^([\s|+\-]*)"(.*)"\s+#(?:page=(\d+)|nameddest=\S*?(\d+))', line)
            if not m:
                continue
            level = m.group(1).count("\t") or 1
            page = int(m.group(3) or m.group(4) or 0)
            named = named or m.group(3) is None
            toc.append((level, m.group(2).strip(), page))
    cache = {}

    def text(p):
        if p not in cache:
            cache[p] = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), path, "-"],
                                      capture_output=True, text=True).stdout
        return cache[p]

    return {"page_count": page_count, "toc": toc, "text": text, "approx": True,
            "named_dests": named}


# ---------- analysis ----------

def detect_offset(doc, samples=40):
    """Find PDF page minus printed page by reading numbers in headers/footers."""
    n = doc["page_count"]
    if n < 10:
        return None, 0
    start, end = int(n * 0.15), int(n * 0.85)
    step = max(1, (end - start) // samples)
    votes = collections.Counter()
    for p in range(start, end, step):
        lines = [l.strip() for l in doc["text"](p).splitlines() if l.strip()]
        for cand in lines[:3] + lines[-3:]:
            if re.fullmatch(r"\d{1,4}", cand):
                printed = int(cand)
                if 0 < printed <= p:
                    votes[p - printed] += 1
    if not votes:
        return None, 0
    offset, count = votes.most_common(1)[0]
    return offset, count / max(1, sum(votes.values()))


def readable(doc, first, last):
    return sum(1 for p in range(first, last + 1)
               if len(doc["text"](p).strip()) >= BLANK_CHARS)


def build(path, depth):
    doc = load_fitz(path) or load_cli(path)
    offset, confidence = detect_offset(doc)
    toc = doc["toc"]
    chapters = []
    top = [i for i, e in enumerate(toc) if e[0] == 1]
    for k, i in enumerate(top):
        lvl, title, first = toc[i]
        nxt = toc[top[k + 1]][2] if k + 1 < len(top) else doc["page_count"] + 1
        last = max(first, nxt - 1)
        sections = [
            {"level": l, "title": t, "pdf": p,
             "printed": (p - offset) if offset is not None and p else None}
            for (l, t, p) in toc[i + 1:(top[k + 1] if k + 1 < len(top) else len(toc))]
            if l <= depth
        ]
        chapters.append({
            "title": title, "pdf_first": first, "pdf_last": last,
            "printed_first": (first - offset) if offset is not None else None,
            "printed_last": (last - offset) if offset is not None else None,
            "readable_pages": readable(doc, first, last) if first else None,
            "sections": sections,
        })
    return {
        "file": path, "pdf_pages": doc["page_count"],
        "offset": offset, "offset_confidence": round(confidence, 2),
        "backend": "cli" if doc.get("approx") else "pymupdf",
        "pages_approximate": bool(doc.get("named_dests")),
        "chapters": chapters,
    }


def show(result):
    off = result["offset"]
    print(f"File: {result['file']}  ({result['pdf_pages']} PDF pages, backend: {result['backend']})")
    if off is None:
        print("Offset: not detected. Check printed page numbers by hand.")
    else:
        print(f"Offset: PDF page = printed page + {off}  "
              f"(confidence {int(result['offset_confidence'] * 100)}%: spot-check two pages)")
    if result.get("pages_approximate"):
        print("⚠️  Outline pages come from named destinations and may be off by a few pages. "
              "Install PyMuPDF (pip install pymupdf) for exact pages, or check with pdftotext.")
    print()
    print(f"{'Printed':>11}  {'PDF':>9}  {'Read':>4}  Title")
    for ch in result["chapters"]:
        if ch["printed_first"] is None:
            pr = "?"
        elif ch["printed_last"] < 1:
            pr = "front"
        else:
            pr = f"{max(1, ch['printed_first'])}–{ch['printed_last']}"
        print(f"{pr:>11}  {ch['pdf_first']}–{ch['pdf_last']:<4}  "
              f"{ch['readable_pages'] if ch['readable_pages'] is not None else '?':>4}  {ch['title']}")
        for s in ch["sections"]:
            indent = "    " * (s["level"] - 1)
            p = s["printed"] if s["printed"] is not None and s["printed"] > 0 else "-"
            print(f"{p:>11}  {s['pdf']:>9}        {indent}{s['title']}")
    if not result["chapters"]:
        print("No outline (bookmarks) in this PDF. Build the chapter list from the table of "
              "contents pages, with pdftotext.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--depth", type=int, default=3, help="deepest outline level to show (default 3)")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a table")
    args = ap.parse_args()
    result = build(args.pdf, args.depth)
    if args.json:
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        print()
    else:
        show(result)


if __name__ == "__main__":
    main()
