import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from rev import G
from oba.minor import cover_page
from rev import art as K

def cover():
    """The holy city, new Jerusalem, coming down out of heaven from God (21:2, 21:10): the city foursquare in light over the
    new earth, its gates of pearl and its wall of jasper, the light breaking round it (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#1A1440"></rect>'
             f'<g transform="translate(0 300)">{K.cover_city(760, 780, 6601)}</g>')
    return cover_page("Revelation", "Volume Sixty-Six", 66, "Chapters 1 – 22", "ヨハネの黙示録", "YOHANE NO MOKUSHIROKU",
                      G.v("21:5", frm="Behold, I make all things new."), scene, bg="#1A1440", band="26,20,64")
