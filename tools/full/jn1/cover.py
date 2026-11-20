import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jn1 import G
from oba.minor import cover_page
from jn1 import art as A

def cover():
    """The true light already shineth: dawn over Ephesus, the night drawing off, the sun coming up out of the sea, and in
    the foreground, on a stone parapet, the letter tied and sealed (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#1A1440"></rect>'
             f'<g transform="translate(0 260)">{A.dawn_ephesus(760, 720, 6201, sun_x=0.7)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(420, 908, 2.3, rot=-7))
    return cover_page("1 John", "Volume Sixty-Two", 62, "Chapters 1 – 5", "ヨハネの第一の手紙", "YOHANE NO DAIICHI NO TEGAMI",
                      G.v("1:5", frm="God is light"), scene, bg="#1A1440", band="26,20,64")
