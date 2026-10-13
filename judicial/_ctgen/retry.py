import json,os,subprocess,time
H=os.path.dirname(os.path.abspath(__file__)); OUT=os.path.dirname(H)+"/audio/ct"
jobs=json.load(open(H+"/jobs.json",encoding="utf-8"))
EDGE="/opt/anaconda3/bin/edge-tts"
for rnd in range(12):
    miss=[j for j in jobs if not os.path.exists(OUT+"/"+j[0]+".mp3")]
    if not miss: print("all done",flush=True); break
    print("round",rnd,"missing",len(miss),flush=True)
    for k,v,t in miss:
        p=OUT+"/"+k+".mp3"
        r=subprocess.run([EDGE,"--voice",v,"--text",t,"--write-media",p],capture_output=True)
        if not(r.returncode==0 and os.path.getsize(p)>800):
            if os.path.exists(p): os.remove(p)
        time.sleep(3)
    time.sleep(45)
miss=[j for j in jobs if not os.path.exists(OUT+"/"+j[0]+".mp3")]
print("FINAL missing",len(miss),flush=True)
