# -*- coding: utf-8 -*-
"""三、適用優先順序及完整合約條款 ㈠Preference（書 pp.29-31）"""
U = {
"code":"3-3-1","ch":"Chapter 參　基本條款","sec":"三、適用優先順序及完整合約條款（Preference, Entire Agreement）",
"title":"適用優先順序條款 Preference：哪一份文件說了算",
"items":[
 {"k":"lead","t":"一筆交易往往不只一份文件：主合約、附件（Schedule）、確認書（Confirmation）、管理協議…條款打架時誰優先？這就是「合約效力適用優先順序條款」要解決的問題。本單元讀書上的說明與一則 ISDA 式的優先順序條款範例。"},

 {"k":"h1","t":"為什麼需要優先順序條款","ic":"📘"},
 {"k":"p","t":"交易本身常常不僅只有一份合約文件，此時，不同合約文件的條款如果有歧異時，就會有適用優先順序的問題。"},
 {"k":"p","t":"舉例言之，若合約文件之架構係如 ISDA 主合約系統設計為主合約、附件及確認書時，就會有主合約、附件以及確認書中的條款適用優先順序的問題，以避免不同文件之條款產生衝突或不一致（inconsistency）之情形。"},
 {"k":"p","t":"此外，如果該交易涉及多數的合約當事人時（例如債券的發行），則相關合約條款也可能會有適用優先順序的問題。例如於一中期債券發行計畫中，主要之信託合約可能於嗣後個別債券之發行後，繼續以其他文件加以補充，債券之主要條款也會因每一次債券的發行，而於個別發行文件中有所調整，因此有必要訂立合約效力適用優先順序條款予以規範。"},
 {"k":"tip","t":"兩個高風險場景要立刻想到優先順序條款：**①主合約＋附件＋確認書的架構（ISDA 衍生性金融商品）**；**②多次發行、多方當事人的架構（中期債券發行計畫 MTN）**。文件越多層，越要把誰優先寫死。"},

 {"k":"h1","t":"範例・優先順序條款","ic":"⚖️"},
 {"k":"en","sp":"附件優先","t":"In the event of any inconsistency between this Agreement and any Schedule hereto, the Schedule shall prevail.",
  "zh":"在合約及附件的條款有不一致時，則附件的條款優先適用。"},
 {"k":"en","sp":"管理協議§5 最優先","t":"Sections 5 of the Managing Agreement, which shall prevail over any inconsistent or conflicting provisions in this Agreement notwithstanding any other provisions in this Agreement to the contrary.",
  "zh":"管理協議的第 5 條將優先於本合約中任何不一致或有衝突之條款而適用，即便本合約其他條款有相反文義。"},
 {"k":"en","sp":"其餘本約優先","t":"Other than Section 5 of the Managing Agreement, in the event and to the extent that there shall be an inconsistency between the provisions of this Agreement and the provisions of the Managing Agreement, this Agreement shall prevail.",
  "zh":"除管理協議第 5 條之外，在本合約及管理協議的條款有不一致，於其不一致的範圍之內，本合約的條款優先適用。"},
 {"k":"tip","t":"把這則條款畫成**優先順序金字塔**：① 附件（Schedule）＞ 本合約；② 管理協議第 5 條 ＞ 本合約；③ 其餘情形 本合約 ＞ 管理協議。三句話建立了完整的三層次序，沒有留下空隙——這就是好的優先順序條款。"},

 {"k":"h1","t":"書中解說","ic":"💡"},
 {"k":"p","t":"在這個合約裡，除了主合約之外，尚有一些附件，另外當事人間也簽訂了一個管理協議。在這個條款之下，則附件的條款具有最優先性，除管理協議的第 5 條之外，主合約的條款將優先適用管理協議。"},
 {"k":"p","t":"合約效力適用優先順序條款的效力，於我國司法實務上會受到尊重及承認。意即，當事人若約定一部分的合約條款優先於其他部分條款的適用，我國法院會予以尊重，而依當事人的約定，決定條款適用的順序及優先性。"},

 {"k":"voc","v":[
  {"w":"inconsistency","pos":"n.","zh":"不一致；歧異","syn":"conflict／discrepancy","tip":"條款標題常寫 Inconsistency／Order of Precedence／Conflict of Terms，看到就知道是優先順序條款。"},
  {"w":"in the event of","pos":"prep. phr.","zh":"於…情形發生時","syn":"if／in case of／in the event that","tip":"in the event of＋名詞；in the event that＋子句。合約最常見的假設語句。"},
  {"w":"shall prevail","pos":"v. phr.","zh":"優先適用；以…為準","syn":"shall govern／shall take precedence over","trap":"prevail 在這裡不是「獲勝」而是「優先適用」。基準語言條款的 \"this English version shall govern\" 是同一個用法。"},
  {"w":"Schedule hereto","pos":"n. phr.","zh":"本合約之附件","syn":"Annex／Appendix／Exhibit／Attachment","trap":"附件是不是合約的一部分、能不能優先於本文，都要寫清楚，否則爭議時無解。"},
  {"w":"notwithstanding any other provisions to the contrary","pos":"phr.","zh":"即便（本合約）其他條款有相反文義","syn":"notwithstanding anything to the contrary herein","trap":"這是合約裡最強的**凌駕句**：它會蓋過其他條款。看到 notwithstanding 就要立刻找出它蓋掉了什麼。"},
  {"w":"conflicting provisions","pos":"n. phr.","zh":"有衝突之條款","syn":"inconsistent provisions","tip":"inconsistent（不一致）比 conflicting（衝突）範圍更寬，兩個字常並列使用以求周延。"},
  {"w":"to the extent that","pos":"phr.","zh":"於…之範圍內","syn":"insofar as","trap":"**限縮語**。\"to the extent that there shall be an inconsistency\" 表示只在衝突的那一小塊優先，其餘條款仍各自有效，不是整份文件被取代。"},
  {"w":"Managing Agreement","pos":"n. phr.","zh":"管理協議","tip":"債券發行中由主辦機構與發行人簽訂的協議；本例把它的第 5 條拉到最優先。"},
  {"w":"Master Agreement","pos":"n. phr.","zh":"主合約","syn":"ISDA Master Agreement","tip":"衍生性金融商品的標準架構：Master Agreement ＋ Schedule ＋ Confirmation，三層文件就是靠優先順序條款串起來。"},
  {"w":"Confirmation","pos":"n.","zh":"確認書","tip":"ISDA 架構中記載個別交易條件的文件，通常約定其條款優先於主合約。"},
  {"w":"medium term note programme","pos":"n. phr.","zh":"中期債券發行計畫","syn":"MTN programme","tip":"一次建立計畫、多次發行；每次發行的個別文件會調整主要條款，所以必須有優先順序條款。"},
  {"w":"trust deed","pos":"n. phr.","zh":"信託合約（契約）","tip":"債券發行中規範受託人與債券持有人關係的主要文件。"},
  {"w":"supplement","pos":"v./n.","zh":"補充（文件）","syn":"amend and restate","tip":"主要文件在後續發行時「繼續以其他文件加以補充」，層層疊加正是衝突的來源。"}
 ]}
]}

