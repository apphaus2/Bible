"""Deuteronomy volume, Chapter 12 — The Blessings and the Curses (Deuteronomy 27–28). Every verse, word for word from
ref/eng-asv. The great stones written with the law and the altar of unhewn stones on mount Ebal; the tribes on Gerizim and on
Ebal; the twelve curses with all the people's Amen as law cells; then Moses' blessings and curses in speech panels over
the land — rain and harvest, then drought, the scattering and the city besieged (28:53–57 are words only: nothing of the
siege's horror is drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from discourse import seg, pack
from exo.kit import law_pages, set_book
from deu import G, art as K, art2 as K2
from deu.common import shade, auto, codify, says, cp, say
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import SKY
from deu import ch11 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
STONES = ("#E8C8A0", lambda w, h: K.stones_written(w, h, 1211))
MOUNTS = ("#F3D8A0", lambda w, h: K.gerizim_ebal(w, h, 1212))
RAIN = ("#5A6E8A", lambda w, h: K.rain(w, h, 1213))
DRY = ("#E8B880", lambda w, h: K.rain(w, h, 1214, shut=True))
SCATTER = ("#2A2A3A", lambda w, h: K2.scattered(w, h, 1215))
SIEGE = ("#3A1A1A", lambda w, h: K.city_siege(w, h, 1216))
NIGHTA = ("#0B0B2A", lambda w, h: X.cosmic(w, h))


@P("DEU-C12-00-Title", "Chapter 12 · The Blessings and the Curses", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect>' + f'<g transform="translate(0 400)">{K.gerizim_ebal(760, 680, 1201)}</g>')
    return chapter_title(12, "第十二話", "The Blessings and the Curses", "Deuteronomy 27 – 28", svg, "#F3D8A0", v("28:6"), "Deuteronomy · Volume Five")


SEGS = (auto(27, 1, 8, ("calm",), head="Great Stones, and Plaster Them with Plaster", stamp=27, arts=[STONES], every=2)
        + [seg([says("27:9-10"), say("27:11"), says("27:12-14")], "DEUT 27:9–14", tok=K.MOSES_CALM, bg="#F3D8A0", head="These Shall Stand upon Mount Gerizim"),
           seg(None, "DEUT 27:12–13", art=MOUNTS[1], bg=MOUNTS[0], h=260)])
PG.extend(pack(SEGS, "DEU-C12-D", PG.next()))
PG.extend(law_pages(codify(27, 15, 26, head="And All the People Shall Say, Amen", budget=200), "DEU-C12-L", PG.next(), "And All the People Shall Say, Amen",
                    title_book="Deuteronomy", carry=True, spoken=True))
SEGS2 = (auto(28, 1, 14, ("calm", "fire"), head="All These Blessings Shall Come upon Thee", stamp=28, arts=[RAIN, MOUNTS], every=2)
         + auto(28, 15, 35, ("stern", "grief"), head="All These Curses Shall Come upon Thee", arts=[DRY, NIGHTA], every=3)
         + auto(28, 36, 52, ("stern", "grief"), head="A Nation of Fierce Countenance", arts=[SCATTER, SIEGE], every=3)
         + auto(28, 53, 68, ("grief", "stern"), head="In the Siege and in the Distress", arts=[SIEGE, SCATTER], every=3))
PG.extend(pack(SEGS2, "DEU-C12-E", PG.next(), end=end_mark("NEXT · CHOOSE LIFE", "right: 10px; top: 10px")))
