import sys, re, pathlib, random
import build3, ladder
def stars(n, w, h, seed):
    r = random.Random(seed)
    return '<g fill="#F3EFE6">' + "".join(f'<circle cx="{r.uniform(0,w):.0f}" cy="{r.uniform(0,h):.0f}" r="{r.choice([0.6,0.8,1,1.2,1.6])}"></circle>' for _ in range(n)) + "</g>"
def tokens():
    t = build3.tokens()
    t["__LADDER_COVER__"] = ladder.ladder(380, 1090, 300, 380, 120, 22, "lc", angels=[(3,-0.5,False),(6,0.4,True),(9,-0.3,False),(12,0.3,True),(15,-0.2,False)])
    t["__LADDER_P05__"] = ladder.ladder(420, 640, 260, 400, -20, 20, "l5", angels=[(2,-0.45,False),(5,0.4,True),(8,-0.3,False),(11,0.3,True),(14,0,False)])
    import faces
    t["__FACE_ESAU_ANGRY__"] = faces.face("adam", skin="#C47A5A", shadow="#5A1A16", hair="#B5421E", hl="#E06A3A", stubble="#B5421E", brow="scowl", light="#FF6A4A")
    t["__BOW__"] = "M-46 0 C -46 -26 -28 -46 0 -48 C 22 -50 40 -38 46 -20 L 56 -10 C 62 -6 64 -2 58 0 Z M38 -24 A 11 11 0 1 0 60 -24 A 11 11 0 1 0 38 -24 Z"
    t["__STARS_B4C__"] = stars(160, 760, 700, 41)
    t["__STARS_B4P5__"] = stars(140, 702, 520, 45)
    return t
if __name__ == "__main__":
    t = tokens()
    for p in sys.argv[1:]:
        s = pathlib.Path(p).read_text()
        for k, v in t.items(): s = s.replace(k, v)
        left = re.findall(r"__[A-Z0-9_]+__", s); assert not left, (p, left)
        pathlib.Path(p).write_text(s)
