"""Deuteronomy volume, Chapter 5 — The Tables of Stone (Deuteronomy 9–10). Every verse, word for word from ref/asv.
Not for thy righteousness: the golden calf remembered (the calf, the tables broken, the calf ground to dust), Moses fallen
down forty days and forty nights, the new tables hewn and laid in the ark, the Levites set apart (an aside), and what
doth Jehovah thy God require of thee."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V, joshua1 as J, numbers1 as N
from fx import chapter_title, end_mark
from discourse import seg, pack
from deu import G, art as K, art2 as K2, art3 as K3
from deu.common import auto, say, gd, cp, says, gods, caps, MOODS
from exo import art10 as A10
from num.art import ALL
from num.pages import Pages
from genesis.art2 import ground
from genesis import art as X
from genesis.ch02 import NIGHT
from genesis.ch04 import COLD
from deu import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
M, MS, MG = MOODS["calm"], MOODS["stern"], MOODS["grief"]

def calf(w, h):
    return f'<rect x="0" y="0" width="{w}" height="{h}" fill="#2A1A1A"></rect>' + V.rays(w * 0.5, h * 0.5, 30, 20, w, color="#FFC14D", op=0.15) + ground(w, h, h * 0.8, "#4A3A2A", dy=0) + V.calf(w * 0.5, h * 0.8, min(1.4, h / 220), uid=f"cf{h}")
def broken(w, h):
    return f'<rect x="0" y="0" width="{w}" height="{h}" fill="#2A1A1A"></rect>' + ground(w, h, h * 0.8, "#4A3A2A", dy=0) + V.shards(w * 0.5, h * 0.82, min(1.6, h / 200), 5)
def fallen(w, h):
    return f'<rect x="0" y="0" width="{w}" height="{h}" fill="#1A1430"></rect>' + V.rays(w * 0.5, 0, 30, 20, h * 1.2, color="#FFF4C2", op=0.18) + ground(w, h, h * 0.78, "#3A2A3A", dy=0) + N.prostrate(w * 0.5, h * 0.82, min(1.6, h / 200), color="#7A5A3A", skin="#C98E66")
def ark(w, h):
    return f'<rect x="0" y="0" width="{w}" height="{h}" fill="#1A0E1E"></rect>' + V.rays(w * 0.5, h * 0.5, 36, 30, w, color="#FFD23F", op=0.2) + J.ark(w * 0.5, h * 0.86, min(1.4, h / 220), uid=f"ak{h}", glow=True)


@P("DEU-C05-00-Title", "Chapter 5 · The Tables of Stone", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A0E1E"></rect>' + f'<g transform="translate(0 380)">{K3.tables(760, 700, 501)}</g>'
    return chapter_title(5, "第五話", "The Tables of Stone", "Deuteronomy 9 – 10", svg, "#1A0E1E", v("10:12", frm="what doth Jehovah thy God require of thee,", to="all thy soul,"), "Deuteronomy · Volume Five")


SEGS = (auto(9, 1, 6, ("calm", "stern"), head="Not for Thy Righteousness", stamp=9, arts=[("#3A2A3A", lambda w, h: K.giants(w, h, 511))], every=2)
        + [seg([says("9:7-11")], "DEUT 9:7–11", tok=MS[0], bg=MS[1], head="Also in Horeb Ye Provoked Jehovah"),
           seg([say("9:12", to="said unto me,"), gd("9:12", frm="Arise,"), say("9:13", to="saying,"), gd("9:13", frm="I have seen"), gd("9:14")], "DEUT 9:12–14", tok=MG[0], bg=MG[1]),
           seg([says("9:15-16")], "DEUT 9:15–16", art=calf, bg="#2A1A1A"),
           seg([say("9:17")], "DEUT 9:17", art=broken, bg="#2A1A1A", hi=19),
           seg([says("9:18-21")], "DEUT 9:18–21", tok=MG[0], bg=MG[1], head="Forty Days and Forty Nights"),
           seg([says("9:22-24")], "DEUT 9:22–24", tok=MS[0], bg=MS[1]),
           seg([says("9:25"), say("9:26", to="and said,"), ("say", v("9:26", frm="O Lord Jehovah,") + " " + sp("9:27-29"))], "DEUT 9:25–29", art=fallen, bg="#1A1430"),
           seg([say("10:1", to="said unto me,"), gd("10:1", frm="Hew thee"), gd("10:2"), says("10:3-5")], "DEUT 10:1–5", tok=M[0], bg=M[1], head="Hew Thee Two Tables of Stone", stamp=10),
           seg(None, "DEUT 10:5", art=ark, bg="#1A0E1E", h=230),
           seg([caps("10:6-9")], "DEUT 10:6–9", art=lambda w, h: K.address("af10", w, h, 512), bg="#F3D8A0"),
           seg([say("10:10"), say("10:11", to="said unto me,"), gd("10:11", frm="Arise,")], "DEUT 10:10–11", tok=M[0], bg=M[1])]
        + auto(10, 12, 22, ("calm", "fire", "calm"), head="What Doth Jehovah Thy God Require of Thee", arts=[("#0B0B2A", lambda w, h: X.cosmic(w, h))], every=3))
PG.extend(pack(SEGS, "DEU-C05-D", PG.next(), end=end_mark("NEXT · THE PLACE WHICH JEHOVAH SHALL CHOOSE", "right: 10px; top: 10px")))
