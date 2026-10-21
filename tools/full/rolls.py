"""Roll pages: lists set as full-width cells (genesis.ch03.clan), one cell per name, border or group of cities, every word
of the verses in the cell. Used for the blessing of the tribes (Deuteronomy 33), the kings Joshua smote (Joshua 12), the
borders and the cities of the tribes (Joshua 13–21), and the like.

    roll_pages([(name, text, ref, accent, head), ...], "JOS-C06-R", PG.next(), "Joshua", tag="THE KINGS · JOSHUA 12")

Cells are packed into pages by estimated height; each page then takes the largest type size (up to 22px) at which its
cells fit, and each row is as tall as its words need."""
import math
from fx import page
from asv import ems
from genesis.ch02 import grid
from genesis.ch03 import clan

ROOM = 1022 - 22

def need(text, s, ncol=1):
    width = (672 - 12 * (ncol - 1)) / ncol - (0 if ncol == 1 else 6)
    return 66 + math.ceil(ems(text, 0.64) / (width / (s * 0.64))) * s * 1.5

def _rows(cells, s, ncol):
    """Row heights: each row as tall as its tallest cell."""
    hs = [need(t, s, ncol) for _, t, _, _ in cells]
    return [max(hs[i:i + ncol]) for i in range(0, len(hs), ncol)]

def roll_page(cells, title, n, tag="", hi=22.0, ncol=1, end=""):
    """One page of cells (name, text, ref, accent), in ncol columns."""
    nrow = math.ceil(len(cells) / ncol)
    room = ROOM - 12 * (nrow - 1) - (70 if end else 0)
    s = hi
    while s > 10 and sum(_rows(cells, s, ncol)) > room: s -= 0.5
    rows_ = _rows(cells, s, ncol)
    if end: rows_[-1] += 70
    fr = " ".join(f"{x:.0f}fr" for x in rows_)
    body = grid([clan(nm, t, ref, c, size=s) for nm, t, ref, c in cells], fr, ncol=ncol)
    if tag:
        body += (f'\n  <div data-label style="position: absolute; left: 26px; right: 26px; top: 8px; text-align: center; font-size: 9px; font-weight: 600; '
                 f'letter-spacing: 0.24em; color: #6B6862">{tag}</div>')
    return page(title, "minmax(0, 1fr)", body + end, n)

def _span(refs, code):
    a = refs[0].replace(code + " ", "").split("–")[0]
    last = refs[-1].replace(code + " ", "")
    b = last.split("–")[-1]
    if ":" not in b: b = last.split(":")[0] + ":" + b
    if a == b: return a
    return f"{a}–{b.split(':')[1]}" if a.split(":")[0] == b.split(":")[0] else f"{a}–{b}"

def roll_pages(items, prefix, start, book, code, tag="", size=13, most=8, head="", ncol=1, end=""):
    """Pack items (name, text, ref, accent, head-or-None) into pages; returns [(file, board title, fn)] like discourse.pack.
    A page breaks when the cells would not fit at `size` px, after `most` cells, or before an item with a new head."""
    groups, cur = [], []
    for it in items:
        if cur and (len(cur) == most or sum(_rows([c[:4] for c in cur + [it]], size, ncol)) > ROOM - 12 * (math.ceil((len(cur) + 1) / ncol) - 1) or (it[4] and it[4] != head)):
            groups.append(cur); cur = []
        cur.append(it)
        if it[4]: head = it[4]
    if cur: groups.append(cur)
    def fits(g, sz): return sum(_rows([c[:4] for c in g], sz, ncol)) <= ROOM - 12 * (math.ceil(len(g) / ncol) - 1)
    if len(groups) > 1 and len(groups[-1]) <= ncol and not groups[-1][0][4] and fits(groups[-2] + groups[-1], 11):
        last = groups.pop(); groups[-1] = groups[-1] + last          # no lone cell on the last page
    out, h = [], ""
    for k, g in enumerate(groups):
        for it in g:
            if it[4]: h = it[4]; break
        rng = _span([it[2] for it in g], code)
        title = f"{book} {rng} — {h}"
        slug = "".join(ch for ch in h.title() if ch.isalpha())[:18]
        cells = [it[:4] for it in g]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {h}", (lambda cells=cells, title=title, n=start + k, e=(end if k == len(groups) - 1 else ""): roll_page(cells, title, n, tag, ncol=ncol, end=e))))
    return out

def verse_cells(G, code, c, a, b, name, accent, head=None, budget=520, brk=None):
    """Roll items for verses c:a–b grouped into cells of about `budget` characters (a cell also ends after a verse matching
    the regex `brk`, e.g. r"villages[.]$" for the city lists). Each cell is named `name`, or name(first verse) if callable."""
    import re
    out, cur, n = [], [], 0
    for k in range(a, b + 1):
        t = G.verses[(c, k)]
        if cur and n + len(t) > budget:
            out.append(cur); cur, n = [], 0
        cur.append(k); n += len(t)
        if brk and re.search(brk, t): out.append(cur); cur, n = [], 0
    if cur: out.append(cur)
    items = []
    for i, g in enumerate(out):
        ref = f"{c}:{g[0]}" + (f"-{g[-1]}" if len(g) > 1 else "")
        text = G.span(ref)
        label = f"{code} {c}:{g[0]}" + (f"–{g[-1]}" if len(g) > 1 else "")
        items.append((name(g[0]) if callable(name) else name, text, label, accent, head if i == 0 else None))
    return items
