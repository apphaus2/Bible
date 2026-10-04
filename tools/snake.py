import math
def catmull(P, n=24):
    pts=[]
    P=[P[0]]+P+[P[-1]]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        for k in range(n):
            t=k/n; t2=t*t; t3=t2*t
            x=0.5*((2*p1[0])+(-p0[0]+p2[0])*t+(2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*t2+(-p0[0]+3*p1[0]-3*p2[0]+p3[0])*t3)
            y=0.5*((2*p1[1])+(-p0[1]+p2[1])*t+(2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*t2+(-p0[1]+3*p1[1]-3*p2[1]+p3[1])*t3)
            pts.append((x,y))
    pts.append(P[-2]); return pts
def width(s, wmax):
    # tail -> body -> neck
    if s<0.35: return 1.2+(wmax-1.2)*(s/0.35)**0.8
    if s<0.78: return wmax
    if s<0.93: return wmax-(wmax*0.28)*((s-0.78)/0.15)
    return wmax*0.72+(wmax*0.12)*((s-0.93)/0.07)
def f(v): return f"{v:.1f}"
def snake(P, wmax, uid, head_scale=1.0):
    pts=catmull(P)
    L=[0]
    for a,b in zip(pts,pts[1:]): L.append(L[-1]+math.dist(a,b))
    tot=L[-1]
    left=[];right=[];mid_l=[];hl=[];belly_in=[]; norms=[]
    for i,(x,y) in enumerate(pts):
        a=pts[max(i-1,0)]; b=pts[min(i+1,len(pts)-1)]
        dx,dy=b[0]-a[0],b[1]-a[1]; d=math.hypot(dx,dy) or 1
        nx,ny=-dy/d,dx/d
        w=width(L[i]/tot,wmax)
        left.append((x+nx*w,y+ny*w)); right.append((x-nx*w,y-ny*w))
        mid_l.append((x+nx*w*0.15,y+ny*w*0.15)); hl.append((x+nx*w*0.55,y+ny*w*0.55))
        belly_in.append((x-nx*w*0.45,y-ny*w*0.45)); norms.append((nx,ny,w))
    poly=lambda A,B: "M"+" L".join(f"{f(x)} {f(y)}" for x,y in A)+" L"+" L".join(f"{f(x)} {f(y)}" for x,y in reversed(B))+" Z"
    line=lambda A: "M"+" L".join(f"{f(x)} {f(y)}" for x,y in A)
    body=poly(left,right)
    belly=poly(belly_in,right)
    shadow=poly(mid_l,right)
    # scutes across belly
    scutes=[]
    acc=0
    for i in range(1,len(pts)):
        acc+=math.dist(pts[i-1],pts[i])
        if acc>5.5:
            acc=0; bx,by=belly_in[i]; rx,ry=right[i]; scutes.append(f"M{f(bx)} {f(by)} L{f(rx)} {f(ry)}")
    # dorsal blotches
    blot=[]; acc=0
    for i in range(1,len(pts)):
        acc+=math.dist(pts[i-1],pts[i])
        s=L[i]/tot
        if acc>wmax*2.2 and 0.12<s<0.95:
            acc=0
            x,y=pts[i]; nx,ny,w=norms[i]
            cx,cy=x+nx*w*0.35,y+ny*w*0.35
            tx,ty=ny,-nx
            r=w*0.55
            pp=[(cx+tx*r,cy+ty*r),(cx+nx*r*0.75,cy+ny*r*0.75),(cx-tx*r,cy-ty*r),(cx-nx*r*0.75,cy-ny*r*0.75)]
            blot.append("M"+" L".join(f"{f(a)} {f(b)}" for a,b in pp)+" Z")
    ex,ey=pts[-1]; px,py=pts[-4]
    ang=math.degrees(math.atan2(ey-py,ex-px))
    out=f'''<defs>
        <clipPath id="{uid}Clip"><path d="{body}"></path></clipPath>
        <pattern id="{uid}Scale" width="7" height="5" patternUnits="userSpaceOnUse"><path d="M0 5 A 3.5 3.5 0 0 1 7 5 M-3.5 2.5 A 3.5 3.5 0 0 1 3.5 2.5 M3.5 2.5 A 3.5 3.5 0 0 1 10.5 2.5" fill="none" stroke="#1B3A12" stroke-width="0.7"></path></pattern>
      </defs>
      <path d="{body}" fill="#5E8F26"></path>
      <g clip-path="url(#{uid}Clip)">
        <rect x="-50" y="-50" width="900" height="500" fill="url(#{uid}Scale)" opacity="0.55"></rect>
        <path d="{shadow}" fill="#1B3A12" opacity="0.45"></path>
        <path d="{"".join(blot)}" fill="#22401A" stroke="#C9E265" stroke-width="1"></path>
        <path d="{belly}" fill="#E4DE9A"></path>
        <path d="{" ".join(scutes)}" stroke="#8A8A50" stroke-width="0.8"></path>
        <path d="{line(hl)}" fill="none" stroke="#D8F08A" stroke-width="{f(max(1,wmax*0.12))}" stroke-linecap="round" opacity="0.7"></path>
      </g>
      <path d="{body}" fill="none" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>
      <g transform="translate({f(ex)} {f(ey)}) rotate({f(ang)}) scale({head_scale} {head_scale*(-1 if abs(ang)>90 else 1)})">
        <path d="M-2 -15 C 10 -20 32 -19 46 -10 C 55 -5 57 2 51 7 C 41 13 20 15 -2 13 C -11 9 -11 -11 -2 -15 Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2" stroke-linejoin="round"></path>
        <path d="M-6 13 C 18 15 40 13 51 7 C 44 9 22 9 -6 6 Z" fill="#E4DE9A"></path>
        <path d="M4 7 C 20 9 38 8 50 5" fill="none" stroke="#0D0D0F" stroke-width="1.4"></path>
        <path d="M-2 -13 C 12 -16 28 -15 40 -9 C 30 -10 16 -10 2 -7 Z" fill="#22401A"></path>
        <path d="M22 -12 C 28 -15 36 -14 40 -10" fill="none" stroke="#0D0D0F" stroke-width="2.2" stroke-linecap="round"></path>
        <ellipse cx="31" cy="-6" rx="5" ry="4" fill="#FF4B3E" stroke="#0D0D0F" stroke-width="1.2"></ellipse>
        <ellipse cx="31" cy="-6" rx="1.2" ry="3.6" fill="#0D0D0F"></ellipse>
        <circle cx="29.5" cy="-7.5" r="0.9" fill="#ffffff"></circle>
        <circle cx="48" cy="-3" r="1.2" fill="#0D0D0F"></circle>
        <path d="M54 2 L 66 3 L 72 -2 M66 3 L 72 8" fill="none" stroke="#D7261E" stroke-width="1.8" stroke-linecap="round"></path>
      </g>'''
    return out
if __name__=="__main__":
    P=[(10,224),(70,212),(130,210),(165,226),(170,256),(190,268),(212,252),(220,222),(240,204),(268,210),(282,240),(300,264),(326,254),(334,226),(356,206),(400,204),(440,194),(470,168),(492,134),(520,110),(560,102),(596,114),(612,136),(604,156)]
    print(snake(P,15,"svSn",1.15))
