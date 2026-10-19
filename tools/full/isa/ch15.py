"""Isaiah volume, Chapter 15 — A Man of Sorrows (Isaiah 52–55). Every verse, word for word from ref/asv.
Awake, awake, O Zion — shake thyself from the dust; ye were sold for nought; how beautiful upon the mountains are the feet of
him that bringeth good tidings; the watchmen sing; depart ye, ye that bear the vessels of Jehovah; then the servant (never
drawn: 52:13–53:12 are words over a root out of a dry ground, an empty road at dusk, sheep gone astray, a lamb silent before
its shearers, an empty grave hewn in the rock, an empty throne in light); sing, O barren — enlarge the place of thy tent; the
waters of Noah and the covenant of peace; thy stones in fair colors (a plate); no weapon formed against thee shall prosper;
ho, every one that thirsteth; seek ye Jehovah while he may be found; as the rain and the snow; and the trees of the field
clapping their hands."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art15 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ISAIAH_AWE, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch14 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C15-00-Title", "Chapter 15 · A Man of Sorrows", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 0)">{K.dry_root(760, 1080, 1501)}</g>')
    return chapter_title(15, "第十五話", "A Man of Sorrows", "Isaiah 52 – 55", svg, "#8A6A3A", v("53:3", to="acquainted with grief:"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("52:1-2", "say", A(lambda w, h: K.zion_rise("zr15", w, h, 1502), "#6A7ABA"), head="Awake, Awake, O Zion")
    + S("52:3-6", "god", [ISAIAH, ISAIAH_STERN, ISAIAH], split=[5, 6])
    + S("52:7-8", "song", A(lambda w, h: K.good_tidings("gt15", w, h, 1503), "#5A6ABA"), head="How Beautiful upon the Mountains")
    + S("52:9-10", "song", A(lambda w, h: K.light_nations(w, h), MAP))
    + S("52:11-12", "say", A(lambda w, h: K.vessels_out("vo15", w, h, 1504), "#C88A5A"))
    + S("52:13-15", "god", A(lambda w, h: K.portion(w, h, 1505), "#1A1438"), head="Behold, My Servant")
    + S("53:1-2", "say", A(lambda w, h: K.dry_root(w, h, 1506), "#C8A880"), head="A Root out of a Dry Ground")
    + S("53:3", "say", A(lambda w, h: K.sorrows_dusk(w, h, 1507), "#2A2040"), head="A Man of Sorrows")
    + S("53:4-5", "say", ISAIAH_GRIEF)
    + S("53:6", "say", A(lambda w, h: K.stray_sheep(w, h, 1508), "#8FB0D8"))
    + S("53:7", "say", A(lambda w, h: K.silent_lamb(w, h, 1509), "#C8B8A8", h=340))
    + S("53:8-9", "say", A(lambda w, h: K.rich_grave(w, h, 1510), "#5A6ABA"))
    + S("53:10", "say", ISAIAH_GRIEF)
    + S("53:11-12", "god", A(lambda w, h: K.portion(w, h, 1511), "#1A1438"))
    + S("54:1-3", "god", [A(lambda w, h: K.barren_tent("bt15", w, h, 1512), SKY), ISAIAH_JOY], split=[3], head="Sing, O Barren")
    + S("54:4-8", "god", [ISAIAH_JOY, ISAIAH], split=[6])
    + S("54:9-10", "god", A(lambda w, h: K.noah_bow(w, h, 1513), "#6A8AB8"), head="The Waters of Noah")
    + S("54:11-12", "god", A(lambda w, h: K.fair_stones(w, h), MAP, h=380))
    + S("54:13-15", "god", ISAIAH_JOY)
    + S("54:16-17", "god", A(lambda w, h: K.smith_coals("sc15", w, h, 1514), "#2A1A16", h=420))
    + S("55:1-3", "god", [A(lambda w, h: K.come_waters("cw15", w, h, 1515), SKY, h=460), ISAIAH_JOY], split=[3], head="Ho, Every One That Thirsteth")
    + S("55:4-5", "god", ISAIAH)
    + S("55:6-7", "say", ISAIAH, head="Seek Ye Jehovah While He May Be Found")
    + S("55:8-9", "god", A(lambda w, h: K.circle_earth(w, h, 1516), "#05050A"))
    + S("55:10-11", "god", A(lambda w, h: K.rain_snow(w, h, 1517), "#7A9AC8"))
    + S("55:12-13", "god", A(lambda w, h: K.trees_clap(w, h, 1518), "#5A9AD8"))
)
PG.extend(pack(SEGS, "ISA-C15-D", PG.next(), end=end_mark("NEXT · THE FAST THAT I HAVE CHOSEN", "right: 10px; bottom: 34px")))
