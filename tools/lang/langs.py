"""The site's languages: one file each, tools/lang/<code>.json (en is the ASV, the source of every page). Every tool that
differs by language reads it from here, so a new language is a new file (plus its labels in tools/full/i18n/<code>/ and its
Worker in tools/site/workers/<code>.jsonc), never an edit of shared code.

    name         the language named in itself, for the menu ("Español")
    text         ref/<eBible id> of its public-domain Bible; credit: the short name on every page ("RV1909")
    fallback     a second eBible text for verses the first one's file lacks (listed in coverage.md)
    versemap     {BOOK: ["c:a-b > tc:tv", …]}: ASV verses c:a…c:b are the translation's tc:tv onward, where asv.align's
                 pairing by length can't find its way (a renumbered chapter); "c:a-b > tc:tv-tw" shares a block of
                 verses divided differently; verse 0 is a psalm's superscription (see versemap()); a mapped chapter's verses no rule names come from fallback
    psalm_title  a regex for where a psalm proper begins inside verse 1, for a text that folds the superscription into it
    css          extra CSS for every page of the language (in the page's own <style>), for layout the translation needs
    drop         a regex for notes the text's file keeps inside its verses, taken out of the pages and the text PDFs (Riveduta's "(H7-1)" Hebrew numbers, Luther 1912's own "[3:19]")
    psalm_title_verses  true for a text that numbers a psalm's superscription as verse 1 (or 1–2), the Hebrew numbering:
                 those verses become the title and the psalm is renumbered from 1 (asv.title_verses; needs psalm_title too)
    accent_room  a share (0.16) by which a cover's book name is set smaller, on the same baseline, when its capitals carry
                 accents (ÉSAÏE), so they clear the line above it (labels.lower)
    unspaced     true for a script written without spaces (Chinese, Japanese): a cut may fall between any two characters
    books, abbr  verse references by rule: English book names / page abbreviations -> this language's; abridged: "ABRIDGED";
                 a value with {n} takes the numbers inside it ("Chapter": "第{n}章"), else they follow it after a space
    codes        extra {book name in the text's \\h line: USFM code} where the text's own names don't match the labels
    fonts        {"load": {family: [weights]}, "fallback": {manga font: family}}: Google Fonts families for a script the
                 manga's fonts lack (Anton and Archivo Narrow have no Cyrillic or CJK, IBM Plex Mono and Source Serif 4, the
                 text PDFs' face, no CJK), each set in every font list right after the font it stands in for (a list:
                 several, in order, e.g. a display face whose glyph set is smaller, then a complete one)
    ui           the website's words (build_site.py); words: the text PDF's (asv_pdf.py); epub: the EPUB's (export_book.py)"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
LANGS = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(HERE.glob("*.json"))}
ORDER = ["en"] + sorted(k for k in LANGS if k != "en")

def get(code): return LANGS[code]
def by_text(tid):
    """The language whose text is ref/<tid>."""
    return next(k for k, v in LANGS.items() if v["text"] == tid)

def numbered(word, n):
    """"Chapter" + 3 -> "Chapter 3"; a word with {n} takes the number inside it ("第{n}章" -> "第3章")."""
    return word.replace("{n}", str(n)) if "{n}" in word else f"{word} {n}"

def versemap(code):
    """{BOOK: [((c, a, b), (tc, tv, tw))]} from the "c:a-b > tc:tv" strings (tw None: verse for verse) and the block form
    "c:a-b > tc:tv-tw" (ASV verses a…b share the translation's verses tv…tw, divided by length at the best breaks: two
    verses the translation joins in one, or one it splits in two). Verse 0 is a psalm's superscription: on the ASV side
    its title (asv.Book("PSA").titles), on the translation's side its \\d line, else a numbered verse ("51:0-0 > 50:1-2")."""
    out = {}
    for book, rules in LANGS[code].get("versemap", {}).items():
        for r in rules:
            c, a, b, tc, tv, tw = re.fullmatch(r"(\d+):(\d+)-(\d+) > (\d+):(\d+)(?:-(\d+))?", r).groups()
            out.setdefault(book, []).append(((int(c), int(a), int(b)), (int(tc), int(tv), int(tw) if tw else None)))
    return out

FAMILY = re.compile(r"""(?<![\w-])(['"]?)(Anton|Archivo Narrow|IBM Plex Mono|Noto Sans JP|Source Serif 4)\1(?=\s*[,;"'])""")
def with_fallbacks(src, code):
    """Page markup or CSS with this language's fallback family after each manga font it stands in for, and, where the
    fallback is wider than the manga font (Anton is very narrow), a font-size-adjust that sets its letters at the size
    the page was laid out for ("adjust": {manga font: x-height ratio})."""
    fb = LANGS[code].get("fonts", {}).get("fallback", {})
    if not fb: return src
    def more(f):                                       # one family, or a list of them (a display face, then a full one)
        return "".join(f", '{x}'" for x in ([f] if isinstance(f, str) else f))
    src = FAMILY.sub(lambda m: m.group(0) + (more(fb[m.group(2)]) if m.group(2) in fb else ""), src)
    for fam, ratio in LANGS[code].get("fonts", {}).get("adjust", {}).items():
        src = re.sub(r"""(font-family:\s*['"]?""" + re.escape(fam) + r"""\b[^;"{}]*)(?=[;"}])""", rf"\1; font-size-adjust: {ratio}", src)
    return src

def font_query(code):
    """The extra families as Google Fonts css2 query parts ("family=Oswald:wght@400;700")."""
    return [f"family={f.replace(' ', '+')}:wght@{';'.join(map(str, w))}" for f, w in LANGS[code].get("fonts", {}).get("load", {}).items()]

def text_pieces(chars, size=600):
    """The characters to subset a font to, in pieces Google Fonts' `text=` accepts (a long one is refused with a 400: a
    whole Bible in a CJK script uses thousands), each with the unicode-range it covers ("" when one piece holds them all)."""
    if len(chars) <= size: return [(chars, "")]
    return [(p, unicode_range(p)) for p in (chars[i:i + size] for i in range(0, len(chars), size))]

def unicode_range(chars):
    cps, out, i = sorted(set(map(ord, chars))), [], 0
    while i < len(cps):
        j = i
        while j + 1 < len(cps) and cps[j + 1] == cps[j] + 1: j += 1
        out.append(f"U+{cps[i]:X}" + (f"-{cps[j]:X}" if j > i else "")); i = j + 1
    return ", ".join(out)
