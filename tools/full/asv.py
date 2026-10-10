"""The ASV text, straight from ref/asv/*.usfm (eBible.org, public domain), and a coverage tracker.

    from asv import Book
    G = Book("GEN")
    G.v("1:3")                          -> the whole verse
    G.v("1:3", to="said,")              -> from the start of the verse through "said,"
    G.v("1:3", frm="Let", to="light:")  -> from "Let" through the first "light:" after it
    G.v("1:3", frm="and there")         -> from "and there" to the end of the verse
    G.span("1:1-3")                     -> whole verses joined with spaces
Every call records which characters of which verse were used, so G.coverage() can report each verse as
full / partial / omitted. Text is never typed by hand: it is always cut out of the USFM."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
FILES = {"GEN": "02-GENeng-asv.usfm", "EXO": "03-EXOeng-asv.usfm", "LEV": "04-LEVeng-asv.usfm", "NUM": "05-NUMeng-asv.usfm",
         "DEU": "06-DEUeng-asv.usfm", "JOS": "07-JOSeng-asv.usfm", "JDG": "08-JDGeng-asv.usfm", "RUT": "09-RUTeng-asv.usfm",
         "1SA": "10-1SAeng-asv.usfm", "2SA": "11-2SAeng-asv.usfm", "1KI": "12-1KIeng-asv.usfm", "2KI": "13-2KIeng-asv.usfm"}

def parse(path):
    """{(chapter, verse): text}: Strong's tags, footnotes and cross-references stripped; supplied (italic) words kept."""
    s = pathlib.Path(path).read_text(encoding="utf-8")
    s = re.sub(r"\\f .*?\\f\*", "", s, flags=re.S)
    s = re.sub(r"\\x .*?\\x\*", "", s, flags=re.S)
    s = re.sub(r"\\\+?w ([^|\\]*)\|[^\\]*\\\+?w\*", r"\1", s)
    s = re.sub(r"\\\+?add\*?", "", s)
    s = re.sub(r"\\(id|h|toc\d|mt\d?|ms\d?|s\d?|d|r)\b[^\n]*", "", s)
    s = re.sub(r"\\(p|q\d?|m|b|nb|pi\d?|li\d?|qc|qr)\b", " ", s)
    out = {}
    for cm in re.finditer(r"\\c (\d+)(.*?)(?=\\c \d+|\Z)", s, flags=re.S):
        ch = int(cm.group(1))
        for vm in re.finditer(r"\\v (\d+)(.*?)(?=\\v \d+|\Z)", cm.group(2), flags=re.S):
            t = re.sub(r"\\[a-z0-9+]+\*?", "", vm.group(2))
            out[(ch, int(vm.group(1)))] = re.sub(r"\s+", " ", t).strip().replace("\u2019", "'").replace("\u2018", "'")
    return out

def key(ref):
    c, v = ref.split(":"); return int(c), int(v)

class Book:
    def __init__(self, code):
        self.code = code
        self.verses = parse(ROOT / "ref" / "asv" / FILES[code])
        self.used = {}                       # (c, v) -> set of character indexes used

    def _mark(self, k, a, b):
        self.used.setdefault(k, set()).update(range(a, b))

    def v(self, ref, frm=None, to=None):
        k = key(ref); t = self.verses[k]
        a = 0 if frm is None else t.find(frm)
        if a < 0: raise ValueError(f"{self.code} {ref}: {frm!r} not in verse")
        if to is None: b = len(t)
        else:
            i = t.find(to, a)
            if i < 0: raise ValueError(f"{self.code} {ref}: {to!r} not after {frm!r}")
            b = i + len(to)
        self._mark(k, a, b)
        return t[a:b].strip()

    def span(self, refs):
        """'1:1-3' or '2:24' -> whole verses joined with spaces."""
        c, vs = refs.split(":")
        a, _, b = vs.partition("-")
        return " ".join(self.v(f"{c}:{n}") for n in range(int(a), int(b or a) + 1))

    def text(self):
        return " ".join(self.verses[k] for k in sorted(self.verses))

    def coverage(self, chapters):
        """[(ref, status, share)] for every verse of the given chapters."""
        rows = []
        for k in sorted(k for k in self.verses if k[0] in chapters):
            t = self.verses[k]
            letters = [i for i, ch in enumerate(t) if not ch.isspace()]
            got = self.used.get(k, set())
            share = sum(1 for i in letters if i in got) / max(1, len(letters))
            st = "full" if share > 0.97 else ("partial" if share > 0 else "omitted")
            rows.append((f"{k[0]}:{k[1]}", st, share))
        return rows
