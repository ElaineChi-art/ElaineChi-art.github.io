# -*- coding: utf-8 -*-
"""五、㈡例一：股份買賣（書 pp.52-54）"""
U = {
"code":"3-5-2","ch":"Chapter 參　基本條款","sec":"五、表述、保證與承諾（Representation, Warranty, Undertaking）",
"title":"例一：股份買賣的表述、保證及承諾",
"items":[
 {"k":"lead","t":"股權買賣的表述保證條款怎麼寫？本單元讀一則完整範例：先宣告附件三的保證在簽約日與完成日都真實正確（雙時點），再課賣方交割前的揭露義務，最後由買方反向作出自己的表述保證。一句英文一句中文對照。"},

 {"k":"h1","t":"(a) 保證之真實性（雙時點）","ic":"✅"},
 {"k":"en","sp":"標題","t":"Representations and Warranties","zh":"表述及保證"},
 {"k":"en","sp":"(a) 真實正確","t":"(a) The representations, warranties and undertakings set out in Schedule 3 (collectively, the \"Warranties\") given by Vendor to Purchaser are true and accurate as of the date of this Agreement and as of the Completion Date or 31 May 2012, whichever is earlier.",
  "zh":"(a) 於附件三中，由賣方給予買方之表述、保證或承諾（合稱「保證」）於本合約簽訂之日及完成日或 2012 年 5 月 31 日（以較早者為準）皆係真實且正確。"},
 {"k":"tip","t":"兩個設計重點：**①保證內容放在 Schedule 3**（本文只放宣告句，細目擺附件，這是股權買賣的標準做法）；**②雙時點**（簽約日＋完成日）——保證不是只在簽約那天真，交割那天也必須真，這叫 **repetition of warranties（保證重述）**。"},

 {"k":"h1","t":"(b) 賣方的揭露義務","ic":"📢"},
 {"k":"en","sp":"(b) 立即揭露","t":"(b) Vendor hereby agrees to disclose promptly to Purchaser in writing upon being aware of any event or circumstance which would arise or become known to it after the date of this Agreement and before Completion which:",
  "zh":"(b) 賣方據此合約同意在本合約簽訂之後但在完成日之前，若有發生任何事件或情事，且此事件或情事可…賣方會立即向買方以書面揭露："},
 {"k":"en","sp":"(i) 違反保證","t":"(i) constitutes a breach of or is inconsistent with any of the Warranties; or",
  "zh":"(i) 構成「保證」之違反或與任何「保證」相牴觸時；或"},
 {"k":"en","sp":"(ii) 重大不利","t":"(ii) has a material adverse effect on the financial condition of the Company.",
  "zh":"(ii) 對標的公司的財務狀況有重大負面影響時。"},
 {"k":"tip","t":"**material adverse effect（MAE，重大不利影響）** 是併購合約最常吵的四個字。要注意三件事：怎麼定義「重大」？以什麼為衡量基準（財務狀況／營運／前景）？有沒有排除事項（carve-out，例如總體經濟、產業普遍性變動）？"},

 {"k":"h1","t":"(c) 買方的表述、保證及承諾","ic":"🔄"},
 {"k":"en","sp":"(c) 買方表述","t":"(c) Purchaser represents, warrants and undertakes to Vendor that as on the Completion Date and at all times between the date hereof and the Completion Date:",
  "zh":"(c) 買方向賣方於完成日（以及於本合約簽訂日至完成日間任何時間）表述、保證及承諾下列事項："},
 {"k":"en","sp":"(i) 權限與拘束力","t":"(i) Each of the Purchaser or the Designated Subsidiary has the legal right, power and authority to enter into, deliver and perform this Agreement and any other documents given by it pursuant to or in connection with this Agreement, which when executed will constitute legal, valid and binding obligations of Purchaser, and enforceable against each of the Purchaser or the Designated Subsidiary in accordance with their respective terms.",
  "zh":"(i) 買方或任何指定之子公司皆有合法權利、權力或授權以簽訂、交付或履行本合約或依本合約交付之其他文件，且本合約或其他文件在訂定時皆係合法、有效且對買方具拘束力，同時可作為向買方或指定子公司依其條款強制執行。"},
 {"k":"en","sp":"(ii) 不牴觸","t":"(ii) The execution, delivery and the performance by the Purchaser or the Designated Subsidiary of this Agreement will not (as applicable): (1) breach the charter documents of each of Purchaser and Designated Subsidiary; (2) result in a violation under any applicable law.",
  "zh":"(ii) 買方或指定子公司之執行、交付或履行本合約，並不會構成：(1) 違反買方或指定子公司之章程；及 (2) 不會導致違反任何適用的法律。"},

 {"k":"h1","t":"書中解說","ic":"💡"},
 {"k":"p","t":"於上述條款中，買賣雙方首先聲明於合約附件三中所為的陳述、保證或承諾皆係真實；其次，條款中約定，如果在合約簽署日後到交割完成日前，有違反保證或有其他重大不利的情況時，賣方必須立即以書面通知買方。"},
 {"k":"p","t":"其三，買方同時也聲明，買方或其指定之受讓關係企業有權簽署、交付並履行本合約或以其為當事人一方之其他與本合約相關之文件，且本合約及該等文件構成對買方或其指定之受讓關係企業合法、有效並有拘束力之義務，並得依本合約或該等文件為強制執行；同時，買方或其關係企業在履行本合約時，不會違反任一公司的章程規定或違反任何相關法律。"},

 {"k":"voc","v":[
  {"w":"set out in Schedule 3","pos":"phr.","zh":"載於附件三","syn":"specified in Schedule 3","tip":"股權買賣的保證細目通常放附件，本文只留宣告句。別忘了翻附件——真正的風險都在那裡。"},
  {"w":"collectively, the \"Warranties\"","pos":"phr.","zh":"合稱「保證」","syn":"together, the …","trap":"把 representations、warranties、undertakings 三者合併定義成一個詞，簡化後文；但也要注意這樣會不會混淆三者**不同的救濟效果**。"},
  {"w":"true and accurate","pos":"adj. phr.","zh":"真實且正確","syn":"true, accurate and not misleading","tip":"加上 not misleading（無誤導）保護更周延，是買方律師會爭取的。"},
  {"w":"as of the date of this Agreement and as of the Completion Date","pos":"phr.","zh":"於本合約簽訂之日及完成日","trap":"**雙時點**：保證在簽約日與交割日都必須為真（repetition of warranties）。賣方會想只綁簽約日，買方會爭取綁雙時點。"},
  {"w":"whichever is earlier","pos":"phr.","zh":"以較早者為準","syn":"whichever is the later／whichever occurs first","tip":"兩個時點並列時一定要寫清楚取哪一個。"},
  {"w":"disclose promptly in writing","pos":"v. phr.","zh":"立即以書面揭露","syn":"notify forthwith in writing","tip":"揭露義務（disclosure obligation）；相對的概念是 disclosure letter（揭露函），賣方用它來排除已揭露事項的責任。"},
  {"w":"upon being aware of","pos":"phr.","zh":"於知悉時","syn":"upon becoming aware of","trap":"知悉標準要寫清楚：實際知悉（actual knowledge）還是應當知悉（constructive knowledge／after due enquiry）？差很多。"},
  {"w":"constitutes a breach of or is inconsistent with","pos":"v. phr.","zh":"構成…之違反或與…相牴觸","tip":"兩個層次並列：直接違反＋雖未違反但相牴觸。"},
  {"w":"material adverse effect","pos":"n. phr.","zh":"重大不利（負面）影響","syn":"MAE／MAC (material adverse change)","trap":"併購合約最常吵的四個字。要看定義、衡量基準與 carve-out（排除總體經濟或產業普遍變動）。"},
  {"w":"financial condition","pos":"n. phr.","zh":"財務狀況","syn":"business, assets, financial condition and prospects","tip":"範圍寫越寬，買方越有機會主張 MAE。"},
  {"w":"represents, warrants and undertakes","pos":"v. phr.","zh":"表述、保證及承諾","tip":"三個動詞並列，等於同時啟動三條救濟路線。"},
  {"w":"at all times between the date hereof and the Completion Date","pos":"phr.","zh":"於本合約簽訂日至完成日間任何時間","trap":"比「雙時點」更嚴：**期間內隨時都必須為真**（continuing warranty）。"},
  {"w":"legal right, power and authority","pos":"n. phr.","zh":"合法權利、權力或授權","syn":"capacity and authority","tip":"三件事：right（權利）、power（權能）、authority（授權）。英美合約的標準三連。"},
  {"w":"enter into, deliver and perform","pos":"v. phr.","zh":"簽訂、交付或履行","syn":"execute, deliver and perform","tip":"與解除條件單元的授權三部曲同一組。"},
  {"w":"legal, valid and binding obligations","pos":"n. phr.","zh":"合法、有效且具拘束力之義務","tip":"融資與併購合約的 capacity warranty 核心句；律師意見書（legal opinion）也是出這一句。"},
  {"w":"enforceable in accordance with their respective terms","pos":"adj. phr.","zh":"得依其各自條款強制執行","trap":"實務上這句後面常接一長串**例外**（subject to bankruptcy, insolvency and general principles of equity），要一併看。"},
  {"w":"charter documents","pos":"n. phr.","zh":"公司章程（設立文件）","syn":"constitutional documents／articles of association","tip":"breach the charter documents＝違反章程。"},
  {"w":"Designated Subsidiary","pos":"n. phr.","zh":"指定之子公司（受讓關係企業）","tip":"買方常保留把交割主體換成集團內子公司的權利，所以保證要把它一起綁進來。"},
  {"w":"result in a violation under any applicable law","pos":"v. phr.","zh":"導致違反任何適用之法律","syn":"contravene any applicable law","tip":"no-conflict warranty（不牴觸保證）的標準寫法：不違章程、不違法、不違既有合約。"}
 ]}
]}

