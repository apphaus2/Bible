import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jn3 import G
from oba.minor import cover_page
from jn3 import art as A

def cover():
    """Gaius' street in the morning: the white houses, his door open for the brethren and strangers, their staffs leaning on
    the wall beside it and a water jar at the door, and in the foreground, on a stone parapet, the elder's letter tied and
    sealed, the reed pen laid beside it (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A4A7A"></rect>'
             '<defs><linearGradient id="c3sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A4A7A"></stop><stop offset="1" stop-color="#6AA8D0"></stop></linearGradient></defs>'
             '<rect x="0" y="0" width="760" height="290" fill="url(#c3sky)"></rect>'
             f'<g transform="translate(0 280)">{A.evening_street(760, 700, 6401, tone="morning", staffs=3)}</g>'
             f'<rect x="-10" y="930" width="780" height="160" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + "".join(f'<path d="M{x} 930 L {x} 1090" stroke="#6A5A4A" stroke-width="2"></path>' for x in range(40, 760, 120))
             + '<path d="M-10 960 L 770 960" stroke="#6A5A4A" stroke-width="2"></path>'
             + A.sealed_scroll(400, 908, 2.3, rot=-7) + A.reed_pen(200, 935, 1.6, rot=-70))
    return cover_page("3 John", "Volume Sixty-Four", 64, "Chapter 1", "ヨハネの第三の手紙", "YOHANE NO DAISAN NO TEGAMI",
                      G.v("1:4"), scene, bg="#2A4A7A", band="42,74,122")
