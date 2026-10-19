"""Jeremiah volume, Chapter 9 — The Yoke (Jeremiah 26–28). Every verse, word for word from ref/asv.
Stand in the court of Jehovah's house, diminish not a word; this house like Shiloh; the priests and the prophets lay hold on
him — thou shalt surely die; the princes in the entry of the new gate; I am in your hand; the elders remember Micah the
Morashtite (Zion ploughed as a field); Uriah who fled into Egypt (his death words over the graves of the common people);
Ahikam's hand; then the bonds and bars upon his neck, sent to the kings of Edom, Moab, Ammon, Tyre and Sidon (a map); serve
the king of Babylon, and live; the vessels left in the house (Solomon's sea as a blueprint); Hananiah breaks the bar — thou
hast broken the bars of wood, but made in their stead bars of iron; and Hananiah died the same year."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art9 as K
from jer.common import (pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PRIEST, PRINCE_CALM, ELDER, HANANIAH, ZEDEKIAH_CALM, GOLDEN, COLD, RED, NIGHT)
from jer import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W2, G2, S2, C2, A2 = (jer(2, "word"), GOLDEN), (jer(2, "grief"), COLD), (jer(2, "stern"), RED), (jer(2, "calm"), GOLDEN), (jer(2, "afraid"), COLD)
MAP = "#0B1A2E"
COURT = "#C8A880"


@P("JER-C09-00-Title", "Chapter 9 · The Yoke", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.bonds_bars("t9", 760, 780, 901)}</g><rect x="0" y="0" width="760" height="302" fill="#8A8A9A"></rect>')
    return chapter_title(9, "第九話", "The Yoke", "Jeremiah 26 – 28", svg, "#4A4A5A", v("27:2", frm="Make thee bonds and bars,"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([cp("26:1"), gods("26:2-3")], "26:1-3", a=("#8FB0C8", lambda w, h: K.temple_gate("tg9", w, h, 902, age=2)), k=0.4, head="Diminish Not a Word", stamp=26),
        O("26:4-6", t=S2),
        S([cp("26:7"), cp("26:8", to="saying,"), say("26:8", frm="Thou shalt surely die."), say("26:9", to="without inhabitant?"), cp("26:9", frm="And all the people were gathered")],
          "26:7-9", a=(COURT, lambda w, h: K.seized("sz9", w, h, 903)), k=0.44, head="Thou Shalt Surely Die"),
        S([cp("26:10"), cp("26:11", to="saying,"), say("26:11", frm="This man is worthy")], "26:10-11", a=("#8FB0C8", lambda w, h: K.new_gate("ng9", w, h, 904)), k=0.4),
        S([cp("26:12", to="saying,"), say("26:12", frm="Jehovah sent me"), says("26:13-14")], "26:12-14", t=C2, head="I Am in Your Hand"),
        O("26:15", kind="say", t=S2),
        S([cp("26:16", to="unto the priests and to the prophets:"), say("26:16", frm="This man is not worthy")], "26:16", t=(PRINCE_CALM, GOLDEN)),
        S([cp("26:17"), say("26:18", to="saying,"), gd("26:18", frm="Thus saith Jehovah of hosts:")], "26:17-18", a=("#8FB0C8", lambda w, h: K.zion_plowed(w, h, 905)), k=0.4,
          head="Micah the Morashtite"),
        O("26:19", kind="say", t=(ELDER, GOLDEN)),
        O("26:20-22", kind="cap", a=(MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "EGYPT", "NOPH"), hi=("EGYPT",), arrows=[("JERUSALEM", "NOPH")], box=(29.0, 38.5, 26.5, 34.5))), k=0.44,
          head="Uriah the Son of Shemaiah"),
        O("26:23-24", kind="cap", a=("#5A4A5A", lambda w, h: K.common_graves(w, h, 906)), k=0.32)]
PG.extend(pack(SEGS, "JER-C09-D", PG.next()))

SEGS2 = [S([cp("27:1"), *cut("27:2", "Thus saith Jehovah to me:")], "27:1-2", a=("#8A8A9A", lambda w, h: K.bonds_bars("bb9", w, h, 907)), k=0.3, head="Bonds and Bars", stamp=27),
         O("27:3-4", a=(MAP, lambda w, h: K.envoys_map(w, h)), k=0.38),
         O("27:5-7", t=W2),
         O("27:8", t=S2),
         O("27:9-11", t=S2),
         S([cp("27:12", to="saying,"), say("27:12", frm="Bring your necks"), says("27:13")], "27:12-13", t=(ZEDEKIAH_CALM, GOLDEN), head="Serve the King of Babylon, and Live"),
         O("27:14-15", kind="say", t=C2),
         S([cp("27:16", to="saying,"), gd("27:16", frm="Thus saith Jehovah:")], "27:16", t=W2),
         O("27:17-18", kind="say", t=S2),
         O("27:19-20", a=("#0B1A2E", lambda w, h: K.vessels_left(w, h)), k=0.42, head="The Vessels That Are Left"),
         O("27:21-22", a=("#5A3A2A", lambda w, h: K.brass_carried("bc9", w, h, 908)))]
PG.extend(pack(SEGS2, "JER-C09-E", PG.next()))

SEGS3 = [S([cp("28:1"), says("28:2-3")], "28:1-3", t=(HANANIAH, GOLDEN), head="Hananiah the Son of Azzur", stamp=28),
         O("28:4", kind="say", a=(MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "BABYLON"), hi=("BABYLON",), arrows=[("BABYLON", "JERUSALEM")], lit="#FFD23F", box=(31.5, 47.5, 28.0, 35.4))), k=0.36),
         S([cp("28:5"), cp("28:6", to="even the prophet Jeremiah said,"), say("28:6", frm="Amen:")], "28:5-6", t=C2),
         O("28:7-9", kind="say", t=S2),
         S([cp("28:10"), cp("28:11", to="saying,"), say("28:11", frm="Thus saith Jehovah:", to="all the nations."), cp("28:11", frm="And the prophet Jeremiah went his way.")],
           "28:10-11", a=(COURT, lambda w, h: K.bar_broken("br9", w, h, 909)), k=0.42, head="Hananiah Brake the Bar"),
         S([cp("28:12"), gods("28:13-14")], "28:12-14", a=("#1A1820", lambda w, h: K.yoke_iron(w, h, 910)), k=0.4, head="Bars of Iron"),
         S([cp("28:15", to="unto Hananiah the prophet,"), say("28:15", frm="Hear now,"), gd("28:16"), cp("28:17")], "28:15-17", t=S2)]
PG.extend(pack(SEGS3, "JER-C09-F", PG.next(), end=end_mark("NEXT · A NEW COVENANT", "right: 10px; bottom: 34px")))
