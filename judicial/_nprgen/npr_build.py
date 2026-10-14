# -*- coding: utf-8 -*-
"""
每日抓 NPR News 文章，做成 nida.html 的「NPR 新聞英語」科目（科目代碼 npr）。
版型與多益／英文商務合約相同：一句英文一句中文、核心字彙、速讀版（結構圖＋克漏字測驗＋念給你聽）。

產出：judicial/npr-data.js (window.NPR)、judicial/npr-sudu-data.js (window.NPR_SUDU)
用法：python3 npr_build.py [文章數，預設 4]
免費、免金鑰：Google gtx／clients5／MyMemory 三層翻譯備援，api.dictionaryapi.dev 查詞性與定義。
"""
import json, os, re, sys, html, time, random, datetime, socket, urllib.parse, urllib.request

socket.setdefaulttimeout(20)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # judicial/
RSS  = "https://feeds.npr.org/1001/rss.xml"                          # NPR News
KEEP_DAYS = 14                                                       # 保留最近幾天
MAX_PARAS = 18                                                       # 一篇最多讀幾段
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
      "Accept-Language": "en-US,en;q=0.9"}

# ── 基本工具 ────────────────────────────────────────────────────────────
def fetch(url, tries=3, timeout=30):
    last = None
    for i in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read().decode("utf-8", "replace")
        except Exception as e:
            last = e; time.sleep(1.5 * (i + 1))
    raise last

def strip_tags(x):
    x = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", x, flags=re.S | re.I)
    x = re.sub(r"<br\s*/?>", " ", x, flags=re.I)
    x = re.sub(r"<[^>]+>", "", x)
    return re.sub(r"\s+", " ", html.unescape(x)).strip()

# 機器翻譯常混入陸用語，換成台灣慣用
TW = [("報道","報導"),("網絡","網路"),("信息","資訊"),("軟件","軟體"),("硬件","硬體"),
      ("視頻","影片"),("互聯網","網際網路"),("數字化","數位化"),("打印","列印"),
      ("質量","品質"),("項目","專案"),("博客","部落格"),("服務器","伺服器"),
      ("奧巴馬","歐巴馬"),("特朗普","川普"),("悉尼","雪梨"),("新西蘭","紐西蘭"),
      ("通過","透過"),("渠道","管道"),("幹擾","干擾"),("乾擾","干擾"),("幹預","干預"),
      ("製程","製程"),("瀏覽器","瀏覽器"),("復蘇","復甦"),("藉口","藉口"),("覆蓋","覆蓋")]
def tw(s):
    for a, b in TW: s = s.replace(a, b)
    return s

_TRCACHE = {}

def _batch(texts):
    """一次送多句（clients5 的 dict-chrome-ex 端點支援多個 q，回傳對齊的陣列）。"""
    qs = "&".join("q=" + urllib.parse.quote(t) for t in texts)
    for base in ("https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=en&tl=zh-TW&",
                 "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-TW&dt=t&"):
        try:
            d = json.loads(fetch(base + qs, tries=2, timeout=25))
            if base.startswith("https://clients5"):
                out = d if isinstance(d, list) and all(isinstance(x, str) for x in d) else None
                if out is None and isinstance(d, list):            # 單句時會回巢狀
                    out = ["".join(x) if isinstance(x, list) else str(x) for x in d]
            else:
                grp = d[0] if isinstance(d, list) else []
                out = ["".join(x[0] for x in grp if x and x[0])] if len(texts) == 1 else None
            if out and len(out) == len(texts):
                return [tw(re.sub(r"\s+", " ", x).strip()) for x in out]
        except Exception:
            time.sleep(1.2)
    return None

def tr_many(texts):
    """批次翻譯；回傳與輸入等長的中文陣列（失敗處為空字串）。"""
    todo = [t for t in texts if t and t not in _TRCACHE]
    uniq, seen = [], set()
    for t in todo:
        if t not in seen: seen.add(t); uniq.append(t)
    i = 0
    while i < len(uniq):
        chunk, n = [], 0
        while i < len(uniq) and len(chunk) < 8 and n < 1600:
            chunk.append(uniq[i]); n += len(uniq[i]); i += 1
        got = _batch(chunk)
        if got is None and len(chunk) > 1:                         # 整批失敗 → 逐句重試
            got = []
            for c in chunk:
                one = _batch([c]); got.append(one[0] if one else ""); time.sleep(0.3)
        for c, g in zip(chunk, got or [""] * len(chunk)):
            _TRCACHE[c] = g or ""
        time.sleep(0.4)
    return [_TRCACHE.get(t, "") if t else "" for t in texts]

