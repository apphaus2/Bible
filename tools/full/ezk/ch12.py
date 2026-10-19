"""Ezekiel volume, Chapter 12 — The Watchman and the Shepherds (Ezekiel 33–34). Every verse, word for word from ref/asv.
The watchman that seeth the sword come and bloweth the trumpet; I have set thee a watchman; have I any pleasure in the death
of the wicked?; the way of the Lord is not equal (the balances); one that had escaped out of Jerusalem — The city is
smitten — and the prophet's mouth opened; the waste places; the people that sit before him as before a lovely song; then the
shepherds of Israel that feed themselves, and the flock scattered on the mountains; I myself will search for my sheep — the
flock gathered into good pasture (no shepherd drawn); the fat sheep and the lean; one shepherd, my servant David; and the
covenant of peace, the showers in their season."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from job.art2 import balances
from ezk import G, art12 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C12-00-Title", "Chapter 12 · The Watchman and the Shepherds", title=True)
def title(n):
    svg = title_art(lambda w, h: K.watch_sword("t12", w, h, 1201), "#1A1A3A")
    return chapter_title(12, "第十二話", "The Watchman and the Shepherds", "Ezekiel 33 – 34", svg, "#1A1A3A", v("33:7", to="unto the house of Israel;"), "Ezekiel · Volume Twenty-Six")


OV = {"33:21": (("c", None), ("s", "The city is smitten.")), "33:22": "c"}
SEGS = run(33, 1, 33, arts={2: ("#1A1A3A", lambda w, h: K.watch_sword("ws12", w, h, 1202)), 7: ("#1A1A3A", lambda w, h: K.watchman("wm12", w, h, 1203)),
                            11: ("#2A1A3A", lambda w, h: K.jerusalem("j12", w, h, 1204, mode="dusk")), 17: ("#2A2A3A", lambda w, h: balances(w, h, 1205)),
                            21: ("#4A4A7A", lambda w, h: K.escaped("es12", w, h, 1206)), 24: ("#8A7A8A", lambda w, h: K.waste_places(w, h, 1207)),
                            27: ("#6A6A7A", lambda w, h: K.jerusalem("j12b", w, h, 1208, mode="empty")), 30: ("#3A2A2A", lambda w, h: K.listeners("ls12", w, h, 1209))},
           faces=FZ, ov=OV, heads={1: "When I Bring the Sword upon a Land", 7: "I Have Set Thee a Watchman", 10: "Turn Ye, Turn Ye", 17: "The Way of the Lord",
                                   21: "The City Is Smitten", 23: "Those Waste Places", 30: "A Very Lovely Song"})
SEGS += run(34, 1, 31, arts={2: ("#3A2A4A", lambda w, h: K.shepherds_feast("sf12", w, h, 1210)), 5: ("#8A6A5A", lambda w, h: K.scattered(w, h, 1211)),
                             10: ("#8A6A5A", lambda w, h: K.scattered(w, h, 1212, beast=False)), 11: ("#6AB0D8", lambda w, h: K.fold(w, h, 1213)),
                             14: ("#6AB0D8", lambda w, h: K.fold(w, h, 1214)), 17: ("#6AA0C8", lambda w, h: K.fat_lean(w, h, 1215)), 20: ("#6AA0C8", lambda w, h: K.fat_lean(w, h, 1216)),
                             23: ("#6AB0D8", lambda w, h: K.david_shepherd("dv12", w, h, 1217)), 26: ("#6AB0D8", lambda w, h: K.showers(w, h, 1218)),
                             29: ("#6AB0D8", lambda w, h: K.gathered(w, h, 1219))},
            faces=FZ, heads={1: "Woe unto the Shepherds of Israel", 11: "I Myself Will Search for My Sheep", 17: "Between Sheep and Sheep", 23: "One Shepherd",
                             25: "A Covenant of Peace"})
PG.extend(pack(SEGS, "EZK-C12-D", PG.next(), end=end_mark("NEXT · THE VALLEY OF DRY BONES", "right: 10px; bottom: 34px")))
