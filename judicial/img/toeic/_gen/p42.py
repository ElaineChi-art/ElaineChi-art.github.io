# -*- coding: utf-8 -*-
from props import *
from photo import scene,fetch
import json
# ---- A: real photo ----
c=json.load(open("p42A.json"))
L=[(150,150,"Office supplies","辦公用品",(90,255)),
   (240,560,"Selection","選擇、品項",(170,600)),
   (560,400,"Showcasing","展示",(455,440)),
   (800,455,"Looking for","尋找",None,22),
   (800,620,"Browsing","瀏覽",None,30),
   (800,760,"Browse a bit more","再多看看",None,24),
   (560,780,"Special pricing","特價",(565,700)),
   (200,880,"Catalog","型錄",(200,830)),
   (1400,320,"Popular models","熱門款式",(1440,400)),
   (1150,440,"Comprehensive","齊全的、全面的",(1120,520)),
   (1230,700,"In stock","有現貨",(1260,640)),
   (1360,880,"Limited availability","數量有限",(1330,840))]
scene("toeic-4-2-a",fetch(c["url"]),L,"Photo: rawpixel (CC0)")
# ---- B: showroom / demo + spec sheet + inventory list ----
b=desk(360)
# banner on wall
b+=f'<g filter="url(#sh2)"><rect x="80" y="40" width="720" height="110" rx="10" fill="#1e3a5f"/></g>'+T(440,90,"SHOWROOM · LIVE PRODUCT DEMONSTRATION",26,"#fff")+T(440,128,"Join us  ·  Free training sessions every Friday 2 pm",18,"#9fc5f0")
b+=label(440,205,"Showroom","展示間",size=26,line=(300,150))
b+=label(700,215,"Product demonstration","產品展示",size=22,line=(600,150))
b+=label(1000,110,"Join us","加入我們、參加",size=22,line=(802,118))
b+=label(1010,230,"Training sessions","培訓課程",size=22,line=(720,140))
# ergonomic chair (simplified realistic)
b+=f'<g filter="url(#sh)"><path d="M300,420 q0,-60 60,-60 h120 q60,0 60,60 v130 h-240z" fill="#2c2f36"/><rect x="290" y="550" width="260" height="34" rx="14" fill="#3a3d45"/><rect x="405" y="584" width="30" height="120" fill="#7b8088"/><path d="M330,720 h180 l-30,-24 h-120z" fill="#7b8088"/></g>'
b+=f'<path d="M330,430 h180" stroke="#4b5563" stroke-width="10" stroke-linecap="round"/><path d="M330,470 h180" stroke="#4b5563" stroke-width="10" stroke-linecap="round"/>'
b+=label(420,300,"Ergonomic","人體工學的",size=26,line=(420,362))
# spec sheet
b+=paper(620,400,330,420,rot=-2)
b+=T(785,440,"SPECIFICATIONS",20,"#111")+T(785,462,"ErgoPro Chair X2",13,"#666")
rows=[("Weight","4.8 kg  ·  lightweight"),("Frame","steel  ·  durable"),("Warranty","10 years"),("Load","150 kg"),("Colors","black / grey")]
for i,(k,v) in enumerate(rows):
    b+=R(640,480+i*44,290,36,"#f3f4f6" if i%2 else "#fff",rx=4)+T(652,504+i*44,k,14,"#555",anchor="start")+T(920,504+i*44,v,14,"#111",anchor="end")
b+=T(785,760,"Lightweight yet durable ✓",16,"#16a34a")
b+=end()
b+=label(785,330,"Specifications","規格",size=26,line=(785,402))
b+=label(1100,480,"Lightweight","輕量的",size=22,line=(925,525))
b+=label(1100,560,"Durable","耐用的",size=22,line=(925,568))
b+=label(1040,780,"Lightweight yet durable","輕量但耐用",size=20,line=(925,760))
# inventory list clipboard
b+=f'<g filter="url(#sh)" transform="rotate(3 1330 620)"><rect x="1180" y="420" width="300" height="400" rx="8" fill="#8a6b47"/><rect x="1195" y="450" width="270" height="360" fill="#fff"/><rect x="1290" y="405" width="80" height="30" rx="6" fill="#4b5563"/></g>'
b+=f'<g transform="rotate(3 1330 620)">'+T(1330,485,"INVENTORY LIST",18,"#111")
inv=[("Chair X2","In stock · 42","#16a34a"),("Desk D1","Available · 8","#2563eb"),("Lamp L3","On backorder","#dc2626"),("Monitor M9","Rush order ✓","#d97706")]
for i,(n,st,col) in enumerate(inv):
    b+=T(1210,530+i*50,n,15,"#333",anchor="start")+T(1450,530+i*50,st,14,col,anchor="end")+R(1210,542+i*50,240,1,"#e5e7eb")
