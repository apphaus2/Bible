"""Daniel volume, Chapter 3 — The Den of Lions (Daniel 5–6). Every verse, word for word from ref/eng-asv.
Belshazzar's feast to a thousand lords with the vessels of the temple; the fingers of a man's hand writing upon the plaster
(drawn only as a script of light on the wall, no hand); the king's knees smote one against another; the queen remembers
Daniel; let thy gifts be to thyself; MENE, TEKEL, PERES as a plate; Daniel clothed with purple; in that night Belshazzar
slain (words over the dark palace); Darius the Mede and his hundred and twenty satraps (a chart); the interdict signed;
Daniel at his open window toward Jerusalem; the den, the stone and the seals; the king's night of fasting; O Daniel,
servant of the living God; the lions' mouths shut (the den within, the lions lying still); the accusers cast in (words
over the sealed stone at dusk); and Darius's decree to all the earth."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from dan import G, art3 as K
from dan.common import (L, DANIEL_GREY, DANIEL_GREY_PRAY, DANIEL_OLD, DANIEL_OLD_PRAY, BELSH, BELSH_AFRAID, BELSH_KING, QUEEN, DARIUS, DARIUS_GRIEF,
                        DARIUS_GLAD, SATRAP, COLD, GOLDEN, RED, NIGHT)
from dan import ch02 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
HALL, BP, FEAST, SKY = "#173A7A", "#0B2A4A", "#3A2A2A", "#8FD0E2"


@P("DAN-C03-00-Title", "Chapter 3 · The Den of Lions", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#1E1824"></rect><g transform="translate(0 280)">{K.den("t3", 760, 800, 301, cover=True)}</g>')
    return chapter_title(3, "第三話", "The Den of Lions", "Daniel 5 – 6", svg, "#1E1824", v("6:22", to="they have not hurt me;"), "Daniel · Volume Twenty-Seven")


c, cs, s, ss, sl, cut, A, T, Nt, g, gs = L.c, L.cs, L.s, L.ss, L.sl, L.cut, L.A, L.T, L.N, L.g, L.gs

SEGS = [A([cs("5:1-2")], "5:1-2", lambda w, h: K.feast("fe1", w, h, 302), FEAST, head="Belshazzar Made a Great Feast", stamp=5),
        A([cs("5:3-4")], "5:3-4", lambda w, h: K.feast("fe2", w, h, 303), FEAST),
        A([cs("5:5")], "5:5", lambda w, h: K.feast("fe3", w, h, 304, stage="write"), FEAST, head="The Writing upon the Plaster"),
        T([cs("5:6"), *cut("5:7", "said to the wise men of Babylon,", "belsh")], "5:6-7", BELSH_AFRAID, COLD, who="belsh"),
        A([cs("5:8-9")], "5:8-9", lambda w, h: K.wise_men("wm3", w, h, 305, who="bel"), HALL),
        T([*cut("5:10", "the queen spake and said,", "queen"), ss("5:11-12", "queen")], "5:10-12", QUEEN, GOLDEN, who="queen"),
        T([*cut("5:13", "said unto Daniel,", "belsh"), ss("5:14-16", "belsh")], "5:13-16", BELSH_KING, GOLDEN, who="belsh", head="Art Thou That Daniel?"),
        T([*cut("5:17", "said before the king,", "daniel"), ss("5:18-19", "daniel")], "5:17-19", DANIEL_GREY, GOLDEN, who="daniel"),
        T([ss("5:20-21", "daniel")], "5:20-21", DANIEL_GREY, COLD, who="daniel"),
        T([ss("5:22-23", "daniel")], "5:22-23", DANIEL_GREY, RED, who="daniel"),
        A([ss("5:24-28", "daniel")], "5:24-28", lambda w, h: K.mene_plate(w, h), BP, who="daniel", head="Mene, Mene, Tekel, Upharsin"),
        A([cs("5:29")], "5:29", lambda w, h: K.purple_chain("pc1", w, h, 306), FEAST),
        A([cs("5:30")], "5:30", lambda w, h: K.dark_palace(w, h, 307), NIGHT, head="In That Night"),
        T([cs("5:31")], "5:31", DARIUS, GOLDEN)]
PG.extend(L.pack(SEGS, "DAN-C03-D", PG.next()))

SEGS2 = [A([cs("6:1-3")], "6:1-3", lambda w, h: K.satraps_chart(w, h), BP, head="Three Presidents", stamp=6),
         T([c("6:4"), *cut("6:5", "Then said these men,", "princes")], "6:4-5", SATRAP, RED, who="princes"),
         A([*cut("6:6", "said thus unto him,", "princes"), ss("6:7-8", "princes")], "6:6-8", lambda w, h: K.darius_court("dc1", w, h, 308), HALL, who="princes"),
         A([cs("6:9")], "6:9", lambda w, h: K.signed(w, h, 309), "#2A1A2A"),
         A([cs("6:10")], "6:10", lambda w, h: K.window_prayer("wp1", w, h, 310), "#8A6A4A", head="His Windows Were Open"),
         A([cs("6:11")], "6:11", lambda w, h: K.window_prayer("wp2", w, h, 311, watchers=True), "#8A6A4A"),
         T([c("6:12", to="the king's interdict:"), s("6:12", "princes", frm="Hast thou not", to="den of lions?"), c("6:12", frm="The king answered", to="and said,"),
            s("6:12", "darius", frm="The thing is true,")], "6:12", SATRAP, RED, who="princes"),
         T([*cut("6:13", "said before the king,", "princes")], "6:13", SATRAP, RED, who="princes"),
         T([c("6:14"), *cut("6:15", "said unto the king,", "princes")], "6:14-15", DARIUS_GRIEF, COLD),
         A([*cut("6:16", "said unto Daniel,", "darius")], "6:16", lambda w, h: K.den_mouth("dm1", w, h, 312, stage="cast"), "#5A3A5A", who="darius", head="The Den of Lions"),
         A([cs("6:17")], "6:17", lambda w, h: K.den_mouth("dm2", w, h, 313, stage="sealed"), "#2A1A3A"),
         A([cs("6:18")], "6:18", lambda w, h: K.king_night("kn1", w, h, 314), "#2A1A2A"),
         A([c("6:19"), *cut("6:20", "said to Daniel,", "darius")], "6:19-20", lambda w, h: K.den_mouth("dm3", w, h, 315, stage="dawn"), "#8A9AC8", who="darius", head="Very Early in the Morning"),
         A([*cut("6:21", "unto the king,", "daniel"), ss("6:22", "daniel")], "6:21-22", lambda w, h: K.den("dn1", w, h, 316, dawn=True, stone=False), "#1E1824", who="daniel"),
         A([cs("6:23")], "6:23", lambda w, h: K.den_mouth("dm4", w, h, 317, stage="up"), SKY),
         A([cs("6:24")], "6:24", lambda w, h: K.den_mouth("dm5", w, h, 318, stage="empty"), "#2A1A3A"),
         A([*cut("6:25", "in all the earth:", "darius"), ss("6:26-27", "darius")], "6:25-27", lambda w, h: K.empire_map(w, h, posts=True), BP, who="darius", head="The Living God"),
         T([cs("6:28")], "6:28", DANIEL_OLD, GOLDEN)]
PG.extend(L.pack(SEGS2, "DAN-C03-E", PG.next(), end=end_mark("NEXT · THE ANCIENT OF DAYS", "right: 10px; bottom: 34px")))
