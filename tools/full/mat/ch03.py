"""Matthew volume, Chapter 3 — The Harvest Is Plenteous (Matthew 8–10). Every verse, word for word from ref/eng-asv.
The leper touched on the road below the mountain; the centurion in the street of Capernaum, his words beside his face; Peter's
house and the evening at the door; the foxes and the birds; the tempest, Jesus asleep in the stern, then standing over the
waves, then the great calm. The Gadarenes: the tombs in the rock and the two men drawn as men (the demons are never drawn,
their words stand over the tombs), the swine running down the steep, the city at its gate. The bed carried and carried home;
Matthew at the place of toll; the publicans at meat; the wine-skins; the ruler, the border of the garment, the flute-players
and the damsel raised; the two blind men; the dumb man; the harvest and the sheep without a shepherd. The twelve named under
their figures; the sending forth; the dust shaken off at the gate; sheep among wolves; the house-tops; two sparrows; a cup of
cold water. The scourging of 10:17 is in words beside his face only."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art3 as A, ch02 as _prev
from mat.common import (K, Pages, drawn, cp, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        CENTURION, SCRIBE, SCRIBE_STERN, RULER, JOHN_DISCIPLE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("MAT-C03-00-Title", "Chapter 3 · The Harvest Is Plenteous", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#5A3A6A"></rect><g transform="translate(0 300)">{A.harvest("t3", 760, 780, 801)}</g>'
    return title(3, "The Harvest Is Plenteous", "Matthew 8 – 10", svg, "#3A2A4A", v("9:37", frm="The harvest"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
def S(a, b):
    ch, x = a.split(":")
    return [sy(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

SEGS = [D([cp("8:1"), cp("8:2", to="saying,"), sy("8:2", frm="Lord, if")], lambda w, h: A.leper("lp1", w, h, 801), "#8FD0E2", head="If Thou Wilt", stamp=8),
        F([cp("8:3", to="saying,"), sy("8:3", frm="I will;", to="made clean."), cp("8:3", frm="And straightway"), cp("8:4", to="saith unto him,"), sy("8:4", frm="See thou")], JESUS),
        D([cp("8:5"), cp("8:6", to="and saying,"), sy("8:6", frm="Lord, my servant")], lambda w, h: A.centurion("ce1", w, h, 802), "#8FD0E2", head="So Great Faith"),
        F([cp("8:7", to="saith unto him,"), sy("8:7", frm="I will come")], JESUS),
        F([cp("8:8", to="answered and said,"), sy("8:8", frm="Lord, I am"), sy("8:9")], CENTURION, bg=GOLDEN),
        F([cp("8:10", to="that followed,"), sy("8:10", frm="Verily"), sy("8:11"), sy("8:12")]),
        D([cp("8:13", to="unto the centurion,"), sy("8:13", frm="Go thy way;", to="done unto thee."), cp("8:13", frm="And the servant")], lambda w, h: A.centurion("ce2", w, h, 803, healed=True), "#8FD0E2"),
        D([cp("8:14"), cp("8:15")], lambda w, h: A.fever("fv1", w, h, 804), "#B8987A", head="He Touched Her Hand"),
        D([cp("8:16"), cp("8:17", to="saying,"), sg("8:17", frm="Himself took")], lambda w, h: A.at_even("ae1", w, h, 805), "#4A2A5A"),
        F([cp("8:18"), cp("8:19", to="said unto him,"), sy("8:19", frm="Teacher,")], SCRIBE, head="Follow Me"),
        D([cp("8:20", to="saith unto him,"), sy("8:20", frm="The foxes")], lambda w, h: A.foxes("fx1", w, h, 806), "#4A2A5A"),
        D([cp("8:21", to="said unto him,"), sy("8:21", frm="Lord, suffer"), cp("8:22", to="saith unto him,"), sy("8:22", frm="Follow me;")],
          lambda w, h: A.road_two("rt1", w, h, 807, cloth="#6A5A3A"), "#8FD0E2"),
        D([cp("8:23"), cp("8:24")], lambda w, h: A.tempest("tp1", w, h, 808), "#14141E", head="Even the Winds and the Sea Obey Him"),
        D([cp("8:25", to="saying,"), sy("8:25", frm="Save, Lord;"), cp("8:26", to="saith unto them,"), sy("8:26", frm="Why are ye", to="little faith?"), cp("8:26", frm="Then he arose")],
          lambda w, h: A.tempest("tp2", w, h, 809, awake=True), "#14141E"),
        D([cp("8:27", to="saying,"), sy("8:27", frm="What manner")], lambda w, h: A.tempest("tp3", w, h, 810, calm=True), "#5AB0D8"),
        D([cp("8:28")], lambda w, h: A.tombs("tb1", w, h, 811), "#6A6A8A", head="The Country of the Gadarenes"),
        D([cp("8:29", to="saying,"), sy("8:29", frm="What have we"), cp("8:30"), cp("8:31", to="saying,"), sy("8:31", frm="If thou cast")],
          lambda w, h: A.tombs("tb2", w, h, 812, jesus_=False, swine=True), "#6A6A8A"),
        D([cp("8:32", to="said unto them,"), sy("8:32", frm="Go.", to="Go."), cp("8:32", frm="And they came out")], lambda w, h: A.swine_steep("sw1", w, h, 813), "#6A6A8A"),
        D([cp("8:33"), cp("8:34")], lambda w, h: A.city_gate("cg1", w, h, 814), "#8FD0E2"),
        # Matthew 9
        D([cp("9:1"), cp("9:2", to="said unto the sick of the palsy,"), sy("9:2", frm="Son, be of")], lambda w, h: A.bed_carried("bc1", w, h, 901), "#8FD0E2", head="Thy Sins Are Forgiven", stamp=9),
        F([cp("9:3", to="within themselves,"), sy("9:3", frm="This man")], SCRIBE_STERN, bg=RED),
        F([cp("9:4", to="thoughts said,"), sy("9:4", frm="Wherefore"), sy("9:5"), sy("9:6", to="forgive sins"), cp("9:6", frm="(then saith", to="palsy),"), sy("9:6", frm="Arise, and take")]),
        D([cp("9:7"), cp("9:8")], lambda w, h: A.bed_carried("bc2", w, h, 902, rise=True), "#8FD0E2"),
        D([cp("9:9", to="saith unto him,"), sy("9:9", frm="Follow me.", to="Follow me."), cp("9:9", frm="And he arose")], lambda w, h: A.toll("tl1", w, h, 903), "#8FD0E2",
          head="Not the Righteous, but Sinners"),
        D([cp("9:10"), cp("9:11", to="unto his disciples,"), sy("9:11", frm="Why eateth")], lambda w, h: A.at_meat("am1", w, h, 904, pharisees=True), "#8A6A4A"),
        F([cp("9:12", to="he said,"), sy("9:12", frm="They that"), sy("9:13")]),
        F([cp("9:14", to="saying,"), sy("9:14", frm="Why do we")], JOHN_DISCIPLE),
        F([cp("9:15", to="said unto them,"), sy("9:15", frm="Can the sons")], JESUS),
        D([sy("9:16"), sy("9:17")], lambda w, h: A.wineskins("ws1", w, h, 905), "#E8D8B8"),
        F([cp("9:18", to="saying,"), sy("9:18", frm="My daughter")], RULER, bg=COLD, head="The Damsel Is Not Dead"),
        D([cp("9:19"), cp("9:20"), cp("9:21", to="within herself,"), sy("9:21", frm="If I do")], lambda w, h: A.border("bd1", w, h, 906), "#8FD0E2"),
        F([cp("9:22", to="seeing her said,"), sy("9:22", frm="Daughter,", to="made thee whole."), cp("9:22", frm="And the woman")], JESUS),
        D([cp("9:23"), cp("9:24", to="he said,"), sy("9:24", frm="Give place:", to="but sleepeth."), cp("9:24", frm="And they laughed")], lambda w, h: A.ruler_house("rh1", w, h, 907),
          "#8FD0E2"),
        D([cp("9:25"), cp("9:26")], lambda w, h: A.ruler_house("rh2", w, h, 908, raised=True), "#C8A878"),
        D([cp("9:27", to="saying,"), sy("9:27", frm="Have mercy")], lambda w, h: A.blind_two("bl1", w, h, 909), "#8FD0E2", head="According to Your Faith"),
        D([cp("9:28", to="saith unto them,"), sy("9:28", frm="Believe ye", to="to do this?"), cp("9:28", frm="They say unto him,", to="They say unto him,"), sy("9:28", frm="Yea, Lord."),
           cp("9:29", to="saying,"), sy("9:29", frm="According"), cp("9:30", to="saying,"), sy("9:30", frm="See that")], lambda w, h: A.blind_two("bl2", w, h, 910, healed=True), "#B8987A"),
        D([cp("9:31"), cp("9:32"), cp("9:33", to="saying,"), sy("9:33", frm="It was never"), cp("9:34", to="said,"), sy("9:34", frm="By the prince")], lambda w, h: A.marvel("mv1", w, h, 911),
          "#8FD0E2"),
        D([cp("9:35"), cp("9:36")], lambda w, h: A.harvest("hv1", w, h, 912), "#5A3A6A", head="The Harvest Indeed Is Plenteous"),
        F([cp("9:37", to="unto his disciples,"), sy("9:37", frm="The harvest"), sy("9:38")]),
        # Matthew 10
        D([cp("10:1"), cp("10:2"), cp("10:3"), cp("10:4")], lambda w, h: A.twelve_named("tw1", w, h, 1001), MAP, head="The Twelve Apostles", stamp=10, art_h=300),
        D([cp("10:5", to="saying,"), sy("10:5", frm="Go not"), sy("10:6"), sy("10:7"), sy("10:8")], lambda w, h: A.sent_forth("sf1", w, h, 1002), "#8FD0E2"),
        F(S("10:9", 10)),
        F(S("10:11", 13), JESUS),
        D(S("10:14", 15), lambda w, h: A.dust_gate("dg1", w, h, 1003), "#C8A890"),
        D(S("10:16", 16), lambda w, h: A.sheep_wolves("sw2", w, h, 1004), "#2A1A3A", head="Sheep in the Midst of Wolves"),
        F(S("10:17", 18), JESUS_STERN, bg=RED),
        F(S("10:19", 20), JESUS),
        F(S("10:21", 23), JESUS_GRIEF, bg=COLD),
        F(S("10:24", 25)),
        D(S("10:26", 27), lambda w, h: A.housetops("ht1", w, h, 1005), "#3A3A7A", head="Fear Them Not"),
        F(S("10:28", 28), JESUS_STERN, bg=RED),
        D(S("10:29", 31), lambda w, h: A.sparrows("sp1", w, h, 1006), "#C8B490"),
        F(S("10:32", 33)),
        F(S("10:34", 36), JESUS_STERN, bg=RED, head="Not Peace, but a Sword"),
        F(S("10:37", 39), JESUS_GRIEF, bg=COLD),
        D(S("10:40", 42), lambda w, h: A.cup_water("cw1", w, h, 1007), "#8FD0E2")]
PG.extend(K.pack(SEGS, "MAT-C03-D", PG.next(), most=4, end=nxt("NEXT · LORD OF THE SABBATH")))
