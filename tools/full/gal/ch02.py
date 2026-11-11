"""Galatians volume, Chapter 2 — The Fruit of the Spirit (Galatians 4–6). Every verse, word for word from ref/eng-asv.
Galatians 4: the heir as a child in his father's hall, under a guardian and a steward, a bondservant passing; the fulness
of the time, the star over Bethlehem (no one drawn); "Abba, Father" beside Paul's face in white light; days, months,
seasons and years as a plate; Paul grieving beside his face (his infirmity told in words) and the Galatians taking him in at
the gate; "my little children"; Hagar with Ishmael and Sarah with Isaac before Abraham's tents; mount Sinai in Arabia under
a dark sky with Hagar's portrait; the Jerusalem that is above, a city of light, with Sarah's portrait and Isaiah's "Rejoice,
thou barren" in a song box; "Cast out the handmaid" in a song box beside Paul's face. Galatians 5: the yoke of bondage
snapped in the light; circumcision in words only beside Paul's stern face (5:2–6, 5:10–12); the runners, one fallen on the
course; the leaven in the lump; the law fulfilled in one word, Leviticus' "Thou shalt love thy neighbor" in a song box; the
works of the flesh as words over a dark, empty street; the fruit of the Spirit as a botanical plate of one tree and nine
fruits. Galatians 6: bearing one another's burdens on the road; the sower between the field of corruption and the field of
life; the reapers in due season; the large letters in Paul's own hand; the new creature, the dawn over a sown field; "the
marks of Jesus" beside his face, no wounds drawn; the benediction over the light."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from gal import G, art as A, ch01 as _prev
from gal.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, gd, wq, qw, v, title, fin, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, PAUL_GRIEF,
                        GOLD_BG, LAMP_BG, STERN_BG, JOY_BG, GRIEF_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("GAL-C02-00-Title", "Chapter 2 · The Fruit of the Spirit", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A3A22"></rect><g transform="translate(20 300)">{A.fruit_tree(720, 640, 4900, title=False)}</g>'
    return title(2, "The Fruit of the Spirit", "Galatians 4–6", svg, "#3A5A2A", v("5:1", to="stand fast therefore"))


from gal.art import art

SEGS = [
    # Galatians 4 — the heir; Hagar and Sarah
    D(lp("4:1-3"), art(A.heir_child, "hc1", 4901), "#E8D8B8", head="The Heir", sky=4, art_h=260),
    D(lp("4:4-5"), art(A.fulness_star, "fs1", 4904), "#05051A", head="The Fulness of the Time", art_h=230),
    F(lp("4:6-7"), PAUL_JOY, bg=JOY_BG),
    D(lp("4:8-11"), art(A.seasons), "#0B1A2E", head="Weak and Beggarly Rudiments", art_h=330),
    F(lp("4:12-14"), PAUL_GRIEF, bg=GRIEF_BG, head="Become as I Am"),
    D(lp("4:15-16"), art(A.welcomed, "wl1", 4915), "#8FD0E2", art_h=250),
    F(lp("4:17-20"), PAUL_GRIEF, bg=GRIEF_BG, head="My Little Children"),
    D(lp("4:21-23"), art(A.two_sons, "tw1", 4921), "#8FD0E2", head="Two Sons", art_h=260),
    D(lp("4:24-25"), art(A.sinai_bondage, 4924), "#1A1424", head="Two Covenants", art_h=260),
    D([lj("4:26", ("4:27", None, "it is written,")), sg("4:27", frm="Rejoice")], art(A.jerusalem_above, 4926), "#3A2A6A", art_h=330),
    F([lt("4:28"), lt("4:29"), lt("4:30", to="saith the scripture?"), sg("4:30", frm="Cast out"), lt("4:31")], PAUL),
    # Galatians 5 — stand fast; walk by the Spirit
    D([lt("5:1")], art(A.yoke_broken, "yb1", 5001), "#3A3A7A", head="Stand Fast", sky=5, art_h=330),
    F(lp("5:2-6"), PAUL_STERN, bg=STERN_BG),
    D(lp("5:7-8"), art(A.race, "rc1", 5007), "#8FD0E2", head="Ye Were Running Well", art_h=230),
    D([lt("5:9")], art(A.leaven, "lv1", 5009), "#C8A878", art_h=230),
    F(lp("5:10-12"), PAUL_STERN, bg=STERN_BG),
    D([lt("5:13"), lt("5:14", to="even in this:"), sg("5:14", frm="Thou shalt love"), lt("5:15")], art(A.love_one_word), "#0B1A2E", head="In One Word", art_h=250),
    D(lp("5:16-18"), art(A.two_ways, "tw2", 5016), "linear-gradient(90deg, #14101E 0%, #3A3048 45%, #C8B080 60%, #FFF4C2 100%)", head="Walk by the Spirit", art_h=240),
    D(lp("5:19-21"), art(A.dark_street, 5019), "#05050E", head="The Works of the Flesh", art_h=200),
    D(lp("5:22-23"), art(A.fruit_tree, 5022), "#F3EAD0", head="The Fruit of the Spirit", art_h=370),
    F(lp("5:24-26"), PAUL_JOY, bg=JOY_BG),
    # Galatians 6 — burdens; sowing and reaping; his own hand
    D(lp("6:1-2"), art(A.burdens, "bd1", 5101), "#8FD0E2", head="Bear Ye One Another's Burdens", sky=6, art_h=250),
    F(lp("6:3-6"), PAUL),
    D(lp("6:7-8"), art(A.sow_two, "sw1", 5107), "linear-gradient(90deg, #4A4450 0%, #8A8A90 45%, #8FD0E2 55%, #FFF4C2 100%)", head="Whatsoever a Man Soweth", art_h=250),
    D(lp("6:9-10"), art(A.reaping, "rp1", 5109), "#5A3A6A", art_h=230),
    D([lt("6:11")], art(A.large_letters, 5111), "#5A341E", head="With Mine Own Hand", art_h=420),
    F(lp("6:12-13"), PAUL_STERN, bg=STERN_BG),
    D(lp("6:14-16"), art(A.new_creation, 5114), "#3A3A7A", head="A New Creature", art_h=230),
    F([lt("6:17")], PAUL),
    glory([lt("6:18")]),
]
PG.extend(K.pack(SEGS, "GAL-C02-D", PG.next(), end=fin("END OF GALATIANS · NEXT · EPHESIANS")))
