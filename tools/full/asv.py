"""The ASV text, straight from ref/eng-asv/*.usfm (eBible.org, public domain), and a coverage tracker.

    from asv import Book
    G = Book("GEN")
    G.v("1:3")                          -> the whole verse
    G.v("1:3", to="said,")              -> from the start of the verse through "said,"
    G.v("1:3", frm="Let", to="light:")  -> from "Let" through the first "light:" after it
    G.v("1:3", frm="and there")         -> from "and there" to the end of the verse
    G.span("1:1-3")                     -> whole verses joined with spaces
Every call records which characters of which verse were used, so G.coverage() can report each verse as
full / partial / omitted. Text is never typed by hand: it is always cut out of the USFM.

Other languages: with BIBLE_LANG=es (any tools/lang/<code>.json) every call returns the same verses from that language's
public-domain text instead. The plans still name their cuts in ASV words, so a cut is found in the ASV verse and mapped onto
the translated verse by its share of the letters, moved to the nearest punctuation or word break (the same share always
lands on the same break, so a verse cut in two pieces still meets in the middle)."""
import os, re, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
import sys; sys.path.insert(0, str(ROOT / "tools" / "lang"))
import langs
LANG = os.environ.get("BIBLE_LANG", "en")
L = langs.get(LANG)                  # the language's text, credit, fallback text and verse map (tools/lang/<code>.json)
CREDIT = L["credit"]
UNSPACED = bool(L.get("unspaced"))   # Chinese, Japanese: a cut may fall between any two characters
def files(folder):
    return {re.match(r"\d\d-(\w{3})", p.name).group(1): p.name for p in sorted((ROOT / "ref" / folder).glob("[0-9][0-9]-*.usfm"))}
FILES = files("eng-asv")                                                     # all 66 books

def parse(path):
    """{(chapter, verse): text}: Strong's tags, footnotes and cross-references stripped; supplied (italic) words kept."""
    s = pathlib.Path(path).read_text(encoding="utf-8")
    s = re.sub(r"\\f .*?\\f\*", "", s, flags=re.S)
    s = re.sub(r"\\x .*?\\x\*", "", s, flags=re.S)
    s = re.sub(r"\\\+?w ([^|\\]*)\|[^\\]*\\\+?w\*", r"\1", s)
    s = re.sub(r"\\\+?add\*?", "", s)
    s = re.sub(r"\\(id|h|toc\d|mt\d?|ms\d?|s\d?|d|r|sp)\b[^\n]*", "", s)    # sp: a speaker heading (Song of Solomon)
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

STOPS = ",;:.!?，、；：。！？"
CLOSE, OPEN = "」』）〉》】”’)]、。，．！？：；・ー々ゝゞぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮヵヶ", "「『（〈《【“‘(["
WIDE = "　-ヿ㐀-䶿一-鿿豈-﫿＀-￯"    # CJK: kana, kanji, full-width forms
def unspace(t):
    """An unspaced script's text with the spaces between two of its characters taken out: those a USFM poetic line
    break or a stripped note leaves inside a verse, and those a plan puts between the verses or cuts it joins (a line
    break is no space there; the text check reads it the same way). Spaces next to Latin letters, digits, · or — stay."""
    return re.sub(f"(?<=[{WIDE}])\\s+(?=[{WIDE}])", "", t) if UNSPACED else t

def _kind(t, i):
    """What kind of break index i is: "speech" (a stop before a capital or an opening quote, as before words spoken), "end"
    (after . ? !), "pause" (after , ; :) or None (between words). Full-width CJK stops count as their Latin kin; in an
    unspaced script a closing quote is looked through (。」 is an end) and any stop before 「 or 『 is speech (言われた。「…)."""
    ch, nxt = t[:i].rstrip()[-1:], t[i:].lstrip()[:1]
    if UNSPACED:
        ch = t[:i].rstrip().rstrip("」』）)”")[-1:]
        if ch and ch in STOPS and nxt in "「『": return "speech"
    if ch and ch in ",:，：" and (nxt.isupper() or nxt in "¿¡«「『“"): return "speech"
    if ch and ch in ".?!。？！": return "end"
    if ch and ch in ",;:，、；：": return "pause"
    return None

def _snap(t, f, kind, lo=0):
    """The index in verse t at share f of its letters, moved to the nearest break after lo: a break of the same kind as
    the ASV cut's (see _kind) is strongly preferred, any other stop a little."""
    if f <= 0.002 and lo == 0: return 0
    if f >= 0.998: return len(t)
    best, bi = 9, len(t)
    for i in range(lo + 1, len(t)):
        if t[i] != " " and not UNSPACED: continue
        if UNSPACED and (t[i] in CLOSE or t[i - 1] in OPEN): continue   # no piece starts with 」、。 or ends with 「
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

def _letters(t): return sum(1 for ch in t if not ch.isspace())

MISSING = []                         # ASV verses a translation's file lacks (see align)

