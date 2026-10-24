"""Mark volume, Chapter 6 — The Last Shall Be First (Mark 9:30–10:52). Every verse, word for word from ref/eng-asv.
Through Galilee, the Son of man delivered up, beside his grieving face; who is the greatest — the little child set in the
midst; one casting out demons in his name; a cup of water; the millstone on the rocks by the deep sea (no one drawn); the
hand, the foot and the eye, over the valley of the unquenchable fire with no one in it; salt. Beyond the Jordan: the
Pharisees' question, and what God hath joined together; the little children brought and blessed; the rich man kneeling on
the road in his plum robe (Matthew's rich young man's looks), the commandments, One thing thou lackest, and the man going
away sorrowful; the camel and the needle's eye; the hundredfold. The road up to Jerusalem, Jesus going before; James and
John, the cup on the dark table; to minister and to give his life a ransom for many. Jericho: blind Bartimæus by the way
side in his grey garment, crying out; the garment cast away; Rabboni; and he followed him in the way."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mrk import G, art6 as A, ch05 as _prev
from mrk.common import (K, Pages, D, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF,
                        PETER, JAMES, JOHN, PHARISEE, RICH_YOUNG, RICH_SAD, BARTIMAEUS, BARTIMAEUS_SEE)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MRK-C06-00-Title", "Chapter 6 · The Last Shall Be First", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#4A2A5A"></rect><g transform="translate(0 300)">{A.to_jerusalem("t6", 760, 780, 1032)}</g>'
    return title(6, "The Last Shall Be First", "Mark 9:30 – 10:52", svg, "#3A5A7A", v("10:31", frm="and the last first."))


def F(lines, tok=JESUS_TEACH, bg=GOLDEN, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [F([cp("9:30"), cp("9:31", to="said unto them,"), sy("9:31", frm="The Son of man"), cp("9:32")], JESUS_GRIEF, bg=COLD, head="Who Is the Greatest"),
        F([cp("9:33", to="he asked them,"), sy("9:33", frm="What were ye"), cp("9:34")], JESUS),
        D([cp("9:35", to="saith unto them,"), sy("9:35", frm="If any man"), cp("9:36"), sy("9:37")], lambda w, h: A.child_midst("cm1", w, h, 935), "#C8A878", art_h=220),
        F([cp("9:38", to="said unto him,"), sy("9:38", frm="Teacher,")], JOHN, bg=COLD),
        D([cp("9:39", to="But Jesus said,"), sy("9:39", frm="Forbid him not:"), sy("9:40"), sy("9:41")], lambda w, h: A.cup_water("cw1", w, h, 939), "#8FD0E2"),
        D([sy("9:42")], lambda w, h: A.millstone("ml1", w, h, 942), "#1A2A3A", head="The Fire Is Not Quenched"),
        D([sy("9:43"), sy("9:45"), sy("9:47"), sy("9:48")], lambda w, h: A.gehenna("gh1", w, h, 943), "#2A0A10", art_h=200),
        D([sy("9:49"), sy("9:50")], lambda w, h: A.salt("st1", w, h, 949), "#C8B490"),
        # Mark 10
        D([cp("10:1")], lambda w, h: A.jordan("jd1", w, h, 1001, jesus_=True, john=False, crowd_n=8), "#8FD0E2", head="What God Hath Joined Together", stamp=10),
        F([cp("10:2", to="asked him,"), sy("10:2", frm="Is it lawful", to="his wife?"), cp("10:2", frm="trying him.")], PHARISEE, bg=RED),
        F([cp("10:3", to="said unto them,"), sy("10:3", frm="What did Moses")], JESUS),
        F([cp("10:4", to="they said,"), sy("10:4", frm="Moses suffered")], PHARISEE, bg=RED),
        F([cp("10:5", to="said unto them,"), sy("10:5", frm="For your hardness"), sy("10:6"), sy("10:7"), sy("10:8"), sy("10:9")], JESUS_TEACH),
        F([cp("10:10"), cp("10:11", to="saith unto them,"), sy("10:11", frm="Whosoever"), sy("10:12")], JESUS),
        D([cp("10:13"), cp("10:14", to="said unto them,"), sy("10:14", frm="Suffer the little")], lambda w, h: A.children_blessed("cb1", w, h, 1013), "#C8A878",
          head="Suffer the Little Children"),
        F([sy("10:15"), cp("10:16")], JESUS),
        D([cp("10:17", to="asked him,"), sy("10:17", frm="Good Teacher,")], lambda w, h: A.rich_kneels("rk1", w, h, 1017), "#8FD0E2", head="One Thing Thou Lackest"),
        F([cp("10:18", to="said unto him,"), sy("10:18", frm="Why callest"), sy("10:19")], JESUS_TEACH),
        F([cp("10:20", to="said unto him,"), sy("10:20", frm="Teacher, all")], RICH_YOUNG),
        F([cp("10:21", to="said unto him,"), sy("10:21", frm="One thing")], JESUS),
        D([cp("10:22")], lambda w, h: A.rich_away("ra1", w, h, 1022), "#8FD0E2"),
        F([cp("10:23", to="unto his disciples,"), sy("10:23", frm="How hardly")], JESUS_GRIEF, bg=COLD),
        D([cp("10:24", to="saith unto them,"), sy("10:24", frm="Children,"), sy("10:25")], lambda w, h: A.needle("nd1", w, h, 1024), "#5A3A6A"),
        F([cp("10:26", to="saying unto him,"), sy("10:26", frm="Then who"), cp("10:27", to="saith,"), sy("10:27", frm="With men")], JESUS, h=320),
        F([cp("10:28", to="say unto him,"), sy("10:28", frm="Lo, we")], PETER, head="The Last Shall Be First"),
        F([cp("10:29", to="Jesus said,"), sy("10:29", frm="Verily"), sy("10:30"), sy("10:31")], JESUS_TEACH),
        D([cp("10:32"), cp("10:33", to="saying,"), sy("10:33", frm="Behold,"), sy("10:34")], lambda w, h: A.to_jerusalem("tj1", w, h, 1032), "#4A2A5A", head="Are Ye Able?",
          art_h=200),
        F([cp("10:35", to="saying unto him,"), sy("10:35", frm="Teacher,")], JAMES),
        F([cp("10:36", to="said unto them,"), sy("10:36", frm="What would")], JESUS),
        F([cp("10:37", to="said unto him,"), sy("10:37", frm="Grant unto us")], JOHN),
        D([cp("10:38", to="said unto them,"), sy("10:38", frm="Ye know not"), cp("10:39", to="said unto him,"), sy("10:39", frm="We are able.", to="We are able."),
           cp("10:39", frm="And Jesus said", to="unto them,"), sy("10:39", frm="The cup that"), sy("10:40")], lambda w, h: A.the_cup("tc1", w, h, 1038), "#1A1630"),
        F([cp("10:41"), cp("10:42", to="saith unto them,"), sy("10:42", frm="Ye know that"), sy("10:43"), sy("10:44"), sy("10:45")], JESUS_TEACH, head="To Give His Life a Ransom"),
        D([cp("10:46")], lambda w, h: A.bartimaeus_way("bw1", w, h, 1046), "#8FD0E2", head="Bartimæus", art_h=220),
        F([cp("10:47", to="and say,"), sy("10:47", frm="Jesus, thou son"), cp("10:48", to="a great deal,"), sy("10:48", frm="Thou son of David,")], BARTIMAEUS),
        D([cp("10:49", to="and said,"), sy("10:49", frm="Call ye him.", to="Call ye him."), cp("10:49", frm="And they call", to="saying unto him,"), sy("10:49", frm="Be of good cheer:"),
           cp("10:50")], lambda w, h: A.bartimaeus_way("bw2", w, h, 1049, sprang=True), "#8FD0E2"),
        F([cp("10:51", to="and said,"), sy("10:51", frm="What wilt", to="unto thee?")], JESUS),
        F([cp("10:51", frm="And the blind man", to="unto him,"), sy("10:51", frm="Rabboni,")], BARTIMAEUS),
        F([cp("10:52", to="said unto him,"), sy("10:52", frm="Go thy way;", to="made thee whole.")], JESUS),
        F([cp("10:52", frm="And straightway")], BARTIMAEUS_SEE)]
PG.extend(K.pack(SEGS, "MRK-C06-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · HOSANNA")))
