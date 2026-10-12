"""Page helpers for the Exodus volume.

talk() is Genesis chapter 14's dialogue panel (a close-up face, and beside it a column of captions and balloons), with one
change: a short line ("Go.", "A rod.") gets a balloon sized to its words instead of the full column width."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from fx import new, vref, cap, balloon
from genesis.ch02 import W1
from genesis.ch04 import fc

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
