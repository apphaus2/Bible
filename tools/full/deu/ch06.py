"""Deuteronomy volume, Chapter 6 — The Place of His Name (Deuteronomy 11–12). Every verse, word for word
from ref/asv. Deuteronomy 11 in speech panels (the rain in its season, the words in your heart, Gerizim and Ebal); then the
statutes begin: Deuteronomy 12 as spoken law cells (exo.kit.law_pages, spoken=True; pictograms picked by picto.pick)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from discourse import seg, pack
from exo.kit import law_pages, set_book
from deu import G, art as K, art3 as K3
from deu.common import shade, auto, codify
from num.pages import Pages
from genesis.ch02 import SKY
from deu import ch05 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("DEU-C06-00-Title", "Chapter 6 · The Place of His Name", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect>' + f'<g transform="translate(0 380)">{K.gerizim_ebal(760, 700, 601)}</g>')
    return chapter_title(6, "第六話", "The Place of His Name", "Deuteronomy 11 – 12", svg, "#F3D8A0", v("11:26"), "Deuteronomy · Volume Five")


RAIN = ("#5A6E8A", lambda w, h: K.rain(w, h, 611))
DRY = ("#E8B880", lambda w, h: K.rain(w, h, 612, shut=True))
SEGS = (auto(11, 1, 9, ("calm", "fire"), head="Know Ye This Day", stamp=11, arts=[("#F3D8A0", lambda w, h: K.address("a11", w, h, 613))])
        + auto(11, 10, 17, ("calm",), head="A Land Which Jehovah Thy God Careth For", arts=[RAIN, DRY], every=2)
        + auto(11, 18, 25, ("calm", "fire"), head="Lay Up These My Words", arts=[(SKY, lambda w, h: K3.doorposts("d11", w, h, 614))])
        + [seg(None, "DEUT 11:29", art=lambda w, h: K.gerizim_ebal(w, h, 615), bg="#F3D8A0", h=280, head="A Blessing and a Curse")]
        + auto(11, 26, 32, ("stern", "calm")))
PG.extend(pack(SEGS, "DEU-C06-D", PG.next()))
PG.extend(law_pages(codify(12, 1, 14, head="The Place Which Jehovah Shall Choose") + codify(12, 15, 28, head="Within All Thy Gates") + codify(12, 29, 32, head="Take Heed to Thyself"),
                    "DEU-C06-L", PG.next(), "The Place Which Jehovah Shall Choose", title_book="Deuteronomy", carry=True, spoken=True,
                    end=end_mark("NEXT · THE YEAR OF RELEASE", "right: 10px; top: 10px")))
