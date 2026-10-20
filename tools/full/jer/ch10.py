"""Jeremiah volume, Chapter 10 — A New Covenant (Jeremiah 29–31). Every verse, word for word from ref/eng-asv.
The letter to the captivity — build ye houses, plant gardens, seek the peace of the city (the exiles by a river of Babylon);
after seventy years I will visit you; thoughts of peace, and not of evil; the vile figs; Ahab and Zedekiah (29:21–22 words over
Babylon's wall, no one drawn); Shemaiah's letter read to Jeremiah; then the book of consolation: write all the words in a book;
the time of Jacob's trouble; I will break his yoke; the city builded upon its own hill; I have loved thee with an everlasting
love; the virgin of Israel dancing; a great company returning; Rachel weeping in Ramah; Ephraim as a calf unaccustomed to the
yoke; waymarks; my sleep was sweet; sour grapes; the new covenant written in their heart; the sun, the moon and the sea; and
the measuring line of the city, holy unto Jehovah (a plan)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art10 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PRIEST, GOLDEN, COLD, RED, NIGHT
from jer import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W2, G2, S2, C2 = (jer(2, "word"), GOLDEN), (jer(2, "grief"), COLD), (jer(2, "stern"), RED), (jer(2, "calm"), GOLDEN)
MAP = "#0B1A2E"
LETTER = ("#2A1A2A", lambda w, h: K.letter(w, h, 1002))
DAWN = "#3A3A7A"


@P("JER-C10-00-Title", "Chapter 10 · A New Covenant", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.new_covenant("t10", 760, 780, 1001)}</g><rect x="0" y="0" width="760" height="302" fill="#3A3A7A"></rect>')
    return chapter_title(10, "第十話", "A New Covenant", "Jeremiah 29 – 31", svg, DAWN, v("31:33", frm="I will put my law", to="will I write it;"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([caps("29:1-2")], "29:1-2", a=LETTER, k=0.36, head="The Letter to the Captivity", stamp=29),
        S([cp("29:3"), gd("29:4")], "29:3-4", a=(MAP, lambda w, h: K.near_east(w, h, ("JERUSALEM", "BABYLON"), hi=("BABYLON",), arrows=[("JERUSALEM", "BABYLON")], lit="#FFD23F",
                                                                                  box=(31.5, 47.5, 28.0, 35.4))), k=0.36),
        O("29:5-7", a=("#8FB0C8", lambda w, h: K.exile_home("eh10", w, h, 1003)), head="Build Ye Houses, and Dwell in Them"),
        O("29:8-9", t=S2),
        O("29:10", a=("#1A1430", lambda w, h: K.seventy(w, h, 1004)), k=0.3),
        O("29:11-13", t=C2, head="Thoughts of Peace"),
        O("29:14", a=(MAP, lambda w, h: K.return_map(w, h)), k=0.34),
        O("29:15-17", t=S2),
        O("29:18-19", a=("#8FB0C8", lambda w, h: K.figs(w, h, 1005, bad=True))),
        O("29:20-21", t=S2),
        O("29:22-23", a=("#2A1A3A", lambda w, h: K.babylon(w, h, 1006, dusk=True))),
        S([cp("29:24"), gd("29:25")], "29:24-25", t=W2, head="Shemaiah the Nehelamite"),
        O("29:26-28", a=LETTER),
        S([cp("29:29"), cp("29:30"), gd("29:31")], "29:29-31", a=("#C8A880", lambda w, h: K.reading_letter("rl10", w, h, 1007)), k=0.42),
        O("29:32", t=S2)]


SEGS2 = [S([cp("30:1"), gods("30:2-3")], "30:1-3", a=("#3A2A1E", lambda w, h: K.book_writing(w, h, 1008)), k=0.34, head="Write Thee All the Words in a Book", stamp=30),
         S([cp("30:4"), gods("30:5-7")], "30:4-7", a=("#6A6A7A", lambda w, h: K.trembling("tr10", w, h, 1009)), head="The Time of Jacob's Trouble"),
         O("30:8-9", a=(DAWN, lambda w, h: K.yoke_off(w, h, 1010)), k=0.34),
         O("30:10-11", t=C2),
         O("30:12-15", t=G2, head="Thy Hurt Is Incurable"),
         O("30:16-17", t=W2),
         O("30:18-20", a=("#8FC0E0", lambda w, h: K.city_rebuilt("cr10", w, h, 1011)), head="The City Builded upon Its Own Hill"),
         O("30:21-22", t=C2),
         O("30:23-24", a=("#1A1A2A", lambda w, h: K.tempest(w, h, 1012)), k=0.36)]


SEGS3 = [O("31:1-3", t=C2, head="An Everlasting Love", stamp=31),
         O("31:4-5", a=("#8FC0E0", lambda w, h: K.dancers("dn10", w, h, 1013))),
         O("31:6-7", a=(DAWN, lambda w, h: K.ephraim_watch("ew10", w, h, 1014))),
         O("31:8-9", a=("#8FB0C8", lambda w, h: K.great_company("gc10", w, h, 1015)), head="A Great Company Shall Return"),
         O("31:10-11", a=("#8FB0C8", lambda w, h: K.flock(w, h, 1016, fold=True))),
         O("31:12-14", a=("#8FC0E0", lambda w, h: K.plenty(w, h, 1017))),
         O("31:15-17", a=("#14122A", lambda w, h: K.rachel("rc10", w, h, 1018)), head="Rachel Weeping for Her Children"),
         O("31:18-20", a=("#8FB0C8", lambda w, h: K.calf_yoke(w, h, 1019)), head="Ephraim Bemoaning Himself"),
         O("31:21-22", a=("#8FB0C8", lambda w, h: K.waymarks(w, h, 1020))),
         S([gods("31:23-25"), say("31:26")], "31:23-26", a=(DAWN, lambda w, h: K.sweet_sleep(w, h, 1021))),
         O("31:27-28", a=("#8FB0C8", lambda w, h: K.sower("sw10", w, h, 1022))),
         O("31:29-30", a=("#C8B880", lambda w, h: K.sour_grapes(w, h, 1023)), k=0.4),
         O("31:31-32", a=("#1A1430", lambda w, h: K.covenant_tables(w, h, 1024, broken=True)), k=0.4, head="A New Covenant"),
         O("31:33-34", a=(DAWN, lambda w, h: K.new_covenant("nc10", w, h, 1025))),
         O("31:35-37", a=("#0B0B2A", lambda w, h: K.ordinances(w, h, 1026))),
         O("31:38-40", a=(MAP, lambda w, h: K.measuring_line(w, h)), k=0.54, head="Holy unto Jehovah")]
PG.extend(pack(SEGS + SEGS2 + SEGS3, "JER-C10-D", PG.next(), end=end_mark("NEXT · THE FIELD AT ANATHOTH", "right: 10px; bottom: 34px")))
