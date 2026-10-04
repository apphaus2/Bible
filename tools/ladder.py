import json, pathlib
FIG = json.loads((pathlib.Path(__file__).parent / "figures.json").read_text())
ROBE = "M-26 -166 C -36 -150 -40 -110 -40 -60 C -40 -30 -36 -10 -30 0 L 30 0 C 36 -10 40 -30 40 -60 C 40 -110 36 -150 26 -166 C 14 -172 -14 -172 -26 -166 Z"
WING = "M-14 -150 C -40 -190 -70 -200 -96 -196 C -74 -180 -60 -160 -54 -130 C -70 -130 -84 -120 -92 -108 C -64 -110 -40 -116 -20 -128 Z"
def f(v): return f"{v:.1f}"
def ladder(cx, y0, w, vx, vy, n, uid, angels=(), ratio=0.86):
    L = lambda t: (cx - w/2 + (vx - 4 - (cx - w/2)) * t, y0 + (vy - y0) * t)
    R = lambda t: (cx + w/2 + (vx + 4 - (cx + w/2)) * t, y0 + (vy - y0) * t)
    out = [f'''<defs>
  <linearGradient id="{uid}Glow" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FFE680" stop-opacity="0.15"></stop><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.95"></stop></linearGradient>
  <path id="{uid}Man" d="{FIG['MAN']}"></path><path id="{uid}Robe" d="{ROBE}"></path><path id="{uid}Wing" d="{WING}"></path>
</defs>''']
    l0, r0, l1, r1 = L(0), R(0), L(1), R(1)
    out.append(f'<path d="M{f(l0[0]-40)} {f(l0[1])} L{f(r0[0]+40)} {f(r0[1])} L{f(r1[0]+30)} {f(r1[1])} L{f(l1[0]-30)} {f(l1[1])} Z" fill="url(#{uid}Glow)"></path>')
    ts = []; t = 0.0; step = 1.0
    gaps = [ratio ** k for k in range(n)]; tot = sum(gaps); acc = 0
    for g in gaps: acc += g; ts.append(acc / tot * 0.98)
    for i, t in enumerate(ts):
        a, b = L(t), R(t); sw = max(0.8, 7 * (1 - t))
        out.append(f'<path d="M{f(a[0])} {f(a[1])} L{f(b[0])} {f(b[1])}" stroke="#FFF4C2" stroke-width="{f(sw)}" stroke-linecap="round"></path>')
    for side in (L, R):
        p0, p1 = side(0), side(1)
        out.append(f'<path d="M{f(p0[0])} {f(p0[1])} L{f(p1[0])} {f(p1[1])}" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round" opacity="0.95"></path>')
        out.append(f'<path d="M{f(p0[0])} {f(p0[1])} L{f(p1[0])} {f(p1[1])}" stroke="#C8A06A" stroke-width="1.4" opacity="0.8"></path>')
    for k, (idx, dx, flip) in enumerate(angels):
        t = ts[idx]; a, b = L(t), R(t); x = (a[0] + b[0]) / 2 + dx * (b[0] - a[0]) / 2; y = a[1]
        s = 0.62 * (1 - t) + 0.05
        sc = f"{f(-s)} {f(s)}" if flip else f"{f(s)} {f(s)}"
        out.append(f'''<g transform="translate({f(x)} {f(y)}) scale({sc})" stroke="#FFD23F" stroke-width="3">
  <use href="#{uid}Wing" fill="#FFFFFF" opacity="0.92"></use><use href="#{uid}Wing" fill="#FFFFFF" opacity="0.92" transform="scale(-1 1)"></use>
  <use href="#{uid}Man" fill="#FFFDF2"></use><use href="#{uid}Robe" fill="#FFFDF2"></use></g>''')
    return "\n".join(out)
