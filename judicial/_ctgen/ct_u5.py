# -*- coding: utf-8 -*-
"""三、㈡完整合約條款 Entire Agreement（書 pp.31-32）"""
U = {
"code":"3-3-2","ch":"Chapter 參　基本條款","sec":"三、適用優先順序及完整合約條款（Preference, Entire Agreement）",
"title":"完整合約條款 Entire Agreement：之前談的全部一筆勾銷",
"items":[
 {"k":"lead","t":"談判期間來來回回的 email、意向書（LOI）、備忘錄（MOU）、口頭承諾——簽約之後還算不算數？完整合約條款就是用一句話把它們全部取代掉。這是英文合約最常見、也最容易被當成樣板而忽略的一般條款。"},

 {"k":"h1","t":"完整合約條款的功能","ic":"📘"},
 {"k":"p","t":"所謂完整合約條款（entire agreement clause or whole agreement clause），係在確認和強調一份合約中涉及和包含的所有部分，為同一份完整的合約。"},
 {"k":"p","t":"特別是對於包含諸多附件或者附表的合約來說，附件或附表都是與該合約中其他條款歸屬於同一份合約，其生效、終止、失效和執行都必須根據同一份合約中約定的內容為適用。"},

 {"k":"h1","t":"範例・完整合約條款","ic":"📄"},
 {"k":"en","sp":"完整合約","t":"This Contract contains the entire agreement of the parties and supersedes all prior agreements, arrangements and letters of intent between the parties, no matter they are made in writing and orally.",
  "zh":"本合約係包含當事人間所有的完整合約，且取代先前當事人間以書面或口頭所達成的任何協議、安排或意向書等。"},
 {"k":"tip","t":"條款的兩個動作：**contains the entire agreement（本約就是全部）** ＋ **supersedes all prior…（先前的全部取代掉）**，而且明說 in writing and orally（書面與口頭都算）。少寫任何一半，效果都會打折。"},

 {"k":"h1","t":"書中解說","ic":"💡"},
 {"k":"p","t":"完整合約條款是在說明，這份合約是代表當事人間所有就此筆交易的完整合約，而且取代當事人間先前無論是書面或口頭達成的其他協議、承諾、安排或意向書等。"},
 {"k":"p","t":"目的就在於確保當事人的權利義務關係，完全依所簽訂最終之合約文件所記載的內容為準，先前其他口頭或書面所達成的各種協議，自本合約簽訂之後即被取代，以避免將來產生法律糾紛。"},
 {"k":"p","t":"在我國法下，完整合約條款會發生當事人所約定的效果，因此在我國法下，一旦合約有完整合約條款，則先前以口頭或書面之所有的任何協議，除非完整合約條款中有所保留，否則應皆不再生任何的效力。"},
 {"k":"tip","t":"⚠ 書中的重要但書：完整合約條款**並不會影響**合約當事人依我國民法得行使之**可得撤銷合約**（例如因詐欺或脅迫而撤銷）的權利。也就是說，它可以掃掉先前的「協議」，但掃不掉對方詐欺你這件事。"},

 {"k":"voc","v":[
  {"w":"entire agreement clause","pos":"n. phr.","zh":"完整合約條款","syn":"whole agreement clause／integration clause（美式）","tip":"美式合約常以 Integration 或 Merger Clause 為標題，意思相同。"},
  {"w":"contains the entire agreement","pos":"v. phr.","zh":"包含（當事人間）所有的完整合約","syn":"constitutes the entire agreement","tip":"標準句型：This Agreement constitutes the entire agreement between the parties with respect to the subject matter hereof."},
  {"w":"supersede","pos":"v.","zh":"取代；優先於（而使先前者失效）","syn":"replace／override","trap":"supersede 是**使先前文件失效**；prevail 只是「在衝突時優先適用」，先前文件仍存在。兩個字效果差很多。"},
  {"w":"prior agreements","pos":"n. phr.","zh":"先前之協議","syn":"previous agreements／antecedent agreements","tip":"常與 arrangements、understandings、negotiations、representations 並列，寫越多掃得越乾淨。"},
  {"w":"arrangements","pos":"n.","zh":"安排；默契","tip":"比 agreement 更鬆散的合意也要一併掃掉，所以要寫進去。"},
  {"w":"letter of intent","pos":"n. phr.","zh":"意向書","syn":"LOI／MOU（memorandum of understanding）／term sheet","trap":"意向書中常有少數**有拘束力的條款**（保密、排他協商、費用分擔）。完整合約條款若沒把它們排除（carve out），可能連這些也一併失效。"},
  {"w":"no matter they are made in writing and orally","pos":"phr.","zh":"無論係以書面或口頭所達成","syn":"whether written or oral","tip":"把口頭承諾也納入取代範圍，是本條款最實用的一半。"},
  {"w":"with respect to the subject matter hereof","pos":"phr.","zh":"就本合約標的事項而言","trap":"實務上非常重要的**限縮語**：只取代「關於這筆交易」的先前協議，不會誤掃掉雙方其他不相干的合約（例如既有的保密協議、代理合約）。"},
  {"w":"save as expressly provided herein","pos":"phr.","zh":"除本合約另有明文規定外","syn":"except as otherwise provided herein","tip":"用來做 carve out（保留條款），把要留下來的先前文件挑出來。"},
  {"w":"rescind / set aside","pos":"v.","zh":"撤銷（合約）","syn":"revoke／avoid","trap":"書中特別點出：完整合約條款**不影響**因詐欺或脅迫而依民法撤銷合約的權利。它掃得掉「協議」，掃不掉「詐欺」。"},
  {"w":"non-reliance","pos":"n.","zh":"不信賴（聲明）","tip":"進階寫法：加一句雙方聲明未信賴本約以外的任何陳述（no reliance on any representation not set out herein），用來阻斷 misrepresentation 的主張。"}
 ]}
]}

