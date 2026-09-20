# -*- coding: utf-8 -*-
"""quick document scenes with numbered glossary"""
from props import *
def glossary(b,labs,start_y=None,cols=5,size=18):
    n=len(labs)
    if n>30: cols=6; size=15
    rows=(n+cols-1)//cols
    gap=90 if rows<=3 else (78 if rows<=5 else 64)
    y0=start_y if start_y else (1000-rows*gap+10)
    xs=[160+i*(1280//(cols-1)) for i in range(cols)]
    for i,(side,yy,num,en,zh) in enumerate(labs):
        r,ci=divmod(i,cols); b+=label(xs[ci],y0+r*gap,f"{num}  {en}",zh,size=size if len(en)<22 else (size-3 if len(en)<30 else max(10,size-6)))
    return b
def make_doc(name,kind,title,lines_,marks,subtitle="",size=None,gap=None,extra=""):
    if size is None: size=22 if len(lines_)<=7 else (20 if len(lines_)<=9 else 18)
    if gap is None: gap=int(size*2.85)
    n=len(marks); cols=6 if n>30 else 5; rows=(n+cols-1)//cols; gl_h=(90 if rows<=3 else (78 if rows<=5 else 64))*rows+20
    top=1000-gl_h  # desk/glossary starts here
    b=desk(top-10)
    if kind=="email":
        s,(sx,sy,sw,sh)=laptop(200,30,1200,top-90); b+=s
        b+=window(sx,sy,sw,sh,title,color="#475569")
        if subtitle: b+=T(sx+30,sy+62,subtitle,13,"#666",anchor="start")
        tx,ty=sx+30,sy+100
    elif kind=="slide":
        b+=f'<g filter="url(#sh)"><rect x="150" y="30" width="1300" height="{top-70}" rx="12" fill="#ffffff"/></g>'
        b+=R(150,30,1300,70,"#1e3a5f",rx=12)+R(150,80,1300,20,"#1e3a5f")+T(180,76,title,24,"#fbbf24",anchor="start")
        b+=R(150,100,1300,6,"#f59e0b")
        if subtitle: b+=T(180,136,subtitle,15,"#64748b",anchor="start")
        tx,ty=180,170
    elif kind=="news":
        b+=paper(120,30,1360,top-70)
        b+=T(800,80,title,34,"#111",fam="Georgia, Times New Roman, serif")+R(150,100,1300,3,"#111")
        if subtitle: b+=T(150,130,subtitle,14,"#666",anchor="start")
        tx,ty=150,170
    elif kind=="memo":
        b+=paper(120,30,1360,top-70)
        b+=T(150,80,"MEMORANDUM",26,"#111",anchor="start")+T(1450,80,title,14,"#666",anchor="end")+R(150,95,1300,2,"#111")
        if subtitle: b+=T(150,125,subtitle,14,"#333",anchor="start")
        tx,ty=150,165
    else: # paper/letter/notice
        b+=paper(120,30,1360,top-70)
        b+=R(140,50,1320,56,"#1f2937")+T(800,87,title,22,"#fff")
        if subtitle: b+=T(150,135,subtitle,14,"#666",anchor="start")
        tx,ty=150,170
    color="#111"
    bottom=(sy+sh-20) if kind=="email" else (top-60)
    avail=bottom-ty
    if len(lines_)*gap>avail:
        gap=int(avail/len(lines_)); size=min(size,int(gap/2.6))
    t,labs=textblock(tx,ty,lines_,size=size,gap=gap,color=color,marks=marks,nolabel=True); b+=t
    b+=extra
    if kind not in ("email","slide"): b+=end()
    b=glossary(b,labs)
    b+=vignette(); render(name,b)
