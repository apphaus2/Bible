"""Speech panels for the long discourses (Deuteronomy, the prophets): a close-up face on one side and, beside it, a column
of text boxes stacked by the browser and sized to fill the panel.

    orate(tok, h, bg, [("cap", narration), ("say", his words), ("god", God's words quoted)], ref="DEUT 1:6–8")

"cap" is a narration caption, "say" a rounded speech box (the man's own words, Archivo Narrow, with a notch toward his
face), "god" a Voice box (God's words, indigo with the gold rule) — used where the speaker quotes Jehovah. The one font
size that fits all the words in the panel is chosen by estimate (the sandbox's fallback fonts are wider, so if it fits
there it fits on the site). tok=None: no face, the column spans the panel over `art` (svg) instead."""
import math
from fx import new, vref
from genesis.ch02 import W1, W2
from genesis.ch04 import fc

def _height(lines, bw, s):
    tot = 0
    for kind, text in lines:
        n = len(text)
        if kind == "cap":
            fs = min(11.5, max(9.5, s * 0.66)); cpl = max(8, (bw - 24) / (fs * 0.64))
            tot += math.ceil(n / cpl) * fs * 1.45 + 20
        elif kind in ("say", "song"):
            cpl = max(6, (bw - 36) / (s * 0.56)); tot += math.ceil(n / cpl) * s * 1.16 + 30
        else:
            cpl = max(6, (bw - 36) / (s * 0.53)); tot += math.ceil(n / cpl) * s * 1.15 + 32
        tot += 9
    return tot

def fit(lines, bw, h, hi=21, lo=9.5):
    s = hi
    while s > lo and _height(lines, bw, s) > h - 34:
        s -= 0.5
    return s

def _cap(text, fs):
    return (f'<div style="align-self: flex-start; padding: 6px 10px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; font-size: {fs}px; '
            f'font-weight: 600; line-height: 1.45; letter-spacing: 0.03em; text-transform: uppercase">{text}</div>')

def _say(text, s, side):
    notch = (f'<div style="position: absolute; {side}: -8px; top: 16px; width: 13px; height: 13px; background: #ffffff; '
             f'border-{side}: 2.5px solid #0D0D0F; border-bottom: 2.5px solid #0D0D0F; transform: rotate({45 if side == "left" else -135}deg)"></div>')
    return (f'<div style="position: relative">{notch}<div style="padding: 11px 16px 12px; background: #ffffff; color: #0D0D0F; border: 2.5px solid #0D0D0F; border-radius: 18px; '
            f"font-family: 'Archivo Narrow', sans-serif; font-weight: 700; font-size: {s}px; line-height: 1.16; text-transform: uppercase\">{text}</div></div>")

def _song(text, s, color="#7A3BA8"):
    """A line of a song: a cream box with a coloured double rule down the left (as exo.kit.song)."""
    return (f'<div style="padding: 10px 14px 10px 20px; background: #FFF8E6; color: #0D0D0F; border: 2.5px solid #0D0D0F; '
            f'box-shadow: inset 6px 0 0 #FFF8E6, inset 10px 0 0 {color}, 4px 4px 0 #0D0D0F; font-family: 'Archivo Narrow', sans-serif; font-weight: 700; '
            f'font-size: {s}px; line-height: 1.18; letter-spacing: 0.02em; text-transform: uppercase">{text}</div>')

def _god(text, s):
    return (f'<div style="padding: 12px 16px; background: #12113A; color: #F3EFE6; box-shadow: inset 0 0 0 4px #12113A, inset 0 0 0 5.5px #FFD23F; '
            f'font-family: Anton, sans-serif; font-size: {s}px; line-height: 1.15; letter-spacing: 0.04em; text-transform: uppercase">{text}</div>')

def column(lines, bw, h, side="left", hi=21):
    s = fit(lines, bw, h, hi=hi)
    fs = min(11.5, max(9.5, s * 0.66))
    items = []
    for kind, text in lines:
        items.append(_cap(text, fs) if kind == "cap" else _say(text, s, side) if kind == "say" else _song(text, s) if kind == "song" else _god(text, s))
    return items

def orate(tok, h, bg, lines, w=W1, flip=False, ref=None, hi=21, art="", extra="", face_w=None, top=None):
    """A speech panel. Not flipped: the face at the left looking right, the words at the right. flip=True mirrors it."""
    if tok is None:
        left, bw = 12, w - 24
        svg = art
    else:
        fw = face_w or (270 if w > 400 else 130)
        bw = w - fw - 24
        left = fw + 12 if not flip else 12
        svg = art + fc(tok, h, w=w, flip=flip)
    top = bool(top) and tok is None                # top=True: words over a drawing sit at the top, leaving the art below
    items = column(lines, bw, h * (0.62 if top else 1), side="left" if not flip else "right", hi=hi)
    col = (f'\n    <div style="position: absolute; left: {left}px; top: {34 if top else 12}px; bottom: 12px; width: {bw}px; display: flex; flex-direction: column; justify-content: {"flex-start" if top else "center"}; gap: 9px">'
           + "".join(items) + '</div>\n')
    r = vref(ref, ("left: 12px; bottom: 12px" if not flip else "right: 12px; bottom: 12px") if tok else "right: 12px; bottom: 12px") if ref else ""
    return new(bg, w, h, svg, col + r + extra)
