import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from php import G
from oba.minor import cover_page
from php import art2 as A

def cover():
    """The letter come to Philippi: the Roman colony at sunrise, the arch over the Egnatian Way and the walls under the
    acropolis, the light of heaven opened over it; and in the foreground, on a stone parapet, the scroll tied and sealed
    (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A5A"></rect>'
             f'<g transform="translate(0 300)">{A.colony_gate("cv", 760, 680, 5001)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(440, 908, 2.3, rot=-7))
    return cover_page("Philippians", "Volume Fifty", 50, "Chapters 1 – 4", "ピリピ人への手紙", "PIRIPIJIN E NO TEGAMI",
                      G.v("1:21"), scene, bg="#2A2A5A", band="42,42,90")
