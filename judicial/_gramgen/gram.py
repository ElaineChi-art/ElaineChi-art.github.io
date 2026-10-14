# -*- coding: utf-8 -*-
"""
句構標記：用 spaCy 分析每個 en 句子，產生「主詞／動詞／副詞／名詞子句／形容詞子句／連接詞」
的分段標記與主幹，寫進資料檔的 en 項目的 g 欄位。
規則依《英文句子標記法筆記》：先找動詞 → 再抓主詞 → 把＜副詞＞遮掉 → 剩下就是主幹。
"""
import json, os, re, sys
import spacy

NLP = spacy.load("en_core_web_sm")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLEAN = lambda s: re.sub(r"\s+", " ", str(s).replace("**", "").replace("—[", "").replace("]—", "")).strip()

# 角色：S 主詞 V 動詞 O 受詞 C 補語 A 副詞 N 名詞子句 J 形容詞子句 K 連接詞/關係詞
SUBJ = {"nsubj", "nsubjpass", "expl"}
OBJ  = {"dobj", "dative", "obj"}
COMP = {"attr", "acomp", "oprd"}
ADV  = {"prep", "advmod", "advcl", "npadvmod", "agent", "prt"}
NCL  = {"ccomp", "csubj", "csubjpass", "xcomp", "pcomp"}

WH = {"WDT", "WP", "WP$", "WRB"}

def span_of(tok):
    ids = [t.i for t in tok.subtree]
    return min(ids), max(ids)

def label_adv(span_toks):
    """給副詞成分一個中文說明。"""
    first = span_toks[0]
    low = first.text.lower()
    if first.dep_ == "advcl" or low in ("because", "since", "as", "when", "while", "if",
                                        "although", "though", "unless", "after", "before",
                                        "until", "once", "whereas"):
        m = {"because": "原因", "since": "原因／時間", "when": "時間", "while": "時間／對比",
             "if": "條件", "unless": "條件", "although": "讓步", "though": "讓步",
             "after": "時間", "before": "時間", "until": "時間", "once": "時間",
             "whereas": "對比", "as": "原因／時間"}.get(low, "")
        if first.tag_ == "VBG": return "分詞構句（副詞）→ 可遮掉"
        return ("%s副詞子句 → 可遮掉" % m) if m else "副詞子句 → 可遮掉"
    if first.dep_ == "prep" or first.pos_ == "ADP":
        return "介系詞片語（副詞）→ 可遮掉"
    if first.tag_ == "TO" or (first.text.lower() == "to" and len(span_toks) > 1):
        return "不定詞表目的 → 可遮掉"
    return "副詞 → 可遮掉"

