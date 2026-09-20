from photo import *
import json
c=json.load(open('p54A.json'))
L=[(800,90,"Staff meeting","員工會議",None,30),
   (1300,300,"Briefing","簡報、說明",(900,380),24),
   (300,330,"Presentation skills","簡報技巧",(560,520),22),
   (1300,560,"Department heads","部門主管",(1050,560),22),
   (200,560,"Attendance","出席",(300,600),22),
   (600,930,"Take the meeting minutes","記錄會議紀錄",(560,840),20),
   (1200,930,"Meeting agenda","會議議程",(1180,800),22),
   (1400,760,"Conference call","電話會議",(1420,600),20)]
scene("toeic-5-4-a",fetch(c["url"]),L,"Photo: CECAR, Flickr (CC BY 2.0)")
c=json.load(open('p55A.json'))
L=[(700,80,"Certificate of Achievement","成就證書",(960,740),22),
   (200,200,"Honor","表揚",(720,520),26),
   (1200,120,"Recognition program","表彰計畫",None,22),
   (1450,560,"Award-winning","獲獎的",(1400,700),22),
   (250,900,"Received","獲得",(760,760),24),
   (1150,930,"Praise","讚揚",(1300,760),24),
   (600,930,"Dedication","投入、奉獻",(800,900),22)]
scene("toeic-5-5-a",fetch(c["url"]),L,"Photo: Khurram.Shahid, Wikimedia Commons (CC BY-SA 3.0)")
c=json.load(open('p44A.json'))
L=[(560,50,"Trade show","商展",(700,105),28),(1450,170,"Vendor booths","供應商攤位",(1350,290),24),(330,540,"Exhibition","展覽",(330,610),26)]
scene("toeic-5-3-a",fetch(c["url"]),L,"Photo: Pangalau, Wikimedia Commons (CC BY-SA 4.0)")