def translate(text):
    text = (text or "").strip()
    if not text: return ""
    if text not in _TRCACHE: tr_many([text])
    return _TRCACHE.get(text, "")

# ── 抓文章 ──────────────────────────────────────────────────────────────
JUNK = re.compile(
    r"(Sponsor Message|hide caption|toggle caption|Enlarge this image|"
    r"NPR does not offer or accept money|Copyright \d{4} NPR|"
    r"transcript of|^Loading\.\.\.$|Additional reporting by|subscribe to NPR|"
    r"newsletter|This story (?:was|originally)|was edited by|produced by NPR|"
    r"Correction:|Editor's note:)", re.I)
CAPTION = re.compile(r"^[A-Z][A-Z\s,\.\-']{4,40}\s[-–]\s[A-Z][a-z]+\s\d{1,2}")

def rss_items(limit):
    x = fetch(RSS)
    out = []
    for blk in re.findall(r"<item>(.*?)</item>", x, re.S):
        def g(tag):
            m = re.search(r"<%s>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</%s>" % (tag, tag), blk, re.S)
            return html.unescape(m.group(1).strip()) if m else ""
        link = g("link")
        if not link or "/podcasts/" in link or "/player/" in link: continue
        out.append({"title": strip_tags(g("title")), "link": link,
                    "desc": strip_tags(g("description")), "pub": g("pubDate")})
        if len(out) >= limit * 3: break
    return out

def article(url):
    h = fetch(url)
    i = h.find('id="storytext"')
    if i < 0: return None
    seg = h[i:]
    end = min([p for p in [seg.find("<footer"), seg.find('class="story-bottom'), 60000] if p > 0] or [60000])
    seg = seg[:end]
    seg = re.sub(r'<div[^>]*class="[^"]*bucketwrap (?:image|audio|video|internallink)[^"]*".*?</div>\s*</div>', " ", seg, flags=re.S)
    paras = []
    for p in re.findall(r"<p[^>]*>(.*?)</p>", seg, re.S):
        c = strip_tags(p)
        if len(c) < 45 or JUNK.search(c) or CAPTION.match(c): continue
        if c.lower().startswith(("npr's", "listen to")) and len(c) < 120: continue
        paras.append(c)
    truncated = len(paras) > MAX_PARAS
    paras = paras[:MAX_PARAS]
    # 作者與章節
    by = re.findall(r'class="byline__name[^"]*"[^>]*>\s*(?:<a[^>]*>)?([^<]{2,60})', h)
    by = [b.strip() for b in by if b.strip() and b.strip() not in (",", "By")]
    kick = re.search(r'<[^>]+class="slug[^"]*"[^>]*>\s*(?:<a[^>]*>)?\s*([^<]{2,40})', h)
    return {"paras": paras, "by": by[:3], "trunc": truncated,
            "sec": (kick.group(1).strip() if kick else "NPR News")}

# ── 斷句 ────────────────────────────────────────────────────────────────
ABBR = r"(?<!\bMr)(?<!\bMrs)(?<!\bMs)(?<!\bDr)(?<!\bSt)(?<!\bU\.S)(?<!\bJr)(?<!\bSr)(?<!\bvs)(?<!\bInc)(?<!\bNo)"
def sentences(p):
    out, buf = [], ""
    for part in re.split(r'(?<=[.!?])(?<!\b[A-Z]\.)\s+(?=[A-Z"\'(])', p):
        part = part.strip()
        if not part: continue
        if len(part) < 25 and buf:
            buf += " " + part
        else:
            if buf: out.append(buf)
            buf = part
    if buf: out.append(buf)
    return [s for s in out if len(s) > 15]

# ── 單字 ────────────────────────────────────────────────────────────────
try:
    from wordfreq import zipf_frequency
except Exception:
    zipf_frequency = None

STOP = set("""about above after again against because before being below between both during
each further having into itself more most other over same should their there these those through
under until very were what when where which while would your could their said says also been
first second third among around another nearly already though since however whether rather
across within toward against including according""".split())

