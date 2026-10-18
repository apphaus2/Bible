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
import mk
from fx import page, vref
from genesis.ch02 import rows, W1
import speech
from genesis import art as X

def seg(lines, ref, tok=None, bg="#2A1A3A", art=None, head=None, stamp=None, flip=None, extra="", h=None, hi=21):
    return dict(lines=lines or [], ref=ref, tok=tok, bg=bg, art=art, head=head, stamp=stamp, flip=flip, extra=extra, h=h, hi=hi)

def _chars(s): return sum(len(t) for _, t in s["lines"])

def _need(s, w=W1):
    """Panel height the words need at a comfortable size (16px), with a floor for faces and drawings."""
    if s["h"]: return s["h"]
    bw = w - (294 if s["tok"] else 24)
    need = speech._height(s["lines"], bw, 16) + 40
    if s["art"] is not None and s["tok"] is None: need = need / 0.62 + 40
    return max(220 if s["tok"] else 150, need)

def pack(segments, prefix, start, book="Deuteronomy", code="DEUT", budget=1250, most=3, end="", default_head=None):
    groups, cur, chars = [], [], 0
    for s in segments:
        n = _chars(s) + (250 if s["h"] else 0)
        if cur and (chars + n > budget or len(cur) == most or (s["head"] and chars > budget * 0.45)):
            groups.append(cur); cur, chars = [], 0
        cur.append(s); chars += n
    if cur: groups.append(cur)
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
            if s["stamp"]: extra += mk.stamp(s["stamp"], ("left" if flip else "right") + ": 14px; top: 12px")
            if end and k == len(groups) - 1 and i == len(g) - 1: extra += end
            if s["lines"]:
                art = (s["art"](W1, hh) if callable(s["art"]) else s["art"]) if s["art"] is not None else (X.cosmic(W1, hh) if s["tok"] is None else "")
                body.append(speech.orate(s["tok"], hh, s["bg"], s["lines"], ref=s["ref"], flip=flip, art=art, top=s["tok"] is None and s["art"] is not None, extra=extra, hi=s["hi"]))
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
