"""Acts volume, Chapter 3 — We Must Obey God (Acts 5–6). Every verse, word for word from ref/eng-asv.
Ananias beside his face, the price kept back; Peter's rebuke beside his stern face; Ananias' death (5:5) and his
burial told in words only over the empty floor of the porch, the purse lying where it was laid and the open door; Sapphira
beside her face; her death (5:10) in words over the empty floor and the door shut. Signs and wonders in Solomon's porch;
the sick on their beds in the street and Peter's long shadow; the multitudes from the cities round about. The high priest's
jealousy and the public ward; the angel of the Lord by night — a figure of white light with a gold rim, no face — at the
open prison door; the apostles teaching in the temple at daybreak; the prison-house found shut in all safety and empty; the
apostles brought without violence; the council; We must obey God rather than men beside Peter's face; Gamaliel standing up
in the council and his counsel beside his face; the beating (5:40) in words only over the council's shut door; the
apostles departing rejoicing. The murmuring over the widows and the daily ministration; the seven chosen and the hands
laid on them; Stephen full of grace and power; the synagogue of the Libertines disputing; the suborned men and the false
witnesses beside their faces; and Stephen's face as it had been the face of an angel (a man's face, in a white light)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art3 as A, ch02 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, PETER, PETER_BOLD, PETER_STERN, ANANIAS, SAPPHIRA,
                        CAIAPHAS, GAMALIEL, STEPHEN, STEPHEN_GLORY, ELDER, SADDUCEE, WHITE_LIGHT)
from mat.common import WITNESS

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C03-00-Title", "Chapter 3 · We Must Obey God", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 300)">{A.prison_opened("t3", 760, 780, 519)}</g>'
    return title(3, "We Must Obey God", "Acts 5 – 6", svg, "#1E1650", v("5:29", frm="We must obey God"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)

SEGS = [D([cp("5:1"), cp("5:2")], lambda w, h: A.at_feet("an1", w, h, 501, giver="ananias"), "#8FD0E2", head="Ananias and Sapphira", sky=(5, "left"), art_h=300),
        F([cp("5:3", to="But Peter said,"), sy("5:3", frm="Ananias, why"), sy("5:4")], PETER_STERN, bg=RED),
        D([cp("5:5"), cp("5:6")], lambda w, h: A.empty_floor("ef1", w, h, 505), "#5A4A44", art_h=220),
        D([cp("5:7")], lambda w, h: A.empty_floor("ef2", w, h, 507, purse=False), "#5A4A44"),
        F([cp("5:8", to="Peter answered unto her,"), sy("5:8", frm="Tell me whether", to="for so much.")], PETER_STERN, bg=RED, h=230),
        F([cp("5:8", frm="And she said,", to="And she said,"), sy("5:8", frm="Yea, for so much.")], SAPPHIRA, bg=COLD, h=230),
        F([cp("5:9", to="But Peter said unto her,"), sy("5:9", frm="How is it")], PETER_STERN, bg=RED),
        D([cp("5:10"), cp("5:11")], lambda w, h: A.empty_floor("ef3", w, h, 510, purse=False, door="shut"), "#5A4A44", art_h=220),
        D([cp("5:12"), cp("5:13"), cp("5:14")], scene("sw1", 512, "porch", [(0.1, "peter", {"flip": True, "up": A.UP_BLESS}), (0.2, "john"), (0.3, "james"),
                                                                            (0.44, "crowd", {"n": 6, "x1": 0.92, "flip": True})]), "#8FD0E2", head="Signs and Wonders"),
        D([cp("5:15")], lambda w, h: A.shadow_street("sh1", w, h, 515), "#3A3A7A", art_h=240),
        D([cp("5:16")], lambda w, h: A.bringing_sick("bs1", w, h, 516), "#8FD0E2"),
        D([cp("5:17"), cp("5:18")], lambda w, h: A.ward("pw1", w, h, 517, who=("peter", "john")), "#3A3238", head="The Prison Doors Opened"),
        D([cp("5:19"), sy("5:20")], lambda w, h: A.prison_opened("po1", w, h, 519), "#05051A", art_h=260),
        D([cp("5:21")], scene("tm1", 521, "temple", [(0.08, "peter", {"flip": True, "up": A.UP_HIGH}), (0.18, "john"), (0.32, "crowd", {"n": 5, "x1": 0.6, "flip": True})], tone="dawn"),
          "#3A3A7A"),
        D([cp("5:22"), cp("5:23", to="saying,"), sy("5:23", frm="The prison-house")], lambda w, h: A.prison_found("pf1", w, h, 522), "#3A3238"),
        D([cp("5:24"), cp("5:25", to="told them,"), sy("5:25", frm="Behold,")], lambda w, h: A.council("cn1", w, h, 524, empty=True), "#4A3A44"),
        D([cp("5:26")], scene("br1", 526, "street", [(0.1, "officer"), (0.22, "peter"), (0.32, "john"), (0.42, "officer"), (0.52, ("apostle", 3)),
                                                     (0.66, "crowd", {"n": 4, "x1": 0.94, "flip": True})]), "#8FD0E2"),
        D([cp("5:27")], lambda w, h: A.council("cn2", w, h, 527, accused=("peter", "john", "james")), "#4A3A44", head="We Must Obey God"),
        F([cp("5:28", to="saying,"), sy("5:28", frm="We strictly charged")], CAIAPHAS, bg=RED),
        F([cp("5:29", to="answered and said,"), sy("5:29", frm="We must obey God"), sy("5:30"), sy("5:31"), sy("5:32")], PETER_BOLD),
        D([cp("5:33"), cp("5:34")], lambda w, h: A.council("cn3", w, h, 533, accused=(), standing=0.3), "#4A3A44", head="Gamaliel"),
        F([cp("5:35", to="said unto them,"), sy("5:35", frm="Ye men of Israel,"), sy("5:36"), sy("5:37")], GAMALIEL),
        F([sy("5:38"), sy("5:39")], GAMALIEL),
        D([cp("5:40")], lambda w, h: A.council_door("cd1", w, h, 540), "#3A3038", art_h=220),
        D([cp("5:41"), cp("5:42")], scene("rj1", 541, "street", [(0.1, "peter", {"up": A.UP_HIGH, "flip": True}), (0.2, "john"), (0.3, "james"), (0.4, ("apostle", 3)),
                                                                 (0.62, "crowd", {"n": 4, "x1": 0.92, "flip": True})]), "#8FD0E2"),
        # Acts 6
        D([cp("6:1")], lambda w, h: A.ministration("mn1", w, h, 601), "#8FD0E2", head="The Seven", sky=(6, "left"), art_h=300),
        F([cp("6:2", to="and said,"), sy("6:2", frm="It is not fit"), sy("6:3"), sy("6:4")], PETER),
        D([cp("6:5")], lambda w, h: A.seven("sv1", w, h, 605), "#8FD0E2"),
        D([cp("6:6"), cp("6:7")], lambda w, h: A.seven("sv2", w, h, 606, hands=True), "#8FD0E2"),
        D([cp("6:8")], scene("st1", 608, "street", [(0.2, "stephen", {"flip": True, "up": A.UP_BLESS}), (0.36, "man", {"c": "#7A7A80", "hr": "#6A645E", "bd": "#6A645E", "flip": True, "up": A.UP_HIGH}),
                                                    (0.5, "crowd", {"n": 5, "x1": 0.92, "flip": True})]), "#8FD0E2", head="Stephen"),
        D([cp("6:9"), cp("6:10")], lambda w, h: A.disputing("ds1", w, h, 609), "#C8B490"),
        F([cp("6:11", to="who said,"), sy("6:11", frm="We have heard")], WITNESS, bg=RED),
        D([cp("6:12")], lambda w, h: A.seized("sz1", w, h, 612), "#8FD0E2"),
        F([cp("6:13", to="who said,"), sy("6:13", frm="This man ceaseth"), sy("6:14")], WITNESS, bg=RED),
        F([cp("6:15")], STEPHEN_GLORY, bg=WHITE_LIGHT, h=300)]
PG.extend(K.pack(SEGS, "ACT-C03-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · STEPHEN")))
