"""Daniel volume, Chapter 2 — The Burning Fiery Furnace (Daniel 3–4). Every verse, word for word from ref/asv.
The image of gold in the plain of Dura and the rulers gathered to its dedication; the herald's decree over a plate of the
instruments; all the peoples fallen down, three men standing; the Chaldeans' accusation; who is that god that shall deliver
you?; we will not serve thy gods; the furnace heated seven times more (the mighty men slain by the flame told in words over
the furnace mouth); four men loose walking in the midst of the fire, the fourth only a shape of light; come forth, and come
hither; then the king's letter to all the peoples: the tree whose height reached unto heaven, the watcher and the holy one,
the stump with its band of iron and brass; Daniel's interpretation; is not this great Babylon?; the voice from heaven in the
Voice box; the king's madness told in words over the field wet with dew; and his understanding returned."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from dan import G, art2 as K
from dan.common import (L, DANIEL, DANIEL_STERN, NEB, NEB_TROUBLED, NEB_ANGRY, NEB_AWE, NEB_RESTORED, CHALDEAN_SLY, SHADRACH,
                        COLD, GOLDEN, RED, NIGHT)
from dan import ch01 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
HALL, BP, FIRE, SKY = "#173A7A", "#0B2A4A", "#2A1A2A", "#8FD0E2"


@P("DAN-C02-00-Title", "Chapter 2 · The Burning Fiery Furnace", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.furnace("t2", 760, 820, 201, stage="cast")}</g><rect x="0" y="0" width="760" height="262" fill="#2A1A2A"></rect>')
    return chapter_title(2, "第二話", "The Burning Fiery Furnace", "Daniel 3 – 4", svg, "#2A1A2A", v("3:25", frm="Lo, I see four men loose,", to="they have no hurt;"), "Daniel · Volume Twenty-Seven")


c, cs, s, ss, sl, cut, A, T, Nt, g, gs = L.c, L.cs, L.s, L.ss, L.sl, L.cut, L.A, L.T, L.N, L.g, L.gs

SEGS = [A([cs("3:1")], "3:1", lambda w, h: K.dura("du1", w, h, 202), SKY, head="The Image of Gold", stamp=3),
        A([cs("3:2-3")], "3:2-3", lambda w, h: K.dura("du2", w, h, 203), SKY),
        A([*cut("3:4", "cried aloud,", "herald"), ss("3:5-6", "herald")], "3:4-6", lambda w, h: K.instruments(w, h), BP, who="herald"),
        A([cs("3:7")], "3:7", lambda w, h: K.dura("du3", w, h, 204, stage="bow"), SKY),
        T([c("3:8"), *cut("3:9", "Nebuchadnezzar the king,", "chald"), ss("3:10-12", "chald")], "3:8-12", CHALDEAN_SLY, COLD, who="chald", head="Certain Chaldeans Came Near"),
        T([c("3:13"), *cut("3:14", "said unto them,", "king"), ss("3:15", "king")], "3:13-15", NEB_ANGRY, RED, who="king"),
        A([*cut("3:16", "said to the king,", "three"), ss("3:17-18", "three")], "3:16-18", lambda w, h: K.three_stand("ts1", w, h, 205), SKY, who="three", head="But If Not"),
        A([cs("3:19-20")], "3:19-20", lambda w, h: K.furnace("fu1", w, h, 206, stage="heat"), FIRE, head="Seven Times More"),
        A([cs("3:21-23")], "3:21-23", lambda w, h: K.furnace("fu2", w, h, 207, stage="cast"), FIRE),
        T([c("3:24", to="unto his counsellors,"), s("3:24", "king", frm="Did not we", to="fire?"), c("3:24", frm="They answered", to="unto the king,"),
           s("3:24", "counsel", frm="True, O king.")], "3:24", NEB_AWE, COLD, who="king", head="Four Men Loose"),
        A([*cut("3:25", "He answered and said,", "king")], "3:25", lambda w, h: K.furnace("fu3", w, h, 208, stage="four"), FIRE, who="king", wk=0.3),
        A([c("3:26", to="he spake and said,"), s("3:26", "king", frm="Shadrach, Meshach, and Abed-nego, ye servants", to="come hither."), c("3:26", frm="Then Shadrach"), c("3:27")],
          "3:26-27", lambda w, h: K.furnace("fu4", w, h, 209, stage="out"), FIRE),
        T([*cut("3:28", "spake and said,", "king"), ss("3:29", "king"), c("3:30")], "3:28-30", NEB_AWE, GOLDEN, who="king")]
PG.extend(L.pack(SEGS, "DAN-C02-D", PG.next()))

SEGS2 = [A([ss("4:1-3", "king")], "4:1-3", lambda w, h: K.babylon(w, h, 210), SKY, who="king", head="Unto All the Peoples", stamp=4),
         A([ss("4:4-7", "king")], "4:4-7", lambda w, h: K.wise_men("wm2", w, h, 211), HALL, who="king"),
         T([ss("4:8-9", "king")], "4:8-9", NEB_TROUBLED, COLD, who="king"),
         A([ss("4:10-12", "king")], "4:10-12", lambda w, h: K.great_tree(w, h, 212), SKY, who="king", head="A Tree in the Midst of the Earth"),
         A([ss("4:13", "king"), *cut("4:14", "and said thus,", "watcher"), ss("4:15-17", "watcher")], "4:13-17", lambda w, h: K.great_tree(w, h, 213, stage=1), NIGHT, who="watcher"),
         T([ss("4:18", "king")], "4:18", NEB_TROUBLED, COLD, who="king"),
         T([c("4:19", to="troubled him."), c("4:19", frm="The king answered", to="and said,"), s("4:19", "king", frm="Belteshazzar, let not", to="trouble thee."),
            c("4:19", frm="Belteshazzar answered", to="and said,"), s("4:19", "daniel", frm="My lord,")], "4:19", DANIEL, COLD, who="daniel", head="It Is Thou, O King"),
         A([ss("4:20-22", "daniel")], "4:20-22", lambda w, h: K.great_tree(w, h, 214), SKY, who="daniel"),
         A([ss("4:23-24", "daniel")], "4:23-24", lambda w, h: K.great_tree(w, h, 215, stage=2), SKY, who="daniel"),
         T([ss("4:25-27", "daniel")], "4:25-27", DANIEL_STERN, GOLDEN, who="daniel"),
         A([cs("4:28-29"), *cut("4:30", "spake and said,", "king")], "4:28-30", lambda w, h: K.palace_roof("pr1", w, h, 216), SKY, head="Is Not This Great Babylon?"),
         Nt([*cut("4:31", "saying,", "god"), gs("4:32")], "4:31-32"),
         A([cs("4:33")], "4:33", lambda w, h: K.dew_field(w, h, 217), "#9AB8D8"),
         T([ss("4:34-35", "king")], "4:34-35", NEB_RESTORED, GOLDEN, who="king", head="Mine Understanding Returned"),
         A([ss("4:36-37", "king")], "4:36-37", lambda w, h: K.restored("rs1", w, h, 218), HALL, who="king")]
PG.extend(L.pack(SEGS2, "DAN-C02-E", PG.next(), end=end_mark("NEXT · THE DEN OF LIONS", "right: 10px; bottom: 34px")))
