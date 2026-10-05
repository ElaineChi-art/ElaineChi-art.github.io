# -*- coding: utf-8 -*-
"""前言例二：股權買賣合約 Share Sale & Purchase（書 pp.24-26）"""
U = {
"code":"3-1-2","ch":"Chapter 參　基本條款","sec":"一、合約之前言（Preamble）",
"title":"合約前言 Preamble 例二：股權買賣合約 (Vendor / Purchaser)",
"items":[
 {"k":"lead","t":"例二換成另一種常見結構：股權買賣（share sale and purchase）。書中點出它與例一的差別——「將合約當事人之名稱與註冊地址以並列之方式呈現，較為清楚」：簽約日單獨一句，再以 BETWEEN…AND… 分段列出雙方，並標明設立地與公司註冊號碼；WHEREAS 用 (a)–(g) 編號逐項鋪陳標的公司、唯一資產、股本、所有權、股東貸款資本化與待售股份。一句英文、一句中文對照精讀。"},

 {"k":"h1","t":"簽約日與當事人 (Parties)","ic":"✍️"},
 {"k":"en","sp":"簽約日","t":"THIS AGREEMENT is made on October 28th, 2012.","zh":"本合約係於 2012 年 10 月 28 日所作成，於下列當事人間所成立："},
 {"k":"en","sp":"賣方","t":"BETWEEN A PTE. Limited, a company incorporated in the Republic of Singapore (company registration number xxxxxxx) and having its registered office at [address] (the \"Vendor\")",
  "zh":"A PTE Ltd.，係依新加坡法成立的公司（註冊號碼為：xxxxxxx），且其註冊主營業所位於〔地址〕（以下簡稱「賣方」）"},
 {"k":"en","sp":"買方","t":"AND B Limited, a company incorporated in Taiwan, Republic of China (company registration number xxxxxxx) and having its registered office at [address] (the \"Purchaser\").",
  "zh":"及 B Ltd.，係依我國法成立的公司（註冊號碼為：xxxxxxx），且其註冊主營業所位於〔地址〕（以下簡稱「買方」）。"},
 {"k":"tip","t":"例二比例一多寫了兩項關鍵資訊：**incorporated in（設立地）** 與 **company registration number（公司註冊號碼）**。跨境交易中設立地決定公司的能力與代表權，註冊號碼才是唯一識別；registered office 則是法定送達地址。書中的評語是：這種把名稱與註冊地址**並列**呈現的方式比較清楚。"},

 {"k":"h1","t":"WHEREAS 鑑於條款 (a)–(g)","ic":"🔎"},
 {"k":"en","sp":"鑑於","t":"WHEREAS:","zh":"鑑於："},
 {"k":"en","sp":"(a) 標的公司","t":"(a) C PTE. LTD. (the \"Company\") is a private company limited by shares incorporated in the Republic of Singapore (Company registration number xxxxxxx) and having its registered office at [address].",
  "zh":"㈠ C PTE. Ltd.（以下稱「標的公司」）係一私營的股份有限公司，於新加坡所設立（註冊號碼為：xxxxxxx），且其註冊主營業所位於〔地址〕。"},
 {"k":"en","sp":"(b) 唯一資產","t":"(b) The sole asset of the Company is its investment in D Ltd., which operates a factory in [place] in the People's Republic of China (\"PRC\").",
  "zh":"㈡「標的公司」之唯一資產為其於 D Ltd. 之投資，後者係在中華人民共和國之〔某處〕營運一工廠。"},
 {"k":"en","sp":"(c) 股本","t":"(c) The Company has a share capital of 2 ordinary shares, all of which are issued and fully paid at the date of this Agreement.",
  "zh":"㈢「標的公司」總共有普通股票共二股，且在本合約簽訂時，皆已經全部發行及認足。"},
 {"k":"en","sp":"(d) 所有權","t":"(d) The Vendor is the registered and beneficial owner of the 2 ordinary shares representing 100% of the issued and paid-up share capital of the Company.",
  "zh":"㈣「賣方」係前揭「標的公司」二股（亦即代表「標的公司」之百分之百發行及認購之股份）之註冊及受益人。"},
 {"k":"en","sp":"(e) 貸款資本化","t":"(e) The Vendor intends to capitalize US$81,526,793 of its shareholders loan into 81,526,793 ordinary shares of the Company by Completion Date.",
  "zh":"㈤「賣方」欲於「完成日」，將其對「標的公司」價值美金 81,526,793 元之貸款，轉換為「標的公司」之 81,526,793 普通股。"},
 {"k":"en","sp":"(f) 待售股份","t":"(f) At Completion, the Company will have US$81,526,793 issued and fully paid-up ordinary shares (\"Sale Shares\").",
  "zh":"㈥ 於「完成日」時，「標的公司」將擁有 81,526,793 股已發行且認購完成之普通股（以下稱「標的股份」）。"},
 {"k":"en","sp":"(g) 買賣意思","t":"(g) The Purchaser desires to purchase and Vendor desires to sell the Sale Shares on the terms and subject to the conditions set forth in this Agreement.",
  "zh":"㈦「買方」希望購買以及「賣方」希望賣出的「標的股份」，其條件依本約所載之條款。"},
 {"k":"tip","t":"這七項 WHEREAS 其實是一張**盡職調查地圖**：標的公司是誰(a)、它值錢的東西是什麼(b)、股本結構(c)、賣方真的有權賣嗎(d)、交割前要先做什麼動作(e)、做完之後股權長什麼樣(f)、雙方的買賣意思(g)。審約時逐項回去要文件驗證。"},
 {"k":"tip","t":"⚠ 書上 (f) 的英文印成 \"US$81,526,793 issued and fully paid-up ordinary shares\"，但對照中譯是「81,526,793 **股**」——股數不該掛幣別符號。這正是實務上最常見的打字錯誤：**數字＋單位（股／元）寫錯**。審約時務必把英文與中文、金額與股數逐一核對。"},

 {"k":"h1","t":"NOW THEREFORE 與第一條","ic":"✅"},
 {"k":"en","sp":"據此約定","t":"NOW THEREFORE, in consideration of the mutual agreements, representations, warranties and subject to the conditions contained herein, the parties hereto hereby agree as follows:",
  "zh":"是故，以相互之協議、表述、保證以及下列之條件作為對價，當事人據此以本合約同意下列事項："},
 {"k":"en","sp":"第1條","t":"Definitions and Interpretation","zh":"定義及解釋"},
 {"k":"tip","t":"注意例二的 NOW THEREFORE 比例一多列了 **representations（表述／陳述）** 與 **warranties（保證）**——這是股權買賣的靈魂：賣方對標的公司的狀況做陳述與保證，不實時買方可請求損害賠償。接著第一條就是 **Definitions and Interpretation（定義及解釋）**，也就是下一單元的主題。"},

 {"k":"h1","t":"書中解說","ic":"💡"},
 {"k":"p","t":"上述合約前言呈現的方式與前一例大同小異，差別在於本例中，將合約當事人之名稱與註冊地址以並列之方式呈現，較為清楚。"},
 {"k":"p","t":"「Whereas」也是相當於中文的「鑑於」之意思，其後則列舉一些雙方當事人或本件交易之基本資訊。"},

 {"k":"voc","v":[
  {"w":"is made on","pos":"v. phr.","zh":"係於…所作成（簽訂）","syn":"is entered into on／dated as of","tip":"效力起算日有時與作成日不同，可寫成 \"made on … with effect from …\" 分開表示。"},
  {"w":"incorporated in","pos":"v. phr.","zh":"於…設立（登記成立）","syn":"organized under the laws of","trap":"設立地決定公司的**屬人法**（能力、代表權、股東權）；與營業地、稅籍地可能都不同，不要混為一談。"},
  {"w":"company registration number","pos":"n. phr.","zh":"公司註冊號碼","syn":"company number／統一編號","tip":"同名公司很多，註冊號碼才是唯一識別。審約必與公司登記謄本核對。"},
  {"w":"registered office","pos":"n. phr.","zh":"註冊（主）營業所","syn":"registered address","trap":"是法定**送達地址**，不等於實際辦公處所（principal place of business）；通知條款（Notices）要寫清楚寄哪一個。"},
  {"w":"Vendor / Purchaser","pos":"n.","zh":"賣方／買方","syn":"Seller／Buyer","tip":"不動產與股權交易慣用 Vendor/Purchaser；一般貨物買賣慣用 Seller/Buyer。"},
  {"w":"private company limited by shares","pos":"n. phr.","zh":"私營的股份有限公司","tip":"英、港、星公司法用語；private＝股份轉讓受限、不得公開募集。"},
  {"w":"sole asset","pos":"n. phr.","zh":"唯一資產","tip":"本例 (b)：唯一資產是對 D Ltd. 的投資，而 D Ltd. 在中國營運一工廠——實質上買的是那座工廠的持股鏈。"},
  {"w":"operates a factory","pos":"v. phr.","zh":"營運一工廠","syn":"runs／carries on a manufacturing plant","tip":"盡職調查要往下一層查 D Ltd.：土地廠房、環保、勞動、關係人交易。"},
  {"w":"share capital","pos":"n. phr.","zh":"股本","syn":"issued share capital（已發行股本）／paid-up share capital（實收股本）","trap":"authorized（授權）≠ issued（已發行）≠ paid-up／fully paid（繳足）。三個數字不同，審約要逐一確認。"},
  {"w":"ordinary shares","pos":"n. phr.","zh":"普通股","syn":"common stock（美式）／preference shares（優先股）","tip":"a share capital of 2 ordinary shares＝股本總共只有兩股，典型的控股用 SPV。"},
  {"w":"issued and fully paid","pos":"adj. phr.","zh":"已（全部）發行及認足","trap":"若有未繳足（partly paid）股份，買方可能承受補繳義務；這是股權買賣的常見地雷。"},
  {"w":"registered and beneficial owner","pos":"n. phr.","zh":"註冊（登記）名義人及受益人","trap":"兩者分離就是**借名登記／信託**。只確認 registered owner 不夠，必須同時確認 beneficial ownership，否則買到有爭議的股權。"},
  {"w":"representing 100% of","pos":"v. phr.","zh":"代表百分之百之…","tip":"用來說明該批股份占全部已發行且繳足股本的比例，等於保證買下去就是全資。"},
  {"w":"paid-up share capital","pos":"n. phr.","zh":"已認購（實收）之股本","syn":"paid-in capital","tip":"issued and paid-up share capital＝已發行且已繳足的股本。"},
  {"w":"intends to capitalize","pos":"v. phr.","zh":"欲將…資本化","syn":"debt-to-equity conversion（債轉股）","tip":"手法：capitalize US$81,526,793 of its shareholders loan **into** 81,526,793 ordinary shares——把債權換成股權，交割時買方一次買下乾淨的股權。"},
  {"w":"shareholders loan","pos":"n. phr.","zh":"股東貸款（股東借款）","trap":"股東貸款若不先資本化或清償，交割後仍是公司對原股東的負債；價金計算與財務報表都會受影響。"},
  {"w":"by Completion Date","pos":"prep. phr.","zh":"於「完成日」（交割日）前","syn":"by Closing（美式）","tip":"Completion／完成日是股權交易的核心時點：前有 conditions precedent（先決條件），後有 post-completion covenants。"},
  {"w":"At Completion","pos":"prep. phr.","zh":"於完成（交割）時","tip":"與 by Completion Date（在完成日前完成某動作）語意不同，前者描述交割當下的狀態。"},
  {"w":"Sale Shares","pos":"n. phr.","zh":"標的股份（待售股份）","tip":"括號定義一出現，後面所有條文的「股份」就只指這一批。"},
  {"w":"desires to purchase / desires to sell","pos":"v. phr.","zh":"希望購買／希望賣出","syn":"has agreed to sell／wishes to acquire","tip":"WHEREAS 最後一項固定表明雙方的交易意思，承接下文 NOW THEREFORE。"},
  {"w":"on the terms and subject to the conditions set forth in this Agreement","pos":"phr.","zh":"其條件依本約所載之條款","trap":"terms（條款內容）與 conditions（條件；不成立則效力受影響）在英美法上效果不同，這組並列句是為了兩面都綁住。"},
  {"w":"representations and warranties","pos":"n. phr.","zh":"表述（陳述）與保證","trap":"兩者救濟不同：representation 不實走 misrepresentation（可能撤銷契約），warranty 不實走違約損害賠償。股權買賣最核心的攻防就在這一欄。"},
  {"w":"the parties hereto","pos":"n. phr.","zh":"本合約之當事人","syn":"the parties to this Agreement","tip":"hereto＝to this Agreement。與 hereof（of this Agreement）、herein（in this Agreement）、hereunder（under this Agreement）成套記。"},
  {"w":"Definitions and Interpretation","pos":"n. phr.","zh":"定義及解釋","tip":"英文合約第一條的標準標題：先定義用語，再規定解釋規則。"}
 ]}
]}