def _pair(src, tgt, A, R, lost=40):
    """Gale–Church pairing of ASV verses A with translated verses R by length: one to one, two to one, one to two, or a verse
    with no partner (lost from a file). Returns [(ASV keys, translated keys)]."""
    la, lr = [_letters(src[k]) for k in A], [_letters(tgt[k]) for k in R]
    c = sum(lr) / max(1, sum(la))
    def cost(a, r, one):
        d = (r - c * a) / ((c * a + 1) ** 0.5)
        return d * d + (0 if one else 6)
    n, m = len(A), len(R); D = {(0, 0): (0, None)}
    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) == (0, 0): continue
            best = (float("inf"), None)
            for di, dj in ((1, 1), (2, 1), (1, 2), (1, 0), (0, 1)):
                if i - di < 0 or j - dj < 0 or (i - di, j - dj) not in D: continue
                x = D[(i - di, j - dj)][0] + (lost if 0 in (di, dj) else cost(sum(la[i - di:i]), sum(lr[j - dj:j]), di == dj == 1))
                if x < best[0]: best = (x, (di, dj))
            if best[1]: D[(i, j)] = best
    out, i, j = [], n, m
    while (i, j) != (0, 0):
        di, dj = D[(i, j)][1]; out.append((A[i - di:i], R[j - dj:j])); i, j = i - di, j - dj
    return out[::-1]

def align(src, tgt):
    """The translated text re-keyed by ASV verse. eBible's Reina-Valera keeps the English verse numbers but, where its own
    numbering differs, shifts the words and leaves slots empty (its Job 39:1 is the ASV's 38:39; it even loses Job 39:28–40:5
    off the end of a chapter). Around every empty or unmatched slot the chapters (the one before, it, the next) are paired by
    length (_pair); everywhere else verse n is verse n. A split translated verse is cut at its best break."""
    t_ok = {k: v for k, v in tgt.items() if v.strip()}
    odd = {k[0] for k in set(src) ^ set(t_ok)}
    ks = sorted(set(src) & set(t_ok))                                    # and chapters where two verses running are out of
    r = [math.log((_letters(t_ok[k]) + 5) / (_letters(src[k]) + 5)) for k in ks]   # proportion: a shift with no empty slot
    mu = sum(r) / max(1, len(r))
    odd |= {ks[i][0] for i in range(1, len(ks)) if abs(r[i] - mu) > 0.6 and abs(r[i - 1] - mu) > 0.6 and ks[i][0] == ks[i - 1][0]}
    if not odd: return dict(tgt)
    chs = sorted({c + d for c in odd for d in (-1, 0, 1)})
    out = {k: tgt[k] for k in src if k in t_ok and k[0] not in chs}
    runs, run = [], []
    for c in chs:                                                        # contiguous runs of chapters to realign
        if run and c != run[-1] + 1: runs.append(run); run = []
        run.append(c)
    if run: runs.append(run)
    for run in runs:
        A = sorted(k for k in src if k[0] in run); R = sorted(k for k in t_ok if k[0] in run)
        for ks, rs in _pair(src, t_ok, A, R):
            text = " ".join(t_ok[k] for k in rs)
            if not ks: continue
            if not text: MISSING.extend(ks); continue
            if len(ks) == 1: out[ks[0]] = text; continue
            la = [_letters(src[k]) for k in ks]; tot, cut, a = sum(la), 0, 0
            for n_, k in enumerate(ks):
                cut += la[n_]
                b = len(text) if n_ == len(ks) - 1 else _snap(text, cut / tot, _kind(src[k] + " X", len(src[k])), a)
                out[k] = text[a:b].strip(); a = b
    return out

def psalm_titles(tgt):
    """A translation that folds a psalm's superscription into verse 1 (Reina-Valera: "Salmo de David, cuando huía de delante
    de Absalom su hijo. ¡OH Jehová …") gets it split off where the psalm proper begins, its first word in capitals.
    Only psalms whose ASV has a superscription (USFM \\d). Returns {psalm: title}; verse 1 keeps the rest."""
    out = {}
    for c in parse_titles(ROOT / "ref" / "eng-asv" / FILES["PSA"]):
        t = tgt.get((c, 1), "")
        m = re.search(L["psalm_title"], t)                  # es: "A JEHOVÁ llamé" (a one-letter word too)
        if m and m.start() > 0:
            out[c] = t[:m.start()].strip(); tgt[(c, 1)] = t[m.start():].strip()
    return out

