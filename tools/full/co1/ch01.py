"""1 Corinthians volume, Chapter 1 — Christ the Power of God (1 Corinthians 1–4). Every verse, word for word from ref/eng-asv.
The letter written at Ephesus by lamplight: Paul dictating, Sosthenes cross-legged on the mat writing (1:1), the window on
Ephesus; its road across the Aegean to Corinth (1:2); Chloe's messenger at the door (1:11); the four factions as one panel
split four ways (1:12); the word of the cross over the hill of the three crosses far off, the Voice box for "I will destroy
the wisdom of the wise" (1:18–19); the colonnade of the disputers (1:20); the Jew asking a sign and the Greek with his
scroll (1:22); the plain folk of the church (1:26). 1 Corinthians 2: Paul coming into Corinth under the Acrocorinth (2:1);
the empty judgment-seat of the rulers of this world (2:6–8); things which eye saw not, a light behind the clouds (2:9); the
deep things, light going down into the sea (2:10). 1 Corinthians 3: milk and meat (3:2); planting and watering, the
increase a shaft of light on the plant (3:6); the foundation plate and the fire that proves the work (3:10–15); the temple
(3:16). 1 Corinthians 4: the stewards (4:1); the hidden things brought to light (4:5); the empty arena (4:9); the
tentmakers' bench (4:12); Timothy sent with a scroll (4:17); the rod or love (4:21)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co1 import G, art as A
from co1.common import (K, Pages, D, F, lt, lts, lp, ltj, lj, sg, gd, wq, qw, v, title, nxt, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, PAUL_GRIEF,
                        GOLD_BG, LAMP_BG, STERN_BG, JOY_BG, GRIEF_BG)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1CO-C01-00-Title", "Chapter 1 · Christ the Power of God", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_co1("t01", 760, 640, 101, fig_h=420)}</g>'
    return title(1, "Christ the Power of God", "1 Corinthians 1–4", svg, "#3A2418", v("1:24", frm="Christ the power of God"))


def st(p, seed, **k): return lambda w, h: A.study_co1(p, w, h, seed, **k)
def dawn(w, h): return A.vista(w, h, 1107, tone="dawn", horizon=0.66, hills_n=2, glow_at=(0.5, 0.66, 0.6, "#FFF4C2"), sun_at=(0.5, 0.64), birds_=4)
def all_yours(w, h): return A.vista(w, h, 1322, tone="dawn", horizon=0.62, hills_n=2, sea_=True, glow_at=(0.5, 0.62, 0.6, "#FFF4C2"), sun_at=(0.5, 0.6), birds_=5)

SEGS = [
    # 1 Corinthians 1 — the letter written at Ephesus
    D([lt("1:1")], st("st1", 1101), "#3A2418", head="Called to Be an Apostle", sky=1, art_h=300),
    D([lt("1:2"), lt("1:3")], lambda w, h: A.aegean_road(w, h), "#0B1A2E", art_h=260),
    F(lp("1:4-6"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("1:7-9"), dawn, "#2A2A5A", art_h=190),
    D(lp("1:10-11"), lambda w, h: A.chloe_word("cw1", w, h, 1110), "#3A2418", head="No Divisions Among You", art_h=260),
    D([lt("1:12"), lt("1:13")], lambda w, h: A.factions("fc1", w, h), "#2A2A3A", art_h=230),
    F(lp("1:14-17"), PAUL),
    D([lt("1:18")] + wq("1:19", "For it is written,", "I will destroy", kind="god"), lambda w, h: A.cross_far("cf1", w, h, 1118), "#05050E",
      head="The Word of the Cross", art_h=200),
    D(lp("1:20-21"), lambda w, h: A.wise_disputer("wd1", w, h, 1120), "#C8B490", art_h=200),
    D(lp("1:22-25"), lambda w, h: A.signs_wisdom("sw1", w, h, 1122), "#2A2A4A", head="Christ the Power of God", art_h=220),
    D(lp("1:26-29"), lambda w, h: A.plain_folk("pf1", w, h, 1126), "#3A2418", head="Not Many Wise", art_h=210),
    F([lt("1:30"), lt("1:31", to="as it is written,"), sg("1:31", frm="He that glorieth")], PAUL_JOY, bg=JOY_BG),
    # 1 Corinthians 2
    D(lp("2:1-3"), lambda w, h: A.corinth_view("cv1", w, h, 1201, paul_=True), "#3A2A5A", head="Jesus Christ, and Him Crucified", sky=2, art_h=230),
    F(lp("2:4-5"), PAUL),
    D(lp("2:6-8"), lambda w, h: A.rulers_seat("rs1", w, h, 1206), "#8FD0E2", head="God's Wisdom in a Mystery", art_h=200),
    D([lt("2:9", to="but as it is written,"), sg("2:9", frm="Things which eye")], lambda w, h: A.prepared(w, h, 1209), "#0B0B2A",
      head="Things Which Eye Saw Not", art_h=230),
    D(lp("2:10-12"), lambda w, h: A.deep_light(w, h, 1210), "#0F2E4A", art_h=200),
    F(lp("2:13-15") + [sg("2:16", to="instruct him?"), lt("2:16", frm="But we have")], PAUL_LAMP, bg=LAMP_BG),
    # 1 Corinthians 3
    D(lp("3:1-2"), lambda w, h: A.milk_meat(w, h, 1301), "#3A2418", head="Babes in Christ", sky=3, art_h=200),
    F(lp("3:3-4"), PAUL_STERN, bg=STERN_BG),
    D(lp("3:5-9"), lambda w, h: A.husbandry("hb1", w, h, 1305), "#8FD0E2", head="God Gave the Increase", art_h=230),
    D(lp("3:10-12"), lambda w, h: A.foundation_plate(w, h), "#0B1A2E", head="Other Foundation Can No Man Lay", art_h=230),
    D(lp("3:13-15"), lambda w, h: A.foundation_plate(w, h, fire=True), "#0B1A2E", art_h=230),
    D(lp("3:16-17"), lambda w, h: A.temple_of_god("tg1", w, h, 1316), "#5A7AB0", head="Ye Are a Temple of God", art_h=220),
    F([lt("3:18"), lt("3:19", to="For it is written,"), sg("3:19", frm="He that taketh"), lt("3:20", to="and again,"), sg("3:20", frm="The Lord knoweth")],
      PAUL_STERN, bg=STERN_BG),
    D(lp("3:21-23"), all_yours, "#2A2A5A", art_h=200),
    # 1 Corinthians 4
    D(lp("4:1-2"), lambda w, h: A.stewards("sd1", w, h, 1401), "#C8B490", head="Stewards of the Mysteries of God", sky=4, art_h=220),
    F(lp("4:3-4"), PAUL),
    D([lt("4:5")], lambda w, h: A.hidden_things(w, h, 1405), "#141018", art_h=200),
    F(lp("4:6-7"), PAUL_STERN, bg=STERN_BG),
    D(lp("4:8-9"), lambda w, h: A.arena("ar1", w, h, 1408), "#E8905A", head="A Spectacle unto the World", art_h=220),
    D(lp("4:10-13"), lambda w, h: A.toil("tl1", w, h, 1410), "#C8B490", head="Fools for Christ's Sake", art_h=250),
    F(lp("4:14-16"), PAUL),
    D([lt("4:17")], lambda w, h: A.timothy_sent("ts1", w, h, 1417), "#3A2418", head="I Have Sent unto You Timothy", art_h=260),
    D(lp("4:18-21"), lambda w, h: A.rod_or_love(w, h, 1418), "#3A2418", art_h=200),
]
PG.extend(K.pack(SEGS, "1CO-C01-D", PG.next(), end=nxt("NEXT · A LITTLE LEAVEN")))
