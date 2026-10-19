"""2 Chronicles volume, Chapter 2 — The Glory Filled the House (2 Chronicles 5–7). Every verse, word for word from ref/asv.
The dedicated things brought in; the ark into the oracle under the wings of the cherubim; the singers and a hundred and
twenty priests sounding as one — for he is good; and the house filled with a cloud; Solomon's blessing from the brazen
scaffold and his prayer, every petition in full; then the fire came down from heaven, and the glory of Jehovah filled the
house; the feast of seven days; and Jehovah's answer by night — if my people, who are called by my name, shall humble
themselves (God's words in the Voice box)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import pack, cp, say, gd, says, gods, caps, drawn, face, joined, SOLOMON, SOLOMON_WISE, COLD, GOLDEN
from chr2 import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK, NIGHT = "#0B1A2E", "#0F0E2A"
PRAY = lambda seed: below(lambda w, h: K.court_scene("pr%d" % seed, w, h, seed, solomon="pray"), 0.5)


@P("2CH-C02-00-Title", "Chapter 2 · The Glory Filled the House", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.court_scene("t2", 760, 820, 201, cloud=True, crowd=False)}</g><rect x="0" y="0" width="760" height="262" fill="#E8E2D6"></rect>')
    return chapter_title(2, "第二話", "The Glory Filled the House", "2 Chronicles 5 – 7", svg, "#8A7A5A", v("5:14", frm="for the glory"), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("5:1")], "2CHR 5:1", below(lambda w, h: K.gold_vessels(w, h), 0.4), INK, head="The Ark into Its Place", stamp=5),
        drawn([caps("5:2-3")], "2CHR 5:2–3", below(lambda w, h: K.court_scene("cs2", w, h, 202), 0.3), "#8FD0E2"),
        drawn([caps("5:4-6")], "2CHR 5:4–6", below(lambda w, h: K.ark_up("au2", w, h, 203), 0.36), "#FFE680"),
        drawn([caps("5:7-10")], "2CHR 5:7–10", below(lambda w, h: K.ark_oracle(w, h), 0.4), INK),
        drawn([caps("5:11-12")], "2CHR 5:11–12", below(lambda w, h: K.singers("sg2", w, h, 204, n=8, top=0.5), 0.4), "#FFB04A", head="As One"),
        drawn([cp("5:13", to="saying,"), say("5:13", frm="For he is good;", to="endureth for ever;"), cp("5:13", frm="that then the house"), caps("5:14")], "2CHR 5:13–14",
              lambda w, h: K.court_scene("cl2", w, h, 205, cloud=True, crowd=False), "#E8E2D6")]
PG.extend(pack(SEGS, "2CH-C02-D", PG.next()))
SEGS2 = [face([cp("6:1", to="Then spake Solomon,"), joined("say", ("6:1", "Jehovah hath said"), "6:2")], "2CHR 6:1–2", SOLOMON_WISE, head="Blessed Be Jehovah", stamp=6),
         drawn([caps("6:3"), cp("6:4", to="And he said,"), joined("say", ("6:4", "Blessed be Jehovah,"), "6:5", "6:6")], "2CHR 6:3–6",
               below(lambda w, h: K.court_scene("bl2", w, h, 206, solomon="bless"), 0.5), "#8FD0E2"),
         face([says("6:7-9")], "2CHR 6:7–9", SOLOMON),
         face([says("6:10-11")], "2CHR 6:10–11", SOLOMON),
         drawn([caps("6:12-13")], "2CHR 6:12–13", PRAY(207), "#8FD0E2", head="The Brazen Scaffold"),
         face([cp("6:14", to="and he said,"), joined("say", ("6:14", "O Jehovah,"), "6:15")], "2CHR 6:14–15", SOLOMON_WISE),
         face([says("6:16-17")], "2CHR 6:16–17", SOLOMON_WISE),
         face([says("6:18-19")], "2CHR 6:18–19", SOLOMON_WISE, bg=COLD, head="Will God in Very Deed Dwell with Men?"),
         face([says("6:20-21")], "2CHR 6:20–21", SOLOMON_WISE),
         face([says("6:22-23")], "2CHR 6:22–23", SOLOMON_WISE, bg=COLD),
         face([says("6:24-25")], "2CHR 6:24–25", SOLOMON_WISE),
         face([says("6:26-27")], "2CHR 6:26–27", SOLOMON_WISE, bg=COLD),
         face([says("6:28-31")], "2CHR 6:28–31", SOLOMON_WISE),
         face([says("6:32-33")], "2CHR 6:32–33", SOLOMON_WISE, head="The Foreigner"),
         face([says("6:34-35")], "2CHR 6:34–35", SOLOMON_WISE, bg=COLD),
         face([says("6:36-37")], "2CHR 6:36–37", SOLOMON_WISE),
         face([says("6:38-39")], "2CHR 6:38–39", SOLOMON_WISE, bg=COLD),
         drawn([says("6:40-42")], "2CHR 6:40–42", PRAY(208), "#8FD0E2", head="Arise, O Jehovah God")]
PG.extend(pack(SEGS2, "2CH-C02-E", PG.next()))
SEGS3 = [drawn([caps("7:1-2")], "2CHR 7:1–2", lambda w, h: K.court_scene("fr2", w, h, 209, cloud=True, smoke=True), "#E8E2D6", head="The Fire Came Down from Heaven", stamp=7),
         drawn([cp("7:3", to="saying,"), say("7:3", frm="For he is good;")], "2CHR 7:3", below(lambda w, h: K.court_scene("bw2", w, h, 210, smoke=True), 0.24), "#8FD0E2"),
         drawn([caps("7:4-6")], "2CHR 7:4–6", below(lambda w, h: K.singers("sg2b", w, h, 211, n=8, top=0.5), 0.5), "#FFB04A"),
         drawn([caps("7:7")], "2CHR 7:7", below(lambda w, h: K.court_scene("sm2", w, h, 212, smoke=True), 0.3), "#8FD0E2"),
         drawn([caps("7:8-10")], "2CHR 7:8–10", below(lambda w, h: K.feast_tents("ft2", w, h, 213), 0.36), "#FFB04A", head="Joyful and Glad of Heart"),
         drawn([caps("7:11"), cp("7:12", to="and said unto him,"), gd("7:12", frm="I have heard")], "2CHR 7:11–12", lambda w, h: K.dream("dr2", w, h, 214), NIGHT,
               head="If My People"),
         drawn([gods("7:13-15")], "2CHR 7:13–15", lambda w, h: K.K2.nathan_night(w, h, 215), NIGHT),
         drawn([gods("7:16-18")], "2CHR 7:16–18", lambda w, h: K.K2.throne_glory(w, h, 216), "#14123A"),
         drawn([gods("7:19-22")], "2CHR 7:19–22", lambda w, h: K.K2.nathan_night(w, h, 217), NIGHT)]
PG.extend(pack(SEGS3, "2CH-C02-F", PG.next(), end=end_mark("NEXT · THE QUEEN OF SHEBA", "right: 10px; bottom: 34px")))
