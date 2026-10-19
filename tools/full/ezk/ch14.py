"""Ezekiel volume, Chapter 14 — Gog (Ezekiel 38–39). Every verse, word for word from ref/asv.
Gog of the land of Magog, prince of Rosh, Meshech and Tubal, with Persia, Cush and Put, Gomer and Togarmah, out of the
uttermost parts of the north (a map); the host on the march; the land of unwalled villages; coming like a storm and a cloud
to cover the land; the great shaking, the hailstones, fire and brimstone (over empty mountains, no one drawn); the bow
smitten out of his hand; the weapons burned seven years; the valley of Hamon-gog and the signs set up by the bones; the
birds of every sort called to the feast — words only over an empty field and the birds wheeling; and I will bring back the
captivity of Jacob, and pour out my Spirit upon the house of Israel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art14 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_AWE,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch13 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("EZK-C14-00-Title", "Chapter 14 · Gog", title=True)
def title(n):
    svg = title_art(lambda w, h: K.gog_map(w, h, 1), MAP)
    return chapter_title(14, "第十四話", "Gog", "Ezekiel 38 – 39", svg, MAP, v("38:2", to="and Tubal,"), "Ezekiel · Volume Twenty-Six")


SEGS = run(38, 1, 23, arts={2: (MAP, lambda w, h: K.gog_map(w, h)), 4: ("#1A1A2A", lambda w, h: K.hordes("hd14", w, h, 1401)), 8: ("#1A1A2A", lambda w, h: K.gog_storm(w, h, 1402)),
                            11: ("#6AB0D8", lambda w, h: K.unwalled("uw14", w, h, 1403)), 13: (MAP, lambda w, h: K.gog_map(w, h, 1)), 15: ("#1A1A2A", lambda w, h: K.hordes("hd14b", w, h, 1404)),
                            19: ("#1A0A0A", lambda w, h: K.shaking(w, h, 1405)), 22: ("#1A0A0A", lambda w, h: K.shaking(w, h, 1406))},
           faces=FZ, heads={1: "Gog, of the Land of Magog", 10: "The Land of Unwalled Villages", 14: "Out of the Uttermost Parts of the North", 18: "A Great Shaking"})
SEGS += run(39, 1, 29, arts={2: ("#3A3A4A", lambda w, h: K.bow_smitten(w, h, 1407)), 6: ("#2A0A0A", lambda w, h: K.tyre(w, h, 1408, "burning")),
                             9: ("#2A2A4A", lambda w, h: K.weapon_fires("wf14", w, h, 1409)), 11: ("#4A5A7A", lambda w, h: K.hamon_gog("hg14", w, h, 1410)),
                             14: ("#4A5A7A", lambda w, h: K.hamon_gog("hg14b", w, h, 1411)), 17: ("#3A2A3A", lambda w, h: K.birds_gather(w, h, 1412)),
                             21: ("#3A4A8A", lambda w, h: K.sanctuary_midst("sm14", w, h, 1413)), 25: (MAP, lambda w, h: K.exile_map(w, h, inward=True)),
                             29: ("#6AB0D8", lambda w, h: K.gathered(w, h, 1414))},
            faces=FZ, heads={1: "Behold, I Am against Thee, O Gog", 9: "Fires of the Weapons", 11: "The Valley of Hamon-gog", 17: "Assemble Yourselves",
                             21: "I Will Set My Glory among the Nations", 25: "Now Will I Bring Back the Captivity of Jacob"})
PG.extend(pack(SEGS, "EZK-C14-D", PG.next(), end=end_mark("NEXT · THE MEASURING REED", "right: 10px; bottom: 34px")))
