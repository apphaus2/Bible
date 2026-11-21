"""Map names that keep clear of each other, in every language.

    pl = Placer(w, h)                      # the drawing's size; names stay inside it
    pl.block(x0, y0, x1, y1)               # something no name may cover (a title box, a key)
    pl.dot(x, y, r)                        # a dot (every dot first, so no name covers one)
    dx, dy, anchor = pl.put(x, y, text, size, ls, [(dx, dy, anchor), ...])   # the first spot that is clear
    spots = pl.solve([(x, y, text, size, ls, [(dx, dy, anchor), ...]), ...])  # several names at once

A name is measured as the language being built will show it (labels.label, BIBLE_LANG), so the German or Russian map gets
spots that fit its own names; the page still carries the English, which build_volume.py translates. IBM Plex Mono is 0.6 em
a letter, plus the letter-spacing; Chinese, Japanese and Korean letters are a full em. put() tries the spots in order and
takes the first that covers no dot, no name already placed and nothing blocked, and stays inside the drawing; if none does,
the one that covers least. solve() places names one by one the same way, then again with the crowded ones first, and keeps
the pass that covers least. AROUND is the usual list of spots about a dot: right, left, above, below, then the corners."""
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
    return ((len(t) - wide) * (0.6 + ls) + wide * (1.0 + ls)) * size * 1.03      # as the browser measures it, halo and all

def box(x, y, text, size, ls=0.14, anchor="middle"):
    w = width(text, size, ls); x0 = {"start": x, "end": x - w}.get(anchor, x - w / 2)
    return (x0 - 1.5, y - 0.85 * size - 1.5, x0 + w + 1.5, y + 0.2 * size + 1.5)

def _over(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0]); h = min(a[3], b[3]) - max(a[1], b[1])
    return w * h if w > 0 and h > 0 else 0

class Placer:
    """Covering a name already placed or a blocked box (a title) costs three times as much as covering a dot, so when no
    spot is clear a name settles on a dot's edge rather than on another name."""
    def __init__(self, w, h, margin=3):
        self.w, self.h, self.m = w, h, margin
        self.boxes = []                              # (x0, y0, x1, y1, weight)
    def block(self, x0, y0, x1, y1): self.boxes.append((x0, y0, x1, y1, 3))      # a title or a key: as a name
    def dot(self, x, y, r): self.boxes.append((x - r, y - r, x + r, y + r, 1))
    def cost(self, b, nw=None):
        """nw: what covering a placed name costs (default its weight, 3)."""
        out = max(0, self.m - b[0]) + max(0, b[2] - (self.w - self.m)) + max(0, self.m - b[1]) + max(0, b[3] - (self.h - self.m))
        return sum(_over(b, o) * (nw if nw and o[4] == 3 else o[4]) for o in self.boxes) + out * 400   # cut off by the edge: the worst
    def on_names(self, b): return sum(_over(b, o) for o in self.boxes if o[4] == 3)
    def _best(self, x, y, text, size, ls, spots, nw=None):
        best = None
        for s in spots:
            b = box(x + s[0], y + s[1], text, size, ls, s[2]); c = self.cost(b, nw)
            if c == 0: return 0, s, b
            if best is None or c < best[0] - 0.5: best = (c, s, b)
        return best
    def put(self, x, y, text, size, ls, spots, keep=True):
        """The first of spots (dx, dy, anchor) that is clear, else the one that covers least; keep=False places nothing."""
        c, s, b = self._best(x, y, text, size, ls, spots)
        if keep: self.boxes.append((*b, 3))
        return s
    def put_clear(self, x, y, text, sizes, ls, spots):
        """A name that may be left out (a region): the first of sizes at which some spot covers no placed name, as
        (dx, dy, anchor, size); None if every size would cover one."""
        for size in sizes:
            c, s, b = self._best(x, y, text, size, ls, spots, nw=1000)
            if self.on_names(b) < 1: self.boxes.append((*b, 3)); return (*s, size)
        return None
    def solve(self, items, passes=8):
        """Several names at once: items [(x, y, text, size, ls, spots)], returns the spot of each. Placed one by one as
        put() does; if some stay crowded, those go first on the next pass, and the pass that covers least is kept."""
        fixed, order, best = list(self.boxes), list(range(len(items))), None
        for _ in range(passes):
            self.boxes = list(fixed); got, bad, total = {}, [], 0
            for i in order:
                c, s, b = self._best(*items[i]); got[i] = s; self.boxes.append((*b, 3))
                if c > 0.5: bad.append(i); total += c
            if best is None or total < best[0]: best = (total, got, list(self.boxes))
            if not bad: break
            order = bad + [i for i in order if i not in bad]
        self.boxes = best[2]
        return [best[1][i] for i in range(len(items))]
