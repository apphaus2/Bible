"""Isaiah volume, Chapter 14 — A Light to the Gentiles (Isaiah 49–51). Every verse, word for word from ref/asv.
The servant's words (he is never drawn: his words stand over his tokens) — listen, O isles; a sharp sword and a polished shaft
hid in the quiver (a plate); I will give thee for a light to the Gentiles (the map lit from Zion); to them that are bound, Go
forth; Zion said, Jehovah hath forsaken me — can a woman forget her sucking child?; thy walls are continually before me;
kings thy nursing fathers; the prey taken from the mighty; the bill of your mother's divorcement; I clothe the heavens with
blackness; the servant again — he wakeneth mine ear morning by morning; I gave my back to the smiters (words over a flint
stone in the dark, nothing more drawn); the moth and the garment; they that walk by their own firebrands; look unto the rock
whence ye were hewn, and unto Abraham and Sarah; her wilderness like Eden; the heavens vanishing like smoke; awake, O arm of
Jehovah — Rahab and the dried sea; the ransomed return; awake, O Jerusalem — the cup of staggering taken out of thy hand."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art14 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ISAIAH_AWE, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch13 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"
LIGHT = A(lambda w, h: K.light_nations(w, h), MAP)


@P("ISA-C14-00-Title", "Chapter 14 · A Light to the Gentiles", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 0)">{K.light_nations(760, 1080)}</g>')
    return chapter_title(14, "第十四話", "A Light to the Gentiles", "Isaiah 49 – 51", svg, MAP, v("49:6", frm="I will also give thee"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("49:1-4", "say", [A(lambda w, h: K.sword_shaft(w, h), MAP), None], split=[3], head="Listen, O Isles, unto Me")
    + S("49:5-6", "say", LIGHT, budget=700)
    + S("49:7-9", "god", [ISAIAH, A(lambda w, h: K.prison_open("po14", w, h, 1402), "#2A2430")], split=[9])
    + S("49:10-12", "god", [A(lambda w, h: K.way_prepared(w, h, 1403), "#E8A050"), A(lambda w, h: K.four_winds(w, h), MAP)], split=[12])
    + S("49:13", "song", A(lambda w, h: K.heavens_sing(w, h, 1404), "#5A9AD8"))
    + [face([cp("49:14", to="But Zion said,"), say("49:14", frm="Jehovah hath forsaken me")], "ISA 49:14", ZION, head="Can a Woman Forget Her Sucking Child?")]
    + S("49:15", "god", A(lambda w, h: K.nursing("nu14", w, h, 1405), "#5A4A7A"))
    + S("49:16-17", "god", A(lambda w, h: K.zion_walls(w, h, 1406), MAP))
    + S("49:18-21", "god", [ISAIAH_JOY, ISAIAH], split=[19, 21])
    + S("49:22-23", "god", A(lambda w, h: K.kings_bear("kb14", w, h, 1407), "#8FB0D8"), budget=700)
    + [face([says("49:24")], "ISA 49:24", ZION)]
    + S("49:25-26", "god", ISAIAH_STERN)
    + S("50:1", "god", A(lambda w, h: K.divorcement(w, h, 1408), "#2A1A2A"), head="The Bill of Your Mother's Divorcement")
    + S("50:2-3", "god", A(lambda w, h: K.black_heavens(w, h, 1409), "#0A0A0E"))
    + S("50:4-5", "say", A(lambda w, h: K.morning_ear(w, h, 1410), "#3A2A3A"), head="He Wakeneth Mine Ear")
    + S("50:6-7", "say", A(lambda w, h: K.flint_face(w, h, 1411), "#14121A"))
    + S("50:8-9", "say", A(lambda w, h: K.moth_garment(w, h, 1412), "#5A4A3A"))
    + S("50:10-11", "say", [ISAIAH, A(lambda w, h: K.firebrand_walkers("fw14", w, h, 1413), "#0A0810")], split=[11])
    + S("51:1-3", "god", [A(lambda w, h: K.quarry(w, h, 1414), "#8FB0D8"), A(lambda w, h: K.abraham_sarah("as14", w, h, 1415), "#05051A"), A(lambda w, h: K.eden_garden(w, h, 1416), "#7AB8E8")],
        split=[2, 3], head="Look unto the Rock Whence Ye Were Hewn")
    + S("51:4-6", "god", [ISAIAH, A(lambda w, h: K.heavens_vanish(w, h, 1417), "#6A6A7A")], split=[6])
    + S("51:7-8", "god", [ISAIAH_JOY])
    + S("51:9-10", "song", A(lambda w, h: K.rahab_sea(w, h, 1418), "#0B1428"), head="Awake, O Arm of Jehovah")
    + S("51:11", "song", A(lambda w, h: K.way_holiness("wh14", w, h, 1419), "#7AB8E8"))
    + S("51:12-16", "god", [ISAIAH, ISAIAH_JOY], split=[14])
    + S("51:17-20", "say", [A(lambda w, h: K.staggering_cup(w, h, 1420), "#3A2A3A"), ISAIAH_GRIEF, A(lambda w, h: K.antelope_net(w, h, 1421), "#5A4A5A")], split=[18, 20], head="Awake, Awake, O Jerusalem")
    + S("51:21", "say", ISAIAH)
    + S("51:22-23", "god", [ISAIAH_JOY, A(lambda w, h: K.staggering_cup(w, h, 1422, others=True), "#3A2A3A")], pre=("cap", "pleadeth the cause of his people,"), split=[23])
)
PG.extend(pack(SEGS, "ISA-C14-D", PG.next(), end=end_mark("NEXT · A MAN OF SORROWS", "right: 10px; bottom: 34px")))
