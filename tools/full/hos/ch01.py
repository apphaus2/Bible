"""Hosea volume, Chapter 1 — A Door of Hope (Hosea 1–3). Every verse, word for word from ref/asv.
The word of Jehovah to Hosea in the days of the kings; Go, take unto thee a wife (Hosea and Gomer before their house, never
more); the children Jezreel, Lo-ruhamah and Lo-ammi as a plate of names, the broken bow in the valley of Jezreel; the sand
of the sea and the gathering under one head; then Jehovah's controversy (2:2–13, in the Voice box, told over an empty
doorway, a hedge of thorns, the gifts taken back and the vines laid waste); the valley of Achor for a door of hope; the
covenant with the beasts and the bow broken; I will betroth thee unto me for ever; the heavens answering the earth; and
Hosea's own words in chapter 3: the woman bought for fifteen pieces of silver and a homer and a half of barley, and Israel
many days without king, prince, sacrifice, pillar, ephod or teraphim."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from hos import G, art as K
from hos.common import L, HOSEA, HOSEA_GRIEF, HOSEA_WORD, GOMER, COLD, GOLDEN, RED, NIGHT

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY, BP, DUSK, DAWN = "#8FD0E2", "#0B2A4A", "#5A3A5A", "#9AB8D8"


@P("HOS-C01-00-Title", "Chapter 1 · A Door of Hope", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.door_hope(760, 800, 101, named=False)}</g><rect x="0" y="0" width="760" height="282" fill="#5A3A5A"></rect>')
    return chapter_title(1, "第一話", "A Door of Hope", "Hosea 1 – 3", svg, "#5A3A5A", v("2:15", frm="and the valley of Achor", to="door of hope;"), "Hosea · Volume Twenty-Eight")


c, cs, s, ss, A, T, Nt, cut, gls, sp2 = L.c, L.cs, L.s, L.ss, L.A, L.T, L.N, L.cut, L.gls, L.split

SEGS = [A([cs("1:1")], "1:1", lambda w, h: K.hosea_land("hl1", w, h, 102), SKY, head="The Word of Jehovah", stamp=1),
        A([*cut("1:2", "Jehovah said unto Hosea,"), c("1:3")], "1:2-3", lambda w, h: K.house("ho1", w, h, 103, babe=True), SKY, head="Go, Take unto Thee a Wife"),
        A([*cut("1:4", "And Jehovah said unto him,"), *gls("1:5")], "1:4-5", lambda w, h: K.jezreel_bow(w, h, 104), SKY),
        A([*cut("1:6", "And Jehovah said unto him,"), *gls("1:7")], "1:6-7", lambda w, h: K.children_plate(w, h, lit=2), BP),
        A([c("1:8"), *cut("1:9", "And Jehovah said,")], "1:8-9", lambda w, h: K.children_plate(w, h, lit=3), BP),
        A([*gls("1:10")], "1:10", lambda w, h: K.sand_sea(w, h, 105), NIGHT),
        A([*gls("1:11")], "1:11", lambda w, h: K.gathered("ga1", w, h, 106), DAWN)]
PG.extend(L.pack(SEGS, "HOS-C01-D", PG.next()))

SEGS2 = [A([*gls("2:1")], "2:1", lambda w, h: K.children_plate(w, h, turned=True), BP, head="Contend with Your Mother", stamp=2),
         A([*gls("2:2-5")], "2:2-5", lambda w, h: K.house("ho2", w, h, 107, who=(), tone="dusk"), DUSK),
         A([*gls("2:6-7")], "2:6-7", lambda w, h: K.thorn_hedge(w, h, 108), SKY),
         A([*gls("2:8-9")], "2:8-9", lambda w, h: K.gifts_plate(w, h), BP),
         A([*gls("2:10-11")], "2:10-11", lambda w, h: K.gifts_plate(w, h, taken=True), BP),
         A([*gls("2:12-13")], "2:12-13", lambda w, h: K.waste_vines(w, h, 109), DUSK),
         A([*gls("2:14-15")], "2:14-15", lambda w, h: K.door_hope(w, h, 110), DUSK, head="A Door of Hope"),
         A([*gls("2:16-17")], "2:16-17", lambda w, h: K.wilderness(w, h, 111), "#E8C890"),
         A([*gls("2:18")], "2:18", lambda w, h: K.peace_land(w, h, 112), DAWN, head="I Will Betroth Thee unto Me"),
         T([*gls("2:19-20")], "2:19-20", HOSEA_WORD, GOLDEN),
         A([*gls("2:21-22")], "2:21-22", lambda w, h: K.answer_chain(w, h), BP),
         A([*gls("2:23")], "2:23", lambda w, h: K.land(w, h, 113, tone="dawn"), DAWN)]
PG.extend(L.pack(SEGS2, "HOS-C01-E", PG.next()))

SEGS3 = [T([*sp2("3:1", "And Jehovah said unto me,", "hosea", "god")], "3:1", HOSEA, GOLDEN, who="hosea", head="Go Again, Love a Woman"),
         A([ss("3:2-3", "hosea")], "3:2-3", lambda w, h: K.bought("bo1", w, h, 114), SKY, who="hosea", stamp=3),
         A([ss("3:4-5", "hosea")], "3:4-5", lambda w, h: K.without_plate(w, h), BP, who="hosea")]
PG.extend(L.pack(SEGS3, "HOS-C01-F", PG.next(), end=end_mark("NEXT · THE CAKE NOT TURNED", "right: 10px; bottom: 34px")))
