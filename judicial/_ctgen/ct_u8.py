# -*- coding: utf-8 -*-
"""四、㈢解除條件 Condition Subsequent（書 pp.38-39）"""
U = {
"code":"3-4-3","ch":"Chapter 參　基本條款","sec":"四、合約效力及內容範圍（Contract Effectiveness）",
"title":"解除條件 Condition Subsequent：條件成就，合約失效",
"items":[
 {"k":"lead","t":"解除條件的效果和停止條件剛好相反：約定的事件一發生，合約或合約所訂的義務就失其效力。本單元讀一則以「貸款人未如期取得董事會決議證書則合約自動失效」為解除條件的範例，並對照我國民法第 99 條第 2 項。"},

 {"k":"h1","t":"解除條件是什麼","ic":"📘"},
 {"k":"p","t":"「解除條件」（condition subsequent）係指雙方當事人約定的事件發生時，則合約或合約所訂的義務將失其效力，即當事人可以不再繼續依合約履行，因此，解除條件的效果剛好和停止條件相反。"},
 {"k":"tip","t":"一句話記住：**停止條件＝條件成就才生效（開關打開）；解除條件＝條件成就就失效（開關關掉）**。"},

 {"k":"h1","t":"範例・解除條件條款","ic":"📄"},
 {"k":"en","sp":"自動失效","t":"This Agreement shall become automatically void and of no force and effect if on or prior to June 13, 2012 Lender shall not have received a certificate from the Secretary or K Corp. certifying (as applicable) that",
  "zh":"假若貸款人無法於 2012 年 6 月 13 日前自 K 公司取得下列證書，則本合約將自動失效，且不再生任何效力："},
 {"k":"en","sp":"(a) 決議真正","t":"(a) attached to each such certificate is a true, complete and correct copy of the resolutions of the Board of Directors of K Corp. authorizing among other things the execution, delivery and performance of this Agreement, and",
  "zh":"(a) 於本證書附有 K 公司之董事會真實、完整且正確的董事會決議，以授權執行、交付及履行本合約；且"},
 {"k":"en","sp":"(b) 決議未變","t":"(b) such resolutions have not been amended, modified, revoked or rescinded since the dates on which they were adopted.",
  "zh":"(b) 此董事會決議自決議日起至今尚未經修訂、更改、撤銷或撤回。"},
 {"k":"p","t":"從上述條款可知，此合約的效力，是建立在 K 公司的有效的董事會決議授權，與前面的停止條件不同的是，此條件並不是設定為合約生效的前提要件，而是設定為貸款人必須在指定的期限前提出證書證明有效董事會決議的存在，否則這個合約就會自動失效。"},
 {"k":"tip","t":"同一件事（董事會決議授權）可以寫成**停止條件**（取得才生效）也可以寫成**解除條件**（沒取得就失效）。差別在於**過渡期間合約有沒有效**——解除條件下合約先生效，拿不到才倒回去；停止條件下合約根本還沒生效。談判時這一點值得爭。"},

 {"k":"h1","t":"我國法對照：民法第 99 條第 2 項","ic":"⚖️"},
 {"k":"p","t":"在我國法下，依民法第 99 條第 2 項之規定：「附解除條件之法律行為，於條件成就時，失其效力。」故上例的條款，符合民法上開條文的規定。"},

 {"k":"voc","v":[
  {"w":"condition subsequent","pos":"n. phr.","zh":"解除條件","syn":"resolutive condition","trap":"與 condition precedent 效果**相反**：前者成就使合約失效，後者成就才生效。"},
  {"w":"become automatically void","pos":"v. phr.","zh":"自動失效","syn":"automatically terminate／lapse","trap":"**自動**＝不必再通知、不必再主張。對想保留彈性的一方很危險，通常會改成「得終止」（may terminate）。"},
  {"w":"of no force and effect","pos":"adj. phr.","zh":"不再生任何效力","syn":"null and void／without effect","tip":"void and of no force and effect 是典型的英美法同義詞堆疊，意思只有一個：無效。"},
  {"w":"certificate","pos":"n.","zh":"證書","syn":"secretary's certificate／officer's certificate","tip":"由公司秘書或高階主管出具，證明決議、章程、授權人等文件為真，是交割日文件包（closing documents）的常客。"},
  {"w":"the Secretary","pos":"n.","zh":"公司秘書","trap":"不是「秘書」職員。英、港、星公司法下的 Company Secretary 是法定職位，負責公司登記文件與決議紀錄。"},
  {"w":"resolutions of the Board of Directors","pos":"n. phr.","zh":"董事會決議","syn":"board resolutions","tip":"授權簽約的核心文件；與「簽字能力及授權」那一節互相呼應。"},
  {"w":"true, complete and correct copy","pos":"n. phr.","zh":"真實、完整且正確的副本","tip":"三個形容詞缺一不可：true（真實）、complete（完整，沒抽頁）、correct（正確，沒改字）。"},
  {"w":"authorizing among other things","pos":"phr.","zh":"授權（包括但不限於）…","syn":"including without limitation","tip":"among other things＝除此之外還有別的，等於 inter alia。"},
  {"w":"execution, delivery and performance","pos":"n. phr.","zh":"執行（簽署）、交付及履行","trap":"英美合約的三部曲：execution（簽署）→ delivery（交付）→ performance（履行）。授權決議三者都要寫到，少一個就可能被質疑授權不足。"},
  {"w":"amended, modified, revoked or rescinded","pos":"v. phr.","zh":"修訂、更改、撤銷或撤回","tip":"四個動詞把「決議被動過手腳」的各種可能都蓋住。"},
  {"w":"since the dates on which they were adopted","pos":"phr.","zh":"自決議（通過）日起","tip":"adopt a resolution＝通過決議。"},
  {"w":"as applicable","pos":"phr.","zh":"（視情形）如適用者","syn":"where applicable／if applicable","tip":"用於一句話套用到多個主體或情形時，表示只適用於相符者。"}
 ]}
]}