_DICT_FAILS = [0]        # dictionaryapi.dev 常掛掉 → 連錯兩次就整輪跳過
def gdict(word):
    """Google 翻譯的字典資料：回傳 (主要中譯, 詞性, 其他中文意思)。"""
    u = ("https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=zh-TW"
         "&dt=t&dt=bd&dj=1&q=" + urllib.parse.quote(word))
    try:
        d = json.loads(fetch(u, tries=2, timeout=20))
        main = tw("".join(x.get("trans", "") for x in d.get("sentences", [])).strip())
        ent = d.get("dict") or []
        pos = ent[0].get("pos", "") if ent else ""
        terms = []
        for e in ent[:2]:
            for t in e.get("terms", [])[:4]:
                t = tw(t)
                if t and t != main and t not in terms: terms.append(t)
        time.sleep(0.25)
        return main, pos, "、".join(terms[:4])
    except Exception:
        return "", "", ""

def pos_zh(word):
    """備援：dictionaryapi.dev 取英文定義與同義字。"""
    if _DICT_FAILS[0] >= 2: return "", "", ""
    try:
        d = json.loads(fetch("https://api.dictionaryapi.dev/api/v2/entries/en/" + urllib.parse.quote(word), tries=1, timeout=8))
        m = d[0]["meanings"][0]
        defi = m["definitions"][0]["definition"]
        syn = m.get("synonyms", []) or m["definitions"][0].get("synonyms", [])
        _DICT_FAILS[0] = 0
        return m["partOfSpeech"], defi, ", ".join(syn[:3])
    except Exception:
        _DICT_FAILS[0] += 1
        return "", "", ""

POSZH = {"noun":"n.","verb":"v.","adjective":"adj.","adverb":"adv.","preposition":"prep.",
         "conjunction":"conj.","pronoun":"pron.","interjection":"int."}

def _z(w):
    return zipf_frequency(w, "en") if zipf_frequency else 3.0

def lemma(w):
    """粗略還原字根：複數、第三人稱、過去式、現在分詞 → 取詞頻最高的合理形式。"""
    c = [w]
    if w.endswith("ies") and len(w) > 5: c.append(w[:-3] + "y")
    if w.endswith("es")  and len(w) > 4: c.append(w[:-2])
    if w.endswith("s")   and not w.endswith("ss"): c.append(w[:-1])
    if w.endswith("ed")  and len(w) > 4:
        c += [w[:-2], w[:-1]]
        if len(w) > 5 and w[-3] == w[-4]: c.append(w[:-3])
        if w.endswith("ied"): c.append(w[:-3] + "y")
    if w.endswith("ing") and len(w) > 5:
        c += [w[:-3], w[:-3] + "e"]
        if len(w) > 6 and w[-4] == w[-5]: c.append(w[:-4])
    c = [x for x in dict.fromkeys(c) if len(x) >= 4]
    best = max(c, key=_z)
    return best if _z(best) >= _z(w) else w

def pick_words(paras, want=12):
    freq, capped, surface = {}, {}, {}
    for p in paras:
        for m in re.finditer(r"[A-Za-z][A-Za-z\-']{4,}", p):
            w = m.group(0); lw = w.lower().strip("-'")
            if lw in STOP or len(lw) < 5: continue
            base = lemma(lw)
            if base in STOP or len(base) < 5: continue
            freq[base] = freq.get(base, 0) + 1
            surface.setdefault(base, w)
            if w[0].isupper(): capped[base] = capped.get(base, 0) + 1
    cand = []
    for w, n in freq.items():
        cap = capped.get(w, 0)
        if cap * 2 >= n or (cap and n <= 2): continue       # 多數大寫、或出現少又大寫 → 人名地名
        z = _z(w)
        if 2.5 <= z <= 4.3:                                 # 太常見沒必要學，太罕用（含人名 0.0）也不值得
            cand.append((z, -n, w))
    cand.sort()
    return [(w, surface[w]) for _, _, w in cand[:want]]

def build_voc(pairs, paras):
    voc = []
    for w, sf in pairs:
        zh, pos, others = gdict(w)
        if not zh: continue
        epos, defi, syn = pos_zh(w)                          # 備援：英英定義與同義字
        ex, stem = "", re.escape(w[:max(4, len(w) - 2)])
        for lo, hi in ((30, 230), (20, 320)):
            for p in paras:
                for m in re.finditer(r"[^.]*\b%s\w*\b[^.]*\." % stem, p, re.I):
                    g = m.group(0).strip()
                    if lo < len(g) < hi: ex = g; break
                if ex: break
            if ex: break
        tip = []
        if others: tip.append("其他意思　" + others)
        if defi:   tip.append("英英定義　" + defi)
        if ex:
            tip.append("本文例句　" + ex)
            ez = translate(ex)
            if ez: tip.append("例句中譯　" + ez)
        voc.append({"w": w, "sf": sf, "pos": POSZH.get(pos or epos, pos or epos or ""), "zh": zh,
                    "syn": syn, "tip": "　|　".join(tip), "trap": ""})
    return voc

