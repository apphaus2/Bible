"""Ezekiel volume, Chapter 8 — Oholah and Oholibah (Ezekiel 22–23). Every verse, word for word from ref/asv.
The bloody city (Jerusalem under a red sky, no one drawn); the house of Israel become dross in the furnace; the conspiracy
of her prophets like a roaring lion, her princes like wolves; the gap in the wall where no man stood; then the parable of
the two sisters told with restraint — the words only, over cities, maps and things, never a figure: Samaria and Jerusalem
and their lovers (maps), the horsemen clothed in blue far off, the Chaldeans portrayed in vermilion upon the wall, the host
with chariots and wagons, the cup of astonishment, the stately bed and the table with no one there, and the judgment words
over a heap of stones and houses burning."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art8 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C08-00-Title", "Chapter 8 · Oholah and Oholibah", title=True)
def title(n):
    svg = title_art(lambda w, h: K.oholah_map(w, h, 1), MAP)
    return chapter_title(8, "第八話", "Oholah and Oholibah", "Ezekiel 22 – 23", svg, MAP, v("23:4", frm="Samaria is Oholah"), "Ezekiel · Volume Twenty-Six")


SEGS = run(22, 1, 31, arts={2: ("#2A1A3A", lambda w, h: K.bloody_city(w, h, 801)), 13: ("#6A6A7A", lambda w, h: K.jerusalem("j8", w, h, 802, mode="empty")),
                            18: ("#1A0A0A", lambda w, h: K.furnace(w, h, 803)), 25: ("#C8803A", lambda w, h: K.lions(w, h, 804, 0)), 28: ("#8FB0C8", lambda w, h: K.daubed(w, h, 805, 0)),
                            30: ("#2A2A4A", lambda w, h: K.gap(w, h, 806))},
           faces=FZ, generic=[("#2A1A3A", lambda w, h: K.bloody_city(w, h, 807))],
           heads={1: "The Bloody City", 17: "Dross in the Furnace", 23: "A Land Not Cleansed", 30: "I Sought for a Man"})
SEGS += run(23, 1, 49, arts={2: (MAP, lambda w, h: K.oholah_map(w, h, 0)), 5: ("#6A8AB0", lambda w, h: K.blue_horsemen("bh8", w, h, 808)), 11: (MAP, lambda w, h: K.oholah_map(w, h, 1)),
                             14: ("#3A2A2A", lambda w, h: K.vermilion(w, h, 809)), 22: (MAP, lambda w, h: K.oholah_map(w, h, 2)), 24: ("#5A4A5A", lambda w, h: K.army("ar8", w, h, 810)),
                             28: ("#5A4A5A", lambda w, h: K.jerusalem("j8b", w, h, 811, mode="siege")), 32: ("#1A0A1A", lambda w, h: K.cup(w, h, 812)),
                             38: ("#3A3A4A", lambda w, h: K.mountains(w, h, 813, "broken")), 41: ("#2A1A2A", lambda w, h: K.stately_bed(w, h, 814)),
                             46: ("#2A0A0A", lambda w, h: K.stones_fire(w, h, 815))},
            faces=FZ + [(EZEKIEL_GRIEF, COLD)], ov={"23:36": (("c", None), ("g", "Son of man,"))},
            heads={1: "Two Women, the Daughters of One Mother", 11: "Her Sister Oholibah", 22: "Therefore, O Oholibah", 31: "Thy Sister's Cup",
                   36: "Wilt Thou Judge Oholah and Oholibah?", 45: "Righteous Men Shall Judge Them"})
PG.extend(pack(SEGS, "EZK-C08-D", PG.next(), end=end_mark("NEXT · THE DESIRE OF THINE EYES", "right: 10px; bottom: 34px")))