SUDU = {
"tree":"""【合約前言 Preamble 例二・股權買賣骨架】
├ ① 簽約日單獨一句：THIS AGREEMENT is made on October 28th, 2012.
├ ② 當事人 BETWEEN … AND …（名稱與註冊地址並列，書評：較為清楚）
│   ├ Vendor＝A PTE. Limited，incorporated in the Republic of Singapore
│   ├ Purchaser＝B Limited，incorporated in Taiwan, Republic of China
│   └ 三件事：incorporated in／company registration number／registered office
├ ③ WHEREAS: (a)-(g) ＝ 一張盡職調查地圖
│   ├ (a) 標的公司 C PTE. LTD.（the \"Company\"）private company limited by shares（新加坡）
│   ├ (b) sole asset＝investment in D Ltd.，D Ltd. operates a factory in PRC
│   ├ (c) share capital of 2 ordinary shares，issued and fully paid
│   ├ (d) Vendor＝registered AND beneficial owner，representing 100% of issued and paid-up share capital
│   ├ (e) by Completion Date：capitalize US$81,526,793 shareholders loan → 81,526,793 ordinary shares（債轉股）
│   ├ (f) At Completion：81,526,793 issued and fully paid-up ordinary shares ＝ the \"Sale Shares\"
│   └ (g) Purchaser desires to purchase／Vendor desires to sell, on the terms and subject to the conditions
├ ④ NOW THEREFORE（比例一多了 representations、warranties）
│   └ in consideration of the mutual agreements, representations, warranties and subject to the conditions
│     contained herein, the parties hereto hereby agree as follows:
└ ⑤ 第一條：Definitions and Interpretation 定義及解釋""",
"quiz":[
 {"q":"\"the Vendor is the registered and beneficial owner of the 2 ordinary shares\" — why are **both** words used?",
  "o":[["A","they are synonyms used for emphasis"],["B","legal title and economic ownership can be held by different persons"],["C","\"registered\" refers to the company, \"beneficial\" to the shares"],["D","it is required by Singapore tax law"]],
  "a":"(B) legal title and economic ownership can be held by different persons","zh":"因為註冊名義人與受益人可能是不同的人（借名登記／信託）。",
  "e":"只查股東名簿（registered owner）不足以確認賣方有權處分；若有 nominee／trust arrangement，受益人另有其人，買方可能買到有瑕疵的股權。"},
 {"q":"\"The Vendor intends to capitalize US$81,526,793 of its shareholders loan into 81,526,793 ordinary shares of the Company by Completion Date.\" The effect is to:",
  "o":[["A","repay the loan in cash before Completion"],["B","convert the Vendor's loan claim into newly issued shares"],["C","write off the loan without consideration"],["D","transfer the loan to the Purchaser"]],
  "a":"(B) convert the Vendor's loan claim into newly issued shares","zh":"把賣方對標的公司的貸款債權轉換為新發行的股份（債轉股）。",
  "e":"這就是為什麼股本從 (c) 的 2 股暴增為 (f) 的 81,526,793 股：資本化後買方一次買下乾淨的股權，交割後公司帳上不再有股東貸款。"},
 {"q":"Recital (b) says the Company's sole asset is its investment in D Ltd., which operates a factory in the PRC. For the Purchaser's due diligence this means:",
  "o":[["A","only the Company's own accounts matter"],["B","the real value sits one level down, so D Ltd. and the factory must also be investigated"],["C","the transaction is a pure asset purchase"],["D","PRC law is irrelevant because the Company is Singaporean"]],
  "a":"(B) the real value sits one level down, so D Ltd. and the factory must also be investigated","zh":"真正的價值在下一層，必須一併查 D Ltd. 與該工廠。",
  "e":"標的公司只是控股 SPV，買股權等於間接買下那座中國工廠。土地廠房權利、環保、勞動、關係人交易與 PRC 法令都要納入盡職調查。"},
 {"q":"Compared with Example 1, the NOW THEREFORE clause in Example 2 additionally refers to:",
  "o":[["A","consideration"],["B","representations and warranties"],["C","the recitals"],["D","the governing law"]],
  "a":"(B) representations and warranties","zh":"例二的 NOW THEREFORE 多了「表述與保證」。",
  "e":"in consideration of the mutual agreements, representations, warranties and subject to the conditions contained herein——陳述與保證是股權買賣的核心：不實時買方可請求損害賠償（warranty）或主張不實表示（misrepresentation）。"},
 {"q":"In \"the parties hereto hereby agree as follows\", **hereto** means:",
  "o":[["A","of this Agreement"],["B","to this Agreement"],["C","in this Agreement"],["D","under that document"]],
  "a":"(B) to this Agreement","zh":"hereto＝to this Agreement（本合約之）。",
  "e":"成套記：hereof＝of this Agreement；hereto＝to this Agreement；herein＝in this Agreement；hereunder＝under this Agreement；thereof＝of that（前述事物）。"}
],
"say":[
 "合約前言例二，股權買賣。簽約日單獨成句：THIS AGREEMENT is made on October twenty-eighth, two thousand twelve.",
 "當事人用 BETWEEN … AND … 分段列出，書上說，把名稱與註冊地址並列呈現比較清楚。賣方 A PTE Limited 是新加坡公司，買方 B Limited 是我國公司。每一方都要寫三件事：incorporated in 設立地、company registration number 公司註冊號碼、registered office 註冊營業所。",
 "WHEREAS 用 a 到 g 編號，等於一張盡職調查地圖。a 標的公司，b 唯一資產是對 D Ltd. 的投資，而 D 公司在中國營運一座工廠，c 股本只有兩股普通股且已發行認足，d 賣方是註冊名義人也是受益人，代表百分之百的已發行且繳足股本。",
 "e 是重點：The Vendor intends to capitalize US dollars eighty-one million five hundred twenty-six thousand seven hundred ninety-three of its shareholders loan into ordinary shares of the Company by Completion Date. 也就是股東貸款資本化，債轉股。f 於完成日，這批股份就是 the Sale Shares 標的股份。g 雙方的買賣意思。",
 "請特別記住三組易混淆用語：authorized 授權資本、issued 已發行、paid-up 或 fully paid 繳足，三者不同。registered owner 註冊名義人與 beneficial owner 受益人，兩者都要確認。representations 表述與 warranties 保證，救濟方法不同。",
 "最後 NOW THEREFORE, in consideration of the mutual agreements, representations, warranties and subject to the conditions contained herein, the parties hereto hereby agree as follows. 而第一條就是 Definitions and Interpretation，定義及解釋。"
]}
