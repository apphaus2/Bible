import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1] / "kit"))  # shared drawing kit
import sys, random, re, pathlib
import faces, tower
ROBE = "M-26 -166 C -36 -150 -40 -110 -40 -60 C -40 -30 -36 -10 -30 0 L 30 0 C 36 -10 40 -30 40 -60 C 40 -110 36 -150 26 -166 C 14 -172 -14 -172 -26 -166 Z"
def stars(n, w, h, seed, uid):
    r = random.Random(seed); out = []
    for _ in range(n):
        x, y = r.uniform(0, w), r.uniform(0, h); s = r.choice([0.6,0.8,1,1,1.2,1.6,2.2])
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{s}"></circle>')
    return f'<g fill="#F3EFE6">{"".join(out)}</g>'
def tokens():
    t = faces.tokens()
    t["__ROBE__"] = ROBE
    t["__TOWER_COVER__"] = tower.tower(470, 960, 560, 66, 12, 0.86, "tc", unfinished=2)
    t["__TOWER_P01__"] = tower.tower(480, 404, 380, 34, 10, 0.85, "t1", unfinished=3)
    t["__TOWER_P02__"] = tower.tower(351, 504, 440, 38, 11, 0.86, "t2", unfinished=2)
    t["__STARS_P04__"] = stars(260, 702, 614, 7, "s4")
    t["__STARS_P08__"] = stars(90, 345, 404, 9, "s8")
    return t
if __name__ == "__main__":
    t = tokens()
    for p in sys.argv[1:]:
        s = pathlib.Path(p).read_text()
        for k, v in t.items(): s = s.replace(k, v)
        left = re.findall(r"__[A-Z0-9_]+__", s); assert not left, (p, left)
        pathlib.Path(p).write_text(s)
