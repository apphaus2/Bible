"""Luke volume, Chapter 5 — The Widow of Nain (Luke 7). Every verse, word for word from ref/eng-asv.
Capernaum: the elders of the Jews before the synagogue the centurion built; his friends on the road — Lord, trouble not
thyself; the centurion's words beside his face; such faith, not in Israel; the servant whole. The gate of Nain: the bier
carried out far off, the widow in black and much people — Weep not; the bier touched and the bearers standing still; Young
man, Arise; he sat up and was given to his mother (no body drawn close: the bier is a covered litter seen at a distance).
John's two messengers on the road; Go and tell John; the reed shaken with the wind; the children in the marketplace. The
Pharisee's house: the woman that was a sinner kneeling veiled at his feet with the alabaster cruse, her tears and kisses
told in words; Simon's thought beside his face; the two debtors; Seest thou this woman?; Thy sins are forgiven; go in
peace."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art4 as A, ch04 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        CENTURION, CROWD_MAN, NAIN_WIDOW, JOHN_DISCIPLE, PHARISEE, SINNER_WOMAN, DOCTOR)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C05-00-Title", "Chapter 5 · The Widow of Nain", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.nain("t5", 760, 780, 701, stage="given")}</g>'
    return title(5, "The Widow of Nain", "Luke 7", svg, "#2A4A6A", v("7:14", frm="Young man,"))


SEGS = [D([cp("7:1"), cp("7:2"), cp("7:3")], lambda w, h: A.centurion("cn1", w, h, 701, healed=False), "#8FD0E2", head="So Great Faith", sky=7),
        D([N("7:4", "earnestly, saying,"), sy("7:5")], lambda w, h: A.elders_ask("ea1", w, h, 702), "#8FD0E2"),
        D([N("7:6", "saying unto him,"), sy("7:7")], lambda w, h: A.elders_ask("ea2", w, h, 703, friends=True), "#8FD0E2"),
        F([sy("7:8")], CENTURION, bg=GOLDEN),
        F([N("7:9", "that followed him,")], JESUS),
        D([cp("7:10")], lambda w, h: A.centurion("cn2", w, h, 704, healed=True), "#8FD0E2"),
        D([cp("7:11"), cp("7:12")], lambda w, h: A.nain("na1", w, h, 705), "#8FD0E2", head="Young Man, Arise", art_h=260),
        F([N("7:13", "said unto her,")], JESUS_GRIEF, bg=COLD),
        D([Q("7:14", "c", "And he said,", "s")], lambda w, h: A.nain("na2", w, h, 706, stage="touch"), "#8FD0E2", art_h=240),
        D([cp("7:15")], lambda w, h: A.nain("na3", w, h, 707, stage="risen"), "#8FD0E2", art_h=240),
        D([Q("7:16", "c", "saying,", "s"), cp("7:17")], lambda w, h: A.nain("na4", w, h, 708, stage="given"), "#8FD0E2"),
        D([cp("7:18"), N("7:19", "saying,")], lambda w, h: A.prison("pr1", w, h, 709), "#2A2A4A", head="Art Thou He That Cometh?"),
        D([N("7:20", "they said,"), cp("7:21")], lambda w, h: A.road_two("rt1", w, h, 710, cloth="#7A5A3A"), "#8FD0E2"),
        F([N("7:22", "said unto them,"), sy("7:23")], JESUS_TEACH),
        D([N("7:24", "concerning John,"), sy("7:25")], lambda w, h: A.reed("rd1", w, h, 711), "#8FD0E2", head="More Than a Prophet"),
        F([sy("7:26"), sy("7:27"), sy("7:28")], JESUS),
        D([cp("7:29"), cp("7:30")], lambda w, h: A.jordan("jd1", w, h, 712, crowd_n=8), "#8FD0E2"),
        D([sy("7:31"), sy("7:32")], lambda w, h: A.market_children("mc1", w, h, 713), "#C8A890"),
        F([sy("7:33"), sy("7:34"), sy("7:35")], JESUS_STERN, bg=RED),
        D([cp("7:36"), cp("7:37")], lambda w, h: A.at_his_feet("af1", w, h, 714, stage="anoint"), "#B8987A", head="She Loved Much", art_h=240),
        D([cp("7:38")], lambda w, h: A.at_his_feet("af2", w, h, 715, stage="anoint"), "#B8987A", art_h=240),
        F([N("7:39", "within himself, saying,")], PHARISEE, bg=RED),
        F((q40 := Q("7:40", "c", "said unto him,", "s", "to say unto thee.", "c", "he saith,", "s"))[:2]),
        F(q40[2:], PHARISEE, bg=GOLDEN, ref="LUKE 7:40"),
        D([sy("7:41"), sy("7:42")], lambda w, h: A.debtors("db1", w, h, 716), "#5A3A2A"),
        F((q43 := Q("7:43", "c", "answered and said,", "s", "forgave the most.", "c", "said unto him,", "s"))[:2], PHARISEE, bg=GOLDEN),
        F(q43[2:], JESUS, ref="LUKE 7:43"),
        D([N("7:44", "said unto Simon,"), sy("7:45"), sy("7:46")], lambda w, h: A.at_his_feet("af3", w, h, 717, stage="turn"), "#B8987A"),
        F([sy("7:47"), N("7:48", "said unto her,")], JESUS),
        D([N("7:49", "within themselves,"), Q("7:50", "c", "unto the woman,", "s")], lambda w, h: A.go_in_peace("gp1", w, h, 718), "#B8987A", art_h=260)]
PG.extend(K.pack(SEGS, "LUK-C05-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE SOWER")))
