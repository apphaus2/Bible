def f(v): return f"{v:.1f}"
FAT = "M0 20 C 0 6 12 0 24 2 L 30 -6 L 34 2 C 60 -6 98 -4 114 10 C 122 16 124 28 120 40 L 118 66 L 110 66 L 108 46 L 34 48 L 30 68 L 22 68 L 22 46 C 14 42 6 36 2 28 Z"
LEAN = "M0 20 C 0 8 10 2 22 4 L 28 -4 L 32 4 C 56 6 88 8 106 14 C 112 20 112 26 108 30 L 110 72 L 105 72 L 100 34 L 38 34 L 32 74 L 27 74 L 27 32 C 16 30 6 28 2 26 Z"
RIBS = "M50 12 L 52 30 M60 12 L 62 30 M70 13 L 72 30 M80 14 L 82 30"
SHEAF = "M-14 0 L -4 -40 L -2 -40 L -8 0 Z M-4 0 L -1 -46 L 1 -46 L 4 0 Z M8 0 L 2 -40 L 4 -40 L 14 0 Z M-10 -28 L 10 -28 L 10 -22 L -10 -22 Z"
def pyramid(cx, by, w, h, lit="#E8C88A", dark="#B5652E", line="#8A5A3E", n=10):
    o = [f'<path d="M{f(cx-w/2)} {f(by)} L{f(cx)} {f(by-h)} L{f(cx+w*0.12)} {f(by)} Z" fill="{lit}" stroke="#0D0D0F" stroke-width="1.6"></path>',
         f'<path d="M{f(cx+w*0.12)} {f(by)} L{f(cx)} {f(by-h)} L{f(cx+w/2)} {f(by)} Z" fill="{dark}" stroke="#0D0D0F" stroke-width="1.6"></path>']
    for i in range(1, n):
        t = i / n; y = by - h * t; xl = cx - w/2 * (1 - t); xr = cx + w/2 * (1 - t); xm = cx + w * 0.12 * (1 - t)
        o.append(f'<path d="M{f(xl)} {f(y)} L{f(xm)} {f(y)} L{f(xr)} {f(y)}" stroke="{line}" stroke-width="0.9" fill="none"></path>')
    return "\n".join(o)
def granaries(x0, by, n, w0, h0, shrink=0.88, gap=0.18, color="#D8B070", shade="#9A6A3A"):
    o = []; x = x0; w = w0; h = h0; y = by
    items = []
    for i in range(n):
        items.append((x, y, w, h)); x += w * (1 + gap); w *= shrink; h *= shrink; y -= h0 * 0.06
    for (x, y, w, h) in reversed(items):
        d = h * 0.55
        o.append(f'<path d="M{f(x)} {f(y)} L{f(x)} {f(y-h)} C {f(x)} {f(y-h-d)} {f(x+w)} {f(y-h-d)} {f(x+w)} {f(y-h)} L{f(x+w)} {f(y)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>')
        o.append(f'<path d="M{f(x+w*0.62)} {f(y)} L{f(x+w*0.62)} {f(y-h)} C {f(x+w*0.7)} {f(y-h-d*0.9)} {f(x+w)} {f(y-h-d*0.5)} {f(x+w)} {f(y-h)} L{f(x+w)} {f(y)} Z" fill="{shade}" opacity="0.6"></path>')
        o.append(f'<path d="M{f(x+w*0.35)} {f(y)} L{f(x+w*0.35)} {f(y-h*0.3)} C {f(x+w*0.35)} {f(y-h*0.42)} {f(x+w*0.55)} {f(y-h*0.42)} {f(x+w*0.55)} {f(y-h*0.3)} L{f(x+w*0.55)} {f(y)} Z" fill="#2A140C"></path>')
        o.append(f'<path d="M{f(x+w*0.1)} {f(y-h*0.7)} L{f(x+w*0.9)} {f(y-h*0.7)}" stroke="#0D0D0F" stroke-width="0.8" opacity="0.6"></path>')
    return "\n".join(o)
