"""Jeremiah volume, Chapter 13 — The Dungeon (Jeremiah 37–39). Every verse, word for word from ref/eng-asv.
Zedekiah made king; pray now unto Jehovah for us; Pharaoh's army and the Chaldeans breaking up (a map); the arrest in the
gate of Benjamin — thou art falling away to the Chaldeans; the dungeon-house; is there any word from Jehovah? There is; the
daily loaf; then the princes — let this man be put to death; the dungeon of Malchijah, no water but mire (the cistern's mouth
and the cords only; the prophet is not drawn in it); Ebed-melech the Ethiopian and the thirty men, the rags and worn-out
garments; the third entry — I will ask thee a thing; the fall of the city: the breach, the princes in the middle gate, the
flight between the two walls, Riblah (39:5–7 words over the empty plain), the city burned, the captives, the poor left with
vineyards; the prophet given to Gedaliah; and the word to Ebed-melech — thy life shall be for a prey unto thee."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art13 as K, art11 as K11
from jer.common import (pack, cp, say, gd, says, gods, caps, cut, S, O, jer, ZEDEKIAH, ZEDEKIAH_CALM, CAPTAIN, PRINCE, EBEDMELECH, NEBUZARADAN, GOLDEN, COLD, RED, NIGHT)
from jer import ch12 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W3, G3, S3, C3, A3 = (jer(3, "word"), GOLDEN), (jer(3, "grief"), COLD), (jer(3, "stern"), RED), (jer(3, "calm"), GOLDEN), (jer(3, "weary"), COLD)
MAP = "#0B1A2E"
PIT = "#6A5A6A"


@P("JER-C13-00-Title", "Chapter 13 · The Dungeon", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.dungeon("t13", 760, 780, 1301, stage=2)}</g><rect x="0" y="0" width="760" height="302" fill="#6A5A6A"></rect>')
    return chapter_title(13, "第十三話", "The Dungeon", "Jeremiah 37 – 39", svg, PIT, v("38:13", to="out of the dungeon:"), "Jeremiah · Volume Twenty-Four")


SEGS = [O("37:1-2", kind="cap", t=(ZEDEKIAH_CALM, GOLDEN), head="Zedekiah Reigned as King", stamp=37),
        S([cp("37:3", to="saying,"), say("37:3", frm="Pray now"), cp("37:4")], "37:3-4", t=(ZEDEKIAH, COLD)),
        O("37:5", kind="cap", a=(MAP, lambda w, h: K.pharaoh_relief(w, h)), k=0.24),
        S([cp("37:6"), gods("37:7-8")], "37:6-8", t=W3),
        O("37:9-10", t=S3),
        O("37:11-12", kind="cap", a=("#8FB0C8", lambda w, h: K11.field_anathoth("fa13", w, h, 1320)), k=0.3),
        S([cp("37:13", to="saying,"), say("37:13", frm="Thou art falling away"), cp("37:14", to="Then said Jeremiah,"), say("37:14", frm="It is false;", to="to the Chaldeans."),
           cp("37:14", frm="But he hearkened not")], "37:13-14", a=("#8FB0C8", lambda w, h: K.gate_arrest("ga13", w, h, 1302)), k=0.42, head="Thou Art Falling Away to the Chaldeans"),
        O("37:15-16", kind="cap", a=("#1E1A1E", lambda w, h: K.cells(w, h, 1303)), k=0.24, head="The Dungeon-House"),
        S([cp("37:17", to="and said,"), say("37:17", frm="Is there any word", to="from Jehovah?"), cp("37:17", frm="And Jeremiah said,", to="And Jeremiah said,"),
           say("37:17", frm="There is.", to="There is."), cp("37:17", frm="He said also,", to="He said also,"), say("37:17", frm="Thou shalt be delivered")], "37:17", t=(ZEDEKIAH, COLD)),
        S([cp("37:18", to="Moreover Jeremiah said unto king Zedekiah,"), say("37:18", frm="Wherein have I sinned"), says("37:19-20")], "37:18-20", t=A3),
        O("37:21", kind="cap", a=("#5A4A3A", lambda w, h: K.loaf(w, h, 1304)), k=0.3)]


SEGS2 = [S([cp("38:1"), gods("38:2-3")], "38:1-3", a=(PIT, lambda w, h: K.court_guard("cg13", w, h, 1305, age=3)), k=0.42, head="Let This Man Be Put to Death", stamp=38),
         S([cp("38:4", to="Then the princes said unto the king,"), say("38:4", frm="Let this man"), cp("38:5", to="And Zedekiah the king said,"), say("38:5", frm="Behold, he is in your hand;")],
           "38:4-5", t=(PRINCE, RED)),
         O("38:6", kind="cap", a=(PIT, lambda w, h: K.dungeon("dg13", w, h, 1306)), k=0.3, head="The Dungeon of Malchijah"),
         S([cp("38:7"), cp("38:8"), say("38:9")], "38:7-9", t=(EBEDMELECH, GOLDEN), head="Ebed-melech the Ethiopian"),
         S([cp("38:10", to="saying,"), say("38:10", frm="Take from hence"), cp("38:11")], "38:10-11", a=(PIT, lambda w, h: K.dungeon("dg13b", w, h, 1307, stage=1)), k=0.36),
         S([cp("38:12", to="said unto Jeremiah,"), say("38:12", frm="Put now these rags", to="under the cords."), cp("38:12", frm="And Jeremiah did so."), cp("38:13")], "38:12-13",
           a=(PIT, lambda w, h: K.dungeon("dg13c", w, h, 1308, stage=2)), k=0.36),
         S([cp("38:14", to="and the king said unto Jeremiah,"), say("38:14", frm="I will ask thee"), cp("38:15", to="Then Jeremiah said unto Zedekiah,"), say("38:15", frm="If I declare it")],
           "38:14-15", a=("#3A2A4A", lambda w, h: K.third_entry("te13", w, h, 1309)), k=0.4, head="I Will Ask Thee a Thing"),
         S([cp("38:16", to="saying,"), say("38:16", frm="As Jehovah liveth,")], "38:16", t=(ZEDEKIAH, COLD)),
         S([cp("38:17", to="Then said Jeremiah unto Zedekiah,"), gd("38:17", frm="Thus saith Jehovah,"), gd("38:18")], "38:17-18", t=W3),
         S([cp("38:19", to="And Zedekiah the king said unto Jeremiah,"), say("38:19", frm="I am afraid")], "38:19", t=(ZEDEKIAH, COLD)),
         S([cp("38:20", to="But Jeremiah said,"), say("38:20", frm="They shall not deliver thee."), say("38:21")], "38:20-21", t=C3),
         O("38:22-23", a=("#5A4A5A", lambda w, h: K.women_brought("wb13", w, h, 1310))),
         S([cp("38:24", to="Then said Zedekiah unto Jeremiah,"), say("38:24", frm="Let no man know"), says("38:25-26")], "38:24-26", t=(ZEDEKIAH, COLD), head="Let No Man Know of These Words"),
         O("38:27-28", kind="cap", a=(PIT, lambda w, h: K.court_guard("cg13b", w, h, 1311, age=3)), k=0.3)]


SEGS3 = [O("39:1-2", kind="cap", a=("#5A4A5A", lambda w, h: K.wall_breach(w, h, 1312)), k=0.3, head="A Breach Was Made in the City", stamp=39),
         O("39:3", kind="cap", a=("#4A3A4A", lambda w, h: K.princes_gate("pg13", w, h, 1313)), k=0.3),
         O("39:4", kind="cap", a=("#0E0C1E", lambda w, h: K.flight("fl13", w, h, 1314)), k=0.3, head="By the Way of the King's Garden"),
         O("39:5", kind="cap", a=(MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "RIBLAH", "HAMATH", "DAMASCUS"), hi=("RIBLAH",), arrows=[("JERUSALEM", "RIBLAH")], box=(33.0, 39.0, 30.8, 35.6))),
           k=0.26),
         O("39:6-7", kind="cap", a=("#2A1A2A", lambda w, h: K.riblah(w, h, 1315)), k=0.26),
         O("39:8", kind="cap", a=("#2A0A0A", lambda w, h: K.burning_city(w, h, 1316)), k=0.22, head="They Burned the King's House"),
         O("39:9", kind="cap", a=("#5A4A5A", lambda w, h: K.captives("cp13", w, h, 1317, city="jerusalem")), k=0.26),
         O("39:10", kind="cap", a=("#8FD0E2", lambda w, h: K.poor_vineyards("pv13", w, h, 1318)), k=0.24),
         S([cp("39:11"), say("39:12")], "39:11-12", t=(NEBUZARADAN, GOLDEN), head="Look Well to Him"),
         O("39:13-14", kind="cap", a=("#8A8A9A", lambda w, h: K.released("rl13", w, h, 1319)), k=0.3),
         S([cp("39:15"), gods("39:16-18")], "39:15-18", t=(EBEDMELECH, GOLDEN), head="Thy Life Shall Be for a Prey unto Thee")]
PG.extend(pack(SEGS + SEGS2 + SEGS3, "JER-C13-D", PG.next(), end=end_mark("NEXT · GEDALIAH", "right: 10px; bottom: 34px")))
