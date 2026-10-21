"""Page layout for the Psalms: discourse.pack and speech.orate (copied here, since shared modules stay untouched) with two
additions for poetry:

  ("song", text)  a verse in a song box, its poetic lines (from psa.text) set one to a row (text holds "\\n" between lines)
  ("head", (num, title, extra))  a psalm's head at the top of its first panel: a red PSALM N block and the superscription
                  (a data-label, cut from ref/eng-asv by psa.text: superscriptions are not verses, so the ASV check skips them)

    seg(lines, ref, tok=FACE, bg=BG, art=None, head=None, title=None, …)
    pages = pack(segments, prefix, start, book="Psalms", code="PS", end=end_mark(...))

A segment with head starts a new page when the page is already more than `brk` full; title names the page (board title)
without forcing a break."""
import re, math, html
import mk
from asv import ems
from fx import page, vref, new
from genesis.ch02 import rows, W1
from genesis.ch04 import fc
from genesis import art as X

def seg(lines, ref, tok=None, bg="#2A1A3A", art=None, head=None, title=None, stamp=None, flip=None, extra="", h=None, hi=17.5):
    return dict(lines=lines or [], ref=ref, tok=tok, bg=bg, art=art, head=head, title=title or head, stamp=stamp, flip=flip, extra=extra, h=h, hi=hi)

# ---- the column of words ---------------------------------------------------------------------------------------------------
def _hd_lines(hd, bw):
    num, title, extra = hd
    t = (extra + " · " if extra else "") + (title or "")
    if not t: return 0
    cpl = max(10, (bw - 150) / 7.0)
    return math.ceil(ems(t, 0.6) / cpl)

def _height(lines, bw, s):
    tot = 0
    for kind, text in lines:
        if kind == "raw":
            tot += 40; continue
        if kind == "head":
            tot += max(36, _hd_lines(text, bw) * 14.5 + 12) + 9; continue
        if kind == "cap":
            fs = min(11.5, max(9.5, s * 0.66)); cpl = max(8, (bw - 24) / (fs * 0.64))
            tot += math.ceil(ems(text, 0.64) / cpl) * fs * 1.45 + 20
        elif kind == "song":
            cpl = max(6, (bw - 40) / (s * 0.56))
            tot += sum(math.ceil(ems(x, 0.56) / cpl) for x in text.split("\n")) * s * 1.18 + 20
        elif kind == "say":
            cpl = max(6, (bw - 36) / (s * 0.56)); tot += math.ceil(ems(text, 0.56) / cpl) * s * 1.16 + 30
        else:
            cpl = max(6, (bw - 36) / (s * 0.53))
            tot += sum(math.ceil(ems(x, 0.53) / cpl) for x in text.split("\n")) * s * 1.15 + 32
        tot += 8
    return tot

def fit(lines, bw, h, hi=21, lo=9.5):
    s = hi
    while s > lo and _height(lines, bw, s) > h - 34:
        s -= 0.5
    return s

def _br(text): return "<br>".join(text.split("\n"))

def _cap(text, fs):
    return (f'<div style="align-self: flex-start; padding: 6px 10px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: {fs}px; '
            f'font-weight: 600; line-height: 1.45; letter-spacing: 0.03em; text-transform: uppercase">{text}</div>')

def _say(text, s, side):
    notch = (f'<div style="position: absolute; {side}: -8px; top: 16px; width: 13px; height: 13px; background: #ffffff; '
             f'border-{side}: 2.5px solid #0D0D0F; border-bottom: 2.5px solid #0D0D0F; transform: rotate({45 if side == "left" else -135}deg)"></div>')
    return (f'<div style="position: relative">{notch}<div style="padding: 11px 16px 12px; background: #ffffff; color: #0D0D0F; border: 2.5px solid #0D0D0F; border-radius: 18px; '
            f"font-family: 'Archivo Narrow', sans-serif; font-weight: 700; font-size: {s}px; line-height: 1.16; text-transform: uppercase\">{text}</div></div>")

