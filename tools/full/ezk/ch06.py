"""Ezekiel volume, Chapter 6 — The Eagles and the Cedar (Ezekiel 17–19). Every verse, word for word from ref/asv.
The riddle: a great eagle cropping the top of the cedar and carrying it to a land of traffic, the vine of low stature, the
second eagle and the vine bending its roots toward him, withered by the east wind; the meaning (a map of the way to Babylon
and the ambassadors to Egypt) and the net spread for the king; the tender twig planted on the mountain of the height of
Israel; the sour grapes and the soul that sinneth (a plate of three generations); is not my way equal? (the balances);
make you a new heart; and the lamentation for the princes of Israel in song boxes — the lioness and her whelps taken in
the pit and brought in a cage with hooks, the vine plucked up and planted in the wilderness."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from job.art2 import balances
from ezk import G, art6 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C06-00-Title", "Chapter 6 · The Eagles and the Cedar", title=True)
def title(n):
    svg = title_art(lambda w, h: K.eagle_cedar(w, h, 601), "#4A7AB0")
    return chapter_title(6, "第六話", "The Eagles and the Cedar", "Ezekiel 17 – 19", svg, "#2A3A5A", v("17:3", frm="A great eagle"), "Ezekiel · Volume Twenty-Six")


SEGS = run(17, 1, 24, arts={3: ("#4A7AB0", lambda w, h: K.eagle_cedar(w, h, 602)), 5: ("#6AA0C8", lambda w, h: K.low_vine(w, h, 603)),
                            7: ("#6AA0C8", lambda w, h: K.low_vine(w, h, 604, eagle2=True)), 10: ("#C88A5A", lambda w, h: K.low_vine(w, h, 605, wither=True)),
                            12: (MAP, lambda w, h: K.treaty_map(w, h)), 20: (MAP, lambda w, h: K.snare(w, h)), 22: ("#5A9AD0", lambda w, h: K.cedar_mountain(w, h, 606))},
           faces=FZ, heads={1: "Two Great Eagles", 11: "Know Ye Not What These Things Mean?", 22: "A Tender Twig"})
SEGS += run(18, 1, 32, arts={2: ("#3A4A3A", lambda w, h: K.sour_grapes(w, h, 607)), 4: (MAP, lambda w, h: K.generations("gn6", w, h)),
                             20: (MAP, lambda w, h: K.generations("gn6b", w, h)), 25: ("#2A2A3A", lambda w, h: balances(w, h, 608)), 31: (MAP, lambda w, h: K.hearts(w, h))},
            faces=FZ, generic=[("#2A1A3A", lambda w, h: K.jerusalem("j6", w, h, 609, mode="dusk")), ("#3A2A2A", lambda w, h: K.elders_house("eh6", w, h, 610))],
            heads={1: "The Soul That Sinneth", 5: "If a Man Be Just", 14: "If He Beget a Son", 21: "Turn Yourselves, and Live", 25: "Is Not My Way Equal?"})
SEGS += run(19, 1, 14, arts={2: ("#C8803A", lambda w, h: K.lions(w, h, 611, 0)), 4: ("#4A3A3A", lambda w, h: K.lions(w, h, 612, 1)), 9: ("#4A3A3A", lambda w, h: K.lions(w, h, 613, 2)),
                             10: ("#6AA0C8", lambda w, h: K.low_vine(w, h, 614, bird=False)), 12: ("#C88A5A", lambda w, h: K.low_vine(w, h, 615, wither=True)), 14: ("#1A0A0A", lambda w, h: K.vine_fire(w, h, 616))},
            faces=[(EZEKIEL_GRIEF, COLD), (EZEKIEL_TEAR, COLD)], ov={f"19:{n}": "n" for n in range(2, 15)}, budget=420,
            heads={1: "A Lamentation for the Princes of Israel", 10: "Thy Mother Was Like a Vine"})
PG.extend(pack(SEGS, "EZK-C06-D", PG.next(), end=end_mark("NEXT · A SWORD, A SWORD", "right: 10px; bottom: 34px")))
