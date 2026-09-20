# -*- coding: utf-8 -*-
"""realistic-ish desk props for abstract vocabulary scenes"""
import subprocess,os
from PIL import Image
from gen import label,T,R,EN,ZH
W,H=1600,1000
DEFS='''<defs>
<filter id="sh" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".35"/></filter>
<filter id="sh2" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity=".3"/></filter>
<linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8b5e3c"/><stop offset="1" stop-color="#5c3a22"/></linearGradient>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef1f4"/><stop offset="1" stop-color="#d9dee4"/></linearGradient>
<linearGradient id="paper" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#f1f1ee"/></linearGradient>
<linearGradient id="screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#f3f6fa"/></linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9dde2"/><stop offset="1" stop-color="#9aa3ad"/></linearGradient>
<radialGradient id="vig" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></radialGradient>
</defs>'''
def desk(top=380):
    s=R(0,0,W,H,"url(#wall)")+R(0,top,W,H-top,"url(#wood)")
    for i in range(0,W,90): s+=f'<rect x="{i}" y="{top}" width="45" height="{H-top}" fill="#000" opacity=".05"/>'
    s+=R(0,top,W,6,"#3c2414",op=.6)
    return s
def vignette(): return R(0,0,W,H,"url(#vig)")
def paper(x,y,w,h,rot=0,fill="url(#paper)"):
    return f'<g transform="rotate({rot} {x+w/2} {y+h/2})" filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#cfcfca" stroke-width="1"/></g><g transform="rotate({rot} {x+w/2} {y+h/2})">'
def end(): return '</g>'
def lines(x,y,w,n,gap=14,color="#c9ccd1",h=6):
    return "".join(R(x,y+i*gap,w*(0.6+0.4*((i*7)%5)/4),h,color,rx=3) for i in range(n))
def stamp(x,y,text,color="#c0392b",rot=-12,size=22):
    return f'<g transform="rotate({rot} {x} {y})"><rect x="{x-60-len(text)*4}" y="{y-20}" width="{120+len(text)*8}" height="40" rx="6" fill="none" stroke="{color}" stroke-width="4" opacity=".85"/>'+T(x,y+8,text,size,color,anchor="middle")+'</g>'
def sticky(x,y,text,color="#fde68a",rot=-4,size=18,w=190,h=110):
    s=f'<g transform="rotate({rot} {x+w/2} {y+h/2})" filter="url(#sh2)"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/></g><g transform="rotate({rot} {x+w/2} {y+h/2})">'
    for i,ln in enumerate(text.split("\n")): s+=T(x+w/2,y+38+i*(size+6),ln,size,"#333",w="600",fam="Marker Felt, Chalkboard, "+EN)
    return s+'</g>'
def laptop(x,y,w,h):
    """screen area returns inner rect"""
    s=f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#2b2f36"/></g>'
    s+=R(x+14,y+14,w-28,h-28,"url(#screen)",rx=6)
    s+=f'<path d="M{x-40},{y+h} h{w+80} l-16,26 h{-(w+48)}z" fill="url(#metal)"/>'
    return s,(x+14,y+14,w-28,h-28)
def window(sx,sy,sw,sh,title,color="#3b82f6"):
    s=R(sx,sy,sw,36,color,rx=6)+R(sx,sy+30,sw,6,color)+T(sx+14,sy+24,title,15,"#fff",anchor="start")
    s+=f'<circle cx="{sx+sw-52}" cy="{sy+18}" r="6" fill="#fbbf24"/><circle cx="{sx+sw-32}" cy="{sy+18}" r="6" fill="#22c55e"/><circle cx="{sx+sw-12}" cy="{sy+18}" r="6" fill="#ef4444"/>'
    return s
def button(x,y,w,text,color="#2563eb",size=14): return R(x,y,w,32,color,rx=6)+T(x+w/2,y+21,text,size,"#fff")
def phone(x,y,w=230,h=440):
    s=f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="30" fill="#1f2937"/></g>'+R(x+12,y+14,w-24,h-28,"#fff",rx=20)
    return s,(x+12,y+14,w-24,h-28)
def person_head(x,y,skin="#e9b995",hair="#2b1d12",shirt="#374151",scale=1):
    return f'<g transform="translate({x},{y}) scale({scale})"><circle cx="0" cy="0" r="30" fill="{skin}"/><path d="M-31,-8 a31,31 0 0 1 62,0 v-2 a31,24 0 0 0 -62,0z" fill="{hair}"/><path d="M-60,110 a60,60 0 0 1 120,0z" fill="{shirt}"/></g>'
def render(name,body,out="jpg"):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{W}" viewBox="0 0 {W} {W}">{DEFS}<rect width="{W}" height="{W}" fill="#fff"/>'+body+'</svg>'
    open(name+".svg","w",encoding="utf-8").write(svg)
    subprocess.run(["qlmanage","-t","-s",str(W),"-o",".",name+".svg"],capture_output=True)
    im=Image.open(name+".svg.png").convert("RGB").crop((0,0,W,H))
    if out=="jpg": im.save(name+".jpg","JPEG",quality=86,optimize=True)
    else: im.save(name+".png",optimize=True)
    os.remove(name+".svg.png"); print(name+"."+out)

from PIL import ImageFont
_FC={}
def tw_(s,size):
    try:
        f=_FC.get(size)
        if not f:
            f=ImageFont.truetype("/System/Library/Fonts/HelveticaNeue.ttc",size); _FC[size]=f
        return f.getlength(s)
    except Exception:
        return sum((size*1.0 if ord(c)>0x2e7f else size*0.52) for c in s)
def textblock(x,y,lines_,size=16,gap=38,color="#111",marks=None,lx=150,rx=1450,lsize=18,place="side",by=760,cols=5,n0=0,nolabel=False):
    """lines_: list of str. marks: [(line_idx,phrase,en,zh,side)] side='l'|'r'. numbered badges, no leader lines"""
    s=""; labs=[]; n=n0
    for i,ln in enumerate(lines_):
        yy=y+i*gap
        for m in (marks or []):
            if m[0]!=i: continue
            li,ph,en,zh,side=m[:5]; n+=1
            k=ln.find(ph)
            if k<0: k=0
            px=x+tw_(ln[:k],size); pw=tw_(ph,size)
            s+=R(px-3,yy-size+2,pw+6,size+8,"#fef08a",rx=4,op=.9)
            s+=f'<circle cx="{px+pw+4:.0f}" cy="{yy-size-4:.0f}" r="{size*0.55:.0f}" fill="#dc2626" stroke="#fff" stroke-width="2"/>'+T(px+pw+4,yy-size-4+size*0.3,str(n),int(size*0.68),"#fff")
            labs.append((side,yy,n,en,zh))
        s+=T(x,yy,ln,size,color,w="400",anchor="start")
    out=""; lastL=-999; lastR=-999
    if nolabel: return s,labs
    if place=="bottom":
        xs=[160+i*(1280//(cols-1)) for i in range(cols)] if cols>1 else [800]
        for i,(side,yy,n,en,zh) in enumerate(labs):
            r,ci=divmod(i,cols); out+=label(xs[ci],by+r*90,f"{n}  {en}",zh,size=lsize)
        return s+out
    for side,yy,n,en,zh in labs:
        if side=="l": ly=max(yy,lastL+64); lastL=ly; X=lx
        else: ly=max(yy,lastR+64); lastR=ly; X=rx
        out+=label(X,ly,f"{n}  {en}",zh,size=lsize)
    return s+out