b+=T(1330,770,"Verified by: K. Lin  ✔",13,"#555")+end()
b+=label(1330,330,"Inventory list","庫存清單",size=24,line=(1330,412))
b+=label(880,900,"Inventory","庫存",size=24,line=(1200,760))
b+=label(1480,940,"On backorder","缺貨待訂",size=20,line=(1440,633))
b+=label(1000,660,"Available","可提供的、有貨的",size=20,line=(1200,580))
b+=label(1230,940,"Rush order","急件訂購",size=20,line=(1440,683))
b+=label(1500,850,"Verify","確認、核實",size=20,line=(1420,770))
# sticky: is there any way / better availability
b+=sticky(60,430,"Is there any way\nto get better\navailability?",rot=-6,size=17)
b+=label(160,620,"Is there any way","有沒有什麼辦法",size=20,line=(150,540))
b+=label(160,720,"Better availability","現貨更充足",size=20,line=(175,545))
b+=vignette()
render("toeic-4-2-b",b)
# ---- C: ordering portal on laptop + memo ----
b=desk(340)
s,(sx,sy,sw,sh)=laptop(330,120,760,520); b+=s
b+=window(sx,sy,sw,sh,"Supplier Portal — Ordering System")
b+=T(sx+30,sy+80,"Welcome back, Elaine",22,"#111",anchor="start")+T(sx+30,sy+106,"Place orders · track inventory · consolidate invoices",14,"#666",anchor="start")
b+=R(sx+30,sy+130,sw-60,1,"#e5e7eb")
b+=T(sx+30,sy+165,"New order",16,"#111",anchor="start")
b+=R(sx+30,sy+180,420,34,"#fff","#cbd5e1",1,rx=6)+T(sx+42,sy+202,"Item: ErgoPro Chair X2   Qty: 25",14,"#333",anchor="start")
b+=button(sx+470,sy+181,140,"Place order")
b+=R(sx+30,sy+235,sw-60,110,"#f8fafc","#e2e8f0",1,rx=8)
b+=T(sx+45,sy+262,"Efficiency +38%   ·   Costs −12%",17,"#16a34a",anchor="start")
b+=T(sx+45,sy+292,"3 suppliers consolidated into one portal",14,"#333",anchor="start")
b+=T(sx+45,sy+318,"Transition completed — old catalog system retired",14,"#333",anchor="start")
b+=R(sx+30,sy+370,200,50,"#eef2ff",rx=8)+T(sx+130,sy+401,"Comprehensive catalog",13,"#3730a3")
b+=R(sx+250,sy+370,200,50,"#ecfdf5",rx=8)+T(sx+350,sy+401,"Reduce costs",13,"#065f46")
b+=label(710,60,"Ordering system","訂購系統",size=26,line=(560,150))
b+=label(1250,150,"Portal","入口網站",size=26,line=(1076,180))
b+=label(1280,320,"Placing orders","下單",size=24,line=(sx+610,sy+197))
b+=label(160,300,"Efficiency","效率",size=24,line=(sx+45,sy+262))
b+=label(160,420,"Consolidate","整合",size=24,line=(sx+45,sy+292))
b+=label(160,540,"Transition","轉換、過渡",size=24,line=(sx+45,sy+318))
b+=label(1300,470,"Comprehensive","齊全的、全面的",size=22,line=(sx+230,sy+395))
b+=label(1300,580,"Reduce costs","降低成本",size=22,line=(sx+450,sy+395))
# printed catalog on desk
b+=paper(120,660,280,300,rot=-8,fill="#1e3a5f")+T(260,720,"2026 CATALOG",22,"#fff")+T(260,750,"Office Furniture",14,"#9fc5f0")+R(150,780,220,140,"#fff",rx=6)+end()
b+=label(300,900,"Catalog","型錄",size=24,line=(300,830))
# coffee cup
b+=f'<g filter="url(#sh2)"><ellipse cx="1350" cy="820" rx="70" ry="22" fill="#e5e7eb"/><rect x="1290" y="720" width="120" height="100" rx="8" fill="#f9fafb"/><ellipse cx="1350" cy="720" rx="60" ry="18" fill="#6b4423"/><path d="M1410,745 q40,0 40,30 t-40,30" stroke="#f9fafb" stroke-width="12" fill="none"/></g>'
b+=vignette()
render("toeic-4-2-c",b)
