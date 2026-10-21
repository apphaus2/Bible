"""What asv.Book leaves out of the Psalms, cut straight from ref/eng-asv (never typed): the superscriptions (USFM \\d, "A Psalm
of David." — asv.parse drops them, so they are not verses and coverage does not count them), the five book heads
(\\ms1 "BOOK I" …), Psalm 119's first letter head (\\qc "א ALEPH.", which comes before verse 1; the other 21 letter heads
sit at the end of verses 8, 16 … and are cut from the verse itself), and the poetic line breaks (\\q1, \\qs) inside
each verse, so a song line can be set one poetic line to a row.

    TITLES[3]  -> "A Psalm of David, when he fled from Absalom his son."
    BOOKS[42]  -> "BOOK II"
    ALEPH      -> "א ALEPH."
    LINES[(1, 1)] -> ["Blessed is the man that walketh not in the counsel of the wicked,", "Nor standeth …", …]
These are shown as labels (data-label): the ASV text check reads only the verses."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = (ROOT / "ref" / "eng-asv" / "20-PSAeng-asv.usfm").read_text(encoding="utf-8")

def _clean(t):
    t = re.sub(r"\\f .*?\\f\*", "", t, flags=re.S)
    t = re.sub(r"\\x .*?\\x\*", "", t, flags=re.S)
    t = re.sub(r"\\\+?w ([^|\\]*)\|[^\\]*\\\+?w\*", r"\1", t)
    t = re.sub(r"\\\+?add\*?", "", t)
    t = re.sub(r"\\[a-z0-9+]+\*?", "", t)
    return re.sub(r"\s+", " ", t).strip().replace("\u2019", "'").replace("\u2018", "'")

TITLES, BOOKS, LINES, ALEPH = {}, {}, {}, None
for cm in re.finditer(r"\\c (\d+)(.*?)(?=\\c \d+|\Z)", SRC, flags=re.S):
    c, body = int(cm.group(1)), cm.group(2)
    head = body.split("\\v ", 1)[0]
    for m in re.finditer(r"^\\d (.*)$", head, flags=re.M): TITLES[c] = _clean(m.group(1))
    for m in re.finditer(r"^\\ms1 (.*)$", head, flags=re.M): BOOKS[c] = _clean(m.group(1))
    for m in re.finditer(r"^\\qc (.*)$", head, flags=re.M): ALEPH = _clean(m.group(1))
    for vm in re.finditer(r"\\v (\d+)(.*?)(?=\\v \d+|\Z)", body, flags=re.S):
        raw = re.sub(r"\\f .*?\\f\*", "", vm.group(2), flags=re.S)
        for m in re.finditer(r"^\\ms1 (.*)$", raw, flags=re.M): BOOKS[c + 1] = _clean(m.group(1))   # "BOOK II" closes Psalm 41
        raw = re.sub(r"^\\ms1 .*$", "", raw, flags=re.M)
        parts = re.split(r"\\(?:q\d?|qs|qc|b)\b(?!\*)", raw)
        LINES[(c, int(vm.group(1)))] = [p for p in (_clean(x) for x in parts) if p]

import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import asv as _asv
HEADS = {}                               # (119, v) -> the letter head a translation sets before verse v ("BETE"), if it has them
if _asv.LANG != "en":                    # another language: titles split off its verse 1 (asv.psalm_titles), no line breaks
    _B = _asv.Book("PSA")
    TITLES, HEADS = _B.titles, {k: h for k, h in getattr(_B, "heads", {}).items() if k[0] == 119}
    LINES = {}

def lines_of(c, x, text):
    """The poetic lines of verse c:x, checked against the verse text asv.Book gives (same words, same order)."""
    ls = LINES.get((c, x), [text])
    joined = " ".join(ls)
    if joined != text:
        return [text]          # a verse whose breaks do not line up is set as one block, never altered
    return ls
