# -*- coding: utf-8 -*-
"""
把 judicial/toeic-data.js 的 60 個多益場景字彙，做成每日英文單字庫可直接吃的資料包。
輸出 vocab/toeic-pack.js（window.TOEIC_PACK），格式同站上的備份碼 {db:{日期:{words:{}}}, shelves:[]}。

規則
- 一天一個場景，依「難易度由易到難」排程（場景平均詞頻）
- 每個詞條三句例句：①本單元原文句（含課本中譯）②其他單元原文句／上下文句 ③自製例句（免費翻譯補中文）
- 初始熟悉度依詞頻分成 熟／普通／不熟，之後由使用者自己點
"""
import json, os, re, sys, time, random, datetime, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOEIC = os.path.join(ROOT, "judicial", "toeic-data.js")
OUT   = os.path.join(ROOT, "vocab", "toeic-pack.js")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
CLEAN = lambda s: re.sub(r"\s+", " ", re.sub(r"—\[\d+\]—", "", str(s or "").replace("**", ""))).strip()

try:
    from wordfreq import zipf_frequency as _z
except Exception:
    _z = None
def zipf(w): return _z(w, "en") if _z else 3.5

# ── 免費批次翻譯（與 NPR 流程同一套）──────────────────────────────
_TR = {}
def _batch(texts):
    qs = "&".join("q=" + urllib.parse.quote(t) for t in texts)
    for base in ("https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=zh-TW&",
                 "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-TW&dt=t&"):
        try:
            raw = urllib.request.urlopen(urllib.request.Request(base + qs, headers=UA), timeout=25).read().decode()
            d = json.loads(raw)
            if base.startswith("https://clients5"):
                out = d if isinstance(d, list) and all(isinstance(x, str) for x in d) else None
            else:
                grp = d[0] if isinstance(d, list) else []
                out = ["".join(x[0] for x in grp if x and x[0])] if len(texts) == 1 else None
            if out and len(out) == len(texts):
                return [re.sub(r"\s+", " ", x).strip() for x in out]
        except Exception:
            time.sleep(1.0)
    return None

def tr_many(texts):
    todo, seen = [], set()
    for t in texts:
        if t and t not in _TR and t not in seen:
            seen.add(t); todo.append(t)
    i = 0
    while i < len(todo):
        chunk, n = [], 0
        while i < len(todo) and len(chunk) < 8 and n < 1500:
            chunk.append(todo[i]); n += len(todo[i]); i += 1
        got = _batch(chunk)
        if got is None and len(chunk) > 1:
            got = []
            for c in chunk:
                one = _batch([c]); got.append(one[0] if one else ""); time.sleep(0.3)
        for c, g in zip(chunk, got or [""] * len(chunk)):
            _TR[c] = g or ""
        time.sleep(0.35)
        if i % 160 == 0: print("   翻譯 %d/%d" % (i, len(todo)), flush=True)
    return [_TR.get(t, "") for t in texts]

# ── 詞條處理 ────────────────────────────────────────────────────
STOP = set("a an the of to in on at for and or with by from is are was were be been being this that".split())
def core_of(term):
    """取可用來比對原文的主體：去掉斜線備選、括號說明。"""
    t = re.split(r"\s*/\s*|（|\(|\.{3}|…|\bvs\b", term, flags=re.I)[0].strip().strip(".,;:")
    return t or term
def head_words(term):
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'\-]+", term) if w.lower() not in STOP]
def difficulty(term):
    hs = head_words(term)
    if not hs: return 3.5
    return min(zipf(h) for h in hs)
def level_of(term):
    z = difficulty(term)
    return "strong" if z >= 4.5 else ("mid" if z >= 3.4 else "weak")

