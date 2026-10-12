"""Page helpers for the Exodus volume.

talk() is Genesis chapter 14's dialogue panel (a close-up face, and beside it a column of captions and balloons), with one
change: a short line ("Go.", "A rod.") gets a balloon sized to its words instead of the full column width."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from fx import new, vref, cap, balloon
from genesis.ch02 import W1
from genesis.ch04 import fc

def song(text, pos, size=15, maxw=None, color="#D7261E"):
    """A line of a song (the Song of Moses, Miriam's answer): a cream box with a red double rule down the left, Archivo
    Narrow like a balloon but square, so a sung line reads apart from both narration and speech."""
    mw = f" max-width: {maxw}px;" if maxw else ""
    return (f'    <div style="position: absolute; {pos};{mw} padding: 10px 14px 10px 18px; background: #FFF8E6; color: #0D0D0F; border: 2.5px solid #0D0D0F; '
            f'box-shadow: inset 6px 0 0 #FFF8E6, inset 10px 0 0 {color}, 4px 4px 0 #0D0D0F; font-family: \'Archivo Narrow\', sans-serif; font-weight: 700; '
            f'font-size: {size}px; line-height: 1.2; letter-spacing: 0.02em; text-transform: uppercase">{text}</div>\n')

def law(heading, text, ref, svg="", size=None, accent="#FFD23F", cell=490, w=336):
    """One cell of a page of ordinances (Exodus 21–23): a Voice box (God's words, indigo with the gold inner rule) with a
    pictogram above (svg in a 320 x 100 viewBox, standing on the cell's ground line and filling whatever height the words
    leave), a heading tag and the verse label (both data-label). size=None sizes the words to the cell (cell = its height in px)."""
    if size is None:                              # as large as the cell allows: the words take ~60% of the height, the pictogram the rest
        size = max(13, min(24, round((w * (cell - 150) / (0.62 * len(text))) ** 0.5 * 2) / 2))
    pic = (f'<div style="position: relative; flex: 1 1 0; min-height: 70px; background: #2A2458; border-bottom: 2px solid {accent}">'
           f'<svg viewBox="0 0 320 100" preserveAspectRatio="xMidYMax meet" style="position: absolute; inset: 0; width: 100%; height: 100%">{svg}</svg></div>' if svg else "")
    return (f'\n    <div style="position: relative; min-height: 0; overflow: hidden; border: 3px solid #0D0D0F; background: #12113A; color: #F3EFE6; box-shadow: inset 0 0 0 4px #12113A, inset 0 0 0 5.5px {accent}; display: flex; flex-direction: column">'
            f'{pic}'
            f'\n      <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px; padding: 8px 12px 0"><span data-label style="font-size: 9px; font-weight: 600; letter-spacing: 0.2em; color: {accent}">{heading}</span>'
            f'<span data-label style="font-size: 9px; font-weight: 600; letter-spacing: 0.18em; white-space: nowrap; opacity: 0.8">{ref}</span></div>'
            f'\n      <div style="padding: 6px 12px 12px; font-family: Anton, sans-serif; font-size: {size}px; line-height: 1.18; letter-spacing: 0.04em; text-transform: uppercase">{text}</div>\n    </div>')

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
