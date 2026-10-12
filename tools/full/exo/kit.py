"""Page helpers for the Exodus volume.

talk() is Genesis chapter 14's dialogue panel (a close-up face, and beside it a column of captions and balloons), with one
change: a short line ("Go.", "A rod.") gets a balloon sized to its words instead of the full column width."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import re
import mk
from fx import new, vref, cap, balloon, god, page
from genesis.ch02 import rows
from genesis.ch02 import W1
from genesis.ch04 import fc

def song(text, pos, size=15, maxw=None, color="#D7261E"):
    """A line of a song (the Song of Moses, Miriam's answer): a cream box with a red double rule down the left, Archivo
    Narrow like a balloon but square, so a sung line reads apart from both narration and speech."""
    mw = f" max-width: {maxw}px;" if maxw else ""
    return (f'    <div style="position: absolute; {pos};{mw} padding: 10px 14px 10px 18px; background: #FFF8E6; color: #0D0D0F; border: 2.5px solid #0D0D0F; '
            f'box-shadow: inset 6px 0 0 #FFF8E6, inset 10px 0 0 {color}, 4px 4px 0 #0D0D0F; font-family: \'Archivo Narrow\', sans-serif; font-weight: 700; '
            f'font-size: {size}px; line-height: 1.2; letter-spacing: 0.02em; text-transform: uppercase">{text}</div>\n')

def law(heading, text, ref, svg="", size=None, accent="#FFD23F", cell=490, w=336, lead="", span=False):
    """One cell of a page of ordinances (Exodus 21–23): a Voice box (God's words, indigo with the gold inner rule) with a
    pictogram above (svg in a 320 x 100 viewBox, standing on the cell's ground line and filling whatever height the words
    leave), a heading tag and the verse label (both data-label). size=None sizes the words to the cell (cell = its height in px).
    lead = a narration lead-in ("And Jehovah spake unto Moses, saying,") set as a small caption line above the Voice words;
    span = the cell spans both columns of its grid."""
    if size is None:                              # as large as the cell allows: the words take ~60% of the height, the pictogram the rest
        size = max(12.5, min(24, round((w * (cell - 150 - (34 if lead else 0)) / (0.62 * len(text))) ** 0.5 * 2) / 2))
    pic = (f'<div style="position: relative; flex: 1 1 0; min-height: 70px; max-height: {300 if w > 400 else 220}px; background: #2A2458; border-bottom: 2px solid {accent}">'
           f'<svg viewBox="0 0 320 100" preserveAspectRatio="xMidYMax meet" style="position: absolute; inset: 0; width: 100%; height: 100%">{svg}</svg></div>' if svg else "")
    return (f'\n    <div style="position: relative; min-height: 0; overflow: hidden; border: 3px solid #0D0D0F; background: #12113A; color: #F3EFE6; box-shadow: inset 0 0 0 4px #12113A, inset 0 0 0 5.5px {accent}; display: flex; flex-direction: column{"; grid-column: span 2" if span else ""}">'
            f'{pic}'
            f'\n      <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px; padding: 8px 12px 0"><span data-label style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: {accent}">{heading}</span>'
            f'<span data-label style="font-size: 9px; font-weight: 600; letter-spacing: 0.18em; white-space: nowrap; opacity: 0.8">{ref}</span></div>'
            + (f'\n      <div style="margin: 6px 12px 0; align-self: flex-start; padding: 3px 7px; background: #F3EFE6; color: #0D0D0F; font-size: 9.5px; font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase">{lead}</div>' if lead else "")
            + f'\n      <div style="padding: 6px 12px 12px; font-family: Anton, sans-serif; font-size: {size}px; line-height: 1.18; letter-spacing: 0.04em; text-transform: uppercase">{text}</div>\n    </div>')

def talk(tok, h, bg, lines, w=W1, flip=False, ref=None, size=12.5, extra=""):
    """lines is a list of ("cap", text) or ("say", text) in reading order."""
    full = w > 400
    left = 300 if full else 140
    side = f"left: {left}px" if not flip else "left: 12px"
    bw = (w - left - 14) if not flip else (w - 314 if full else w - 154)
    o, y = [], 12
    for kind, text in lines:
        n = len(text)
        if kind == "cap":
            o.append(cap(text, f"{side}; top: {y}px", size=10 if not full else 10.5, maxw=bw))
            y += 34 + 15 * (n // (bw // 7 or 1))
        else:
            long_ = n > 160                       # long speeches get a deeper oval so the corners don't cut the text
            pad = (f"{min(48, 18 + n // 12)}px 40px" if full else f"{min(36, 16 + n // 12)}px 26px") if long_ else ("18px 24px" if full else "16px 18px")
            width = min(bw, max(110, int(n * size * 0.62) + 60))
            o.append(balloon(text, f"{side}; top: {y}px", width, size=size if full else size - 1, pad=pad))
            y += 50 + 17 * (n // max(1, (bw - 40) // 7)) + (n // 6 if long_ else 0)
    if ref: o.append(vref(ref, "left: 12px; bottom: 12px" if not flip else "right: 12px; bottom: 12px"))
    return new(bg, w, h, fc(tok, h, w=w, flip=flip), "".join(o) + extra)


# ---- blueprint pages (chapters 9, 11, 12) ------------------------------------------------------------------
# items: (verse label "28:1–2", words, drawing f(w, h), heading or None); words is a list of ("god" | "cap" | "nar", text):
# "god" = God's words in a Voice box, "cap" = a short lead-in caption, "nar" = narration set large in a caption box.
BP_INK = "#0B1A2E"

def nchars(words): return sum(len(t) for _, t in words)

def bp_panel(h, label_, words, art, extra="", code="EX"):
    """One blueprint panel: the drawing, and in the left half the words, sized to fit the panel."""
    bw = 380; n = nchars(words)
    size = max(11.5, min(19, (bw * (h - 60) / (0.6 * n)) ** 0.5 * 0.82))
    o, y = [], 34
    for kind, text in words:
        if kind == "cap":
            o.append(cap(text, f"left: 12px; top: {y}px", size=10.5, maxw=bw)); y += 38
        elif kind == "nar":
            o.append(cap(text, f"left: 12px; top: {y}px", size=round(size * 0.82 * 2) / 2, maxw=bw)); y += 34 + int(len(text) * size * 0.82 * 0.68 / bw) * size * 1.25
        elif kind == "say":                    # a man's long speech: a white speech box with rounded corners
            o.append(balloon(text, f"left: 12px; top: {y}px", bw, size=round(size * 0.86 * 2) / 2, pad="12px 16px").replace("border-radius: 50%", "border-radius: 22px"))
        else:
            o.append(god(text, f"left: 12px; top: {y}px", size=round(size * 2) / 2, maxw=bw))
    ah = min(h, 520)                          # keep each drawing wide: a taller panel gets the grid above it and the drawing at the foot
    if ah == h: svg = art(W1, h)
    else:                                      # the drawing's title label stays at the top of the panel
        a = art(W1, ah); m = re.search(r'<text x="14\.0" y="18\.0"[^>]*>[^<]*</text>', a)
        top = m.group(0) if m else ""
        svg = _grid(W1, h) + top + f'<g transform="translate(0 {h - ah})">{a.replace(top, "", 1) if top else a}</g>'
    return new(BP_INK, W1, h, svg, "".join(o) + vref(code + " " + label_, "right: 8px; top: 8px") + extra)

def _grid(w, h):
    from exo.art8 import bp
    return bp(w, h)

def bp_pack(items, budget=1500, most=3):
    pages, cur, chars = [], [], 0
    for it in items:
        n = nchars(it[1])
        if cur and (chars + n > budget or len(cur) == most or it[3]) and not (n < 150 and not it[3]):   # a short tail verse stays with its page
            pages.append(cur); cur, chars = [], 0
        cur.append(it); chars += n
    if cur: pages.append(cur)
    return pages

def span_label(group):
    a = group[0][0].split("–")[0]; ca = a.split(":")[0]
    cb, vb = group[-1][0].split(":"); vb = vb.split("–")[-1]
    return f"{a}–{vb}" if ca == cb else f"{a}–{cb}:{vb}"

def blueprints(items, prefix, start, default_head, budget=1500, end="", book="Exodus"):
    """Pack items into blueprint pages; returns [(file name, board title, page fn)], numbered from start. Each panel's height
    is in proportion to its words; a chapter stamp goes on the panel where a Bible chapter begins; end = overlay HTML for the
    very last panel (a つづく box)."""
    out = []; groups = bp_pack(items, budget)
    for k, group in enumerate(groups):
        total = sum(nchars(it[1]) for it in group); gaps = 12 * (len(group) - 1)
        room = 1022 - gaps; low = min(190, room // len(group))
        hs = [max(low, round(room * nchars(it[1]) / total)) for it in group]
        while sum(hs[:-1]) > room - low: hs[hs.index(max(hs[:-1]))] -= 10      # leave the last panel at least `low`
        hs[-1] = None
        t, h = rows(*hs)
        stamp = lambda lab: mk.stamp(int(lab.split(":")[0]), "right: 14px; bottom: 14px") if lab.split(":")[1].split("–")[0] == "1" else ""
        last = k == len(groups) - 1
        body = "".join(bp_panel(hh, it[0], it[1], it[2], stamp(it[0]) + (end if last and i == len(group) - 1 else ""), code=_BK.get(book, "EX")) for i, (hh, it) in enumerate(zip(h, group)))
        head = group[0][3] or default_head
        title = f"{book} {span_label(group)} — {head}"
        slug = re.sub(r"[^A-Za-z]", "", head.title())[:18]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {head}", (lambda title=title, t=t, body=body, n=start + k: page(title, t, body, n))))
    return out


# ---- law pages (Leviticus) -------------------------------------------------------------------------------------------
_ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")
_BK = {"Leviticus": "LEV", "Exodus": "EX", "Numbers": "NUM", "Deuteronomy": "DEUT"}
_SP = {}
def set_book(G):
    """law_pages() cuts text from this book (set by the volume package)."""
    _SP["G"] = G
def _sp(refs): return _SP["G"].span(refs)

def law_pages(items, prefix, start, default_head, title_book="Leviticus", budget=1450, most=6, end=""):
    """Pack law cells into pages. items: (heading, refs "1:2-4", pictogram f(p) -> svg or None, lead text or "", page head
    or None). A page holds up to `most` cells and about `budget` characters; a page head starts a new page. Cells sit two
    to a row (one to a row when a page has only one or two long cells); an odd last cell spans both columns. The lead, if
    the cell's text begins with it, is lifted out into its own caption line. Returns [(file name, board title, page fn)]."""
    from genesis.ch02 import grid
    pages, cur, chars = [], [], 0
    for it in items:
        n = len(_sp(it[1]))
        heading_break = it[4] and (len(cur) >= 3 or chars >= 700)      # a page head starts a new page unless this page is still short
        if cur and (chars + n > budget or len(cur) == most or heading_break):
            pages.append(cur); cur, chars = [], 0
        cur.append(it); chars += n
    if cur: pages.append(cur)
    if len(pages) > 1 and len(pages[-1]) == 1 and len(pages[-2]) < most and len(_sp(pages[-1][0][1])) < 450:
        tail = pages.pop(); pages[-1] += tail                    # no lone short cell at the end
    out = []
    for k, group in enumerate(pages):
        n = len(group); one = n == 1 or (n == 2 and sum(len(_sp(it[1])) for it in group) > 500)
        ncol = 1 if one else 2; nrow = n if ncol == 1 else (n + 1) // 2
        cell = (1022 - 12 * (nrow - 1)) // nrow
        cells = []
        for i, (hd, refs, pic, lead, _) in enumerate(group):
            c, vs = refs.split(":"); a, _, b = vs.partition("-")
            span = ncol == 2 and n % 2 == 1 and i == n - 1
            cw = 696 if (ncol == 1 or span) else 336
            uid = f"lw{prefix[-2:]}{k}x{i}"
            svg = (mk.defs(uid, *_ALL) + pic(uid)) if pic else ""
            text = _sp(refs)
            if lead and text.startswith(lead): text = text[len(lead):].strip()
            else: lead = ""
            cell_html = law(hd, text, f"{_BK[title_book]} {c}:{a}" + (f"–{b}" if b else ""), svg, cell=cell, w=cw, lead=lead, span=span)
            if a == "1":                               # a chapter stamp where a Bible chapter begins
                cell_html = cell_html[: cell_html.rfind("</div>")] + mk.stamp(int(c), "right: 10px; top: 10px") + "</div>"
            cells.append(cell_html)
        if end and k == len(pages) - 1:
            cells[-1] = cells[-1][: cells[-1].rfind("</div>")] + end + "</div>"
        head = next((it[4] for it in group if it[4]), None) or default_head
        a0 = group[0][1].split("-")[0]; cl, vl = group[-1][1].split(":"); vl = vl.split("-")[-1]
        rng = a0 if f"{cl}:{vl}" == a0 else (f"{a0}–{vl}" if a0.split(":")[0] == cl else f"{a0}–{cl}:{vl}")
        title = f"{title_book} {rng} — {head}"
        slug = re.sub(r"[^A-Za-z]", "", head.title())[:18]
        body = grid(cells, f"repeat({nrow}, minmax(0, 1fr))", ncol=ncol)
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {head}", (lambda title=title, body=body, num=start + k: page(title, "minmax(0, 1fr)", body, num))))
    return out
