# -*- coding: utf-8 -*-
"""多來源找真實照片候選：Openverse ＋ Wikimedia Commons，輸出聯絡表讓人挑。"""
import json,os,re,urllib.parse,urllib.request,hashlib,time
from PIL import Image,ImageDraw
from photo import fetch
H={"User-Agent":"toeic-study/1.0 (elaine; study material)"}

def ov(q,n=12,page=1):
    u="https://api.openverse.org/v1/images/?"+urllib.parse.urlencode(
        {"q":q,"license_type":"commercial,modification","page_size":n,"page":page,"mature":"false"})
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40))
    except Exception: return []
    out=[]
    for x in d.get("results",[]):
        w=x.get("width") or 0; h=x.get("height") or 0
        if w and (w<900 or h and w/h<1.1): continue
        out.append({"url":x["url"],"title":(x.get("title") or "")[:60],
                    "cred":"%s (%s)"%(x.get("creator") or x["source"], (x["license"]+"-"+(x.get("license_version") or "")).strip("-").upper())})
    return out

def commons(q,n=12):
    u="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({
        "action":"query","format":"json","generator":"search","gsrnamespace":6,
        "gsrsearch":q+" filetype:bitmap","gsrlimit":n,"prop":"imageinfo",
        "iiprop":"url|size|extmetadata","iiurlwidth":1600})
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40))
    except Exception: return []
    out=[]
    for p in (d.get("query",{}).get("pages") or {}).values():
        ii=(p.get("imageinfo") or [{}])[0]
        w,h=ii.get("width") or 0, ii.get("height") or 0
        if w<900 or (h and w/h<1.1): continue
        em=ii.get("extmetadata") or {}
        lic=(em.get("LicenseShortName",{}) or {}).get("value","CC")
        art=re.sub(r"<[^>]+>","",(em.get("Artist",{}) or {}).get("value","Wikimedia"))[:34]
        out.append({"url":ii.get("thumburl") or ii.get("url"),"title":p["title"][5:65],
                    "cred":"%s (%s)"%(art.strip(), lic)})
    return out

def cands(queries,limit=12):
    seen,out=set(),[]
    for q in queries:
        for src in (ov,commons):
            for c in src(q):
                k=c["url"].split("/")[-1][:40]
                if k in seen: continue
                seen.add(k); out.append(c)
                if len(out)>=limit: return out
            time.sleep(0.3)
    return out

def sheet(cs,name,cols=4,tw=420,th=290):
    if not cs: print("!! 沒有候選",name); return []
    rows=max(1,(len(cs)+cols-1)//cols)
    S=Image.new("RGB",(cols*tw,rows*th),"#1b1b1b"); dr=ImageDraw.Draw(S)
    ok=[]
    for i,c in enumerate(cs):
        try: im=Image.open(fetch(c["url"])).convert("RGB")
        except Exception: continue
        im.thumbnail((tw-10,th-30)); x=(i%cols)*tw+5; y=(i//cols)*th+25
        S.paste(im,(x,y))
        dr.rectangle([x,y-24,x+46,y],fill="#c0392b"); dr.text((x+14,y-18),str(i),fill="#fff")
        dr.text((x+54,y-18),c["title"][:44],fill="#ddd")
        ok.append(i)
    S.save(name,"JPEG",quality=82); print(name,S.size,"候選",ok)
    json.dump(cs,open(name.replace(".jpg",".json"),"w",encoding="utf-8"),ensure_ascii=False)
    return ok

# ── 真實場景圖：照片 ＋ 少量貼在物件上的標籤 ＋ 底部詞彙帶 ──────────────
import base64,subprocess
from gen import label,T,R,EN,ZH,esc
from photo import cover

def strip_rows(terms,W=1600,size=21,pad=16,cols=4):
    """底部詞彙帶：en／zh 成對，分欄排列。回傳 (svg, 高度)"""
    if not terms: return "",0
    rows=(len(terms)+cols-1)//cols
    rh=size*2+16; h=rows*rh+pad*2+26
    s=R(0,0,W,h,"#101418",op=.93)
    s+=T(22,pad+20,"這個場景會用到的說法",17,"#f1c40f",w="700",anchor="start",fam=ZH)
    cw=(W-44)//cols
    for i,(en,zh) in enumerate(terms):
        x=22+(i%cols)*cw; y=pad+40+(i//cols)*rh
        s+=T(x,y+size,en,size,"#fff",w="700",anchor="start")
        s+=T(x,y+size*2+2,zh,size-3,"#9fd3ff",w="700",anchor="start",fam=ZH)
    return s,h

def scene2(name,photo_url,labels,credit,terms=(),focus=(.5,.5),zoom=1.0,size=27):
    """labels: [(lx,ly,en,zh,bx,by)]  lx,ly=指到的物件點；bx,by=標籤框中心"""
    fn=fetch(photo_url)
    sh,hh=strip_rows(list(terms))
    PH=1000-hh if hh else 1000
    im=cover(fn,W=1600,Hh=PH,focus=focus,zoom=zoom)
    tmp=name+"_bg.jpg"; im.save(tmp,"JPEG",quality=90)
    b64=base64.b64encode(open(tmp,"rb").read()).decode(); os.remove(tmp)
    b=f'<image href="data:image/jpeg;base64,{b64}" x="0" y="0" width="1600" height="{PH}"/>'
    for L in labels:
        lx,ly,en,zh,bx,by=L[:6]
        sz=(L[6] if len(L)>6 else size)
        by=max(sz+34, min(by, PH-sz-40))          # 標籤框不可掉出照片
        bx=max(140, min(bx, 1600-140))
        ly=max(6, min(ly, PH-6))
        b+=label(bx,by,en,zh,size=sz,line=(lx,ly))
    b+=R(0,PH-26,1600,26,"#000",op=.55)+T(1590,PH-7,credit,13,"#ddd",w="400",anchor="end")
    if hh: b+=f'<g transform="translate(0,{PH})">'+sh+'</g>'
    svg=('<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1600" viewBox="0 0 1600 1600">'
         '<rect width="1600" height="1600" fill="#101418"/>'+b+'</svg>')
    open(name+".svg","w",encoding="utf-8").write(svg)
    subprocess.run(["qlmanage","-t","-s","1600","-o",".",name+".svg"],capture_output=True)
    out=Image.open(name+".svg.png").convert("RGB").crop((0,0,1600,1000))
    out.save(name+".jpg","JPEG",quality=86,optimize=True)
    os.remove(name+".svg.png")
    print(name+".jpg", "標籤",len(labels),"詞彙帶",len(terms))

def pick(sheetjson,i):
    cs=json.load(open(sheetjson,encoding="utf-8")); return cs[i]

def gridshot(photo_url,out,focus=(.5,.5),zoom=1.0,PH=1000):
    im=cover(fetch(photo_url),W=1600,Hh=PH,focus=focus,zoom=zoom); dr=ImageDraw.Draw(im)
    for x in range(0,1600,100):
        dr.line([x,0,x,PH],fill=(255,255,0),width=1); dr.text((x+3,3),str(x),fill=(255,255,0))
    for y in range(0,PH,100):
        dr.line([0,y,1600,y],fill=(255,255,0),width=1); dr.text((3,y+3),str(y),fill=(255,255,0))
    im.save(out,"JPEG",quality=80); print(out)