SUDU = {
"tree":"""【完整合約條款 Entire Agreement・骨架】
├ ① 功能
│   ├ 確認「這一份」就是當事人間完整的合約
│   └ 附件、附表與本文同屬一份合約（生效、終止、失效、執行都依同一份）
├ ② 條款的兩個動作
│   ├ contains the entire agreement（本約即全部）
│   └ supersedes all prior agreements, arrangements and letters of intent
│       no matter they are made **in writing and orally**（書面＋口頭都掃）
├ ③ 目的：權利義務完全以最終合約文件為準，避免將來法律糾紛
├ ④ 我國法效果
│   ├ 會發生當事人約定的效果 → 先前協議除有保留外皆不再生效力
│   └ ⚠ 但**不影響**依民法得撤銷合約之權利（詐欺、脅迫）
└ ⑤ 審約必加的兩個限縮／保留
    ├ with respect to the subject matter hereof（只掃這筆交易）
    └ save as expressly provided herein（保留 LOI 中仍有效的保密／排他條款）""",
"quiz":[
 {"q":"\"This Contract … supersedes all prior agreements, arrangements and letters of intent…\" The verb **supersedes** means the prior documents:",
  "o":[["A","rank below this Contract but remain in force"],["B","cease to have effect"],["C","are incorporated into this Contract"],["D","must be re-signed"]],
  "a":"(B) cease to have effect","zh":"先前文件失其效力。",
  "e":"supersede＝取代使之失效；prevail 只是衝突時優先適用，先前文件仍然存在。這組對比是審約的基本功。"},
 {"q":"Why do the words \"no matter they are made in writing and orally\" matter?",
  "o":[["A","they extend the clause to oral promises made during negotiation"],["B","they require all agreements to be in writing"],["C","they limit the clause to written documents"],["D","they relate to the governing language"]],
  "a":"(A) they extend the clause to oral promises made during negotiation","zh":"把談判中的口頭承諾也一併取代掉。",
  "e":"談判過程中的口頭保證最難舉證也最容易生糾紛，把 oral 寫進去正是這個條款最實用的一半。"},
 {"q":"According to the book, an entire agreement clause under Taiwanese law does NOT affect:",
  "o":[["A","prior written agreements"],["B","prior oral understandings"],["C","the right to rescind the contract for fraud or duress"],["D","the schedules to the contract"]],
  "a":"(C) the right to rescind the contract for fraud or duress","zh":"不影響因詐欺或脅迫而撤銷合約的權利。",
  "e":"書中明言：完整合約條款會發生當事人約定的效果，但並不會影響合約當事人依我國民法得行使之可得撤銷合約的權利。它掃得掉「協議」，掃不掉「詐欺」。"},
 {"q":"A letter of intent contains binding confidentiality and exclusivity clauses. A plain entire agreement clause in the final contract risks:",
  "o":[["A","nothing, LOIs are never binding"],["B","wiping out those still-useful binding clauses as well"],["C","making the LOI prevail over the contract"],["D","extending the LOI indefinitely"]],
  "a":"(B) wiping out those still-useful binding clauses as well","zh":"可能連意向書中仍然有用的保密與排他條款一起掃掉。",
  "e":"所以要加保留語 save as expressly provided herein（除本合約另有明文規定外），把要留下的條款 carve out 出來。"},
 {"q":"Which added phrase stops the clause from accidentally terminating the parties' unrelated existing contracts?",
  "o":[["A","notwithstanding anything to the contrary"],["B","with respect to the subject matter hereof"],["C","time is of the essence"],["D","for the avoidance of doubt"]],
  "a":"(B) with respect to the subject matter hereof","zh":"「就本合約標的事項而言」把取代範圍限縮在這筆交易。",
  "e":"少了這一句，條款字面上會掃掉雙方之間**所有**先前協議，包括不相干的既有保密協議或代理合約。這是實務上最常見的補救語。"}
],
"say":[
 "完整合約條款。所謂完整合約條款，entire agreement clause，或稱 whole agreement clause，係在確認和強調一份合約中涉及和包含的所有部分，為同一份完整的合約。",
 "特別是對於包含諸多附件或附表的合約，附件與附表都與本文歸屬於同一份合約，其生效、終止、失效和執行都必須依同一份合約中約定的內容。",
 "範例條款：This Contract contains the entire agreement of the parties and supersedes all prior agreements, arrangements and letters of intent between the parties, no matter they are made in writing and orally.",
 "它做兩件事：第一，宣告本約就是全部；第二，把先前的協議、安排與意向書全部取代掉，而且書面與口頭都算。",
 "請分清楚兩個動詞：supersede 是取代、使先前文件失效；prevail 只是衝突時優先適用，先前文件仍然存在。",
 "在我國法下，完整合約條款會發生當事人所約定的效果，先前以口頭或書面達成的任何協議，除非條款中有所保留，否則皆不再生效力。",
 "但是請記住書上的但書：這並不會影響合約當事人依我國民法得行使之可得撤銷合約的權利，例如因詐欺或脅迫而撤銷。它掃得掉協議，掃不掉詐欺。"
]}
