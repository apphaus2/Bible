import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jas import G
from oba.minor import cover_page
from jas import art as A
from mat.art import jerusalem_far

def cover():
    """The letter sent out from Jerusalem: the city and the house of God at sunrise seen from the mount of Olives, and in the
    foreground, on a stone parapet, the scroll tied and sealed for the twelve tribes of the Dispersion (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A1E3A"></rect>'
             f'<g transform="translate(0 330)">{jerusalem_far(760, 640, 5900, tone="dawn")}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(420, 908, 2.3, rot=-7))
    return cover_page("James", "Volume Fifty-Nine", 59, "Chapters 1 – 5", "ヤコブの手紙", "YAKOBU NO TEGAMI",
                      G.v("1:22", to="not hearers only"), scene, bg="#2A1E3A", band="42,30,58")
