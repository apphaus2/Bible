import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jn2 import G
from oba.minor import cover_page
from jn2 import art as A

def cover():
    """The elect lady's house at evening: the street of white houses, her door open on the lamplit room, and in the
    foreground, on a stone parapet, the elder's letter tied and sealed (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A1E3A"></rect>'
             f'<g transform="translate(0 280)">{A.evening_street(760, 700, 6301)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(420, 908, 2.3, rot=-7))
    return cover_page("2 John", "Volume Sixty-Three", 63, "Chapter 1", "ヨハネの第二の手紙", "YOHANE NO DAINI NO TEGAMI",
                      G.v("1:4", to="walking in truth,"), scene, bg="#2A1E3A", band="42,30,58")
