"""Roll pages: lists set as full-width cells (genesis.ch03.clan), one cell per name, border or group of cities, every word
of the verses in the cell. Used for the blessing of the tribes (Deuteronomy 33), the kings Joshua smote (Joshua 12), the
borders and the cities of the tribes (Joshua 13–21), and the like.

    roll_pages([(name, text, ref, accent, head), ...], "JOS-C06-R", PG.next(), "Joshua", tag="THE KINGS · JOSHUA 12")

Cells are packed into pages by estimated height; each page then takes the largest type size (up to 22px) at which its
cells fit, and each row is as tall as its words need."""
import math
from fx import page
from genesis.ch02 import grid
from genesis.ch03 import clan

ROOM = 1022 - 22

def need(text, s):
    return 66 + math.ceil(len(text) / (672 / (s * 0.64))) * s * 1.5

def roll_page(cells, title, n, tag="", hi=22.0):
    """One page of cells (name, text, ref, accent)."""
    room = ROOM - 12 * (len(cells) - 1)
    s = hi
    while s > 10 and sum(need(t, s) for _, t, _, _ in cells) > room: s -= 0.5
    fr = " ".join(f"{need(t, s):.0f}fr" for _, t, _, _ in cells)
    body = grid([clan(nm, t, ref, c, size=s) for nm, t, ref, c in cells], fr, ncol=1)
    if tag:
        body += (f'\n  <div data-label style="position: absolute; left: 26px; right: 26px; top: 8px; text-align: center; font-size: 9px; font-weight: 600; '
                 f'letter-spacing: 0.24em; color: #6B6862">{tag}</div>')
    return page(title, "minmax(0, 1fr)", body, n)

def _span(refs, code):
    a = refs[0].replace(code + " ", "").split("–")[0]
    last = refs[-1].replace(code + " ", "")
    b = last.split("–")[-1]
    if ":" not in b: b = last.split(":")[0] + ":" + b
    if a == b: return a
    return f"{a}–{b.split(':')[1]}" if a.split(":")[0] == b.split(":")[0] else f"{a}–{b}"

def roll_pages(items, prefix, start, book, code, tag="", size=15, most=7, head=""):
    """Pack items (name, text, ref, accent, head-or-None) into pages; returns [(file, board title, fn)] like discourse.pack.
    A page breaks when the cells would not fit at `size` px, after `most` cells, or before an item with a new head."""
    groups, cur = [], []
    for it in items:
        if cur and (len(cur) == most or sum(need(c[1], size) for c in cur + [it]) > ROOM - 12 * len(cur) or (it[4] and it[4] != head)):
            groups.append(cur); cur = []
        cur.append(it)
        if it[4]: head = it[4]
    if cur: groups.append(cur)
    out, h = [], ""
    for k, g in enumerate(groups):
        for it in g:
            if it[4]: h = it[4]; break
        rng = _span([it[2] for it in g], code)
        title = f"{book} {rng} — {h}"
        slug = "".join(ch for ch in h.title() if ch.isalpha())[:18]
        cells = [it[:4] for it in g]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {h}", (lambda cells=cells, title=title, n=start + k: roll_page(cells, title, n, tag))))
    return out
