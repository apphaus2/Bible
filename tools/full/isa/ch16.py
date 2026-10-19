"""Isaiah volume, Chapter 16 — The Fast That I Have Chosen (Isaiah 56–59). Every verse, word for word from ref/asv.
Keep ye justice — the foreigner and the eunuch in the house of prayer for all peoples; his watchmen are blind, dumb dogs asleep;
the righteous perisheth and entereth into peace; ye sons of the sorceress (57:5–8 told in words only, over an empty valley of
oaks and smooth stones and a shut door on a high place); cast ye up, prepare the way; the high and holy place, and the contrite
heart; the wicked like the troubled sea; cry aloud, lift up thy voice like a trumpet; is such the fast that I have chosen? — the
bread dealt to the hungry, thy light breaking forth as the morning, a watered garden, the repairer of the breach; the sabbath a
delight; your iniquities have separated; adders' eggs and the spider's web (a plate); we grope for the wall like the blind;
truth is fallen in the street; righteousness as a breastplate (the armor laid out as a plate, no one wearing it); and a
Redeemer will come to Zion."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art16 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ISAIAH_AWE, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch15 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C16-00-Title", "Chapter 16 · The Fast That I Have Chosen", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FB0D8"></rect><g transform="translate(0 240)">{K.true_fast("t16", 760, 840, 1601)}</g>')
    return chapter_title(16, "第十六話", "The Fast That I Have Chosen", "Isaiah 56 – 59", svg, "#3A5A8A", v("58:6", to="the bands of the yoke,"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("56:1-3", "god", [ISAIAH, ISAIAH_JOY], kinds={3: "say"}, split=[3], head="Keep Ye Justice")
    + S("56:4-5", "god", ISAIAH_JOY)
    + S("56:6-8", "god", A(lambda w, h: K.house_prayer("hp16", w, h, 1602), SKY), head="A House of Prayer for All Peoples", budget=700)
    + S("56:9-12", "say", [A(lambda w, h: K.dumb_dogs(w, h, 1603), "#0B0B2A"), ISAIAH_STERN], split=[11], head="His Watchmen Are Blind")
    + S("57:1-2", "say", A(lambda w, h: K.at_rest(w, h, 1604), "#4A4A7A"), head="The Righteous Perisheth")
    + S("57:3-6", "god", [ISAIAH_STERN, A(lambda w, h: K.oaks_valley(w, h, 1605), "#3A2A3A")], split=[5])
    + S("57:7-10", "god", [A(lambda w, h: K.shut_door(w, h, 1606), "#2A2040"), ISAIAH_STERN], split=[9])
    + S("57:11-13", "god", ISAIAH_STERN)
    + S("57:14", "god", A(lambda w, h: K.way_prepared(w, h, 1607), "#E8A050"), pre=("cap", "And he will say,"))
    + S("57:15", "god", A(lambda w, h: K.high_holy("hh16", w, h, 1608), "#14123A"), head="The High and Holy Place")
    + S("57:16-19", "god", [ISAIAH, ISAIAH_JOY], split=[18])
    + S("57:20-21", "say", A(lambda w, h: K.troubled_sea(w, h, 1609), "#3A3A4A"))
    + S("58:1-2", "god", A(lambda w, h: K.trumpet_cry("tc16", w, h, 1610), "#8A6A8A"), head="Cry Aloud, Spare Not")
    + S("58:3-5", "god", [ISAIAH_STERN, A(lambda w, h: K.false_fast("ff16", w, h, 1611), "#8A7A6A")], split=[5])
    + S("58:6-7", "god", A(lambda w, h: K.true_fast("tf16", w, h, 1612), "#8FB0D8"), head="Is Not This the Fast That I Have Chosen?", budget=700)
    + S("58:8-11", "god", [A(lambda w, h: K.light_morning(w, h, 1613), "#6A7ABA"), ISAIAH_JOY], split=[10])
    + S("58:12", "god", A(lambda w, h: K.repairer("rp16", w, h, 1614), SKY, h=400))
    + S("58:13-14", "god", A(lambda w, h: K.sabbath_rest("sr16", w, h, 1615), "#5A6ABA"))
    + S("59:1-4", "say", [ISAIAH_STERN, ISAIAH_GRIEF], split=[3], head="Your Iniquities Have Separated")
    + S("59:5-6", "say", A(lambda w, h: K.eggs_web(w, h), MAP))
    + S("59:7-8", "say", ISAIAH_STERN)
    + S("59:9-11", "say", A(lambda w, h: K.grope_wall("gw16", w, h, 1616), "#4A4A5A"), head="We Grope for the Wall")
    + S("59:12-13", "say", ISAIAH_GRIEF)
    + S("59:14-16", "say", [A(lambda w, h: K.truth_fallen(w, h, 1617), "#6A5A6A"), ISAIAH], split=[16])
    + S("59:17-19", "say", [A(lambda w, h: K.armor(w, h), MAP, h=400), A(lambda w, h: K.rushing_stream(w, h, 1618), "#5A7ABA")], split=[18], head="Righteousness as a Breastplate")
    + S("59:20-21", "god", ISAIAH_JOY, head="A Redeemer Will Come to Zion")
)
PG.extend(pack(SEGS, "ISA-C16-D", PG.next(), end=end_mark("NEXT · ARISE, SHINE", "right: 10px; bottom: 34px")))