def _song(text, s, color="#7A3BA8"):
    """A verse of a psalm: a cream box with a coloured double rule down the left, one poetic line to a row."""
    return (f'<div style="padding: 5px 12px 5px 20px; background: #FFF8E6; color: #0D0D0F; border: 2.5px solid #0D0D0F; '
            f'box-shadow: inset 6px 0 0 #FFF8E6, inset 10px 0 0 {color}, 3px 3px 0 #0D0D0F; font-family: \'Archivo Narrow\', sans-serif; font-weight: 700; '
            f'font-size: {s}px; line-height: 1.18; letter-spacing: 0.02em; text-transform: uppercase">{_br(text)}</div>')

def _god(text, s):
    return (f'<div style="padding: 12px 16px; background: #12113A; color: #F3EFE6; box-shadow: inset 0 0 0 4px #12113A, inset 0 0 0 5.5px #FFD23F; '
            f'font-family: Anton, sans-serif; font-size: {s}px; line-height: 1.15; letter-spacing: 0.04em; text-transform: uppercase">{_br(text)}</div>')

def kanji(n):
    """Kanji numerals up to 199 (mk.kanji_num stops at 99): 23 → 二十三, 119 → 百十九."""
    return ("百" if n >= 100 else "") + (mk.kanji_num(n % 100) if n % 100 else "")

def _head(hd):
    num, title, extra = hd
    kan = f'<span style="display: block; font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 9px; letter-spacing: 0.1em; color: #FFD23F; margin-top: 2px">第{kanji(num)}篇</span>' if isinstance(num, int) else ""
    lab = f"PSALM {num}" if isinstance(num, int) else num
    t = ""
    if extra: t += f'<span style="color: #FF8A6A">{extra}</span>' + (" · " if title else "")
    if title: t += html.escape(title, quote=False)
    tx = (f'<span data-label style="align-self: center; padding: 5px 12px 5px 10px; color: #F3EFE6; font-size: 10px; font-weight: 600; line-height: 1.4; '
          f'letter-spacing: 0.08em; text-transform: uppercase">{t}</span>') if t else ""
    return (f'<div data-label style="align-self: flex-start; display: flex; align-items: stretch; max-width: 100%; background: #12113A; border: 2px solid #0D0D0F; box-shadow: 3px 3px 0 #0D0D0F">'
            f'<span data-label style="flex: none; padding: 4px 10px 3px; background: #D7261E; color: #F3EFE6; font-family: Anton, sans-serif; font-size: 21px; line-height: 1.05; letter-spacing: 0.05em; text-align: center">{lab}{kan}</span>'
            f'{tx}</div>')

def column(lines, bw, h, side="left", hi=21, color="#7A3BA8"):
    s = fit(lines, bw, h, hi=hi)
    fs = min(11.5, max(9.5, s * 0.66))
    items = []
    for kind, text in lines:
        items.append(text if kind == "raw" else _head(text) if kind == "head" else _cap(text, fs) if kind == "cap" else _say(text, s, side) if kind == "say"
                     else _song(text, s, color) if kind == "song" else _god(text, s))
    return items

def orate(tok, h, bg, lines, w=W1, flip=False, ref=None, hi=21, art="", extra="", face_w=None, top=None, color="#7A3BA8"):
    if tok is None:
        left, bw = 12, w - 24
        svg = art
    else:
        fw = face_w or (270 if w > 400 else 130)
        bw = w - fw - 24
        left = fw + 12 if not flip else 12
        svg = art + fc(tok, h, w=w, flip=flip)
    top = bool(top) and tok is None
    items = column(lines, bw, h * (TOP if top else 1), side="left" if not flip else "right", hi=hi, color=color)
    col = (f'\n    <div style="position: absolute; left: {left}px; top: {12 if top else 12}px; bottom: 12px; width: {bw}px; display: flex; flex-direction: column; justify-content: {"flex-start" if top else "center"}; gap: 8px">'
           + "".join(items) + '</div>\n')
    r = vref(ref, ("left: 12px; bottom: 12px" if not flip else "right: 12px; bottom: 12px") if tok else "right: 12px; bottom: 12px") if ref else ""
    return new(bg, w, h, svg, col + r + extra)

NEED_SIZE = 14
TOP = 0.7          # words over a drawing use the top part of the panel; the drawing keeps the rest

# ---- packing segments into pages -------------------------------------------------------------------------------------------
def _chars(s): return sum((ems(t) if isinstance(t, str) else 60) for _, t in s["lines"])

