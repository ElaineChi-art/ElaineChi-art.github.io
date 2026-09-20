# -*- coding: utf-8 -*-
from props import *
from photo import scene,fetch
import json
c=json.load(open("p43A.json"))
L=[(620,110,"Receipt","收據",(560,335)),
   (900,90,"Process your payment","處理您的付款",(720,240),22),
   (300,930,"Valued customers","尊貴的顧客",(300,720),22),
   (150,300,"Company credit card","公司信用卡",(500,380),20),
   (280,500,"Payment methods","付款方式",(545,432),22),
   (1150,150,"Incredible","驚人的",(1290,250),22),
   (1450,160,"Promotions","促銷活動",(1400,270),22),
   (960,600,"Special offer","特別優惠",(940,520)),
   (1300,720,"Select items","精選商品",(1250,640),22),
   (560,800,"Clearance sale","清倉特賣",(560,700),22),
   (820,700,"Store gift cards","商店禮品卡",(640,590),20),
   (1480,80,"Branch","分公司",None,22)]
scene("toeic-4-3-a",fetch(c["url"]),L,"Photo: Tessa Bury (CC BY 4.0)")
# ---- B: sale flyer + coupon ----
b=desk(330)
b+=paper(120,90,560,760,rot=-3,fill="#fff7ed")
b+=R(140,110,520,110,"#dc2626")+T(400,160,"CLEARANCE SALE",44,"#fff")+T(400,200,"THIS WEEKEND ONLY",20,"#fde68a")
b+=T(400,300,"30% OFF",70,"#dc2626")+T(400,340,"select items",22,"#7c2d12")
b+=T(400,400,"Incredible savings for our valued customers",16,"#333")
b+=R(160,430,480,60,"#fef3c7",rx=8)+T(400,468,"FLAT RATE shipping $9.99 — regardless of size",16,"#78350f")
b+=T(400,540,"Exclusive in-store promotion",18,"#111")
b+=T(400,580,"Cannot be combined with other promotions.",14,"#555")
b+=T(400,610,"Free of charge gift wrapping on purchases exceeding $100.",14,"#555")
b+=T(400,700,"Wesley Office Supply · Downtown Branch",14,"#777")
b+=end()
b+=label(400,40,"Clearance sale","清倉特賣",size=28,line=(400,110))
b+=label(820,190,"This weekend only","僅限本週末",size=22,line=(600,200))
b+=label(820,290,"30 percent off","打 7 折、減 30%",size=24,line=(560,300))
b+=label(820,380,"Select items","精選商品",size=22,line=(500,340))
b+=label(820,470,"Flat rate","統一費率／統一價",size=22,line=(640,465))
b+=label(830,560,"Regardless of","不論",size=22,line=(640,475))
b+=label(880,650,"Cannot be combined with","不可與…併用",size=20,line=(640,585))
b+=label(160,770,"Exclusive","專屬的",size=22,line=(300,545))
b+=label(870,740,"Exceeding","超過",size=22,line=(650,612))
b+=label(870,830,"Free of charge","免費",size=22,line=(280,612))
# coupon
b+=f'<g transform="rotate(6 1300 500)" filter="url(#sh)"><rect x="1080" y="400" width="440" height="220" rx="12" fill="#fff" stroke="#16a34a" stroke-width="6" stroke-dasharray="14,8"/></g>'
b+=f'<g transform="rotate(6 1300 500)">'+T(1300,450,"CORPORATE COUPON",22,"#16a34a")+T(1300,510,"ADDITIONAL 10% OFF",30,"#111")+T(1300,545,"Apply code CORP10 at checkout",14,"#555")+T(1300,585,"Valid to 12/31 · Present with receipt",12,"#777")+end()
b+=label(1300,300,"Corporate coupon","企業優惠券",size=24,line=(1180,405))
b+=label(1180,760,"Additional 10% off","額外再折 10%",size=22,line=(1230,530))
b+=label(1450,760,"Apply","套用（優惠）",size=22,line=(1300,575))
b+=label(1300,900,"Accompanied by","附上",size=22,line=(1380,610))
b+=vignette(); render("toeic-4-3-b",b)
# ---- C: receipt + invoice ----
b=desk(300)
# receipt (thermal)
b+=paper(160,60,400,880,rot=2,fill="#fff")
b+=T(360,110,"WESLEY OFFICE SUPPLY",18,"#111")+T(360,132,"Downtown Branch · #0021",12,"#666")+R(190,150,340,1,"#999")
rows=[("Ergo Chair X2  ×3",""),("  original unit price $40.00","120.00"),("Bulk discount (3+)","-12.00"),("SUBTOTAL (before tax)","108.00"),("Corporate coupon CORP10 applied","-10.80"),("After both discounts","97.20"),("Tax amount 5%","4.86"),("Shipping charge","FREE"),("TOTAL CHARGES","102.06"),("Paid: company credit card ****4471","")]
y=185
for k,v in rows:
    bold=k.isupper() or k.startswith("TOTAL")
    b+=T(200,y,k,14 if not bold else 15,"#111",w="700" if bold else "400",anchor="start")+T(520,y,v,14,"#111",anchor="end")
    y+=44
