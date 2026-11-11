"""1 Corinthians volume, Chapter 3 — This Do in Remembrance of Me (1 Corinthians 8–11). Every verse, word for word from
ref/eng-asv. 1 Corinthians 8: the idol's temple and the meat sold from its sacrifices (8:1); gods many and lords many, and
the light of the one God (8:4–6); a man at meat in the idol's temple and the weak brother at the door (8:10). 1 Corinthians
9: the road near Damascus in the light (9:1, Jesus not drawn); the soldier, the vinedresser and the shepherd (9:7); the ox
treading out the corn, unmuzzled, Moses' law in a song box (9:9); the altar and the priest's portion (9:13); Paul among Jew,
Greek and the weak (9:19–21); the race, the two crowns, the boxer striking out (9:24–27). 1 Corinthians 10: the pillar of
cloud between the camps, the manna, the rock (Exodus', John's and Isaiah's drawings, 10:1–4); the empty desert (10:5); the
calf, Exodus 32:6 in a song box (10:7); 10:8–10 over the desert at evening and the serpents on the sand, no one drawn; the way
of escape (10:13); the cup of blessing and the broken loaf (10:16); 10:18–22 (demons, words only) over the idol's court at
night, empty; the meat market (10:25); the feast (10:27). 1 Corinthians 11: praying bareheaded and veiled (11:4–6, 11:13–15);
the courtyard household (11:11–12); the divided supper (11:21); the Lord's supper — Matthew's drawing, Jesus' words in
balloons (11:23–25); 11:30 words only, beside Paul's face; the table set and waiting (11:33)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from co1 import G, art3 as A, ch02 as _prev
from co1.common import (K, Pages, D, F, lt, lts, lp, ltj, lj, sg, gd, sy, wq, qw, v, title, nxt, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, PAUL_GRIEF,
                        GOLD_BG, LAMP_BG, STERN_BG, JOY_BG, GRIEF_BG)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("1CO-C03-00-Title", "Chapter 3 · In Remembrance of Me", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1E1A"></rect><g transform="translate(0 300)">{A.cup_bread(760, 780, 1123)}</g>'
    return title(3, "In Remembrance of Me", "1 Corinthians 8–11", svg, "#2A1E1A", v("11:24", frm="this do in remembrance of me"))


def st(p, seed, **k): return lambda w, h: A.study_co1(p, w, h, seed, **k)

SEGS = [
    # 1 Corinthians 8
    D(lp("8:1-3"), lambda w, h: A.idol_meat("im1", w, h, 1801), "#8FD0E2", head="Knowledge Puffeth Up", sky=8, art_h=240),
    D(lp("8:4-6"), lambda w, h: A.one_god(w, h, 1804), "#5A4A5A", head="One God, the Father", art_h=220),
    F(lp("8:7-9"), PAUL),
    D(lp("8:10-13"), lambda w, h: A.temple_meal("tm1", w, h, 1810), "#7A5A4A", art_h=230),
    # 1 Corinthians 9
    D(lp("9:1-3"), lambda w, h: A.seen_lord("sl1", w, h, 1901), "#FFF4C2", head="Am I Not an Apostle?", sky=9, art_h=240),
    F(lp("9:4-6"), PAUL),
    D(lp("9:7-8"), lambda w, h: A.wages("wg1", w, h, 1907), "#C8B490", art_h=230),
    D([lt("9:9", to="in the law of Moses,"), sg("9:9", frm="Thou shalt not muzzle", to="treadeth out the corn."), lt("9:9", frm="Is it for the oxen"), lt("9:10")],
      lambda w, h: A.ox_tread("ox1", w, h, 1909), "#8FD0E2", head="Thou Shalt Not Muzzle the Ox", art_h=230),
    F(lp("9:11-12"), PAUL_STERN, bg=STERN_BG),
    D(lp("9:13-14"), lambda w, h: A.altar_portion("ap1", w, h, 1913), "#E8D8B0", art_h=230),
    F(lp("9:15-16"), PAUL_LAMP, bg=LAMP_BG, head="Woe Is unto Me"),
    D(lp("9:17-18"), st("st9", 1917), "#3A2418", art_h=250),
    D(lp("9:19-21"), lambda w, h: A.all_men("am1", w, h, 1919), "#8FD0E2", head="All Things to All Men", art_h=230),
    F(lp("9:22-23"), PAUL_JOY, bg=JOY_BG),
    D([lt("9:24")], lambda w, h: A.race("rc1", w, h, 1924), "#8FD0E2", head="So Run, That Ye May Attain", art_h=240),
    D([lt("9:25")], lambda w, h: A.crowns(w, h, 1925), "#0B1A2E", art_h=210),
    D(lp("9:26-27"), lambda w, h: A.boxer("bx1", w, h, 1926), "#E8905A", art_h=230),
    # 1 Corinthians 10
    D(lp("10:1-2"), lambda w, h: A.under_cloud("uc1", w, h, 2001), "#2A2A4A", head="Under the Cloud", sky=10, art_h=240),
    D([lt("10:3")], lambda w, h: A.manna("mn1", w, h, 2003), "#FFB07A", art_h=210),
    D([lt("10:4")], lambda w, h: A.rock("rk1", w, h, 2004), "#E8B880", art_h=220),
    D(lp("10:5-6"), lambda w, h: A.desert_empty(w, h, 2005), "#FFE6A0", art_h=200),
    D([lt("10:7", to="as it is written,"), sg("10:7", frm="The people sat down")], lambda w, h: A.calf_camp("cc1", w, h, 2007), "#FFE6A0", art_h=230),
    D(lp("10:8-10"), lambda w, h: A.serpents(w, h, 2008), "#2A1A3A", art_h=220),
    F(lp("10:11-12"), PAUL_STERN, bg=STERN_BG),
    D([lt("10:13")], lambda w, h: A.way_escape(w, h, 2013), "#FFF4C2", head="The Way of Escape", art_h=230),
    D(lp("10:14-17"), lambda w, h: A.cup_bread(w, h, 2014), "#2A1E1A", head="The Cup of Blessing", art_h=230),
    D(lp("10:18-22"), lambda w, h: A.idol_court(w, h, 2018), "#05051A", art_h=200),
    F(lp("10:23-24"), PAUL),
    D([lt("10:25"), sg("10:26")], lambda w, h: A.market_meats("mm2", w, h, 2025), "#E8905A", art_h=220),
    D(lp("10:27-30"), lambda w, h: A.feast("fs1", w, h, 2027), "#8A4A3A", art_h=230),
    F(lp("10:31-33") + [lt("11:1")], PAUL_JOY, bg=JOY_BG, head="Do All to the Glory of God"),
    # 1 Corinthians 11
    D(lp("11:2-4"), lambda w, h: A.praying("pr1", w, h, 2102), "#5A3E2E", head="Praying or Prophesying", sky=11, art_h=240),
    F(lp("11:5-6"), PAUL),
    F(lp("11:7-10"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("11:11-12"), lambda w, h: A.household("hh2", w, h, 2111), "#8FD0E2", art_h=230),
    D(lp("11:13-16"), lambda w, h: A.praying("pr2", w, h, 2113, stage="hair"), "#5A3E2E", art_h=230),
    D(lp("11:17-19"), lambda w, h: A.divided_supper("dv1", w, h, 2117), "#7A4A3A", head="Not for the Better", art_h=230),
    F(lp("11:20-22"), PAUL_STERN, bg=STERN_BG),
    D([lt("11:23"), lt("11:24", to="and said,"), sy("11:24", frm="This is my body")], lambda w, h: A.lords_supper("ls1", w, h, 2123), "#4A3438",
      head="This Do in Remembrance of Me", art_h=250),
    D([lt("11:25", to="saying,"), sy("11:25", frm="This cup"), lt("11:26")], lambda w, h: A.lords_supper("ls2", w, h, 2125, stage="cup"), "#4A3438", art_h=250),
    F(lp("11:27-29"), PAUL_STERN, bg=STERN_BG),
    F(lp("11:30-32"), PAUL_GRIEF, bg=GRIEF_BG),
    D(lp("11:33-34"), lambda w, h: A.table_waiting(w, h, 2133), "#3A2A20", art_h=230),
]
PG.extend(K.pack(SEGS, "1CO-C03-D", PG.next(), lone=1.5, end=nxt("NEXT · THE GREATEST OF THESE IS LOVE")))
