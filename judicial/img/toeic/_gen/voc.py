import json,re,sys,os
D=os.path.dirname(os.path.abspath(__file__)); f=os.path.join(D,"../../../toeic-data.js")
T=json.loads(re.search(r'window\.TOEIC=(.*);$',open(f,encoding="utf-8").read(),re.S).group(1))
for code in sys.argv[1:]:
    t=[x for x in T if x["code"]==code][0]; print("##",code,t["title"].split(" (")[0])
    for i in t["items"]:
        if i["k"]=="voc":
            for w in i["v"]: print(" ",w["w"],"|",w["zh"])
