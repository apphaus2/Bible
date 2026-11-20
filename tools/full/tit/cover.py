import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from tit import G
from oba.minor import cover_page
from tit import art as A

def cover():
    """The letter come to Crete: dawn over the sea of Crete, the sun rising behind the island's long ridge, and in the
    foreground, on a stone parapet above the shore, the scroll tied and sealed (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A5A"></rect>'
             f'<g transform="translate(0 300)">{A.crete_dawn(760, 680, 5602)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(420, 908, 2.3, rot=-7))
    return cover_page("Titus", "Volume Fifty-Six", 56, "Chapters 1 – 3", "テトスへの手紙", "TETOSU E NO TEGAMI",
                      G.v("2:11", to="appeared,"), scene, bg="#2A2A5A", band="42,42,90")
