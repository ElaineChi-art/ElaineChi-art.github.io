# -*- coding: utf-8 -*-
from docs import *
from photo import scene,fetch
import json
M=lambda i,ph,en,zh:(i,ph,en,zh,"l")
P=lambda k:fetch(json.load(open(f'p{k}A.json'))["url"])
scene("toeic-16-4-a",P("164"),[(800,70,"Construction project","建設專案",None,28),(300,250,"Construction","建設、施工",(330,300),24),(1200,930,"Distribution facility","配送設施／物流中心",(1000,500),22),
 (300,900,"Industrial district","工業區",(300,770),22),(1400,250,"State-of-the-art warehouse technology","最先進的倉庫技術",(1300,400),16),(700,930,"Completion","完工",(700,780),24),(1450,900,"Eighteen months","18 個月",None,22)],
 "Photo: A J Paxton, Wikimedia Commons (CC BY-SA 2.0)")
scene("toeic-16-1-a",P("134"),[(800,80,"Prototype","原型、樣品機",(790,340),28),(300,300,"Innovative features","創新功能",(720,400),22),(1300,200,"Test phase","測試階段",(1100,250),24),
 (1300,700,"Quality checks","品質檢查",(900,450),22),(300,900,"Design decisions","設計決定",(500,650),22),(1000,930,"Prototype completion","原型完成",(850,600),20),(1300,900,"Differentiator","差異化特徵",None,22)],
 "Photo: Crew, Wikimedia Commons (CC0)")
scene("toeic-16-2-a",P("154"),[(800,70,"Partnership agreement","合作協議",(1050,490),24),(430,150,"Negotiations","談判、協商",(450,400),24),(1300,900,"Contract finalization","合約定案",(1300,700),22),
 (300,930,"Strategic alliance","策略聯盟",(300,650),22),(1100,930,"Mutual benefit","互惠互利",(1050,800),22),(1300,300,"Stakeholders","利益相關者",(1300,240),22),(200,600,"Joint venture","合資企業",(400,400),24)],
 "Photo: Homedust, Flickr (CC BY 2.0)")
scene("toeic-16-3-a",P("113"),[(800,70,"Automation","自動化",None,30),(800,930,"Full automation","全面自動化",(800,830),24),(250,150,"Increase productivity","提高生產力",(240,470),20),
 (1350,150,"Technology upgrade","技術升級",(1360,400),22),(1300,900,"Operational efficiency","營運效率",(1200,700),20),(250,900,"Advanced automation features","先進的自動化功能",(300,750),18),(800,660,"Smooth performance","順暢運行",(720,545),20)],
 "Photo: jurvetson, Flickr (CC BY 2.0)")
