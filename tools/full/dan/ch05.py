"""Daniel volume, Chapter 5 — Seventy Weeks (Daniel 9–10). Every verse, word for word from ref/asv.
Daniel understands by the books Jeremiah's seventy years (a chart) and sets his face to seek the Lord in sackcloth and
ashes; his confession and supplication in full — we have sinned, O Lord, hear; O Lord, forgive — over his face at prayer,
Jerusalem's desolations, the scroll of the law of Moses and the sea divided; Gabriel caused to fly swiftly at the time of
the evening oblation (a figure of light); the seventy weeks as a chart; then in the third year of Cyrus, three whole weeks of
mourning; the man clothed in linen by the great river Hiddekel (only light, girded with gold); the men fled, Daniel fallen,
set upon his knees; the prince of Persia, the prince of Greece and Michael as a chart; O man greatly beloved, be strong."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from dan import G, art5 as K
from dan.common import L, DANIEL_OLD, DANIEL_OLD_AWE, DANIEL_OLD_GRIEF, DANIEL_OLD_PRAY, COLD, GOLDEN, RED, NIGHT
from dan import ch04 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BP, EVE, RIVER = "#0B2A4A", "#3A2A5A", "#5A7AA8"


@P("DAN-C05-00-Title", "Chapter 5 · Seventy Weeks", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.gabriel_fly("t5", 760, 820, 501)}</g><rect x="0" y="0" width="760" height="262" fill="#3A2A5A"></rect>')
    return chapter_title(5, "第五話", "Seventy Weeks", "Daniel 9 – 10", svg, "#3A2A5A", v("9:23", frm="for thou art greatly beloved:"), "Daniel · Volume Twenty-Seven")


c, cs, s, ss, sl, cut, A, T, Nt, sp2 = L.c, L.cs, L.s, L.ss, L.sl, L.cut, L.A, L.T, L.N, L.split
d = lambda refs: ss(refs, "daniel")

SEGS = [A([d("9:1-2")], "9:1-2", lambda w, h: K.seventy_years(w, h), BP, who="daniel", head="Seventy Years", stamp=9),
        A([d("9:3")], "9:3", lambda w, h: K.sackcloth("sc1", w, h, 502), "#8A6A4A", who="daniel"),
        T([d("9:4-6")], "9:4-6", DANIEL_OLD_PRAY, GOLDEN, who="daniel", head="We Have Sinned"),
        A([d("9:7-8")], "9:7-8", lambda w, h: K.jerusalem_desolate(w, h, 503), "#5A4A5A", who="daniel"),
        T([d("9:9-11")], "9:9-11", DANIEL_OLD_GRIEF, COLD, who="daniel"),
        A([d("9:12-14")], "9:12-14", lambda w, h: K.law_scroll(w, h, 504), "#2A1A2A", who="daniel"),
        A([d("9:15-16")], "9:15-16", lambda w, h: K.exodus_sea(w, h, 505), "#8FD0E2", who="daniel"),
        T([d("9:17-19")], "9:17-19", DANIEL_OLD_PRAY, GOLDEN, who="daniel", head="O Lord, Hear; O Lord, Forgive"),
        A([d("9:20-21")], "9:20-21", lambda w, h: K.gabriel_fly("gf1", w, h, 506), EVE, who="daniel", head="The Man Gabriel"),
        Nt([*sp2("9:22", "and said,", "daniel", "gabriel"), ss("9:23", "gabriel")], "9:22-23", who="gabriel"),
        A([ss("9:24-27", "gabriel")], "9:24-27", lambda w, h: K.weeks_chart(w, h), BP, who="gabriel", head="Seventy Weeks")]
PG.extend(L.pack(SEGS, "DAN-C05-D", PG.next()))

SEGS2 = [T([c("10:1"), d("10:2-3")], "10:1-3", DANIEL_OLD_GRIEF, COLD, who="daniel", head="A Great Warfare", stamp=10),
         A([d("10:4-6")], "10:4-6", lambda w, h: K.hiddekel("hd1", w, h, 507), RIVER, who="daniel", head="A Man Clothed in Linen"),
         A([d("10:7-9")], "10:7-9", lambda w, h: K.hiddekel("hd2", w, h, 508, stage="fled"), RIVER, who="daniel"),
         A([d("10:10"), s("10:11", "daniel", to="And he said unto me,"), s("10:11", "linen", frm="O Daniel", to="I now sent."), s("10:11", "daniel", frm="And when he had spoken")],
           "10:10-11", lambda w, h: K.hiddekel("hd3", w, h, 509, stage="knees"), RIVER, who="linen"),
         A([*sp2("10:12", "Then said he unto me,", "daniel", "linen"), ss("10:13-14", "linen")], "10:12-14", lambda w, h: K.princes_chart(w, h), BP, who="linen"),
         T([d("10:15-17")], "10:15-17", DANIEL_OLD_AWE, COLD, who="daniel"),
         A([d("10:18"), s("10:19", "daniel", to="And he said,"), s("10:19", "touch", frm="O man greatly", to="yea, be strong."), s("10:19", "daniel", frm="And when he spake")],
           "10:18-19", lambda w, h: K.hiddekel("hd4", w, h, 510, stage="stand"), RIVER, who="touch"),
         A([*sp2("10:20", "Then said he,", "daniel", "linen"), ss("10:21", "linen")], "10:20-21", lambda w, h: K.princes_chart(w, h), BP, who="linen")]
PG.extend(L.pack(SEGS2, "DAN-C05-E", PG.next(), end=end_mark("NEXT · THE TIME OF THE END", "right: 10px; bottom: 34px")))
