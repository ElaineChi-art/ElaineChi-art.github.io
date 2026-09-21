// 示範組織：鏈譜音樂科技（虛構）— 音樂 NFT 授權平台，示範一套創新治理管理系統填滿後的樣子
window.IGS_DEMO = {
  org: {
    name: "鏈譜音樂科技股份有限公司",
    industry: "音樂版權科技／區塊鏈授權平台",
    capital: 200000000,
    listed: "興櫃",
    scope: "本創新治理管理系統適用於本公司音樂版權數位授權平台之研發、營運與授權業務，涵蓋智慧合約開發、音樂 NFT 發行、版稅分潤與相關資訊系統。",
    vision: "讓每一首歌的每一次使用，都能即時、透明、公平地回到創作者手上。",
    intent: "以區塊鏈智慧合約重構音樂授權與版稅分潤流程，三年內成為華語音樂圈最受信任的數位授權基礎設施（數位轉型・永續運作・有吸引力的品牌）。",
    topMgmt: "董事長 林可歆",
    boardReportDate: "2026-06-20"
  },
  issues: [
    {id:1,type:"外部",cat:"法規",desc:"虛擬資產服務法三讀（2026/6/30），NFT 是否納管、平台是否須登記尚待子法",impact:"風險",note:"持續追蹤金管會子法草案"},
    {id:2,type:"外部",cat:"市場",desc:"串流平台版稅分潤不透明，獨立音樂人對即時分潤需求強烈",impact:"機會",note:"核心市場缺口"},
    {id:3,type:"外部",cat:"科技",desc:"生成式 AI 音樂大量湧現，訓練資料授權與著作權歸屬爭議升溫",impact:"兩者",note:"可發展 AI 訓練授權產品線，亦有侵權風險"},
    {id:4,type:"外部",cat:"競爭",desc:"國際平台（Audius、Royal）進入亞洲市場",impact:"風險",note:""},
    {id:5,type:"內部",cat:"人員",desc:"智慧合約工程師僅 2 名，關鍵技術集中於少數人",impact:"風險",note:"知識流失風險"},
    {id:6,type:"內部",cat:"技術",desc:"自研版稅分潤智慧合約已於測試網驗證，具可專利性",impact:"機會",note:"應儘速權利化"},
    {id:7,type:"內部",cat:"財務",desc:"研發費用占營收 38%，需對董事會說明投資效益",impact:"兩者",note:""}
  ],
  stakeholders: [
    {id:1,name:"董事會／股東",type:"治理",needs:"創新投資效益透明、智財與資安風險可控",expect:"每年智財管理計畫報告、ESG 評鑑 S-10/S-12 達標",relevance:"高"},
    {id:2,name:"獨立音樂創作者",type:"客戶",needs:"即時分潤、授權條件清楚、不被綁約",expect:"版稅 T+0 到帳、授權合約易懂",relevance:"高"},
    {id:3,name:"唱片公司／版權代理",type:"客戶／夥伴",needs:"批次授權管理、報表對帳",expect:"API 介接、符合集管團體規範",relevance:"高"},
    {id:4,name:"金管會／經濟部智慧局",type:"主管機關",needs:"合規、洗錢防制、著作權登記正確",expect:"依法登記、KYC/AML 機制",relevance:"高"},
    {id:5,name:"研發團隊",type:"員工",needs:"研發成果被記錄與肯定、發明獎勵",expect:"職務發明獎勵辦法、研發紀錄制度",relevance:"中"},
    {id:6,name:"集管團體（MÜST、ACMA）",type:"產業",needs:"授權資料互通、不衝突",expect:"分潤資料格式相容",relevance:"中"}
  ],
  areas: [
    {id:1,theme:"即時版稅分潤（智慧合約）",rationale:"串流分潤不透明 × 創作者需求強烈",linkedIntent:"數位轉型"},
    {id:2,theme:"AI 訓練資料音樂授權市場",rationale:"生成式 AI 授權爭議 → 合法訓練資料需求",linkedIntent:"有吸引力的品牌"},
    {id:3,theme:"跨平台授權資料互通標準",rationale:"集管團體與唱片公司需要相容格式",linkedIntent:"永續運作"}
  ],
  leadership: {
    commitment: {c1:true,c2:true,c3:true,c4:false,c5:true,c6:false},
    policy: {text:"本公司視音樂版權技術與資料為核心經營資產，承諾：一、依法取得、保護、維護並運用智慧財產；二、尊重他人智慧財產，不為侵權；三、將創新與智財風險納入公司整體風險管理；四、提供必要資源，並每年檢討本政策與目標之達成。",version:"v2.0",approver:"董事會",date:"2026-03-15"},
    strategy: {text:"重點領域：即時分潤智慧合約、AI 訓練授權、授權資料標準。創新類型：以流程創新為主、產品創新為輔。三年抱負：專利 5 件、平台授權曲目 10 萬首。責任：技術長主導、法務長把關、董事會每年審查。衡量：見創新目標之 KPI。"}
  },
  roles: [
    {id:1,role:"最高管理者（董事長）",person:"林可歆",resp:"承諾與資源、核定政策與目標、主持管理審查",clause:"5.1 / 9.3"},
    {id:2,role:"創新治理主管（技術長）",person:"張以恆",resp:"創新組合、倡議推動、研發紀錄制度",clause:"6.4 / 8.2"},
    {id:3,role:"智財管理主管（法務長）",person:"姬政妤",resp:"智財取得保護維護運用、合約與委外管理、爭議處理",clause:"8.1–8.4"},
    {id:4,role:"資安主管",person:"陳柏宇",resp:"資訊安全管理系統、機密資訊保護",clause:"7.1.5 / ISMS"},
    {id:5,role:"內部稽核",person:"稽核室 吳佩珊",resp:"年度稽核計畫（含研發循環）、內部稽核",clause:"9.2"}
  ],
  objectives: [
    {id:1,name:"版稅分潤智慧合約權利化",kpi:"發明專利申請件數",target:"3",actual:"2",due:"2026-12-31",owner:"法務長",status:"進行中"},
    {id:2,name:"平台授權曲目數",kpi:"累計授權曲目",target:"30000",actual:"18400",due:"2026-12-31",owner:"營運長",status:"進行中"},
    {id:3,name:"研發紀錄制度導入",kpi:"研發專案研發紀錄完成率",target:"100%",actual:"85%",due:"2026-09-30",owner:"技術長",status:"進行中"},
    {id:4,name:"營業秘密盤點",kpi:"核心技術營業秘密盤點完成",target:"完成",actual:"完成",due:"2026-06-30",owner:"法務長",status:"已達成"},
    {id:5,name:"AI 訓練授權產品上線",kpi:"簽約 AI 業者數",target:"2",actual:"0",due:"2027-03-31",owner:"技術長",status:"進行中"}
  ],
  riskCriteria: {lowMax:5, midMax:12},
  risks: [
    {id:1,src:"外部／法規",desc:"虛擬資產服務法子法將 NFT 平台納管，須申請登記否則不得營業",cat:"法遵",L:4,I:5,treat:"降低",control:"法務追蹤子法；預備登記文件；必要時調整代幣設計避免歸類為虛擬資產",owner:"法務長",status:"處理中"},
    {id:2,src:"內部／技術",desc:"智慧合約程式碼在申請專利前外流或被反向工程",cat:"智財",L:3,I:5,treat:"降低",control:"程式碼分級機密管理、GitHub 私有庫權限、專利優先申請",owner:"法務長",status:"處理中"},
    {id:3,src:"內部／人員",desc:"關鍵工程師離職帶走技術知識",cat:"智財",L:3,I:4,treat:"降低",control:"競業與保密協議、知識文件化、職務發明獎勵",owner:"技術長",status:"處理中"},
    {id:4,src:"外部／侵權",desc:"平台上架曲目未經授權，遭權利人主張著作權侵害",cat:"智財",L:3,I:4,treat:"降低",control:"上架前權利鏈審查、通知取下機制、保險",owner:"營運長",status:"處理中"},
    {id:5,src:"外部／資安",desc:"智慧合約漏洞遭利用導致版稅資金被盜",cat:"資安",L:2,I:5,treat:"降低",control:"第三方合約審計、多簽錢包、漏洞賞金",owner:"資安主管",status:"處理中"},
    {id:6,src:"外部／AI",desc:"AI 生成音樂上架造成著作權歸屬爭議",cat:"AI",L:3,I:3,treat:"降低",control:"AI 生成標示、上架聲明條款",owner:"法務長",status:"待處理"},
    {id:7,src:"內部／財務",desc:"研發投入無法在董事會取得持續支持",cat:"經營",L:2,I:4,treat:"降低",control:"每季向董事會報告創新組合進度與價值",owner:"技術長",status:"處理中"},
    {id:8,src:"外部／競爭",desc:"國際平台以低費率搶佔創作者",cat:"經營",L:3,I:3,treat:"接受",control:"差異化：華語曲庫與集管團體互通",owner:"營運長",status:"監控中"},
    {id:9,src:"外部／資安",desc:"個資（創作者身分與收款資料）外洩",cat:"資安",L:2,I:4,treat:"降低",control:"加密、最小權限、個資盤點（待 ISMS 導入）",owner:"資安主管",status:"待處理"}
  ],
  initiatives: [
    {id:1,name:"RoyaltyFlow 即時分潤智慧合約 v2",intent:"數位轉型",stage:"開發解決方案",portfolio:"開發",budget:"6,000,000",uncert:"鏈上手續費波動影響小額分潤可行性",owner:"技術長",status:"進行中"},
    {id:2,name:"AI 訓練資料授權市集",intent:"有吸引力的品牌",stage:"驗證概念",portfolio:"探索",budget:"1,500,000",uncert:"AI 業者付費意願、法規對訓練資料的認定",owner:"技術長",status:"進行中"},
    {id:3,name:"授權資料互通標準（與集管團體合作）",intent:"永續運作",stage:"創造概念",portfolio:"探索",budget:"800,000",uncert:"集管團體參與意願",owner:"營運長",status:"進行中"},
    {id:4,name:"音樂 NFT 發行工具 v1",intent:"數位轉型",stage:"部署",portfolio:"部署",budget:"3,200,000",uncert:"已上線，觀察採用率",owner:"營運長",status:"已部署"}
  ],
  partners: [
    {id:1,name:"國立陽明交通大學 科法所",type:"學研",scope:"智慧合約法制與授權條款研究",agreement:"產學合作契約（含智財歸屬條款）"},
    {id:2,name:"MÜST 社團法人中華音樂著作權協會",type:"產業",scope:"授權資料互通",agreement:"合作備忘錄（MOU）"},
    {id:3,name:"區塊鏈資安審計公司",type:"供應商",scope:"智慧合約審計",agreement:"服務契約＋保密協議"}
  ],
  resources: [
    {id:1,kind:"人員",desc:"智慧合約工程師 2 名、後端 3 名、法務 2 名",amount:"7 人",owner:"人資"},
    {id:2,kind:"時間",desc:"研發人員每週 20% 探索時間",amount:"20%",owner:"技術長"},
    {id:3,kind:"財務",desc:"年度創新預算",amount:"NT$ 12,000,000",owner:"財務長"},
    {id:4,kind:"基礎設施",desc:"GitHub Enterprise、測試鏈節點、AI 開發工具（Copilot）",amount:"—",owner:"資安主管"},
    {id:5,kind:"知識",desc:"專利檢索資料庫、產業情報（策略情報管理）",amount:"—",owner:"法務長"}
  ],
  competence: [
    {id:1,person:"智慧合約工程師",skill:"Solidity 安全開發",level:"中",training:"外部合約審計課程",due:"2026-11-30"},
    {id:2,person:"法務",skill:"專利申請與 TIPS 導入",level:"高",training:"TIPS 導入輔導班",due:"完成"},
    {id:3,person:"全體員工",skill:"營業秘密與資安意識",level:"低",training:"年度教育訓練 2 小時",due:"2026-10-31"}
  ],
  comms: [
    {id:1,what:"創新組合進度與價值",who:"董事會",when:"每季",channel:"董事會報告",owner:"技術長"},
    {id:2,what:"智財管理計畫執行情形（ESG S-10）",who:"董事會",when:"每年",channel:"董事會報告",owner:"法務長"},
    {id:3,what:"智財政策、保密規範",who:"全體員工",when:"到職／每年",channel:"教育訓練、內網",owner:"法務長"},
    {id:4,what:"授權條款與分潤規則",who:"創作者",when:"變更時",channel:"平台公告",owner:"營運長"}
  ],
  docs: [
    {id:1,code:"IGS-P-01",title:"智財與創新管理政策",ver:"2.0",owner:"法務長",review:"2027-03-15",type:"政策"},
    {id:2,code:"IGS-M-01",title:"創新治理管理手冊",ver:"1.1",owner:"技術長",review:"2027-01-31",type:"手冊"},
    {id:3,code:"IGS-SOP-08-1",title:"研發紀錄與成果審查程序",ver:"1.0",owner:"技術長",review:"2027-06-30",type:"程序"},
    {id:4,code:"IGS-SOP-08-2",title:"機密資訊分級與委外管理程序",ver:"1.2",owner:"法務長",review:"2027-06-30",type:"程序"},
    {id:5,code:"IGS-F-06",title:"風險評鑑表",ver:"1.0",owner:"法務長",review:"2027-06-30",type:"表單"},
    {id:6,code:"IGS-R-01",title:"職務發明獎勵辦法",ver:"1.0",owner:"人資",review:"2027-12-31",type:"辦法"}
  ],
  ip: [
    {id:1,name:"鏈上版稅即時分潤方法及系統",type:"發明專利",stage:"取得",juris:"TW",appNo:"115xxxxxx",date:"2026-05-12",owner:"法務長",initiative:"RoyaltyFlow 即時分潤智慧合約 v2",value:"核心",status:"審查中",note:"美國申請評估中"},
    {id:2,name:"多方授權金分配之智慧合約架構",type:"發明專利",stage:"取得",juris:"TW",appNo:"115xxxxxx",date:"2026-08-03",owner:"法務長",initiative:"RoyaltyFlow 即時分潤智慧合約 v2",value:"核心",status:"審查中",note:""},
    {id:3,name:"RoyaltyFlow 分潤引擎原始碼",type:"營業秘密",stage:"保護",juris:"—",appNo:"—",date:"2025-11-01",owner:"技術長",initiative:"RoyaltyFlow 即時分潤智慧合約 v2",value:"核心",status:"生效中",note:"機密等級 A；存取名單 4 人"},
    {id:4,name:"鏈譜 ChainScore",type:"商標",stage:"維護",juris:"TW",appNo:"註冊第 0xxxxxxx 號",date:"2024-02-20",owner:"法務長",initiative:"",value:"重要",status:"有效",note:"2034 到期前一年續展"},
    {id:5,name:"平台前端與 App 程式著作",type:"著作權",stage:"維護",juris:"TW",appNo:"—",date:"2024-06-01",owner:"技術長",initiative:"音樂 NFT 發行工具 v1",value:"一般",status:"有效",note:"完成日紀錄留存"},
    {id:6,name:"NFT 發行工具授權（白牌）",type:"授權",stage:"運用",juris:"TW",appNo:"—",date:"2026-04-01",owner:"營運長",initiative:"音樂 NFT 發行工具 v1",value:"重要",status:"授權中",note:"授權予 2 家獨立廠牌，年授權金 NT$ 1.2M"},
    {id:7,name:"AI 訓練資料授權合約範本",type:"著作權",stage:"成果",juris:"TW",appNo:"—",date:"2026-08-20",owner:"法務長",initiative:"AI 訓練資料授權市集",value:"重要",status:"審查中",note:"成果審查會 9/30"},
    {id:8,name:"歌曲指紋比對演算法改良",type:"發明專利",stage:"提案",juris:"—",appNo:"—",date:"2026-09-10",owner:"技術長",initiative:"授權資料互通標準（與集管團體合作）",value:"待評估",status:"提案中",note:"先做先前技術檢索"}
  ],
  audits: [
    {id:1,date:"2026-05-08",scope:"8.1 取得／8.2 保護（研發紀錄、機密管理）",auditor:"稽核室 吳佩珊",finding:"研發紀錄簿有 3 件專案未完成主管簽核；委外合約 1 件缺智財歸屬條款",result:"2 項不符合"},
    {id:2,date:"2026-05-08",scope:"5 領導／6 規劃",auditor:"稽核室 吳佩珊",finding:"政策與目標已核定並公告；風險評鑑準則已訂",result:"符合"}
  ],
  reviews: [
    {id:1,date:"2026-06-20",chair:"董事長 林可歆",inputs:"內部稽核結果、目標達成情形、風險登錄、利害關係人回饋、資源充足性",decisions:"1. 核准美國專利申請預算 2. 資安主管納入管理審查固定成員 3. 2026Q4 啟動 ISMS 導入評估 4. 政策 v2.0 維持"}
  ],
  ncs: [
    {id:1,src:"內部稽核 2026-05",desc:"3 件研發專案研發紀錄未完成主管簽核",cause:"簽核流程未電子化，主管出差延誤",action:"研發紀錄改電子簽核，逾期系統提醒",owner:"技術長",due:"2026-08-31",status:"已完成"},
    {id:2,src:"內部稽核 2026-05",desc:"委外合約缺智財歸屬條款",cause:"採購未使用法務範本",action:"採購流程強制附加法務合約範本檢核",owner:"法務長",due:"2026-09-30",status:"進行中"},
    {id:3,src:"風險評鑑",desc:"個資盤點尚未執行",cause:"尚無資安管理系統",action:"2026Q4 啟動 ISMS 導入評估",owner:"資安主管",due:"2026-12-31",status:"進行中"}
  ],
  improvements: [
    {id:1,date:"2026-08-31",desc:"研發紀錄電子簽核上線",effect:"研發紀錄完成率 60% → 85%"},
    {id:2,date:"2026-06-30",desc:"完成核心技術營業秘密盤點與分級",effect:"9 項核心技術納入機密管理"}
  ]
};
