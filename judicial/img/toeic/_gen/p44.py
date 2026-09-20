# -*- coding: utf-8 -*-
from props import *
from photo import scene,fetch
import json
c=json.load(open("p44A.json"))
L=[(560,50,"Trade show","商展",(700,105),26),
   (1000,50,"Booth number 45","45 號攤位",(830,132),22),
   (1420,50,"Electricity","電力",(1350,95),22),
   (1450,170,"Vendor booths","供應商攤位",(1350,290),22),
   (150,290,"Standard booth","標準攤位",None,22),
   (330,540,"Product showcase","產品展示",(330,610),22),
   (160,700,"Exclusive show prices","展場專屬價格",(350,610),20),
   (620,520,"Networking","人脈交流",(740,620),22),
   (1000,520,"Participating vendors","參展供應商",(1080,600),20),
   (1450,520,"Buyers","買家",(1330,640),24),
   (1000,880,"Display","展示",(1000,810),22),
   (1450,860,"Complimentary","免費贈送的",(1450,905),22)]
scene("toeic-4-4-a",fetch(c["url"]),L,"Photo: Pangalau, Wikimedia Commons (CC BY-SA 4.0)")
# ---- B: online vendor registration form ----
b=desk(420)
s,(sx,sy,sw,sh)=laptop(300,50,1000,780); b+=s
b+=window(sx,sy,sw,sh,"Vendor Registration — Online Form",color="#0f766e")
b+=T(sx+30,sy+80,"Register for the 2026 Trade Show · Business-to-business (B2B) vendors only",15,"#333",anchor="start")
fields=[("Supplier information","Wesley Office Supply Co."),("Wholesale account no.","WS-20481"),("Business license","BL-7731-TW"),("Tax ID","53-118820"),("Tax exemption certificate","Upload PDF ✓"),("Credit references","2 attached"),("Corporate orders / bulk purchases","Yes — 500+ units")]
for i,(k,v) in enumerate(fields):
    yy=sy+110+i*52
    b+=T(sx+30,yy+20,k,14,"#374151",anchor="start")+R(sx+330,yy,560,36,"#fff","#cbd5e1",1,rx=6)+T(sx+342,yy+24,v,14,"#111",anchor="start")
