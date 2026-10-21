"""The site's languages: one file each, tools/lang/<code>.json (en is the ASV, the source of every page). Every tool that
differs by language reads it from here, so a new language is a new file (plus its labels in tools/full/i18n/<code>/ and its
Worker in tools/site/workers/<code>.jsonc), never an edit of shared code.

    name         the language named in itself, for the menu ("Español")
    text         ref/<eBible id> of its public-domain Bible; credit: the short name on every page ("RV1909")
    fallback     a second eBible text for verses the first one's file lacks (listed in coverage.md)
    versemap     {BOOK: ["c:a-b > tc:tv", …]}: ASV verses c:a…c:b are the translation's tc:tv onward, where asv.align's
                 pairing by length can't find its way (a renumbered chapter)
    psalm_title  a regex for where a psalm proper begins inside verse 1, for a text that folds the superscription into it
    unspaced     true for a script written without spaces (Chinese, Japanese): a cut may fall between any two characters
    accent_room  true: a big <h1> title whose capitals carry accents (GÊNESIS) is set lower by an accent's height, so the
                 accent clears the line above it (labels.translate)
    fit_room     true, for a language whose words run longer than the English: a law cell sets its words a little smaller,
                 and smaller again by a heading that runs to a second line (exo.kit.law); a dialogue panel whose words
                 overrun it sets its balloons smaller (exo.kit.talk_fit); a drawn IBM Plex Mono label that would run out of
                 its drawing shrinks to fit as a data-fit label does (labels.translate)
    strip        regexes (multiline) cut out of the text's USFM files before anything reads them: stray matter a draft
                 text left in its verses (porbrbsl: a machine translator's "Aqui está a tradução …:" and ``` fences)
    thousands    the thousands separator for numbers in labels and drawings (601,730 -> "." 601.730); none: kept as is
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

def usfm(path):
    """A USFM file's source, less what its language's "strip" patterns cut out (the text is known by its ref/<id> folder)."""
    s = pathlib.Path(path).read_text(encoding="utf-8")
    for v in LANGS.values():
        if v["text"] == pathlib.Path(path).parent.name:
            for pat in v.get("strip", []): s = re.sub(pat, "", s, flags=re.M)
    return s

def versemap(code):
    """{BOOK: [((c, a, b), (tc, tv))]} from the "c:a-b > tc:tv" strings."""
    out = {}
    for book, rules in LANGS[code].get("versemap", {}).items():
        for r in rules:
            c, a, b, tc, tv = map(int, re.fullmatch(r"(\d+):(\d+)-(\d+) > (\d+):(\d+)", r).groups())
            out.setdefault(book, []).append(((c, a, b), (tc, tv)))
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
