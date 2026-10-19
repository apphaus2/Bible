"""Jeremiah volume, Chapter 14 — Gedaliah (Jeremiah 40–42). Every verse, word for word from ref/asv.
The chains loosed at Ramah — all the land is before thee; the prophet goes to Gedaliah at Mizpah; the captains of the forces;
fear not to serve the Chaldeans; the Jews return from Moab, Ammon and Edom (a map) and gather wine and summer fruits; Johanan's
warning, believed not; Ishmael at table in Mizpah; the slaying of Gedaliah and of the fourscore men, and Asa's pit (41:2–3,
41:7–9 words over the shut house at night and the pit's mouth at evening; no one drawn); the ten men with stores hidden in the
field; the captives carried toward Ammon and turned back at the great waters of Gibeon; Geruth Chimham; then the remnant before
the prophet — pray for us; after ten days, if ye will still abide in this land; go ye not into Egypt."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art14 as K
from jer.common import (pack, cp, say, gd, says, gods, caps, cut, S, O, jer, GEDALIAH, NEBUZARADAN, JOHANAN, ISHMAEL, PEOPLE, GOLDEN, COLD, RED, NIGHT)
from jer import ch13 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W3, G3, S3, C3 = (jer(3, "word"), GOLDEN), (jer(3, "grief"), COLD), (jer(3, "stern"), RED), (jer(3, "calm"), GOLDEN)
MAP = "#0B1A2E"
MIZ = ("#8FD0E2", lambda w, h: K.mizpah("mz14", w, h, 1402))


@P("JER-C14-00-Title", "Chapter 14 · Gedaliah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.mizpah_harvest("t14", 760, 780, 1401)}</g><rect x="0" y="0" width="760" height="302" fill="#8FC0E0"></rect>')
    return chapter_title(14, "第十四話", "Gedaliah", "Jeremiah 40 – 42", svg, "#3A5A6A", v("40:9", frm="Fear not to serve the Chaldeans:"), "Jeremiah · Volume Twenty-Four")


SEGS = [O("40:1", kind="cap", a=("#6A5A6A", lambda w, h: K.chains_loosed("cl14", w, h, 1403)), k=0.26, head="The Chains Which Are upon Thy Hand", stamp=40),
        S([cp("40:2", to="and said unto him,"), say("40:2", frm="Jehovah thy God"), say("40:3")], "40:2-3", t=(NEBUZARADAN, GOLDEN)),
        O("40:4", kind="say", t=(NEBUZARADAN, GOLDEN)),
        S([cp("40:5", to="Now while he was not yet gone back,"), say("40:5", frm="Go back then,", to="Go back then,"), cp("40:5", frm="said he,", to="said he,"),
           say("40:5", frm="to Gedaliah", to="to go."), cp("40:5", frm="So the captain")], "40:5", t=(NEBUZARADAN, GOLDEN)),
        O("40:6", kind="cap", a=MIZ, k=0.3, head="Gedaliah at Mizpah"),
        O("40:7-8", kind="cap", a=("#8FD0E2", lambda w, h: K.mizpah("mz14b", w, h, 1404))),
        S([cp("40:9", to="saying,"), say("40:9", frm="Fear not"), say("40:10")], "40:9-10", t=(GEDALIAH, GOLDEN)),
        O("40:11-12", kind="cap", a=(MAP, lambda w, h: K.jews_return(w, h)), k=0.44),
        S([cp("40:13"), cp("40:14", to="and said unto him,"), say("40:14", frm="Dost thou know", to="to take thy life?"), cp("40:14", frm="But Gedaliah")], "40:13-14",
          t=(JOHANAN, RED), head="Dost Thou Know?"),
        S([cp("40:15", to="saying,"), say("40:15", frm="Let me go,")], "40:15", t=(JOHANAN, RED)),
        S([cp("40:16", to="said unto Johanan the son of Kareah,"), say("40:16", frm="Thou shalt not do this thing;")], "40:16", t=(GEDALIAH, GOLDEN)),
        O("41:1", kind="cap", a=("#5A3A2A", lambda w, h: K.eat_bread("eb14", w, h, 1406)), k=0.3, head="In the Seventh Month", stamp=41),
        O("41:2-3", kind="cap", a=("#120E1E", lambda w, h: K.shut_house(w, h, 1407)), k=0.28),
        S([caps("41:4-5")], "41:4-5", a=("#8A8A9A", lambda w, h: K.fourscore("fs14", w, h, 1408)), k=0.36, head="Fourscore Men"),
        S([cp("41:6", to="he said unto them,"), say("41:6", frm="Come to Gedaliah")], "41:6", t=(ISHMAEL, RED)),
        S([cp("41:7"), cp("41:8", to="that said unto Ishmael,"), say("41:8", frm="Slay us not;", to="and of honey."), cp("41:8", frm="So he forbare,")], "41:7-8",
          a=("#8FB0C8", lambda w, h: K.stores(w, h, 1409)), k=0.42),
        O("41:9", kind="cap", a=("#2A1A2A", lambda w, h: K.asa_pit(w, h, 1410)), k=0.3),
        O("41:10", kind="cap", a=("#6A5A6A", lambda w, h: K.captives_ammon("ca14", w, h, 1411)), k=0.32),
        O("41:11-14", kind="cap", a=("#8FB0C8", lambda w, h: K.gibeon_waters("gw14", w, h, 1412)), head="The Great Waters That Are in Gibeon"),
        O("41:15-16", kind="cap", t=(JOHANAN, GOLDEN)),
        O("41:17-18", kind="cap", a=(MAP, lambda w, h: K.geruth(w, h)), k=0.3),
        S([cp("42:1"), cp("42:2", to="and said unto Jeremiah the prophet,"), say("42:2", frm="Let, we pray thee,"), say("42:3")], "42:1-3",
          a=("#8A8A9A", lambda w, h: K.remnant("rm14", w, h, 1413)), k=0.48, head="Pray for Us", stamp=42),
        S([cp("42:4", to="Then Jeremiah the prophet said unto them,"), say("42:4", frm="I have heard you;")], "42:4", t=C3),
        S([cp("42:5", to="Then they said to Jeremiah,"), say("42:5", frm="Jehovah be"), say("42:6")], "42:5-6", t=(JOHANAN, GOLDEN)),
        S([cp("42:7"), cp("42:8"), cp("42:9", to="and said unto them,"), gd("42:9", frm="Thus saith")], "42:7-9", t=W3, head="After Ten Days"),
        O("42:10-12", a=("#8FC0E0", lambda w, h: K.summer_fruits("sf14", w, h, 1414))),
        O("42:13-14", a=("#E8A060", lambda w, h: K.egypt_road(w, h, 1415)), head="Go Ye Not into Egypt"),
        O("42:15-16", t=S3),
        O("42:17-18", t=S3),
        O("42:19-20", kind="say", t=G3),
        O("42:21-22", kind="say", t=S3)]
PG.extend(pack(SEGS, "JER-C14-D", PG.next(), end=end_mark("NEXT · INTO EGYPT", "right: 10px; bottom: 34px")))
