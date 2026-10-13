# -*- coding: utf-8 -*-
"""四、㈥期間及續約 Term and Renewal（書 pp.41-43）"""
U = {
"code":"3-4-5","ch":"Chapter 參　基本條款","sec":"四、合約效力及內容範圍（Contract Effectiveness）",
"title":"期間及續約 Term and Renewal：合約活多久、怎麼自動展延",
"items":[
 {"k":"lead","t":"合約什麼時候到期？到期之後會不會自己續下去？期間條款與續約條款就是在處理這兩件事。本單元讀一則「一年期＋九十日前書面通知否則按月自動展延」的標準條款，並對照我國民法第 102 條。"},

 {"k":"h1","t":"期間與續約條款的功能","ic":"📘"},
 {"k":"p","t":"合約的期間條款，規定了合約於何時到期，如何認定合約的到期，以及在合約到期時如何延長合約的期間。"},
 {"k":"p","t":"合約會因為以下幾種情況到期：首先是法定的合約期限，由適用的法律來規定某些合約不得超過一定的年限；其次，是雙方約定的期限，合約雙方在合約中議訂合約的期限；第三，無期限合約，但是雙方可以在合約中加入合約終止條款（terminations），規定在何種情形下合約可以終止。"},
 {"k":"p","t":"而續約條款係規範在合約期限到期之時，合約雙方根據何種條件為合約的續約。"},
 {"k":"tip","t":"三種到期型態要分清楚：**①法定期限**（法律限制最長年限）**②約定期限**（雙方自己訂）**③無期限但有終止條款**。第三種最容易被誤以為「永久有效」，其實是靠 termination clause 來收尾。"},

 {"k":"h1","t":"範例・期間及續約條款","ic":"📅"},
 {"k":"en","sp":"標題","t":"Term","zh":"期間"},
 {"k":"en","sp":"(a) 期間","t":"(a) The term of this Agreement shall be for one (1) year commencing on the 1st day of August 2012 and terminating on the 31st day of July, 2013 (the \"Term\"), unless otherwise terminated pursuant to this Agreement.",
  "zh":"(a) 本合約之期間為一年，自 2012 年 8 月 1 日起算，至 2013 年 7 月 31 日止（以下稱「期間」），除非另外有依本合約之約定終止本合約。"},
 {"k":"en","sp":"(b) 自動展延","t":"(b) Unless terminated or unless either party has given the other at least ninety (90) days written notice of its intention to terminate the Agreement prior to expiration, then the Term shall automatically be extended from month to month after its expiration.",
  "zh":"(b) 除非依本合約約定終止本合約，或任一方當事人於合約期間終止前九十日以書面通知他方，則本合約之期間將自期間屆滿時起每月展延。"},
 {"k":"p","t":"這個條款的目的基本上有兩個，第一個目的在於說明，這份合約的期間為一年，並特別指明開始及終止的日期，以免爭議；其次，這個條款也約定，原則上本合約於期限屆滿之後，會自動按月展延，除非當事人有提前以書面通知他方，這就是自動展延的條款。"},
 {"k":"tip","t":"自動展延條款的三個關鍵數字要一起看：**展延單位**（from month to month 按月／year to year 按年）、**通知期間**（at least ninety days）、**通知方式**（written notice）。少看一個，就可能錯過退出的時間窗，被自動綁下一期。"},

 {"k":"h1","t":"我國法對照：民法第 102 條","ic":"⚖️"},
 {"k":"p","t":"在我國法下，依民法第 102 條第 1 項及第 2 項的規定：「附始期之法律行為，於期限屆至時，發生效力。」「附終期之法律行為，於期限屆滿時，失其效力。」"},
 {"k":"p","t":"在一份合約之中，雖然合約的簽字日不必然為合約的生效日，惟除非有特別約定，合約通常係自簽約日生效（as of the date hereof）。我國民法雖然沒有針對「展延」有特別的規定，不過原則上如果當事人如上述條款有自動展延的約定，我國法院也會予以尊重。"},

 {"k":"voc","v":[
  {"w":"term","pos":"n.","zh":"（合約）期間","trap":"注意一字多義：**the Term**（大寫，合約期間）／**terms**（條款）／**terms and conditions**（條款）。讀合約時看大寫與單複數分辨。"},
  {"w":"commencing on","pos":"v. phr.","zh":"自…起算","syn":"starting from／with effect from","tip":"commence＝開始（正式用語），合約中幾乎不用 start。"},
  {"w":"terminating on","pos":"v. phr.","zh":"至…止","syn":"expiring on／ending on","tip":"期間一定要寫明起訖日，書中說「特別指明開始及終止的日期，以免爭議」。"},
  {"w":"unless otherwise terminated pursuant to this Agreement","pos":"phr.","zh":"除非另依本合約之約定終止","tip":"把提前終止的可能性保留下來，避免與終止條款衝突。"},
  {"w":"written notice","pos":"n. phr.","zh":"書面通知","syn":"notice in writing","trap":"要回頭看 Notices（通知）條款：書面包不包括 email？送達以寄出日還是收到日為準？這決定九十日怎麼算。"},
  {"w":"notice of its intention to terminate","pos":"n. phr.","zh":"終止意思之通知","syn":"notice of non-renewal","tip":"不續約通知與終止通知在實務上常混用，條款怎麼寫就怎麼算。"},
  {"w":"prior to expiration","pos":"prep. phr.","zh":"於期間屆滿前","syn":"before the expiry of the Term","tip":"與 Long Stop Date 一樣，時點是爭議核心。"},
  {"w":"automatically be extended","pos":"v. phr.","zh":"自動展延","syn":"shall automatically renew／evergreen clause","trap":"俗稱 **evergreen clause（長青條款）**。錯過通知期間就被綁下一期，是最常見的商務地雷。"},
  {"w":"from month to month","pos":"phr.","zh":"按月（展延）","syn":"from year to year／for successive one-year periods","tip":"展延單位決定你下次能退出的時間點。"},
  {"w":"expiration","pos":"n.","zh":"期間屆滿","syn":"expiry（英式）","trap":"expiration（自然屆滿）≠ termination（提前終止），兩者在效力保留、違約金、通知條款的效果都不同。"},
  {"w":"termination clause","pos":"n. phr.","zh":"終止條款","syn":"termination for convenience（任意終止）／termination for cause（有因終止）","tip":"無期限合約就是靠終止條款收尾，規定在何種情形下合約可以終止。"},
  {"w":"renewal","pos":"n.","zh":"續約","syn":"extension／roll-over","tip":"renewal 通常指成立新期間，extension 指延長原期間，審約時看定義怎麼寫。"},
  {"w":"as of the date hereof","pos":"phr.","zh":"自本合約簽約日起","syn":"with effect from the date of this Agreement","tip":"書中點出：合約的簽字日不必然為生效日，惟除非有特別約定，通常自簽約日生效。"},
  {"w":"附始期／附終期","pos":"n. phr.","zh":"民法§102 的始期與終期","tip":"附始期之法律行為於期限屆至時發生效力；附終期之法律行為於期限屆滿時失其效力。"}
 ]}
]}

