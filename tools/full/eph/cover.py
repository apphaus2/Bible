import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from eph import G
from oba.minor import cover_page
from eph import art as A

def cover():
    """The letter come from Rome: Ephesus at dawn — the theatre cut into the hill, the roofs, the temple of Diana far off on
    the plain — and in the foreground, on a stone parapet, the scroll tied and sealed, and beside it the iron chain of the
    prisoner who sent it (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A1E3A"></rect>'
             f'<g transform="translate(0 300)">{A.ephesus_dawn(760, 680, 4901)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.chain(250, 942, 640, 930, s=2.0, sag=0.04)
             + A.sealed_scroll(440, 906, 2.3, rot=-7))
    return cover_page("Ephesians", "Volume Forty-Nine", 49, "Chapters 1 – 6", "エペソ人への手紙", "EPESOJIN E NO TEGAMI",
                      G.v("2:8", to="through faith;"), scene, bg="#2A1E3A", band="42,30,58")
