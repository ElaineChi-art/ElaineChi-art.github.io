# -*- coding: utf-8 -*-
import subprocess,os
from PIL import Image
W,H=1600,1000
EN="Helvetica Neue, Helvetica, Arial, sans-serif"; ZH="PingFang TC, Hiragino Sans, sans-serif"
def tw(s,size,zh=False):
    return sum((size*1.0 if ord(c)>0x2e7f else size*0.6) for c in s)
def label(x,y,en,zh,anchor="c",size=30,line=None):
    """black rounded box; anchor c=center at x,y ; l=left top at x,y"""
    es,zs=size,size*0.84
    w=max(tw(en,es),tw(zh,zs,True))+34; h=es+zs+30
    if anchor=="c": x0,y0=x-w/2,y-h/2
    else: x0,y0=x,y
    s=""
    if line:
        lx,ly=line; s+=f'<line x1="{x0+w/2:.0f}" y1="{y0+h:.0f}" x2="{lx}" y2="{ly}" stroke="#111" stroke-width="3"/><circle cx="{lx}" cy="{ly}" r="6" fill="#111" stroke="#fff" stroke-width="2"/>'
    s+=f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{w:.0f}" height="{h:.0f}" rx="8" fill="#111" opacity=".92"/>'
    s+=f'<text x="{x0+w/2:.0f}" y="{y0+es+6:.0f}" font-family="{EN}" font-weight="700" font-size="{es}" fill="#fff" text-anchor="middle">{en}</text>'
    s+=f'<text x="{x0+w/2:.0f}" y="{y0+es+zs+16:.0f}" font-family="{ZH}" font-weight="700" font-size="{zs:.0f}" fill="#fff" text-anchor="middle">{zh}</text>'
    return s
def T(x,y,t,size=20,fill="#222",w="700",anchor="middle",fam=None):
    return f'<text x="{x}" y="{y}" font-family="{fam or EN}" font-weight="{w}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{t}</text>'
def R(x,y,w,h,fill,stroke=None,sw=2,rx=0,op=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{op}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>'
def box(x,y,w,h,shade=0):
    c=["#d2a06a","#c8955c","#bf8a50"][shade]
    s=R(x,y,w,h,c,"#8f6337",3)
    s+=f'<line x1="{x+w/2}" y1="{y}" x2="{x+w/2}" y2="{y+h}" stroke="#a9773f" stroke-width="3"/>'
    s+=R(x+w/2-10,y,20,h,"#e8d5b5",op=.6)
    return s
def person(x,y,shirt="#5b4a3b",skin="#e9b995",hair="#2b1d12",scale=1.0):
    s=f'<g transform="translate({x},{y}) scale({scale})">'
    s+=f'<circle cx="0" cy="0" r="26" fill="{skin}"/><path d="M-27,-6 a27,27 0 0 1 54,0 v-4 a27,20 0 0 0 -54,0z" fill="{hair}"/>'
    s+=f'<rect x="-34" y="28" width="68" height="90" rx="18" fill="{shirt}"/>'
    s+=f'<rect x="-30" y="115" width="26" height="80" rx="8" fill="#2f3a4a"/><rect x="4" y="115" width="26" height="80" rx="8" fill="#2f3a4a"/>'
    s+='</g>'; return s
def render(name,body):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{W}" viewBox="0 0 {W} {W}"><rect width="{W}" height="{W}" fill="#fff"/>'+body+'</svg>'
    open(name+".svg","w",encoding="utf-8").write(svg)
    subprocess.run(["qlmanage","-t","-s","1600","-o",".",name+".svg"],capture_output=True)
    im=Image.open(name+".svg.png").convert("RGB"); im=im.crop((0,0,W,H)); im.save(name+".png",optimize=True); os.remove(name+".svg.png")
    print(name+".png",im.size)
