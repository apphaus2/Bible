"""Ezekiel volume, Chapter 7 — A Sword, a Sword (Ezekiel 20–21). Every verse, word for word from ref/asv.
The elders come to inquire; the history of the rebellions: Egypt (a map), the statutes and the sabbaths (the tables), the
wilderness and the camp, the high places in the land; the wilderness of the peoples and passing under the rod; the holy
mountain and the sweet savor; the forest of the South set on fire; Ah Lord Jehovah! is he not a speaker of parables?; then
the sword drawn out of its sheath, sharpened and furbished (a great glittering blade, no blow drawn); sigh, with the
breaking of thy loins; the king of Babylon at the parting of the way with his divination (a map); remove the mitre, and
take off the crown — overturn, overturn, overturn it; and the sword against the children of Ammon, returned into its sheath."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art7 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_TEAR,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C07-00-Title", "Chapter 7 · A Sword, a Sword", title=True)
def title(n):
    svg = title_art(lambda w, h: K.sword(w, h, 701), "#0B0B1A")
    return chapter_title(7, "第七話", "A Sword, a Sword", "Ezekiel 20 – 21", svg, "#0B0B1A", v("21:9", frm="A sword, a sword"), "Ezekiel · Volume Twenty-Six")


SEGS = run(20, 1, 49, arts={1: ("#3A2A2A", lambda w, h: K.elders_house("eh7", w, h, 702)), 5: (MAP, lambda w, h: K.exodus_map(w, h, legs=("RAAMSES", "THE RED SEA", "THE WILDERNESS"))),
                            11: ("#1A0E1E", lambda w, h: K.tables(w, h, 703)), 15: ("#C8803A", lambda w, h: K.wilderness_camp(w, h, 704)),
                            28: ("#4A3A6A", lambda w, h: K.high_places(w, h, 705)), 35: ("#C8803A", lambda w, h: K.wilderness_camp(w, h, 706)),
                            37: ("#6A8AB0", lambda w, h: K.under_rod(w, h, 707)), 40: ("#6AB0D8", lambda w, h: K.covenant_dawn(w, h, 708)),
                            46: ("#1A0A0A", lambda w, h: K.forest_fire(w, h, 709))},
           faces=FZ, ov={"20:1": "c"}, generic=[("#C8803A", lambda w, h: K.wilderness_camp(w, h, 711)), ("#2A1A3A", lambda w, h: K.jerusalem("j7", w, h, 710, mode="dusk"))],
           heads={1: "Is It to Inquire of Me?", 5: "In the Day When I Chose Israel", 10: "In the Wilderness", 27: "When I Had Brought Them into the Land",
                  33: "I Will Be King over You", 39: "In My Holy Mountain", 45: "The Forest of the South"})
SEGS += run(21, 1, 32, arts={3: ("#0B0B1A", lambda w, h: K.sword(w, h, 712)), 9: ("#0B0B1A", lambda w, h: K.sword(w, h, 713)), 14: ("#5A4A5A", lambda w, h: K.jerusalem("j7b", w, h, 714, mode="siege")),
                             19: (MAP, lambda w, h: K.parting(w, h)), 22: ("#5A4A5A", lambda w, h: K.jerusalem("j7c", w, h, 715, mode="siege")),
                             26: ("#1A1A2A", lambda w, h: K.mitre_crown(w, h, 716)), 28: ("#0B0B1A", lambda w, h: K.sword(w, h, 717)),
                             30: ("#0B0B1A", lambda w, h: K.sword(w, h, 718, sheath=True)), 31: ("#2A0A0A", lambda w, h: K.rabbah(w, h, 719))},
            faces=FZ + [(EZEKIEL_GRIEF, COLD)], heads={1: "I Have Drawn Forth My Sword", 6: "Sigh Therefore", 8: "A Sword, a Sword", 18: "The Parting of the Way",
                                                     25: "Remove the Mitre", 28: "Concerning the Children of Ammon"})
PG.extend(pack(SEGS, "EZK-C07-D", PG.next(), end=end_mark("NEXT · OHOLAH AND OHOLIBAH", "right: 10px; bottom: 34px")))
