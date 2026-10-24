"""Luke volume, Chapter 12 — The Rich Man and Lazarus (Luke 16–17). Every verse, word for word from ref/eng-asv.
The unrighteous steward called to account and the debtors' bonds rewritten — fifty, fourscore; faithful in a very little;
no servant can serve two masters; the Pharisees who were lovers of money scoffing; one tittle of the law. The rich man and
Lazarus: the rich man's gate and his feast, Lazarus laid at the gate with the dogs (the sores in words only); carried away
by the angels of light; the rich man buried, his tomb shut; Hades only darkness and smoke, the great gulf fixed, and
Abraham's bosom far across as light — no one drawn in torment and no figure drawn in the light; Moses and the prophets. The
millstone; forgive seven times; increase our faith, the sycamine tree planted in the sea; unprofitable servants. The ten
lepers standing afar off, cleansed as they went, the Samaritan turned back on his face at his feet — where are the nine?
The kingdom of God within you; the lightning; the days of Noah and of Lot, fire and brimstone over the city far off (Lot's
wife in words only); one taken and the other left; and the eagles gathered. Luke 17:36 has no text in the ASV."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art10 as A, ch11 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        ANDREW, PHARISEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C12-00-Title", "Chapter 12 · The Rich Man and Lazarus", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0A0608"></rect><g transform="translate(0 300)">{A.gulf("t12", 760, 780, 1601)}</g>'
    return title(12, "The Rich Man and Lazarus", "Luke 16 – 17", svg, "#0A0608", v("16:26", frm="between us and you there is a great gulf fixed,", to="a great gulf fixed,"))


SEGS = [D([N("16:1", "unto the disciples,"), sy("16:2")], lambda w, h: A.steward_bonds("sb1", w, h, 1601), "#A88A6A", head="The Unrighteous Steward", sky=16),
        D([sy("16:3"), sy("16:4")], lambda w, h: A.steward_bonds("sb2", w, h, 1602), "#A88A6A"),
        D([sy("16:5"), sy("16:6"), sy("16:7")], lambda w, h: A.steward_bonds("sb3", w, h, 1603, stage="bonds"), "#A88A6A"),
        F([sy("16:8"), sy("16:9")], JESUS_TEACH),
        F([sy("16:10"), sy("16:11"), sy("16:12"), sy("16:13")], JESUS, head="Ye Cannot Serve God and Mammon"),
        F([cp("16:14")], PHARISEE, bg=RED),
        F([N("16:15", "said unto them,")], JESUS_STERN, bg=RED),
        D([sy("16:16"), sy("16:17"), sy("16:18")], lambda w, h: A.law_scroll("lw1", w, h, 1604), "#1A1630"),
        D([sy("16:19"), sy("16:20"), sy("16:21")], lambda w, h: A.rich_gate("rg1", w, h, 1605), "#8FD0E2", head="A Certain Beggar Named Lazarus", art_h=240),
        D([sy("16:22", to="Abraham's bosom:")], lambda w, h: A.rich_gate("rg2", w, h, 1606, stage="carried"), NIGHT, art_h=260),
        D([sy("16:22", frm="and the rich man also")], lambda w, h: A.rich_gate("rg3", w, h, 1607, stage="buried"), "#5A4A7A", art_h=220),
        D([sy("16:23"), sy("16:24")], lambda w, h: A.gulf("gf1", w, h, 1608), "#0A0608", head="A Great Gulf Fixed"),
        D([sy("16:25"), sy("16:26")], lambda w, h: A.gulf("gf2", w, h, 1609), "#0A0608"),
        D([sy("16:27"), sy("16:28")], lambda w, h: A.gulf("gf3", w, h, 1610), "#0A0608"),
        D([sy("16:29"), sy("16:30"), sy("16:31")], lambda w, h: A.prophecy("pp1", w, h, 1611), "#1A1630"),
        # Luke 17
        D([N("17:1", "unto his disciples,"), sy("17:2")], lambda w, h: A.millstone("ml1", w, h, 1701), "#1F4C68", head="Increase Our Faith", sky=17),
        F([sy("17:3"), sy("17:4")], JESUS),
        F([N("17:5", "unto the Lord,")], ANDREW, bg=COLD),
        D([N("17:6", "And the Lord said,")], lambda w, h: A.sycamine("sc1", w, h, 1702, uprooted=True), "#8FD0E2", art_h=240),
        D([sy("17:7"), sy("17:8"), sy("17:9"), sy("17:10")], lambda w, h: A.plowman_serves("ps1", w, h, 1703), "#A88A6A"),
        D([cp("17:11"), cp("17:12"), N("17:13", "saying,")], lambda w, h: A.ten_lepers("tl1", w, h, 1704), "#8FD0E2", head="Where Are the Nine?", art_h=220),
        D([Q("17:14", "c", "said unto them,", "s", "unto the priests.", "c")], lambda w, h: A.ten_lepers("tl2", w, h, 1705, stage="go"), "#8FD0E2"),
        D([cp("17:15"), cp("17:16")], lambda w, h: A.ten_lepers("tl3", w, h, 1706, stage="back"), "#8FD0E2", art_h=240),
        F([N("17:17", "answering said,"), sy("17:18"), N("17:19", "said unto him,")], JESUS),
        F([N("17:20", "answered them and said,"), sy("17:21")], JESUS_TEACH, head="The Kingdom of God Is within You"),
        D([N("17:22", "unto the disciples,"), sy("17:23"), sy("17:24"), sy("17:25")], lambda w, h: A.lightning_sky("ls1", w, h, 1707), "#14141E"),
        D([sy("17:26"), sy("17:27")], lambda w, h: A.flood_ark("fa1", w, h, 1708), "#2A2A3A", head="As in the Days of Noah"),
        D([sy("17:28"), sy("17:29"), sy("17:30")], lambda w, h: A.city_smoke("cs1", w, h, 1709), "#3A1A1A"),
        D([sy("17:31"), sy("17:32"), sy("17:33")], lambda w, h: A.flee("fl1", w, h, 1710), "#8A7A6A"),
        D([sy("17:34"), sy("17:35")], lambda w, h: A.taken_left("tk1", w, h, 1711), "#8FD0E2"),
        D([Q("17:37", "c", "say unto him,", "s", "Where, Lord?", "c", "said unto them,", "s")], A.footed(lambda w, h: A.eagles_gather("eg1", w, h, 1712), "#6A5A4A"),
          "#8A7A6A", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C12-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · ZACCHAEUS")))
