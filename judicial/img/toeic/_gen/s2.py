# -*- coding: utf-8 -*-
from gen import *
b=""
b+=R(0,0,W,H,"#eef1f5")+R(0,640,W,H-640,"#c9ced6")+R(0,0,W,70,"#dfe4ea")
# window
# team sign
b+=R(430,90,420,70,"#2c3e50",rx=8)+T(640,138,"CUSTOMER SERVICE",30,"#fff")
b+=label(640,40,"Customer service team","客服團隊",size=30)
# desk
b+=R(380,600,900,26,"#8a6b47")+R(400,626,20,260,"#6f5537")+R(1240,626,20,260,"#6f5537")
# monitor (order status)
b+=R(560,300,420,290,"#1f2a3a",rx=10)+R(575,315,390,250,"#fff")+R(740,590,60,40,"#4a5563")+R(700,628,140,10,"#4a5563",rx=4)
b+=R(575,315,390,36,"#3b82f6")+T(600,340,"ORDER STATUS",16,"#fff",anchor="start")
b+=f'<circle cx="940" cy="333" r="7" fill="#22c55e"/>'+T(925,338,"LIVE",12,"#fff",anchor="end")
b+=T(600,385,"Order number:",15,"#666",anchor="start")+T(760,385,"#ORD-48213",17,"#c0392b",anchor="start")
b+=T(600,420,"Shipment status:",15,"#666",anchor="start")+T(760,420,"In transit",17,"#2563eb",anchor="start")
b+=T(600,455,"Delivery option:",15,"#666",anchor="start")+R(760,438,180,26,"#f3f4f6","#999",1,rx=4)+T(770,457,"Standard ▾  Express",13,"#333",anchor="start")
b+=T(600,492,"Expected delivery:",15,"#666",anchor="start")+T(760,492,"Thu, 3 business days",15,"#111",anchor="start")
b+=R(600,515,120,34,"#e5e7eb",rx=6)+T(660,538,"⟳ Update",14,"#111")
b+=R(740,515,200,34,"#16a34a",rx=6)+T(840,538,"✓ Guaranteed",14,"#fff")
b+=label(770,230,"Order number","訂單編號",size=24,line=(790,372))
b+=label(1000,230,"Shipment status","貨件狀態",size=24,line=(830,410))
b+=label(1110,305,"Real-time updates","即時更新",size=22,line=(945,326))
b+=label(1120,470,"Delivery option","配送方式",size=22,line=(945,451))
b+=label(1160,570,"Expected delivery date","預計送達日期",size=20,line=(960,490))
b+=label(470,490,"Update","更新（資訊）",size=22,line=(660,552))
b+=label(1000,690,"Guaranteed","保證的",size=22,line=(840,552))
# agent with headset
b+=person(110,470,shirt="#2c5f8a",scale=.85)
b+=f'<path d="M88,458 a22,22 0 0 1 44,0" stroke="#111" stroke-width="6" fill="none"/><rect x="128" y="455" width="9" height="18" rx="3" fill="#111"/><line x1="132" y1="473" x2="120" y2="488" stroke="#111" stroke-width="4"/>'
# speech bubble unfortunately / on our end
b+=f'<path d="M290,330 h330 a12,12 0 0 1 12,12 v90 a12,12 0 0 1 -12,12 h-250 l-30,28 v-28 h-50 a12,12 0 0 1 -12,-12 v-90 a12,12 0 0 1 12,-12z" fill="#fff" stroke="#9aa5b1" stroke-width="3"/>'
b+=T(305,362,"Unfortunately, there's a delay —",16,"#c0392b",anchor="start")
b+=T(305,390,"the delay was on our end.",16,"#333",anchor="start")
b+=T(305,418,"We'll update you within the hour.",16,"#333",anchor="start")
b+=label(150,220,"Unfortunately","很遺憾地",size=24,line=(300,348))
b+=label(170,120,"Delay was on our end","延誤是我方造成的",size=20,line=(340,392))
b+=label(300,560,"Within the hour","一小時內",size=22,line=(320,422))
# clock
b+=f'<circle cx="480" cy="230" r="34" fill="#fff" stroke="#333" stroke-width="5"/><line x1="480" y1="230" x2="480" y2="206" stroke="#333" stroke-width="5"/><line x1="480" y1="230" x2="500" y2="240" stroke="#333" stroke-width="5"/>'
# email window (right top)
b+=R(1230,90,330,190,"#fff","#9aa5b1",3,rx=8)+R(1230,90,330,30,"#e5e7eb",rx=8)+T(1245,111,"✉ Confirmation email",14,"#333",anchor="start")
b+=T(1245,150,"Subject: Order #ORD-48213 confirmed",13,"#111",anchor="start")
b+=T(1245,175,"Your order has been processed.",13,"#333",anchor="start")
b+=T(1245,200,"Tracking updates will follow.",13,"#333",anchor="start")
b+=T(1245,255,"— This email was automatically generated —",11,"#888",anchor="start")
b+=label(1395,40,"Confirmation email","確認郵件",size=24)
b+=label(1420,340,"Automatically generated","自動產生的",size=20,line=(1395,258))
# notification bell
b+=f'<path d="M1120,120 a30,30 0 0 1 60,0 v28 l12,16 h-84 l12,-16z" fill="#f59e0b"/><circle cx="1150" cy="172" r="8" fill="#f59e0b"/><circle cx="1178" cy="112" r="12" fill="#ef4444"/>'+T(1178,117,"3",14,"#fff")
b+=label(990,50,"Confirmations","確認通知",size=22,line=(1130,118))
# invoice docs (left bottom, on desk)
b+=R(60,660,200,260,"#fff","#999",2)+T(160,695,"INVOICE",22,"#111")+T(160,718,"No. INV-2024-0917",12,"#666")
for i in range(6): b+=R(80,740+i*22,160,8,"#d1d5db")
b+=R(90,880,140,28,"#fff","#16a34a",3,rx=4)+T(160,900,"VALID ✓",16,"#16a34a")
b+=R(300,690,200,230,"#fff","#999",2)+T(400,725,"INVOICE",22,"#111")+R(330,735,140,26,"#fbbf24",rx=4)+T(400,753,"UPDATED v2",14,"#111")
for i in range(5): b+=R(320,780+i*22,160,8,"#d1d5db")
b+=R(540,720,200,200,"#f9fafb","#999",2)+T(640,755,"INVOICE",22,"#9ca3af")+T(640,830,"COPY",40,"#d1d5db")
b+=label(210,630,"Invoice","發票",size=26,line=(160,660))
b+=label(400,640,"Updated invoice","更新後的發票",size=22,line=(400,690))
b+=label(700,690,"Invoice copy","發票副本",size=22,line=(640,720))
b+=label(120,960,"Valid","有效的",size=24,line=(160,910))
# calendar (right)
b+=R(1300,640,270,250,"#fff","#9aa5b1",3,rx=8)+R(1300,640,270,40,"#ef4444",rx=8)+T(1435,668,"SEPTEMBER",18,"#fff")
days=["M","T","W","T","F","S","S"]
for i,d in enumerate(days): b+=T(1322+i*38,705,d,13,"#666")
n=1
for r in range(4):
    for c in range(7):
        x=1322+c*38; y=735+r*36
        if n<=28:
            col="#111" if c<5 else "#bbb"
            if n in (15,16,17,18,19): b+=R(x-16,y-22,32,30,"#dbeafe",rx=4)
            if n==18: b+=f'<circle cx="{x}" cy="{y-7}" r="16" fill="none" stroke="#ef4444" stroke-width="4"/>'
            b+=T(x,y,str(n),14,col)
        n+=1
b+=label(1430,590,"Business days","工作日",size=22,line=(1400,712))
b+=label(1180,780,"By Thursday","週四前",size=22,line=(1436,736))
render("toeic-4-1-b",b)