def d_titles(path):
    """{psalm: superscription} from the \\d lines of a USFM file (a text that keeps them out of verse 1, as the ASV does)."""
    s = pathlib.Path(path).read_text(encoding="utf-8")
    out = {}
    for c, body in re.findall(r"\\c (\d+)(.*?)(?=\\c \d+|\Z)", s, flags=re.S):
        m = re.search(r"^\\d (.*)", body.split("\\v ", 1)[0], flags=re.M | re.S)
        if m:
            t = re.sub(r"\\f .*?\\f\*", "", m.group(1), flags=re.S)
            t = re.sub(r"\\\+?w ([^|\\]*)\|[^\\]*\\\+?w\*", r"\1", t)
            out[int(c)] = re.sub(r"\s+", " ", re.sub(r"\\[a-z0-9+]+\*?", "", t)).strip().replace("\u2019", "'").replace("\u2018", "'")
    return out

def parse_titles(path):
    """The psalms that have a superscription (a \\d line before verse 1) in a USFM file."""
    s = pathlib.Path(path).read_text(encoding="utf-8")
    return [int(c) for c, body in re.findall(r"\\c (\d+)(.*?)(?=\\c \d+|\Z)", s, flags=re.S)
            if re.search(r"^\\d ", body.split("\\v ", 1)[0], flags=re.M)]

def key(ref):
    c, v = ref.split(":"); return int(c), int(v)

class Cut(str):
    """A cut of a translated verse that still answers the plans in ASV words: index/find and slicing work on the ASV text
    of the same cut (a plan that cuts again by an English phrase gets ASV text back and hands it to v(), which maps it).
    Everything else (strip, len, printing) is the translation."""
    def __new__(cls, text, en):
        o = super().__new__(cls, text); o.en = en; return o
    def index(self, *a): return self.en.index(*a)
    def find(self, *a): return self.en.find(*a)
    def rfind(self, *a): return self.en.rfind(*a)
    def __getitem__(self, i): return self.en[i]

class Book:
    def __init__(self, code):
        self.code = code
        self.src = self.verses = parse(ROOT / "ref" / "eng-asv" / FILES[code])   # the ASV: plans find their words here
        self.borrowed = []                   # verses taken from FALLBACK (listed in coverage.md)
        if LANG == "en": self.tgt = self.src
        else:
            tid = L["text"]; raw = parse(ROOT / "ref" / tid / files(tid)[code])
            self.tgt = align(self.src, raw)
            rules = langs.versemap(LANG).get(code, [])
            for (c, a, b), (tc, tv) in rules:
                for n in range(a, b + 1): self.tgt[(c, n)] = raw[(tc, tv + n - a)]
            if code == "PSA":                # superscriptions: the text's own \d lines, else split off verse 1
                self.titles = d_titles(ROOT / "ref" / tid / files(tid)[code]) or (psalm_titles(self.tgt) if L.get("psalm_title") else {})
            ruled = {(c, n) for (c, a, b), _ in rules for n in range(a, b + 1)}
            lost = [k for k in self.src if not self.tgt.get(k, "").strip() or (rules and k[0] in {r[0][0] for r in rules} and k not in ruled)]
            if lost and L.get("fallback"):
                fb = parse(ROOT / "ref" / L["fallback"] / files(L["fallback"])[code])
                for k in lost:
                    if fb.get(k, "").strip(): self.tgt[k] = fb[k]; self.borrowed.append(k)
            if UNSPACED:
                self.tgt = {k: unspace(t) for k, t in self.tgt.items()}
                if code == "PSA": self.titles = {c: unspace(t) for c, t in self.titles.items()}
        self.used = {}                      # (c, v) -> set of character indexes used
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
            en, a_en, b_en = t, a, b
            t = self.tgt.get(k, "")
            a, b = mapped(self.src[k], a, b, t, self.last.get(k))
            self.last[k] = (b_en, b)
            self._mark(k, a, b)
            self.cuts.append((ref, t[a:b].strip()))
            return Cut(t[a:b].strip(), en[a_en:b_en].strip())
        self._mark(k, a, b)
        self.cuts.append((ref, t[a:b].strip()))
        return t[a:b].strip()

    def span(self, refs):
        """'1:1-3' or '2:24' -> whole verses joined with spaces."""
        c, vs = refs.split(":")
        a, _, b = vs.partition("-")
        return " ".join(self.v(f"{c}:{n}") for n in range(int(a), int(b or a) + 1))

    def text(self):
        return " ".join(self.tgt[k] for k in sorted(self.tgt))

    def coverage(self, chapters, span=None):
        """[(ref, status, share)] for every verse of the given chapters; span=("24:1", "25:18") limits it to a run of
        verses, for a manga chapter that starts or ends inside a Bible chapter."""
        rows = []
        lo, hi = (key(span[0]), key(span[1])) if span else ((0, 0), (999, 999))
        for k in sorted(k for k in self.tgt if k[0] in chapters and lo <= k <= hi):
            t = self.tgt[k]
            letters = [i for i, ch in enumerate(t) if not ch.isspace()]
            got = self.used.get(k, set())
            share = sum(1 for i in letters if i in got) / max(1, len(letters))
            st = "full" if share > 0.97 else ("partial" if share > 0 else "omitted")
            rows.append((f"{k[0]}:{k[1]}", st, share))
        return rows
