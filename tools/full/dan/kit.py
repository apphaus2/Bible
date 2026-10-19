"""Line and panel builders for Daniel and the prophets after it (Hosea, Joel and Amos import this too).

    L = Lines(G, "DAN", "Daniel", SPK)       # SPK = {"daniel": ("DANIEL", "#1F5FAD"), ...}
    L.c("1:1")  L.cs("1:1-3")                # narration captions (a cut / whole verses in one box)
    L.s("2:5", "king", frm=…)  L.ss("2:5-6", "king")   # a speaker's words in a song box of his colour
    L.g("…")  L.gs("…")  L.gl("…")  L.gls("…")         # God's words: Voice box (gl/gls keep the poem's lines, a box a verse)
    L.cut("2:3", "said unto them,", "king")  # [caption up to and including the words, the rest as speech]
    L.T(lines, "1:8-9", FACE, bg, who="daniel")         # beside a face, the speaker's name tagged
    L.A(lines, "1:1-2", fn, bg, who=None)    # over a drawing fn(w, h) set just under the words
    L.pack(segs, prefix, start, end=…)       # job.jdiscourse.pack: the fewest pages on which the words stay readable

Panels are job.jdiscourse segments (speaker tags, the share of a drawn panel the words may take)."""
import re
from job.jdiscourse import seg, pack as _pack
from job import jspeech

NIGHT = "#0F0E2A"

def br(t):
    """Keep a poem's lines: a break before each line the ASV starts with a capital after a stop (as job.common.br)."""
    parts = re.split(r"(?<=[,;:.!?]) (?=[A-Z])", t)
    out = [parts[0]]
    for p in parts[1:]:
        if len(out[-1]) < 24 or len(p) < 16: out[-1] += " " + p
        else: out.append(p)
    return "<br>".join(out)

def under(fn, lines, wk=0.7):
    """A drawing fn(w, h) set just under the column of words at the top of its panel."""
    def art(w, h):
        bw = w - 24
        s = jspeech.fit(lines, bw, h * wk)
        k = min(wk, (jspeech._height(lines, bw, s) + 34 + 8) / h)
        return f'<g transform="translate(0 {h * k:.1f})">' + fn(w, h * (1 - k)) + '</g>'
    return art

def refs_of(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]

class Lines:
    def __init__(self, G, code, book, spk):
        self.G, self.code, self.book, self.spk = G, code, book, spk

    # ---- lines --------------------------------------------------------------------------------------------------------
    def v(self, ref, frm=None, to=None, after=None): return self.G.v(ref, frm=frm, to=to, after=after)
    def c(self, ref, frm=None, to=None, after=None): return ("cap", self.v(ref, frm, to, after))
    def cs(self, refs): return ("cap", self.G.span(refs))
    def s(self, ref, who, frm=None, to=None, after=None, poem=False):
        t = self.v(ref, frm, to, after)
        return ("song" + self.spk[who][1], br(t) if poem else t)
    def ss(self, refs, who): return ("song" + self.spk[who][1], self.G.span(refs))
    def sl(self, refs, who): return [("song" + self.spk[who][1], br(self.v(r))) for r in refs_of(refs)]
    def g(self, ref, frm=None, to=None, after=None): return ("god", self.v(ref, frm, to, after))
    def gs(self, refs): return ("god", self.G.span(refs))
    def gl(self, ref, frm=None, to=None, after=None): return ("god", br(self.v(ref, frm, to, after)))
    def gls(self, refs): return [("god", br(self.v(r))) for r in refs_of(refs)]
    def cut(self, ref, at, who="god", poem=False):
        """A verse split after the words `at`: the caption up to them, then the words of `who` ("god" for the Voice box)."""
        rest = self.v(ref, after=at)
        if poem: rest = br(rest)
        return [("cap", self.v(ref, to=at)), ("god", rest) if who == "god" else ("song" + self.spk[who][1], rest)]
    def joined(self, kind, *parts):
        """One box from several cuts: joined("god", ("1:2", "Let there"), "1:3") — a ref alone is the whole verse."""
        return (kind, " ".join(self.v(p) if isinstance(p, str) else self.v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

    # ---- panels -------------------------------------------------------------------------------------------------------
    def label(self, refs):
        a, _, b = refs.partition("-")
        return f"{self.code} {a}" + (f"–{b}" if b else "")
    def _who(self, who): return self.spk[who][:2] if who else None
    def T(self, lines, refs, tok, bg, who=None, **k):
        """Words beside a face."""
        return seg(lines, self.label(refs), tok=tok, bg=bg, who=self._who(who), **k)
    def A(self, lines, refs, fn, bg, who=None, wk=0.5, **k):
        """Words at the top of a drawing fn(w, h), the drawing set just under them."""
        return seg(lines, self.label(refs), bg=bg, art=under(fn, lines, wk), who=self._who(who), wk=wk, **k)
    def N(self, lines, refs, bg=NIGHT, who=None, **k):
        """Words over the night sky."""
        return seg(lines, self.label(refs), bg=bg, who=self._who(who), **k)
    def pack(self, segs, prefix, start, **k):
        k.setdefault("by_need", True)
        k.setdefault("room", 1.3)
        k.setdefault("min_size", 12.5)
        return _pack(segs, prefix, start, book=self.book, code=self.code, **k)
