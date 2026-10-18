"""Lift the drawn art out of a digest page so the full edition can reuse it.

    panels("digest/genesis/book-01/P05-Eden.dc.html") -> [Art(bg, w, h, svg), ...] in page order
Each Art keeps its own viewBox size; ids inside are renamed with a unique prefix so two lifted panels can
share a page. Only the <svg> drawing (plus any full-panel overlay div, kept as a background layer) is taken: captions,
balloons and sound effects are left behind."""
import re, pathlib, itertools
ROOT = pathlib.Path(__file__).resolve().parents[2]
_n = itertools.count()

class Art:
    def __init__(self, bg, w, h, svg): self.bg, self.w, self.h, self.svg = bg, w, h, svg

def _prefix(svg):
    p = f"r{next(_n)}_"
    ids = set(re.findall(r'id="([^"]+)"', svg))
    for i in sorted(ids, key=len, reverse=True):
        svg = re.sub(rf'id="{re.escape(i)}"', f'id="{p}{i}"', svg)
        svg = re.sub(rf'(href="#|url\(#){re.escape(i)}([")])', rf'\g<1>{p}{i}\2', svg)
    return svg

def panels(rel):
    s = (ROOT / rel).read_text()
    out = []
    for m in re.finditer(r'<div style="position: relative; overflow: hidden; border: 3px solid #0D0D0F; background: ([^"]*)">\s*'
                         r'((?:<div style="position: absolute; inset: 0; background: [^"]*"></div>\s*)*)<svg viewBox="0 0 (\d+) (\d+)"[^>]*>(.*?)</svg>', s, re.S):
        # an overlay div (e.g. rain streaks) becomes an extra background layer on top of the panel's own
        layers = re.findall(r'background: ([^"]*)"', m.group(2)) + [m.group(1)]
        out.append(Art(", ".join(layers), int(m.group(3)), int(m.group(4)), _prefix(m.group(5))))
    return out

def fill(art, align="xMidYMid"):
    """A lifted panel as a drawing for any panel size: f(w, h) -> svg, the old viewBox cropped (slice) to fill w x h
    (align="xMidYMax" keeps the bottom, where the figures stand, when a narrow panel is widened)."""
    return lambda w, h: (f'<svg x="0" y="0" width="{w}" height="{h}" viewBox="0 0 {art.w} {art.h}" preserveAspectRatio="{align} slice">'
                         f'{art.svg}</svg>')
