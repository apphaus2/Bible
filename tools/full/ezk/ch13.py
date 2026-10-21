"""Ezekiel volume, Chapter 13 — The Valley of Dry Bones (Ezekiel 35–37). Every verse, word for word from ref/asv.
Against mount Seir, a perpetual desolation (red mountains, empty cities); then to the mountains of Israel — ye shall shoot
forth your branches, ye shall be tilled and sown; for mine holy name's sake: I will sprinkle clean water upon you, a new
heart also will I give you; the land become like the garden of Eden; the flocks of Jerusalem in her appointed feasts. The
valley of dry bones: a field of white bones, very many and very dry — can these bones live? O Lord Jehovah, thou knowest;
the noise and the earthquake, bone to its bone; come from the four winds, O breath; and an exceeding great army standing
upon their feet; the graves opened; the two sticks made one in thy hand; and my sanctuary in the midst of them."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art13 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_AWE,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch12 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, VB = "#0B1A2E", "#3A3A5A"


@P("EZK-C13-00-Title", "Chapter 13 · The Valley of Dry Bones", title=True)
def title(n):
    svg = title_art(lambda w, h: K.valley_bones("t13", w, h, 1301), VB)
    return chapter_title(13, "第十三話", "The Valley of Dry Bones", "Ezekiel 35 – 37", svg, "#2A2A3A", v("37:3", frm="Son of man, can these bones live?"), "Ezekiel · Volume Twenty-Six")


SEGS = run(35, 1, 15, arts={2: ("#5A2A2A", lambda w, h: K.seir(w, h, 1302)), 6: ("#5A2A2A", lambda w, h: K.seir(w, h, 1303)), 10: (MAP, lambda w, h: K.nations_map(w, h, hi=("EDOM",))),
                            14: ("#5A2A2A", lambda w, h: K.seir(w, h, 1304))},
           faces=FZ, heads={1: "O Mount Seir", 10: "These Two Nations"})
SEGS += run(36, 1, 38, arts={1: ("#6AB0D8", lambda w, h: K.mountains(w, h, 1305, "desolate")), 4: ("#8A6A5A", lambda w, h: K.mountains(w, h, 1306, "desolate")),
                             8: ("#6AB0D8", lambda w, h: K.mountains(w, h, 1307, "fruitful")), 9: ("#6AB0D8", lambda w, h: K.tilled("tl13", w, h, 1308)),
                             13: ("#6AB0D8", lambda w, h: K.gathered(w, h, 1309)), 19: (MAP, lambda w, h: K.exile_map(w, h)),
                             24: (MAP, lambda w, h: K.exile_map(w, h, inward=True)), 25: ("#1A3A5A", lambda w, h: K.sprinkle(w, h, 1310)), 26: (MAP, lambda w, h: K.hearts(w, h)),
                             29: ("#6AB0D8", lambda w, h: K.showers(w, h, 1311)), 35: ("#6AB0D8", lambda w, h: K.eden_land(w, h, 1312)), 38: ("#6AB0D8", lambda w, h: K.feast_flocks(w, h, 1313))},
            faces=FZ, heads={1: "Ye Mountains of Israel, Hear", 8: "Ye Shall Shoot Forth Your Branches", 16: "For Mine Holy Name", 25: "A New Heart Also Will I Give You",
                             33: "Like the Garden of Eden"})
OV = {"37:1": "c", "37:2": "c", "37:3": (("c", None), ("g", "Son of man,"), ("c", "And I answered,"), ("s", "O Lord Jehovah,")), "37:7": "c", "37:8": "c", "37:10": "c"}
SEGS += [drawn(wl("37:1-2", ov=OV), "EZEK 37:1–2", lambda w, h: K.valley_bones("vb13", w, h, 1314), VB, head="The Valley Full of Bones", stamp=37, h=400),
         face(wl("37:3-4", ov=OV), "EZEK 37:3–4", EZEKIEL_AWE, bg=COLD),
         fz("37:5-6", EZEKIEL, GOLDEN),
         drawn(wl("37:7-8", ov=OV), "EZEK 37:7–8", lambda w, h: K.valley_bones("vb13b", w, h, 1315, stage=1), VB, head="Bone to Its Bone", h=380),
         drawn(wl("37:9", ov=OV), "EZEK 37:9", lambda w, h: K.valley_bones("vb13c", w, h, 1316, stage=2), VB, head="Come from the Four Winds, O Breath"),
         drawn(wl("37:10", ov=OV), "EZEK 37:10", lambda w, h: K.valley_bones("vb13d", w, h, 1317, stage=3), "#5A7AA8"),
         fz("37:11", EZEKIEL, GOLDEN, ov=OV, head="These Bones Are the Whole House of Israel"),
         dz("37:12-14", lambda w, h: K.graves_open("go13", w, h, 1318), "#3A4A7A")]
SEGS += run(37, 15, 28, arts={16: ("#2A2A3A", lambda w, h: K.sticks(w, h, 1319)), 19: ("#2A2A3A", lambda w, h: K.sticks(w, h, 1320, joined=True)),
                              21: ("#6AB0D8", lambda w, h: K.gathered(w, h, 1321)), 24: ("#6AB0D8", lambda w, h: K.david_shepherd("dv13", w, h, 1322)),
                              26: ("#3A4A8A", lambda w, h: K.sanctuary_midst("sm13", w, h, 1323))},
            faces=FZ, heads={15: "One Stick", 21: "One Nation upon the Mountains of Israel", 26: "My Sanctuary in the Midst of Them"})
PG.extend(pack(SEGS, "EZK-C13-D", PG.next(), end=end_mark("NEXT · GOG", "right: 10px; bottom: 34px")))
