"""Isaiah volume, Chapter 10 — On Whom Dost Thou Trust? (Isaiah 36–39). Every verse, word for word from ref/asv.
The story of Hezekiah and Sennacherib, drawn as in 2 Kings (kg2.art, kg2.common): Rabshakeh at the conduit of the upper pool
— on whom dost thou trust?; the cry in the Jews' language to the men on the wall; Hezekiah in sackcloth and Isaiah's answer;
the letter spread before Jehovah and his prayer; the virgin daughter of Zion hath despised thee (the Voice box over Lebanon,
the empty throne in light, the vine and the fig-tree); the angel of Jehovah in the camp of the Assyrians (37:36 words over
the silent camp) and Sennacherib at Nineveh (37:38 words only); Hezekiah sick unto death, the shadow returned ten steps on
the dial of Ahaz, and the writing of Hezekiah as song lines; the envoys of Babylon and the word that all shall be carried
to Babylon."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art10 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, HEZEKIAH, HEZEKIAH_GRIEF, HEZEKIAH_SICK, HEZEKIAH_JOY, RABSHAKEH, ELIAKIM, MESSENGER,
                        COLD, GOLDEN, RED)
from isa import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTC = "#14123A"
MAP = "#0B1A2E"
POOL = "#C8B8A0"


@P("ISA-C10-00-Title", "Chapter 10 · On Whom Dost Thou Trust?", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#C8B8A0"></rect><g transform="translate(0 320)">{K.upper_pool("t10", 760, 760, 1001)}</g>')
    return chapter_title(10, "第十話", "On Whom Dost Thou Trust?", "Isaiah 36 – 39", svg, "#8A5A1A", v("36:5", frm="now on whom dost thou trust,"), "Isaiah · Volume Twenty-Three")


SEGS = [drawn([caps("36:1")], "ISA 36:1", A(lambda w, h: K.assyria_map(w, h, arrows=(("NINEVEH", "SAMARIA"),)), MAP), None, head="Sennacherib King of Assyria", stamp=36),
        drawn([caps("36:2-3")], "ISA 36:2–3", A(lambda w, h: K.upper_pool("up10", w, h, 1002), POOL), None, head="Rabshakeh"),
        face([cp("36:4", to="And Rabshakeh said unto them,"), say("36:4", frm="Say ye now"), says("36:5-6")], "ISA 36:4–6", RABSHAKEH),
        face([says("36:7-10")], "ISA 36:7–10", RABSHAKEH),
        face([cp("36:11", to="unto Rabshakeh,"), say("36:11", frm="Speak, I pray thee")], "ISA 36:11", ELIAKIM),
        face([cp("36:12", to="But Rabshakeh said,"), say("36:12", frm="Hath my master")], "ISA 36:12", RABSHAKEH),
        drawn([cp("36:13", to="and said,"), say("36:13", frm="Hear ye the words"), says("36:14-15")], "ISA 36:13–15", A(lambda w, h: K.upper_pool("up10b", w, h, 1003), POOL), None,
              head="In the Jews' Language"),
        face([says("36:16-17")], "ISA 36:16–17", RABSHAKEH),
        face([says("36:18-20")], "ISA 36:18–20", RABSHAKEH),
        drawn([caps("36:21-22")], "ISA 36:21–22", A(lambda w, h: K.upper_pool("up10c", w, h, 1004), POOL), None),
        face([caps("37:1-2")], "ISA 37:1–2", HEZEKIAH_GRIEF, head="Isaiah the Prophet", stamp=37),
        face([cp("37:3", to="And they said unto him,"), say("37:3", frm="Thus saith Hezekiah,"), says("37:4")], "ISA 37:3–4", ELIAKIM),
        face([caps("37:5"), cp("37:6", to="And Isaiah said unto them,"), say("37:6", frm="Thus shall ye say", to="Thus saith Jehovah,"), gd("37:6", frm="Be not afraid"), gods("37:7")], "ISA 37:5–7", ISAIAH),
        drawn([caps("37:8-9")], "ISA 37:8–9", A(lambda w, h: K.nations_map(w, h, hi=("ETHIOPIA",), show=["ETHIOPIA", "EGYPT", "JERUSALEM", "PHILISTIA", "NINEVEH", "DAMASCUS"]), MAP), None),
        face([says("37:10-13")], "ISA 37:10–13", MESSENGER, bg=RED),
        drawn([caps("37:14-15"), says("37:16")], "ISA 37:14–16", A(lambda w, h: K.letter_spread("ls10", w, h, 1005), "#3A2A1A"), None, head="Hezekiah Prayed unto Jehovah"),
        face([says("37:17-20")], "ISA 37:17–20", HEZEKIAH_GRIEF),
        face([cp("37:21", to="saying,"), say("37:21", frm="Thus saith Jehovah,", to="the God of Israel,"), gd("37:21", frm="Whereas"), say("37:22", to="concerning him:"), gd("37:22", frm="The virgin daughter"), gods("37:23")],
             "ISA 37:21–23", ISAIAH, bg=NIGHTC, head="The Virgin Daughter of Zion"),
        drawn([gods("37:24-25")], "ISA 37:24–25", A(lambda w, h: K.lebanon("lb10", w, h, 1006), "#8FD0E2"), None),
        drawn([gods("37:26-29")], "ISA 37:26–29", lambda w, h: K.K2.throne_glory(w, h, 1007), NIGHTC, full=True),
        drawn([gods("37:30-32")], "ISA 37:30–32", A(lambda w, h: K.vine_fig("vf10", w, h, 1008), "#8FD0E2"), None),
        drawn([cp("37:33", to="concerning the king of Assyria,"), gd("37:33", frm="He shall not come"), gods("37:34-35")], "ISA 37:33–35", A(lambda w, h: K.upper_pool("up10d", w, h, 1009, wall_people=True), POOL), None),
        drawn([caps("37:36-37")], "ISA 37:36–37", lambda w, h: K.silent_camp("sc10", w, h, 1010), "#8A8AA8", full=True, head="The Camp of the Assyrians"),
        drawn([caps("37:38")], "ISA 37:38", A(lambda w, h: K.nineveh(w, h, 1011), "#3A2A2A"), None),
        drawn([cp("38:1", to="and said unto him,"), say("38:1", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("38:1", frm="Set thy house")], "ISA 38:1",
              A(lambda w, h: K.hezekiah_bed("hb10", w, h, 1012), "#5A3A2A"), None, head="Sick unto Death", stamp=38),
        face([caps("38:2"), cp("38:3", to="and said,"), say("38:3", frm="Remember now", to="in thy sight."), cp("38:3", frm="And Hezekiah wept sore.")], "ISA 38:2–3", HEZEKIAH_SICK),
        face([caps("38:4"), gods("38:5-6")], "ISA 38:4–6", ISAIAH),
        drawn([gods("38:7"), gd("38:8", to="to return backward ten steps."), cp("38:8", frm="So the sun returned")], "ISA 38:7–8", A(lambda w, h: K.dial(w, h, back=True), MAP), None, head="The Shadow on the Dial")]
SEGS += (S("38:9-14", "song", [HEZEKIAH_SICK], kinds={9: "cap"}, at={12: A(lambda w, h: K.loom_tent(w, h, 1013), "#5A4A6A"),
                                                                                                                                       14: A(lambda w, h: K.swallow_crane(w, h, 1014), "#3A3A6A")}, head="The Writing of Hezekiah")
         + S("38:15-20", "song", [HEZEKIAH_SICK, HEZEKIAH_JOY], split=[17]))
SEGS += [drawn([cp("38:21", to="Now Isaiah had said,"), say("38:21", frm="Let them take"), cp("38:22", to="Hezekiah also had said,"), say("38:22", frm="What is the sign")], "ISA 38:21–22",
               A(lambda w, h: K.fig_cake(w, h, 1015), "#3A2A2A"), None),
         drawn([caps("39:1-2")], "ISA 39:1–2", A(lambda w, h: K.treasures("tr10", w, h, 1016), "#5A2A1E"), None, head="The Envoys of Babylon", stamp=39),
         drawn([cp("39:3", to="and said unto him,"), say("39:3", frm="What said these men?", to="unto thee?"), cp("39:3", frm="And Hezekiah said,", to="Hezekiah said,"), say("39:3", frm="They are come"),
                cp("39:4", to="Then said he,"), say("39:4", frm="What have they seen", to="in thy house?"), cp("39:4", frm="And Hezekiah answered,", to="Hezekiah answered,"), say("39:4", frm="All that is in my house")],
               "ISA 39:3–4", A(lambda w, h: K.treasures("tr10b", w, h, 1017), "#5A2A1E"), None),
         face([cp("39:5", to="Then said Isaiah to Hezekiah,"), say("39:5", frm="Hear the word"), gods("39:6-7")], "ISA 39:5–7", ISAIAH_STERN),
         face([cp("39:8", to="Then said Hezekiah unto Isaiah,"), say("39:8", frm="Good is the word", to="hast spoken."), cp("39:8", frm="He said moreover,", to="He said moreover,"), say("39:8", frm="For there shall be peace")],
              "ISA 39:8", HEZEKIAH)]
PG.extend(pack(SEGS, "ISA-C10-D", PG.next(), end=end_mark("NEXT · COMFORT YE MY PEOPLE", "right: 10px; bottom: 34px")))
