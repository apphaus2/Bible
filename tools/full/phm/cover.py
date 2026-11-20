import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from phm import G
from oba.minor import cover_page
from phm import art as A

def cover():
    """Onesimus come home: Philemon's house at Colossæ at evening, under snowy Mount Cadmus, the door standing open on the lit
    court, Apphia in the doorway and Philemon before it, and Onesimus holding out the sealed letter (full-bleed)."""
    scene = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A5A"></rect>'
             f'<g transform="translate(0 300)">{A.philemon_house("cv", 760, 780, 5701, stage="arrive")}</g>')
    return cover_page("Philemon", "Volume Fifty-Seven", 57, "Chapter 1", "ピレモンへの手紙", "PIREMON E NO TEGAMI",
                      G.v("1:16", to="a brother beloved,"), scene, bg="#2A2A5A", band="42,42,90")
