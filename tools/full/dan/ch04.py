"""Daniel volume, Chapter 4 — The Ancient of Days (Daniel 7–8). Every verse, word for word from ref/eng-asv.
Daniel's dream in the first year of Belshazzar, told in his own words over plates: the four winds upon the great sea; the
four beasts as heraldic emblems on a dark field (the lion with eagle's wings, the bear with three ribs, the leopard with four
wings and four heads, the fourth beast with iron teeth and ten horns, and the little horn with eyes); thrones placed and the
throne of fiery flames with its burning wheels and the fiery stream — light only where the ancient of days sat, never a
figure; the beast given to the fire; one like unto a son of man with the clouds of heaven (light in the clouds); the
interpretation by one that stood by (a gold-ruled box): four kings, ten horns, a time and times and half a time; then the
vision at Shushan by the river Ulai: the ram with two horns and the he-goat from the west, the four horns and the little
horn, two thousand and three hundred evenings and mornings, and Gabriel (a shape of light) — understand, O son of man."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from dan import G, art4 as K
from dan.common import L, DANIEL_OLD, DANIEL_OLD_AWE, DANIEL_OLD_GRIEF, DANIEL_OLD_PRAY, COLD, GOLDEN, RED, NIGHT
from dan import ch03 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
FLD, SEA, BP = K.FIELD, "#0B0B2A", "#0B2A4A"


@P("DAN-C04-00-Title", "Chapter 4 · The Ancient of Days", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 240)">{K.fiery_throne(760, 840, 401)}</g><rect x="0" y="0" width="760" height="242" fill="#0B0B2A"></rect>')
    return chapter_title(4, "第四話", "The Ancient of Days", "Daniel 7 – 8", svg, "#0B0B2A", v("7:9", frm="his throne was fiery flames,"), "Daniel · Volume Twenty-Seven")


c, cs, s, ss, sl, cut, A, T, Nt, sp2 = L.c, L.cs, L.s, L.ss, L.sl, L.cut, L.A, L.T, L.N, L.split
d = lambda refs: ss(refs, "daniel")

SEGS = [A([c("7:1"), *cut("7:2", "Daniel spake and said,", "daniel"), d("7:3")], "7:1-3", lambda w, h: K.sea_winds(w, h, 402), SEA, who="daniel", head="Four Great Beasts", stamp=7),
        A([d("7:4")], "7:4", lambda w, h: K.beast_plate(w, h, 1), FLD, who="daniel"),
        A([d("7:5")], "7:5", lambda w, h: K.beast_plate(w, h, 2), FLD, who="daniel"),
        A([d("7:6")], "7:6", lambda w, h: K.beast_plate(w, h, 3), FLD, who="daniel"),
        A([d("7:7")], "7:7", lambda w, h: K.beast_plate(w, h, 4), FLD, who="daniel"),
        A([d("7:8")], "7:8", lambda w, h: K.beast_plate(w, h, 4, 1), FLD, who="daniel"),
        A([d("7:9-10")], "7:9-10", lambda w, h: K.fiery_throne(w, h, 403), SEA, who="daniel", head="One That Was Ancient of Days"),
        A([d("7:11-12")], "7:11-12", lambda w, h: K.burned(w, h, 404), FLD, who="daniel"),
        A([d("7:13-14")], "7:13-14", lambda w, h: K.fiery_throne(w, h, 405, son=True, books=False), SEA, who="daniel", head="One Like unto a Son of Man"),
        T([d("7:15-16")], "7:15-16", DANIEL_OLD_AWE, COLD, who="daniel"),
        A([ss("7:17-18", "angel")], "7:17-18", lambda w, h: K.four_beasts(w, h, 406), FLD, who="angel"),
        A([d("7:19-20")], "7:19-20", lambda w, h: K.beast_plate(w, h, 4, 1), FLD, who="daniel"),
        T([d("7:21-22")], "7:21-22", DANIEL_OLD_AWE, COLD, who="daniel"),
        A([*sp2("7:23", "Thus he said,", "daniel", "angel"), ss("7:24-25", "angel")], "7:23-25", lambda w, h: K.time_bars(w, h), BP, who="angel"),
        A([ss("7:26-27", "angel")], "7:26-27", lambda w, h: K.kingdom_light(w, h, 407), "#FFE680", who="angel"),
        T([d("7:28")], "7:28", DANIEL_OLD_GRIEF, COLD, who="daniel")]
PG.extend(L.pack(SEGS, "DAN-C04-D", PG.next()))

SEGS2 = [A([d("8:1-2")], "8:1-2", lambda w, h: K.shushan(w, h, 408, tone="dusk"), "#3A2A5A", who="daniel", head="The Ram and the He-goat", stamp=8),
         A([d("8:3-4")], "8:3-4", lambda w, h: K.ulai("u1", w, h, 409, "ram"), FLD, who="daniel"),
         A([d("8:5-6")], "8:5-6", lambda w, h: K.ulai("u2", w, h, 410, "goat"), FLD, who="daniel"),
         A([d("8:7")], "8:7", lambda w, h: K.ulai("u3", w, h, 411, "smite"), FLD, who="daniel"),
         A([d("8:8")], "8:8", lambda w, h: K.ulai("u4", w, h, 412, "four"), FLD, who="daniel"),
         A([d("8:9-12")], "8:9-12", lambda w, h: K.ulai("u5", w, h, 413, "little"), FLD, who="daniel"),
         A([*sp2("8:13", "who spake,", "daniel", "holy"), *sp2("8:14", "said unto me,", "daniel", "holy")], "8:13-14", lambda w, h: K.evenings(w, h), BP, who="holy", head="How Long Shall Be the Vision?"),
         A([d("8:15"), *sp2("8:16", "and said,", "daniel", "ulai")], "8:15-16", lambda w, h: K.gabriel_bank("gb1", w, h, 414, fallen=False), "#2A2A5A", who="daniel", head="Gabriel"),
         A([*sp2("8:17", "said unto me,", "daniel", "gabriel"), d("8:18")], "8:17-18", lambda w, h: K.gabriel_bank("gb2", w, h, 415), "#2A2A5A", who="gabriel"),
         A([*sp2("8:19", "And he said,", "daniel", "gabriel"), ss("8:20-22", "gabriel")], "8:19-22", lambda w, h: K.ulai("u6", w, h, 416, "smite"), FLD, who="gabriel"),
         Nt([ss("8:23-26", "gabriel")], "8:23-26", who="gabriel"),
         T([d("8:27")], "8:27", DANIEL_OLD_GRIEF, COLD, who="daniel")]
PG.extend(L.pack(SEGS2, "DAN-C04-E", PG.next(), end=end_mark("NEXT · SEVENTY WEEKS", "right: 10px; bottom: 34px")))
