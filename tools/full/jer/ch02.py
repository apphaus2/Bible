"""Jeremiah volume, Chapter 2 — Evil from the North (Jeremiah 4–6). Every verse, word for word from ref/asv.
Break up your fallow ground; blow ye the trumpet in the land (a watchman on the wall, a standard toward Zion); a lion gone up
from his thicket; chariots as the whirlwind; my anguish, my anguish! (the prophet's own words in speech boxes); waste and
void — the earth without light, no man, no bird; the daughter of Zion spreading her hands; run to and fro through the streets
of Jerusalem (one man in an empty street); the sand the bound of the sea; the fowler's cage; the mound cast up against the
wall; peace, peace, when there is no peace; the old paths; a people from the north country; the refiner's furnace."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, PEOPLE, GOLDEN, COLD, RED, NIGHT
from jer import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W0, G0, S0, A0 = (jer(0, "word"), GOLDEN), (jer(0, "grief"), COLD), (jer(0, "stern"), RED), (jer(0, "afraid"), COLD)


@P("JER-C02-00-Title", "Chapter 2 · Evil from the North", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.trumpet_walls("t2", 760, 780, 201, dusk=True)}</g><rect x="0" y="0" width="760" height="302" fill="#5A3A5A"></rect>')
    return chapter_title(2, "第二話", "Evil from the North", "Jeremiah 4 – 6", svg, "#5A3A5A", v("4:6", frm="for I will bring evil"), "Jeremiah · Volume Twenty-Four")


SEGS = [O("4:1-2", t=W0, head="If Thou Wilt Return", stamp=4),
        O("4:3-4", a=("#8FB0C8", lambda w, h: K.fallow(w, h, 202))),
        O("4:5-6", a=("#8FB0C8", lambda w, h: K.trumpet_walls("tw2", w, h, 203)), k=0.4, head="Blow Ye the Trumpet"),
        O("4:7-8", a=("#C8703A", lambda w, h: K.lion_thicket(w, h, 204))),
        S([gd("4:9"), *cut("4:10", "Then said I,", "cap", "say")], "4:9-10", t=A0),
        O("4:11-13", a=("#3A3A4A", lambda w, h: K.whirlwind_chariots(w, h, 205))),
        O("4:14-16", t=S0),
        O("4:17-18", a=("#2A1A3A", lambda w, h: K.tents_round(w, h, 206))),
        S([says("4:19-21"), gd("4:22")], "4:19-22", t=G0, head="My Anguish, My Anguish!"),
        O("4:23-26", kind="say", a=("#0A0A10", lambda w, h: K.waste_void(w, h, 207)), k=0.44, head="Waste and Void"),
        O("4:27-28", t=S0),
        O("4:29-30", a=("#8A8A9A", lambda w, h: K.empty_city(w, h, 208))),
        O("4:31", a=("#3A2A4A", lambda w, h: K.daughter_zion("dz2", w, h, 209)), k=0.36)]
PG.extend(pack(SEGS, "JER-C02-D", PG.next()))

SEGS2 = [O("5:1-2", a=("#8A8A9A", lambda w, h: K.streets_search("ss2", w, h, 210)), k=0.36, head="Run Ye to and Fro", stamp=5),
         S([say("5:3"), *cut("5:4", "Then I said,", "cap", "say"), say("5:5")], "5:3-5", t=G0),
         O("5:6", a=("#2A1A3A", lambda w, h: K.beasts(w, h, 211)), k=0.34),
         O("5:7-9", t=S0),
         O("5:10-13", t=W0),
         O("5:14", a=("#1A0A0A", lambda w, h: K.fire_wood(w, h, 212)), k=0.3, head="My Words in Thy Mouth Fire"),
         O("5:15-16", a=("#4A3A4A", lambda w, h: K.north_host("nh2", w, h, 213)), k=0.34),
         O("5:17-18", t=S0),
         O("5:19", t=W0),
         O("5:20-22", a=("#3A4A6A", lambda w, h: K.sea_bound(w, h, 214)), head="The Sand for the Bound of the Sea"),
         O("5:23-25", a=("#5A6A8A", lambda w, h: K.rain_field(w, h, 215))),
         O("5:26-28", a=("#5A4A3A", lambda w, h: K.fowler(w, h, 216))),
         O("5:29-31", t=S0)]
PG.extend(pack(SEGS2, "JER-C02-E", PG.next()))

SEGS3 = [O("6:1-3", a=("#2A1A3A", lambda w, h: K.tekoa_signal(w, h, 217)), head="Flee for Safety", stamp=6),
         O("6:4-5", a=("#2A1A3A", lambda w, h: K.tents_round(w, h, 218)), k=0.3),
         O("6:6-8", a=("#4A3A4A", lambda w, h: K.mound("md2", w, h, 219))),
         O("6:9", a=("#8FD0E2", lambda w, h: K.glean_vine("gv2", w, h, 220)), k=0.3),
         S([say("6:10"), say("6:11", to="I am weary with holding in:"), gd("6:11", after="I am weary with holding in:")], "6:10-11", t=G0),
         O("6:12-13", t=S0),
         O("6:14-15", t=W0, head="Peace, Peace"),
         O("6:16-17", a=("#8FB0C8", lambda w, h: K.old_paths("op2", w, h, 221)), head="Ask for the Old Paths"),
         O("6:18-19", t=S0),
         O("6:20-21", a=("#FFB04A", lambda w, h: K.sheba_train("sb2", w, h, 222))),
         O("6:22-23", a=("#4A3A4A", lambda w, h: K.north_host("nh2b", w, h, 223)), head="A People from the North Country"),
         S([says("6:24-26")], "6:24-26", a=("#3A3A4A", lambda w, h: K.ashes("as2", w, h, 224))),
         O("6:27-30", a=("#1A1012", lambda w, h: K.refiner(w, h, 225)), head="A Trier among My People")]
PG.extend(pack(SEGS3, "JER-C02-F", PG.next(), end=end_mark("NEXT · THE TEMPLE OF JEHOVAH", "right: 10px; bottom: 34px")))
