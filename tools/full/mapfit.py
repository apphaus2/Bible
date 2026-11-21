"""Map names that keep clear of each other, in every language.

    pl = Placer(w, h)                      # the drawing's size; names stay inside it
    pl.block(x0, y0, x1, y1)               # something no name may cover (a title box, a key)
    pl.dot(x, y, r)                        # a dot (every dot first, so no name covers one)
    dx, dy, anchor = pl.put(x, y, text, size, ls, [(dx, dy, anchor), ...])   # the first spot that is clear

A name is measured as the language being built will show it (labels.label, BIBLE_LANG), so the German or Russian map gets
spots that fit its own names; the page still carries the English, which build_volume.py translates. IBM Plex Mono is 0.6 em
a letter, plus the letter-spacing; Chinese, Japanese and Korean letters are a full em. put() tries the spots in order and
takes the first that covers no dot, no name already placed and nothing blocked, and stays inside the drawing; if none does,
the one that covers least. AROUND is the usual list of spots about a dot: right, left, above, below, then the corners."""
import re

AROUND = [(8, 4, "start"), (-8, 4, "end"), (0, -10, "middle"), (0, 16, "middle"),
          (7, -6, "start"), (-7, -6, "end"), (7, 13, "start"), (-7, 13, "end")]
_TAB = {}
WIDE = re.compile(r"[ᄀ-ᇿ⺀-鿿가-힯＀-￯]")

def shown(text):
    """The label as the language being built shows it."""
    import asv
    if asv.LANG == "en": return text
    import labels
    return labels.label(labels.norm(text), asv.LANG, _TAB.setdefault(asv.LANG, labels.table(asv.LANG)))

def width(text, size, ls=0.14):
    t = shown(text); wide = len(WIDE.findall(t))
    return ((len(t) - wide) * (0.6 + ls) + wide * (1.0 + ls) - ls) * size

def box(x, y, text, size, ls=0.14, anchor="middle"):
    w = width(text, size, ls); x0 = {"start": x, "end": x - w}.get(anchor, x - w / 2)
    return (x0 - 1.5, y - 0.85 * size - 1.5, x0 + w + 1.5, y + 0.2 * size + 1.5)

def _over(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0]); h = min(a[3], b[3]) - max(a[1], b[1])
    return w * h if w > 0 and h > 0 else 0

class Placer:
    def __init__(self, w, h, margin=3):
        self.w, self.h, self.m = w, h, margin
        self.boxes = []
    def block(self, x0, y0, x1, y1): self.boxes.append((x0, y0, x1, y1))
    def dot(self, x, y, r): self.boxes.append((x - r, y - r, x + r, y + r))
    def cost(self, b):
        out = max(0, self.m - b[0]) + max(0, b[2] - (self.w - self.m)) + max(0, self.m - b[1]) + max(0, b[3] - (self.h - self.m))
        return sum(_over(b, o) for o in self.boxes) + out * 40
    def put(self, x, y, text, size, ls, spots, keep=True):
        """The first of spots (dx, dy, anchor) that is clear, else the one that covers least; keep=False places nothing."""
        best = None
        for s in spots:
            b = box(x + s[0], y + s[1], text, size, ls, s[2]); c = self.cost(b)
            if c == 0: best = (0, s, b); break
            if best is None or c < best[0] - 0.5: best = (c, s, b)
        if keep: self.boxes.append(best[2])
        return best[1]
