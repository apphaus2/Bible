import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from co2 import G
from oba.minor import cover_page
from co2 import art as A

def cover():
    """The treasure in earthen vessels: Corinth's citadel on its rock at dusk behind, and in the foreground, on a stone
    parapet beside the sealed letter, the clay jar with the light shining out of it (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#1E1430"></rect>'
             f'<g transform="translate(0 300)">{A.corinth_dusk(760, 680, 4701)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#6A5A54" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#4A3E3A" stroke-width="2"></path>' for x in range(60, 760, 140))
             + '<path d="M-10 958 L 770 958" stroke="#4A3E3A" stroke-width="2"></path>'
             + A.sealed_scroll(230, 912, 1.7, rot=-8) + A.jar(520, 932, 1.55, "cvjar"))
    return cover_page("2 Corinthians", "Volume Forty-Seven", 47, "Chapters 1 – 13", "コリント人への第二の手紙", "KORINTOJIN E NO DAINI NO TEGAMI",
                      G.v("4:7", frm="we have this treasure", to="from ourselves;"), scene, bg="#1E1430", band="30,20,48")
