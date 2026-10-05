# -*- coding: utf-8 -*-
"""把 ct_u*.py 的單元組成 contract-data.js / contract-sudu-data.js，並列出需要產生的 edge-tts 語音清單。"""
import json,hashlib,importlib,os,sys,re
D=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))

MODS=["ct_u1","ct_u2","ct_u3"]
VEN="en-US-JennyNeural"      # 英文條款朗讀（與多益同一組真人語音）
VZH="zh-TW-HsiaoChenNeural"  # 中文
VSAY="zh-TW-HsiaoChenNeural" # 速讀念給你聽（中英夾雜，用中文聲線）

def clean(s): return re.sub(r"\s+"," ",str(s).replace("**","").replace("—[","").replace("]—","")).strip()
def h(v,t): return hashlib.sha1((v+"|"+clean(t)).encode("utf-8")).hexdigest()[:12]


STOP={"means","includes","as of","by way of","expressions","accounts"}
def bold(u):
    """把本單元核心字彙在英文條文與中譯裡自動加粗（最多 3 處／句），幫助掃讀。"""
    vocs=[v for it in u["items"] if it["k"]=="voc" for v in it["v"]]
    en=sorted({v["w"] for v in vocs if len(v["w"])>3 and v["w"].lower() not in STOP},key=len,reverse=True)
    zh=sorted({re.split(r"[（(；;]",v["zh"])[0].strip() for v in vocs if len(re.split(r"[（(；;]",v["zh"])[0].strip())>=3},key=len,reverse=True)
    def wrap(text,terms,ci):
        used=[]; n=0
        if len(text)<12: return text
        for term in terms:
            if n>=3: break
            flags=re.I if ci else 0
            for m in re.finditer(re.escape(term),text,flags):
                a,b=m.span()
                if any(a<y and x<b for x,y in used): continue
                if ci and ((a>0 and text[a-1].isalnum()) or (b<len(text) and text[b].isalnum())): continue
                if (b-a)/len(text)>0.6: break
                used.append((a,b)); n+=1; break
        for a,b in sorted(used,reverse=True): text=text[:a]+"**"+text[a:b]+"**"+text[b:]
        return text
    for it in u["items"]:
        if it["k"]!="en": continue
        if "**" not in it["t"]: it["t"]=wrap(it["t"],en,True)
        if it.get("zh") and "**" not in it["zh"]: it["zh"]=wrap(it["zh"],zh,False)

DATA=[];SUDU={};JOBS={}
def job(v,t):
    k=h(v,t); JOBS[k]=(v,clean(t)); return k

for m in MODS:
    mod=importlib.import_module(m)
    u=json.loads(json.dumps(mod.U))          # deep copy
    bold(u)
    for it in u["items"]:
        if it["k"]=="en":
            it["a"]=job(VEN,it["t"])
        elif it["k"]=="voc":
            for w in it["v"]:
                w.setdefault("syn","");w.setdefault("trap","");w.setdefault("tip","")
                w["a"]=job(VEN,w["w"]); w["az"]=job(VZH,w["zh"])
    DATA.append(u)
    s=json.loads(json.dumps(mod.SUDU))
    s["saya"]=[job(VSAY,x) for x in s.get("say",[])]
    SUDU[u["code"]]=s

open(D+"contract-data.js","w",encoding="utf-8").write("window.CONTRACT="+json.dumps(DATA,ensure_ascii=False)+";")
open(D+"contract-sudu-data.js","w",encoding="utf-8").write("window.CONTRACT_SUDU="+json.dumps(SUDU,ensure_ascii=False)+";")
json.dump([[k,v[0],v[1]] for k,v in JOBS.items()],open(os.path.dirname(os.path.abspath(__file__))+"/jobs.json","w",encoding="utf-8"),ensure_ascii=False)
print("units",len(DATA),"| en 句",sum(1 for u in DATA for i in u["items"] if i["k"]=="en"),
      "| 字彙",sum(len(i["v"]) for u in DATA for i in u["items"] if i["k"]=="voc"),
      "| 語音檔",len(JOBS))
for u in DATA: print(" ",u["code"],u["title"],"| quiz",len(SUDU[u["code"]]["quiz"]),"| say",len(SUDU[u["code"]]["say"]))
