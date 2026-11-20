import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from col import G
from oba.minor import cover_page
from col import art as A

def cover():
    """The letter come to Colossæ: the valley of the Lycus in the morning, Mount Cadmus with snow on its top, Colossæ at its
    foot, Laodicea and Hierapolis across the plain; and in the foreground, on a stone parapet, the scroll tied and sealed
    (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#3A5A7A"></rect>'
             f'<g transform="translate(0 300)">{A.lycus_valley("cv", 760, 680, 5101, names=False)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(420, 908, 2.3, rot=-7))
    return cover_page("Colossians", "Volume Fifty-One", 51, "Chapters 1 – 4", "コロサイ人への手紙", "KOROSAIJIN E NO TEGAMI",
                      G.v("3:2", to="above,"), scene, bg="#3A5A7A", band="40,62,90")
