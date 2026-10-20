"""Jeremiah volume, Chapter 11 — The Field at Anathoth (Jeremiah 32–33). Every verse, word for word from ref/eng-asv.
In the tenth year of Zedekiah, the city besieged and the prophet shut up in the court of the guard; Hanamel comes — buy thee my
field that is in Anathoth; seventeen shekels weighed, the deed sealed and open, put in an earthen vessel; houses and fields and
vineyards shall yet again be bought; ah Lord Jehovah, there is nothing too hard for thee; is there anything too hard for me?;
the city given to the Chaldeans and burned (words over the walls and the fire); the everlasting covenant; fields bought again;
then call unto me, and I will answer thee; health and cure; the voice of the bridegroom and the bride; the flocks passing under
the hand of him that numbereth them; the Branch of righteousness; the covenant of the day and of the night."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art11 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, ZEDEKIAH, BARUCH, GOLDEN, COLD, RED, NIGHT
from jer import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W2, G2, S2, C2 = (jer(2, "word"), GOLDEN), (jer(2, "grief"), COLD), (jer(2, "stern"), RED), (jer(2, "calm"), GOLDEN)
COURT = ("#6A5A6A", lambda w, h: K.court_guard("cg11", w, h, 1102))
FIELD = "#8FB0C8"


@P("JER-C11-00-Title", "Chapter 11 · The Field at Anathoth", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.field_anathoth("t11", 760, 780, 1101)}</g><rect x="0" y="0" width="760" height="302" fill="#8FB0C8"></rect>')
    return chapter_title(11, "第十一話", "The Field at Anathoth", "Jeremiah 32 – 33", svg, "#3A5A6A", v("32:15", frm="Houses and fields"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([caps("32:1-2")], "32:1-2", a=COURT, k=0.3, head="Shut Up in the Court of the Guard", stamp=32),
        S([cp("32:3", to="saying,"), say("32:3", frm="Wherefore dost thou prophesy,")], "32:3", t=(ZEDEKIAH, COLD)),
        O("32:4-5", kind="say", t=(ZEDEKIAH, COLD)),
        S([cp("32:6", to="And Jeremiah said,"), say("32:6", frm="The word of Jehovah"), gd("32:7")], "32:6-7", t=C2, head="Buy Thee My Field"),
        S([cp("32:8", to="and said unto me,"), say("32:8", frm="Buy my field,", to="buy it for thyself."), cp("32:8", frm="Then I knew")], "32:8",
          a=("#6A5A6A", lambda w, h: K.court_guard("cg11b", w, h, 1103, visitor=True)), k=0.32),
        O("32:9-11", kind="cap", a=("#3A2A22", lambda w, h: K.deeds(w, h, 1104)), k=0.3, head="Seventeen Shekels of Silver"),
        S([cp("32:12"), cp("32:13")], "32:12-13", t=(BARUCH, GOLDEN)),
        O("32:14-15", a=("#3A2A22", lambda w, h: K.deeds(w, h, 1105, vessel=True)), k=0.3),
        S([cp("32:16"), say("32:17")], "32:16-17", a=("#2A2A5A", lambda w, h: K.prayer("pr11", w, h, 1106)), k=0.34, head="There Is Nothing Too Hard for Thee"),
        O("32:18-19", kind="say", t=C2),
        O("32:20-21", kind="say", a=("#0B2E4A", lambda w, h: K.egypt_wonders(w, h, 1107))),
        O("32:22-23", kind="say", a=("#8FC0E0", lambda w, h: K.milk_honey(w, h, 1108))),
        O("32:24-25", kind="say", a=("#4A3A4A", lambda w, h: K.mound("md11", w, h, 1109))),
        S([cp("32:26"), gods("32:27-28")], "32:26-28", t=W2, head="Is There Anything Too Hard for Me?"),
        O("32:29", a=("#2A0A0A", lambda w, h: K.burning_city(w, h, 1110)), k=0.3),
        O("32:30-31", t=S2),
        O("32:32-33", t=S2),
        O("32:34-35", a=("#1A0A12", lambda w, h: K.topheth(w, h, 1111))),
        O("32:36-37", a=(NIGHT, lambda w, h: K.return_map(w, h)), k=0.4),
        O("32:38-41", t=C2, head="An Everlasting Covenant"),
        O("32:42-43", t=W2),
        O("32:44", a=(FIELD, lambda w, h: K.field_anathoth("fa11", w, h, 1112, buyers=True)), k=0.3)]
PG.extend(pack(SEGS, "JER-C11-D", PG.next()))

SEGS2 = [S([cp("33:1"), gods("33:2-3")], "33:1-3", a=("#0F0E2A", lambda w, h: K.call_night(w, h, 1113)), k=0.4, head="Call unto Me", stamp=33),
         O("33:4-5", a=("#5A4A5A", lambda w, h: K.jackal_heaps(w, h, 1114))),
         O("33:6-8", t=C2),
         O("33:9", t=W2),
         O("33:10", a=("#3A2A4A", lambda w, h: K.empty_city(w, h, 1115, dusk=True)), k=0.38, head="The Voice of the Bridegroom"),
         O("33:11", a=("#8FC0E0", lambda w, h: K.city_rebuilt("cr11", w, h, 1116)), k=0.42),
         O("33:12-13", a=(FIELD, lambda w, h: K.numbering("nb11", w, h, 1117)), head="Under the Hands of Him That Numbereth"),
         O("33:14-16", a=("#3A3A7A", lambda w, h: K.branch(w, h, 1118)), head="A Branch of Righteousness"),
         O("33:17-18", a=("#5A4A6A", lambda w, h: K.levites("lv11", w, h, 1119))),
         S([cp("33:19"), gods("33:20-21")], "33:19-21", a=("#0B0B2A", lambda w, h: K.ordinances(w, h, 1120)), head="My Covenant of the Day and of the Night"),
         O("33:22", a=("#0B0B2A", lambda w, h: K.stars_sand(w, h, 1121)), k=0.3),
         S([cp("33:23"), gd("33:24")], "33:23-24", t=S2),
         O("33:25-26", t=C2)]
PG.extend(pack(SEGS2, "JER-C11-E", PG.next(), end=end_mark("NEXT · THE ROLL", "right: 10px; bottom: 34px")))
