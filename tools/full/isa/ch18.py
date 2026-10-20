"""Isaiah volume, Chapter 18 — New Heavens and a New Earth (Isaiah 63–66), the last chapter of Isaiah. Every verse, word for word
from ref/eng-asv. Who is this that cometh from Edom? — I have trodden the winepress alone (63:1–6 words over an empty winepress
running red at sunset: no one drawn); the lovingkindnesses of Jehovah, the angel of his presence, Moses and the sea, the cattle
going down into the valley; look down from heaven; oh that thou wouldest rend the heavens; we are the clay, and thou our potter;
Zion a wilderness, the house burned with fire; I am found of them that sought me not — the gardens and the graves; the new wine
in the cluster; a table for Fortune and Destiny; my servants shall eat; behold, I create new heavens and a new earth; the wolf and
the lamb; heaven is my throne, and the earth my footstool; shall a land be born in one day?; peace like a river, as one whom his
mother comforteth; Jehovah will come with fire; the nations bringing your brethren to the holy mountain; all flesh worshipping
from one sabbath to another; and the valley outside the city (66:24 words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art18 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ISAIAH_AWE, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch17 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C18-00-Title", "Chapter 18 · New Heavens and a New Earth", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 0)">{K.new_heavens(760, 1080, 1801)}</g>')
    return chapter_title(18, "第十八話", "New Heavens and a New Earth", "Isaiah 63 – 66", svg, "#3A6A9A", v("65:17", to="a new earth;"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("63:1-3", "god", A(lambda w, h: K.winepress_alone(w, h, 1802), "#3A0A14"), pre=("say", "greatness of his strength?"), kinds={2: "say"}, head="Who Is This That Cometh from Edom?", budget=700)
    + S("63:4-6", "god", ISAIAH_STERN)
    + S("63:7-10", "say", [ISAIAH_JOY, ISAIAH_GRIEF], split=[10], head="The Lovingkindnesses of Jehovah")
    + S("63:11-13", "say", A(lambda w, h: K.sea_way(w, h, 1803), SKY))
    + S("63:14", "say", A(lambda w, h: K.cattle_valley(w, h, 1804), "#7A8AC8"))
    + S("63:15-17", "say", [A(lambda w, h: K.look_down(w, h, 1805), "#2A3A6A"), ISAIAH_GRIEF], split=[16], head="Look Down from Heaven")
    + S("63:18-19", "say", ISAIAH_GRIEF)
    + S("64:1-4", "say", [A(lambda w, h: K.rend_heavens(w, h, 1806), "#14102A"), ISAIAH_AWE], split=[3], head="Oh That Thou Wouldest Rend the Heavens")
    + S("64:5-7", "say", [ISAIAH_GRIEF, A(lambda w, h: K.fading_leaf(w, h, 1807), "#6A6A7A")], at={6: A(lambda w, h: K.fading_leaf(w, h, 1807), "#6A6A7A")})
    + S("64:8-9", "say", A(lambda w, h: K.potter("pt18", w, h, 1808), "#5A3A2A"))
    + S("64:10-12", "say", A(lambda w, h: K.zion_wilderness(w, h, 1809), "#2A0A0A"))
    + S("65:1-2", "god", [ISAIAH], head="I Am Found of Them That Sought Me Not")
    + S("65:3-5", "god", A(lambda w, h: K.graves_gardens(w, h, 1810), "#0B0B2A"))
    + S("65:6-7", "god", ISAIAH_STERN)
    + S("65:8-10", "god", [A(lambda w, h: K.cluster(w, h, 1811), "#C8B898"), A(lambda w, h: K.sharon_fold(w, h, 1812), SKY)], split=[10])
    + S("65:11-12", "god", A(lambda w, h: K.fortune_table(w, h, 1813), "#2A1A24"))
    + S("65:13-16", "god", [ISAIAH_STERN, ISAIAH], split=[15])
    + S("65:17-19", "god", A(lambda w, h: K.new_heavens(w, h, 1814), "#5AA8E8"), head="New Heavens and a New Earth", budget=600)
    + S("65:20-23", "god", [ISAIAH_JOY, A(lambda w, h: K.build_plant("bp18", w, h, 1815), SKY)], split=[21])
    + S("65:24-25", "god", A(lambda w, h: K.peace_mountain("pm18", w, h, 1816), SKY))
    + S("66:1-2", "god", A(lambda w, h: K.throne_footstool(w, h, 1817), "#05050A", h=520), head="Heaven Is My Throne")
    + S("66:3-4", "god", ISAIAH_STERN)
    + S("66:5-6", "god", [ISAIAH, ISAIAH_STERN], pre=("say", "ye that tremble at his word:"), kinds={6: "say"}, split=[6])
    + S("66:7-9", "say", A(lambda w, h: K.land_born("lb18", w, h, 1818), "#6A7ABA"), kinds={9: "god"}, head="Shall a Land Be Born in One Day?", budget=600)
    + S("66:10-11", "say", ZION_JOY)
    + S("66:12-14", "god", [A(lambda w, h: K.river_waves(w, h, 1819), "#7AB8E8"), A(lambda w, h: K.nursing("nu18", w, h, 1820), "#5A4A7A"), ISAIAH_JOY], split=[13, 14])
    + S("66:15-17", "say", [A(lambda w, h: K.storm_far(w, h, 1821), "#1A0A1A"), ISAIAH_STERN], kinds={17: "god"}, split=[17])
    + S("66:18-19", "god", A(lambda w, h: K.nations_map(w, h, hi=("TARSHISH", "KITTIM", "EGYPT", "ETHIOPIA"), arrows=(("JERUSALEM", "TARSHISH"), ("JERUSALEM", "KITTIM"), ("JERUSALEM", "EGYPT")),
                                                              lit="#FFD23F", show=["JERUSALEM", "TARSHISH", "KITTIM", "EGYPT", "ETHIOPIA", "BABYLON", "MEDIA"]), MAP), head="I Will Gather All Nations", budget=600)
    + S("66:20-21", "god", A(lambda w, h: K.brethren_brought("bb18", w, h, 1822), "#8FB0D8"), budget=600)
    + S("66:22-23", "god", A(lambda w, h: K.every_knee("ek18", w, h, 1823), "#5A6ABA"))
    + S("66:24", "god", A(lambda w, h: K.outside_valley(w, h, 1824), "#2A1A2A"))
)
PG.extend(pack(SEGS, "ISA-C18-D", PG.next(), end=end_mark("END OF ISAIAH · NEXT · JEREMIAH", "right: 10px; bottom: 34px", ch="完")))
