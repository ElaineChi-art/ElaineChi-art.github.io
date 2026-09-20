from photo import *
import json; c=json.load(open('p51A.json'))
L=[(380,80,"Conference","研討會",(380,250),28),
   (1250,90,"Convention","大會",(1300,320),26),
   (500,560,"Industry leaders","產業領袖",(520,640),24),
   (1260,420,"Proposal","提案",(1260,480),24),
   (1130,930,"Strategic planning","策略規劃",(1130,760),22),
   (860,930,"Best practices","最佳實務",(860,580),22),
   (300,930,"Cooperation","合作",(380,760),22)]
scene("toeic-5-1-a",fetch(c["url"]),L,"Photo: CTBTO Photostream, Flickr (CC BY 2.0)")
