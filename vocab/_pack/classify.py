# -*- coding: utf-8 -*-
"""
詞彙類型分類器（規則式，可重複檢查全部資料）
類型：word 單字｜phrase 片語｜collocation 固定搭配｜compound 複合名詞｜expression 句型表達
      time 時間｜date 日期｜number 數字金額｜abbrev 縮寫｜code 代碼編號｜other 待人工確認
只有 word / phrase / collocation / compound 計入「學習詞彙量」；其餘標記後另區練習。
"""
import re

FUNC = set("""a an the of to in on at for and or but with by from as into onto over under
after before during until unless if that which who whom whose than then so such about
up down out off through across between among per via toward towards within without
is are was were be been being am do does did have has had will would shall should
can could may might must not no nor""".split())
PREP = set("""about above across after against along among around at before behind below beneath
beside between beyond by down during except for from in inside into near of off on onto out
outside over past since through throughout to toward under until up upon with within without""".split())

RX_TIME   = re.compile(r"\b\d{1,2}\s*(:\s*\d{2})?\s*(a\.?m\.?|p\.?m\.?|o'clock)\b|\b\d{1,2}:\d{2}\b", re.I)
RX_MONEY  = re.compile(r"[$€£¥]|\b(usd|ntd|twd|eur|jpy)\b|\bdollars?\b.*\d|\d+\s*(million|billion|thousand|k)\b", re.I)
RX_PCT    = re.compile(r"\d\s*%|\bpercent\b.*\d|\b\d+\s*(percent|off)\b", re.I)
RX_DATE   = re.compile(r"\b(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}(st|nd|rd|th)?\b"
                       r"|\b\d{1,2}(st|nd|rd|th)\s+(of\s+)?(january|february|march|april|may|june|july|august|september|october|november|december)\b"
                       r"|\b(end|beginning|start|mid)\s+of\s+(the\s+)?(month|quarter|year|week)\b"
                       r"|\bq[1-4]\b"
                       r"|\b\d{1,2}\s+(days?|weeks?|months?|years?|hours?|minutes?|business days?|working days?)\b"
                       r"|\b(mon|tues|wednes|thurs|fri|satur|sun)day\b", re.I)
RX_CODE   = re.compile(r"\b[A-Z]{1,4}[-–]?\d{2,}\b|\b\d{3}-\d{4}\b|\b[A-Z]{2,}\d+\b")
RX_ABBR   = re.compile(r"^[A-Z]{2,6}$|^(?:[A-Z]\.){2,}$|^[A-Z][a-z]{0,3}\.$|^\d+\(k\)$|^[A-Z](?:&[A-Z])+$")  # 大小寫敏感
RX_SENT   = re.compile(r"[.?!]\s*$|^(please|could|would|thank|we|i|you|it|there)\b", re.I)

ART = {"a","an","the"}
def tokens(t):
    return re.findall(r"[^\W\d_][\w'\-]*|\d+[\w%$.]*", t, re.UNICODE)

def n_pre(ws): return len(ws)

def classify(term, pos=""):
    """回傳 (kind, needs_review, why)"""
    t = (term or "").strip()
    p = (pos or "").strip().lower()
    if not t: return "other", True, "空白"
    ws = tokens(t)
    low = t.lower()
    has_digit = bool(re.search(r"\d", t))

    # —— 非一般詞彙：時間 / 日期 / 數字金額 / 代碼 / 縮寫 ——
    if RX_CODE.search(t) and has_digit:            return "code", False, "代碼或編號格式"
    if RX_TIME.search(t):                          return "time", False, "時間表達"
    # 日期要排在數字前面，否則 "October 1st" 會被當成數字
    if RX_DATE.search(t) and has_digit:            return "date", False, "日期或期間"
    # 含數字又長到像一句話 → 句型表達（例：Improve efficiency by 40%）
    if has_digit and (n_pre(ws) >= 4 or RX_SENT.search(t)):
                                                   return "expression", False, "含數字的整句或長詞組"
    if RX_PCT.search(t) or RX_MONEY.search(t):     return "number", False, "數字／金額／百分比"
    if has_digit and n_pre(ws) <= 3:               return "number", False, "含數字的量值"
    if has_digit and (pos or "").strip().lower().startswith("n"):
        return "compound", True, "含數字但為名詞性詞組"
    if RX_ABBR.match(t.strip()):
        return "abbrev", False, "縮寫"

    n = len(ws)
    # 動詞＋冠詞＋名詞（meet a deadline / submit an application）＝固定搭配，不是一般片語
    if p.startswith("v") and 2 <= n <= 4:
        others = [w.lower() for w in ws[1:] if w.lower() in FUNC]
        if all(w in ART for w in others):
            return "collocation", False, "動詞＋名詞固定搭配"
    # —— 句型／固定表達 ——
    if p.startswith("clause") or RX_SENT.search(t) or n >= 6:
        if n >= 3: return "expression", n < 4, "整句或子句型表達"
    # —— 單字 ——
    if n == 1:
        if re.fullmatch(r"[^\W\d_][\w'\-]*", t, re.UNICODE): return "word", False, "單一英文詞"
        return "other", True, "單一 token 但含非字母"
    # —— 多字：看有沒有功能詞 ——
    lows = [w.lower() for w in ws]
    has_prep = any(w in PREP for w in lows)
    has_func = any(w in FUNC for w in lows)
    if has_prep or (has_func and n <= 4):
        return "phrase", False, "含介系詞或功能詞的片語"
    # —— 動詞開頭且 2-3 字 → 固定搭配（動＋名）——
    if p.startswith("v") and 2 <= n <= 4:
        return "collocation", False, "動詞＋名詞固定搭配"
    if p.startswith("adv") or (p.startswith("adj") and n == 2):
        return "collocation", False, "副詞／形容詞固定搭配"
    # —— 名詞性 2-3 字且無功能詞 → 複合名詞 ——
    if p.startswith("n") and 2 <= n <= 3:
        return "compound", False, "名詞＋名詞複合名詞"
    if 2 <= n <= 3 and not has_func:
        return "compound", True, "疑似複合名詞（詞性缺漏）"
    return "phrase", True, "多字但無法判定，暫列片語"

COUNTABLE = {"word", "phrase", "collocation", "compound"}
KIND_ZH = {"word":"單字","phrase":"片語","collocation":"固定搭配","compound":"複合名詞",
           "expression":"句型表達","time":"時間表達","date":"日期","number":"數字金額",
           "abbrev":"縮寫","code":"代碼","other":"待人工確認"}
