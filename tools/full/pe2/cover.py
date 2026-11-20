import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pe2 import G
from oba.minor import cover_page
from pe2 import art as A

def cover():
    """Until the day dawn: the hills at first light, the day-star over them, and in the foreground on a stone parapet the
    clay lamp still burning beside the scroll tied and sealed (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#14183A"></rect>'
             f'<g transform="translate(0 300)">{A.lamp_daystar(760, 640, 6100).split("<path d=\"M-10 -10 L")[0]}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#4A3A3A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#4A3A3A" stroke-width="2"></path>'
             + A.lamp_glow(170, 900, 220, "cvl", op=0.6) + A.clay_lamp(170, 928, 2.2)
             + A.sealed_scroll(450, 908, 2.3, rot=-7))
    return cover_page("2 Peter", "Volume Sixty-One", 61, "Chapters 1 – 3", "ペテロの第二の手紙", "PETERO NO DAINI NO TEGAMI",
                      G.v("1:19", frm="as unto a lamp", to="until the day dawn"), scene, bg="#14183A", band="20,24,58")
