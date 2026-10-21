"""Pack a discourse (Deuteronomy, the prophets, the epistles) into pages automatically.

    seg(lines, ref, tok=FACE, bg=BG, art=None, head=None, stamp=None, flip=None, extra="", h=None)
    pages = pack(segments, prefix="DEU-C03-D", start=PG.next(), book="Deuteronomy", end=end_mark(...))
    PG.extend(pages)

Each segment is one panel. lines are speech lines ("cap" / "say" / "god", see speech.py). With tok, the panel is a face
beside the words; with tok=None and art, the words sit at the top of the drawing; with tok=None and no art, the words
are set over the night sky. A segment with h set (and no lines, or few) is a picture panel of that height.
Pages hold up to three panels and about 1,250 characters; a head starts a new page. Panel heights follow the words.
Faces alternate sides from panel to panel unless flip is given. stamp=N puts the chapter stamp on the panel."""
import re, math
from textw import width
import mk
from fx import page, vref
from genesis.ch02 import rows, W1
import speech
from genesis import art as X

def seg(lines, ref, tok=None, bg="#2A1A3A", art=None, head=None, stamp=None, flip=None, extra="", h=None, hi=21):
    return dict(lines=lines or [], ref=ref, tok=tok, bg=bg, art=art, head=head, stamp=stamp, flip=flip, extra=extra, h=h, hi=hi)

def _chars(s): return sum(width(t) for _, t in s["lines"])

def _need(s, w=W1):
    """Panel height the words need at a comfortable size (16px), with a floor for faces and drawings."""
    if s["h"]: return s["h"]
    bw = w - (294 if s["tok"] else 24)
    need = speech._height(s["lines"], bw, 16) + 40
    if s["art"] is not None and s["tok"] is None: need = need / 0.62 + 40
    return max(220 if s["tok"] else 150, need)

def pack(segments, prefix, start, book="Deuteronomy", code="DEUT", budget=1250, most=3, end="", default_head=None, by_need=False, room=1.08, min_size=None):
    """by_need=True also breaks a page when the panels' estimated heights at a comfortable size would not fit (so a page of
    many short speeches does not shrink the type)."""
    groups, cur, chars, need = [], [], 0, 0
    for s in segments:
        n = _chars(s) + (250 if s["h"] else 0)
        nd = _need(s)
        if cur and (chars + n > budget or len(cur) == most or (s["head"] and chars > budget * 0.45) or (by_need and need + nd > 1022 * room - 12 * len(cur))):
            groups.append(cur); cur, chars, need = [], 0, 0
        cur.append(s); chars += n; need += nd
    if cur: groups.append(cur)
    if len(groups) > 1 and len(groups[-1]) == 1 and len(groups[-2]) < most + 1 and _chars(groups[-1][0]) < 700 and not groups[-1][0]["head"]:
        last = groups.pop(); groups[-1] += last     # no lone short panel on the last page (pop first: groups[-2] += groups.pop() stores at the shifted index)
    if min_size:                                   # split any page on which a panel's words would fall below min_size px
        i = 0
        while i < len(groups):
            g = groups[i]
            if len(g) > 1 and min(_sizes(g)) < min_size:
                cut = max(1, len(g) // 2)
                groups[i:i + 1] = [g[:cut], g[cut:]]
                continue
            i += 1
    out, head_now, side = [], default_head or "", False
    for k, g in enumerate(groups):
        needs = [_need(s) for s in g]
        room = 1022 - 12 * (len(g) - 1)
        fixed = [s["h"] for s in g]
        flex_total = sum(nd for nd, fx in zip(needs, fixed) if not fx) or 1
        flex_room = room - sum(fx for fx in fixed if fx)
        hs = [fx if fx else max(150, round(flex_room * nd / flex_total)) for nd, fx in zip(needs, fixed)]
        hs[-1] = None
        t, h = rows(*hs)
        body = []
        for i, (s, hh) in enumerate(zip(g, h)):
            flip = s["flip"] if s["flip"] is not None else side
            if s["tok"]: side = not side
            extra = s["extra"]
            if s["stamp"]:                         # on the face's side, or above the verse label when words span the panel
                pos = (("right" if flip else "left") + ": 14px; top: 12px") if s["tok"] else "right: 14px; bottom: 36px" if s["lines"] else "right: 14px; top: 12px"
                extra += mk.stamp(s["stamp"], pos)
            lines = s["lines"]
            if end and k == len(groups) - 1 and i == len(g) - 1:
                if s["tok"] and lines:                 # beside a face: the end mark closes the column of words, so it never overlaps them
                    lines = lines + [("raw", re.sub(r"position: absolute; (?:(?:left|right|top|bottom): [-\d.]+px; )+", "align-self: flex-end; ", end))]
                else:
                    extra += end
            if s["lines"]:
                art = (s["art"](W1, hh) if callable(s["art"]) else s["art"]) if s["art"] is not None else (X.cosmic(W1, hh) if s["tok"] is None else "")
                body.append(speech.orate(s["tok"], hh, s["bg"], lines, ref=s["ref"], flip=flip, art=art, top=s["tok"] is None and s["art"] is not None, extra=extra, hi=s["hi"]))
            else:
                art = s["art"](W1, hh) if callable(s["art"]) else (s["art"] or "")
                from fx import new
                body.append(new(s["bg"], W1, hh, art, (vref(s["ref"], "right: 12px; bottom: 12px") if s["ref"] else "") + extra))
        for s in g:
            if s["head"]: head_now = s["head"]
        refs = [s["ref"] for s in g if s["ref"] and s["lines"]] or [s["ref"] for s in g if s["ref"]]
        rng = _span(refs, code)
        title = f"{book} {rng} — {head_now}"
        slug = re.sub(r"[^A-Za-z]", "", head_now.title())[:18]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {head_now}", (lambda title=title, t=t, body="".join(body), n=start + k: page(title, t, body, n))))
    return out

def _heights(g):
    needs = [_need(s) for s in g]
    room = 1022 - 12 * (len(g) - 1)
    fixed = [s["h"] for s in g]
    flex_total = sum(nd for nd, fx in zip(needs, fixed) if not fx) or 1
    flex_room = room - sum(fx for fx in fixed if fx)
    hs = [fx if fx else max(150, round(flex_room * nd / flex_total)) for nd, fx in zip(needs, fixed)]
    hs[-1] = room - sum(hs[:-1])
    return hs

def _sizes(g):
    """The type size each panel of a page would get (speech panels only; drawings without words count as large)."""
    out = []
    for s, hh in zip(g, _heights(g)):
        if not s["lines"]: out.append(99); continue
        bw = W1 - (294 if s["tok"] else 24)
        top = s["tok"] is None and s["art"] is not None
        out.append(speech.fit(s["lines"], bw, hh * (0.62 if top else 1), hi=s["hi"]))
    return out

def _span(refs, code):
    """'DEUT 5:1–3', 'DEUT 5:4' ... → '5:1–6'."""
    vs = []
    for r in refs:
        r = r.replace(code + " ", "")
        for part in r.split(", "):
            a, _, b = part.partition("–")
            c = a.split(":")[0]
            vs.append(a)
            if b: vs.append(b if ":" in b else f"{c}:{b}")
    if not vs: return ""
    first, last = vs[0], vs[-1]
    if first == last: return first
    return f"{first}–{last.split(':')[1]}" if first.split(":")[0] == last.split(":")[0] else f"{first}–{last}"
