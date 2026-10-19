"""Song of Solomon volume, Chapter 1 — I Am a Rose of Sharon (Song of Solomon 1–2). Every verse, word for word from ref/asv.
The Song of songs (1:1 in a caption) and the bride's first lines beside her face; black, but comely, among the vineyards,
the tents of Kedar and the curtains of Solomon; the flocks at noon and the shepherds' tents; a steed in Pharaoh's chariots
and plaits of gold; the henna-flowers of En-gedi; the green couch under the cedars, with doves; the rose of Sharon and the
lily among thorns; the apple-tree and the banner; the roes and the hinds of the field; the hart leaping on the mountains and
the lattice; the winter past and the voice of the turtle-dove; the dove in the clefts of the rock; the little foxes; the
flock among the lilies."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from sng import G, art as K
from sng.common import (paged, face, drawn, cp, sg, sgs, BRIDE, BRIDE_GLAD, BELOVED, DAUGHTER, COLD, GOLDEN, DUSK, ROSE, LEAF)

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("SNG-C01-00-Title", "Chapter 1 · I Am a Rose of Sharon", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 280)">{K.spring(760, 800, 101)}</g>')
    return chapter_title(1, "第一話", "I Am a Rose of Sharon", "Song of Solomon 1 – 2", svg, "#4A7A5A", v("2:4", frm="And his banner"), "Song of Solomon · Volume Twenty-Two")


PAGE = [[face("1:1-4", BRIDE, lines=[cp("1:1"), *sgs("1:2-4")], bg=ROSE, head="The Song of Songs", stamp=1),
         drawn("1:5-6", lambda w, h: K.vineyard_keeper("vk1", w, h, 102), "#FFB04A")],
        [face("1:7", BRIDE, bg=ROSE),
         drawn("1:8", lambda w, h: K.noon_flocks("nf1", w, h, 103), "#8FD0E2"),
         face("1:9-11", BELOVED)],
        [drawn("1:12-14", lambda w, h: K.engedi(w, h, 104), "#E8B88A"),
         face("1:15", BELOVED)],
        [drawn("1:16-17", lambda w, h: K.bower(w, h, 105), "#CFE8C8"),
         drawn("2:1-2", lambda w, h: K.rose_lily(w, h, 106), "#CFE8C8", head="A Rose of Sharon", stamp=2)],
        [drawn("2:3-4", lambda w, h: K.apple_tree("at1", w, h, 107), "#8FD0E2"),
         face("2:5-6", BRIDE_GLAD, bg=ROSE)],
        [drawn("2:7", lambda w, h: K.roes_field(w, h, 108), "#6A5A8A"),
         drawn("2:8-9", lambda w, h: K.leaping(w, h, 109), "#8FD0E2")],
        [drawn("2:10-13", lambda w, h: K.spring(w, h, 110), "#8FD0E2", lines=[sg("2:10", to="said unto me,"), sg("2:10", frm="Rise up"), *sgs("2:11-13")], head="The Winter Is Past"),
         drawn("2:14", lambda w, h: K.dove_rock(w, h, 111), "#8FD0E2")],
        [drawn("2:15", lambda w, h: K.foxes(w, h, 112), "#8FD0E2"),
         drawn("2:16-17", lambda w, h: K.lilies_flock("lf1", w, h, 113), "#5A4A7A")]]
PG.extend(paged(PAGE, "SNG-C01-", PG.next(), end=end_mark("NEXT · A GARDEN SHUT UP", "right: 10px; bottom: 34px")))
