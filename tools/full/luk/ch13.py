"""Luke volume, Chapter 13 — Zacchæus (Luke 18–19). Every verse, word for word from ref/eng-asv.
The unrighteous judge in the gate and the widow's continual coming; the Pharisee standing forward and the publican afar off,
God, be thou merciful to me a sinner; the babes brought to him; the ruler — one thing thou lackest, and his going away
sorrowful; the camel and the needle's eye; we go up to Jerusalem; the blind man by the way side at Jericho, Receive thy
sight. Zacchæus little of stature up the sycomore over the crowd, Make haste, and come down; the murmuring; the half of my
goods; the Son of man came to seek and to save that which was lost. The pounds: the nobleman's journey, the ten servants
reckoned with, the pound kept in a napkin; his enemies slain before him told in words only over the empty hall. Bethphage
and the colt; the garments in the way, Blessed is the King that cometh; the stones would cry out; he wept over the city;
the temple cleansed — a house of prayer; teaching daily in the temple."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art11 as A, ch12 as _prev
from luk.common import (K, Pages, D, F, Q, N, T, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, CROWD_MAN, RICH_YOUNG, RICH_SAD, BARTIMAEUS, BARTIMAEUS_SEE, ZACCHAEUS, PHARISEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C13-00-Title", "Chapter 13 · Zacchæus", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.sycomore("t13", 760, 780, 1901, stage="call")}</g>'
    return title(13, "Zacchæus", "Luke 18 – 19", svg, "#2A4A3A", v("19:10"))


SEGS = [D([cp("18:1"), Q("18:2", "c", "saying,", "s"), sy("18:3")], lambda w, h: A.judge_widow("jw1", w, h, 1801), "#8FD0E2", head="They Ought Always to Pray", sky=18),
        D([sy("18:4"), sy("18:5")], lambda w, h: A.judge_widow("jw2", w, h, 1802, avenged=True), "#8FD0E2"),
        F([N("18:6", "And the Lord said,"), sy("18:7"), sy("18:8")], JESUS),
        D([cp("18:9"), sy("18:10"), sy("18:11"), sy("18:12")], lambda w, h: A.pharisee_publican("pp1", w, h, 1803), "#8FD0E2", head="Two Men Went Up into the Temple to Pray"),
        D([sy("18:13"), sy("18:14")], lambda w, h: A.pharisee_publican("pp2", w, h, 1804), "#8FD0E2"),
        D([cp("18:15"), N("18:16", "saying,"), sy("18:17")], lambda w, h: A.children_blessed("cb1", w, h, 1805), "#8FD0E2", head="Suffer the Little Children"),
        F([N("18:18", "asked him, saying,")], RICH_YOUNG, head="One Thing Thou Lackest"),
        F([N("18:19", "said unto him,"), sy("18:20")], JESUS),
        F([N("18:21", "And he said,")], RICH_YOUNG),
        D([N("18:22", "he said unto him,")], lambda w, h: A.rich_kneels("rk1", w, h, 1806), "#8FD0E2"),
        D([cp("18:23")], lambda w, h: A.rich_away("ra1", w, h, 1807), "#8FD0E2"),
        D([N("18:24", "seeing him said,"), sy("18:25")], lambda w, h: A.needle("nd1", w, h, 1808), "#3A2A5A"),
        F([N("18:26", "heard it said,")], CROWD_MAN, bg=COLD),
        F([N("18:27", "But he said,")], JESUS),
        F([N("18:28", "And Peter said,")], PETER),
        F([N("18:29", "said unto them,"), sy("18:30")], JESUS_TEACH),
        D([N("18:31", "said unto them,"), sy("18:32"), sy("18:33"), cp("18:34")], lambda w, h: A.to_jerusalem("tj1", w, h, 1809), "#4A3A6A", head="We Go Up to Jerusalem"),
        D([cp("18:35"), cp("18:36"), cp("18:37")], lambda w, h: A.bartimaeus_way("bw1", w, h, 1810), "#8FD0E2", head="Receive Thy Sight"),
        D([N("18:38", "cried, saying,"), Q("18:39", "c", "the more a great deal,", "s")], lambda w, h: A.bartimaeus_way("bw2", w, h, 1811), "#8FD0E2"),
        F([cp("18:40"), (q41 := Q("18:41", "s", "unto thee?", "c", "And he said,", "s"))[0]], JESUS),
        F(q41[1:], BARTIMAEUS, bg=COLD, ref="LUKE 18:41"),
        F([N("18:42", "said unto him,")], JESUS),
        D([cp("18:43")], lambda w, h: A.bartimaeus_way("bw3", w, h, 1812, sprang=True), "#8FD0E2"),
        # Luke 19
        D([cp("19:1"), cp("19:2"), cp("19:3"), cp("19:4")], lambda w, h: A.sycomore("zc1", w, h, 1901), "#8FD0E2", head="Zacchæus, Make Haste", sky=(19, "left"), art_h=240),
        D([N("19:5", "said unto him,")], lambda w, h: A.sycomore("zc2", w, h, 1902, stage="call"), "#8FD0E2", art_h=260),
        D([cp("19:6"), N("19:7", "murmured, saying,")], lambda w, h: A.sycomore("zc3", w, h, 1903, stage="house"), "#8FD0E2"),
        F([N("19:8", "said unto the Lord,")], ZACCHAEUS),
        D([N("19:9", "said unto him,"), sy("19:10")], lambda w, h: A.sycomore("zc4", w, h, 1904, stage="stood"), "#8FD0E2", art_h=220),
        D([cp("19:11"), N("19:12", "He said therefore,"), sy("19:13"), sy("19:14")], lambda w, h: A.nobleman("nb1", w, h, 1905), "#8FD0E2", head="Trade Ye Herewith Till I Come"),
        D([sy("19:15"), sy("19:16"), sy("19:17"), sy("19:18"), sy("19:19")], lambda w, h: A.talents("tl1", w, h, 1906, stage="reckon"), "#5A3A4A"),
        D([sy("19:20"), sy("19:21"), sy("19:22"), sy("19:23")], lambda w, h: A.nobleman("nb2", w, h, 1907, stage="napkin"), "#3A1A2A"),
        D([sy("19:24"), sy("19:25"), sy("19:26"), sy("19:27")], lambda w, h: A.king_hall("kh1", w, h, 1908, kneel=False, angry=True), "#3A1A2A"),
        D([cp("19:28"), cp("19:29"), Q("19:30", "c", "saying,", "s"), sy("19:31")], lambda w, h: A.bethphage("bp1", w, h, 1909), "#8FD0E2", head="Blessed Is the King That Cometh"),
        D([cp("19:32"), N("19:33", "said unto them,"), N("19:34", "And they said,")], lambda w, h: A.bethphage("bp2", w, h, 1910), "#8FD0E2"),
        D([cp("19:35"), cp("19:36"), cp("19:37"), Q("19:38", "c", "saying,", "s")], lambda w, h: A.entry("en1", w, h, 1911), "#8FD0E2", art_h=220),
        F([N("19:39", "said unto him,")], PHARISEE, bg=RED),
        F([N("19:40", "answered and said,")], JESUS),
        D([cp("19:41"), Q("19:42", "c", "saying,", "s")], lambda w, h: A.wept_city("wc1", w, h, 1912), "#5A6A9A", head="He Saw the City and Wept over It", art_h=240),
        F([sy("19:43"), sy("19:44")], JESUS_GRIEF, bg=COLD),
        D([cp("19:45"), Q("19:46", "c", "saying unto them,", "s")], lambda w, h: A.temple_court("tc1", w, h, 1913, cleansed=True), "#8FD0E2", head="A House of Prayer"),
        D([cp("19:47"), cp("19:48")], A.footed(lambda w, h: A.temple_teaching("tt1", w, h, 1914), "#8A7A5A"), "#C8B490", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C13-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · RENDER UNTO CÆSAR")))
