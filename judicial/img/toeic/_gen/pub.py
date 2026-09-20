# -*- coding: utf-8 -*-
"""pub.py CODE  img=caption  img=caption ...   (img = filename in _gen, copied to ../ ; replaces pics of that topic)"""
import json,re,sys,shutil,os
D=os.path.dirname(os.path.abspath(__file__)); J=os.path.abspath(os.path.join(D,"../../.."))
f=os.path.join(J,"toeic-data.js"); raw=open(f,encoding="utf-8").read()
T=json.loads(re.search(r'window\.TOEIC=(.*);$',raw,re.S).group(1))
code=sys.argv[1]; t=[x for x in T if x["code"]==code][0]
pics=[]
for a in sys.argv[2:]:
    fn,cap=a.split("=",1); shutil.copy(os.path.join(D,fn),os.path.join(D,"..",fn)); pics.append({"src":"img/toeic/"+fn,"cap":cap})
t["pics"]=pics
open(f,"w",encoding="utf-8").write("window.TOEIC="+json.dumps(T,ensure_ascii=False,separators=(',',':'))+";")
print(code,len(pics),"pics")
