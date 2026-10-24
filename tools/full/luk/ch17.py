"""Luke volume, Chapter 17 — He Is Risen (Luke 24). Every verse, word for word from ref/eng-asv.
At early dawn the women with their spices; the stone rolled away and the body not found; two men in dazzling apparel —
figures of white light with a gold rim, no faces — and the women bowed to the earth: Why seek ye the living among the dead?;
the words told to the eleven as idle talk; Peter stooping at the tomb, the linen cloths by themselves. The road to Emmaus:
the two communing, Jesus risen in white light drawing near and going with them, their eyes holden; Cleopas beside his face;
O foolish men, and slow of heart; Abide with us; the table at evening, the bread blessed and broken and their eyes opened,
his place empty; Was not our heart burning within us?; the road back by night — the Lord is risen indeed. In the midst of
the eleven: Peace be unto you; see my hands and my feet (no wounds drawn: Jesus risen in white light); the broiled fish;
the scriptures opened; tarry ye in the city. At Bethany, his hands lifted up, blessing them, parted from them and carried
up into heaven in a cloud of light (God never drawn: the light only); and continually in the temple, blessing God."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art13 as A, ch16 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, fin, COLD, GOLDEN, RED, NIGHT, JESUS_RISEN, CLEOPAS, CLEOPAS_JOY)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
RISEN_LIGHT = "radial-gradient(circle at 26% 46%, #FFFFFF 0 70px, #FFF8DC 220px, #F3E2B0 460px)"


@P("LUK-C17-00-Title", "Chapter 17 · He Is Risen", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#5A6A9A"></rect><g transform="translate(0 300)">{A.stone_back("t17", 760, 780, 2401, women=False)}</g>'
    return title(17, "He Is Risen", "Luke 24", svg, "#3A4A7A", v("24:6", frm="He is not here, but is risen:", to="but is risen:"))


SEGS = [D([cp("24:1")], lambda w, h: A.spices_dawn("sd1", w, h, 2401), "#3A3A7A", head="Why Seek Ye the Living among the Dead?", sky=24, art_h=240),
        D([cp("24:2"), cp("24:3")], lambda w, h: A.stone_back("sb1", w, h, 2402), "#5A6A9A"),
        D([cp("24:4"), N("24:5", "they said unto them,")], lambda w, h: A.two_men("tm1", w, h, 2404), "#2A2220", art_h=260),
        D([sy("24:6"), sy("24:7")], lambda w, h: A.two_men("tm2", w, h, 2406), "#2A2220"),
        D([cp("24:8"), cp("24:9"), cp("24:10"), cp("24:11")], lambda w, h: A.mourners("mr1", w, h, 2408), "#5A4A4A", art_h=220),
        D([cp("24:12")], lambda w, h: A.peter_stoops("ps1", w, h, 2412), "#5A6A9A", art_h=260),
        D([cp("24:13"), cp("24:14")], lambda w, h: A.emmaus("em1", w, h, 2413), "#8FD0E2", head="Their Eyes Were Holden"),
        D([cp("24:15"), cp("24:16")], lambda w, h: A.emmaus("em2", w, h, 2415, stage="joined"), "#8FD0E2", art_h=240),
        D([Q("24:17", "c", "said unto them,", "s", "as ye walk?", "c")], lambda w, h: A.emmaus("em3", w, h, 2417, stage="joined"), "#8FD0E2"),
        F([N("24:18", "answering said unto him,")], CLEOPAS, bg=COLD),
        F((q19 := Q("24:19", "c", "And he said unto them,", "s", "What things?", "c", "said unto him,", "s"))[:2], JESUS_RISEN, bg=RISEN_LIGHT),
        F([q19[2:], sy("24:20"), sy("24:21")], CLEOPAS, bg=COLD, ref="LUKE 24:19–21"),
        F([sy("24:22"), sy("24:23"), sy("24:24")], CLEOPAS, bg=COLD),
        D([N("24:25", "said unto them,"), sy("24:26"), cp("24:27")], lambda w, h: A.emmaus("em4", w, h, 2425, stage="joined"), "#8FD0E2", head="Slow of Heart to Believe"),
        D([cp("24:28"), Q("24:29", "c", "saying,", "s", "far spent.", "c")], lambda w, h: A.emmaus("em5", w, h, 2428, stage="village"), "#4A3A6A", head="Abide with Us"),
        D([cp("24:30")], lambda w, h: A.emmaus("em6", w, h, 2430, stage="table"), "#5A4A48", art_h=260),
        D([cp("24:31")], lambda w, h: A.emmaus("em7", w, h, 2431, stage="gone"), "#5A4A48", art_h=240),
        F([N("24:32", "one to another,")], CLEOPAS_JOY),
        D([cp("24:33"), N("24:34", "saying,"), cp("24:35")], lambda w, h: A.emmaus("em8", w, h, 2433, stage="back"), NIGHT),
        D([Q("24:36", "c", "saith unto them,", "s"), cp("24:37")], lambda w, h: A.eleven_meat("el1", w, h, 2436), "#6A5A4A", head="Peace Be unto You", art_h=240),
        F([N("24:38", "said unto them,"), sy("24:39")], JESUS_RISEN, bg=RISEN_LIGHT),
        D([cp("24:40"), N("24:41", "he said unto them,"), cp("24:42"), cp("24:43")], lambda w, h: A.eleven_meat("el2", w, h, 2440), "#6A5A4A"),
        F([N("24:44", "said unto them,")], JESUS_RISEN, bg=RISEN_LIGHT, head="Ye Are Witnesses"),
        F([cp("24:45"), N("24:46", "said unto them,"), sy("24:47"), sy("24:48"), sy("24:49")], JESUS_RISEN, bg=RISEN_LIGHT),
        D([cp("24:50")], lambda w, h: A.bethany_bless("bb1", w, h, 2450), "#5A8AC8", head="He Was Carried Up into Heaven", art_h=260),
        D([cp("24:51")], lambda w, h: A.received_up("ru1", w, h, 2451), "#2A3A7A", art_h=280),
        D([cp("24:52"), cp("24:53")], lambda w, h: A.temple_joy("tj1", w, h, 2452), "#8FD0E2", art_h=300)]
PG.extend(K.pack(SEGS, "LUK-C17-D", PG.next(), most=4, lone=0.5, end=fin("END OF LUKE · NEXT · JOHN")))
