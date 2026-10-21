"""Deuteronomy volume, Chapter 15 — The Death of Moses (Deuteronomy 33–34), the last chapter of Deuteronomy. Every verse,
word for word from ref/eng-asv. The blessing wherewith Moses blessed the children of Israel: Jehovah came from Sinai (song
boxes over the mount on fire), then the tribes as three pages of cells, one per tribe (as Jacob's blessing in Genesis 49),
then the everlasting arms; Moses on the top of Pisgah and the land shown him as a map; his death (caption only, over the
valley over against Beth-peor: no grave is drawn), the thirty days of weeping, Joshua full of the spirit of wisdom, and
there hath not arisen a prophet since in Israel like unto Moses."""
import math, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark, page
from asv import ems
from discourse import seg, pack
from deu import G, art as K, art4 as K4
from deu.common import shade, cp, gd, caps, MOODS
from exo import art4 as A4
from num import art13 as N13
from num.art import ALL
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import grid
from genesis.ch03 import clan
from genesis.ch06 import GOLDEN
from deu import ch14 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = ("#0B0B2A", lambda w, h: X.cosmic(w, h))

def nebo(p, seed):
    """Moses upon the mountain looking over the land, the drawing lowered so the words above leave his head clear."""
    return lambda w, h: f'<g transform="translate(0 {h * 0.36:.1f})">' + N13.abarim(p, w, h * 0.64, seed) + '</g>'

def song(ref, frm=None, to=None): return ("song", v(ref, frm=frm, to=to))


@P("DEU-C15-00-Title", "Chapter 15 · The Death of Moses", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3C88A"></rect>' + f'<g transform="translate(0 360)">{N13.abarim("t15", 760, 720, 1501)}</g>')
    return chapter_title(15, "第十五話", "The Death of Moses", "Deuteronomy 33 – 34", svg, "#F3C88A", v("34:7", frm="his eye was not dim,"), "Deuteronomy · Volume Five")


SEGS = [seg([cp("33:1")], "DEUT 33:1", art=lambda w, h: K.address("ad15", w, h, 1502, raise_hand=True), bg="#F3D8A0", head="The Blessing", h=330),
        seg([cp("33:2", to="And he said,"), song("33:2", frm="Jehovah came"), song("33:3"), song("33:4"), song("33:5")], "DEUT 33:2–5",
            art=lambda w, h: K.horeb(w, h, 1503, fire=True), bg="#2A0A0A", stamp=33)]
PG.extend(pack(SEGS, "DEU-C15-D", PG.next()))

# ---- the tribes: one cell per tribe, the words in full -------------------------------------------------------------------
def tribe_page(cells, title, n):
    """A page of tribe cells stacked full width; one type size for the page, each row as tall as its words need."""
    room = 1022 - 22 - 12 * (len(cells) - 1)
    def need(text, s):
        return 66 + math.ceil(ems(text, 0.64) / (672 / (s * 0.64))) * s * 1.5
    s = 22.0
    while s > 11 and sum(need(t, s) for _, t, _, _ in cells) > room: s -= 0.5
    fr = " ".join(f"{need(t, s):.0f}fr" for _, t, _, _ in cells)
    body = grid([clan(nm, t, ref, c, size=s) for nm, t, ref, c in cells], fr, ncol=1)
    tag = (f'\n  <div data-label style="position: absolute; left: 26px; right: 26px; top: 8px; text-align: center; font-size: 9px; font-weight: 600; '
           f'letter-spacing: 0.24em; color: #6B6862">THE BLESSING OF MOSES · DEUTERONOMY 33</div>')
    return page(title, "minmax(0, 1fr)", body + tag, n)

TRIBES = [("Let Reuben Live", [("Reuben", v("33:6"), "DEUT 33:6", "#FF6A5A"), ("Judah", v("33:7"), "DEUT 33:7", "#5AD87A"),
                                ("Levi", sp("33:8-11"), "DEUT 33:8–11", "#FF8A3D"), ("Benjamin", v("33:12"), "DEUT 33:12", "#9CCB5E")], "33:6–12"),
          ("Blessed of Jehovah Be His Land", [("Joseph", sp("33:13-15"), "DEUT 33:13–15", "#8FD0E2"), ("Joseph", sp("33:16-17"), "DEUT 33:16–17", "#8FD0E2"),
                                              ("Zebulun · Issachar", sp("33:18-19"), "DEUT 33:18–19", "#5AC8C8")], "33:13–19"),
          ("As Thy Days, So Shall Thy Strength Be", [("Gad", sp("33:20-21"), "DEUT 33:20–21", "#FFB04A"), ("Dan", v("33:22"), "DEUT 33:22", "#7AA8FF"),
                                                     ("Naphtali", v("33:23"), "DEUT 33:23", "#D8E4F0"), ("Asher", sp("33:24-25"), "DEUT 33:24–25", "#E8C88A")], "33:20–25")]
for k, (head, cells, rng) in enumerate(TRIBES):
    slug = "".join(ch for ch in head.title() if ch.isalpha())[:18]
    PG.P(f"DEU-C15-T{k + 1:02d}-{slug}", head)(lambda n, head=head, cells=cells, rng=rng: tribe_page(cells, f"Deuteronomy {rng} — {head}", n))

MG = MOODS["grief"]
SEGS2 = [seg([song("33:26"), song("33:27")], "DEUT 33:26–27", art=NIGHTA[1], bg=NIGHTA[0], head="The Everlasting Arms"),
         seg([song("33:28"), song("33:29")], "DEUT 33:28–29", tok=K.MOSES_FIRE, bg=GOLDEN),
         seg([caps("34:1-3")], "DEUT 34:1–3", art=nebo("ab15", 1504), bg="#F3C88A", head="The Top of Pisgah"),
         seg(None, "DEUT 34:1–3", art=K4.nebo_map, bg="#0B1A2E", h=420, stamp=34),
         seg([cp("34:4", to="said unto him,"), gd("34:4", frm="This is the land")], "DEUT 34:4", tok=MG[0], bg=MG[1]),
         seg([caps("34:5-6")], "DEUT 34:5–6", art=lambda w, h: K4.beth_peor(w, h, 1505), bg="#3A2A4A", head="So Moses the Servant of Jehovah Died"),
         seg([caps("34:7-8")], "DEUT 34:7–8", art=lambda w, h: K4.weeping(w, h, 1506), bg="#3A3450"),
         seg([caps("34:9")], "DEUT 34:9", art=lambda w, h: N13.joshua_set("js15", w, h, 1507), bg=GOLDEN),
         seg([caps("34:10-12")], "DEUT 34:10–12", art=lambda w, h: mk.defs("dw15", *ALL) + A4.dry_walk("dw15", w, h, 1508), bg="#0F4C68",
             head="Whom Jehovah Knew Face to Face")]
PG.extend(pack(SEGS2, "DEU-C15-E", PG.next(), end=end_mark("END OF DEUTERONOMY · NEXT · JOSHUA", "right: 10px; bottom: 34px", ch="完")))
