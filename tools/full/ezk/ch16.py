"""Ezekiel volume, Chapter 16 — The Glory Returns (Ezekiel 43–44). Every verse, word for word from ref/asv.
The glory of the God of Israel coming from the way of the east, his voice like the sound of many waters, the earth shining
(light over the eastern hills, no figure); the glory entering by the east gate and filling the house; one speaking out of the
house — this is the place of my throne; the law of the house; the altar measured by cubits (a blueprint plate) and its
consecration seven days (the beasts whole beside the altar, then fire); the outer east gate shut, for Jehovah hath entered
in by it; the prince eating bread in the gate; no foreigner in the sanctuary; the Levites keeping the gates; the sons of
Zadok in linen garments; and I am their inheritance."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art16 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_AWE,
                        EZEKIEL_FIRE, AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch15 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BP = "#0B1A2E"
VP = lambda *hi, **k: (BP, lambda w, h: K.vision_plan(w, h, hi=hi, **k), 470)


@P("EZK-C16-00-Title", "Chapter 16 · The Glory Returns", title=True)
def title(n):
    svg = title_art(lambda w, h: K.glory_east("t16", w, h, 1601), "#1A1A4A")
    return chapter_title(16, "第十六話", "The Glory Returns", "Ezekiel 43 – 44", svg, "#1A1A4A", v("43:2"), "Ezekiel · Volume Twenty-Six")


OV = {"43:1": "c", "43:2": "c", "43:3": "c", "43:4": "c", "43:5": "c", "43:6": "c", "44:1": "c", "44:4": "c"}
SEGS = [drawn(wl("43:1-3", ov=OV), "EZEK 43:1–3", lambda w, h: K.glory_east("ge16", w, h, 1602), "#1A1A4A", head="From the Way of the East", stamp=43),
        drawn(wl("43:4-6", ov=OV), "EZEK 43:4–6", lambda w, h: K.threshold("th16", w, h, 1603), "#2A2A4A", head="The Glory of Jehovah Filled the House")]
SEGS += run(43, 7, 27, arts={7: ("#2A2A4A", lambda w, h: K.threshold("th16b", w, h, 1604)), 10: VP("house", "inner_court", "altar", "outer_wall"),
                             13: (BP, lambda w, h: K.altar_plate(w, h), 470), 15: (BP, lambda w, h: K.altar_plate(w, h), 470), 18: ("#5A6A8A", lambda w, h: K.consecration("cs16", w, h, 1605)),
                             22: ("#5A6A8A", lambda w, h: K.consecration("cs16b", w, h, 1606, beast="goat")), 25: ("#5A6A8A", lambda w, h: K.consecration("cs16c", w, h, 1607, beast="ram"))},
            faces=[(EZEKIEL_FIRE, AMBER), (EZEKIEL, GOLDEN)], ov=OV,
            heads={7: "The Place of My Throne", 10: "Show the House", 13: "The Measures of the Altar", 18: "The Ordinances of the Altar"})
SEGS += run(44, 1, 31, arts={1: ("#3A4A7A", lambda w, h: K.shut_gate("sg16", w, h, 1608)), 3: ("#3A4A7A", lambda w, h: K.shut_gate("sg16b", w, h, 1609, prince=True)),
                             4: ("#2A2A4A", lambda w, h: K.threshold("th16c", w, h, 1610)), 9: VP("east_gate", "north_gate", "south_gate"),
                             11: ("#5A6A8A", lambda w, h: K.gatekeepers("gk16", w, h, 1611)), 15: ("#6A8AB0", lambda w, h: K.linen_priests("lp16", w, h, 1612)),
                             17: ("#6A8AB0", lambda w, h: K.linen_priests("lp16b", w, h, 1613)), 23: ("#5A6A8A", lambda w, h: K.judges_gate("jg16", w, h, 1614)),
                             28: ("#C8905A", lambda w, h: K.firstfruits(w, h, 1615))},
            faces=[(EZEKIEL_AWE, AMBER), (EZEKIEL, GOLDEN)], ov=OV,
            heads={1: "This Gate Shall Be Shut", 4: "Mark Well", 10: "The Levites", 15: "The Sons of Zadok", 17: "Linen Garments", 28: "I Am Their Inheritance"})
PG.extend(pack(SEGS, "EZK-C16-D", PG.next(), end=end_mark("NEXT · THE HOLY OBLATION", "right: 10px; bottom: 34px")))
