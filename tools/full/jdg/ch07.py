"""Judges volume, Chapter 7 — Delilah (Judges 16). Every verse, word for word from ref/eng-asv.
Gaza (16:1 is words over the gate at night) and the doors of the gate carried to the top of the mountain; Delilah and the
lords' eleven hundred pieces of silver; the green withes, the new ropes, the web — The Philistines are upon thee, Samson;
the razor, the seven locks shaven (the digest's panels); the prison-house mill (16:21 is words over the mill: no wound
drawn); the feast of Dagon; the two middle pillars; Let me die with the Philistines; and his burial between Zorah and
Eshtaol at evening."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import judges2 as J2
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis.art2 import hills, ground
from genesis.art3 import sun
from jdg import G, art as K
from jdg.common import pack, say, gd, cp, says, gods, caps, over, face, drawn, D, SAMSON, SAMSON_SLEEP, SAMSON_PRAY, DELILAH, RED, COLD, GOLDEN
from jdg import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P

def dagon(w, h, seed):
    """The house of Dagon full of men and women, the lords within and three thousand upon the roof."""
    return f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#3A1A2E"></rect>' + J2.temple(w, h, h * 0.16, (w * 0.4, w * 0.6), uid=f"dg{seed}", seed=seed)

def zorah(w, h, seed):
    """Between Zorah and Eshtaol at evening: the hills of Dan, no grave drawn."""
    return (f'<rect x="-10" y="-10" width="{w + 20}" height="{h + 20}" fill="#3A2A4A"></rect>' + sun(w * 0.5, h * 0.6, 34, color="#FF8A3D", op=0.4)
            + hills(w, h, h * 0.56, seed, color="#4A3050", amp=30, step=110) + hills(w, h, h * 0.72, seed + 1, color="#2A1E30", amp=20))


@P("JDG-C07-00-Title", "Chapter 7 · Delilah", title=True)
def title(n):
    bg, art = D("B8", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A1A2E"></rect><g transform="translate(0 300)">{art(760, 780)}</g>')
    return chapter_title(7, "第七話", "Delilah", "Judges 16", svg, "#3A1A2E", v("16:28", frm="remember me,", to="only this once,"), "Judges · Volume Seven")


SEGS = [over([caps("16:1"), cp("16:2", to="saying,"), say("16:2", frm="Samson is come", to="hither."), cp("16:2", frm="And they compassed", to="saying,"), say("16:2", frm="Let be")],
             "JDG 16:1–2", "B5", 0, head="The Gate of Gaza", stamp=16),
        over([caps("16:3")], "JDG 16:3", "B5", 1),
        over([caps("16:4")], "JDG 16:4", "B5", 2, head="Delilah"),
        over([cp("16:5", to="said unto her,"), say("16:5", frm="Entice him,")], "JDG 16:5", "B6", 0),
        face([cp("16:6", to="said to Samson,"), say("16:6", frm="Tell me,")], "JDG 16:6", DELILAH, bg=RED),
        face([cp("16:7", to="said unto her,"), say("16:7", frm="If they bind"), caps("16:8"), cp("16:9", to="said unto him,"), say("16:9", frm="The Philistines are upon thee,", to="Samson."),
              cp("16:9", frm="And he brake")], "JDG 16:7–9", SAMSON),
        face([cp("16:10", to="said unto Samson,"), say("16:10", frm="Behold,"), cp("16:11", to="said unto her,"), say("16:11", frm="If they only")], "JDG 16:10–11", DELILAH, bg=RED),
        face([cp("16:12", to="and said unto him,"), say("16:12", frm="The Philistines", to="Samson."), cp("16:12", frm="And the liers-in-wait")], "JDG 16:12", SAMSON),
        face([cp("16:13", to="said unto Samson,"), say("16:13", frm="Hitherto", to="mightest be bound."), cp("16:13", frm="And he said unto her,", to="said unto her,"), say("16:13", frm="If thou weavest"),
              cp("16:14", to="and said unto him,"), say("16:14", frm="The Philistines", to="Samson."), cp("16:14", frm="And he awaked")], "JDG 16:13–14", DELILAH, bg=RED),
        over([cp("16:15", to="And she said unto him,"), say("16:15", frm="How canst"), caps("16:16")], "JDG 16:15–16", "B6", 1, head="He Told Her All His Heart"),
        over([cp("16:17", to="and said unto her,"), say("16:17", frm="There hath not")], "JDG 16:17", "B6", 2),
        face([cp("16:18", to="saying,"), say("16:18", frm="Come up", to="all his heart."), cp("16:18", frm="Then the lords")], "JDG 16:18", DELILAH, bg=RED),
        over([caps("16:19")], "JDG 16:19", "B7", 0),
        over([cp("16:20", to="And she said,"), say("16:20", frm="The Philistines", to="Samson.")], "JDG 16:20", "B7", 1),
        over([cp("16:20", frm="And he awoke", to="and said,"), say("16:20", frm="I will go out", to="free."), cp("16:20", frm="But he knew not")], "JDG 16:20", "B7", 2),
        over([caps("16:21-22")], "JDG 16:21–22", "B7", 3, head="The Prison-house"),
        drawn([cp("16:23", to="for they said,"), say("16:23", frm="Our god hath"), cp("16:24", to="for they said,"), say("16:24", frm="Our god hath")], "JDG 16:23–24",
              K.below(lambda w, h: dagon(w, h, 711), 0.3), "#3A1A2E", head="Dagon Their God"),
        drawn([cp("16:25", to="that they said,"), say("16:25", frm="Call for Samson,", to="make us sport."), cp("16:25", frm="And they called"), cp("16:26", to="held him by the hand,"),
               say("16:26", frm="Suffer me"), caps("16:27")], "JDG 16:25–27", K.below(lambda w, h: dagon(w, h, 712), 0.42), "#3A1A2E"),
        face([cp("16:28", to="and said,"), say("16:28", frm="O Lord Jehovah,")], "JDG 16:28", SAMSON_PRAY, bg=GOLDEN, head="Remember Me"),
        over([caps("16:29"), cp("16:30", to="And Samson said,"), say("16:30", frm="Let me die", to="Philistines."), cp("16:30", frm="And he bowed", to="all his might;")], "JDG 16:29–30", "B8", 1, head="The Two Middle Pillars"),
        over([cp("16:30", frm="and the house fell")], "JDG 16:30", "B8", 2),
        drawn([caps("16:31")], "JDG 16:31", lambda w, h: zorah(w, h, 713), "#3A2A4A")]
PG.extend(pack(SEGS[:-3], "JDG-C07-D", PG.next()))
PG.extend(pack(SEGS[-3:], "JDG-C07-E", PG.next(), end=end_mark("NEXT · MICAH AND THE DANITES", "right: 10px; bottom: 34px")))
