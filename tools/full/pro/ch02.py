"""Proverbs volume, Chapter 2 — Get Wisdom (Proverbs 4–6). Every verse, word for word from ref/eng-asv.
Hear, my sons, the instruction of a father: Solomon remembers David teaching him (David's words beside David's old face);
the son running on the straight road; the path of the righteous as the dawning light and the way of the wicked as
darkness; keep thy heart. The strange woman never drawn: a shut door at dusk, the son walking the other way; the young
man mourning at his latter end; thine own cistern and well; the fountain with a hind and a doe. Surety struck at the gate,
the roe and the bird escaping; go to the ant, thou sluggard; the sluggard asleep and poverty coming as an armed man; the
six things, yea seven, as numbered signs (no blood drawn); the commandment a lamp; fire and coals; the hungry thief."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art2 as K
from pro.common import (pack, cp, say, sg, sgs, says, caps, face, drawn, joined, SOLOMON, SOLOMON_WISE, SOLOMON_STERN, DAVID_OLD, YOUTH_RUE,
                        COLD, GOLDEN, RED)
from pro import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C02-00-Title", "Chapter 2 · Get Wisdom", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A8FC8"></rect><g transform="translate(0 300)">{K.run_path("t2", 760, 780, 201)}</g>')
    return chapter_title(2, "第二話", "Get Wisdom", "Proverbs 4 – 6", svg, "#5A8FC8", v("4:7", to="get wisdom;"), "Proverbs · Volume Twenty")


SEGS = [face([says("4:1-2")], "4:1-2", SOLOMON, head="Get Wisdom", stamp=4),
        drawn(sgs("4:3"), "4:3", lambda w, h: K.david_teaching("dt2", w, h, 202), "#4A2A18", h=380),
        face([cp("4:4", to="said unto me:"), joined("say", ("4:4", "Let thy heart"), "4:5", "4:6")], "4:4-6", DAVID_OLD),
        face([says("4:7-9")], "4:7-9", DAVID_OLD, bg=COLD),
        drawn(sgs("4:10-13"), "4:10-13", lambda w, h: K.run_path("rp2", w, h, 203), "#5A8FC8"),
        face([says("4:14-17")], "4:14-17", SOLOMON_STERN, bg=RED, head="The Path of the Wicked"),
        drawn(sgs("4:18-19"), "4:18-19", lambda w, h: K.two_ways(w, h, 204), "#14141E", h=360),
        face([says("4:20-23")], "4:20-23", SOLOMON_WISE, bg=COLD, head="Keep Thy Heart"),
        drawn(sgs("4:24-27"), "4:24-27", lambda w, h: K.straight_path(w, h, 205), "#5A8FC8"),
        face([says("5:1-6")], "5:1-6", SOLOMON_STERN, bg=RED, head="The Lips of a Strange Woman", stamp=5),
        drawn(sgs("5:7-8"), "5:7-8", lambda w, h: K.door_away("da2", w, h, 206), "#1A0A1A", h=340),
        face([says("5:9-14")], "5:9-14", YOUTH_RUE, bg=COLD),
        drawn(sgs("5:15-17"), "5:15-17", lambda w, h: K.well_home("wh2", w, h, 207), "#8FD0E2", head="Thine Own Well"),
        drawn(sgs("5:18-19"), "5:18-19", lambda w, h: K.hinds_fountain(w, h, 208), "#8FD0E2"),
        face([says("5:20-23")], "5:20-23", SOLOMON_STERN, bg=RED),
        drawn(sgs("6:1-3"), "6:1-3", lambda w, h: K.handshake("hs2", w, h, 209), "#FFE3B8", head="Surety for Thy Neighbor", stamp=6),
        drawn(sgs("6:4-5"), "6:4-5", lambda w, h: K.roe_flee(w, h, 210), "#8FD0E2"),
        drawn(sgs("6:6-8"), "6:6-8", lambda w, h: K.ant_hill(w, h, 211), "#FFE3B8"),
        drawn(sgs("6:9-11"), "6:9-11", lambda w, h: K.sluggard_bed("sb2", w, h, 212), "#6A4A3A", h=360),
        face([says("6:12-15")], "6:12-15", SOLOMON_STERN, bg=RED, head="A Worthless Person"),
        drawn(sgs("6:16-19"), "6:16-19", lambda w, h: K.seven(w, h, 213), "#14102A", h=380),
        face([says("6:20-22")], "6:20-22", SOLOMON, head="The Commandment Is a Lamp"),
        drawn(sgs("6:23-24"), "6:23-24", lambda w, h: K.lamp_light(w, h, 214), "#0B0B2A", h=340),
        face([says("6:25-26")], "6:25-26", SOLOMON_STERN, bg=RED),
        drawn(sgs("6:27-29"), "6:27-29", lambda w, h: K.coals_scene(w, h, 215), "#1A0A0A"),
        drawn(sgs("6:30-31"), "6:30-31", lambda w, h: K.thief("th2", w, h, 216), "#05050A"),
        face([says("6:32-35")], "6:32-35", SOLOMON_STERN, bg=RED)]
PG.extend(pack(SEGS, "PRO-C02-D", PG.next(), end=end_mark("NEXT · WISDOM HATH BUILDED HER HOUSE", "right: 10px; bottom: 34px")))
