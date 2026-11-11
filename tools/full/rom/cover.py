import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from rom import G
from oba.minor import cover_page
from rom import art as A

def cover():
    """The letter come to Rome: the city on its hills at sunrise (Acts' Rome), and in the foreground, on a stone parapet, the
    scroll tied and sealed (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A1E3A"></rect>'
             f'<g transform="translate(0 300)">{A.rome("cv", 760, 680, 4501)}</g>'
             f'<rect x="0" y="300" width="760" height="680" fill="#FF9A4A" opacity="0.16"></rect>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(420, 908, 2.3, rot=-7))
    return cover_page("Romans", "Volume Forty-Five", 45, "Chapters 1 – 16", "ローマ人への手紙", "RŌMAJIN E NO TEGAMI",
                      G.v("1:7", frm="Grace to you and peace"), scene, bg="#2A1E3A", band="42,30,58")