SUDU = {
"tree":"""【期間及續約 Term and Renewal・骨架】
├ ① 期間條款管三件事：何時到期、如何認定到期、到期如何延長
├ ② 合約到期的三種型態
│   ├ ㈠法定期限（法律規定某些合約不得超過一定年限）
│   ├ ㈡約定期限（雙方自行議訂）
│   └ ㈢無期限合約 ＋ 終止條款（terminations）規定何種情形可終止
├ ③ 範例 (a) 期間
│   └ for one (1) year **commencing on** 1 Aug 2012 **and terminating on** 31 Jul 2013 (the \\"Term\\"),
│     unless otherwise terminated pursuant to this Agreement
├ ④ 範例 (b) 自動展延（evergreen）
│   ├ Unless terminated or unless either party has given **at least ninety (90) days written notice**
│   │   of its intention to terminate **prior to expiration**
│   └ then the Term shall **automatically be extended from month to month**
│   └ 三個關鍵數字：展延單位／通知期間／通知方式
└ ⑤ 我國法
    ├ 民法§102Ⅰ 附始期之法律行為，於期限屆至時發生效力
    ├ 民法§102Ⅱ 附終期之法律行為，於期限屆滿時失其效力
    ├ 簽字日≠生效日，但除非特別約定通常自簽約日生效（as of the date hereof）
    └ 民法未規定「展延」，但法院尊重當事人的自動展延約定""",
"quiz":[
 {"q":"Under the sample clause, what must a party do to stop the agreement rolling on?",
  "o":[["A","nothing; it ends automatically on 31 July 2013"],["B","give the other party at least 90 days' written notice before expiration"],["C","obtain the other party's consent"],["D","apply to court"]],
  "a":"(B) give the other party at least 90 days' written notice before expiration","zh":"於期間屆滿前至少九十日以書面通知他方。",
  "e":"這就是 evergreen（長青）條款的陷阱：**什麼都不做反而會被自動綁下一期**，而且本例是按月展延。"},
 {"q":"\"the Term shall automatically be extended from month to month\" means each extension lasts:",
  "o":[["A","one year"],["B","one month"],["C","until terminated by court"],["D","indefinitely with no exit"]],
  "a":"(B) one month","zh":"每次展延一個月。",
  "e":"展延單位決定你下次能退出的時間點。若寫 from year to year，錯過通知就要再等一年。"},
 {"q":"Which is NOT one of the three ways a contract comes to an end, per the book?",
  "o":[["A","a statutory maximum term"],["B","a term agreed by the parties"],["C","no fixed term, but with a termination clause"],["D","unilateral revocation at any time without any clause"]],
  "a":"(D) unilateral revocation at any time without any clause","zh":"沒有任何條款依據就片面撤回，不是書中所列的型態。",
  "e":"書中列舉：㈠法定的合約期限㈡雙方約定的期限㈢無期限合約但加入合約終止條款（terminations）。"},
 {"q":"\"附終期之法律行為，於期限屆滿時，失其效力\" corresponds to:",
  "o":[["A","民法第 99 條"],["B","民法第 102 條第 2 項"],["C","民法第 111 條"],["D","民法第 98 條"]],
  "a":"(B) 民法第 102 條第 2 項","zh":"附終期之法律行為，於期限屆滿時，失其效力。",
  "e":"§102Ⅰ 附始期→期限屆至發生效力；§102Ⅱ 附終期→期限屆滿失其效力。與§99（條件）成對記：條件管「會不會發生」，期限管「什麼時候」。"},
 {"q":"According to the book, the signing date of a contract:",
  "o":[["A","is always the effective date"],["B","is never the effective date"],["C","is not necessarily the effective date, but absent special agreement the contract usually takes effect from signing"],["D","must be approved by the court"]],
  "a":"(C) is not necessarily the effective date, but absent special agreement the contract usually takes effect from signing","zh":"簽字日不必然為生效日，惟除非特別約定，通常自簽約日生效。",
  "e":"要另訂生效日就寫清楚，例如 with effect from…；否則就是 as of the date hereof。"}
],
"say":[
 "期間及續約條款。合約的期間條款規定了合約於何時到期、如何認定合約的到期，以及在合約到期時如何延長合約的期間。",
 "合約會因為三種情況到期。第一是法定的合約期限，由適用的法律規定某些合約不得超過一定的年限。第二是雙方約定的期限。第三是無期限合約，但雙方可以加入合約終止條款，規定在何種情形下合約可以終止。",
 "範例 a 項：The term of this Agreement shall be for one year commencing on the first day of August two thousand twelve and terminating on the thirty-first day of July two thousand thirteen, the Term, unless otherwise terminated pursuant to this Agreement.",
 "範例 b 項是自動展延：Unless terminated or unless either party has given the other at least ninety days written notice of its intention to terminate the Agreement prior to expiration, then the Term shall automatically be extended from month to month after its expiration.",
 "自動展延條款俗稱長青條款，evergreen clause。三個關鍵數字要一起看：展延單位是按月還是按年、通知期間幾天、以及通知方式是不是書面。少看一個就會被自動綁下一期。",
 "我國法對照，民法第一百零二條第一項：附始期之法律行為，於期限屆至時，發生效力。第二項：附終期之法律行為，於期限屆滿時，失其效力。",
 "另外請記住，合約的簽字日不必然為合約的生效日，但除非有特別約定，合約通常自簽約日生效，英文寫作 as of the date hereof。我國民法雖然沒有針對展延的特別規定，不過法院原則上會尊重當事人自動展延的約定。"
]}
