import math
def f(v): return f"{v:.1f}"
def tower(cx, base_y, base_w, tier_h, n, shrink, uid, unfinished=2, light="#E8A35A", dark="#7A3E22", brick="#B5652E"):
    out=[f'''<defs>
  <pattern id="{uid}Brick" width="12" height="6" patternUnits="userSpaceOnUse"><rect width="12" height="6" fill="{brick}"></rect><path d="M0 0 L 12 0 M6 0 L 6 3 M0 3 L 12 3 M0 3 L 0 6 M12 3 L 12 6" stroke="{dark}" stroke-width="0.7"></path></pattern>
  <pattern id="{uid}Arch" width="16" height="14" patternUnits="userSpaceOnUse"><path d="M4 14 L 4 6 A 4 4 0 0 1 12 6 L 12 14 Z" fill="#2A140C"></path></pattern>
</defs>''']
    w=base_w; y=base_y
    for i in range(n):
        w2=w*shrink; top=y-tier_h
        built = i < n-unfinished
        poly=f"M{f(cx-w/2)} {f(y)} L{f(cx+w/2)} {f(y)} L{f(cx+w/2-3)} {f(top)} L{f(cx-w/2+3)} {f(top)} Z"
        if built:
            out.append(f'<path d="{poly}" fill="url(#{uid}Brick)" stroke="#0D0D0F" stroke-width="1.6"></path>')
            out.append(f'<path d="M{f(cx+w*0.18)} {f(y)} L{f(cx+w/2)} {f(y)} L{f(cx+w/2-3)} {f(top)} L{f(cx+w*0.18)} {f(top)} Z" fill="{dark}" opacity="0.55"></path>')
            out.append(f'<path d="M{f(cx-w/2+4)} {f(top+3)} L{f(cx-w*0.25)} {f(top+3)}" stroke="{light}" stroke-width="2" opacity="0.8"></path>')
            ah=min(14,tier_h*0.45)
            out.append(f'<rect x="{f(cx-w/2+8)}" y="{f(y-tier_h*0.62)}" width="{f(w-16)}" height="{f(ah)}" fill="url(#{uid}Arch)" opacity="0.9"></rect>')
            # ramp
            if i%2==0: rp=f"M{f(cx-w/2)} {f(y)} L{f(cx-w/2+10)} {f(y)} L{f(cx+w/2)} {f(top+4)} L{f(cx+w/2)} {f(top)} Z"
            else: rp=f"M{f(cx+w/2)} {f(y)} L{f(cx+w/2-10)} {f(y)} L{f(cx-w/2)} {f(top+4)} L{f(cx-w/2)} {f(top)} Z"
            out.append(f'<path d="{rp}" fill="{light}" stroke="#0D0D0F" stroke-width="1" opacity="0.9"></path>')
        else:
            out.append(f'<path d="{poly}" fill="none" stroke="#3A2214" stroke-width="1.2"></path>')
            k=int(w//14)
            for j in range(k+1):
                x=cx-w/2+3+j*(w-6)/max(k,1)
                out.append(f'<path d="M{f(x)} {f(y)} L{f(x)} {f(top-6)}" stroke="#3A2214" stroke-width="1.4"></path>')
            out.append(f'<path d="M{f(cx-w/2)} {f(y-tier_h/2)} L{f(cx+w/2)} {f(y-tier_h/2)} M{f(cx-w/2)} {f(y)} L{f(cx+w/2)} {f(top)}" stroke="#3A2214" stroke-width="1"></path>')
        w=w2; y=top
    # crane on top
    out.append(f'<path d="M{f(cx+w*0.3)} {f(y+tier_h)} L{f(cx+w*0.3)} {f(y-tier_h*1.6)} L{f(cx-w*1.2)} {f(y-tier_h*1.2)} M{f(cx+w*0.3)} {f(y-tier_h*1.6)} L{f(cx+w*0.9)} {f(y-tier_h*1.0)} M{f(cx-w*1.0)} {f(y-tier_h*1.25)} L{f(cx-w*1.0)} {f(y-tier_h*0.2)}" fill="none" stroke="#2A140C" stroke-width="2"></path>')
    out.append(f'<rect x="{f(cx-w*1.0-4)}" y="{f(y-tier_h*0.2)}" width="8" height="6" fill="{brick}" stroke="#0D0D0F" stroke-width="0.8"></rect>')
    return "\n".join(out)
