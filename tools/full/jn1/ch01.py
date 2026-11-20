"""1 John volume, Chapter 1 — God Is Light (1 John 1–2). Every verse, word for word from ref/eng-asv.
1 John 1: that which was from the beginning, as three remembered scenes of the Gospel in framed insets (Jesus teaching by
the sea, the young John and Peter at his feet; Jesus on the beach at daybreak; the risen Lord in the shut room, Thomas
reaching out his hand); the letter written at Ephesus, John the elder standing with his staff and dictating, the young scribe
on his mat, the window on the theatre and Diana's temple; "God is light" as light only; the brethren walking together out of
the night into the morning; John's face beside "If we say that we have no sin". 1 John 2: an Advocate with the Father — Jesus
risen in white light before the empty throne of light (the Father never drawn), the world beneath; the darkness passing away
and the true light shining, dawn over Ephesus; he that hateth his brother walking in darkness, feeling his way by night, the
lit doorway far off; little children, fathers and young men as a plate of three cells; the world passing away, a market
street thinning into haze; "it is the last hour" and antichrist in words only beside John's stern face; the anointing as a
horn of oil pouring gold in the light; the church at Ephesus hearing the letter read by lamplight; "abide in him" beside
John's face in white light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jn1 import G, art as A
from jn1.common import (K, Pages, D, F, lt, lts, lp, ltj, v, title, nxt, JOHN_OLD, JOHN_LAMP, JOHN_STERN, JOHN_JOY, GOLD_BG, LAMP_BG, STERN_BG, JOY_BG)
from gal.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1JN-C01-00-Title", "Chapter 1 · God Is Light", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_john("t01", 760, 640, 1100, fig_h=400)}</g>'
    return title(1, "God Is Light", "1 John 1–2", svg, "#3A2418", v("2:8", frm="the darkness is passing away"))


SEGS = [
    # 1 John 1 — that which was from the beginning; God is light
    D([lt("1:1")], art(A.memory, 1101), "#1E140E", head="That Which Was from the Beginning", sky=1, art_h=300),
    D(lp("1:2-4"), art(A.study_john, "sj1", 1102), "#3A2418", art_h=260),
    D([lt("1:5")], art(A.god_light, 1105), "#FFE680", head="God Is Light", art_h=280),
    D(lp("1:6-7"), art(A.walk_light, "wl1", 1106), "#3A2A5A", head="Walk in the Light", art_h=240),
    F(lp("1:8-10"), JOHN_OLD),
    # 1 John 2 — an Advocate; the true light; little children, fathers, young men; the last hour; abide in him
    D(lp("2:1-2"), art(A.advocate, "ad1", 1201), "#2A2060", head="An Advocate with the Father", sky=2, art_h=260),
    F(lp("2:3-6"), JOHN_LAMP, bg=LAMP_BG),
    D(lp("2:7-8"), art(A.dawn_ephesus, 1207), "#3A2A6A", head="The True Light Already Shineth", art_h=250),
    D(lp("2:9-11"), art(A.dark_road, "dr1", 1209), "#05050E", art_h=230),
    D(lts("2:12-14"), art(A.three_ages, "ta1"), "#0B1A2E", head="I Write unto You", art_h=270),
    D(lp("2:15-17"), art(A.world_passing, "wp1", 1215), "#C8906A", head="Love Not the World", art_h=250),
    F(lp("2:18-19"), JOHN_STERN, bg=STERN_BG, head="It Is the Last Hour"),
    D(lp("2:20-21"), art(A.horn_oil, 1220), "#1A1440", head="An Anointing from the Holy One", art_h=230),
    F(lp("2:22-25"), JOHN_STERN, bg=STERN_BG),
    D(lp("2:26-27"), art(A.church_read, "cr1", 1226), "#5A3E2E", art_h=240),
    F(lp("2:28-29"), JOHN_JOY, bg=JOY_BG, head="Abide in Him"),
]
PG.extend(K.pack(SEGS, "1JN-C01-D", PG.next(), end=nxt("NEXT · GOD IS LOVE")))