SUDU = {
"tree":"""【例一：股份買賣的表述保證・骨架】
├ (a) 保證之真實性
│   ├ 內容放在 **Schedule 3**，合稱 the \\"Warranties\\"
│   ├ 由 Vendor 給 Purchaser
│   └ **true and accurate**　as of 簽約日 **and** as of Completion Date or 31 May 2012,
│     **whichever is earlier**（雙時點 repetition of warranties）
├ (b) 賣方的揭露義務（簽約日後、完成日前）
│   ├ **disclose promptly in writing upon being aware of** any event or circumstance
│   ├ (i) constitutes a breach of or is **inconsistent with** any of the Warranties；或
│   └ (ii) has a **material adverse effect** on the financial condition of the Company（MAE）
└ (c) 買方的表述、保證及承諾
    ├ 時點：as on the Completion Date **and at all times between** the date hereof and Completion
    ├ (i) Purchaser 或 **Designated Subsidiary** 有 legal right, power and authority
    │     to enter into, deliver and perform；構成 **legal, valid and binding obligations**
    │     且 **enforceable in accordance with their respective terms**
    └ (ii) 不會 (1) breach the **charter documents**（章程）
          (2) result in a **violation under any applicable law**（不牴觸保證）""",
"quiz":[
 {"q":"\"are true and accurate as of the date of this Agreement and as of the Completion Date\" means the Warranties must be true:",
  "o":[["A","only when the contract is signed"],["B","only at completion"],["C","at both signing and completion"],["D","only if the buyer asks"]],
  "a":"(C) at both signing and completion","zh":"簽約日與完成日兩個時點都必須真實正確。",
  "e":"這叫 repetition of warranties（保證重述）。賣方會想只綁簽約日，買方會爭取綁雙時點甚至期間內隨時——(c) 項對買方就是用 at all times between 的更嚴格寫法。"},
 {"q":"Why are the detailed warranties \"set out in Schedule 3\" rather than in the body?",
  "o":[["A","because they are not binding"],["B","because they are long and detailed; the body keeps only the declaratory sentence"],["C","to keep them confidential"],["D","because schedules prevail over the body"]],
  "a":"(B) because they are long and detailed; the body keeps only the declaratory sentence","zh":"保證細目很長，所以放附件，本文只留宣告句。",
  "e":"這是股權買賣的標準做法。**真正的風險都在附件裡**，審約時一定要翻到 Schedule 去逐條看，不能只讀本文。"},
 {"q":"Under limb (b), when must the Vendor disclose?",
  "o":[["A","at completion only"],["B","promptly in writing upon becoming aware of a breach or a material adverse effect"],["C","within 30 days of signing"],["D","only if the Purchaser asks"]],
  "a":"(B) promptly in writing upon becoming aware of a breach or a material adverse effect","zh":"於知悉違反保證或有重大不利影響時，立即以書面揭露。",
  "e":"揭露義務的三個要素：觸發事由（breach／inconsistent／MAE）、時點（promptly upon being aware）、方式（in writing）。知悉標準是實際知悉還是應當知悉，實務上要寫清楚。"},
 {"q":"\"material adverse effect\" is heavily negotiated mainly because:",
  "o":[["A","it is hard to translate"],["B","what counts as \"material\", the yardstick used, and the carve-outs are all open to argument"],["C","it only applies to the buyer"],["D","it is prohibited in Taiwan"]],
  "a":"(B) what counts as \"material\", the yardstick used, and the carve-outs are all open to argument","zh":"「重大」的門檻、衡量基準與排除事項都是爭點。",
  "e":"MAE／MAC 是併購合約最常吵的四個字。常見的 carve-out 包括總體經濟變動、產業普遍性變動、法令修改等不可歸責於標的公司的因素。"},
 {"q":"Limb (c)(ii) is a so-called **no-conflict warranty**. What does it promise?",
  "o":[["A","that the price is fair"],["B","that performing the agreement will not breach the charter documents or applicable law"],["C","that the company is profitable"],["D","that the shares are free from encumbrances"]],
  "a":"(B) that performing the agreement will not breach the charter documents or applicable law","zh":"履行本合約不會違反章程，也不會違反任何適用的法律。",
  "e":"完整的 no-conflict warranty 通常有三支：不違章程（charter documents）、不違法（applicable law）、不違既有合約（existing agreements）。本例寫了前兩支。"}
],
"say":[
 "例一，股份買賣的表述、保證及承諾。",
 "a 項：The representations, warranties and undertakings set out in Schedule 3, collectively the Warranties, given by Vendor to Purchaser are true and accurate as of the date of this Agreement and as of the Completion Date or thirty-first May two thousand twelve, whichever is earlier.",
 "請注意兩個設計重點。第一，保證的細目放在附件三，本文只留宣告句，這是股權買賣的標準做法，真正的風險都在附件裡。第二，雙時點：簽約日與完成日都必須真實正確，這叫保證重述。",
 "b 項是賣方的揭露義務：Vendor hereby agrees to disclose promptly to Purchaser in writing upon being aware of any event or circumstance which constitutes a breach of or is inconsistent with any of the Warranties, or has a material adverse effect on the financial condition of the Company.",
 "material adverse effect，重大不利影響，是併購合約最常吵的四個字。要看三件事：重大的門檻怎麼定、以什麼為衡量基準、以及有沒有排除事項。",
 "c 項換成買方作表述、保證及承諾，而且時點更嚴：as on the Completion Date and at all times between the date hereof and the Completion Date，期間內隨時都必須為真。",
 "買方保證兩件事。第一，有 legal right, power and authority 簽訂、交付及履行本合約，且構成 legal, valid and binding obligations，並得依其各自條款強制執行。第二是不牴觸保證：不會違反買方或指定子公司的章程，也不會導致違反任何適用的法律。"
]}
