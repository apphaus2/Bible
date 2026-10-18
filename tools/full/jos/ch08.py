"""Joshua volume, Chapter 8 — The Lots of the Seven Tribes (Joshua 18–19). Every verse, word for word from ref/asv.
The tent of meeting set up at Shiloh; How long are ye slack?; three men of each tribe describe the land by cities into seven
portions in a book; Joshua casts lots before Jehovah; then the seven lots — Benjamin, Simeon, Zebulun, Issachar, Asher,
Naphtali and Dan — as roll cells, every border and city; and Joshua's own inheritance, Timnath-serah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages, verse_cells
from deu.common import shade
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn
from jos import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
CODE = "JOSH"


@P("JOS-C08-00-Title", "Chapter 8 · The Lots of the Seven Tribes", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#E8D8B0"></rect><g transform="translate(0 360)">{K.shiloh("t8", 760, 720, 801, lots=True)}</g>')
    return chapter_title(8, "第八話", "The Lots of the Seven Tribes", "Joshua 18 – 19", svg, "#E8D8B0", v("18:10", to="before Jehovah:"), "Joshua · Volume Six")


SEGS = [drawn([caps("18:1-2")], "JOSH 18:1–2", lambda w, h: K.shiloh("sh8", w, h, 811), "#E8D8B0", head="At Shiloh", stamp=18),
        face([cp("18:3", to="children of Israel,"), ("say", v("18:3", frm="How long") + " " + sp("18:4-7"))], "JOSH 18:3–7", "lead"),
        drawn([cp("18:8", to="saying,"), say("18:8", frm="Go and walk"), caps("18:9")], "JOSH 18:8–9", K.below(lambda w, h: K.surveyors("sv8", w, h, 812), 0.42), "#0B1A2E"),
        drawn([caps("18:10")], "JOSH 18:10", lambda w, h: K.shiloh("sh8b", w, h, 813, lots=True), "#E8D8B0")]
PG.extend(pack(SEGS, "JOS-C08-D", PG.next()))

HEAD = "The Seven Lots"
LOTS = (verse_cells(G, CODE, 18, 11, 20, "Benjamin", "#9CCB5E", head=HEAD, budget=700)
        + verse_cells(G, CODE, 18, 21, 28, "Benjamin", "#9CCB5E", budget=600, brk=r"villages[.]")
        + verse_cells(G, CODE, 19, 1, 9, "Simeon", "#E8C840", budget=700)
        + verse_cells(G, CODE, 19, 10, 16, "Zebulun", "#5AC8C8", budget=700)
        + verse_cells(G, CODE, 19, 17, 23, "Issachar", "#B88AE8", budget=700)
        + verse_cells(G, CODE, 19, 24, 31, "Asher", "#E8C88A", budget=700)
        + verse_cells(G, CODE, 19, 32, 39, "Naphtali", "#D8E4F0", budget=700)
        + verse_cells(G, CODE, 19, 40, 48, "Dan", "#7AA8FF", budget=700))
PG.extend(roll_pages(LOTS, "JOS-C08-L", PG.next(), "Joshua", CODE, tag="THE LOTS OF THE SEVEN TRIBES · JOSHUA 18–19"))

SEGS2 = [drawn([caps("19:49-51")], "JOSH 19:49–51", lambda w, h: K.timnath("tm8", w, h, 814), "#F3D8A0", head="Timnath-serah")]
PG.extend(pack(SEGS2, "JOS-C08-E", PG.next(), end=end_mark("NEXT · THE CITIES OF REFUGE", "right: 10px; bottom: 34px")))