def _need(s, w=W1):
    if s["h"]: return s["h"]
    bw = w - (294 if s["tok"] else 24)
    need = _height(s["lines"], bw, NEED_SIZE) + 40
    if s["art"] is not None and s["tok"] is None: need = need / TOP + 30
    return max(220 if s["tok"] else 150, need)

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
    out = []
    for s, hh in zip(g, _heights(g)):
        if not s["lines"]: out.append(99); continue
        bw = W1 - (294 if s["tok"] else 24)
        top = s["tok"] is None and s["art"] is not None
        out.append(fit(s["lines"], bw, (hh - 6) * (TOP if top else 1), hi=s["hi"]))
    return out

def pack(segments, prefix, start, book="Psalms", code="PS", budget=1250, most=3, end="", by_need=True, room=0.94, min_size=13, brk=0.7):
    groups, cur, chars, need = [], [], 0, 0
    for s in segments:
        n = _chars(s) + (250 if s["h"] else 0)
        nd = _need(s)
        if cur and (chars + n > budget or len(cur) == most or (s["head"] and chars > budget * brk) or (by_need and need + nd > 1022 * room - 12 * len(cur))):
            groups.append(cur); cur, chars, need = [], 0, 0
        cur.append(s); chars += n; need += nd
    if cur: groups.append(cur)
    if len(groups) > 1 and len(groups[-2]) + len(groups[-1]) <= most and sum(_chars(x) for x in groups[-1]) < 520 and not groups[-1][0]["head"]:
        last = groups.pop(); groups[-1] += last
    elif len(groups) > 1 and len(groups[-1]) == 1 and len(groups[-2]) >= 2 and _chars(groups[-1][0]) < 700:
        groups[-1].insert(0, groups[-2].pop())          # no lone panel on the last page: it takes the panel before it
    if min_size:
        i = 0
        while i < len(groups):
            g = groups[i]
            if len(g) > 1 and min(_sizes(g)) < min_size:
                cut = max(1, len(g) // 2)
                groups[i:i + 1] = [g[:cut], g[cut:]]
                continue
            i += 1
    out, title_now, side = [], "", False
    for k, g in enumerate(groups):
        hs = _heights(g)
        hs[-1] = None
        t, h = rows(*hs)
        body = []
        for i, (s, hh) in enumerate(zip(g, h)):
            flip = s["flip"] if s["flip"] is not None else side
            if s["tok"]: side = not side
            extra = s["extra"]
            if s["stamp"]:
                pos = (("right" if flip else "left") + ": 14px; top: 12px") if s["tok"] else "right: 14px; bottom: 36px"
                extra += mk.stamp(s["stamp"], pos)
            lines = s["lines"]
            if end and k == len(groups) - 1 and i == len(g) - 1:
                if s["tok"] and lines:
                    lines = lines + [("raw", re.sub(r"position: absolute; (?:(?:left|right|top|bottom): [-\d.]+px; )+", "align-self: flex-end; ", end))]
                else:
                    extra += end
            if s["lines"]:
                art = (s["art"](W1, hh) if callable(s["art"]) else s["art"]) if s["art"] is not None else (X.cosmic(W1, hh) if s["tok"] is None else "")
                body.append(orate(s["tok"], hh, s["bg"], lines, ref=s["ref"], flip=flip, art=art, top=s["tok"] is None and s["art"] is not None, extra=extra, hi=s["hi"]))
            else:
                art = s["art"](W1, hh) if callable(s["art"]) else (s["art"] or "")
                body.append(new(s["bg"], W1, hh, art, (vref(s["ref"], "right: 12px; bottom: 12px") if s["ref"] else "") + extra))
        firsts = [s["title"] for s in g if s["title"]]
        page_title = g[0]["title"] or title_now or (firsts[0] if firsts else "")
        if firsts: title_now = firsts[-1]
        refs = [s["ref"] for s in g if s["ref"] and s["lines"]] or [s["ref"] for s in g if s["ref"]]
        rng = _span(refs, code)
        title = f"{book} {rng} — {page_title}"
        slug = re.sub(r"[^A-Za-z0-9]", "", page_title.title())[:18]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {page_title}", (lambda title=title, t=t, body="".join(body), n=start + k: page(title, t, body, n))))
    return out

def _span(refs, code):
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
