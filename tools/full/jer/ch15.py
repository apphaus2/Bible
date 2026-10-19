"""Jeremiah volume, Chapter 15 — Into Egypt (Jeremiah 43–45). Every verse, word for word from ref/asv.
Thou speakest falsely; Baruch setteth thee on against us; the remnant of Judah carried into Egypt, the prophet and Baruch
among them, unto Tahpanhes; great stones hid in the mortar of the brickwork at the entry of Pharaoh's house, and the royal
pavilion spread over them; the houses of the gods of Egypt burned and the pillars of Beth-shemesh broken (no one drawn); then
the word to all the Jews in Egypt (a map of Migdol, Tahpanhes, Memphis and Pathros); the women and the queen of heaven — we will
not hearken unto thee; the sign of Pharaoh Hophra; and the word to Baruch: seekest thou great things for thyself? seek them not."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art15 as K
from jer.common import (pack, cp, say, gd, says, gods, caps, cut, S, O, jer, JOHANAN, BARUCH, BARUCH_GRIEF, WOMAN, GOLDEN, COLD, RED, NIGHT)
from jer import ch14 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W3, G3, S3, C3 = (jer(3, "word"), GOLDEN), (jer(3, "grief"), COLD), (jer(3, "stern"), RED), (jer(3, "calm"), GOLDEN)
MAP = "#0B1A2E"
DES = "#E8A060"


@P("JER-C15-00-Title", "Chapter 15 · Into Egypt", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.into_egypt("t15", 760, 780, 1501)}</g><rect x="0" y="0" width="760" height="302" fill="#E8A060"></rect>')
    return chapter_title(15, "第十五話", "Into Egypt", "Jeremiah 43 – 45", svg, "#8A4A2A", v("43:7", to="and they came unto Tahpanhes."), "Jeremiah · Volume Twenty-Four")


SEGS = [S([cp("43:1"), cp("43:2", to="saying unto Jeremiah,"), say("43:2", frm="Thou speakest falsely:"), say("43:3")], "43:1-3", t=(JOHANAN, RED), head="Thou Speakest Falsely", stamp=43),
        O("43:4", kind="cap", t=(JOHANAN, RED)),
        O("43:5-7", kind="cap", a=(DES, lambda w, h: K.into_egypt("ie15", w, h, 1502)), head="They Came unto Tahpanhes"),
        S([cp("43:8"), gd("43:9")], "43:8-9", a=(DES, lambda w, h: K.pharaoh_house("ph15", w, h, 1503)), k=0.34, head="Great Stones in the Brickwork"),
        O("43:10", a=(DES, lambda w, h: K.pharaoh_house("ph15b", w, h, 1504, pavilion=True)), k=0.34),
        O("43:11", t=S3),
        O("43:12-13", a=("#2A0A0A", lambda w, h: K.egypt_temples(w, h, 1505))),
        O("44:1", kind="cap", a=(MAP, lambda w, h: K.egypt_map(w, h)), k=0.3, h=340, head="All the Jews That Dwelt in the Land of Egypt", stamp=44),
        O("44:2-4", t=W3),
        O("44:5-6", a=("#2A0A0A", lambda w, h: K.burning_city(w, h, 1506))),
        O("44:7-8", t=S3),
        O("44:9-10", t=G3),
        O("44:11-12", t=S3),
        O("44:13-14", t=S3),
        S([cp("44:15", to="answered Jeremiah, saying,"), says("44:16")], "44:15-16", a=("#1A1430", lambda w, h: K.women_vows("wv15", w, h, 1507)), k=0.42, head="The Queen of Heaven"),
        O("44:17", kind="say", t=(WOMAN, RED)),
        O("44:18-19", kind="say", a=("#1A1430", lambda w, h: K.queen_heaven("qh15", w, h, 1508))),
        S([cp("44:20"), say("44:21")], "44:20-21", t=S3),
        O("44:22-23", kind="say", t=G3),
        S([cp("44:24", to="and to all the women,"), say("44:24", frm="Hear the word"), gd("44:25")], "44:24-25", t=S3),
        O("44:26-27", t=S3),
        O("44:28", t=W3),
        O("44:29-30", a=(MAP, lambda w, h: K.near_east(w, h, ("EGYPT", "NOPH", "BABYLON", "JERUSALEM"), hi=("EGYPT",), arrows=[("BABYLON", "EGYPT")], box=(29.0, 46.0, 25.0, 35.0))),
          k=0.36, head="Pharaoh Hophra"),
        S([caps("45:1"), gd("45:2")], "45:1-2", a=("#2A2028", lambda w, h: K.baruch_weary("bw15", w, h, 1509)), k=0.4, head="O Baruch", stamp=45),
        O("45:3", t=G3),
        O("45:4-5", t=C3)]
PG.extend(pack(SEGS, "JER-C15-D", PG.next(), end=end_mark("NEXT · AGAINST THE NATIONS", "right: 10px; bottom: 34px")))
