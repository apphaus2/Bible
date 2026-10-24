"""Acts volume, Chapter 6 — What God Hath Cleansed (Acts 10–11). Every verse, word for word from ref/eng-asv.
Cornelius at the ninth hour in his house at Cæsarea, the angel of God coming in (white light, no face); Cornelius beside his
face; his servants and the devout soldier sent to Joppa. Peter on the housetop at the sixth hour; the heaven opened and the
great sheet let down by four corners with the beasts, the creeping things and the birds; the voice in the Voice box (God
never drawn); the three men at the gate; the Spirit's words in the Voice box; the coast road; Cornelius at Peter's feet —
Stand up; I myself also am a man; the kinsmen gathered; Peter's sermon beside his face, the court of the house between; the
Holy Spirit falling on the Gentiles as light from above. Peter at Jerusalem among them of the circumcision, telling the
vision again (the sheet drawn again, the voice again in the Voice box); Then to the Gentiles also. The scattered ones as far
as Phœnicia, Cyprus and Antioch on the map; Antioch's colonnaded street; Barnabas sent, then Saul fetched from Tarsus; the
disciples called Christians first in Antioch; Agabus standing up; the relief carried to Judæa."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art6 as A, ch05 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PETER, PETER_BOLD, CORNELIUS, CORNELIUS_PRAY, BARNABAS,
                        AGABUS, PHARISEE, WHITE_LIGHT)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C06-00-Title", "Chapter 6 · What God Hath Cleansed", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#5AB0D8"></rect><g transform="translate(0 240)">{A.housetop("t6", 760, 840, 1011, sheet=True)}</g>'
    return title(6, "What God Hath Cleansed", "Acts 10 – 11", svg, "#2A5A8A", v("10:15", frm="What God hath cleansed,"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)
house = A.cornelius_house

SEGS = [D([cp("10:1"), cp("10:2")], lambda w, h: house("co1", w, h, 1001), "#A8382E", head="Cornelius", sky=(10, "left"), art_h=240),
        D([cp("10:3", to="saying to him,"), sy("10:3", frm="Cornelius.")], lambda w, h: house("co2", w, h, 1003, angel_=True), "#A8382E", art_h=240),
        F([cp("10:4", to="being affrighted, said,"), sy("10:4", frm="What is it, Lord?", to="What is it, Lord?")], CORNELIUS_PRAY, bg=COLD, h=220),
        D([cp("10:4", frm="And he said unto him,", to="And he said unto him,"), sy("10:4", frm="Thy prayers"), sy("10:5"), sy("10:6")],
          lambda w, h: house("co3", w, h, 1004, angel_=True), "#A8382E"),
        D([cp("10:7"), cp("10:8")], lambda w, h: house("co4", w, h, 1007, sending=True), "#A8382E"),
        D([cp("10:9"), cp("10:10")], lambda w, h: A.housetop("ht1", w, h, 1009), "#5AB0D8", head="Upon the Housetop", art_h=260),
        D([cp("10:11"), cp("10:12")], lambda w, h: A.housetop("ht2", w, h, 1011, sheet=True), "#5AB0D8", art_h=320),
        D([cp("10:13", to="a voice to him,"), gd("10:13", frm="Rise, Peter;"), cp("10:14", to="But Peter said,"), sy("10:14", frm="Not so, Lord;"),
           cp("10:15", to="the second time,"), gd("10:15", frm="What God hath cleansed,"), cp("10:16")], lambda w, h: A.housetop("ht3", w, h, 1013, sheet=True), "#5AB0D8", art_h=260),
        D([cp("10:17"), cp("10:18")], lambda w, h: A.housetop("ht4", w, h, 1017, men=True, perplexed=True), "#5AB0D8"),
        D([cp("10:19", to="the Spirit said unto him,"), gd("10:19", frm="Behold, three men"), gd("10:20")], lambda w, h: A.housetop("ht5", w, h, 1019, men=True, perplexed=True), "#5AB0D8"),
        D([cp("10:21", to="and said,"), sy("10:21", frm="Behold, I am he"), cp("10:22", to="And they said,"), sy("10:22", frm="Cornelius a centurion,")],
          lambda w, h: A.tanner("tn1", w, h, 1021), "#8FD0E2"),
        D([cp("10:23"), cp("10:24")], A.coast_road, "#0B1A2E", art_h=240),
        D([cp("10:25"), cp("10:26", to="saying,"), sy("10:26", frm="Stand up;")], lambda w, h: house("co5", w, h, 1025, fell=True), "#A8382E", head="I Myself Also Am a Man", art_h=240),
        D([cp("10:27"), cp("10:28", to="and he said unto them,"), sy("10:28", frm="Ye yourselves know"), sy("10:29")], lambda w, h: house("co6", w, h, 1027, gathered=True, peter_in=True), "#A8382E"),
        F([cp("10:30", to="And Cornelius said,"), sy("10:30", frm="Four days ago,"), sy("10:31"), sy("10:32"), sy("10:33")], CORNELIUS),
        F([cp("10:34", to="and said,"), sy("10:34", frm="Of a truth"), sy("10:35"), sy("10:36"), sy("10:37")], PETER_BOLD, head="God Is No Respecter of Persons"),
        D([sy("10:38"), sy("10:39")], lambda w, h: A.multitudes("mu1", w, h, 1038), "#8FD0E2"),
        F([sy("10:40"), sy("10:41"), sy("10:42"), sy("10:43")], PETER),
        D([cp("10:44"), cp("10:45"), cp("10:46", to="magnify God.")], lambda w, h: house("co7", w, h, 1044, gathered=True, peter_in=True, spirit=True), "#A8382E", art_h=240),
        F([cp("10:46", frm="Then answered Peter,"), sy("10:47"), cp("10:48")], PETER_BOLD),
        # Acts 11
        D([cp("11:1"), cp("11:2"), cp("11:3", to="saying,"), sy("11:3", frm="Thou wentest in")], lambda w, h: A.contended("ct1", w, h, 1101), "#C8A878",
          head="Peter at Jerusalem", sky=(11, "left"), art_h=260),
        F([cp("11:4"), sy("11:5"), sy("11:6")], PETER),
        D([sy("11:7", to="saying unto me,"), gd("11:7", frm="Rise, Peter;"), sy("11:8"), sy("11:9", to="out of heaven,"), gd("11:9", frm="What God hath cleansed,"), sy("11:10")],
          lambda w, h: A.housetop("ht6", w, h, 1107, sheet=True), "#5AB0D8", art_h=240),
        F([sy("11:11"), sy("11:12"), sy("11:13"), sy("11:14")], PETER),
        F([sy("11:15"), sy("11:16"), sy("11:17")], PETER_BOLD),
        D([cp("11:18", to="saying,"), sy("11:18", frm="Then to the Gentiles")], lambda w, h: A.contended("ct2", w, h, 1118), "#C8A878"),
        D([cp("11:19"), cp("11:20"), cp("11:21")], A.antioch_map, "#0B1A2E", head="Christians First in Antioch", art_h=260),
        D([cp("11:22"), cp("11:23"), cp("11:24")], lambda w, h: A.antioch("an1", w, h, 1122, who=("barnabas",)), "#8FD0E2"),
        D([cp("11:25"), cp("11:26")], lambda w, h: A.antioch("an2", w, h, 1125), "#8FD0E2", art_h=240),
        D([cp("11:27"), cp("11:28")], lambda w, h: A.agabus_stood("ag1", w, h, 1127), "#D8C098", art_h=240),
        D([cp("11:29"), cp("11:30")], lambda w, h: A.relief("rl1", w, h, 1129), "#8FD0E2")]
PG.extend(K.pack(SEGS, "ACT-C06-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE WORD OF GOD GREW")))
