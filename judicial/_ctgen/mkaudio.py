# -*- coding: utf-8 -*-
"""依 jobs.json 產生 judicial/audio/ct/<hash>.mp3（已存在者跳過）。"""
import json,os,subprocess,sys
H=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.dirname(H)+"/audio/ct"
os.makedirs(OUT,exist_ok=True)
jobs=json.load(open(H+"/jobs.json",encoding="utf-8"))
todo=[j for j in jobs if not os.path.exists(OUT+"/"+j[0]+".mp3")]
print("total",len(jobs),"todo",len(todo),flush=True)
EDGE="/opt/anaconda3/bin/edge-tts"
bad=[]
for n,(k,v,t) in enumerate(todo,1):
    p=OUT+"/"+k+".mp3"
    for attempt in range(3):
        try:
            r=subprocess.run([EDGE,"--voice",v,"--text",t,"--write-media",p],capture_output=True,timeout=90)
            if r.returncode==0 and os.path.exists(p) and os.path.getsize(p)>800: break
        except subprocess.TimeoutExpired:
            pass
        if os.path.exists(p): os.remove(p)
    else:
        bad.append((k,v,t[:40])); print("FAIL",k,t[:50],flush=True); continue
    if n%20==0: print(n,"/",len(todo),flush=True)
print("done. fail",len(bad),flush=True)
for b in bad: print(b,flush=True)
