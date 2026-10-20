"""Isaiah volume, Chapter 11 — Comfort Ye My People (Isaiah 40–42). Every verse, word for word from ref/eng-asv.
Comfort ye, comfort ye my people; the voice of one that crieth — prepare ye in the wilderness the way of Jehovah (the
highway, every valley exalted); all flesh is grass; the herald on a high mountain — behold, your God!; he will feed his flock
like a shepherd (the flock and the lambs, no shepherd drawn); who hath measured the waters (a plate of the measures); the
nations as a drop of a bucket; the goldsmith's image; the circle of the earth; the host of stars; they shall mount up with
wings as eagles; the islands called to judgment and one raised from the east (a map); fear thou not, thou worm Jacob — the
threshing sledge with teeth; rivers on the bare heights and the seven trees in the desert; produce your cause; behold my
servant — a bruised reed will he not break (a plate); a light of the Gentiles; sing unto Jehovah a new song; the blind led by
a way they know not; and a people robbed and snared."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art11 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ISAIAH_AWE, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C11-00-Title", "Chapter 11 · Comfort Ye My People", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 0)">{K.way_prepared(760, 1080, 1101)}</g>')
    return chapter_title(11, "第十一話", "Comfort Ye My People", "Isaiah 40 – 42", svg, "#C86A3A", v("40:1"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("40:1-2", "god", A(lambda w, h: K.comfort_city(w, h, 1102), "#6A7ABA"), head="Comfort Ye My People")
    + S("40:3-5", "say", A(lambda w, h: K.way_prepared(w, h, 1103), "#E8A050"), head="The Voice of One That Crieth")
    + S("40:6-8", "say", A(lambda w, h: K.grass_flower(w, h, 1104), "#E8B070"))
    + S("40:9-10", "say", A(lambda w, h: K.herald("hd11", w, h, 1105), "#7AA8E0"), head="Behold, Your God!")
    + S("40:11", "say", A(lambda w, h: K.flock_fold(w, h, 1106), SKY))
    + S("40:12-14", "say", A(lambda w, h: K.measures(w, h), MAP), head="Who Hath Measured the Waters?", budget=600)
    + S("40:15-17", "say", A(lambda w, h: K.bucket_drop(w, h, 1107), MAP))
    + S("40:18-20", "say", A(lambda w, h: K.goldsmith("gs11", w, h, 1108), "#3A2418"))
    + S("40:21-24", "say", [A(lambda w, h: K.circle_earth(w, h, 1109), "#05050A"), ISAIAH_AWE], split=[23])
    + S("40:25-26", "say", A(lambda w, h: K.host_stars(w, h, 1110), "#05051A"), kinds={25: "god"})
    + S("40:27-31", "say", [ISAIAH, A(lambda w, h: K.eagles(w, h, 1111), "#5A8AD0")], split=[29], head="They Shall Mount Up with Wings as Eagles")
    + S("41:1-4", "god", [ISAIAH, A(lambda w, h: K.east_one(w, h), MAP)], split=[2], head="One from the East")
    + S("41:5-7", "god", A(lambda w, h: K.goldsmith("gs11b", w, h, 1112), "#3A2418"))
    + S("41:8-13", "god", [ISAIAH_JOY, ISAIAH], head="Fear Thou Not")
    + S("41:14-16", "god", A(lambda w, h: K.threshing_sledge(w, h), MAP))
    + S("41:17-20", "god", [ISAIAH, A(lambda w, h: K.desert_trees(w, h, 1113), SKY)], split=[18])
    + S("41:21-24", "god", [ISAIAH_STERN], head="Produce Your Cause")
    + S("41:25-29", "god", [A(lambda w, h: K.east_one(w, h, note="FROM THE NORTH · FROM THE RISING OF THE SUN"), MAP), ISAIAH_STERN], split=[27])
    + S("42:1-4", "god", [ISAIAH_JOY, A(lambda w, h: K.reed_wick(w, h), MAP)], at={3: A(lambda w, h: K.reed_wick(w, h), MAP)}, head="Behold My Servant")
    + S("42:5-9", "god", [ISAIAH, A(lambda w, h: K.light_nations(w, h), MAP), ISAIAH_JOY], pre=("cap", "Thus saith God Jehovah,"), split=[6, 8])
    + S("42:10-12", "song", A(lambda w, h: K.new_song("ns11", w, h, 1114), SKY), head="Sing unto Jehovah a New Song", budget=600)
    + S("42:13-17", "say", [ISAIAH, ISAIAH_STERN], kinds={14: "god", 15: "god", 16: "god", 17: "god"}, split=[14, 17], at={16: A(lambda w, h: K.blind_led("bl11", w, h, 1115), "#14122A")})
    + S("42:18-20", "god", ISAIAH_STERN, head="Hear, Ye Deaf")
    + S("42:21-25", "say", [ISAIAH_GRIEF, A(lambda w, h: K.snared(w, h, 1116), "#4A4A5A")], split=[22, 23])
)
PG.extend(pack(SEGS, "ISA-C11-D", PG.next(), end=end_mark("NEXT · YE ARE MY WITNESSES", "right: 10px; bottom: 34px")))
