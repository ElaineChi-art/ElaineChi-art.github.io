# -*- coding: utf-8 -*-
from docs import *
from photo import scene,fetch
import json
M=lambda i,ph,en,zh:(i,ph,en,zh,"l")
P=lambda k:fetch(json.load(open(f'p{k}A.json'))["url"])
scene("toeic-13-1-a",P("131"),[(240,120,"Backup system","備份系統",(240,400),24),(1280,120,"Cloud storage","雲端儲存",(1280,400),24),(800,80,"Upgraded platform","升級平台",None,26),
 (800,930,"System overhaul","系統全面改造",(800,800),22),(300,930,"Secure document access","安全的文件存取",(300,700),20),(1300,930,"Enhanced security features","增強的安全功能",(1300,700),20),(800,300,"Access control","門禁控制",(800,400),22)],
 "Photo: Christopher Bowns, Wikimedia Commons (CC BY-SA 2.0)")
scene("toeic-13-2-a",P("132"),[(250,700,"Help desk","技術支援台",(450,840),26),(528,430,"Troubleshooting ticket","故障排除工單",(528,536),20),(1200,200,"Extension 5544","分機 5544",(1200,360),22),
 (560,300,"Specialist team","專家團隊",(560,440),22),(1200,930,"Security protocols","安全協定",(1200,700),22),(176,150,"Reset credentials","重設登入憑證",(176,280),20),(1450,930,"Investigation","調查",(1360,600),24)],
 "Photo: Fanti Salms, Wikimedia Commons (CC BY-SA 4.0)")
scene("toeic-13-3-a",P("73"),[(800,70,"Tutorial","教學課程",None,28),(250,930,"Instructor","講師",(400,780),24),(480,930,"Hands-on","實作的",(480,620),24),(300,150,"Database system","資料庫系統",(290,450),22),
 (1300,700,"Demonstration","操作示範",(1000,500),24),(1300,200,"Orientation","新人訓練",(1100,300),24),(1200,900,"Assessment","測驗、評估",(1152,660),24)],
 "Photo: sridgway, Flickr (CC BY 2.0)")
scene("toeic-13-4-a",P("134"),[(800,80,"Wearable devices","穿戴式裝置",(790,340),28),(300,300,"Intuitive interface","直覺的介面",(720,400),22),(1300,200,"Prototype","原型、樣機",(1100,250),24),
 (1300,700,"Functionality features","功能特點",(900,450),20),(300,900,"Performance","效能、表現",(500,650),22),(1000,930,"Beta testing","測試版測試",(850,600),22),(1300,900,"Breakthrough design","突破性設計",None,20)],
 "Photo: Crew, Wikimedia Commons (CC0)")
