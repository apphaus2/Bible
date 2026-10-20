"""The ASV text, straight from ref/asv/*.usfm (eBible.org, public domain), and a coverage tracker.

    from asv import Book
    G = Book("GEN")
    G.v("1:3")                          -> the whole verse
    G.v("1:3", to="said,")              -> from the start of the verse through "said,"
    G.v("1:3", frm="Let", to="light:")  -> from "Let" through the first "light:" after it
    G.v("1:3", frm="and there")         -> from "and there" to the end of the verse
    G.span("1:1-3")                     -> whole verses joined with spaces
Every call records which characters of which verse were used, so G.coverage() can report each verse as
full / partial / omitted. Text is never typed by hand: it is always cut out of the USFM.

Other languages: with BIBLE_LANG=es (or fr) every call returns the same verses from that language's public-domain text
(TEXTS below) instead. The plans still name their cuts in ASV words, so a cut is found in the ASV verse and mapped onto
the translated verse by its share of the letters, moved to the nearest punctuation or word break (the same share always
lands on the same break, so a verse cut in two pieces still meets in the middle)."""
import os, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
TEXTS = {"en": ("asv", "ASV"), "es": ("rv1909", "RV1909"), "fr": ("lsg", "LSG")}   # language -> (ref/ folder, credit)
LANG = os.environ.get("BIBLE_LANG", "en")
CREDIT = TEXTS[LANG][1]
def files(folder):
    return {re.match(r"\d\d-(\w{3})", p.name).group(1): p.name for p in sorted((ROOT / "ref" / folder).glob("[0-9][0-9]-*.usfm"))}
FILES = files("asv")                                                     # all 66 books

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

def _share(t, i):
    """The share of a verse's letters that come before index i."""
    n = sum(1 for ch in t if not ch.isspace())
    return sum(1 for ch in t[:i] if not ch.isspace()) / max(1, n)

STOPS = ",;:.!?"
def _kind(t, i):
    """What kind of break index i is: "speech" (a stop before a capital, as before words spoken), "end" (after . ? !),
    "pause" (after , ; :) or None (between words)."""
    ch, nxt = t[:i].rstrip()[-1:], t[i:].lstrip()[:1]
    if ch and ch in ",:" and (nxt.isupper() or nxt in "¿¡«"): return "speech"
    if ch and ch in ".?!": return "end"
    if ch and ch in ",;:": return "pause"
    return None

def _snap(t, f, kind, lo=0):
    """The index in verse t at share f of its letters, moved to the nearest break after lo: a break of the same kind as
    the ASV cut's (see _kind) is strongly preferred, any other stop a little."""
    if f <= 0.002 and lo == 0: return 0
    if f >= 0.998: return len(t)
    best, bi = 9, len(t)
    for i in range(lo + 1, len(t)):
        if t[i] != " ": continue
        k = _kind(t, i)
        d = abs(_share(t, i) - f) - (0.25 if k and k == kind else 0.06 if k else 0)
        if d < best: best, bi = d, i
    return bi

def mapped(src, a, b, t, prev=None):
    """A cut [a, b) of the ASV verse src, as a cut of the translated verse t. prev = (ASV end, translated end) of the cut
    before it in the same verse: a cut that starts where that one ended starts where its translation ended."""
    while a < len(src) and src[a].isspace(): a += 1
    if prev and prev[0] <= a and src[prev[0]:a].strip() == "": a2 = prev[1]
    else: a2 = _snap(t, _share(src, a), _kind(src, a))
    while a2 < len(t) and t[a2].isspace(): a2 += 1
    b2 = _snap(t, _share(src, b), _kind(src, b), a2)
    return a2, max(b2, a2)

def key(ref):
    c, v = ref.split(":"); return int(c), int(v)

class Book:
    def __init__(self, code):
        self.code = code
        self.src = parse(ROOT / "ref" / "asv" / FILES[code])          # where the plans' ASV words are found
        self.verses = self.src if LANG == "en" else parse(ROOT / "ref" / TEXTS[LANG][0] / files(TEXTS[LANG][0])[code])
        self.used = {}                       # (c, v) -> set of character indexes used
        self.cuts = []                       # every (ref, text) handed out, for build_volume's lost-text check
        self.last = {}                       # (c, v) -> (ASV end, translated end) of the last cut, other languages only

    def _mark(self, k, a, b):
        self.used.setdefault(k, set()).update(range(a, b))

    def v(self, ref, frm=None, to=None, after=None):
        """after: start looking for frm only past the first occurrence of this text (for a phrase said twice in a verse)."""
        k = key(ref); t = self.src[k]
        s0 = 0 if after is None else t.index(after) + len(after)
        a = s0 if frm is None else t.find(frm, s0)
        if a < 0: raise ValueError(f"{self.code} {ref}: {frm!r} not in verse")
        if to is None: b = len(t)
        else:
            i = t.find(to, a)
            if i < 0: raise ValueError(f"{self.code} {ref}: {to!r} not after {frm!r}")
            b = i + len(to)
        if LANG != "en":
            t, b_en = self.verses.get(k, ""), b
            a, b = mapped(self.src[k], a, b, t, self.last.get(k))
            self.last[k] = (b_en, b)
        self._mark(k, a, b)
        self.cuts.append((ref, t[a:b].strip()))
        return t[a:b].strip()

    def span(self, refs):
        """'1:1-3' or '2:24' -> whole verses joined with spaces."""
        c, vs = refs.split(":")
        a, _, b = vs.partition("-")
        return " ".join(self.v(f"{c}:{n}") for n in range(int(a), int(b or a) + 1))

    def text(self):
        return " ".join(self.verses[k] for k in sorted(self.verses))

    def coverage(self, chapters, span=None):
        """[(ref, status, share)] for every verse of the given chapters; span=("24:1", "25:18") limits it to a run of
        verses, for a manga chapter that starts or ends inside a Bible chapter."""
        rows = []
        lo, hi = (key(span[0]), key(span[1])) if span else ((0, 0), (999, 999))
        for k in sorted(k for k in self.verses if k[0] in chapters and lo <= k <= hi):
            t = self.verses[k]
            letters = [i for i, ch in enumerate(t) if not ch.isspace()]
            got = self.used.get(k, set())
            share = sum(1 for i in letters if i in got) / max(1, len(letters))
            st = "full" if share > 0.97 else ("partial" if share > 0 else "omitted")
            rows.append((f"{k[0]}:{k[1]}", st, share))
        return rows