SUDU = {
"tree":"""【解除條件 Condition Subsequent・骨架】
├ ① 定義：約定事件發生時，合約或合約所訂義務**失其效力**
│   └ 效果與停止條件**剛好相反**（停止＝開；解除＝關）
├ ② 範例：以董事會決議證書為解除條件
│   ├ This Agreement shall become **automatically void and of no force and effect**
│   │   if on or prior to June 13, 2012 Lender shall not have received a certificate…
│   ├ (a) true, complete and correct copy of the **resolutions of the Board of Directors**
│   │     authorizing the **execution, delivery and performance** of this Agreement
│   └ (b) such resolutions have not been **amended, modified, revoked or rescinded**
├ ③ 與停止條件的差異（書中特別點出）
│   ├ 停止條件：設定為合約**生效的前提要件**
│   └ 本例：合約先有效，貸款人未於期限前提出證書 → **自動失效**
└ ④ 我國法：民法§99Ⅱ 附解除條件之法律行為，於條件成就時，失其效力""",
"quiz":[
 {"q":"A condition subsequent, when satisfied, causes the contract to:",
  "o":[["A","come into effect"],["B","cease to have effect"],["C","be extended"],["D","be assigned"]],
  "a":"(B) cease to have effect","zh":"失其效力。",
  "e":"停止條件成就才生效（民法§99Ⅰ）；解除條件成就則失效（民法§99Ⅱ）。效果剛好相反。"},
 {"q":"\"This Agreement shall become automatically void\" is riskier for a party than \"a party may terminate\" because:",
  "o":[["A","it requires notice"],["B","no notice or election is needed — the contract dies by itself"],["C","it needs court approval"],["D","it only applies to the lender"]],
  "a":"(B) no notice or election is needed — the contract dies by itself","zh":"不必通知、不必主張，合約自己失效。",
  "e":"automatically void 剝奪了「要不要繼續」的選擇權。想保留彈性時，談判上會爭取改成 may terminate（得終止）。"},
 {"q":"What must the certificate attach, under limb (a)?",
  "o":[["A","the company's financial statements"],["B","a true, complete and correct copy of the board resolutions authorizing execution, delivery and performance"],["C","the shareholders' register"],["D","the articles of association"]],
  "a":"(B) a true, complete and correct copy of the board resolutions authorizing execution, delivery and performance","zh":"附上授權執行、交付及履行本合約之董事會決議的真實、完整且正確副本。",
  "e":"execution, delivery and performance 是英美合約的授權三部曲，授權決議三者都要寫到，否則可能被質疑授權不足。"},
 {"q":"Limb (b) requires the resolutions not to have been \"amended, modified, revoked or rescinded\". The purpose is to ensure:",
  "o":[["A","the resolutions are recent"],["B","the authority relied on is still alive at the relevant date"],["C","the board has met"],["D","the company is solvent"]],
  "a":"(B) the authority relied on is still alive at the relevant date","zh":"確保所依賴的授權到該時點仍然有效存在。",
  "e":"決議通過了之後還可能被修訂或撤回，所以要證明「自決議日起至今」未經變動。四個動詞把動手腳的各種可能都蓋住。"},
 {"q":"The book notes that this clause differs from a condition precedent because:",
  "o":[["A","it is not a condition at all"],["B","it is not set as a prerequisite to the contract taking effect, but makes the contract lapse if the certificate is not produced in time"],["C","it only binds the borrower"],["D","it requires government approval"]],
  "a":"(B) it is not set as a prerequisite to the contract taking effect, but makes the contract lapse if the certificate is not produced in time","zh":"不是設定為合約生效的前提要件，而是未如期提出證書則合約自動失效。",
  "e":"同一件事可以寫成停止條件或解除條件，差別在**過渡期間合約有沒有效**。解除條件下合約先生效，拿不到才倒回去。"}
],
"say":[
 "解除條件，condition subsequent，係指雙方當事人約定的事件發生時，合約或合約所訂的義務將失其效力，當事人可以不再繼續依合約履行。解除條件的效果，剛好和停止條件相反。",
 "一句話記住：停止條件是條件成就才生效，開關打開；解除條件是條件成就就失效，開關關掉。",
 "範例條款：This Agreement shall become automatically void and of no force and effect if on or prior to June thirteenth, two thousand twelve, Lender shall not have received a certificate from the Secretary of K Corp. certifying that (a) attached to each such certificate is a true, complete and correct copy of the resolutions of the Board of Directors authorizing the execution, delivery and performance of this Agreement, and (b) such resolutions have not been amended, modified, revoked or rescinded.",
 "書中特別點出，與前面的停止條件不同的是，這個條件並不是設定為合約生效的前提要件，而是設定為貸款人必須在指定期限前提出證書證明有效董事會決議的存在，否則合約就會自動失效。",
 "請注意 automatically void，自動失效，不必通知也不必主張。想保留彈性時，談判上會爭取改成 may terminate，得終止。",
 "我國法對照，民法第九十九條第二項：附解除條件之法律行為，於條件成就時，失其效力。本例的條款符合這條規定。"
]}
