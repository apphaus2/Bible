"""1 Kings volume, Chapter 6 — The Glory of Jehovah (1 Kings 8). Every verse, word for word from ref/eng-asv.
The ark brought up from Zion into the oracle under the wings of the cherubim; the cloud filling the house — the glory of
Jehovah; Solomon blessing the assembly; his prayer before the altar with his hands spread toward heaven (speech panels):
will God in very deed dwell on the earth? — hear thou in heaven thy dwelling-place, and forgive; the blessing; the
peace-offerings and the feast of fourteen days."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, cp, says, caps, joined, face, drawn, SOLOMON, SOLOMON_WISE, RED, COLD, GOLDEN)
from kg1 import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = "#0B1A2E"
PRAY = lambda seed: below(lambda w, h: K.court_scene("pr%d" % seed, w, h, seed, solomon="pray"), 0.5)


@P("1KI-C06-00-Title", "Chapter 6 · The Glory of Jehovah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#E8E2D6"></rect><g transform="translate(0 300)">{K.court_scene("t6", 760, 780, 601, cloud=True, crowd=False)}</g>')
    return chapter_title(6, "第六話", "The Glory of Jehovah", "1 Kings 8", svg, "#8A7A5A", v("8:11", frm="for the glory of Jehovah"), "1 Kings · Volume Eleven")


SEGS = [drawn([caps("8:1-2")], "1KGS 8:1–2", below(lambda w, h: K.court_scene("cs6", w, h, 602, crowd=True), 0.3), "#8FD0E2", head="The Ark into Its Place", stamp=8),
        drawn([caps("8:3-5")], "1KGS 8:3–5", below(lambda w, h: K.ark_up("au6", w, h, 603), 0.3), "#FFE680"),
        drawn([caps("8:6-9")], "1KGS 8:6–9", below(lambda w, h: K.ark_oracle(w, h), 0.36), INK),
        drawn([caps("8:10-11")], "1KGS 8:10–11", lambda w, h: K.court_scene("cl6", w, h, 604, cloud=True, crowd=False), "#E8E2D6", head="The Cloud Filled the House"),
        face([cp("8:12", to="Then spake Solomon,"), joined("say", ("8:12", "Jehovah hath said"), "8:13")], "1KGS 8:12–13", SOLOMON_WISE),
        drawn([caps("8:14"), cp("8:15", to="And he said,"), joined("say", ("8:15", "Blessed be Jehovah,"), "8:16")], "1KGS 8:14–16",
              below(lambda w, h: K.court_scene("bl6", w, h, 605, solomon="bless"), 0.46), "#8FD0E2", head="Blessed Be Jehovah"),
        face([says("8:17-19")], "1KGS 8:17–19", SOLOMON),
        face([says("8:20-21")], "1KGS 8:20–21", SOLOMON),
        drawn([caps("8:22"), cp("8:23", to="and he said,"), say("8:23", frm="O Jehovah,")], "1KGS 8:22–23", PRAY(606), "#8FD0E2", head="The Prayer of Solomon"),
        face([says("8:24-26")], "1KGS 8:24–26", SOLOMON_WISE),
        face([says("8:27-29")], "1KGS 8:27–29", SOLOMON_WISE, bg=COLD, head="Will God Dwell on the Earth?"),
        face([says("8:30-32")], "1KGS 8:30–32", SOLOMON_WISE),
        face([says("8:33-34")], "1KGS 8:33–34", SOLOMON_WISE, bg=COLD),
        face([says("8:35-36")], "1KGS 8:35–36", SOLOMON_WISE),
        face([says("8:37-40")], "1KGS 8:37–40", SOLOMON_WISE, bg=COLD),
        face([says("8:41-43")], "1KGS 8:41–43", SOLOMON_WISE, head="The Foreigner"),
        face([says("8:44-46")], "1KGS 8:44–46", SOLOMON_WISE, bg=COLD),
        face([says("8:47-49")], "1KGS 8:47–49", SOLOMON_WISE),
        face([says("8:50-53")], "1KGS 8:50–53", SOLOMON_WISE, bg=COLD),
        drawn([caps("8:54"), cp("8:55"), joined("say", "8:56", "8:57")], "1KGS 8:54–57", below(lambda w, h: K.court_scene("bl6b", w, h, 607, solomon="bless"), 0.44), "#8FD0E2",
              head="Not One Word Hath Failed"),
        face([says("8:58-61")], "1KGS 8:58–61", SOLOMON),
        drawn([caps("8:62-64")], "1KGS 8:62–64", below(lambda w, h: K.court_scene("sm6", w, h, 608, smoke=True), 0.34), "#8FD0E2"),
        drawn([caps("8:65-66")], "1KGS 8:65–66", below(lambda w, h: K.feast_tents("ft6", w, h, 609), 0.3), "#FFB04A")]
PG.extend(pack(SEGS, "1KI-C06-D", PG.next(), end=end_mark("NEXT · THE QUEEN OF SHEBA", "right: 10px; bottom: 34px")))
