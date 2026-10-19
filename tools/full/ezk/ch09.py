"""Ezekiel volume, Chapter 9 — The Desire of Thine Eyes (Ezekiel 24–25). Every verse, word for word from ref/asv.
The name of the day written — the king of Babylon drew close unto Jerusalem this selfsame day; the parable of the caldron
set on the fire, then set empty on the coals that its rust may be consumed; the desire of thine eyes taken with a stroke —
the death of Ezekiel's wife words only, over the empty house at evening and in the morning; the headtire and the shoes;
the people's question and Ezekiel a sign; he that escapeth shall come unto thee; then the nations round about as maps:
Ammon (Rabbah a stable for camels), Moab, Edom and the Philistines."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art9 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C09-00-Title", "Chapter 9 · The Desire of Thine Eyes", title=True)
def title(n):
    svg = title_art(lambda w, h: K.empty_house(w, h, 901), "#1A1A3A")
    return chapter_title(9, "第九話", "The Desire of Thine Eyes", "Ezekiel 24 – 25", svg, "#1A1A3A", v("24:16", to="with a stroke:"), "Ezekiel · Volume Twenty-Six")


OV = {"24:18": "c", "24:19": (("c", None), ("s", "Wilt thou not"))}
SEGS = run(24, 1, 14, arts={2: ("#2A1A1A", lambda w, h: K.day_tablet(w, h, 902)), 3: ("#2A1A2A", lambda w, h: K.rusty_caldron(w, h, 903)),
                            9: ("#2A1A3A", lambda w, h: K.bloody_city(w, h, 904)), 11: ("#2A1A2A", lambda w, h: K.rusty_caldron(w, h, 905, empty=True))},
           faces=FZ, heads={1: "This Selfsame Day", 3: "Set On the Caldron", 9: "Woe to the Bloody City"})
SEGS += [fz("24:15-16", EZEKIEL_GRIEF, COLD, head="The Desire of Thine Eyes"),
         dz("24:17", lambda w, h: K.headtire(w, h, 906), "#2A2A3A"),
         drawn(wl("24:18", ov=OV), "EZEK 24:18", lambda w, h: K.empty_house(w, h, 907), "#1A1A3A"),
         drawn(wl("24:19-20", ov=OV), "EZEK 24:19–20", lambda w, h: K.empty_house(w, h, 908, dawn=True), "#3A3A6A")]
SEGS += run(24, 21, 27, arts={21: ("#6A6A7A", lambda w, h: K.jerusalem("j9", w, h, 909, mode="empty")), 26: ("#4A4A7A", lambda w, h: K.escaped("es9", w, h, 910))},
            faces=[(EZEKIEL_TEAR, COLD), (EZEKIEL, GOLDEN)], heads={21: "Ezekiel Shall Be unto You a Sign"})
SEGS += run(25, 1, 17, arts={2: (MAP, lambda w, h: K.nations_map(w, h, hi=("AMMON",))), 5: ("#C8803A", lambda w, h: K.camels_rabbah(w, h, 911)),
                             8: (MAP, lambda w, h: K.nations_map(w, h, hi=("MOAB", "BETH-JESHIMOTH", "BAAL-MEON", "KIRIATHAIM", "THE CHILDREN OF THE EAST"))),
                             12: (MAP, lambda w, h: K.nations_map(w, h, hi=("EDOM", "DEDAN"))), 15: (MAP, lambda w, h: K.nations_map(w, h, hi=("THE PHILISTINES", "THE CHERETHITES")))},
            faces=FZ, heads={1: "Against the Children of Ammon", 8: "Moab and Seir", 12: "Edom", 15: "The Philistines"})
PG.extend(pack(SEGS, "EZK-C09-D", PG.next(), end=end_mark("NEXT · THE SHIP OF TYRE", "right: 10px; bottom: 34px")))
