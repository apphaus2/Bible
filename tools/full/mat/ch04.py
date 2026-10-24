"""Matthew volume, Chapter 4 — Lord of the Sabbath (Matthew 11–12). Every verse, word for word from ref/eng-asv.
John in the prison and his messengers; a reed shaken with the wind; the children in the marketplaces; the woes over the
cities of the lake; come unto me, and the yoke. The grainfields on the sabbath and the Pharisees watching; the withered hand
stretched forth; the sheep in the pit; the Pharisees taking counsel; the servant of Isaiah in song boxes over the bruised
reed and the smoking flax (the servant himself is not drawn). The blind and dumb man healed; the strong man's house; the
sign of Jonah over the great fish, Nineveh in sackcloth, the queen of the south's train; the unclean spirit never drawn —
his words over the waterless places and the empty, swept house; his mother and his brethren at the door."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art4 as A, ch03 as _prev
from mat.common import (K, Pages, drawn, cp, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        JOHN_DISCIPLE, PHARISEE, SCRIBE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C04-00-Title", "Chapter 4 · Lord of the Sabbath", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.grainfield("t4", 760, 780, 1101, pharisees=False)}</g>'
    return title(4, "Lord of the Sabbath", "Matthew 11 – 12", svg, "#2A3A5A", v("11:28"))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)
def S(a, b):
    ch, x = a.split(":")
    return [sy(f"{ch}:{k}") for k in range(int(x), int(b) + 1)]

SEGS = [D([cp("11:1"), cp("11:2"), cp("11:3", to="and said unto him,"), sy("11:3", frm="Art thou")], lambda w, h: A.prison("pr1", w, h, 1101), "#2A2A4A",
          head="Art Thou He That Cometh?", stamp=11),
        F([cp("11:4", to="said unto them,"), sy("11:4", frm="Go and tell"), sy("11:5"), sy("11:6")], JESUS),
        D([cp("11:7", to="concerning John,"), sy("11:7", frm="What went ye"), sy("11:8")], lambda w, h: A.reed("rd1", w, h, 1102), "#8FD0E2"),
        F(S("11:9", 11)),
        F(S("11:12", 15), JESUS),
        D(S("11:16", 17), lambda w, h: A.market_children("mc1", w, h, 1103), "#8FD0E2", head="We Piped unto You"),
        F(S("11:18", 19), JESUS_STERN, bg=RED),
        D([cp("11:20"), sy("11:21"), sy("11:22")], lambda w, h: A.woe("wo1", w, h, 1104), "#1A1A2E", head="Woe unto Thee, Chorazin"),
        F(S("11:23", 24), JESUS_GRIEF, bg=COLD),
        F([cp("11:25", to="answered and said,"), sy("11:25", frm="I thank thee"), sy("11:26"), sy("11:27")], JESUS, head="Come unto Me"),
        D(S("11:28", 30), lambda w, h: A.yoke("yk1", w, h, 1105), "#5A3A6A"),
        # Matthew 12
        D([cp("12:1"), cp("12:2", to="said unto him,"), sy("12:2", frm="Behold,")], lambda w, h: A.grainfield("gf1", w, h, 1201), "#8FD0E2", head="Lord of the Sabbath", stamp=12),
        F([cp("12:3", to="said unto them,"), sy("12:3", frm="Have ye not"), sy("12:4"), sy("12:5")]),
        F(S("12:6", 8), JESUS),
        D([cp("12:9"), cp("12:10", to="saying,"), sy("12:10", frm="Is it lawful", to="sabbath day?"), cp("12:10", frm="that they might")], lambda w, h: A.withered("wh1", w, h, 1202), "#C8B490",
          head="Stretch Forth Thy Hand"),
        D([cp("12:11", to="said unto them,"), sy("12:11", frm="What man"), sy("12:12")], lambda w, h: A.sheep_pit("sp1", w, h, 1203), "#8FD0E2"),
        D([cp("12:13", to="to the man,"), sy("12:13", frm="Stretch forth", to="thy hand."), cp("12:13", frm="And he stretched")], lambda w, h: A.withered("wh2", w, h, 1204, restored=True),
          "#C8B490"),
        D([cp("12:14")], lambda w, h: A.counsel("cn1", w, h, 1205), "#2A1A2A"),
        D([cp("12:15"), cp("12:16"), cp("12:17"), sg("12:18"), sg("12:19"), sg("12:20"), sg("12:21")], lambda w, h: A.reed_flax("rf1", w, h, 1206), "#3A3A6A",
          head="A Bruised Reed Shall He Not Break"),
        D([cp("12:22"), cp("12:23", to="and said,"), sy("12:23", frm="Can this"), cp("12:24", to="they said,"), sy("12:24", frm="This man")], lambda w, h: A.marvel("mv2", w, h, 1207),
          "#8FD0E2", head="A Kingdom Divided"),
        F([cp("12:25", to="said unto them,"), sy("12:25", frm="Every kingdom"), sy("12:26"), sy("12:27"), sy("12:28")], JESUS_STERN, bg=RED),
        D(S("12:29", 30), lambda w, h: A.strong_house("sh1", w, h, 1208), "#3A3A5A"),
        F(S("12:31", 32), JESUS_STERN, bg=RED),
        D(S("12:33", 33), lambda w, h: A.fruit_trees("ft2", w, h, 1209), "#8FD0E2"),
        F(S("12:34", 37)),
        F([cp("12:38", to="saying,"), sy("12:38", frm="Teacher,")], PHARISEE, bg=RED, head="The Sign of Jonah"),
        D([cp("12:39", to="said unto them,"), sy("12:39", frm="An evil"), sy("12:40")], lambda w, h: A.jonah_sign("js1", w, h, 1210), "#0B2A44"),
        D(S("12:41", 41), lambda w, h: A.nineveh("nv1", w, h, 1211), "#E8C890"),
        D(S("12:42", 42), lambda w, h: A.queen_south("qs1", w, h, 1212), "#E8C890"),
        D(S("12:43", 43), lambda w, h: A.waterless("wl1", w, h, 1213), "#0B0B1A"),
        D(S("12:44", 45), lambda w, h: A.swept("sw1", w, h, 1214), "#C8B8A0"),
        D([cp("12:46"), cp("12:47", to="said unto him,"), sy("12:47", frm="Behold,"), cp("12:48", to="that told him,"), sy("12:48", frm="Who is my"),
           cp("12:49", to="and said,"), sy("12:49", frm="Behold,"), sy("12:50")], lambda w, h: A.kindred("kn1", w, h, 1215), "#B8987A", head="My Mother and My Brethren")]
PG.extend(K.pack(SEGS, "MAT-C04-D", PG.next(), most=4, end=nxt("NEXT · THE KINGDOM OF HEAVEN IS LIKE")))