make_doc("toeic-13-1-b","email","Mail — IT: system overhaul this weekend",
["We will launch the upgraded platform with enhanced security features and cloud storage.",
"The system overhaul (weekend of April 18-19) will modernize access control with biometric readers and secure document access;",
"software installation runs in phases from midnight and should complete by 6 AM.",
"Before leaving today, disconnect peripheral devices (printer and scanner); this will not affect the backup system.",
"The vendor will monitor the transition; the diagnostic tool will undergo testing by Friday."],
[M(0,"launch","Launch","推出"),M(0,"upgraded platform","Upgraded platform","升級平台"),M(0,"enhanced security features","Enhanced security features","增強的安全功能"),M(0,"cloud storage","Cloud storage","雲端儲存"),
M(1,"system overhaul","System overhaul","系統全面改造"),M(1,"weekend of April 18-19","Weekend of April 18-19","4/18-19 週末"),M(1,"modernize","Modernize","使現代化"),M(1,"access control","Access control","門禁控制"),M(1,"biometric readers","Biometric readers","生物識別讀取器"),M(1,"secure document access","Secure document access","安全的文件存取"),
M(2,"software installation","Software installation","軟體安裝"),M(2,"in phases","In phases","分階段地"),M(2,"midnight","Midnight","午夜"),M(2,"complete by 6 AM","Complete by 6 AM","早上 6 點前完成"),
M(3,"Before leaving today","Before leaving today","今天下班前"),M(3,"peripheral devices","Peripheral devices","周邊裝置"),M(3,"printer and scanner","Printer and scanner","印表機與掃描器"),M(3,"affect","Affect","影響"),M(3,"backup system","Backup system","備份系統"),
M(4,"vendor","Vendor","供應商"),M(4,"monitor the transition","Monitor the transition","監控轉換過程"),M(4,"diagnostic tool","Diagnostic tool","診斷工具"),M(4,"undergo testing","Undergo testing","接受測試"),M(4,"by Friday","By Friday","週五前")],
subtitle="From: it-department@company.com")
make_doc("toeic-13-2-b","email","Mail — Troubleshooting ticket #5544: authentication errors",
["Several users reported authentication errors after the server malfunction; the help desk opened a troubleshooting ticket.",
"Troubleshooting steps: reset credentials, use the temporary password we sent, and retrieve files from the weekly backup.",
"The specialist team is leading the investigation; security protocols require your identification number.",
"Temporary passwords expire in 24 hours — change them before Friday. Questions: extension 5544.",
"If the malfunction continues, submit a new ticket with your credentials."],
[M(0,"reported","Reported","回報"),M(0,"authentication errors","Authentication errors","身份驗證錯誤"),M(0,"server malfunction","Server malfunction","伺服器故障"),M(0,"help desk","Help desk","技術支援台"),M(0,"troubleshooting ticket","Troubleshooting ticket","故障排除工單"),
M(1,"Troubleshooting","Troubleshooting","故障排除"),M(1,"reset credentials","Reset credentials","重設登入憑證"),M(1,"temporary password","Temporary password","臨時密碼"),M(1,"retrieve","Retrieve","取回"),M(1,"weekly backup","Weekly backup","每週備份"),
M(2,"specialist team","Specialist team","專家團隊"),M(2,"investigation","Investigation","調查"),M(2,"security protocols","Security protocols","安全協定"),M(2,"identification number","Identification number","識別號碼"),
M(3,"expire","Expire","到期"),M(3,"before Friday","Before Friday","週五前"),M(3,"extension 5544","Extension 5544","分機 5544"),M(4,"malfunction","Malfunction","故障"),M(4,"credentials","Credentials","登入憑證")],
subtitle="From: helpdesk@company.com")
make_doc("toeic-13-3-b","paper","TRAINING PORTAL — Database system certification",
["Mandatory orientation for the proprietary database system: read the manual and technical specifications on the portal,",
"then watch the video tutorials before attending the hands-on demonstration by the instructor.",
"The tutorial has three sections; the documentation is user-friendly. The 20-minute assessment follows —",
"qualified staff earn certification immediately; otherwise retake the test next month.",
"One-on-one tutorials are available on request."],
[M(0,"Mandatory","Mandatory","強制性的"),M(0,"orientation","Orientation","新人訓練"),M(0,"proprietary","Proprietary","專有的"),M(0,"database system","Database system","資料庫系統"),M(0,"manual","Manual","手冊"),M(0,"technical specifications","Technical specifications","技術規格"),M(0,"portal","Portal","入口網站"),
M(1,"video tutorials","Video tutorials","影片教學"),M(1,"before attending","Before attending","參加前"),M(1,"hands-on","Hands-on","實作的"),M(1,"demonstration","Demonstration","操作示範"),M(1,"instructor","Instructor","講師"),
M(2,"tutorial","Tutorial","教學課程"),M(2,"three sections","Three sections","三個部分"),M(2,"documentation","Documentation","說明文件"),M(2,"user-friendly","User-friendly","好上手的"),M(2,"20-minute assessment","20-minute assessment","20 分鐘評估"),
M(3,"qualified","Qualified","合格的"),M(3,"earn certification immediately","Earn certification immediately","立即獲得認證"),M(3,"retake the test next month","Retake the test next month","下個月重考"),M(4,"One-on-one tutorials","One-on-one tutorials","一對一教學"),M(2,"assessment","Assessment","測驗、評估")],
subtitle="Training portal · IT learning")
make_doc("toeic-13-4-b","news","Tech Weekly — Prototype demonstration at the technology conference",
["At the technology conference, our booth will showcase a prototype of our wearable devices —",
"a breakthrough design with an intuitive interface. Prototype demonstration: main stage at 2 PM (arrive early);",
"the prototype display shows functionality features and performance data.",
"After design revisions for compatibility, quality assurance ran rigorous beta testing with 500 users:",
"a 40 percent reduction in errors — major progress. Implementation of this revolutionary device",
"supports our digital transformation; full release next quarter."],
[M(0,"technology conference","Technology conference","技術會議"),M(0,"booth","Booth","攤位"),M(0,"showcase","Showcase","展出"),M(0,"prototype","Prototype","原型"),M(0,"wearable devices","Wearable devices","穿戴式裝置"),
M(1,"breakthrough design","Breakthrough design","突破性設計"),M(1,"intuitive interface","Intuitive interface","直覺的介面"),M(1,"Prototype demonstration","Prototype demonstration","原型操作示範"),M(1,"main stage at 2 PM","Main stage at 2 PM","下午 2 點主舞台"),M(1,"arrive early","Arrive early","提早到達"),
M(2,"prototype display","Prototype display","原型展示"),M(2,"functionality features","Functionality features","功能特點"),M(2,"performance","Performance","效能"),
M(3,"design revisions","Design revisions","設計修改"),M(3,"compatibility","Compatibility","相容性"),M(3,"quality assurance","Quality assurance","品質保證"),M(3,"rigorous","Rigorous","嚴格的"),M(3,"beta testing","Beta testing","測試版測試"),M(3,"500 users","500 users","500 名測試使用者"),
M(4,"40 percent reduction","40 percent reduction","40% 的減少"),M(4,"major progress","Major progress","重大進展"),M(4,"Implementation","Implementation","實施"),M(4,"revolutionary","Revolutionary","革命性的"),
M(5,"digital transformation","Digital transformation","數位轉型"),M(5,"next quarter","Next quarter","下個季度")],
subtitle="Innovation section · September")
