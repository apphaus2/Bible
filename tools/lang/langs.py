"""The site's languages: one file each, tools/lang/<code>.json (en is the ASV, the source of every page). Every tool that
differs by language reads it from here, so a new language is a new file (plus its labels in tools/full/i18n/<code>/ and its
Worker in tools/site/workers/<code>.jsonc), never an edit of shared code.

    name         the language named in itself, for the menu ("Español")
    text         ref/<eBible id> of its public-domain Bible; credit: the short name on every page ("RV1909")
    fallback     a second eBible text for verses the first one's file lacks (listed in coverage.md)
    versemap     {BOOK: ["c:a-b > tc:tv", …]}: ASV verses c:a…c:b are the translation's tc:tv onward, where asv.align's
                 pairing by length can't find its way (a renumbered chapter); "c:a-b > tc:tv-tw" shares a block of
                 verses divided differently; verse 0 is a psalm's superscription (see versemap())
    psalm_title  a regex for where a psalm proper begins inside verse 1, for a text that folds the superscription into it
    unspaced     true for a script written without spaces (Chinese, Japanese): a cut may fall between any two characters
    books, abbr  verse references by rule: English book names / page abbreviations -> this language's; abridged: "ABRIDGED"
    codes        extra {book name in the text's \\h line: USFM code} where the text's own names don't match the labels
    fonts        {"load": {family: [weights]}, "fallback": {manga font: family}}: Google Fonts families for a script the
                 manga's fonts lack (Anton and Archivo Narrow have no Cyrillic or CJK, IBM Plex Mono and Source Serif 4, the
                 text PDFs' face, no CJK), each set in every font list right after the font it stands in for
    ui           the website's words (build_site.py); words: the text PDF's (asv_pdf.py); epub: the EPUB's (export_book.py)"""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
LANGS = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(HERE.glob("*.json"))}
ORDER = ["en"] + sorted(k for k in LANGS if k != "en")

def get(code): return LANGS[code]
def by_text(tid):
    """The language whose text is ref/<tid>."""
    return next(k for k, v in LANGS.items() if v["text"] == tid)

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
    """Page markup or CSS with this language's fallback family after each manga font it stands in for."""
    fb = LANGS[code].get("fonts", {}).get("fallback", {})
    if not fb: return src
    return FAMILY.sub(lambda m: m.group(0) + (f", '{fb[m.group(2)]}'" if m.group(2) in fb else ""), src)

def font_query(code):
    """The extra families as Google Fonts css2 query parts ("family=Oswald:wght@400;700")."""
    return [f"family={f.replace(' ', '+')}:wght@{';'.join(map(str, w))}" for f, w in LANGS[code].get("fonts", {}).get("load", {}).items()]