b+=R(190,y-20,340,1,"#999")+T(360,y+10,"Prices exclude tax unless stated",11,"#777")+T(360,y+30,"Keep this receipt for returns",11,"#777")
b+=end()
b+=label(360,20,"Receipt","收據",size=26,line=(360,60))
b+=label(760,240,"Original unit price","原本的單價",size=22,line=(520,224))
b+=label(760,320,"Bulk discount","大量折扣",size=22,line=(520,268))
b+=label(760,400,"Subtotal","小計",size=22,line=(520,312))
b+=label(760,480,"Before tax","稅前",size=22,line=(400,312))
b+=label(780,560,"Applied","套用",size=22,line=(520,356))
b+=label(780,640,"After both discounts","兩次折扣後",size=20,line=(520,400))
b+=label(760,720,"Tax amount","稅額",size=22,line=(520,444))
b+=label(760,800,"Shipping charge","運費",size=22,line=(520,488))
b+=label(760,880,"Total charges","總費用",size=22,line=(520,532))
b+=label(520,960,"Exclude tax","不含稅",size=20,line=(360,650))
# invoice
b+=paper(1000,100,520,640,rot=-2)
b+=R(1020,120,480,60,"#1e3a5f")+T(1040,158,"INVOICE",22,"#fff",anchor="start")+T(1480,158,"No. 2026-0917",13,"#cbd5e1",anchor="end")
b+=T(1040,215,"Bill to: Elaine Chi · Account #4471",13,"#333",anchor="start")
b+=T(1040,240,"Payment due: within three business days",13,"#dc2626",anchor="start")
inv=[("Unit cost","$36.00"),("Qty","25"),("Amount","$900.00"),("Bank transfer fee","$0.00"),("Late payment fee (after 30 days)","2%")]
for i,(k,v) in enumerate(inv):
    b+=R(1040,265+i*40,440,32,"#f8fafc" if i%2 else "#fff",rx=4)+T(1052,287+i*40,k,13,"#333",anchor="start")+T(1470,287+i*40,v,13,"#111",anchor="end")
