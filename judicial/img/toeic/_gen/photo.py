# -*- coding: utf-8 -*-
import json,urllib.request,urllib.parse,base64,os,subprocess,hashlib
from PIL import Image,ImageDraw
from gen import label,T,R,EN,ZH
H={"User-Agent":"toeic-study/1.0 (elaine)"}
CACHE="cache"; os.makedirs(CACHE,exist_ok=True)
def ov(q,n=10,page=1):
    u="https://api.openverse.org/v1/images/?"+urllib.parse.urlencode({"q":q,"license_type":"commercial,modification","page_size":n,"page":page,"mature":"false"})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40))
    out=[]
    for x in d.get("results",[]):
        w=x.get("width") or 0
        if w and w<900: continue
        out.append({"id":x["id"][:8],"url":x["url"],"title":x.get("title") or "","creator":x.get("creator") or "","source":x["source"],"lic":x["license"]+("-"+x["license_version"] if x.get("license_version") else ""),"w":w,"h":x.get("height")})
    return out
def fetch(url):
    fn=os.path.join(CACHE,hashlib.sha1(url.encode()).hexdigest()[:12]+".jpg")
    if not os.path.exists(fn):
        d=urllib.request.urlopen(urllib.request.Request(url,headers=H),timeout=90).read()
        open(fn,"wb").write(d)
        try: Image.open(fn).convert("RGB").save(fn,"JPEG",quality=88)
        except Exception as e: os.remove(fn); raise
    return fn
def sheet(cands,name,cols=4,tw=400,th=270):
    """contact sheet with index numbers"""
    rows=(len(cands)+cols-1)//cols
    S=Image.new("RGB",(cols*tw,rows*th),"#222"); dr=ImageDraw.Draw(S)
    ok=[]
    for i,c in enumerate(cands):
        try: im=Image.open(fetch(c["url"])).convert("RGB")
        except Exception as e: print("skip",c["url"][:60],e); continue
        im.thumbnail((tw-8,th-8)); x=(i%cols)*tw+4; y=(i//cols)*th+4
        S.paste(im,(x,y)); dr.rectangle([x,y,x+60,y+30],fill="#c00"); dr.text((x+8,y+6),str(i),fill="#fff")
        ok.append(i)
    S.save(name); print(name,S.size,"ok",ok)
def cover(fn,W=1600,Hh=1000,focus=(0.5,0.5),zoom=1.0):
    im=Image.open(fn).convert("RGB"); w,h=im.size
    s=max(W/w,Hh/h)*zoom; nw,nh=int(w*s),int(h*s); im=im.resize((nw,nh),Image.LANCZOS)
    x=int((nw-W)*focus[0]); y=int((nh-Hh)*focus[1]); x=max(0,min(x,nw-W)); y=max(0,min(y,nh-Hh))
    return im.crop((x,y,x+W,y+Hh))
def grid(fn,out,focus=(0.5,0.5),zoom=1.0):
    im=cover(fn,focus=focus,zoom=zoom); dr=ImageDraw.Draw(im)
    for x in range(0,1600,100):
        dr.line([x,0,x,1000],fill=(255,255,0),width=1); dr.text((x+3,3),str(x),fill=(255,255,0))
    for y in range(0,1000,100):
        dr.line([0,y,1600,y],fill=(255,255,0),width=1); dr.text((3,y+3),str(y),fill=(255,255,0))
    im.save(out); return out
def scene(name,fn,labels,credit,focus=(0.5,0.5),zoom=1.0,size=26):
    """labels: list of (x,y,en,zh[,line=(lx,ly)][,size])"""
    im=cover(fn,focus=focus,zoom=zoom); tmp=name+"_bg.jpg"; im.save(tmp,"JPEG",quality=90)
    b64=base64.b64encode(open(tmp,"rb").read()).decode(); os.remove(tmp)
    b=f'<image href="data:image/jpeg;base64,{b64}" x="0" y="0" width="1600" height="1000"/>'
    for L in labels:
        x,y,en,zh=L[:4]; line=L[4] if len(L)>4 else None; sz=L[5] if len(L)>5 else size
        b+=label(x,y,en,zh,size=sz,line=line)
    b+=R(0,972,1600,28,"#000",op=.55)+T(1590,992,credit,13,"#ddd",w="400",anchor="end")
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1600" viewBox="0 0 1600 1600"><rect width="1600" height="1600" fill="#fff"/>'+b+'</svg>'
    open(name+".svg","w",encoding="utf-8").write(svg)
    subprocess.run(["qlmanage","-t","-s","1600","-o",".",name+".svg"],capture_output=True)
    out=Image.open(name+".svg.png").convert("RGB").crop((0,0,1600,1000)); out.save(name+".jpg","JPEG",quality=86,optimize=True)
    os.remove(name+".svg.png"); os.remove(name+".svg"); print(name+".jpg")
def cm(q,n=10):
    u="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({"action":"query","generator":"search","gsrsearch":q,"gsrnamespace":6,"gsrlimit":n,"prop":"imageinfo","iiprop":"url|size|mime|extmetadata","iiurlwidth":1600,"format":"json"})
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40))
    out=[]
    for p in d.get("query",{}).get("pages",{}).values():
        ii=p["imageinfo"][0]
        if not ii.get("mime","").startswith("image/jpeg") or (ii.get("width") or 0)<1000: continue
        m=ii.get("extmetadata",{})
        out.append({"id":str(p["pageid"]),"url":ii.get("thumburl") or ii["url"],"title":p["title"][5:],"creator":re.sub(r'<[^>]+>','',m.get("Artist",{}).get("value","")).strip()[:40],"source":"wikimedia","lic":m.get("LicenseShortName",{}).get("value",""),"w":ii.get("width"),"h":ii.get("height")})
    return out
import re
def find(queries,name,per=6):
    seen=set();cc=[]
    for q in queries:
        for fn_ in (cm,ov):
            try:
                for c in fn_(q,per):
                    if c["url"] in seen: continue
                    seen.add(c["url"]); cc.append(c)
            except Exception as e: print("err",q,e)
    cc=cc[:16]
    if not cc: print("NO RESULTS",name); return []
    sheet(cc,name+".jpg"); json.dump(cc,open(name+".json","w"))
    for i,c in enumerate(cc): print(i,c["lic"],c["creator"][:20],"|",c["title"][:50])
    return cc
