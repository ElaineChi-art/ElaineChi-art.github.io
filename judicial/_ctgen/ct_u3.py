# -*- coding: utf-8 -*-
"""二、定義條款 Definition（書 p.27）"""
U = {
"code":"3-2-1","ch":"Chapter 參　基本條款","sec":"二、定義條款（Definition）",
"title":"定義條款 Definition：把名詞釘死，條文才有意義",
"items":[
 {"k":"lead","t":"定義條款通常是英文合約的第一條，也是最容易被跳過、卻最常出事的一條。它把合約中反覆出現的專有名詞一次定義清楚，之後凡以開頭大寫出現，就只指這個意思。本單元讀書上的說明，以及 \"Accounts\"、\"Accounting Date\" 兩個互相引用的會計類定義範例。"},

 {"k":"h1","t":"為什麼要有定義條款","ic":"📘"},
 {"k":"p","t":"於篇幅較長、內容複雜或專有名詞較多的英文合約，常常會設計一條（或專節）定義條款，內容是規定在本合約中使用的專有名詞的定義和解釋（Definitions and Interpretation）。"},
 {"k":"p","t":"通常會在英文合約第一條或第一節，但是有些合約也會把定義條款放在合約的最後一條或最後一節，以避免整份文件頭重腳輕。"},
 {"k":"p","t":"經定義之用語，於合約中使用時會以開頭大寫之英文字母呈現（例如 Manufacturer、Product、Trademark、Accounts），這代表本合約之中如果有使用到這些用語時，就代表在定義條款中所特定之文義。"},
 {"k":"tip","t":"審約口訣：**看到大寫就回頭查定義**。很多爭議不是出在義務條文寫錯，而是定義被悄悄寫寬或寫窄（例如 Affiliates、Confidential Information、Territory、Net Sales）。另外也要記得**往後翻**——定義條款不一定在第一條，有些合約擺在最後。"},

 {"k":"h1","t":"範例・定義條款的引導句","ic":"✍️"},
 {"k":"en","sp":"引導句","t":"In this Agreement, unless the contract otherwise requires, the following expressions shall have the meaning set out against them:",
  "zh":"於本合約中，除非合約另有約定，下列名詞應具有下述所載之意義："},
 {"k":"tip","t":"引導句的三個固定零件：**範圍**（In this Agreement）＋**例外**（unless the contract otherwise requires，除非合約另有約定）＋**效力**（shall have the meaning set out against them，應具有下述所載之意義）。實務上更常見的寫法是把 contract 換成 context：**unless the context otherwise requires**（除依上下文另有所指外）——兩種都要看得懂。"},

 {"k":"h1","t":"範例・定義 (a) Accounts、(b) Accounting Date","ic":"📊"},
 {"k":"en","sp":"定義 (a)","t":"(a) \"Accounts\" means the audited financial statement comprising the balance sheet, the profit and loss account and the cash flow statement of XYZ as of the Accounting Date;",
  "zh":"㈠「會計帳目」意指就 XYZ 公司於「審計日」經審計之財務報表，包括其資產負債表、損益表以及現金流量表；"},
 {"k":"en","sp":"定義 (b)","t":"(b) \"Accounting Date\" means with respect to XYZ, the date of such Accounts for the financial year ended 31 December 2012;",
  "zh":"㈡「審計日」意指就 XYZ 公司，於 2012 年 12 月 31 日所終止之會計年度之「會計帳目」之日期；"},
 {"k":"en","sp":"定義 (c)","t":"(c) \"Completion Date\" shall have the meaning specified in Clause 5;",
  "zh":"㈢「完成日」之意義應依第 5 條規定為定義；"},
 {"k":"en","sp":"定義 (d)","t":"(d) \"US$\" means the lawful currency of the United States of America.",
  "zh":"㈣「美金」意指美利堅合眾國之法定貨幣。"},
 {"k":"tip","t":"注意定義的三種寫法：**means**（直接給定義，如 Accounts、US$）、**shall have the meaning specified in Clause X**（指向別條，如 Completion Date）、以及引用其他已定義用語（Accounts 要看 Accounting Date）。被定義的名詞通常**依開頭英文字母順序**排列。"},
 {"k":"tip","t":"注意兩個定義**互相引用**：Accounts 要看 Accounting Date 才知道是哪一天的報表，而 Accounting Date 又要看 Accounts 才知道是哪一份報表。這種鏈狀結構很常見，審約時要把整條鏈拉出來看，才知道最後指向哪一份文件、哪一個日期。"},

 {"k":"h1","t":"定義條款的常見句型","ic":"🧩"},
 {"k":"p","t":"means（意指）＝封閉式定義，範圍就是後面寫的那些；includes（包括）＝開放式定義，後面只是例示，範圍可能更大；means and includes＝先封閉再補充。審約時 means 與 includes 一字之差，範圍差很多。"},
 {"k":"p","t":"其他常見解釋規則會與定義條款放在同一條（Interpretation）：words importing the singular include the plural（單數用語包含複數）、headings are for convenience only and shall not affect the interpretation（標題僅供便利，不影響解釋）、references to any statute include that statute as amended from time to time（法規之引用包括其不時修正之版本）。"},

 {"k":"h1","t":"書中解說：定義條款的功能與讀法","ic":"💡"},
 {"k":"p","t":"被定義之專有名詞，於合約中特別使用開頭字大寫（例如 this Facility…），以表彰這個名詞具有特殊意義，如此可避免合約條款中每處皆必須為特定名詞解釋，導致合約文字過長及複雜。"},
 {"k":"p","t":"於合約中特別標定開頭大寫之專有名詞，通常會於定義條款中，依開頭英文字母順序依序予以定義；定義條款中就特定專有名詞之解釋，也可以引用其他被定義之專有名詞（例如 Accounts 的定義，必須另外又視 Accounting Date 之定義）。"},
 {"k":"p","t":"對其中使用的各種用語加以定義、確定其所指涉的範圍，可以使合約清晰化，特別是可以避免或者儘量減少合約雙方搬弄文字的機會。例如，融資合約中若提到「Facility」，經過定義係指「貸款」，那麼任何一方就沒有機會指鹿為馬的將合約中出現的「Facility」稱為「配備」、「場地」或「設施」等其他涵義。這也體現了合約的重要功能，即在合約雙方產生糾紛時，以為公正評斷雙方權利義務關係之依據。"},
 {"k":"p","t":"定義和解釋條款的重要意義，還在於藉此機會詳細說明英文合約中涉及到的交易各方面爭議和問題。例如在融資合約中定義並解釋適用何種「會計準則」，即明確規定合約所針對交易中必須適用的會計準則，如果某一方不依約履行，則可能導致違約。"},
 {"k":"p","t":"定義和解釋條款的使用，還可以提高合約閱讀和理解的效率，節省合約本文的長度。但如果被定義的專有名詞太多時，有時亦會導致讀者隨時需翻閱定義條款以確定其意義，這是使用定義條款需注意之處。"},
 {"k":"tip","t":"**第一次讀英文合約的正確順序**：先通讀一遍定義和解釋條款，概略瞭解此合約涉及的基本問題；不必強記每一個定義，接下來讀主要條款與一般條款時，凡遇到開頭字母大寫的專有名詞，再索引定義和解釋，就會事半功倍。"},
 {"k":"p","t":"在我國法下，「定義條款」與其他合約條款具有相同的效力，因此原則上合約中對特定名詞的解釋，我國的法院會尊重當事人在合約中所為的「定義」。"},
 {"k":"tip","t":"⚠ 訴訟實務上的陷阱：我國法院審理時會要求當事人（或其律師）提出外文文件之**中文譯本**以方便法官審理，此時必須注意翻譯後條款的中文文字，是否確實表達英文的文義，**以免在訴訟中反而產生對自己不利的結果**。"},
 {"k":"p","t":"最後需注意的是，並非英文合約就一定需要定義條款，如果需定義之專有名詞不多，或使用的地方有限時，也可以直接於特定的條款之下為特別之定義，而不必另外設計定義條款。"},

 {"k":"voc","v":[
  {"w":"unless the contract otherwise requires","pos":"phr.","zh":"除非合約另有約定","syn":"unless the context otherwise requires（除依上下文另有所指外）","trap":"這是定義條款的**安全閥**：允許在另有約定或上下文明顯不同時不套用該定義。書上印的是 contract，實務上更通用的是 context，兩者都要認得。"},
  {"w":"expressions","pos":"n.","zh":"名詞；用語","syn":"terms／words and expressions","tip":"the following expressions shall have the meaning…＝下列名詞應具有…之意義。"},
  {"w":"shall have the meaning set out against them","pos":"phr.","zh":"應具有下述所載之意義","syn":"shall have the following meanings","tip":"set out against them 字面是「列在它們旁邊」，源自定義採兩欄並列的排版方式。"},
  {"w":"means","pos":"v.","zh":"意指（封閉式定義）","syn":"shall mean","trap":"means 是**窮盡列舉**；若要擴張範圍必須改用 includes 或 means and includes。這一字之差是審約必查點。"},
  {"w":"includes","pos":"v.","zh":"包括（開放式定義，例示）","syn":"including without limitation／including but not limited to","tip":"加上 without limitation 就是為了避免被解釋成窮盡列舉。"},
  {"w":"audited financial statement","pos":"n. phr.","zh":"經審計（查核簽證）之財務報表","syn":"audited accounts","trap":"audited（已查核）與 management accounts（管理帳，未查核）可靠度差很多；股權買賣的價金調整常綁在 audited accounts 上。"},
  {"w":"comprising","pos":"prep.","zh":"包括（由…組成）","syn":"consisting of／made up of","tip":"comprising 後面接的是組成部分，語氣偏封閉；若要留擴張空間用 including。"},
  {"w":"balance sheet","pos":"n. phr.","zh":"資產負債表","syn":"statement of financial position","tip":"表達某一時點的資產、負債與權益。"},
  {"w":"profit and loss account","pos":"n. phr.","zh":"損益表","syn":"income statement（美式）","tip":"英式用 profit and loss account，美式用 income statement，內容相同。"},
  {"w":"cash flow statement","pos":"n. phr.","zh":"現金流量表","tip":"三大報表一起背：balance sheet、profit and loss account、cash flow statement。"},
  {"w":"as of","pos":"prep.","zh":"於（截至）某日","syn":"as at（英式）","tip":"as of the Accounting Date＝於審計日。財務數字一定要綁定時點。"},
  {"w":"with respect to","pos":"prep. phr.","zh":"就…而言；關於","syn":"in respect of／in relation to","tip":"means with respect to XYZ, the date of…＝就 XYZ 公司而言，意指…之日期。用來把定義限縮在特定主體。"},
  {"w":"the financial year ended 31 December 2012","pos":"n. phr.","zh":"於 2012 年 12 月 31 日所終止之會計年度","syn":"fiscal year（美式）","trap":"ended（過去分詞）＝已結束；ending（現在分詞）＝將結束、尚未結束。一字之差時點就不同，價金調整與保證期間都會跟著錯。"},
  {"w":"words importing the singular include the plural","pos":"phr.","zh":"單數用語包含複數","tip":"解釋條款的標準句，常與 words importing one gender include every gender 併列。"},
  {"w":"headings are for convenience only","pos":"phr.","zh":"標題僅為便利之用（不影響解釋）","syn":"headings shall not affect the construction of this Agreement","tip":"construction 在合約裡是「解釋」的意思，不是「建造」。"},
  {"w":"shall have the meaning specified in Clause 5","pos":"phr.","zh":"其意義應依第 5 條規定為定義","syn":"as defined in Clause 5／has the meaning given to it in…","tip":"定義條款的第二種寫法：不在這裡給定義，而是**指向別條**。審約時要跳過去把那一條讀完。"},
  {"w":"lawful currency","pos":"n. phr.","zh":"法定貨幣","syn":"legal tender","trap":"跨境合約一定要定義幣別（US$、HK$、NTD），否則 \"dollars\" 到底是美金還是港幣會變成爭點。"},
  {"w":"Facility","pos":"n.","zh":"（融資合約中）貸款、授信額度","trap":"書中的經典例子：Facility 一般字義是「設施、場地、配備」，但在融資合約經定義後專指「貸款」。**沒定義就會被指鹿為馬**。"},
  {"w":"accounting principles / standards","pos":"n. phr.","zh":"會計準則","syn":"GAAP／IFRS","tip":"融資合約會明定適用何種會計準則，財務比率（covenants）才算得準；不依約履行可能導致違約。"},
  {"w":"as amended from time to time","pos":"phr.","zh":"及其不時之修正","trap":"引用法規時加上這句，表示包含未來修正版本；若省略，可能被解為凍結在簽約時的版本。"}
 ]}
]}

