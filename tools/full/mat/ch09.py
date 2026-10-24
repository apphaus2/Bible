"""Matthew volume, Chapter 9 — The Son of Man Cometh (Matthew 23–25). Every verse, word for word from ref/eng-asv.
The woes, his words beside his stern face and over Moses' seat, the heavy burdens, the gnat and the camel, the cup clean
without, the whited sepulchres (nothing within drawn), the tombs of the prophets; O Jerusalem, over the hen and her chickens.
The great stones of the temple; the mount of Olives at evening; the signs of the end drawn as landscapes with no one hurt in
them — wars and earthquakes far off, the flight to the mountains, the lightning, the eagles, the sun darkened and the stars
falling, the clouds and the angels of light; the fig tree; the ark on the flood; one taken and one left; the thief at night;
the faithful and the evil steward. The ten virgins; the talents; the throne of his glory, the sheep and the goats, and the
six works of mercy. The outer darkness and the eternal fire are words only. Verse 23:14 has no words in the ASV."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art9 as A, ch08 as _prev
from mat.common import (K, Pages, drawn, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, PETER)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C09-00-Title", "Chapter 9 · The Son of Man Cometh", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A6A"></rect><g transform="translate(0 300)">{A.clouds_glory("t9", 760, 780, 2401)}</g>'
    return title(9, "The Son of Man Cometh", "Matthew 23 – 25", svg, "#2A2A6A", v("24:44", frm="Therefore be ye"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
def S(a, b):
    ch, x = a.split(":")
    return [sy(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]
STERN = dict(tok=JESUS_STERN, bg=RED)

SEGS = [D([cp("23:1"), cp("23:2", to="saying,"), sy("23:2", frm="The scribes"), sy("23:3")], lambda w, h: A.moses_seat("ms1", w, h, 2301), "#C8B490", head="Woe unto You", stamp=23),
        D(S("23:4", 4), lambda w, h: A.burdens("bu1", w, h, 2302), "#C8A890"),
        F(S("23:5", 7), **STERN),
        F(S("23:8", 12)),
        F(S("23:13", 13) + S("23:15", 15), **STERN),
        F(S("23:16", 19), **STERN),
        F(S("23:20", 22)),
        D(S("23:23", 24), lambda w, h: A.gnat_camel("gc1", w, h, 2303), "#C8A878"),
        D(S("23:25", 26), lambda w, h: A.cup_platter("cp1", w, h, 2304), "#2A1A2A"),
        D(S("23:27", 28), lambda w, h: A.sepulchres("sp1", w, h, 2305), "#5AB0D8"),
        D(S("23:29", 31), lambda w, h: A.prophets_tombs("pt1", w, h, 2306), "#8FD0E2"),
        F(S("23:32", 34), **STERN),
        F(S("23:35", 36), **STERN),
        D(S("23:37", 39), lambda w, h: A.hen_chickens("hc1", w, h, 2307), "#4A2A5A", head="O Jerusalem, Jerusalem"),
        # Matthew 24
        D([cp("24:1"), cp("24:2", to="said unto them,"), sy("24:2", frm="See ye not")], lambda w, h: A.temple_stones("ts1", w, h, 2401), "#8FD0E2", head="The Sign of Thy Coming", stamp=24),
        D([cp("24:3", to="saying,"), sy("24:3", frm="Tell us")], lambda w, h: A.olivet("ol1", w, h, 2402), "#4A2A5A"),
        F([cp("24:4", to="said unto them,"), sy("24:4", frm="Take heed"), sy("24:5")], JESUS),
        D(S("24:6", 8), lambda w, h: A.wars_far("wf1", w, h, 2403), "#2A1A2A"),
        F(S("24:9", 14), JESUS_GRIEF, bg=COLD),
        D(S("24:15", 18), lambda w, h: A.flee("fl1", w, h, 2404), "#3A2A4A"),
        F(S("24:19", 22), JESUS_GRIEF, bg=COLD),
        F(S("24:23", 26), **STERN),
        D(S("24:27", 27), lambda w, h: A.lightning_sky("lg1", w, h, 2405), "#05051A"),
        D(S("24:28", 28), lambda w, h: A.eagles_gather("eg1", w, h, 2406), "#FFD89A"),
        D(S("24:29", 29), lambda w, h: A.darkened("dk1", w, h, 2407), "#05050E", head="Coming on the Clouds of Heaven"),
        D(S("24:30", 31), lambda w, h: A.clouds_glory("cg1", w, h, 2408), "#2A2A6A"),
        D(S("24:32", 35), lambda w, h: A.fig_leaf("fl2", w, h, 2409), "#8FD0E2"),
        F(S("24:36", 36), JESUS),
        D(S("24:37", 39), lambda w, h: A.flood_ark("fa1", w, h, 2410), "#2A2A3A", head="Watch Therefore"),
        D(S("24:40", 42), lambda w, h: A.taken_left("tl1", w, h, 2411), "#8FD0E2"),
        D(S("24:43", 44), lambda w, h: A.thief("th1", w, h, 2412), "#05051A"),
        D(S("24:45", 47), lambda w, h: A.steward("sw1", w, h, 2413), "#B8987A"),
        D(S("24:48", 51), lambda w, h: A.steward("sw2", w, h, 2414, evil=True), "#4A3438"),
        # Matthew 25
        D(S("25:1", 5), lambda w, h: A.virgins("vg1", w, h, 2501), "#05051A", head="The Ten Virgins", stamp=25),
        D(S("25:6", 9), lambda w, h: A.virgins("vg2", w, h, 2502, stage="cry"), "#05051A"),
        D(S("25:10", 13), lambda w, h: A.virgins("vg3", w, h, 2503, stage="shut"), "#05051A"),
        D(S("25:14", 15), lambda w, h: A.talents("tn1", w, h, 2504), "#8FD0E2", head="The Talents"),
        D(S("25:16", 18), lambda w, h: A.talents("tn2", w, h, 2505, stage="dig"), "#5A3A6A"),
        D(S("25:19", 21), lambda w, h: A.talents("tn3", w, h, 2506, stage="reckon"), "#8FD0E2"),
        F(S("25:22", 23), JESUS),
        F(S("25:24", 25)),
        F(S("25:26", 30), **STERN),
        D(S("25:31", 33), lambda w, h: A.throne_glory("tg1", w, h, 2507), "#1A1A4A", head="The Throne of His Glory", art_h=260),
        D(S("25:34", 36), lambda w, h: A.mercies("mc1", w, h, 2508), "#12113A"),
        F(S("25:37", 40), JESUS),
        F(S("25:41", 43), **STERN),
        F(S("25:44", 46), JESUS_GRIEF, bg=COLD)]
PG.extend(K.pack(SEGS, "MAT-C09-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · GETHSEMANE")))
