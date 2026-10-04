import sys, re, pathlib
import build4, egypt
def tokens():
    t = build4.tokens()
    t["__FAT__"] = egypt.FAT; t["__LEAN__"] = egypt.LEAN; t["__RIBS__"] = egypt.RIBS; t["__SHEAF__"] = egypt.SHEAF
    t["__PYRAMIDS_COVER__"] = egypt.pyramid(520, 820, 520, 330) + egypt.pyramid(250, 830, 300, 190) + egypt.pyramid(700, 840, 220, 140)
    t["__PYRAMIDS_P04__"] = egypt.pyramid(470, 220, 260, 150, n=8) + egypt.pyramid(640, 226, 160, 96, n=6)
    t["__GRANARIES_P07__"] = egypt.granaries(20, 400, 9, 120, 160, shrink=0.86)
    t["__PYRAMIDS_P06__"] = egypt.pyramid(110, 330, 200, 120, n=7) + egypt.pyramid(600, 330, 220, 130, n=7)
    return t
if __name__ == "__main__":
    t = tokens()
    for p in sys.argv[1:]:
        s = pathlib.Path(p).read_text()
        for k, v in t.items(): s = s.replace(k, v)
        left = re.findall(r"__[A-Z0-9_]+__", s); assert not left, (p, left)
        pathlib.Path(p).write_text(s)
