"""2 Kings volume, Chapter 10 — Hezekiah (2 Kings 18–19). Every verse, word for word from ref/asv.
Hezekiah who trusted in Jehovah, and the brazen serpent broken in pieces; Samaria's fall recalled; Sennacherib at Lachish and
the silver and gold sent; Rabshakeh at the conduit of the upper pool — what confidence is this?; speak in the Syrian
language; the cry in the Jews' language to the men on the wall; Hezekiah in sackcloth and Isaiah's answer; the letter spread
before Jehovah and his prayer; the word against Sennacherib — the virgin daughter of Zion hath despised thee (the Voice box);
the angel of Jehovah in the camp of the Assyrians (19:35 words over the silent camp); and Sennacherib at Nineveh (19:37
words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, HEZEKIAH, HEZEKIAH_GRIEF, RABSHAKEH, ELIAKIM, ISAIAH, MESSENGER, RED, COLD, GOLDEN)
from kg2 import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"
MAP = "#0B1A2E"


@P("2KI-C10-00-Title", "Chapter 10 · Hezekiah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#C8B8A0"></rect><g transform="translate(0 320)">{K.upper_pool("t10", 760, 760, 1001)}</g>')
    return chapter_title(10, "第十話", "Hezekiah", "2 Kings 18 – 19", svg, "#8A5A1A", v("18:5", to="the God of Israel;"), "2 Kings · Volume Twelve")


SEGS = [face([caps("18:1-3")], "2KGS 18:1–3", HEZEKIAH, head="He Trusted in Jehovah", stamp=18),
        drawn([caps("18:4-6")], "2KGS 18:4–6", below(lambda w, h: K.brazen_serpent(w, h, 1002), 0.36), "#5A3A3A"),
        drawn([caps("18:7-8")], "2KGS 18:7–8", lambda w, h: K.assyria_map(w, h), MAP),
        drawn([caps("18:9-12")], "2KGS 18:9–12", below(lambda w, h: K.exile_map(w, h), 0.4), MAP),
        drawn([caps("18:13"), cp("18:14", to="saying,"), say("18:14", frm="I have offended;", to="will I bear."), cp("18:14", frm="And the king of Assyria appointed"), caps("18:15-16")],
              "2KGS 18:13–16", below(lambda w, h: K.K2.vessels(w, h, 1003), 0.44), "#2A1A3A", head="Sennacherib"),
        drawn([caps("18:17-18")], "2KGS 18:17–18", below(lambda w, h: K.upper_pool("up10", w, h, 1004), 0.28), "#C8B8A0", head="Rabshakeh"),
        face([cp("18:19", to="said unto them,"), joined("say", ("18:19", "Say ye now"), "18:20", "18:21")], "2KGS 18:19–21", RABSHAKEH, bg=RED),
        face([says("18:22-25")], "2KGS 18:22–25", RABSHAKEH, bg=RED),
        face([cp("18:26", to="unto Rabshakeh,"), say("18:26", frm="Speak,")], "2KGS 18:26", ELIAKIM),
        face([cp("18:27", to="said unto them,"), say("18:27", frm="Hath my master")], "2KGS 18:27", RABSHAKEH, bg=RED),
        drawn([cp("18:28", to="and spake, saying,"), joined("say", ("18:28", "Hear ye"), "18:29", "18:30")], "2KGS 18:28–30", below(lambda w, h: K.upper_pool("up10b", w, h, 1005), 0.46), "#C8B8A0",
              head="In the Jews' Language"),
        face([joined("say", "18:31", "18:32")], "2KGS 18:31–32", RABSHAKEH, bg=RED),
        face([says("18:33-35")], "2KGS 18:33–35", RABSHAKEH, bg=RED),
        drawn([caps("18:36-37")], "2KGS 18:36–37", below(lambda w, h: K.upper_pool("up10c", w, h, 1006), 0.26), "#C8B8A0"),
        face([caps("19:1-2"), cp("19:3", to="And they said unto him,"), joined("say", ("19:3", "Thus saith Hezekiah,"), "19:4")], "2KGS 19:1–4", HEZEKIAH_GRIEF, bg=COLD, head="Isaiah the Prophet", stamp=19),
        face([caps("19:5"), cp("19:6", to="And Isaiah said unto them,"), say("19:6", frm="Thus shall ye say", to="Thus saith Jehovah,"), gd("19:6", frm="Be not afraid"), gods("19:7")], "2KGS 19:5–7", ISAIAH),
        face([caps("19:8"), cp("19:9", to="saying,"), joined("say", "19:10", "19:11", "19:12", "19:13")], "2KGS 19:8–13", MESSENGER, bg=RED),
        drawn([caps("19:14"), cp("19:15", to="and said,"), say("19:15", frm="O Jehovah,"), says("19:16")], "2KGS 19:14–16", below(lambda w, h: K.letter_spread("ls10", w, h, 1007), 0.5), "#3A2A1A",
              head="The Letter Spread before Jehovah"),
        face([says("19:17-19")], "2KGS 19:17–19", HEZEKIAH_GRIEF, bg=COLD),
        face([cp("19:20", to="saying,"), say("19:20", frm="Thus saith Jehovah,", to="the God of Israel,"), gd("19:20", frm="Whereas"), say("19:21", to="concerning him:"), gd("19:21", frm="The virgin daughter")],
             "2KGS 19:20–21", ISAIAH, bg=NIGHT, head="The Virgin Daughter of Zion"),
        drawn([gods("19:22-24")], "2KGS 19:22–24", lambda w, h: K.lebanon("lb10", w, h, 1008), "#8FD0E2"),
        drawn([gods("19:25-28")], "2KGS 19:25–28", lambda w, h: K.K2.throne_glory(w, h, 1009), "#14123A"),
        drawn([gods("19:29-31")], "2KGS 19:29–31", below(lambda w, h: K.vine_fig("vf10", w, h, 1010), 0.42), "#8FD0E2"),
        drawn([say("19:32", to="concerning the king of Assyria,"), gd("19:32", frm="He shall not come"), gods("19:33-34")], "2KGS 19:32–34", below(lambda w, h: K.upper_pool("up10d", w, h, 1011, wall_people=True), 0.4),
              "#C8B8A0"),
        drawn([caps("19:35-36")], "2KGS 19:35–36", lambda w, h: K.silent_camp("sc10", w, h, 1012), "#8A8AA8", head="That Night"),
        drawn([caps("19:37")], "2KGS 19:37", lambda w, h: K.nineveh(w, h, 1013), "#3A2A2A")]
PG.extend(pack(SEGS, "2KI-C10-D", PG.next(), end=end_mark("NEXT · THE SHADOW ON THE DIAL", "right: 10px; bottom: 34px")))
