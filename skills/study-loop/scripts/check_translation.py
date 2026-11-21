#!/usr/bin/env python3
"""Mechanical checks for a faithful translation (study-loop skill).

    python3 check_translation.py translation.md --source source.md [--lang fa]

Compares the translation with the source text block by block (headings,
paragraphs, lists, code, images), checks that code, URLs and numbers in code
survived unchanged, and for Persian (--lang fa) checks orthography: Arabic
ي/ك, mixed digit systems, ASCII punctuation in Persian prose, missing
half-spaces (ZWNJ), and paragraphs that start with a Latin word (they flip to
left-to-right when direction is auto-detected).

It catches mechanical slips only. Voice and storytelling still need a read.
Keep the source text in a scratch directory, not in the notes.
"""
from __future__ import annotations

import argparse
import re
import sys

FA = "؀-ۿ"
ZWNJ = "‌"


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5:]
    return text


def strip_header(text: str) -> str:
    """Drop a file header (source line, license, links) that ends with a `---` line,
    as long as it holds no heading. Translations and saved sources both use one."""
    m = re.search(r"\n-{3,}\n", "\n" + text)
    if m and m.start() < 2000 and not re.search(r"^#{1,6} ", text[:m.start()], re.M):
        return ("\n" + text)[m.end():]
    return text


def blocks(text: str):
    """Split Markdown into blocks, keeping fenced code blocks whole."""
    out, cur, fence = [], [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fence = not fence
            cur.append(line)
            if not fence:
                out.append("\n".join(cur)); cur = []
            continue
        if fence:
            cur.append(line); continue
        if not line.strip():
            if cur:
                out.append("\n".join(cur)); cur = []
        else:
            cur.append(line)
    if cur:
        out.append("\n".join(cur))
    return [b for b in out if b.strip() and not re.fullmatch(r"-{3,}", b.strip())]


def kind(b: str) -> str:
    s = b.lstrip()
    if s.startswith("```"): return "code"
    m = re.match(r"(#{1,6}) ", s)
    if m: return f"h{len(m.group(1))}"
    if s.startswith("!["): return "image"
    if re.match(r"\[\^[^\]]+\]:", s): return "footnote"
    if re.match(r"([-*+]|\d+[.)]) ", s): return "list"
    if s.startswith(">"): return "quote"
    if s.startswith("|"): return "table"
    return "p"


def code_blocks(bs):
    return [b for b in bs if kind(b) == "code"]


def urls(text):
    return sorted(re.findall(r"https?://[^\s)>\]]+", text))


def check_structure(src_bs, tr_bs, problems):
    sk = [kind(b) for b in src_bs if kind(b) != "footnote"]
    tk = [kind(b) for b in tr_bs if kind(b) != "footnote"]
    if sk != tk:
        problems.append(f"Block structure differs.\n   source:      {sk}\n   translation: {tk}")
    else:
        print(f"✅ Structure: {len(sk)} blocks in the same order "
              f"({sk.count('p')} paragraphs, {sum(k.startswith('h') for k in sk)} headings)")
    sc, tc = code_blocks(src_bs), code_blocks(tr_bs)
    if sc != tc:
        problems.append(f"Code blocks changed ({len(sc)} in source, {len(tc)} in translation, "
                        f"{sum(a != b for a, b in zip(sc, tc))} differ).")
    elif sc:
        print(f"✅ Code: {len(sc)} code blocks byte-for-byte identical")
    su = urls("\n".join(src_bs)); tu = urls("\n".join(tr_bs))
    if su != tu:
        missing = sorted(set(su) - set(tu)); extra = sorted(set(tu) - set(su))
        problems.append(f"URLs differ. Missing: {missing}  Extra: {extra}")
    elif su:
        print(f"✅ URLs: {len(su)} identical")


def prose(b: str) -> str:
    b = re.sub(r"`[^`]*`", " ", b)                      # inline code
    b = re.sub(r"\]\([^)]*\)", "]", b)                  # link targets
    b = re.sub(r"https?://\S+", " ", b)
    b = re.sub(r"\[\^[^\]]+\]", " ", b)                 # footnote refs
    return b


def check_persian(tr_bs, problems):
    text = "\n\n".join(prose(b) for b in tr_bs if kind(b) not in ("code",))
    arabic = re.findall(r"\S*[يك]\S*", text)
    if arabic:
        problems.append(f"Arabic ي/ك instead of Persian ی/ک: {arabic[:8]}")
    fa_digits = re.findall("[۰-۹]", text); latin_digits = re.findall(r"(?<![A-Za-z])\d", text)
    if fa_digits and latin_digits:
        problems.append(f"Mixed digits: {len(fa_digits)} Persian and {len(latin_digits)} Latin. Pick one (code stays Latin).")
    # ASCII punctuation touching Persian letters
    ascii_p = re.findall(rf"[{FA}][,;?]|[,;?]\s*[{FA}]", text)
    if ascii_p:
        problems.append(f"ASCII , ; ? next to Persian text (use ، ؛ ؟): {ascii_p[:8]}")
    quotes = re.findall(rf"\"[^\"]*[{FA}][^\"]*\"", text)
    if quotes:
        problems.append(f"ASCII quotes around Persian (use «…»): {quotes[:5]}")
    mi = re.findall(r"(?:^|\s)(ن?می) (\S+)", text)
    if mi:
        problems.append(f"«می» followed by a full space (needs ZWNJ): {[' '.join(x) for x in mi[:8]]}")
    ha = re.findall(rf"[{FA}]+ (?:ها|های|هایی|هایم|هایت)(?=[\s،.؛؟]|$)", text)
    if ha:
        problems.append(f"Plural «ها» after a full space (needs ZWNJ): {ha[:8]}")
    latin_ha = re.findall(r"[A-Za-z]+(?:ها|های)", text)
    if latin_ha:
        problems.append(f"Latin word joined to «ها» without ZWNJ: {latin_ha[:8]}")
    ltr_start = []
    for b in tr_bs:
        if kind(b) not in ("p", "list", "quote"):
            continue
        m = re.search(rf"[A-Za-z{FA}]", re.sub(r"^[\s>*\-+\d.)#«(\[!]+", "", b))
        if m and not ("؀" <= m.group() <= "ۿ"):
            ltr_start.append(b.strip()[:40].replace("\n", " "))
    if ltr_start:
        problems.append("Paragraphs starting with a Latin letter (may render left-to-right; start with a Persian word): "
                        + "; ".join(ltr_start[:5]))
    if not problems:
        print(f"✅ Persian orthography: no Arabic ي/ك, consistent digits, Persian punctuation, "
              f"{text.count(ZWNJ)} half-spaces")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("translation")
    ap.add_argument("--source", help="the original text, same Markdown block layout")
    ap.add_argument("--lang", default="", help="target language code, e.g. fa")
    ap.add_argument("--skip-header", type=int, default=0,
                    help="ignore the first N blocks of the translation (its own header)")
    args = ap.parse_args()

    tr_bs = blocks(strip_header(strip_frontmatter(open(args.translation, encoding="utf-8").read())))[args.skip_header:]
    problems: list[str] = []
    if args.source:
        src_bs = blocks(strip_header(strip_frontmatter(open(args.source, encoding="utf-8").read())))
        check_structure(src_bs, tr_bs, problems)
    if args.lang.lower() in ("fa", "per", "persian", "farsi"):
        check_persian(tr_bs, problems)
    for p in problems:
        print(f"⚠️  {p}")
    if not problems:
        print("All mechanical checks passed. Now read it side by side for voice and storytelling.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