b+=T(1040,505,"Payment methods: bank transfers · company credit card",12,"#555",anchor="start")
b+=T(1040,528,"Installment plans available on orders over $500",12,"#555",anchor="start")
b+=T(1040,551,"Free of charge delivery within the city",12,"#555",anchor="start")
b+=stamp(1380,640,"PAID",color="#16a34a",rot=-14)
b+=end()
b+=label(1130,50,"Invoice","發票",size=26,line=(1200,110))
b+=label(1420,50,"Within three business days","三個工作天內",size=18,line=(1440,232))
b+=label(1150,820,"Unit cost","單價",size=22,line=(1090,300))
b+=label(1380,820,"Bank transfers","銀行轉帳",size=22,line=(1300,504))
b+=label(1180,900,"Installment plans","分期付款方案",size=20,line=(1300,527))
b+=label(1440,900,"Late payment fees","滯納金",size=20,line=(1470,428))
b+=vignette(); render("toeic-4-3-c",b)
# ---- D: email about pricing discrepancy ----
b=desk(420)
s,(sx,sy,sw,sh)=laptop(300,60,1000,760); b+=s
b+=window(sx,sy,sw,sh,"Mail — Re: Inquiry about pricing discrepancy",color="#475569")
b+=T(sx+30,sy+70,"From: billing@wesleysupply.com   To: elaine@company.com",13,"#666",anchor="start")
lines_=["Dear Ms. Chi,",
"Thank you for your inquiry regarding the",
"pricing discrepancy on your account #4471.",
"We would like to clarify: the unit cost on your",
"invoice reflects the bulk discount, but the",
"corporate coupon had expired, so it was not applied.",
"As a one-time courtesy discount, we will reduce",
"the total by 10% and refund $12.00, credited to",
"your original payment method within three business days.",
"Your payment history shows you qualify for installment plans.",
"Please confirm acceptance by replying to this email.",
"We value your continued business and are committed",
"to customer satisfaction.",
"Best regards, Billing Team"]
marks=[(1,"inquiry","Inquiry","詢問","r"),(2,"pricing discrepancy","Pricing discrepancy","價格差異、價格不符","l"),(2,"account","Account","帳戶","r"),
(3,"clarify","Clarify","釐清","l"),(4,"reflects","Reflects","反映","r"),(5,"expired","Expired","過期","l"),(5,"applied","Applied","套用","r"),
(6,"one-time courtesy discount","One-time courtesy discount","一次性禮遇折扣","l"),(6,"reduce","Reduce","降低","r"),(7,"refund","Refund","退款","r"),(7,"credited to","Credited to","退回（款項）至","l"),
(8,"original payment method","Original payment method","原付款方式","l"),(8,"within three business days","Within three business days","三個工作天內","r"),
(9,"payment history","Payment history","付款紀錄","l"),(9,"qualify for","Qualify for","符合…資格","r"),
(10,"confirm acceptance","Confirm acceptance","確認接受","l"),(11,"continued business","Continued business","持續的惠顧","r"),(12,"customer satisfaction","Customer satisfaction","顧客滿意","l")]
b+=textblock(sx+30,sy+120,lines_,size=17,gap=44,marks=marks)
b+=vignette(); render("toeic-4-3-d",b)
# ---- E: return policy sign at counter ----
b=desk(700)
b+=f'<g filter="url(#sh)"><rect x="300" y="80" width="1000" height="580" rx="16" fill="#1f2937"/></g>'+R(320,100,960,540,"#111827",rx=10)
b+=T(800,160,"RETURN & PAYMENT POLICY",30,"#fbbf24")
pol=["• Returns accepted within 14 days, accompanied by the original receipt.",
"• Refunds are credited to the original payment method.",
"• Store gift cards cannot be exchanged for cash.",
"• Payment methods: cash · company credit card · bank transfers.",
"• Late payment fees apply to invoices exceeding 30 days.",
"• Installment plans: qualify for 0% interest on orders over $500.",
"• Corporate coupons cannot be combined with clearance promotions."]
for i,ln in enumerate(pol): b+=T(360,225+i*52,ln,18,"#e5e7eb",w="400",anchor="start")
b+=label(230,110,"Return","退貨",size=24,line=(420,218))
b+=label(1420,140,"Accompanied by","附上",size=20,line=(1000,218))
b+=label(160,300,"Refund","退款",size=24,line=(400,270))
b+=label(1430,300,"Store gift cards","商店禮品卡",size=20,line=(560,322))
b+=label(160,480,"Payment methods","付款方式",size=20,line=(480,374))
b+=label(1430,440,"Exceeding","超過",size=22,line=(1080,426))
b+=label(160,640,"Qualify for","符合…資格",size=22,line=(660,478))
b+=label(1440,600,"Promotions","促銷活動",size=22,line=(1130,530))
b+=label(800,760,"Customer satisfaction guaranteed","顧客滿意保證",size=22)
b+=vignette(); render("toeic-4-3-e",b)
