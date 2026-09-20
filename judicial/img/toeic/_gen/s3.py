# -*- coding: utf-8 -*-
from gen import *
b=""
b+=R(0,0,W,H,"#f3efe6")+R(0,700,W,H-700,"#d8d0c0")
# big rate board
b+=R(80,90,620,560,"#1f2a3a",rx=14)+T(390,150,"SHIPPING FEES",40,"#f1c40f")+T(390,190,"Commercial Rate Card · Starting Oct 1",18,"#cfd8e3")
b+=label(390,45,"Shipping fees","運費",size=30)
b+=label(660,150,"Starting","從…起",size=22,line=(556,192))
rows=[("Standard shipment","$8.00"),("Express delivery","$15.00"),("Urgent / same-day","$29.00")]
for i,(n,p) in enumerate(rows):
    y=250+i*60
    b+=R(120,y-30,540,48,"#2c3e50",rx=8)+T(140,y+2,n,20,"#fff",anchor="start")+T(640,y+2,p,22,"#f1c40f",anchor="end")
# flat rate + $20
b+=R(120,410,540,70,"#16a34a",rx=8)+T(140,455,"FLAT RATE  ·  any size, any weight",20,"#fff",anchor="start")+T(640,457,"$20",30,"#fff",anchor="end")
# additional fee
b+=R(120,500,540,48,"#7f1d1d",rx=8)+T(140,532,"+ Additional shipping fee (remote area)",18,"#fff",anchor="start")+T(640,532,"+$5",20,"#fca5a5",anchor="end")
b+=label(180,610,"Additional shipping fee","額外運費",size=22,line=(200,548))
b+=label(250,700,"Flat","統一的（費率）",size=24,line=(300,480))
b+=label(660,45,"Twenty dollar","20 美元的",size=22,line=(632,412))
# reduce arrow
b+=f'<path d="M620,560 v70 m-20,-20 l20,20 l20,-20" stroke="#16a34a" stroke-width="8" fill="none"/>'
b+=label(560,690,"Reduce","降低",size=24,line=(620,632))
# clients (right): three tiers
b+=R(760,90,780,560,"#fff","#c9c2b4",4,rx=14)+T(1150,140,"B2B CLIENT PROGRAM",28,"#1f2a3a")
# commercial customers row
for i in range(3): b+=person(830+i*80,230,shirt="#374151",scale=.6)+R(818+i*80,258,24,20,"#8b5e3c",rx=3)
b+=T(950,340,"Commercial customers",18,"#333",anchor="start")
b+=label(1240,200,"Commercial customers","商業客戶",size=22,line=(1120,335))
# large-volume with boxes
b+=box(830,420,50,40,0)+box(885,420,50,40,1)+box(940,420,50,40,2)+box(858,375,50,40,1)+box(913,375,50,40,0)
b+=T(1010,450,"Large-volume customers",18,"#333",anchor="start")
b+=label(1350,395,"Large-volume customers","大量採購客戶",size=22,line=(1200,445))
# high-volume clients vip
b+=R(820,500,180,70,"#f1c40f",rx=8)+T(910,530,"VIP",26,"#1f2a3a")+T(910,556,"HIGH-VOLUME",14,"#1f2a3a")
b+=T(1010,545,"High-volume clients",18,"#333",anchor="start")
b+=label(1330,520,"High-volume clients","大量採購客戶",size=22,line=(1190,540))
# special rates tag
b+=f'<path d="M1030,590 h150 l25,25 l-25,25 h-150z" fill="#ef4444"/>'+T(1105,622,"SPECIAL RATES",15,"#fff")
b+=label(1400,600,"Special rates","特殊費率",size=22,line=(1190,615))
# exclusively badge
b+=f'<circle cx="1470" cy="330" r="44" fill="#7c3aed"/>'+T(1470,325,"ONLY",16,"#fff")+T(1470,345,"B2B",14,"#fff")
b+=label(1470,200,"Exclusively","專門地、僅",size=22,line=(1470,286))
# account manager (bottom right)
b+=person(1420,760,shirt="#1d4ed8")
b+=R(1370,880,100,30,"#fff","#333",2,rx=4)+T(1420,900,"ACCOUNT MGR",11,"#111")
b+=label(1330,700,"Dedicated account management","專屬帳戶管理",size=20,line=(1420,735))
# route map (bottom center) customized logistics
b+=R(720,730,520,240,"#fff","#c9c2b4",4,rx=10)+T(980,762,"CUSTOM ROUTE PLAN",16,"#333")
b+=f'<path d="M760,900 C820,800 900,950 980,840 S1120,780 1200,900" stroke="#3b82f6" stroke-width="6" fill="none" stroke-dasharray="12,8"/>'
for x,y in [(760,900),(980,840),(1200,900)]: b+=f'<circle cx="{x}" cy="{y}" r="12" fill="#ef4444" stroke="#fff" stroke-width="3"/>'
b+=T(760,935,"Hub A",12,"#333")+T(980,875,"Client site",12,"#333")+T(1200,935,"Port",12,"#333")
b+=label(950,690,"Customized logistics solutions","客製化物流方案",size=20,line=(980,730))
# as usual badge (left bottom)
b+=R(80,760,300,90,"#fff","#c9c2b4",4,rx=10)+T(230,800,"Delivered on time",18,"#333")+T(230,830,"— as usual ✓",18,"#16a34a")
b+=label(230,900,"As usual","照常",size=24,line=(230,850))
render("toeic-4-1-c",b)
