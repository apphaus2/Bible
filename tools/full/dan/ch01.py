"""Daniel volume, Chapter 1 — A Stone Cut Out Without Hands (Daniel 1–2). Every verse, word for word from ref/asv.
Jerusalem besieged and the vessels of the house of God carried to Shinar; the youths of the seed royal in the king's palace
and their new names (a plate); Daniel purposed in his heart — prove thy servants ten days (the gold table and the plain
board); ten times better than all the magicians; then the king's dream that none could tell, the Chaldeans before the throne,
the decree (Arioch's men going out), the four praying by night and Daniel's blessing; and the great image as a blueprint
plate: the metals, the stone cut out without hands, the chaff and the mountain, the four kingdoms; the king fallen upon his
face, and Daniel ruler over the province of Babylon."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from dan import G, art as K
from dan.common import (L, DANIEL_Y, DANIEL_Y_PRAY, DANIEL, DANIEL_PRAY, NEB, NEB_TROUBLED, NEB_ANGRY, NEB_AWE, ASHPENAZ, ARIOCH, CHALDEAN,
                        COLD, GOLDEN, RED, NIGHT)

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
HALL, BP, DUSK = "#173A7A", "#0B2A4A", "#3A2A5A"


@P("DAN-C01-00-Title", "Chapter 1 · A Stone Cut Out Without Hands", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0B2A4A"></rect><g transform="translate(60 300)">{K.image_plate(640, 780, 1)}</g>')
    return chapter_title(1, "第一話", "A Stone Cut Out Without Hands", "Daniel 1 – 2", svg, "#0B2A4A", v("2:34", to="without hands,"), "Daniel · Volume Twenty-Seven")


c, cs, s, ss, sl, cut, A, T, Nt = L.c, L.cs, L.s, L.ss, L.sl, L.cut, L.A, L.T, L.N

SEGS = [A([c("1:1")], "1:1", lambda w, h: K.siege_forts("sf1", w, h, 101), "#5A4A5A", head="Nebuchadnezzar Came unto Jerusalem", stamp=1),
        A([c("1:2")], "1:2", lambda w, h: K.treasure_house("th1", w, h, 111), "#1A2440"),
        A([cs("1:3-5")], "1:3-5", lambda w, h: K.youths("yo1", w, h, 102), HALL, head="The King's Dainties"),
        A([cs("1:6-7")], "1:6-7", lambda w, h: K.names_plate(w, h), BP),
        T([cs("1:8-9")], "1:8-9", DANIEL_Y, GOLDEN),
        T([*cut("1:10", "said unto Daniel,", "eunuch")], "1:10", ASHPENAZ, COLD, who="eunuch"),
        A([c("1:11"), ss("1:12-13", "daniel")], "1:11-13", lambda w, h: K.two_tables(w, h, 103), HALL, who="daniel", head="Prove Thy Servants Ten Days"),
        A([cs("1:14-16")], "1:14-16", lambda w, h: K.two_tables(w, h, 104, ten=True), HALL),
        T([cs("1:17")], "1:17", DANIEL_Y_PRAY, GOLDEN),
        A([cs("1:18-21")], "1:18-21", lambda w, h: K.before_king("bk1", w, h, 105), HALL, head="Ten Times Better")]
PG.extend(L.pack(SEGS, "DAN-C01-D", PG.next()))

SEGS2 = [A([cs("2:1")], "2:1", lambda w, h: K.king_bed("kb1", w, h, 106), "#2A1A2A", head="Nebuchadnezzar Dreamed Dreams", stamp=2),
         A([c("2:2"), *cut("2:3", "said unto them,", "king")], "2:2-3", lambda w, h: K.wise_men("wm1", w, h, 107), HALL, who="king"),
         T([*cut("2:4", "in the Syrian language,", "chald")], "2:4", CHALDEAN, COLD, who="chald"),
         T([*cut("2:5", "said to the Chaldeans,", "king"), ss("2:6", "king")], "2:5-6", NEB_ANGRY, RED, who="king"),
         T([*cut("2:7", "and said,", "chald")], "2:7", CHALDEAN, COLD, who="chald"),
         T([*cut("2:8", "and said,", "king"), ss("2:9", "king")], "2:8-9", NEB_ANGRY, RED, who="king"),
         T([*cut("2:10", "and said,", "chald"), ss("2:11", "chald")], "2:10-11", CHALDEAN, COLD, who="chald"),
         A([cs("2:12-13")], "2:12-13", lambda w, h: K.guards_out("go1", w, h, 108), DUSK, head="The Decree Went Forth"),
         T([c("2:14"), c("2:15", to="the king's captain,"), s("2:15", "daniel", frm="Wherefore", to="from the king?"), c("2:15", frm="Then Arioch")], "2:14-15", DANIEL, GOLDEN, who="daniel"),
         T([cs("2:16")], "2:16", DANIEL, GOLDEN),
         A([cs("2:17-19")], "2:17-19", lambda w, h: K.four_pray("fp1", w, h, 109), "#3A2A2A", head="A Vision of the Night"),
         Nt([*cut("2:20", "and said,", "daniel", poem=True), *sl("2:21-23", "daniel")], "2:20-23", who="daniel"),
         T([*cut("2:24", "said thus unto him:", "daniel")], "2:24", DANIEL, GOLDEN, who="daniel"),
         T([*cut("2:25", "said thus unto him,", "arioch")], "2:25", ARIOCH, RED, who="arioch"),
         T([*cut("2:26", "Belteshazzar,", "king")], "2:26", NEB_TROUBLED, COLD, who="king", head="There Is a God in Heaven"),
         T([*cut("2:27", "and said,", "daniel"), ss("2:28-30", "daniel")], "2:27-30", DANIEL, GOLDEN, who="daniel"),
         A([ss("2:31-33", "daniel")], "2:31-33", lambda w, h: K.image_plate(w, h, 0), BP, who="daniel", head="A Great Image", wk=0.4),
         A([ss("2:34", "daniel")], "2:34", lambda w, h: K.image_plate(w, h, 1), BP, who="daniel", wk=0.3),
         A([ss("2:35", "daniel")], "2:35", lambda w, h: K.image_plate(w, h, 2), BP, who="daniel", wk=0.45),
         T([ss("2:36-38", "daniel")], "2:36-38", DANIEL, GOLDEN, who="daniel", head="Thou Art the Head of Gold"),
         A([ss("2:39-43", "daniel")], "2:39-43", lambda w, h: K.image_plate(w, h, 3), BP, who="daniel", wk=0.62),
         T([ss("2:44-45", "daniel")], "2:44-45", DANIEL, GOLDEN, who="daniel", head="A Kingdom Which Shall Never Be Destroyed"),
         A([c("2:46"), *cut("2:47", "and said,", "king"), cs("2:48-49")], "2:46-49", lambda w, h: K.oblation("ob1", w, h, 110), HALL)]
PG.extend(L.pack(SEGS2, "DAN-C01-E", PG.next(), end=end_mark("NEXT · THE BURNING FIERY FURNACE", "right: 10px; bottom: 34px")))