SUDU = {
"tree":"""【定義條款 Definition・骨架】
├ ① 何時需要：篇幅長、內容複雜、專有名詞多的英文合約
├ ② 擺哪裡：通常第一條或第一節；有些放最後一條或最後一節（避免文件頭重腳輕）
├ ③ 辨識方式：經定義用語一律**開頭大寫**（Manufacturer／Product／Trademark／Accounts）
│   └ 口訣：看到大寫就回頭查定義；找不到就往合約最後翻
├ ④ 引導句三零件
│   ├ 範圍 In this Agreement
│   ├ 例外 unless the contract（實務多作 context）otherwise requires
│   └ 效力 shall have the meaning set out against them
├ ⑤ 範例（會計類，兩個定義互相引用）
│   ├ (a) \"Accounts\" means the audited financial statement comprising
│   │     the balance sheet ＋ the profit and loss account ＋ the cash flow statement
│   │     of XYZ **as of the Accounting Date**
│   └ (b) \"Accounting Date\" means **with respect to XYZ**, the date of such **Accounts**
│         for the financial year **ended** 31 December 2012
├ ⑥ 另兩種定義寫法
│   ├ (c) \"Completion Date\" **shall have the meaning specified in Clause 5**（指向別條）
│   └ (d) \"US$\" means the lawful currency of the United States of America（幣別必定義）
├ ⑦ 讀法：先通讀定義條款 → 讀本文遇大寫字再回查（事半功倍）
├ ⑧ 功能：清晰化、避免搬弄文字（Facility＝貸款，不是設施）、縮短本文、爭議時的評斷依據
├ ⑨ 我國法：定義條款與其他條款效力相同，法院尊重當事人的定義
│   └ ⚠ 訴訟要提中文譯本，**譯錯會對自己不利**
├ ⑩ 不是每份合約都要定義條款（名詞不多可就地定義）
├ ⑪ 句型差異
│   ├ means ＝ 封閉式（窮盡列舉）
│   ├ includes ＝ 開放式（例示；including without limitation）
│   └ means and includes ＝ 先封閉再補充
└ ⑫ 同條常見解釋規則（Interpretation）
    ├ singular include the plural（單數包含複數）
    ├ headings are for convenience only（標題不影響解釋）
    └ statute as amended from time to time（法規含不時修正）""",
"quiz":[
 {"q":"Why are defined terms written with an initial capital letter throughout a contract?",
  "o":[["A","to emphasize their commercial importance"],["B","to signal that the word bears the specific meaning given in the definitions clause"],["C","because they are proper nouns"],["D","to show they are governed by foreign law"]],
  "a":"(B) to signal that the word bears the specific meaning given in the definitions clause","zh":"大寫是在提示該用語採定義條款所賦予之特定意義。",
  "e":"看到大寫字就不能用一般字義推測，必須回到定義條款確認範圍。書上以 Manufacturer 即代表 DEF Ltd. 公司為例。"},
 {"q":"Where is the definitions clause usually found, according to the book?",
  "o":[["A","always in the preamble, before WITNESSETH"],["B","usually the first clause or section, but sometimes the last, to avoid a top-heavy document"],["C","always as an appendix"],["D","always immediately before the signature page"]],
  "a":"(B) usually the first clause or section, but sometimes the last, to avoid a top-heavy document","zh":"通常在第一條或第一節，但有些合約放在最後，以免整份文件頭重腳輕。",
  "e":"所以查不到定義時要記得**往後翻**。審約的習慣是先把定義條款整條讀完，再回頭讀義務條文。"},
 {"q":"\"Accounts\" means the audited financial statement comprising the balance sheet, the profit and loss account and the cash flow statement … — the word **means** indicates that the definition is:",
  "o":[["A","illustrative, so other documents may also be Accounts"],["B","exhaustive, limited to the documents listed"],["C","subject to the auditors' discretion"],["D","applicable only to the balance sheet"]],
  "a":"(B) exhaustive, limited to the documents listed","zh":"means 表示封閉式、窮盡的定義，僅限所列文件。",
  "e":"means＝封閉式；若要留擴張空間要用 includes 或 including without limitation。一字之差，範圍差很多，是審約必查點。"},
 {"q":"What is the relationship between the two definitions (a) and (b)?",
  "o":[["A","they are independent of each other"],["B","each is defined by reference to the other, so the whole chain must be read together"],["C","(b) overrides (a)"],["D","(a) applies only to XYZ and (b) only to the Purchaser"]],
  "a":"(B) each is defined by reference to the other, so the whole chain must be read together","zh":"兩個定義互相引用，必須整條鏈一起讀。",
  "e":"Accounts 要靠 Accounting Date 定出時點，Accounting Date 又要靠 Accounts 定出是哪一份報表，最後才收斂到 2012 年 12 月 31 日終止之會計年度。"},
 {"q":"\"the financial year ended 31 December 2012\" — changing **ended** to **ending** would:",
  "o":[["A","make no difference"],["B","refer to a financial year that has not yet closed"],["C","extend the definition to all financial years"],["D","make the definition void"]],
  "a":"(B) refer to a financial year that has not yet closed","zh":"改成 ending 會變成指尚未結束的會計年度。",
  "e":"ended（過去分詞）＝已結束；ending（現在分詞）＝將結束、尚未結束。財務數字綁錯時點，價金調整與保證期間都會跟著錯。"},
 {"q":"\"Completion Date\" shall have the meaning specified in Clause 5. This drafting technique means:",
  "o":[["A","the term is undefined and left to the court"],["B","the definition is given elsewhere in the contract and must be read across"],["C","Clause 5 is incorporated into the definitions clause"],["D","the term only applies to Clause 5"]],
  "a":"(B) the definition is given elsewhere in the contract and must be read across","zh":"定義寫在別條，必須跳過去一併閱讀。",
  "e":"定義條款有三種寫法：means（就地定義）、shall have the meaning specified in Clause X（指向別條）、以及引用其他已定義用語。審約時要把整條鏈讀完。"},
 {"q":"According to the book, why is defining \"Facility\" as a loan in a financing agreement so important?",
  "o":[["A","to shorten the contract"],["B","to stop a party later arguing that \"Facility\" means premises, equipment or a site"],["C","because the law requires it"],["D","to satisfy the auditors"]],
  "a":"(B) to stop a party later arguing that \"Facility\" means premises, equipment or a site","zh":"為了避免一方「指鹿為馬」，把 Facility 解釋成配備、場地或設施。",
  "e":"書中用這個例子說明定義條款的核心功能：確定用語所指涉的範圍，**減少合約雙方搬弄文字的機會**，並在糾紛時作為公正評斷權利義務的依據。"}
],
"say":[
 "定義條款。於篇幅較長、內容複雜或專有名詞較多的英文合約，常常會設計一條或一節定義條款，規定本合約中使用的專有名詞的定義和解釋。",
 "位置通常在第一條或第一節，但有些合約會放在最後一條或最後一節，以避免整份文件頭重腳輕。所以查不到定義時記得往後翻。",
 "辨識方式很簡單：經定義的用語一律開頭大寫。口訣是，看到大寫就回頭查定義。",
 "引導句有三個固定零件：範圍 In this Agreement；例外 unless the contract otherwise requires，實務上更常見的寫法是 unless the context otherwise requires；效力 shall have the meaning set out against them。",
 "範例是會計類定義，而且兩個定義互相引用。Accounts means the audited financial statement comprising the balance sheet, the profit and loss account and the cash flow statement of XYZ as of the Accounting Date. 而 Accounting Date means with respect to XYZ, the date of such Accounts for the financial year ended thirty-first December, two thousand twelve.",
 "定義還有另外兩種寫法。Completion Date shall have the meaning specified in Clause 5，意義寫在別條，要跳過去讀。還有 US dollars means the lawful currency of the United States of America，跨境合約一定要定義幣別。",
 "第一次讀英文合約的正確順序是：先通讀一遍定義和解釋條款，不必強記，接下來讀主要條款時，凡遇到開頭字母大寫的專有名詞，再回頭索引定義，就會事半功倍。",
 "書中的經典例子：融資合約中的 Facility，經過定義係指貸款，那麼任何一方就沒有機會指鹿為馬，把它說成配備、場地或設施。這就是定義條款的核心功能。",
 "在我國法下，定義條款與其他合約條款效力相同，法院會尊重當事人的定義。但要特別注意，訴訟時法院會要求提出中文譯本，譯文如果沒有確實表達英文文義，反而會產生對自己不利的結果。",
 "最後記住句型差異：means 是封閉式的窮盡列舉，includes 是開放式的例示，means and includes 是先封閉再補充。一字之差，範圍差很多。"
]}
