"""1 John volume, Chapter 2 — God Is Love (1 John 3–5). Every verse, word for word from ref/eng-asv.
1 John 3: "Behold what manner of love" — the church and its children on a hill under the stars, a soft light on them from
above (no figure in it); "we shall see him even as he is" — Jesus risen in white light on the hill at morning, the brethren
below; sin and the works of the devil in words beside John's face (the devil never drawn); not as Cain — the field at dusk
with two altars, one smoke rising and one beaten down, a mattock in the furrow, Genesis' Cain in a framed portrait, angry
and marked, and no one in the field; "whosoever hateth his brother is a murderer" over the same field by night, empty; he
laid down his life for us — three crosses far off under a darkened sky; the brother in need at the rich man's shut door.
1 John 4: prove the spirits — the assayer's touchstone, balance and crucible as a plate; "God is love" — a warm light from
above on the brethren at a house door; the Son sent into the world — Bethlehem under its star, no one drawn; "we have
beheld" — Jesus on the beach at daybreak; perfect love casteth out fear — a child running out of the night into its mother's
arms at a lit door. 1 John 5: the victory that overcometh the world, a laurel wreath in the light over the city; the water,
the blood and the Spirit as an emblem of three medallions (a pitcher pouring water, a cup, the dove of light: nothing drawn
as blood); the letter read back in the study; John handing the sealed letter to the bearer at the door; "guard yourselves
from idols" — images on their plinths in a colonnade and a cold altar, no one at it."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jn1 import G, art as A, ch01 as _prev
from jn1.common import (K, Pages, D, F, lt, lts, lp, ltj, v, title, fin, JOHN_OLD, JOHN_LAMP, JOHN_STERN, JOHN_JOY, JOHN_GRIEF, GOLD_BG, LAMP_BG, STERN_BG,
                        JOY_BG, GRIEF_BG)
from gal.art import art

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1JN-C02-00-Title", "Chapter 2 · God Is Love", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#5A2A4A"></rect><g transform="translate(0 300)">{A.love_light("t02", 760, 700, 1300)}</g>'
    return title(2, "God Is Love", "1 John 3–5", svg, "#5A2A4A", v("4:8", frm="God is love."))


BEARER = dict(cloth="#4A6A6A", head="#2A5A5A", beard="#4A2E1E")          # the brother who carries the letter (a dark-teal headcloth)

SEGS = [
    # 1 John 3 — children of God; not as Cain; love in deed and truth
    D(lp("3:1"), art(A.children_stars, "cs1", 1301), "#05051A", head="Behold What Manner of Love", sky=3, art_h=260),
    D(lp("3:2-3"), art(A.see_him, "sh1", 1302), "#3A3A7A", head="We Shall Be Like Him", art_h=250),
    F(lp("3:4-6"), JOHN_OLD),
    F(lp("3:7-10"), JOHN_STERN, bg=STERN_BG, head="Let No Man Lead You Astray"),
    D(lp("3:11-12"), art(A.cain_field, "cf1", 1311), "#3A1A2A", head="Not as Cain", art_h=250),
    D(lp("3:13-15"), art(A.cain_field, "cf2", 1313, night_=True), "#0B0B2A", art_h=210),
    D(lp("3:16"), art(A.far_crosses, 1316), "#05050E", head="He Laid Down His Life for Us", art_h=210),
    D(lp("3:17-18"), art(A.shut_heart, "sh2", 1317), "#3A2A5A", head="In Deed and Truth", art_h=240),
    F(lp("3:19-22"), JOHN_LAMP, bg=LAMP_BG),
    D(lp("3:23-24"), art(A.love_feast, "lf1", 1323), "#6A4A34", art_h=240),
    # 1 John 4 — prove the spirits; God is love; perfect love casteth out fear
    D(lp("4:1-3"), art(A.assay), "#0B1A2E", head="Prove the Spirits", sky=4, art_h=320),
    F(lp("4:4-6"), JOHN_OLD),
    D(lp("4:7-8"), art(A.love_light, "ll1", 1407), "#5A2A4A", head="God Is Love", art_h=260),
    D(lp("4:9-10"), art(A.fulness_star, "fs1", 1409), "#05051A", head="He Sent His Son", art_h=230),
    F(lp("4:11-13"), JOHN_JOY, bg=JOY_BG),
    D(lp("4:14-16"), art(A.beach, "bc1", 1414), "#3A3A7A", head="We Have Beheld", art_h=240),
    D(lp("4:17-18"), art(A.no_fear, "nf1", 1417), "#05050E", head="Perfect Love Casteth Out Fear", art_h=250),
    F(lp("4:19-21"), JOHN_OLD),
    # 1 John 5 — the victory; three that bear witness; guard yourselves from idols
    D(lp("5:1-5"), art(A.victory, 1501), "#2A2A6A", head="The Victory That Overcometh", sky=5, art_h=230),
    D(lp("5:6-8"), art(A.three_witness, "tw1"), "#0B1A2E", head="Three Who Bear Witness", art_h=260),
    F(lp("5:9-12"), JOHN_OLD),
    D(lp("5:13-15"), art(A.study_john, "sj2", 1513, stage="read"), "#3A2418", head="That Ye May Know", art_h=250),
    F(lp("5:16-17"), JOHN_GRIEF, bg=GRIEF_BG),
    D(lp("5:18-20"), art(A.study_john, "sj3", 1518, stage="give", bearer=BEARER), "#3A2418", art_h=250),
    D([lt("5:21")], art(A.idols_cold, "ic1", 1521), "#2A1E3A", head="Guard Yourselves from Idols", art_h=280),
]
PG.extend(K.pack(SEGS, "1JN-C02-D", PG.next(), end=fin("END OF 1 JOHN · NEXT · 2 JOHN")))
