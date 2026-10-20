"""Amos volume, Chapter 1 — For Three Transgressions (Amos 1–4). Every verse, word for word from ref/eng-asv.
The words of Amos among the herdsmen of Tekoa; Jehovah will roar from Zion and the top of Carmel withers; then the eight
oracles, each over the map of the nations with that one lit and fire on its wall — Damascus, Gaza, Tyre, Edom, Ammon (1:13
in words only over Rabbah's burning wall), Moab, Judah, and Israel: the righteous sold for silver and the needy for a pair
of shoes, the Amorite cut down like a cedar, the Nazirites given wine, the cart pressed full of sheaves, flight perished from
the swift; shall two walk together? (a plate of causes); the lion hath roared; the palaces of Ashdod and Egypt called to
behold Samaria; the shepherd's scrap from the lion's mouth; the corner of a couch; the horns of the altar cut off; ye kine of
Bashan; hooks and the breaches; come to Beth-el and transgress; five times yet have ye not returned — the empty bowls, the
rain on one city, the blasting, the pestilence, the brand plucked out of the burning; prepare to meet thy God, O Israel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from amo import G, art as K
from dan.kit import refs_of
from amo.common import L, AMOS, AMOS_STERN, AMOS_GRIEF, AMOS_PRAY, AMAZIAH, COLD, GOLDEN, RED, NIGHT

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY, MAP, DUSK, GREY, FIRE = "#8FD0E2", "#0B1A2E", "#5A3A5A", "#8A8A9A", "#2A0A0A"
TSJ = "Thus saith Jehovah:"


@P("AMO-C01-00-Title", "Chapter 1 · For Three Transgressions", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.tekoa("t1", 760, 800, 101)}</g><rect x="0" y="0" width="760" height="282" fill="#9AB8D8"></rect>')
    return chapter_title(1, "第一話", "For Three Transgressions", "Amos 1 – 4", svg, "#3A4A6A", v("1:3", frm="For three transgressions", to="yea, for four,"), "Amos · Volume Thirty")


c, cs, s, ss, sl, A, T, Nt, gls, cut, sp2 = L.c, L.cs, L.s, L.ss, L.sl, L.A, L.T, L.N, L.gls, L.cut, L.split
am = lambda refs: ss(refs, "amos")

def oracle(a, b, lit, fire, extra=(), moves=(), **k):
    """One of the eight oracles: thus saith Jehovah (a caption), then his words, over the map with `lit` lit."""
    refs = f"{a}-{b.split(':')[1]}" if b != a else a
    rs = refs_of(refs)
    lines = [*cut(rs[0], TSJ, poem=True)] + [l for r in rs[1:] for l in gls(r)]
    return A(lines, refs, lambda w, h: K.nations(w, h, lit=lit, fire=fire, extra=extra, moves=moves), MAP, **k)

SEGS = [A([cs("1:1")], "1:1", lambda w, h: K.tekoa("tk1", w, h, 102), "#9AB8D8", head="The Herdsmen of Tekoa", stamp=1),
        A([*cut("1:2", "And he said,", "amos", poem=True)], "1:2", lambda w, h: K.carmel(w, h, 103), "#C8A880", who="amos"),
        oracle("1:3", "1:5", "DAMASCUS", ("DAMASCUS",), extra=("KIR",), moves=[("DAMASCUS", "KIR")], head="For Three Transgressions"),
        oracle("1:6", "1:8", "GAZA", ("GAZA",), extra=("ASHDOD", "ASHKELON", "EKRON")),
        oracle("1:9", "1:10", "TYRE", ("TYRE",)),
        oracle("1:11", "1:12", "EDOM", ("TEMAN", "BOZRAH"), extra=("TEMAN", "BOZRAH")),
        A([*cut("1:13", TSJ, poem=True), *gls("1:14-15")], "1:13-15", lambda w, h: K.burning_wall(w, h, 104), FIRE),
        oracle("2:1", "2:3", "MOAB", ("KERIOTH",), extra=("KERIOTH",), stamp=2),
        oracle("2:4", "2:5", "JUDAH", ("JERUSALEM",), extra=("JERUSALEM",)),
        A([*cut("2:6", TSJ, poem=True)], "2:6", lambda w, h: K.sold(w, h), MAP, head="For Three Transgressions of Israel"),
        A([*gls("2:7-8")], "2:7-8", lambda w, h: K.bethel_gilgal(w, h, 105), DUSK),
        A([*gls("2:9-10")], "2:9-10", lambda w, h: K.amorite(w, h, 106), SKY),
        A([*gls("2:11-12")], "2:11-12", lambda w, h: K.nazirite("nz1", w, h, 107), DUSK),
        A([*gls("2:13")], "2:13", lambda w, h: K.cart_sheaves(w, h, 108), SKY),
        A([*gls("2:14-16")], "2:14-16", lambda w, h: K.mighty_flee("mf1", w, h, 109), "#5A3A3A", wk=0.66)]
PG.extend(L.pack(SEGS, "AMO-C01-D", PG.next()))

SEGS2 = [T([am("3:1"), *gls("3:2")], "3:1-2", AMOS_STERN, RED, who="amos", head="Hear This Word", stamp=3),
         A([am("3:3-6")], "3:3-6", lambda w, h: K.two_walk(w, h), MAP, who="amos", head="Shall Two Walk Together?"),
         A([am("3:7-8")], "3:7-8", lambda w, h: K.lion_roar(w, h, 110), "#5A3A3A", who="amos"),
         A([*gls("3:9-10")], "3:9-10", lambda w, h: K.samaria_mount(w, h, 111), SKY),
         A([*cut("3:11", "thus saith the Lord Jehovah:", poem=True), *cut("3:12", "Thus saith Jehovah:", poem=True)], "3:11-12", lambda w, h: K.lion_mouth(w, h, 112), GREY),
         A([*gls("3:13-15")], "3:13-15", lambda w, h: K.horns_cut(w, h, 113), DUSK),
         A([*gls("4:1-3")], "4:1-3", lambda w, h: K.kine(w, h, 114), SKY, head="Ye Kine of Bashan", stamp=4),
         A([*gls("4:4-5")], "4:4-5", lambda w, h: K.bethel_gilgal(w, h, 115), DUSK),
         A([*gls("4:6")], "4:6", lambda w, h: K.empty_bowls(w, h, 116), "#4A3A30", head="Yet Have Ye Not Returned"),
         A([*gls("4:7-8")], "4:7-8", lambda w, h: K.rain_one_city(w, h, 117), "#C8B898"),
         A([*gls("4:9")], "4:9", lambda w, h: K.blasted(w, h, 118), "#9A9A8A"),
         A([*gls("4:10-11")], "4:10-11", lambda w, h: K.brand(w, h, 119), "#3A1A1A"),
         A([*gls("4:12-13")], "4:12-13", lambda w, h: K.he_formeth(w, h, 120), "#1A1A3A", head="Prepare to Meet Thy God")]
PG.extend(L.pack(SEGS2, "AMO-C01-E", PG.next(), end=end_mark("NEXT · THE PLUMB-LINE", "right: 10px; bottom: 34px")))
