import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pe1 import G
from oba.minor import cover_page
from jas import art as A
from act.art16 import rome

def cover():
    """The letter sent out from Babylon: Rome on its hills by day (Acts' drawing — the temples on the Capitol, the red roofs,
    the aqueduct), and in the foreground, on a stone parapet, the scroll tied and sealed for the sojourners of the Dispersion
    (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A1E3A"></rect>'
             f'<g transform="translate(0 330)">{rome("cv", 760, 640, 6000)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(420, 908, 2.3, rot=-7))
    return cover_page("1 Peter", "Volume Sixty", 60, "Chapters 1 – 5", "ペテロの第一の手紙", "PETERO NO DAIICHI NO TEGAMI",
                      G.v("2:9", to="a royal priesthood"), scene, bg="#2A1E3A", band="42,30,58")
