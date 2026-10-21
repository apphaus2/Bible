import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from nam import G
from oba.minor import cover_page
from nam import art as K

def cover():
    """Nineveh's wall at night, its river gates burst and the flood pouring through (full-bleed)."""
    scene = f'<rect x="0" y="0" width="760" height="1080" fill="#1A1A2A"></rect><g transform="translate(0 300)">{K.river_gates(760, 780, 34)}</g>'
    return cover_page("Nahum", "Volume Thirty-Four", 34, "Chapters 1 – 3", "ナホム書", "NAHOMU-SHO", G.v("2:6"), scene, bg="#1A1A2A", band="26,26,42")
