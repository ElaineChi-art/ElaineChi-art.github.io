# -*- coding: utf-8 -*-
from props import *
from photo import scene,fetch
import json
c=json.load(open("p45A.json"))
L=[(600,110,"Complaints","投訴",(740,250),24),
   (1050,160,"Resolve","解決",(930,235),24),
   (1200,70,"Return policy","退貨政策",(880,30),22),
   (1380,300,"Original receipt","原始收據",(1200,380),20),
   (170,160,"Stock room","倉庫、儲藏室",(400,240),22),
   (120,470,"Store credit","商店額度",(150,340),20),
   (330,470,"Full refund","全額退款",(330,300),20),
   (300,560,"Exchange","換貨",(420,640),22),
   (560,800,"Replacement","替換品",(500,730),22),
   (1350,720,"Promptly","迅速地",(1250,540),22)]
scene("toeic-4-5-a",fetch(c["url"]),L,"Photo: W.carter, Wikimedia Commons (CC0)")
# ---- B: complaint email + phone note ----
b=desk(420)
s,(sx,sy,sw,sh)=laptop(300,60,1000,760); b+=s
b+=window(sx,sy,sw,sh,"Mail — Re: Order #7731 — coffee maker not working properly",color="#7f1d1d")
lines_=["Dear Customer Service,",
"The coffee maker I bought is not working properly: it stops heating up",
"after two minutes, and the display shows strange lines. The manual",
"says the timer is one of its features, but it is missing from the box.",
"I believe the unit is defective. Please call me back at 0912-345-678.",
"",
"Reply from Customer Service:",
"We apologize for the inconvenience — this was our mistake.",
"A replacement will be shipped for immediate delivery, and we will",
"add a $20 store credit as compensation. Missing items are being",
"sent from our stock room today. We stand by our products and",
"stand behind our satisfaction guarantee. We will resolve this promptly."]
marks=[(1,"not working properly","Not working properly","無法正常運作","l"),(1,"heating up","Heating up","加熱","r"),
(2,"strange lines","Strange lines","異常線條","l"),(3,"features","Features","功能、特色","r"),(3,"missing","Missing","缺少的、漏掉的","l"),
(4,"defective","Defective","有瑕疵的","r"),(4,"call me back","Call me back","回電給我","l"),
(7,"inconvenience","Inconvenience","不便","r"),(7,"our mistake","Our mistake","我方的疏失","l"),
(8,"replacement","Replacement","替換品","r"),(8,"immediate","Immediate","立即的","l"),
(9,"compensation","Compensation","補償","r"),(9,"Missing items","Missing items","漏件","l"),
(10,"stock room","Stock room","倉庫、儲藏室","r"),(10,"stand by","Stand by","堅守、支持","l"),
(11,"stand behind","Stand behind","為…負責、支持","r"),(11,"satisfaction guarantee","Satisfaction guarantee","滿意保證","l"),(11,"promptly","Promptly","迅速地","r")]
b+=textblock(sx+30,sy+90,lines_,size=16,gap=44,marks=marks,lsize=16,rx=1430)
b+=vignette(); render("toeic-4-5-b",b)
# ---- C: return policy notice (new vs previous) ----
b=desk(700)
b+=paper(100,50,700,560,rot=-1.5)
b+=R(120,70,660,56,"#dc2626")+T(450,107,"NEW RETURN POLICY — effective March 1",20,"#fff")
pol=["• 30-day return policy for all items.","• Defective or damaged items: either a full refund","   or an exchange — your decision.","• Customer mistakes (wrong size): store credit only.","• Original receipt required for every return.","• Missing items reported within 7 days are replaced."]
m1=[(0,"30-day return policy","30-day return policy","30 天退貨政策","l"),(1,"Defective or damaged items","Defective or damaged items","瑕疵或損壞商品","l"),(1,"either","Either…or","二選一","l"),(1,"full refund","Full refund","全額退款","l"),(2,"decision","Decision","決定","l"),(3,"Customer mistakes","Customer mistakes","顧客錯誤","l"),(3,"store credit","Store credit","商店額度","l"),(4,"Original receipt","Original receipt","原始收據","l")]
t1,l1=textblock(150,175,pol,size=17,gap=60,marks=m1,nolabel=True); b+=t1
b+=end()
b+=paper(880,90,600,480,rot=2.5,fill="#f5f5f4")
b+=R(900,110,560,48,"#6b7280")+T(1180,142,"PREVIOUS POLICY (before March 1)",16,"#fff")
old=["• Previously: 14-day return window.","• Refunds: store credit only.","• Exchange: defective items only.","• The satisfaction guarantee","   remains unchanged."]
m2=[(0,"Previously","Previously","先前","l"),(2,"Exchange","Exchange","換貨","l"),(4,"remains unchanged","Remains unchanged","維持不變","l")]
t2,l2=textblock(920,210,old,size=17,gap=60,marks=m2,nolabel=True,n0=len(l1)); b+=t2
b+=stamp(1200,520,"SUPERSEDED",color="#9ca3af",rot=-10,size=20)
b+=end()
b+=label(450,20,"Return policy","退貨政策",size=22,line=(300,70))
b+=label(1180,40,"Effective","生效的",size=22,line=(660,96))
b+=label(1350,620,"Previous policy","先前的政策",size=20,line=(1180,158))
labs=l1+l2; xs=[160,480,800,1120,1440]
for i,(side,yy,n,en,zh) in enumerate(labs):
    r,ci=divmod(i,5); b+=label(xs[ci],760+r*95,f"{n}  {en}",zh,size=18)
b+=vignette(); render("toeic-4-5-c",b)