# ── 組裝一篇文章 ────────────────────────────────────────────────────────
def make_topic(code, day_ch, meta, art, idx):
    paras, title, link = art["paras"], meta["title"], meta["link"]
    tr_many([title] + ([meta["desc"]] if meta.get("desc") else []))
    zh_title = translate(title)
    items = []
    lead = ("今日 NPR 新聞英語。本篇出自 NPR News，"
            + ("作者 " + "、".join(art["by"]) + "，" if art["by"] else "")
            + "全文共 %d 段、%d 句。畫面預設只顯示英文原句，點任一句展開中譯；"
            "右上角「🔍 全面解析」可一次展開全部中譯與字彙；「🌲 速讀」是文章結構圖＋單字克漏字測驗。"
            % (len(paras), sum(len(sentences(p)) for p in paras)))
    if meta.get("desc"): lead += "　本篇摘要：" + (translate(meta["desc"]) or meta["desc"])
    items.append({"k": "lead", "t": lead})
    items.append({"k": "src", "t": "📎 NPR 原文連結（點擊開新分頁）", "u": link})
    if art.get("trunc"):
        items.append({"k": "tip", "t": "本篇較長，站上只收前 %d 段；想讀完整篇請點上方的 NPR 原文連結。" % MAX_PARAS})

    items.append({"k": "h1", "t": "📰 原文逐句 Full Text", "ic": "📰"})
    tr_many([title] + ([meta["desc"]] if meta.get("desc") else []) + paras +
            [x for p in paras for x in sentences(p)])      # 一次批次翻完，後面全部走快取
    all_zh = []
    for pi, p in enumerate(paras, 1):
        p_zh = translate(p)
        all_zh.append(p_zh or "")
        items.append({"k": "h2", "t": "第 %d 段" % pi,
                      "d": (p_zh[:34] + "…") if len(p_zh) > 34 else p_zh, "ic": "¶"})
        for si, s in enumerate(sentences(p)):
            it = {"k": "en", "sp": ("¶%d" % pi) if si == 0 else "", "t": s, "zh": translate(s) or ""}
            if si: it["cn"] = 1
            items.append(it)

    if any(all_zh):
        items.append({"k": "h1", "t": "📖 全文中譯", "ic": "📖"})
        items.append({"k": "zhblk", "t": "　".join(x for x in all_zh if x)})

    pairs = pick_words(paras)
    tr_many([w for w, _ in pairs])
    voc = build_voc(pairs, paras)
    if voc:
        items.append({"k": "h1", "t": "📝 本篇核心字彙", "ic": "📝"})
        items.append({"k": "tip", "t": "依 wordfreq 詞頻自動挑出本篇最值得學的生字（越罕用越前面）。"
                                       "點單字左邊的 ☆ 可標記，標完用標題列的「⭐ 只念星號」反覆聽。"})
        items.append({"k": "voc", "v": voc})
    return {"code": code, "ch": day_ch, "sec": art["sec"] or "NPR News",
            "title": title + ("　／　" + zh_title if zh_title else ""), "items": items}, voc, paras