# 16-1
make_doc("toeic-16-1-b","email","Mail — New product development: survey results",
["New product development: the development team finished six months of intensive research for the innovation project: market research with 500 participants",
"and the research department's survey of 1,000 customers. Survey results and customer feedback show strong customer interest",
"and clear preferences — a 30% gap in the market for quality with affordability. These shape our design decisions.",
"The prototype with innovative features (innovation features) passes rigorous testing protocols; quality checks by internal teams",
"and selected customers confirm the quality standards and market expectations."],
[M(0,"development team","Development team","開發團隊"),M(0,"six months of intensive research","Six months of intensive research","六個月密集研究"),M(0,"innovation project","Innovation project","創新專案"),M(0,"market research","Market research","市場研究"),M(0,"500 participants","500 participants","500 名參與者"),
M(1,"research department's survey","Research department's survey","研究部門的調查"),M(1,"1,000 customers","1,000 customers","1,000 名客戶"),M(1,"Survey results","Survey results","調查結果"),M(1,"customer feedback","Customer feedback","客戶回饋"),M(1,"customer interest","Customer interest","客戶興趣"),
M(2,"preferences","Preferences","偏好"),M(2,"30% gap in the market","30% gap in the market","30% 市場缺口"),M(2,"quality with affordability","Quality with affordability","高性價比"),M(2,"design decisions","Design decisions","設計決定"),
M(3,"prototype","Prototype","原型"),M(3,"innovative features","Innovative features","創新功能"),M(3,"innovation features","Innovation features","創新功能"),M(3,"rigorous","Rigorous","嚴格的"),M(3,"testing protocols","Testing protocols","測試規程"),M(3,"quality checks","Quality checks","品質檢查"),M(3,"internal teams","Internal teams","內部團隊"),
M(4,"selected customers","Selected customers","選定客戶"),M(4,"quality standards","Quality standards","品質標準"),M(4,"market expectations","Market expectations","市場預期"),M(0,"New product development","New product development","新產品開發")],
subtitle="New product development · From: r&d@company.com")
make_doc("toeic-16-1-c","slide","Launch Strategy — Product line & market launch",
["Launch timeline: prototype completion in March (a critical milestone), test phase in April, full production in May,",
"initial release and full market launch in June. Targeted marketing will differentiate the product line from the competition;",
"quality is our key differentiator. This customer-driven development marks a new stage in our innovation journey."],
[M(0,"Launch timeline","Launch timeline","推出時程表"),M(0,"prototype completion","Prototype completion","原型完成"),M(0,"critical milestone","Critical milestone","關鍵里程碑"),M(0,"test phase","Test phase","測試階段"),M(0,"full production","Full production","全面量產"),
M(1,"initial release","Initial release","首次發布"),M(1,"full market launch","Full market launch","全面市場推出"),M(1,"June","June","六月"),M(1,"Targeted marketing","Targeted marketing","精準行銷"),M(1,"differentiate","Differentiate","使差異化"),M(1,"product line","Product line","產品線"),M(1,"competition","Competition","競爭對手"),
M(2,"quality","Quality","品質"),M(2,"differentiator","Differentiator","差異化特徵"),M(2,"customer-driven development","Customer-driven development","客戶導向開發"),M(2,"innovation journey","Innovation journey","創新旅程"),M(0,"Launch","Launch strategy","推出策略"),M(1,"market launch","Market launch","市場推出")],
subtitle="Launch strategy · Slide 5")
# 16-2
make_doc("toeic-16-2-b","email","Mail — Partnership proposal & joint venture negotiations",
["Our partnership proposal outlines a collaboration opportunity: a joint venture that shares technology resources and our network to reduce costs.",
"Negotiations continue on the partnership agreement; a possible merger needs stakeholder analysis and board approval of the acquisition terms.",
"Suppliers agree material costs fall under the alliance: we leverage combined purchasing power and resource sharing.",
"Cooperation covers three major projects; the strategic alliance and strategic planning will be reviewed with stakeholders."],
[M(0,"partnership proposal","Partnership proposal","合作提案"),M(0,"collaboration opportunity","Collaboration opportunity","合作機會"),M(0,"joint venture","Joint venture","合資企業"),M(0,"technology resources","Technology resources","技術資源"),M(0,"network","Network","網絡"),M(0,"reduce costs","Reduce costs","降低成本"),
M(1,"Negotiations","Negotiations","談判"),M(1,"partnership agreement","Partnership agreement","合作協議"),M(1,"merger","Merger","合併"),M(1,"stakeholder analysis","Stakeholder analysis","利益相關者分析"),M(1,"board approval","Board approval","董事會批准"),M(1,"acquisition terms","Acquisition terms","收購條款"),
M(2,"Suppliers","Suppliers","供應商"),M(2,"material costs","Material costs","材料成本"),M(2,"alliance","Alliance","聯盟"),M(2,"leverage","Leverage","運用優勢"),M(2,"combined purchasing power","Combined purchasing power","合併採購力"),M(2,"resource sharing","Resource sharing","資源共享"),
M(3,"Cooperation","Cooperation","合作"),M(3,"three major projects","Three major projects","三個重大專案"),M(3,"strategic alliance","Strategic alliance","策略聯盟"),M(3,"strategic planning","Strategic planning","策略規劃"),M(3,"stakeholders","Stakeholders","利益相關者")],
subtitle="From: bizdev@company.com")
make_doc("toeic-16-2-c","news","Business Daily — Strategic resource integration",
["Network expansion and joint research projects complement each other's capabilities for mutual benefit; the acquisition strategy",
"will transform the technology sector. Strategic resource integration is discussed at stakeholder meetings; implementation details follow.",
"Pending regulatory approval, projected revenues rise 40% within two years by combining manufacturing expertise with research capabilities",
"and a wider resource base: consolidated purchasing agreements give stable resource availability from 150 suppliers in fifteen countries.",
"Technology transfer and resource optimization start after contract finalization at month-end."],
[M(0,"Network expansion","Network expansion","網絡擴張"),M(0,"research projects","Research projects","研究專案"),M(0,"complement","Complement","使互補"),M(0,"capabilities","Capabilities","能力"),M(0,"mutual benefit","Mutual benefit","互惠互利"),M(0,"acquisition strategy","Acquisition strategy","收購策略"),
M(1,"transform","Transform","徹底改變"),M(1,"technology sector","Technology sector","科技領域"),M(1,"Strategic resource integration","Strategic resource integration","策略資源整合"),M(1,"stakeholder meetings","Stakeholder meetings","利益相關者會議"),M(1,"implementation details","Implementation details","實施細節"),
M(2,"regulatory approval","Regulatory approval","監管批准"),M(2,"projected revenues","Projected revenues","預估營收"),M(2,"40%","40%","百分之四十"),M(2,"within two years","Within two years","兩年之內"),M(2,"manufacturing expertise","Manufacturing expertise","製造專長"),M(2,"research capabilities","Research capabilities","研發實力"),
M(3,"resource base","Resource base","資源基礎"),M(3,"consolidated purchasing agreements","Consolidated purchasing agreements","統一採購協議"),M(3,"stable resource availability","Stable resource availability","穩定的資源供應"),M(3,"150 suppliers","150 suppliers","150 家供應商"),M(3,"fifteen countries","Fifteen countries","15 個國家"),
M(4,"Technology transfer","Technology transfer","技術轉移"),M(4,"resource optimization","Resource optimization","資源優化"),M(4,"contract finalization","Contract finalization","合約定案"),M(4,"month-end","Month-end","月底")],
subtitle="Markets · Tuesday")
# 16-3
make_doc("toeic-16-3-b","email","Mail — Automation project: implementation timeline",
["The automation project installs a new software system to increase productivity by twenty percent; the technology upgrade lifts overall efficiency.",
"Implementation: we install the technology platform over the weekend to minimize disruption; regular equipment maintenance continues.",
"Implementation timeline: six weeks in phases — pilot testing, then full automation of inventory management.",
"Specialists from TechServ Solutions provide three days of hands-on practice, hands-on exercises on operation scenarios,",
"system navigation, maintenance procedures and troubleshooting, plus ongoing support and monthly service checks for smooth performance."],
[M(0,"automation project","Automation project","自動化專案"),M(0,"software system","Software system","軟體系統"),M(0,"increase productivity","Increase productivity","提高生產力"),M(0,"twenty percent","Twenty percent","百分之二十"),M(0,"technology upgrade","Technology upgrade","技術升級"),M(0,"overall efficiency","Overall efficiency","整體效率"),
M(1,"Implementation","Implementation","實施"),M(1,"install","Install","安裝"),M(1,"technology platform","Technology platform","技術平台"),M(1,"weekend","Weekend","週末"),M(1,"minimize disruption","Minimize disruption","將干擾降至最低"),M(1,"regular equipment maintenance","Regular equipment maintenance","定期設備維護"),
M(2,"Implementation timeline","Implementation timeline","實施時程"),M(2,"six weeks","Six weeks","六週"),M(2,"phases","Phases","階段"),M(2,"pilot testing","Pilot testing","試點測試"),M(2,"full automation","Full automation","全面自動化"),M(2,"inventory management","Inventory management","庫存管理"),
M(3,"Specialists","Specialists","專家"),M(3,"TechServ Solutions","TechServ Solutions","泰克服解決方案公司"),M(3,"three days of hands-on practice","Three days of hands-on practice","三天實踐練習"),M(3,"hands-on exercises","Hands-on exercises","動手演練"),M(3,"operation scenarios","Operation scenarios","營運場景"),
M(4,"system navigation","System navigation","系統操作"),M(4,"maintenance procedures","Maintenance procedures","維護程序"),M(4,"troubleshooting","Troubleshooting","故障排除"),M(4,"ongoing support","Ongoing support","持續支援"),M(4,"monthly service checks","Monthly service checks","每月維護檢查"),M(4,"smooth performance","Smooth performance","順暢運行")],
subtitle="From: operations@company.com")
make_doc("toeic-16-3-c","slide","Operational Efficiency Initiative — Operations review",
["Operations review: projections show performance gaps; the operational efficiency initiative uses automation and process improvement",
"to streamline workflows. Advanced automation features optimize operational efficiency; temporary adjustments cover the transition.",
"Performance metrics track efficiency gains and operational challenges; initial implementation costs are offset by projected efficiency savings",
"within eight months. The total investment package includes maintenance contracts, training resources and an implementation schedule",
"for successful adoption and practical application — a real operational improvement."],
[M(0,"Operations review","Operations review","營運審查"),M(0,"projections","Projections","預測"),M(0,"performance gaps","Performance gaps","績效缺口"),M(0,"operational efficiency initiative","Operational efficiency initiative","營運效率計畫"),M(0,"automation","Automation","自動化"),M(0,"process improvement","Process improvement","流程改善"),
M(1,"streamline","Streamline","簡化"),M(1,"Advanced automation features","Advanced automation features","先進自動化功能"),M(1,"optimize","Optimize","優化"),M(1,"operational efficiency","Operational efficiency","營運效率"),M(1,"temporary adjustments","Temporary adjustments","臨時調整"),M(1,"transition","Transition","過渡期"),
M(2,"Performance metrics","Performance metrics","績效指標"),M(2,"efficiency gains","Efficiency gains","效率增益"),M(2,"operational challenges","Operational challenges","營運挑戰"),M(2,"initial implementation costs","Initial implementation costs","初始實施成本"),M(2,"offset","Offset","抵消"),M(2,"projected efficiency savings","Projected efficiency savings","預期效率節省"),
M(3,"eight months","Eight months","八個月"),M(3,"total investment package","Total investment package","總投資方案"),M(3,"maintenance contracts","Maintenance contracts","維護合約"),M(3,"training resources","Training resources","培訓資源"),M(3,"implementation schedule","Implementation schedule","實施進度表"),
M(4,"successful adoption","Successful adoption","成功導入"),M(4,"practical application","Practical application","實際應用"),M(4,"operational improvement","Operational improvement","營運改善")],
subtitle="Operational efficiency initiative · Slide 7")
# 16-4
make_doc("toeic-16-4-b","memo","Capital investment update · To: all managers",
["Capital investment update: the board approved our growth strategy: a $5 million construction project for a new distribution facility in the industrial district",
"with warehouse access to meet distribution demands; the expansion strategy adds three branches. The investment budget also funds",
"a factory renovation project ($10 million investment) to double our production capacity — construction starts next month,",
"completion in eighteen months (December); capital comes from retained earnings. State-of-the-art warehouse technology boosts distribution efficiency.",
"Headquarters renovations ensure strategic alignment as we capture emerging market opportunities and growth."],
[M(0,"board approved","Board approved","董事會批准"),M(0,"growth strategy","Growth strategy","成長策略"),M(0,"$5 million","$5 million","500 萬美元"),M(0,"construction project","Construction project","建設專案"),M(0,"distribution facility","Distribution facility","配送設施"),M(0,"industrial district","Industrial district","工業區"),
M(1,"warehouse access","Warehouse access","倉庫進出通道"),M(1,"distribution demands","Distribution demands","配送需求"),M(1,"expansion strategy","Expansion strategy","擴張策略"),M(1,"three branches","Three branches","三家分公司"),M(1,"investment budget","Investment budget","投資預算"),
M(2,"factory renovation project","Factory renovation project","工廠翻新專案"),M(2,"$10 million investment","$10 million investment","1,000 萬美元投資"),M(2,"double our production capacity","Double our production capacity","產能翻倍"),M(2,"construction","Construction","施工"),M(2,"next month","Next month","下個月"),
M(3,"completion","Completion","完工"),M(3,"eighteen months","Eighteen months","18 個月"),M(3,"December","December","十二月"),M(3,"capital","Capital","資本"),M(3,"State-of-the-art warehouse technology","State-of-the-art warehouse technology","最先進倉庫技術"),M(3,"distribution efficiency","Distribution efficiency","配送效率"),
M(4,"Headquarters renovations","Headquarters renovations","總部翻新"),M(4,"strategic alignment","Strategic alignment","策略一致"),M(4,"capture","Capture","佔領（市場）"),M(4,"emerging market opportunities","Emerging market opportunities","新興市場機會"),M(4,"growth","Growth","成長"),M(0,"Capital investment update","Capital investment update","資本投資更新")],
subtitle="Capital investment update · From: CFO")
make_doc("toeic-16-4-c","slide","Capital Investment Program — Distribution networks",
["The board approved capital investment program ($25 million) targets metropolitan areas with high growth potential.",
"Current headquarters and distribution networks have limitations; an expanded distribution network with new distribution points,",
"consolidating shipments, will cut shipping costs and support 30% revenue growth.",
"Construction timelines are managed by the project management team, which will provide quarterly updates."],
[M(0,"capital investment program","Capital investment program","資本投資計畫"),M(0,"$25 million","$25 million","2,500 萬美元"),M(0,"metropolitan areas","Metropolitan areas","大都市地區"),M(0,"growth potential","Growth potential","成長潛力"),
M(1,"headquarters","Headquarters","總部"),M(1,"distribution networks","Distribution networks","配送網絡"),M(1,"limitations","Limitations","限制"),M(1,"expanded distribution network","Expanded distribution network","擴展後配送網絡"),M(1,"distribution points","Distribution points","配送點"),
M(2,"consolidating","Consolidating","整合"),M(2,"shipping costs","Shipping costs","運輸成本"),M(2,"30% revenue growth","30% revenue growth","30% 營收成長"),
M(3,"Construction timelines","Construction timelines","施工時程"),M(3,"project management team","Project management team","專案管理團隊"),M(3,"quarterly updates","Quarterly updates","每季更新"),M(0,"board approved","Board approved","董事會批准的")],
subtitle="Capital investment program · Slide 3")
