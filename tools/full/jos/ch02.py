"""Joshua volume, Chapter 2 — The Waters of the Jordan (Joshua 3–5). Every verse, word for word from ref/asv.
The ark goes before with a space of two thousand cubits; the priests' feet in the brink and the waters standing in one heap;
all Israel over on dry ground; twelve stones out of the midst of the Jordan, set up in Gilgal — what mean these stones?;
the kings' hearts melted; the knives of flint (drawn as the knives laid on a stone and the camp abiding: nothing more);
the passover at Gilgal and the manna ceased; and the prince of the host of Jehovah with his sword drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from exo import art3 as A3, art4 as A4
from jos import G, art as K
from jos.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D
from jos import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JOS-C02-00-Title", "Chapter 2 · The Waters of the Jordan", title=True)
def title(n):
    bg, art = D("P03", 0)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFC14D"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(2, "第二話", "The Waters of the Jordan", "Joshua 3 – 5", svg, "#FFC14D", v("3:16", frm="the waters which came down", to="in one heap,"), "Joshua · Volume Six")


SEGS = [over([caps("3:1-2")], "JOSH 3:1–2", "P01", 1, head="The Ark of the Covenant", stamp=3),
        drawn([cp("3:3", to="saying,"), ("say", v("3:3", frm="When ye see") + " " + v("3:4"))], "JOSH 3:3–4", lambda w, h: K.ark_ahead("aa2", w, h, 211), "#F3D8A0"),
        face([cp("3:5", to="unto the people,"), say("3:5", frm="Sanctify"), cp("3:6", to="saying,"), say("3:6", frm="Take up", to="before the people."),
              cp("3:6", frm="And they took up")], "JOSH 3:5–6", "lead"),
        face([cp("3:7", to="unto Joshua,"), gd("3:7", frm="This day"), gd("3:8")], "JOSH 3:7–8", "awe"),
        face([cp("3:9", to="children of Israel,"), say("3:9", frm="Come hither"), cp("3:10", to="And Joshua said,"),
              ("say", v("3:10", frm="Hereby") + " " + sp("3:11-13"))], "JOSH 3:9–13", "lead", head="They Shall Stand in One Heap"),
        over([caps("3:14-16")], "JOSH 3:14–16", "P03", 0),
        over([caps("3:17")], "JOSH 3:17", "P03", 1),
        face([cp("4:1"), gods("4:2-3")], "JOSH 4:1–3", "awe", head="Twelve Stones", stamp=4),
        face([cp("4:4"), cp("4:5", to="said unto them,"), ("say", v("4:5", frm="Pass over") + " " + sp("4:6-7"))], "JOSH 4:4–7", "calm"),
        drawn([caps("4:8-9")], "JOSH 4:8–9", lambda w, h: K.stones_carried("st2", w, h, 212), "#8FD0E2"),
        drawn([caps("4:10-13")], "JOSH 4:10–13", lambda w, h: K.armed("ar2", w, h, 213), "#F3D8A0"),
        face([caps("4:14"), cp("4:15"), gd("4:16"), cp("4:17", to="saying,"), say("4:17", frm="Come ye up")], "JOSH 4:14–17", "awe"),
        drawn([caps("4:18")], "JOSH 4:18", lambda w, h: K.waters_return("wr2", w, h, 214), "#8FD0E2"),
        drawn([caps("4:19-20"), cp("4:21", to="saying,"), ("say", v("4:21", frm="When your") + " " + sp("4:22-24"))], "JOSH 4:19–24",
              lambda w, h: K.gilgal("gg2", w, h, 215), "#F3D8A0", head="What Mean These Stones?"),
        drawn([caps("5:1")], "JOSH 5:1", lambda w, h: K.kings_afar("ka2", w, h, 216), "#3A1A2E", head="Knives of Flint", stamp=5),
        drawn([cp("5:2", to="unto Joshua,"), gd("5:2", frm="Make thee"), caps("5:3-5")], "JOSH 5:2–5", lambda w, h: K.flint(w, h, 217), "#E8C88A"),
        drawn([caps("5:6-8")], "JOSH 5:6–8", lambda w, h: A4.wilderness("wd2", w, h, 218), "#E8C88A"),
        face([cp("5:9", to="unto Joshua,"), gd("5:9", frm="This day", to="from off you."), cp("5:9", frm="Wherefore")], "JOSH 5:9", "awe"),
        drawn([caps("5:10-12")], "JOSH 5:10–12", lambda w, h: A3.cakes(w, h, 219), "#2A1A2E", head="The Manna Ceased"),
        over([cp("5:13", to="said unto him,"), say("5:13", frm="Art thou")], "JOSH 5:13", "P04", 0, head="The Prince of the Host of Jehovah"),
        over([cp("5:14", to="And he said,"), gd("5:14", frm="Nay;", to="now come."), cp("5:14", frm="And Joshua fell", to="said unto him,"), say("5:14", frm="What saith")],
             "JOSH 5:14", "P04", 1),
        over([cp("5:15", to="said unto Joshua,"), gd("5:15", frm="Put off", to="is holy."), cp("5:15", frm="And Joshua did so.")], "JOSH 5:15", "P04", 3)]
PG.extend(pack(SEGS, "JOS-C02-D", PG.next(), end=end_mark("NEXT · THE WALLS OF JERICHO", "right: 10px; bottom: 34px")))