b+=R(sx+30,sy+485,860,60,"#ecfeff","#a5f3fc",1,rx=8)+T(sx+45,sy+510,"In order to set up your wholesale account, please complete all fields.",14,"#155e75",anchor="start")+T(sx+45,sy+532,"A deposit of $200 secures your booth; full payment is due 30 days before the show.",14,"#155e75",anchor="start")
b+=button(sx+30,sy+575,200,"Submit registration",color="#0f766e")+button(sx+250,sy+575,160,"Save & complete later",color="#64748b",size=12)
b+=label(150,90,"Register for","登記、註冊",size=22,line=(sx+110,sy+82))
b+=label(1450,90,"Online form","線上表單",size=22,line=(sx+900,sy+30))
b+=label(1470,180,"Business-to-business","企業對企業的（B2B）",size=18,line=(sx+560,sy+82))
b+=label(150,190,"Vendor registration","供應商註冊",size=20,line=(sx+250,sy+30))
b+=label(150,290,"Supplier information","供應商資訊",size=20,line=(sx+120,sy+130))
b+=label(150,380,"Wholesale account","批發帳戶",size=20,line=(sx+120,sy+182))
b+=label(150,470,"Business license","營業執照",size=20,line=(sx+110,sy+234))
b+=label(150,560,"Tax ID","稅籍編號",size=22,line=(sx+60,sy+286))
b+=label(150,650,"Tax exemption certificate","免稅證明",size=18,line=(sx+140,sy+338))
b+=label(150,740,"Credit references","信用證明",size=20,line=(sx+110,sy+390))
b+=label(160,840,"Bulk purchases","大量採購",size=20,line=(sx+230,sy+442))
b+=label(1450,290,"Corporate orders","企業訂單",size=20,line=(sx+890,sy+442))
b+=label(1450,400,"In order to set up","為了設立",size=20,line=(sx+890,sy+505))
b+=label(1450,500,"Deposit","訂金",size=22,line=(sx+890,sy+527))
b+=label(1450,600,"Secure","保留、確保",size=22,line=(sx+400,sy+545))
b+=label(1450,700,"Full payment","全額付款",size=22,line=(sx+560,sy+545))
b+=label(1450,800,"Complete","完成的",size=22,line=(sx+330,sy+592))
b+=vignette(); render("toeic-4-4-b",b)
# ---- C: confirmation email ----
b=desk(420)
s,(sx,sy,sw,sh)=laptop(300,60,1000,760); b+=s
b+=window(sx,sy,sw,sh,"Mail — Vendor registration confirmation",color="#475569")
lines_=["Dear Wesley Office Supply,",
"Your vendor registration has been received and is complete.",
"Confirmation number: TS-2026-0451",
"Once your registration is confirmed, you will receive your",
"vendor registration packet with setup instructions,",
"two vendor passes and complimentary parking passes.",
"Your booth number is 45 (premium, better positioned",
"near the main entrance). Electricity is included.",
"Please get in touch with our vendor coordinator, Ms. Park,",
"or the vendor services team for any questions.",
"Registration desk opens at 8 a.m. on show day.",
"— Trade Show Organizing Committee"]
marks=[(1,"has been received","Has been received","已收到","l"),(1,"complete","Complete","完成的","r"),(2,"Confirmation","Confirmation","確認","l"),
(3,"Once your registration is confirmed","Once your registration is confirmed","一旦您的註冊確認","r"),(4,"vendor registration packet","Vendor registration packet","供應商註冊資料袋","l"),(4,"setup instructions","Setup instructions","布置說明","r"),
(5,"vendor passes","Vendor pass","供應商通行證","l"),(5,"parking passes","Parking passes","停車證","r"),(6,"premium","Premium","進階的、高級的","l"),(6,"better positioned","Better positioned","位置較佳的","r"),
(8,"get in touch with","Get in touch with","聯繫","l"),(8,"vendor coordinator","Vendor coordinator","供應商協調員","r"),(9,"vendor services team","Vendor services team","供應商服務團隊","l"),(10,"Registration desk","Registration desk","註冊櫃檯","r")]
b+=textblock(sx+30,sy+90,lines_,size=17,gap=46,marks=marks,lsize=16,rx=1430)
b+=vignette(); render("toeic-4-4-c",b)
# ---- D: booth packages board ----
b=desk(720)
b+=f'<g filter="url(#sh)"><rect x="120" y="60" width="1360" height="600" rx="16" fill="#0f172a"/></g>'
b+=T(800,120,"EXHIBITOR PACKAGES · 2026 TRADE SHOW",30,"#fbbf24")
tiers=[("STANDARD BOOTH","$1,200","3m × 3m · directory listing · 1 vendor pass","#334155"),("PREMIUM BOOTH","$2,400","better positioned · electricity · 2 passes","#1d4ed8"),("PLATINUM BOOTH","$4,800","entrance location · buyer contact database · display support","#7c3aed")]
for i,(n,p,d,col) in enumerate(tiers):
    x=160+i*440
    b+=R(x,160,400,380,col,rx=14)+T(x+200,215,n,22,"#fff")+T(x+200,275,p,40,"#fff")
    for j,ln in enumerate(d.split(" · ")): b+=T(x+200,330+j*36,ln,15,"#e2e8f0",w="400")
    b+=R(x+120,470,160,40,"#fbbf24",rx=8)+T(x+200,496,"Special rates for early birds",11,"#111")
b+=T(800,600,"Exclusive show prices: participating vendors saved an average of 18% on bulk orders — savings averaged $3,400 per vendor.",15,"#cbd5e1",w="400")
b+=label(360,70,"Standard booth","標準攤位",size=22,line=(360,160))
b+=label(800,70,"Premium","進階的、高級的",size=22,line=(800,160))
b+=label(1240,70,"Platinum","白金級的（最高等級）",size=20,line=(1240,160))
def badge(x,y,n): return f'<circle cx="{x}" cy="{y}" r="13" fill="#dc2626" stroke="#fff" stroke-width="2"/>'+T(x,y+5,str(n),14,"#fff")
pts=[(470,366,1),(870,330,2),(870,366,3),(1310,366,4),(1310,402,5),(430,490,6),(430,598,7),(1000,598,8),(1200,598,9)]
for x,y,n in pts: b+=badge(x,y,n)
labs=[("1  Directory listing","名錄登載"),("2  Better positioned","位置較佳的"),("3  Electricity","電力"),("4  Buyer contact database","買家聯絡資料庫"),("5  Display","展示"),("6  Special rates","特殊優惠價格"),("7  Exclusive show prices","展場專屬價格"),("8  Averaged","平均達"),("9  Savings","節省（金額）")]
xs=[190,470,760,1060,1400]
for i,(en,zh) in enumerate(labs):
    r,cidx=divmod(i,5); b+=label(xs[cidx],770+r*100,en,zh,size=19)
b+=vignette(); render("toeic-4-4-d",b)
