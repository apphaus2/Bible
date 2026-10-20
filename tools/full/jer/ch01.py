"""Jeremiah volume, Chapter 1 — The Almond Rod (Jeremiah 1–3). Every verse, word for word from ref/eng-asv.
The words of Jeremiah of Anathoth; before I formed thee in the belly I knew thee — ah, Lord Jehovah! I am a child; his mouth
touched (a shaft of light, the prophet kneeling: God is not drawn); the rod of an almond-tree and the boiling caldron from the
north (drawn as things); the kingdoms of the north at the gates as a map; an iron pillar and brazen walls; then the kindness
of thy youth, the fountain of living waters and the broken cisterns, the noble vine, the wild ass; backsliding Israel and
treacherous Judah; return, O backsliding children."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PENITENT, GOLDEN, COLD, RED, NIGHT

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
W0, G0, S0, A0 = (jer(0, "word"), GOLDEN), (jer(0, "grief"), COLD), (jer(0, "stern"), RED), (jer(0, "afraid"), COLD)
MAP = "#0B1A2E"


@P("JER-C01-00-Title", "Chapter 1 · The Almond Rod", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.almond(760, 780, 101)}</g><rect x="0" y="0" width="760" height="302" fill="#3A3060"></rect>')
    return chapter_title(1, "第一話", "The Almond Rod", "Jeremiah 1 – 3", svg, "#3A3060", v("1:5", to="I knew thee,"), "Jeremiah · Volume Twenty-Four")


CALL = ("#3A3A6A", lambda w, h: K.anathoth_call("ac1", w, h, 102))
SEGS = [S([caps("1:1-3")], "1:1-3", a=CALL, k=0.36, head="The Words of Jeremiah", stamp=1),
        S([cp("1:4"), gd("1:5")], "1:4-5", t=W0),
        S(cut("1:6", "Then said I,", "cap", "say") + cut("1:7", "But Jehovah said unto me,") + [gd("1:8")], "1:6-8", t=A0),
        S(cut("1:9", "and Jehovah said unto me,") + [gd("1:10")], "1:9-10", a=("#3A3A6A", lambda w, h: K.anathoth_call("ac1b", w, h, 103, kneel=True))),
        S([cp("1:11", to="saying,"), gd("1:11", frm="Jeremiah,", to="what seest thou?"), cp("1:11", frm="And I said,", to="And I said,"), say("1:11", frm="I see"),
           *cut("1:12", "Then said Jehovah unto me,")], "1:11-12", a=("#3A3060", lambda w, h: K.almond(w, h, 104)), k=0.48, head="A Rod of an Almond-Tree"),
        S([cp("1:13", to="saying,"), gd("1:13", frm="What seest", to="thou?"), cp("1:13", frm="And I said,", to="And I said,"), say("1:13", frm="I see"),
           *cut("1:14", "Then Jehovah said unto me,")], "1:13-14", a=("#2A1A2A", lambda w, h: K.caldron(w, h, 105)), k=0.46, head="A Boiling Caldron"),
        O("1:15-16", a=(MAP, lambda w, h: K.north_map(w, h)), k=0.42),
        O("1:17-19", a=("#4A3A5A", lambda w, h: K.iron_pillar("ip1", w, h, 106)), k=0.44, head="An Iron Pillar and Brazen Walls")]
PG.extend(pack(SEGS, "JER-C01-D", PG.next()))

WILD = ("#E8A060", lambda w, h: K.wilderness(w, h, 107))
WAYS = (MAP, lambda w, h: K.ways_map(w, h))
SEGS2 = [S([cp("2:1"), gods("2:2-3")], "2:1-3", a=WILD, k=0.42, head="The Kindness of Thy Youth", stamp=2),
         O("2:4-5", t=W0),
         O("2:6-7", a=("#1A1A3A", lambda w, h: K.wilderness(w, h, 108, night_=True))),
         O("2:8-9", t=S0),
         O("2:10-12", t=G0),
         O("2:13", a=("#8FD0E2", lambda w, h: K.cisterns(w, h, 109)), k=0.3, head="Broken Cisterns"),
         O("2:14-16", a=("#3A1A1A", lambda w, h: K.lions_waste(w, h, 110))),
         O("2:17-18", a=WAYS, k=0.36),
         O("2:19", t=S0),
         O("2:20-21", a=("#8FD0E2", lambda w, h: K.vine(w, h, 111)), head="A Noble Vine"),
         O("2:22-23", t=W0),
         O("2:24-25", a=("#E8A060", lambda w, h: K.wild_ass(w, h, 112))),
         O("2:26-27", t=S0),
         O("2:28-29", a=("#5A3A5A", lambda w, h: K.high_hill(w, h, 113))),
         O("2:30-32", t=G0, head="Days without Number"),
         O("2:33-35", t=S0),
         O("2:36-37", a=WAYS, k=0.36)]
PG.extend(pack(SEGS2, "JER-C01-E", PG.next()))

SEGS3 = [O("3:1-2", t=S0, head="Return Again to Me", stamp=3),
         O("3:3-5", a=("#C8A880", lambda w, h: K.bare_heights(w, h, 114))),
         S([cp("3:6", to="in the days of Josiah the king,"), gd("3:6", after="in the days of Josiah the king,"), gd("3:7")], "3:6-7",
           a=(MAP, lambda w, h: K.return_map(w, h, sisters=True)), k=0.44, head="Backsliding Israel and Treacherous Judah"),
         O("3:8-9", t=G0),
         S([gd("3:10"), *cut("3:11", "And Jehovah said unto me,")], "3:10-11", t=W0),
         O("3:12-13", t=W0, head="Return, O Backsliding Children"),
         O("3:14-15", a=(MAP, lambda w, h: K.return_map(w, h)), k=0.34),
         O("3:16", a=("#1A1428", lambda w, h: K.ark_forgotten(w, h, 116)), k=0.36),
         O("3:17-18", a=(MAP, lambda w, h: K.return_map(w, h)), k=0.44),
         O("3:19-20", t=G0),
         S([gd("3:21"), gd("3:22", to="your backslidings.")], "3:21-22", a=("#C8A880", lambda w, h: K.bare_heights(w, h, 115, weeping=True)), k=0.34),
         S([say("3:22", frm="Behold, we are come"), says("3:23-25")], "3:22-25", t=(PENITENT, COLD))]
PG.extend(pack(SEGS3, "JER-C01-F", PG.next(), end=end_mark("NEXT · EVIL FROM THE NORTH", "right: 10px; bottom: 34px")))