def analyse(sent_text):
    txt = CLEAN(sent_text)
    if not txt: return None
    doc = NLP(txt)
    n = len(doc)
    if n < 3: return None
    root = next((t for t in doc if t.dep_ == "ROOT"), None)
    if root is None: return None
    toks = list(doc)
    role = [""] * n

    # 每個子句的動詞（ROOT 以及 ccomp/advcl/relcl/acl/csubj/conj 的中心動詞）
    verbs = {root.i}
    for t in doc:
        if t.dep_ in ("ccomp", "csubj", "csubjpass", "advcl", "relcl", "acl", "pcomp", "conj") \
           and t.pos_ in ("VERB", "AUX"):
            verbs.add(t.i)

    # 先收集所有成分，大的先寫、小的後寫（內層蓋過外層）
    spans = []
    for t in doc:
        if t.i in verbs: continue
        d = t.dep_
        r = ("S" if d in SUBJ else "O" if d in OBJ else "C" if d in COMP else
             "N" if d in NCL else "J" if d in ("relcl", "acl") else
             "A" if d in ADV and d != "prt" else "")
        if not r: continue
        a_, b_ = span_of(t)
        spans.append((b_ - a_, a_, b_, r, t))
    spans.sort(key=lambda x: -x[0])
    for _, a_, b_, r, t in spans:
        for i in range(a_, b_ + 1): role[i] = r

    # 動詞最後蓋（含助動詞與否定）
    vmap = {}
    for vi in verbs:
        v = doc[vi]
        ids = sorted({vi} | {c.i for c in v.children if c.dep_ in ("aux", "auxpass", "neg")})
        vmap[vi] = ids
        for i in ids: role[i] = "V"
    # 連接詞／關係詞（單字，最高優先）
    for t in doc:
        if t.dep_ in ("mark", "cc"):
            role[t.i] = "K"
        elif t.tag_ in WH and t.head.dep_ in ("relcl", "acl"):
            role[t.i] = "K"

    # 合併連續同角色 → chunk（保留原始空白）
    chunks, i = [], 0
    while i < n:
        j = i
        while j + 1 < n and role[j + 1] == role[i]: j += 1
        a_ = toks[i].idx; b_ = toks[j].idx + len(toks[j].text)
        pre = txt[chunks[-1][2]:a_] if chunks else txt[:a_]
        chunks.append([pre + txt[a_:b_], role[i], b_])
        i = j + 1
    if chunks and chunks[-1][2] < len(txt): chunks[-1][0] += txt[chunks[-1][2]:]
    out = [[c[0], c[1]] for c in chunks]

    # ── 條列說明：只列主句層級＋全句的形容詞子句 ──
    rows = []
    vids = vmap.get(root.i, [root.i])
    tense = "過去式" if root.tag_ in ("VBD", "VBN") else ("現在式" if root.tag_ in ("VBZ", "VBP") else "")
    rows.append(["V", " ".join(doc[i].text for i in vids),
                 "主要動詞" + ("（%s）" % tense if tense else "")
                 + ("　被動語態" if any(c.dep_ == "auxpass" for c in root.children) else "")])
    for ch in root.children:
        a_, b_ = span_of(ch); seg = doc[a_:b_+1].text
        if ch.dep_ in SUBJ:      rows.append(["S", seg, "主詞"])
        elif ch.dep_ in OBJ:     rows.append(["O", seg, "受詞"])
        elif ch.dep_ in COMP:    rows.append(["C", seg, "補語"])
        elif ch.dep_ in NCL:     rows.append(["N", seg, "名詞子句 ＝ " + ("主詞" if ch.dep_.startswith("csubj") else "受詞")])
        elif ch.dep_ in ADV and ch.dep_ != "prt":
            rows.append(["A", seg, label_adv(list(doc[a_:b_+1]))])
    for t in doc:
        for ch in t.children:
            if ch.dep_ in ("relcl", "acl"):
                a_, b_ = span_of(ch)
                rows.append(["J", doc[a_:b_+1].text, "形容詞子句 → 修飾「%s」" % t.text])

    # ── 主幹：拿掉主句層級的副詞；名詞子句縮成〔…〕 ──
    drop = set()
    for ch in root.children:
        if ch.dep_ in ADV and ch.dep_ != "prt":
            if ch.i == 0 and ch.tag_ in WH: continue        # 疑問句開頭的 How/Why… 要留著
            a_, b_ = span_of(ch); drop |= set(range(a_, b_ + 1))
            if ch.i - 1 >= 0 and doc[ch.i - 1].dep_ == "mark": drop.add(ch.i - 1)
    for t in doc:                                            # 形容詞子句也從主幹拿掉
        for ch in t.children:
            if ch.dep_ in ("relcl", "acl"):
                a_, b_ = span_of(ch); drop |= set(range(a_, b_ + 1))
    collapse = {}
    for ch in root.children:
        if ch.dep_ in NCL:
            a_, b_ = span_of(ch)
            if b_ - a_ >= 4:
                for i in range(a_, b_ + 1): collapse[i] = (a_ == i)
    core, i = "", 0
    while i < n:
        if i in drop: i += 1; continue
        if i in collapse:
            if collapse[i]: core += " 〔…〕"
            i += 1; continue
        core += (" " if core and not doc[i].is_punct else "") + doc[i].text
        i += 1
    core = re.sub(r"\s+", " ", core).strip(" ,;")
    if core and not core.endswith((".", "?", "!")): core += "。"

    seen, rows2 = set(), []
    for r in rows:
        k = (r[0], r[1])
        if k in seen: continue
        seen.add(k); rows2.append(r)
    return {"t": out, "c": core, "r": rows2}

def run(fn, var, codes_prefix):
    p = os.path.join(ROOT, fn)
    s = open(p, encoding="utf-8").read()
    D = json.loads(re.search(r"window\." + var + r"=(.*);$", s, re.S).group(1))
    done = 0
    for t in D:
        if codes_prefix and not t["code"].startswith(codes_prefix): continue
        for it in t["items"]:
            if it["k"] != "en": continue
            g = analyse(it["t"])
            if g: it["g"] = g; done += 1
    open(p, "w", encoding="utf-8").write("window." + var + "=" + json.dumps(D, ensure_ascii=False) + ";")
    print("%s：標了 %d 句" % (fn, done))

if __name__ == "__main__":
    fn  = sys.argv[1] if len(sys.argv) > 1 else "toeic-data.js"
    var = sys.argv[2] if len(sys.argv) > 2 else "TOEIC"
    pre = sys.argv[3] if len(sys.argv) > 3 else "16-"
    run(fn, var, pre)