def rx_for(core):
    """彈性比對：詞與詞之間允許夾 0-2 個字（a/the/your…），字尾允許變化。"""
    ws = [w for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", core)]
    if not ws: return None
    parts = [re.escape(ws[0]) + r"[A-Za-z]{0,3}"]
    for w in ws[1:]:
        parts.append(r"(?:\W+[A-Za-z']+){0,2}\W+" + re.escape(w) + r"[A-Za-z]{0,3}")
    try: return re.compile(r"\b" + "".join(parts), re.I)
    except re.error: return None

def content_words(core):
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'\-]{1,}", core) if w.lower() not in STOP]

def cover(sentence, ws):
    """句子涵蓋了詞條的幾個實詞（允許字尾變化）。"""
    low = sentence.lower()
    return sum(1 for w in ws if re.search(r"\b" + re.escape(w) + r"[a-z]{0,3}\b", low))

POSKIND = lambda p: ("v" if re.match(r"^v", (p or "").strip(), re.I) else
                     "adj" if re.match(r"^adj", (p or "").strip(), re.I) else
                     "adv" if re.match(r"^adv", (p or "").strip(), re.I) else
                     "n" if re.match(r"^n", (p or "").strip(), re.I) else "")
T_N  = ["Please confirm the {t} before the meeting ends.",
        "Our manager asked about the {t} this morning.",
        "We will send you the {t} by the end of the day.",
        "The client wants to review the {t} first."]
T_V  = ["Our team will {t} the request before Friday.",
        "Could you {t} this with the supplier today?",
        "We need to {t} it again after the update.",
        "They agreed to {t} the plan next quarter."]
T_AJ = ["The manager found the new proposal {t}.",
        "Customers told us the service was {t}.",
        "This part of the report is {t}.",
        "Everyone agreed that the result was {t}."]
T_AV = ["The team handled the request {t}.",
        "We reviewed the figures {t} before approval.",
        "She replied to the client {t}.",
        "The shipment was processed {t}."]
BAD = re.compile(r"n't|\d|\(|\)|/|%|…|\.{3}|\bvs\b", re.I)
BAD_CAPS = re.compile(r"[A-Z]{2,}")   # 大小寫敏感，re.I 會讓它比到所有字

def make_template(term, pos):
    core = core_of(term)
    kind = POSKIND(pos)
    if not kind or BAD.search(core) or BAD_CAPS.search(core) or len(core.split()) > 5: return ""
    core = core[0].lower() + core[1:] if core[:1].isupper() else core
    if kind == "v":
        head = core.split()[0].lower()
        if head in ("not", "no", "never", "be", "been", "being"): return ""
        if head.endswith(("ing", "ed")) or (head.endswith("s") and not head.endswith("ss")): return ""
        bank = T_V
    elif kind == "adj": bank = T_AJ
    elif kind == "adv": bank = T_AV
    else:
        bank = T_N
        core = core[0].lower() + core[1:] if core[:1].isupper() and core.lower() == core.lower() else core
    return random.choice(bank).format(t=core)

# ── 主程式 ──────────────────────────────────────────────────────
def main():
    D = json.loads(re.search(r"window\.TOEIC=(.*);$", open(TOEIC, encoding="utf-8").read(), re.S).group(1))
    corpus, bycode = [], {}
    for t in D:
        lst = []
        for it in t["items"]:
            if it["k"] == "en":
                e, z = CLEAN(it["t"]), CLEAN(it.get("zh"))
                if len(e) > 18: lst.append((e, z))
        bycode[t["code"]] = lst
        corpus += [(e, z, t["code"]) for e, z in lst]
    print("語料句 %d" % len(corpus))

    scenes = []
    for t in D:
        seen, items = set(), []
        for it in t["items"]:
            if it["k"] != "voc": continue
            for v in it["v"]:
                w = (v.get("w") or "").strip()
                k = w.lower()
                if not w or k in seen: continue
                seen.add(k); items.append(v)
        if items:
            scenes.append({"code": t["code"], "title": t["title"], "ch": t.get("ch", ""), "voc": items,
                           "diff": sum(difficulty(v["w"]) for v in items) / len(items)})
    scenes.sort(key=lambda s: -s["diff"])          # 詞頻越高＝越簡單 → 先排簡單的
    print("場景 %d，由易到難排程" % len(scenes))

    start = datetime.date.today()
    db, shelves, need_tr = {}, ["多益場景"], []
    plan = []
    for di, sc in enumerate(scenes):
        date = (start + datetime.timedelta(days=di)).isoformat()
        short = re.sub(r"\s*\(.*", "", sc["title"]).strip()
        m = re.match(r"Chapter\s*0?(\d+)\s*(.*)", (sc["ch"] or "").replace("\u3000", " ").strip())
        chs = ("Ch%02d %s" % (int(m.group(1)), m.group(2).strip())) if m else "其他"
        chap = "多益場景 ▸ " + chs
        shelf = "%s ▸ %s %s" % (chap, sc["code"], short)
        if chap not in shelves: shelves.append(chap)
        shelves.append(shelf)
        own = bycode.get(sc["code"], [])
        words = {}
        for v in sc["voc"]:
            term = v["w"].strip()
            core = core_of(term)
            cw = content_words(core)
            rx0 = rx_for(core)
            need_all = len(cw)
            need_loose = max(2, len(cw) - 1) if len(cw) >= 3 else len(cw)
            sents = []
            def take(pool, test, cap):
                for e, z in pool:
                    if len(sents) >= cap: return
                    if any(s["ex"] == e for s in sents): continue
                    if test(e): sents.append({"ex": e, "exZh": z, "src": "user"})
            own_p  = own
            rest_p = [(e, z) for e, z, c in corpus if c != sc["code"]]
            if cw:
                take(own_p,  lambda e: rx0 and rx0.search(e), 2)                       # ① 本單元：完整片語
                take(own_p,  lambda e: cover(e, cw) >= need_all, 3)                    # ② 本單元：實詞全中
                take(rest_p, lambda e: rx0 and rx0.search(e), 3)                       # ③ 他單元：完整片語
                take(rest_p, lambda e: cover(e, cw) >= need_all, 3)                    # ④ 他單元：實詞全中
                if len(sents) < 3 and len(cw) >= 3:
                    take(own_p,  lambda e: cover(e, cw) >= need_loose, 3)              # ⑤ 放寬一個字
                    take(rest_p, lambda e: cover(e, cw) >= need_loose, 3)
            rx0 = rx_for(core)
            if len(sents) < 3 and own and rx0:                  # ③ 上下文句
                for i, (e, z) in enumerate(own):
                    if rx0.search(e):
                        for j in (i + 1, i - 1):
                            if 0 <= j < len(own) and not any(s["ex"] == own[j][0] for s in sents):
                                sents.append({"ex": own[j][0], "exZh": own[j][1], "src": "ctx"})
                                break
                        break
            if len(sents) < 3:                                  # ④ 自製例句
                g = make_template(term, v.get("pos", ""))
                if g and not any(s["ex"] == g for s in sents):
                    sents.append({"ex": g, "exZh": "", "src": "gen"}); need_tr.append(g)
            note = []
            if v.get("syn"):  note.append("同義代換　" + v["syn"])
            if v.get("tip"):  note.append("考點　" + v["tip"])
            if v.get("trap"): note.append("⚠ 防雷　" + v["trap"])
            note.append("出處　多益 %s %s" % (sc["code"], short))
            zh_word = (v.get("zh") or "").strip()
            if not zh_word:                                     # 來源沒中譯 → 用考點第一句或翻譯補上
                zh_word = re.split(r"[；;。\n]", (v.get("tip") or ""))[0][:28] or tr_many([term])[0]
            words[term.lower()] = {
                "word": term, "phonetic": "", "audio": "", "wordZh": zh_word,
                "pos": v.get("pos", ""), "meanings": [], "sentences": sents[:3],
                "note": "\n".join(note), "shelves": ["多益場景", chap, shelf],
                "stats": {"right": 0, "wrong": 0, "last": None},
                "level": level_of(term), "addedAt": int(time.time() * 1000)}
        db[date] = {"words": words}
        plan.append((date, sc["code"], short, len(words), round(sc["diff"], 2)))

    if need_tr:
        print("自製例句需翻譯 %d 句" % len(need_tr), flush=True)
        tr_many(need_tr)
        for d in db.values():
            for r in d["words"].values():
                for s in r["sentences"]:
                    if s["src"] == "gen" and not s["exZh"]: s["exZh"] = _TR.get(s["ex"], "")

    pack = {"v": 1, "name": "多益場景字庫", "db": db, "shelves": shelves,
            "plan": [{"date": d, "code": c, "title": t, "n": n} for d, c, t, n, _ in plan]}
    open(OUT, "w", encoding="utf-8").write("window.TOEIC_PACK=" + json.dumps(pack, ensure_ascii=False) + ";")

    tot = sum(len(d["words"]) for d in db.values())
    s3 = sum(1 for d in db.values() for r in d["words"].values() if len(r["sentences"]) >= 3)
    s0 = sum(1 for d in db.values() for r in d["words"].values() if not r["sentences"])
    lv = {}
    for d in db.values():
        for r in d["words"].values(): lv[r["level"]] = lv.get(r["level"], 0) + 1
    print("詞條 %d｜三句以上 %d (%.0f%%)｜完全沒例句 %d" % (tot, s3, 100 * s3 / tot, s0))
    print("熟悉度初值", lv, "｜檔案 %.0f KB" % (os.path.getsize(OUT) / 1024))
    print("前五天：", [(p[0], p[1], p[2][:18], p[3]) for p in plan[:5]])

if __name__ == "__main__":
    main()
