"""Romans volume, Chapter 3 — No Condemnation (Romans 8). Every verse, word for word from ref/eng-asv.
The high point of the letter, given room: the cell standing open in the morning (8:1–2); the plate of the two minds; new
grain springing from the furrows at dawn (8:11); the plate of bondage and adoption, Abba, Father; the whole creation
groaning — a stormy horizon at dawn, the light breaking low (8:19–22); Paul kneeling by night at the window, the Spirit
not drawn (8:26–27); the golden chain of 8:29–30; the judgment-seat with no accuser and the empty throne in light (8:33–34,
God never drawn); Paul's face in white light from 8:31; the ring of the love of Christ (8:35); Psalm 44 in a song box over
the empty sheepfold at dusk (8:36, words only); and the technical diagram of 8:38–39, neither height nor depth, angels only
named."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rom import G, art3 as A, ch02 as _prev
from rom.common import (K, Pages, D, F, lt, lp, sg, gd, v, title, nxt, glory, PAUL, PAUL_STERN, PAUL_JOY, PAUL_LAMP, GOLD_BG, STERN_BG, JOY_BG, LAMP_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ROM-C03-00-Title", "Chapter 3 · No Condemnation", title=True)
def title_page(n):
    svg = f'<g transform="translate(0 260)">{A.groaning(760, 820, 308, dawn=0.6)}</g><rect x="0" y="0" width="760" height="262" fill="#1A1A2E"></rect>'
    return title(3, "No Condemnation", "Romans 8", svg, "#1A1A2E", v("8:1"))


def st(p, seed, **k): return lambda w, h: A.study(p, w, h, seed, **k)

SEGS = [
    D(lp("8:1-2"), lambda w, h: A.open_cell(w, h, 1801), "#3A3238", head="No Condemnation", sky=8, art_h=300),
    F(lp("8:3-4"), PAUL),
    D(lp("8:5-8"), lambda w, h: A.two_minds(w, h), "#0B1A2E", art_h=210),
    F(lp("8:9-10"), PAUL),
    D([lt("8:11")], lambda w, h: A.new_grain(w, h, 1811), "#3A3A7A", art_h=280),
    F(lp("8:12-14"), PAUL_STERN, bg=STERN_BG),
    D(lp("8:15-17"), lambda w, h: A.adoption(w, h), "#0B1A2E", head="Abba, Father", art_h=230),
    D(lp("8:18-19"), lambda w, h: A.groaning(w, h, 1818, dawn=0.3), "#1A1A2E", head="The Whole Creation Groaneth", art_h=290),
    D(lp("8:20-22"), lambda w, h: A.groaning(w, h, 1820, dawn=0.55), "#1A1A2E", art_h=290),
    F(lp("8:23-25"), PAUL),
    D(lp("8:26-27"), lambda w, h: A.kneeling_prayer("kp1", w, h, 1826), "#1E1A2A", art_h=310),
    D(lp("8:28-30"), lambda w, h: A.golden_chain(w, h), "#0B1A2E", head="All Things Work Together for Good", art_h=270),
    F(lp("8:31-32"), PAUL_JOY, bg=JOY_BG, head="If God Is for Us"),
    D(lp("8:33-34"), lambda w, h: A.no_accuser("na1", w, h, 1833), "#8FD0E2", art_h=310),
    D([lt("8:35")], lambda w, h: A.love_ring(w, h), "#0B1A2E", head="Who Shall Separate Us", art_h=330),
    D([lt("8:36", to="Even as it is written,"), sg("8:36", frm="For thy sake")], lambda w, h: A.empty_pasture(w, h, 1836), "#2A1A3A", art_h=270),
    F([lt("8:37")], PAUL_JOY, bg=JOY_BG),
    D(lp("8:38-39"), lambda w, h: A.height_depth(w, h), "#0B1A2E", h=1010),
]
PG.extend(K.pack(SEGS, "ROM-C03-D", PG.next(), end=nxt("NEXT · THE DEPTH OF THE RICHES")))
