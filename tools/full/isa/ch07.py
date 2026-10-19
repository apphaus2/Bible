"""Isaiah volume, Chapter 7 — Thy Dead Shall Live (Isaiah 24–27). Every verse, word for word from ref/asv.
Jehovah maketh the earth empty; the city of confusion shut up and its gate smitten; the gleanings of the vintage; fear, and
the pit, and the snare — the earth reeling like a hammock; the sun ashamed and Zion in glory; the song of praise and the
stronghold in the storm; the feast of fat things on the mountain and the veil destroyed — he hath swallowed up death for
ever; the song of the strong city; with my soul have I desired thee in the night; thy dead shall live (the dew of herbs at
dawn); enter thou into thy chambers; leviathan the swift serpent (the serpent in the sea, no one drawn); the vineyard of
wine and its keeper; the altar's stones as chalkstones; and the great trumpet."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art7 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY = "#8FC8E8"


@P("ISA-C07-00-Title", "Chapter 7 · Thy Dead Shall Live", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FC8E8"></rect><g transform="translate(0 200)">{K.feast_mountain("t7", 760, 880, 701)}</g>')
    return chapter_title(7, "第七話", "Thy Dead Shall Live", "Isaiah 24 – 27", svg, "#3A5A8A", v("25:8", to="from off all faces;"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("24:1-6", "say", [A(lambda w, h: K.earth_empty("ee7", w, h, 702), "#4A4A5A"), ISAIAH_STERN], head="The Earth Made Empty", split=[4])
    + S("24:7-12", "say", [ISAIAH_GRIEF, A(lambda w, h: K.gate_smitten(w, h, 703), "#5A5A6A")], split=[10])
    + S("24:13-16", "say", [A(lambda w, h: K.olive_gleaning("og7", w, h, 704), "#C8B8A0"), ISAIAH_JOY, ISAIAH_GRIEF], split=[14, 16])
    + S("24:17-20", "say", [ISAIAH_STERN, A(lambda w, h: K.earth_reels(w, h, 705), "#1A1A2A")], split=[19], head="Fear, and the Pit, and the Snare")
    + S("24:21-23", "say", [ISAIAH, A(lambda w, h: K.sun_moon_zion(w, h, 706), "#2A2A4A")], split=[23])
    + S("25:1-5", "song", [ZION_JOY, A(lambda w, h: K.stronghold("sg7", w, h, 707), "#2A2A3A")], split=[4], head="O Jehovah, Thou Art My God")
    + S("25:6-8", "say", A(lambda w, h: K.feast_mountain("fm7", w, h, 708), SKY), head="He Hath Swallowed Up Death", budget=700)
    + S("25:9", "song", ZION_JOY, pre=("cap", "And it shall be said in that day,"))
    + S("25:10-12", "say", ISAIAH_STERN)
    + S("26:1-6", "song", [A(lambda w, h: K.strong_city("sc7", w, h, 709), SKY), ZION_JOY], pre=("cap", "in the land of Judah:"), head="We Have a Strong City", split=[3])
    + S("26:7-11", "song", [A(lambda w, h: K.night_seek("ns7", w, h, 710), "#1A1428"), ISAIAH], split=[9, 10])
    + S("26:12-15", "song", [ZION_JOY, ISAIAH])
    + S("26:16-18", "song", ZION)
    + S("26:19", "song", A(lambda w, h: K.dew_dawn(w, h, 711), "#5A6ABA"), head="Thy Dead Shall Live")
    + S("26:20", "god", A(lambda w, h: K.chambers(w, h, 712), "#14142A"))
    + S("26:21", "say", ISAIAH_STERN)
    + S("27:1", "say", A(lambda w, h: K.leviathan(w, h, 713), "#0B1428"), head="Leviathan the Swift Serpent")
    + S("27:2-5", "god", [A(lambda w, h: K.vineyard("vy7", w, h, 714), "#8FD0E2"), ISAIAH], pre=("cap", "In that day:"), kinds={2: "song"}, split=[4], head="A Vineyard of Wine")
    + S("27:6", "say", ISAIAH_JOY)
    + S("27:7-11", "say", [ISAIAH_STERN, A(lambda w, h: K.chalkstones("ck7", w, h, 715), "#9AB0C8")], split=[9])
    + S("27:12-13", "say", A(lambda w, h: K.great_trumpet("gt7", w, h, 716), SKY), head="A Great Trumpet", budget=600)
)
PG.extend(pack(SEGS, "ISA-C07-D", PG.next(), end=end_mark("NEXT · IN RETURNING AND REST", "right: 10px; bottom: 34px")))
