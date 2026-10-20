"""Isaiah volume, Chapter 12 — Ye Are My Witnesses (Isaiah 43–45). Every verse, word for word from ref/eng-asv.
Fear not, for I have redeemed thee — through the waters and through the fire; the four quarters giving up the sons and the
daughters; the nations assembled — ye are my witnesses; a way in the sea, and a new thing — rivers in the desert; blotted out
for mine own sake; water on the thirsty, willows by the watercourses; I am the first, and I am the last; the smith and the
carpenter (a plate) and the tree half burned and half a god; the thick cloud blotted out; sing, O ye heavens; Cyrus, my
shepherd and mine anointed — the doors of brass broken before him; I form the light, and create darkness; distil, ye heavens;
woe unto him that striveth with his Maker (the potter); the labor of Egypt come over; and unto me every knee shall bow."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art12 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ISAIAH_AWE, CYRUS, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C12-00-Title", "Chapter 12 · Ye Are My Witnesses", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FB0D8"></rect><g transform="translate(0 220)">{K.witnesses("t12", 760, 860, 1201)}</g>')
    return chapter_title(12, "第十二話", "Ye Are My Witnesses", "Isaiah 43 – 45", svg, "#3A5A8A", v("43:10", to="whom I have chosen;"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("43:1-4", "god", [A(lambda w, h: K.waters_fire("wf12", w, h, 1202), SKY), ISAIAH_JOY], split=[3], head="Fear Not, for I Have Redeemed Thee")
    + S("43:5-7", "god", A(lambda w, h: K.four_winds(w, h), MAP))
    + S("43:8-13", "god", [A(lambda w, h: K.witnesses("ws12", w, h, 1203), "#8FB0D8"), ISAIAH], split=[10], head="Ye Are My Witnesses")
    + S("43:14-15", "god", ISAIAH_STERN)
    + S("43:16-17", "god", A(lambda w, h: K.sea_way(w, h, 1204), SKY), head="A Way in the Sea")
    + S("43:18-21", "god", [ISAIAH_JOY, A(lambda w, h: K.desert_beasts(w, h, 1205), "#E8A050")], split=[20])
    + S("43:22-28", "god", [ISAIAH_STERN, ISAIAH, ISAIAH_STERN], split=[25, 27])
    + S("44:1-5", "god", [ISAIAH_JOY, A(lambda w, h: K.willows(w, h, 1206), "#7A9AC8"), ISAIAH], split=[3, 5], head="Fear Not, O Jacob My Servant")
    + S("44:6-8", "god", ISAIAH, head="I Am the First, and I Am the Last")
    + S("44:9-11", "say", ISAIAH_STERN, head="They That Fashion a Graven Image")
    + S("44:12-14", "say", A(lambda w, h: K.idol_plate(w, h), MAP), budget=700)
    + S("44:15-17", "say", A(lambda w, h: K.half_tree("ht12", w, h, 1207), "#2A1A20"), budget=700)
    + S("44:18-20", "say", ISAIAH_GRIEF)
    + S("44:21-22", "god", A(lambda w, h: K.cloud_blotted(w, h, 1208), "#5A9AD8"))
    + S("44:23", "song", A(lambda w, h: K.heavens_sing(w, h, 1209), "#5A9AD8"))
    + S("44:24-28", "god", [ISAIAH, ISAIAH_JOY], split=[26], head="Cyrus, My Shepherd")
    + S("45:1-3", "god", [A(lambda w, h: K.brass_doors("bd12", w, h, 1210), "#C86A3A"), CYRUS], pre=("cap", "to Cyrus,"), split=[2], head="To His Anointed, to Cyrus")
    + S("45:4-6", "god", CYRUS)
    + S("45:7", "god", A(lambda w, h: K.light_dark(w, h, 1211), "#05051A"))
    + S("45:8", "god", A(lambda w, h: K.distil(w, h, 1212), "#8FB8E8"))
    + S("45:9-10", "say", A(lambda w, h: K.potter("pt12", w, h, 1213), "#5A3A2A"), head="Woe unto Him That Striveth with His Maker")
    + S("45:11-13", "god", [ISAIAH, ISAIAH_JOY], split=[13])
    + S("45:14", "god", A(lambda w, h: K.nations_come(w, h), MAP), budget=700)
    + S("45:15-17", "say", ISAIAH_AWE)
    + S("45:18-21", "god", [ISAIAH, ISAIAH_STERN], pre=("cap", "that formed it to be inhabited:"), split=[20])
    + S("45:22-25", "god", [A(lambda w, h: K.every_knee("ek12", w, h, 1214), "#5A6ABA"), ISAIAH_JOY], split=[24], head="Every Knee Shall Bow")
)
PG.extend(pack(SEGS, "ISA-C12-D", PG.next(), end=end_mark("NEXT · GO YE FORTH FROM BABYLON", "right: 10px; bottom: 34px")))
