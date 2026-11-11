"""Romans volume, Chapter 2 — Justified by Faith (Romans 4–7). Every verse, word for word from ref/eng-asv.
Abraham under the stars, his arm lifted (Genesis 15), with the scripture he believed in a song box; David's harp and Psalm
32 in song boxes; the plate of faith reckoned before the sign (Genesis 15, then 17) and the two lines of his children;
Abraham's road from Ur (Acts' map) for the heir of the world; God's own words to Abraham — "A father of many nations have I
made thee", "So shall thy seed be" — in the Voice box over the stars beyond count; Abraham and Sarah old at the tent door;
the tomb opened at dawn (4:25). Romans 5: peace with God at the writing table; the chain from tribulation to hope; the
three crosses far off against the darkened sky (5:6–8, ntcast's rule); the garden shut with the flame of the sword (no
cherub, no serpent drawn); the plate of death reigning from Adam until Moses; the one and the many; grace as light over the
sea. Romans 6: baptism in the river, the sealed tomb, the broken chain, the wages and the free gift. Romans 7: the bond of
the law; Sinai and the two tables with "Thou shalt not covet" in the Voice box; a man standing between the lamp and his
own long shadow (the body of this death, no torment drawn); the plate of the two laws; the door thrown open on the
morning."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rom import G, art2 as A, ch01 as _prev
from rom.common import (K, Pages, D, F, lt, lp, sg, gd, v, title, nxt, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, PAUL_GRIEF, GOLD_BG, LAMP_BG,
                        STERN_BG, JOY_BG, GRIEF_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ROM-C02-00-Title", "Chapter 2 · Justified by Faith", title=True)
def title_page(n):
    svg = f'<g transform="translate(0 300)">{A.abraham_stars("t02", 760, 780, 204)}</g><rect x="0" y="0" width="760" height="302" fill="#0B0B2A"></rect>'
    return title(2, "Justified by Faith", "Romans 4–7", svg, "#0B0B2A", v("5:1", to="we have peace with God"))


def st(p, seed, **k): return lambda w, h: A.study(p, w, h, seed, **k)

SEGS = [
    # Romans 4
    D([lt("4:1"), lt("4:2"), lt("4:3", to="saith the scripture?"), sg("4:3", frm="And Abraham believed")], lambda w, h: A.abraham_stars("as1", w, h, 1401),
      "#0B0B2A", head="Abraham Believed God", sky=4, art_h=230),
    F(lp("4:4-5"), PAUL),
    D([K.lj("4:6", ("4:7", None, "saying,")), sg("4:7", frm="Blessed are they"), sg("4:8")], lambda w, h: A.harp(w, h, 1406), "#2A1A2A", art_h=170),
    D(lp("4:9-12"), lambda w, h: A.sign_after(w, h), "#0B1A2E", head="The Father of All Them That Believe", art_h=230),
    D(lp("4:13-14"), lambda w, h: A.abraham_road(w, h), "#0B1A2E", head="Heir of the World", art_h=220),
    F(lp("4:15-16"), PAUL),
    D([lt("4:17", to="as it is written,"), gd("4:17", frm="A father of many nations", to="made thee)"), lt("4:17", frm="before him whom he believed")],
      lambda w, h: A.seed_stars(w, h, 1417), "#0B0B2A", art_h=170),
    D([lt("4:18", to="which had been spoken,"), gd("4:18", frm="So shall thy seed be."), lt("4:19")], lambda w, h: A.tent_old("to1", w, h, 1418), "#2A1A3A",
      head="In Hope Believed Against Hope", art_h=220),
    F(lp("4:20-22"), PAUL_JOY, bg=JOY_BG),
    D(lp("4:23-25"), lambda w, h: A.tomb_dawn("td1", w, h, 1423), "#3A3A7A", art_h=190),
    # Romans 5
    D(lp("5:1-2"), st("st5", 1501), "#3A2418", head="Peace with God", sky=5, art_h=240),
    D(lp("5:3-5"), lambda w, h: A.hope_chain(w, h), "#0B1A2E", art_h=200),
    D(lp("5:6-8"), lambda w, h: A.crosses_far("cf1", w, h, 1506), "#05050E", head="While We Were Yet Sinners", art_h=200),
    F(lp("5:9-11"), PAUL_JOY, bg=JOY_BG),
    D([lt("5:12")], lambda w, h: A.garden_shut(w, h, 1512), "#2A1A3A", head="Through One Man", art_h=230),
    D(lp("5:13-14"), lambda w, h: A.adam_moses(w, h), "#0B1A2E", art_h=200),
    F(lp("5:15-17"), PAUL),
    D(lp("5:18-19"), lambda w, h: A.one_many(w, h), "#0B1A2E", art_h=240),
    D(lp("5:20-21"), lambda w, h: A.grace_flood(w, h, 1520), "#2A2A6A", art_h=170),
    # Romans 6
    D(lp("6:1-4"), lambda w, h: A.baptism("bp1", w, h, 1601), "#3A3A7A", head="Newness of Life", sky=6, art_h=240),
    D(lp("6:5-7"), lambda w, h: A.sealed_tomb("tb1", w, h, 1605), "#3A2A4A", art_h=180),
    F(lp("6:8-11"), PAUL_JOY, bg=JOY_BG),
    F(lp("6:12-14"), PAUL_STERN, bg=STERN_BG),
    D(lp("6:15-18"), lambda w, h: A.broken_chains(w, h, 1615), "#6A8AB0", head="Servants of Righteousness", art_h=180),
    F(lp("6:19-22"), PAUL),
    D([lt("6:23")], lambda w, h: A.wages_gift(w, h), "#0B1A2E", art_h=230),
    # Romans 7
    D(lp("7:1-3"), lambda w, h: A.bond(w, h), "#0B1A2E", head="Dead to the Law", sky=7, art_h=210),
    F(lp("7:4-6"), PAUL),
    D([lt("7:7", to="except the law had said,"), gd("7:7", frm="Thou shalt not covet:")], lambda w, h: A.sinai_tables(w, h, 1707), "#1A1430",
      head="The Law Is Holy", art_h=240),
    D(lp("7:8-11"), st("st7", 1708, stage="read"), "#3A2418", art_h=220),
    F(lp("7:12-14"), PAUL_STERN, bg=STERN_BG),
    D(lp("7:15-17"), lambda w, h: A.shadow_man("sm1", w, h, 1715), "#3A2E2E", head="Wretched Man That I Am", art_h=220),
    F(lp("7:18-20"), PAUL_GRIEF, bg=GRIEF_BG),
    D(lp("7:21-23"), lambda w, h: A.two_laws(w, h), "#0B1A2E", art_h=230),
    F([lt("7:24")], PAUL_GRIEF, bg=GRIEF_BG),
    D([lt("7:25")], lambda w, h: A.deliverance(w, h, 1725), "#3A2E2E", art_h=230),
]
PG.extend(K.pack(SEGS, "ROM-C02-D", PG.next(), end=nxt("NEXT · NO CONDEMNATION")))
