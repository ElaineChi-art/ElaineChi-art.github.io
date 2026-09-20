# -*- coding: utf-8 -*-
from gen import *
b=""
# background wall + floor
b+=R(0,0,W,H,"#e6e9ee")
b+=R(0,0,W,80,"#3b4250")  # ceiling beam
for i in range(0,W,160): b+=R(i+40,10,80,60,"#4a5262")
b+=R(0,620,W,H-620,"#b8bec8")
b+=f'<path d="M0,620 L{W},620 L{W},640 L0,640z" fill="#9aa2ae"/>'
# big sign
b+=R(560,100,500,86,"#1f2a3a",rx=10)+T(810,158,"DISTRIBUTION CENTER",40,"#fff")
b+=label(780,60,"Distribution center","配送中心",size=32)
# wholesale division door (left)
b+=R(70,260,170,360,"#8b97a7","#5c6674",4)+R(90,280,130,320,"#6e7a8c")+f'<circle cx="205" cy="450" r="7" fill="#e5c86b"/>'
b+=R(60,205,190,44,"#2c3e50",rx=6)+T(155,236,"WHOLESALE DIVISION",18,"#fff")
b+=label(155,140,"Wholesale division","批發部門",size=26,line=(155,205))
# schedule whiteboard (arrange)
b+=R(290,170,240,170,"#fdfdfd","#7d8794",4,rx=4)+T(410,200,"DELIVERY SCHEDULE",17,"#334")
for i,(d,t) in enumerate([("MON","09:00 A-12"),("TUE","10:30 B-07"),("WED","14:00 C-03"),("THU","08:00 A-19")]):
    b+=T(318,233+i*26,d,15,"#2a5db0",anchor="start")+T(372,233+i*26,t,15,"#333",anchor="start")
b+=label(410,110,"Arrange","安排",size=26,line=(410,170))
# purchase order clipboard
b+=R(1040,150,150,190,"#8a6b47",rx=8)+R(1052,175,126,158,"#fff")+R(1085,140,60,24,"#555",rx=4)
b+=T(1115,202,"PURCHASE ORDER",12,"#222")+T(1115,222,"PO-2024-0917",12,"#c0392b")
for i in range(5): b+=R(1062,235+i*16,106,6,"#ccd")
b+=label(1180,80,"Purchase order","採購單",size=26,line=(1115,142))
# racking with boxes (background, center-left)
for r,y in enumerate([300,420,540]):
    b+=R(560,y,420,10,"#6d7684")
    for i in range(4): b+=box(575+i*105,y-70,85,70,(i+r)%3)
b+=R(555,240,10,380,"#6d7684")+R(985,240,10,380,"#6d7684")
# pallet with bulk boxes (left-center)
px,py=300,470
b+=R(px-10,py+150,240,22,"#8f6337")
for r in range(3):
    for i in range(3): b+=box(px+i*72,py+150-(r+1)*50,66,48,(r+i)%3)
b+=R(px+150,py-20,90,34,"#c0392b",rx=6)+T(px+195,py+4,"500+ units",15,"#fff")
b+=label(410,400,"Bulk orders","大量訂單",size=28,line=(410,470))
b+=label(668,400,"Over 500 units","超過 500 件",size=24,line=(px+245,py-3))
# conveyor belt across
b+=R(600,700,760,60,"#3c3f45",rx=8)+R(600,760,760,16,"#7b7f88")
for i in range(9): b+=f'<circle cx="{640+i*90}" cy="790" r="12" fill="#5b5f68"/>'
for i in range(6): b+=R(620+i*126,706,90,48,"#55595f",rx=4)
# boxes on belt
b+=box(640,640,120,64,0)+R(655,652,90,20,"#ffffff")+T(700,667,"STANDARD",12,"#2c3e50")
b+=label(700,585,"Standard shipment","標準運送",size=26,line=(700,640))
b+=box(820,640,120,64,1)+R(835,648,92,26,"#c0392b",rx=4)+T(881,667,"EXPRESS",14,"#fff")
b+=label(890,505,"Express delivery","快遞",size=26,line=(880,640))
b+=box(1000,640,120,64,2)+f'<polygon points="1108,600 1160,612 1108,624" fill="#e74c3c"/><rect x="1104" y="596" width="6" height="48" fill="#8e2b21"/>'
b+=T(1060,678,"URGENT",14,"#c0392b")
b+=label(1010,415,"Urgent shipments","緊急貨件",size=26,line=(1108,598))
# expedited lane sign
b+=R(1160,636,180,56,"#f39c12",rx=8)+T(1250,672,"⚡ EXPEDITED",20,"#fff")
b+=label(1230,540,"Expedited service","加急服務",size=26,line=(1250,636))
# worker scanning box with tracking label
b+=box(1000,860,150,90,0)+R(1015,875,120,44,"#fff")
for i in range(18): b+=R(1022+i*6,880,3 if i%3 else 2,22,"#111")
b+=T(1075,914,"TRK 1Z 884 220 71",10,"#333")
b+=person(1230,760,shirt="#5b4a3b")
b+=f'<rect x="1175" y="800" width="60" height="22" rx="6" fill="#2c3e50" transform="rotate(-20 1205 811)"/><line x1="1170" y1="822" x2="1140" y2="880" stroke="#e74c3c" stroke-width="3" stroke-dasharray="6,5"/>'
b+=label(1075,810,"Tracking number","追蹤號碼",size=24,line=(1075,875))
b+=label(1420,760,"Process","處理",size=26,line=(1262,790))
# processed box with green check
b+=box(690,860,140,90,1)+f'<circle cx="760" cy="905" r="30" fill="#27ae60"/><path d="M744,905 l12,12 l22,-24" stroke="#fff" stroke-width="6" fill="none"/>'
b+=label(760,815,"Has been processed","已處理完成",size=22,line=(760,860))
# on-hold shelf: hasn't shipped yet + delay
b+=R(70,720,220,12,"#6d7684")+box(90,650,110,70,2)+R(80,740,200,40,"#e8e8e8",rx=4)+T(180,767,"ON HOLD",18,"#7f8c8d")
b+=f'<circle cx="240" cy="670" r="30" fill="#fff" stroke="#c0392b" stroke-width="5"/><line x1="240" y1="670" x2="240" y2="650" stroke="#c0392b" stroke-width="5"/><line x1="240" y1="670" x2="256" y2="678" stroke="#c0392b" stroke-width="5"/>'
b+=label(150,590,"Hasn't shipped yet","尚未出貨",size=24,line=(145,650))
b+=label(300,820,"Delay","延誤",size=26,line=(262,700))
# truck at dock (right)
b+=R(1390,300,210,320,"#2f3a4a")  # dock opening
b+=R(1405,380,195,190,"#f4f6f8","#9aa5b1",4,rx=6)+R(1405,560,195,30,"#7f8c8d")
b+=R(1420,450,165,60,"#1f2a3a",rx=4)+T(1502,490,"CARRIER",26,"#f1c40f")
b+=T(1502,425,"PRIMARY",18,"#2c3e50")
b+=f'<circle cx="1440" cy="600" r="24" fill="#222"/><circle cx="1565" cy="600" r="24" fill="#222"/>'
b+=f'<path d="M1370,660 h150 m-30,-18 l30,18 l-30,18" stroke="#e67e22" stroke-width="8" fill="none"/>'
b+=label(1450,330,"Primary carrier","主要承運商",size=26,line=(1500,380))
b+=label(1440,880,"Leaves our facility","離開設施（出貨）",size=24,line=(1450,668))
render("toeic-4-1-a",b)
