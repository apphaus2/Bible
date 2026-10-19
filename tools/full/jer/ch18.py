"""Jeremiah volume, Chapter 18 — The Hammer of the Whole Earth (Jeremiah 51). Every verse, word for word from ref/asv.
A destroying wind against Babylon, and strangers to winnow her; flee out of the midst of Babylon; a golden cup in Jehovah's
hand; we would have healed Babylon; the kings of the Medes; a standard against her walls; thou that dwellest upon many waters;
he hath made the earth by his power; thou art my battle-axe; O destroying mountain, a burnt mountain; the kingdoms of Ararat,
Minni and Ashkenaz (a map); the posts running and the reeds burned; the threshing-floor; Nebuchadrezzar hath swallowed me up;
the sea is come up upon Babylon; Bel made to bring forth that which he swallowed; my people, go ye out of the midst of her; the
broad walls overthrown and the high gates burned; then Seraiah's book read at the Euphrates and sunk with a stone — thus shall
Babylon sink. Thus far are the words of Jeremiah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art18 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, SERAIAH, PENITENT, GOLDEN, COLD, RED, NIGHT
from jer import ch17 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W3, G3, S3, C3 = (jer(3, "word"), GOLDEN), (jer(3, "grief"), COLD), (jer(3, "stern"), RED), (jer(3, "calm"), GOLDEN)
MAP = "#0B1A2E"
BAB = "#2A1A3A"
EUPH = "#E8A060"


@P("JER-C18-00-Title", "Chapter 18 · The Hammer of the Whole Earth", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.sunk_book("t18", 760, 780, 1801, stage=1)}</g><rect x="0" y="0" width="760" height="302" fill="#E8A060"></rect>')
    return chapter_title(18, "第十八話", "The Hammer of the Whole Earth", "Jeremiah 51", svg, "#8A4A2A", v("51:64", frm="Thus shall Babylon sink,", to="rise again"), "Jeremiah · Volume Twenty-Four")


SEGS = [O("51:1-2", a=(BAB, lambda w, h: K.destroying_wind(w, h, 1802)), head="A Destroying Wind", stamp=51),
        O("51:3-5", t=S3),
        O("51:6-7", a=("#2A0E14", lambda w, h: K.golden_cup(w, h, 1803)), head="A Golden Cup in Jehovah's Hand"),
        O("51:8-10", t=G3),
        O("51:11-12", a=("#14122A", lambda w, h: K.walls_watch("ww18", w, h, 1804))),
        O("51:13-14", a=("#8FB0C8", lambda w, h: K.many_waters(w, h, 1805)), head="Thou That Dwellest upon Many Waters"),
        O("51:15-16", a=("#1A1A3A", lambda w, h: K.heavens_waters(w, h, 1806))),
        O("51:17-19", t=W3),
        O("51:20-22", a=("#3A2A3A", lambda w, h: K.battle_axe(w, h, 1807)), head="Thou Art My Battle-Axe"),
        O("51:23-24", t=S3),
        O("51:25-26", a=("#2A1A1A", lambda w, h: K.burnt_mountain(w, h, 1808)), head="O Destroying Mountain"),
        O("51:27-28", a=(MAP, lambda w, h: K.kingdoms_map(w, h)), k=0.4),
        O("51:29-30", a=("#2A1A3A", lambda w, h: K.babylon(w, h, 1809, burning=True))),
        O("51:31-32", a=("#3A2A3A", lambda w, h: K.posts("po18", w, h, 1810)), head="One Post Shall Run to Meet Another"),
        O("51:33", a=(EUPH, lambda w, h: K.threshing("th18", w, h, 1811)), k=0.3),
        O("51:34-35", kind="say", t=(PENITENT, COLD), head="He Hath Swallowed Me Up"),
        O("51:36-37", a=("#E8A060", lambda w, h: K.ostriches(w, h, 1812))),
        O("51:38-40", t=S3),
        O("51:41-43", a=("#2A3A5A", lambda w, h: K.sea_over(w, h, 1813)), head="How Is Sheshach Taken!"),
        O("51:44", a=("#5A3A4A", lambda w, h: K.bel_shamed(w, h, 1814)), k=0.36),
        O("51:45-46", t=C3, head="My People, Go Ye Out of the Midst of Her"),
        O("51:47-49", t=S3),
        O("51:50-51", kind="say", t=(PENITENT, COLD)),
        O("51:52-53", t=S3),
        O("51:54-56", a=("#2A1A3A", lambda w, h: K.babylon(w, h, 1815, burning=True, broken=True))),
        O("51:57-58", a=("#2A1A3A", lambda w, h: K.babylon(w, h, 1816, dusk=True, broken=True)), head="The Broad Walls of Babylon"),
        O("51:59-60", kind="cap", t=(SERAIAH, GOLDEN), head="Seraiah the Son of Neriah"),
        S([cp("51:61", to="And Jeremiah said to Seraiah,"), say("51:61", frm="When thou comest"), say("51:62")], "51:61-62", a=(EUPH, lambda w, h: K.sunk_book("sb18", w, h, 1817)), k=0.4),
        O("51:63", kind="say", t=C3),
        S([say("51:64", to="and they shall be weary."), cp("51:64", frm="Thus far are the words")], "51:64", a=(EUPH, lambda w, h: K.sunk_book("sb18b", w, h, 1818, stage=1)), k=0.36,
          head="Thus Shall Babylon Sink")]
PG.extend(pack(SEGS, "JER-C18-D", PG.next(), end=end_mark("NEXT · THE FALL OF JERUSALEM", "right: 10px; bottom: 34px")))
