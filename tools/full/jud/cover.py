import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jud import G
from oba.minor import cover_page
from jud import art as A

def cover():
    """The faith once for all delivered: the hills of Judæa under a night sky full of stars, and in the foreground on a stone
    parapet the scroll tied and sealed beside a burning lamp (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect>'
             + A.starfield(760, 900, 6500, 120, 0.7) + A.halo(560, 520, 300, "#FFF4C2", 0.25)
             + A.hills(760, 1080, 760, 6500, color="#2A2440", amp=30, step=120) + A.hills(760, 1080, 840, 6501, color="#3A3050", amp=20, step=90)
             + f'<rect x="-10" y="930" width="780" height="160" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#4A3A3A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#4A3A3A" stroke-width="2"></path>'
             + A.lamp_glow(170, 900, 220, "cvj", op=0.6) + A.clay_lamp(170, 928, 2.2)
             + A.sealed_scroll(450, 908, 2.3, rot=-7))
    return cover_page("Jude", "Volume Sixty-Five", 65, "Verses 1 – 25", "ユダの手紙", "YUDA NO TEGAMI",
                      G.v("1:3", frm="contend earnestly", to="unto the saints."), scene, bg="#0B0B2A", band="11,11,42")