SUDU = {
"tree":"""【適用優先順序條款 Preference・骨架】
├ ① 問題：一筆交易不只一份文件，條款歧異時誰優先？
├ ② 兩個高風險架構
│   ├ ISDA 主合約系統：Master Agreement ＋ Schedule ＋ Confirmation
│   └ 多當事人／多次發行：中期債券發行計畫（信託合約＋個別發行文件補充）
├ ③ 範例的三層次序
│   ├ 第1句 Schedule ＞ this Agreement
│   │     In the event of any inconsistency … the Schedule shall prevail
│   ├ 第2句 Managing Agreement §5 ＞ this Agreement
│   │     notwithstanding any other provisions in this Agreement to the contrary（凌駕句）
│   └ 第3句 其餘 this Agreement ＞ Managing Agreement
│         in the event and **to the extent that**（限縮語，只在衝突範圍內）
├ ④ 關鍵字
│   ├ shall prevail ＝ 優先適用（不是「獲勝」）
│   ├ notwithstanding … to the contrary ＝ 最強凌駕句
│   └ to the extent that ＝ 只在那一塊優先
└ ⑤ 我國法：司法實務尊重當事人約定的適用順序及優先性""",
"quiz":[
 {"q":"\"In the event of any inconsistency between this Agreement and any Schedule hereto, the Schedule shall prevail.\" This means:",
  "o":[["A","the Schedule is void if it conflicts with the Agreement"],["B","the Schedule's terms are applied in preference to the Agreement's"],["C","the court decides which applies"],["D","both are applied equally"]],
  "a":"(B) the Schedule's terms are applied in preference to the Agreement's","zh":"附件的條款優先於本合約適用。",
  "e":"prevail 在合約裡＝優先適用、以…為準，不是「獲勝」。同一個用法還有基準語言條款的 this English version shall govern。"},
 {"q":"What is the effect of \"notwithstanding any other provisions in this Agreement to the contrary\"?",
  "o":[["A","it limits the clause to non-conflicting situations"],["B","it overrides every other provision of the Agreement, even those saying the opposite"],["C","it makes the clause subject to the rest of the Agreement"],["D","it has no legal effect"]],
  "a":"(B) it overrides every other provision of the Agreement, even those saying the opposite","zh":"它凌駕本合約所有其他條款，連相反文義的條款也蓋過去。",
  "e":"notwithstanding 是合約中最強的**凌駕句**。審約時看到它，要立刻回頭找出它蓋掉了哪些條款——這是最常被忽略的風險點。"},
 {"q":"\"in the event and to the extent that there shall be an inconsistency\" — the words **to the extent that** mean the priority applies:",
  "o":[["A","to the whole of the Managing Agreement"],["B","only so far as the two documents actually conflict"],["C","only if both parties agree"],["D","only after Completion"]],
  "a":"(B) only so far as the two documents actually conflict","zh":"只在兩份文件真正衝突的範圍內優先。",
  "e":"to the extent that 是**限縮語**，不衝突的部分兩份文件仍各自有效，不會整份被取代。和 notwithstanding（擴張、凌駕）剛好相反。"},
 {"q":"Under the sample clause, which document ranks highest overall?",
  "o":[["A","this Agreement"],["B","the Managing Agreement"],["C","the Schedule"],["D","they rank equally"]],
  "a":"(C) the Schedule","zh":"附件最優先。",
  "e":"次序是：附件 ＞ 本合約；管理協議第 5 條 ＞ 本合約；其餘情形本合約 ＞ 管理協議。書中說「附件的條款具有最優先性」。"},
 {"q":"Which contract architecture most urgently needs an order-of-precedence clause?",
  "o":[["A","a one-page purchase order"],["B","an ISDA master agreement with schedules and confirmations"],["C","a simple NDA"],["D","an employment contract"]],
  "a":"(B) an ISDA master agreement with schedules and confirmations","zh":"ISDA 主合約＋附件＋確認書的多層架構最需要。",
  "e":"文件層次越多、當事人越多（例如中期債券發行計畫每次發行都補充文件），條款衝突的機率越高，優先順序條款就越必要。"}
],
"say":[
 "適用優先順序條款。問題意識很簡單：一筆交易常常不只一份合約文件，不同文件的條款如果有歧異，就會有適用優先順序的問題。",
 "兩個高風險架構要記住。第一是 ISDA 主合約系統，設計為主合約、附件及確認書三層。第二是涉及多數當事人的架構，例如債券發行，中期債券發行計畫中的信託合約會在每次發行後繼續以其他文件加以補充。",
 "範例條款建立了三層次序。第一句：In the event of any inconsistency between this Agreement and any Schedule hereto, the Schedule shall prevail. 附件優先。",
 "第二句：Sections 5 of the Managing Agreement shall prevail over any inconsistent or conflicting provisions in this Agreement, notwithstanding any other provisions in this Agreement to the contrary. 管理協議第五條最優先。",
 "第三句：Other than Section 5 of the Managing Agreement, in the event and to the extent that there shall be an inconsistency, this Agreement shall prevail. 其餘情形本合約優先。",
 "三個關鍵用語：shall prevail 是優先適用，不是獲勝。notwithstanding … to the contrary 是最強的凌駕句。to the extent that 是限縮語，只在衝突的範圍內優先。",
 "最後，合約效力適用優先順序條款的效力，於我國司法實務上會受到尊重及承認，法院會依當事人的約定決定條款適用的順序及優先性。"
]}