def make_sudu(topic, voc, paras):
    title = topic["title"].split("　／　")[0]
    tree = ["【%s・文章結構】" % (topic["title"].split("　／　")[-1][:28] or title[:28])]
    for pi, p in enumerate(paras, 1):
        z = translate(p)
        tree.append(("├ ¶%d　" % pi) + ((z[:40] + "…") if len(z) > 40 else (z or p[:60])))
    if len(tree) > 1: tree[-1] = "└" + tree[-1][1:]
    tree.append("")
    tree.append("【本篇關鍵字】" + "、".join("%s（%s）" % (v["w"], v["zh"]) for v in voc[:10]))

    # 單字克漏字測驗
    quiz, pool = [], [v.get("sf") or v["w"] for v in voc]
    for v in voc:
        if len(quiz) >= 6: break
        sf = v.get("sf") or v["w"]
        sent = ""
        for p in paras:
            m = re.search(r"[^.]*\b%s\b[^.]*\." % re.escape(sf), p, re.I)
            if m and 40 < len(m.group(0)) < 230: sent = m.group(0).strip(); break
        if not sent: continue
        blanked = re.sub(r"\b%s\b" % re.escape(sf), "______", sent, count=1, flags=re.I)
        wrong = [w for w in pool if w != sf]
        random.shuffle(wrong)
        opts = [sf] + wrong[:3]
        if len(opts) < 4: continue
        random.shuffle(opts)
        letters = ["A", "B", "C", "D"]
        ans = letters[opts.index(sf)]
        quiz.append({"q": "Fill in the blank:　" + blanked,
                     "o": [[letters[i], opts[i]] for i in range(4)],
                     "a": "(%s) %s" % (ans, sf),
                     "zh": translate(sent) or "",
                     "e": "%s　%s%s" % (v["w"], (v["pos"] + "　") if v["pos"] else "", v["zh"])
                          + (("　|　同義代換 " + v["syn"]) if v["syn"] else "")})

    say = ["今天的 NPR 新聞英語。標題是：" + title + "。"]
    if "　／　" in topic["title"]: say.append("中文標題：" + topic["title"].split("　／　")[1] + "。")
    for pi, p in enumerate(paras[:6], 1):
        z = translate(p)
        if z: say.append("第 %d 段。%s" % (pi, z))
    if voc:
        say.append("本篇關鍵字：" + "、".join("%s，%s" % (v["w"], v["zh"]) for v in voc[:8]) + "。")
    return {"tree": "\n".join(tree), "quiz": quiz, "say": say}

# ── 主程式 ──────────────────────────────────────────────────────────────
def load(fn, var):
    p = os.path.join(ROOT, fn)
    if not os.path.exists(p): return None
    m = re.search(r"window\." + var + r"=(.*);$", open(p, encoding="utf-8").read(), re.S)
    return json.loads(m.group(1)) if m else None

def main():
    want = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
    wk = "一二三四五六日"[today.weekday()]
    day_ch = "%s　週%s" % (today.strftime("%Y-%m-%d"), wk)

    old_data = load("npr-data.js", "NPR") or []
    old_sudu = load("npr-sudu-data.js", "NPR_SUDU") or {}
    have_links = {it.get("_u") for it in old_data}

    picked, new_topics, new_sudu = 0, [], {}
    for meta in rss_items(want):
        if picked >= want: break
        if meta["link"] in have_links: continue
        try:
            art = article(meta["link"])
        except Exception as e:
            print("  ! 抓不到", meta["link"], e); continue
        if not art or len(art["paras"]) < 3:
            print("  - 跳過（內容太短）", meta["title"][:50]); continue
        picked += 1
        code = "%s-%d" % (today.strftime("%Y%m%d"), picked)
        print("  ✓ [%s] %s" % (code, meta["title"][:60]))
        t, voc, paras = make_topic(code, day_ch, meta, art, picked)
        t["_u"] = meta["link"]
        new_topics.append(t)
        new_sudu[code] = make_sudu(t, voc, paras)

    if not new_topics:
        print("今天沒有新文章，資料未變更。"); return

    data = new_topics + [t for t in old_data if t.get("ch") != day_ch or t.get("_u") not in {x["_u"] for x in new_topics}]
    # 只留最近 KEEP_DAYS 天
    keep_days = sorted({t["ch"] for t in data}, reverse=True)[:KEEP_DAYS]
    data = [t for t in data if t["ch"] in keep_days]
    sudu = {}
    for t in data:
        sudu[t["code"]] = new_sudu.get(t["code"]) or old_sudu.get(t["code"]) or {"tree": "", "quiz": [], "say": []}

    open(os.path.join(ROOT, "npr-data.js"), "w", encoding="utf-8").write(
        "window.NPR=" + json.dumps(data, ensure_ascii=False) + ";")
    open(os.path.join(ROOT, "npr-sudu-data.js"), "w", encoding="utf-8").write(
        "window.NPR_SUDU=" + json.dumps(sudu, ensure_ascii=False) + ";")

    # 更新 nida.html 的快取版本戳與資料日期
    nh = os.path.join(ROOT, "nida.html")
    s = open(nh, encoding="utf-8").read()
    s = re.sub(r"\?v=\d{12}", "?v=" + today.strftime("%Y%m%d%H%M"), s)
    s = re.sub(r"資料 \d{8}-\d{4}", "資料 " + today.strftime("%Y%m%d-%H%M"), s)
    open(nh, "w", encoding="utf-8").write(s)
    print("完成：新增 %d 篇，站上共 %d 篇（%d 天）" % (len(new_topics), len(data), len(keep_days)))

if __name__ == "__main__":
    main()
