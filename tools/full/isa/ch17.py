"""Isaiah volume, Chapter 17 — Arise, Shine (Isaiah 60–62). Every verse, word for word from ref/eng-asv.
Arise, shine; for thy light is come — Zion alone in light while darkness covers the earth; the camels of Midian and Ephah, gold
and frankincense; who are these that fly as a cloud? — the ships of Tarshish; the gates open day and night; the glory of
Lebanon for the sanctuary; for brass gold (a plate) — thy walls Salvation, thy gates Praise; no more sun, but an everlasting
light; the Spirit of the Lord Jehovah is upon me (the anointed one never drawn: the horn of oil, the scroll, the prison
opened); a garland for ashes; strangers feeding your flocks; the garments of salvation, as a bride with her jewels; for Zion's
sake will I not hold my peace — a crown of beauty, Hephzi-bah and Beulah; watchmen upon thy walls; the grain eaten in the courts
of the sanctuary; and cast up the highway — Sought out, A city not forsaken."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art17 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ISAIAH_AWE, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch16 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C17-00-Title", "Chapter 17 · Arise, Shine", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 0)">{K.zion_shine(760, 1080, 1701)}</g>')
    return chapter_title(17, "第十七話", "Arise, Shine", "Isaiah 60 – 62", svg, "#05050F", v("60:1"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("60:1-3", "say", A(lambda w, h: K.zion_shine(w, h, 1702), "#05050F"), head="Arise, Shine")
    + S("60:4-6", "say", [ZION_JOY, A(lambda w, h: K.camels_gifts("cg17", w, h, 1703), "#FFB04A")], split=[6])
    + S("60:7-9", "god", [ISAIAH_JOY, A(lambda w, h: K.doves_ships(w, h, 1704), SKY)], split=[8])
    + S("60:10-12", "god", A(lambda w, h: K.open_gates("og17", w, h, 1705), "#5A4A8A"), head="Thy Gates Shall Be Open Continually", budget=600)
    + S("60:13-14", "god", A(lambda w, h: K.lebanon_sanctuary(w, h, 1706), SKY))
    + S("60:15-16", "god", ISAIAH_JOY)
    + S("60:17-18", "god", A(lambda w, h: K.brass_gold(w, h), MAP))
    + S("60:19-22", "god", [A(lambda w, h: K.everlasting_light(w, h, 1707), "#FFF4C2"), ISAIAH_JOY], split=[21])
    + S("61:1-3", "say", [A(lambda w, h: K.anointed(w, h, 1708), "#2A1A2A"), A(lambda w, h: K.garland_ashes(w, h, 1709), "#5A5A60")], split=[3],
        head="The Spirit of the Lord Jehovah Is upon Me")
    + S("61:4-7", "say", [ISAIAH_JOY], at={5: A(lambda w, h: K.strangers_flocks("sf17", w, h, 1710), SKY)}, split=[6])
    + S("61:8-9", "god", ISAIAH)
    + S("61:10-11", "song", A(lambda w, h: K.bride(w, h, 1711), "#FFE0C8"), head="The Garments of Salvation", budget=600)
    + S("62:1-3", "say", [ISAIAH_JOY, A(lambda w, h: K.crown_beauty(w, h, 1712), "#1A1438")], split=[3], head="For Zion's Sake")
    + S("62:4-5", "say", ZION_JOY)
    + S("62:6-7", "god", A(lambda w, h: K.wall_watchmen("ww17", w, h, 1713), "#05051A"))
    + S("62:8-9", "god", A(lambda w, h: K.garnered("gn17", w, h, 1714), "#FFC890"), pre=("cap", "by the arm of his strength,"))
    + S("62:10-12", "say", [A(lambda w, h: K.cast_up("cu17", w, h, 1715), "#E8A050"), ISAIAH_JOY], split=[11], head="Cast Up the Highway")
)
PG.extend(pack(SEGS, "ISA-C17-D", PG.next(), end=end_mark("NEXT · NEW HEAVENS AND A NEW EARTH", "right: 10px; bottom: 34px")))
