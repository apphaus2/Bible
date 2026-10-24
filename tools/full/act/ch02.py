"""Acts volume, Chapter 2 — Silver and Gold Have I None (Acts 3–4). Every verse, word for word from ref/eng-asv.
Peter and John going up at the ninth hour; the door of the temple called Beautiful, its great leaves of brass, the lame man
laid at the side on his mat with his alms-bowl; Look on us; Silver and gold have I none, beside Peter's face; the right
hand taken and the man raised up, then leaping in at the gate with his arms lifted. Solomon's porch thronged; Peter's
sermon beside his face, Moses and the promise to Abraham in song boxes, the heaven that must receive him (the empty sky
of light), the stars of Abraham's seed. The priests and the captain of the temple coming upon them; the ward at eventide;
the council on the morrow in its half-circle under the lamp, Annas and Caiaphas, Peter and John standing in the midst with
the man that was healed; the stone set at nought made the head of the corner; the council conferring alone; We cannot
but speak. The company praying with one accord, the Psalm in song boxes (the kings of the earth in array; Herod and Pilate
at the judgment-seat); the place shaken; one heart and soul; the prices laid at the apostles' feet; and Joseph surnamed
Barnabas beside his face."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art2 as A, ch01 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, PETER, PETER_BOLD, JOHN_BOLD, BARNABAS, SADDUCEE)
from mat.art8 import corner_stone
from mat.art11 import judgment_seat
from oba.minor import vista

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C02-00-Title", "Chapter 2 · Silver and Gold Have I None", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.beautiful_gate("t2", 760, 780, 301, stage="leap")}</g>'
    return title(2, "Silver and Gold Have I None", "Acts 3 – 4", svg, "#3A5A7A", v("3:6", frm="Silver and gold have I none;", to="that give I thee."))


SEGS = [D([cp("3:1"), cp("3:2")], lambda w, h: A.beautiful_gate("bg1", w, h, 301), "#8FD0E2", head="The Gate Called Beautiful", sky=(3, "left"), art_h=240),
        D([cp("3:3"), cp("3:4", to="said,"), sy("3:4", frm="Look on us."), cp("3:5")], lambda w, h: A.beautiful_gate("bg2", w, h, 303, stage="look"), "#8FD0E2"),
        F([cp("3:6", to="But Peter said,"), sy("3:6", frm="Silver and gold")], PETER_BOLD),
        D([cp("3:7")], lambda w, h: A.beautiful_gate("bg3", w, h, 307, stage="raise"), "#8FD0E2", art_h=240),
        D([cp("3:8"), cp("3:9"), cp("3:10")], lambda w, h: A.beautiful_gate("bg4", w, h, 308, stage="leap"), "#8FD0E2", art_h=220),
        D([cp("3:11"), cp("3:12", to="unto the people,"), sy("3:12", frm="Ye men of Israel,")], lambda w, h: A.porch_crowd("pc1", w, h, 311), "#8FD0E2",
          head="In the Porch Called Solomon's"),
        F([sy("3:13"), sy("3:14"), sy("3:15")], PETER_BOLD, bg=RED),
        F([sy("3:16"), sy("3:17"), sy("3:18")], PETER),
        D([sy("3:19"), sy("3:20"), sy("3:21")], lambda w, h: A.ascension("ag1", w, h, 319, gone=True), "#2A3A7A"),
        F([sy("3:22", to="Moses indeed said,"), sg("3:22", frm="A prophet"), sg("3:23"), sy("3:24")], PETER_BOLD),
        D([sy("3:25", to="saying unto Abraham,"), sg("3:25", frm="And in thy seed"), sy("3:26")],
          lambda w, h: vista(w, h, 325, tone="night", stars=True, hills_n=2, horizon=0.7), "#05051A", art_h=200),
        # Acts 4
        D([cp("4:1"), cp("4:2")], lambda w, h: A.scene("pt1", w, h, 401, "porch", [(0.12, "peter", {"up": A.UP_HIGH, "flip": True}), (0.22, "john"),
                                                                                 (0.36, "crowd", {"n": 3, "x1": 0.5}), (0.62, "officer", {"flip": True}),
                                                                                 (0.72, "priest", {"flip": True}), (0.82, "elder", {"flip": True}), (0.92, "officer", {"flip": True})]),
          "#8FD0E2", head="Put in Ward", sky=(4, "left")),
        D([cp("4:3"), cp("4:4")], lambda w, h: A.ward("wd1", w, h, 403), "#3A3238", art_h=200),
        D([cp("4:5"), cp("4:6")], lambda w, h: A.council("cn1", w, h, 405, accused=()), "#4A3A44", head="By What Power?"),
        D([cp("4:7", to="they inquired,"), sy("4:7", frm="By what power,")], lambda w, h: A.council("cn2", w, h, 407, healed=True), "#4A3A44"),
        F([cp("4:8", to="said unto them,"), sy("4:8", frm="Ye rulers"), sy("4:9"), sy("4:10")], PETER_BOLD, bg=RED),
        D([sy("4:11"), sy("4:12")], lambda w, h: corner_stone("cs1", w, h, 411), "#FFC890"),
        D([cp("4:13"), cp("4:14")], lambda w, h: A.council("cn3", w, h, 413, healed=True), "#4A3A44"),
        D([cp("4:15")], lambda w, h: A.council("cn4", w, h, 415, empty=True), "#4A3A44", head="We Cannot but Speak"),
        F([cp("4:16", to="saying,"), sy("4:16", frm="What shall we do"), sy("4:17")], SADDUCEE, bg=RED),
        D([cp("4:18")], lambda w, h: A.council("cn5", w, h, 418), "#4A3A44"),
        F([cp("4:19", to="said unto them,"), sy("4:19", frm="Whether it is right"), sy("4:20")], JOHN_BOLD),
        D([cp("4:21"), cp("4:22")], lambda w, h: A.scene("lg1", w, h, 421, "street", [(0.1, "peter"), (0.2, "john"), (0.31, "man", {"c": "#8A7A5A", "v": "#6A5A3A", "bd": "#3A2A1E", "up": A.UP_HIGH}),
                                                                                  (0.5, "crowd", {"n": 6, "x1": 0.92, "flip": True})]), "#8FD0E2"),
        D([cp("4:23"), cp("4:24", to="and said,"), sy("4:24", frm="O Lord,")], lambda w, h: A.company_pray("cp1", w, h, 423), "#C8A878", head="With One Accord"),
        D([sy("4:25", to="didst say,"), sg("4:25", frm="Why did the Gentiles"), sg("4:26")], lambda w, h: A.kings_array("ka1", w, h, 425), "#3A0A10", art_h=220),
        D([sy("4:27"), sy("4:28")], lambda w, h: judgment_seat("js1", w, h, 427), "#8FD0E2"),
        D([sy("4:29"), sy("4:30")], lambda w, h: A.company_pray("cp2", w, h, 429), "#C8A878"),
        D([cp("4:31")], lambda w, h: A.company_pray("cp3", w, h, 431, shaken=True), "#FFF4C2", art_h=240),
        D([cp("4:32"), cp("4:33")], lambda w, h: A.scene("oh1", w, h, 432, "porch", [(0.1, "peter", {"up": A.UP_BLESS, "flip": True}), (0.2, "john"), (0.3, "james"),
                                                                                 (0.44, "seated", {"c": "#6A4A3A", "v": "#3A4A6A", "flip": True}),
                                                                                 (0.56, "woman", {"c": "#2A4A7A", "v": "#3A6AA8", "flip": True}),
                                                                                 (0.68, "seated", {"c": "#5A6A3A", "flip": True}), (0.8, "woman", {"c": "#6A4A5A", "v": "#3A3A5A", "flip": True}),
                                                                                 (0.9, "seated", {"c": "#7A3A3A", "v": "#E8E2D6", "bd": "#6A645E", "flip": True})]), "#8FD0E2",
          head="One Heart and Soul"),
        D([cp("4:34"), cp("4:35")], lambda w, h: A.all_common("al1", w, h, 434), "#8FD0E2"),
        D([cp("4:36")], lambda w, h: A.at_feet("af2", w, h, 436), "#8FD0E2", head="Barnabas"),
        F([cp("4:37")], BARNABAS, h=260)]
PG.extend(K.pack(SEGS, "ACT-C02-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · WE MUST OBEY GOD")))
