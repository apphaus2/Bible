"""Proverbs volume, Chapter 3 — Wisdom Hath Builded Her House (Proverbs 7–9). Every verse, word for word from ref/asv.
Keep my words; say unto wisdom, Thou art my sister. Proverbs 7 drawn with restraint: the father at his lattice over the
street at twilight, the young man passing near the corner, a far veiled figure there; her words in song boxes over the
empty street, the shut house with its lamp and the full moon on the road; the ox led on its rope and the bird to the net;
the stair going down into the dark. Wisdom crying on the high places where the paths meet, her words beside her face;
better than rubies; by me kings reign; Jehovah possessed me in the beginning — the deep before the mountains, the circle
on the face of the deep, the habitable earth (God never drawn); her house of seven pillars and her table; the scoffer and
the wise; the foolish woman at the door of her house far off, and the depths of Sheol."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art3 as K
from pro.common import (pack, cp, say, sg, sgs, says, caps, face, drawn, joined, SOLOMON, SOLOMON_WISE, SOLOMON_STERN, WISDOM, WISDOM_STERN,
                        COLD, GOLDEN, RED)
from pro import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C03-00-Title", "Chapter 3 · Wisdom Hath Builded Her House", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 280)">{K.seven_pillars("t3", 760, 700, 301)}</g><rect x="0" y="910" width="760" height="170" fill="#E8C88A"></rect>')
    return chapter_title(3, "第三話", "Wisdom Hath Builded Her House", "Proverbs 7 – 9", svg, "#5A8FC8", v("9:1"), "Proverbs · Volume Twenty")


SEGS = [face([says("7:1-3")], "7:1-3", SOLOMON, head="Keep My Words", stamp=7),
        drawn(sgs("7:4-5"), "7:4-5", lambda w, h: K.wisdom_son("ws3", w, h, 302), "#8FD0E2", h=360),
        drawn(sgs("7:6-9"), "7:6-9", lambda w, h: K.lattice_window("lw3", w, h, 303), "#2A1A4A", h=400, head="At the Window of My House"),
        drawn(sgs("7:10-12"), "7:10-12", lambda w, h: K.corner_dusk("cd3", w, h, 304), "#1A0A2A"),
        drawn(sgs("7:13-15"), "7:13-15", lambda w, h: K.corner_dusk("cd3b", w, h, 305, figure=False), "#1A0A2A"),
        drawn(sgs("7:16-18"), "7:16-18", lambda w, h: K.shut_house("sh3", w, h, 306), "#05050A"),
        drawn(sgs("7:19-20"), "7:19-20", lambda w, h: K.moon_road(w, h, 307), "#05050A"),
        drawn(sgs("7:21-23"), "7:21-23", lambda w, h: K.ox_snare("ox3", w, h, 308), "#C8B8A0"),
        face([says("7:24-25")], "7:24-25", SOLOMON_STERN, bg=RED),
        drawn(sgs("7:26-27"), "7:26-27", lambda w, h: K.stair_down(w, h, 309), "#05050A", h=330),
        drawn(sgs("8:1-3"), "8:1-3", lambda w, h: K.high_place("hp3", w, h, 310), "#8FD0E2", h=440, head="Doth Not Wisdom Cry?", stamp=8),
        face([says("8:4-9")], "8:4-9", WISDOM),
        drawn(sgs("8:10-11"), "8:10-11", lambda w, h: K.emb_art("chest", w, h, 311, k=min(2.4, h / 120)), "#1A1430"),
        face([says("8:12-14")], "8:12-14", WISDOM_STERN, bg=RED),
        drawn(sgs("8:15-16"), "8:15-16", lambda w, h: K.emb_art("king_people", w, h, 312, k=min(2.4, h / 120)), "#8FD0E2"),
        face([says("8:17-21")], "8:17-21", WISDOM),
        drawn(sgs("8:22-26"), "8:22-26", lambda w, h: K.before_earth(w, h, 313), "#05050A", head="Jehovah Possessed Me in the Beginning"),
        drawn(sgs("8:27-29"), "8:27-29", lambda w, h: K.circle_deep(w, h, 314), "#05050A"),
        drawn(sgs("8:30-31"), "8:30-31", lambda w, h: K.habitable_earth("he3", w, h, 315), "#8FD0E2", h=380),
        face([says("8:32-36")], "8:32-36", WISDOM, bg=COLD),
        drawn(sgs("9:1-3"), "9:1-3", lambda w, h: K.seven_pillars("sp3", w, h, 316), "#8FD0E2", h=480, head="Her Seven Pillars", stamp=9),
        face([says("9:4-6")], "9:4-6", WISDOM),
        face([says("9:7-9")], "9:7-9", SOLOMON_WISE, bg=COLD),
        drawn(sgs("9:10-12"), "9:10-12", lambda w, h: K.emb_art("scroll", w, h, 317, k=min(2.2, h / 120)), "#12113A"),
        drawn(sgs("9:13-15"), "9:13-15", lambda w, h: K.folly_door("fd3", w, h, 318), "#2A1A3A", h=360, head="The Foolish Woman"),
        drawn(sgs("9:16-18"), "9:16-18", lambda w, h: K.stair_down(w, h, 319), "#05050A")]
PG.extend(pack(SEGS, "PRO-C03-D", PG.next(), end=end_mark("NEXT · A WISE SON", "right: 10px; bottom: 34px")))
