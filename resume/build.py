#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
國際化履歷 / 作品集產生器（中英雙語 · 案例研究格式）
用法： python3 build.py
讀 resume.json → 產出：
  index.html                      對外 SEO 履歷網站（含 EN/中文 切換）
  exports/104.txt, 1111.txt       台灣人力銀行文案（中）
  exports/linkedin_en.txt         LinkedIn About（英）
  exports/linkedin_zh.txt         LinkedIn About（中）
  exports/headline.txt            LinkedIn / 104 標題（中英）
"""
import json, os, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))

def load():
    with open(os.path.join(HERE, "resume.json"), encoding="utf-8") as f:
        return json.load(f)

def is_todo(v):
    return isinstance(v, str) and v.strip().upper().startswith("TODO")

def e(s):
    return html.escape(str(s or ""))

def L(v, lang):
    """取雙語欄位；v 可能是 {en,zh} 或純字串。"""
    if isinstance(v, dict):
        return v.get(lang) or v.get("en") or v.get("zh") or ""
    return v or ""

def clean_list(items, textkeys):
    out = []
    for it in items or []:
        vals = []
        for k in textkeys:
            val = it.get(k, "")
            vals.append(L(val, "en") if isinstance(val, dict) else val)
        if any(v and not is_todo(v) for v in vals):
            out.append(it)
    return out

# ---------------------------------------------------------------- 網站
def span2(v):
    """輸出同時含中英兩份文字的元素，靠 body class 切換顯示。"""
    return f'<span class="en">{e(L(v,"en"))}</span><span class="zh">{e(L(v,"zh"))}</span>'

def span2br(v):
    """同 span2，但保留換行（\\n → <br>），給 About 這種多段文字用。"""
    en = e(L(v, "en")).replace("\n", "<br>")
    zh = e(L(v, "zh")).replace("\n", "<br>")
    return f'<span class="en">{en}</span><span class="zh">{zh}</span>'

def build_html(d):
    p = d["profile"]
    today = datetime.date.today().isoformat()

    contacts = []
    if p.get("email"): contacts.append(f'<a href="mailto:{e(p["email"])}">✉️ {e(p["email"])}</a>')
    if p.get("phone") and not is_todo(p["phone"]): contacts.append(f'<span>📞 {e(p["phone"])}</span>')
    if p.get("github"): contacts.append(f'<a href="{e(p["github"])}" target="_blank">💻 GitHub</a>')
    if p.get("linkedin") and not is_todo(p["linkedin"]): contacts.append(f'<a href="{e(p["linkedin"])}" target="_blank">🔗 LinkedIn</a>')
    if p.get("website"): contacts.append(f'<a href="{e(p["website"])}" target="_blank"><span class="en">🌐 All projects</span><span class="zh">🌐 作品總站</span></a>')
    contacts_html = " · ".join(contacts)

    roles_en = "".join(f'<span class="tag">{e(r)}</span>' for r in p.get("target_roles", {}).get("en", []))
    roles_zh = "".join(f'<span class="tag">{e(r)}</span>' for r in p.get("target_roles", {}).get("zh", []))
    roles_html = f'<span class="en">{roles_en}</span><span class="zh">{roles_zh}</span>'

    skills_html = ""
    for grp in d.get("skills", []):
        chips = "".join(f'<span class="chip">{e(i)}</span>' for i in grp.get("items", []))
        skills_html += f'<div class="skgroup"><h4>{span2(grp["cat"])}</h4><div class="chips">{chips}</div></div>'

    proj_html = ""
    for pr in d.get("projects", []):
        metrics = "".join(f'<span class="metric">{span2(m)}</span>' for m in pr.get("metrics", []))
        stack = "".join(f'<span class="tag">{e(t)}</span>' for t in pr.get("stack", []))
        usage = f'<div class="usage">📈 {e(pr["usage"])}</div>' if pr.get("usage") else ''
        proj_html += f'''
      <a class="proj" href="{e(pr.get("url","#"))}" target="_blank">
        <div class="proj-ti">{span2(pr.get("name",""))}</div>
        <div class="proj-role">{span2(pr.get("role",""))}</div>
        <div class="metrics">{metrics}</div>
        <div class="cs"><b class="lbl"><span class="en">Problem</span><span class="zh">問題</span></b> {span2(pr.get("problem",""))}</div>
        <div class="cs"><b class="lbl"><span class="en">Approach</span><span class="zh">做法</span></b> {span2(pr.get("approach",""))}</div>
        <div class="cs"><b class="lbl"><span class="en">Impact</span><span class="zh">影響</span></b> {span2(pr.get("impact",""))}</div>
        {usage}
        <div class="tags">{stack}</div>
      </a>'''

    exp = clean_list(d.get("experience"), ["role", "desc"])
    exp_html = ""
    if exp:
        rows = ""
        for x in exp:
            rows += f'''<div class="row"><div class="rh"><b>{span2(x.get("role",""))}</b> · {e(x.get("org",""))}<span class="period">{e(x.get("period",""))}</span></div><div class="rd">{span2(x.get("desc",""))}</div></div>'''
        exp_html = f'<section><h2><span class="en">Experience</span><span class="zh">經歷</span></h2>{rows}</section>'

    edu = clean_list(d.get("education"), ["degree"])
    edu_html = ""
    if edu:
        rows = ""
        for x in edu:
            rows += f'''<div class="row"><div class="rh"><b>{e(x.get("school",""))}</b> · {span2(x.get("degree",""))}<span class="period">{e(x.get("period",""))}</span></div></div>'''
        edu_html = f'<section><h2><span class="en">Education</span><span class="zh">學歷</span></h2>{rows}</section>'

    same_as = [u for u in [p.get("github"), p.get("linkedin"), p.get("website")] if u and not is_todo(u)]
    jsonld = {
        "@context": "https://schema.org", "@type": "Person",
        "name": p.get("name"), "jobTitle": L(p.get("title"), "en"),
        "email": f'mailto:{p.get("email")}' if p.get("email") else None,
        "url": p.get("website"), "sameAs": same_as, "address": p.get("location"),
        "description": L(d.get("summary"), "en"),
        "knowsAbout": [i for g in d.get("skills", []) for i in g.get("items", [])],
    }
    jsonld = {k: v for k, v in jsonld.items() if v}

    desc_meta = e(L(d.get("summary"), "en")[:155])
    open_badge = '<span class="oa"><span class="en">🟢 Open to opportunities</span><span class="zh">🟢 開放工作機會</span></span>' if p.get("open_to_work") else ''
    photo_html = f'<img class="avatar" src="{e(p["photo"])}" alt="{e(p.get("name",""))}">' if p.get("photo") else ''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(p.get("name",""))} — {e(L(p.get("title"),"en"))}</title>
<meta name="description" content="{desc_meta}">
<meta name="author" content="{e(p.get("name",""))}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="profile">
<meta property="og:title" content="{e(p.get("name",""))} — {e(L(p.get("title"),"en"))}">
<meta property="og:description" content="{desc_meta}">
<meta property="og:url" content="{e(p.get("website",""))}resume/">
<meta property="og:image" content="{e(p.get("website",""))}resume/img/cover.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{e(p.get("website",""))}resume/img/cover.png">
<link rel="canonical" href="{e(p.get("website",""))}resume/">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:"Inter","PingFang TC","Microsoft JhengHei",system-ui,sans-serif;
       background:linear-gradient(160deg,#14161c,#26262f);color:#e8e6e0;line-height:1.7;padding:0 20px 60px}}
  /* 語言切換：預設顯示英文 */
  .zh{{display:none}} body.lang-zh .zh{{display:inline}} body.lang-zh .en{{display:none}}
  .wrap{{max-width:880px;margin:0 auto}}
  .langbar{{position:sticky;top:0;padding:12px 0;text-align:right;z-index:10}}
  .langbar button{{background:#20262f;color:#cfd6e2;border:1px solid #33405255;border-radius:8px;
       padding:6px 14px;font-size:13px;font-weight:600;cursor:pointer;margin-left:6px}}
  .langbar button.on{{background:#1f3a56;color:#7fb5ff;border-color:#2b5680}}
  header{{padding:28px 0 32px;text-align:center}}
  .avatar{{width:150px;height:150px;border-radius:50%;object-fit:cover;object-position:center top;
       border:3px solid #7fb5ff;box-shadow:0 6px 20px rgba(0,0,0,.35);margin-bottom:18px}}
  .oa{{display:inline-block;font-size:13px;color:#8ff0b0;border:1px solid #2f6b47;background:#122a1c;border-radius:20px;padding:4px 14px;margin-bottom:16px}}
  h1{{font-size:42px;letter-spacing:1px}}
  .role{{color:#7fb5ff;font-size:19px;font-weight:600;margin:8px 0}}
  .tagline{{color:#b9b3a3;font-size:16px;max-width:640px;margin:10px auto 0}}
  .loc{{color:#8a8576;font-size:13px;margin-top:8px}}
  .contacts{{margin-top:20px;font-size:14px}}
  .contacts a,.contacts span{{color:#cfd6e2;text-decoration:none;margin:0 4px}}
  .contacts a:hover{{color:#7fb5ff}}
  .targets{{margin-top:16px;display:flex;gap:8px;flex-wrap:wrap;justify-content:center}}
  section{{margin-top:42px}}
  h2{{font-size:22px;color:#f0d68a;border-left:4px solid #d6a32e;padding-left:12px;margin-bottom:18px}}
  .summary{{font-size:16px;color:#d8d4ca}}
  .tag{{font-size:12px;color:#cbd5e1;background:#20263180;border:1px solid #33405233;border-radius:16px;padding:3px 11px}}
  .chip{{font-size:13px;color:#e8e6e0;background:#2a2f3a;border-radius:8px;padding:5px 11px;display:inline-block}}
  .chips{{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}}
  .skgroup{{margin-bottom:16px}} .skgroup h4{{color:#9aa4b2;font-size:14px}}
  .projects{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}}
  a.proj{{display:block;background:#fffdf7;color:#26262b;text-decoration:none;border-radius:16px;padding:22px;
         box-shadow:0 8px 22px rgba(0,0,0,.3);transition:.18s}}
  a.proj:hover{{transform:translateY(-4px);box-shadow:0 14px 30px rgba(0,0,0,.45)}}
  .proj-ti{{font-size:19px;font-weight:bold}}
  .proj-role{{font-size:12px;color:#999;margin-bottom:10px}}
  .metrics{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:12px}}
  .metric{{font-size:12px;font-weight:700;color:#b06a1f;background:#f6ead2;border-radius:6px;padding:3px 9px}}
  .cs{{font-size:13.5px;color:#444;margin-bottom:7px}}
  .cs .lbl{{color:#b06a1f;font-size:11px;text-transform:uppercase;letter-spacing:.5px}}
  .usage{{font-size:13px;color:#1f7a4d;font-weight:600;margin-top:6px}}
  .proj .tags{{margin-top:12px;display:flex;gap:6px;flex-wrap:wrap}}
  .proj .tag{{color:#555;background:#f0ece0;border:none}}
  .row{{margin-bottom:16px}} .rh{{font-size:16px}} .period{{color:#8a8576;font-size:13px;margin-left:10px}}
  .rd{{color:#b9b3a3;font-size:14px;margin-top:4px}}
  footer{{margin-top:56px;text-align:center;color:#8a8576;font-size:13px}}
  footer a{{color:#8a8576}}
  @media(max-width:600px){{h1{{font-size:32px}}}}
</style>
</head>
<body class="lang-en">
<div class="wrap">
  <div class="langbar">
    <button id="b-en" class="on" onclick="setLang('en')">EN</button>
    <button id="b-zh" onclick="setLang('zh')">中文</button>
  </div>
  <header>
    {photo_html}
    <div>{open_badge}</div>
    <h1>{e(p.get("name",""))}</h1>
    <div class="role">{span2(p.get("title",""))}</div>
    <div class="tagline">{span2(p.get("tagline",""))}</div>
    <div class="loc">📍 {e(p.get("location",""))}</div>
    <div class="contacts">{contacts_html}</div>
    <div class="targets">{roles_html}</div>
  </header>

  <section><h2><span class="en">About</span><span class="zh">關於我</span></h2><p class="summary">{span2br(d.get("summary",""))}</p></section>

  <section><h2><span class="en">Core Skills</span><span class="zh">核心技能</span></h2>{skills_html}</section>

  <section><h2><span class="en">Selected Work</span><span class="zh">精選作品</span></h2><div class="projects">{proj_html}</div></section>

  {exp_html}
  {edu_html}

  <footer>
    <span class="en">Last updated: {today} · auto-generated from resume.json</span>
    <span class="zh">最近更新：{today} · 由 resume.json 自動生成</span><br>
    © 2026 姬政妤 Elaine Chi · 保留所有權利 All Rights Reserved<br>
    <a href="../">← <span class="en">All projects</span><span class="zh">回作品總站</span></a>
  </footer>
</div>
<!-- GoatCounter 流量分析 -->
<script data-goatcounter="https://elainechi.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<script>
function setLang(l){{
  document.body.className='lang-'+l;
  document.getElementById('b-en').classList.toggle('on',l==='en');
  document.getElementById('b-zh').classList.toggle('on',l==='zh');
  document.documentElement.lang = (l==='zh'?'zh-TW':'en');
  try{{localStorage.setItem('resumeLang',l)}}catch(e){{}}
}}
try{{var s=localStorage.getItem('resumeLang');if(s)setLang(s);}}catch(e){{}}
</script>
</body>
</html>'''

# ---------------------------------------------------------------- 文字文案
def build_text(d, platform, lang):
    p = d["profile"]
    o = []
    o.append(f"{p.get('name','')} — {L(p.get('title'),lang)}")
    o.append(L(p.get("tagline"), lang))
    o.append(f"📍 {p.get('location','')}")
    o.append("")
    o.append("About" if lang=="en" else "■ 關於我")
    o.append(L(d.get("summary"), lang))
    o.append("")
    o.append("Core Skills" if lang=="en" else "■ 核心技能")
    for g in d.get("skills", []):
        o.append(f"  {L(g['cat'],lang)}: {', '.join(g.get('items',[]))}")
    o.append("")
    o.append("Selected Work" if lang=="en" else "■ 精選作品")
    for pr in d.get("projects", []):
        ms = " · ".join(L(m,lang) for m in pr.get("metrics", []))
        o.append(f"• {L(pr.get('name'),lang)}  [{ms}]")
        o.append(f"  {'Problem' if lang=='en' else '問題'}: {L(pr.get('problem'),lang)}")
        o.append(f"  {'Approach' if lang=='en' else '做法'}: {L(pr.get('approach'),lang)}")
        o.append(f"  {'Impact' if lang=='en' else '影響'}: {L(pr.get('impact'),lang)}")
        o.append(f"  {pr.get('url','')}")
    exp = clean_list(d.get("experience"), ["role","desc"])
    if exp:
        o.append("")
        o.append("Experience" if lang=="en" else "■ 經歷")
        for x in exp:
            o.append(f"• {L(x.get('role'),lang)} · {x.get('org','')} ({x.get('period','')})")
            if L(x.get('desc'),lang): o.append(f"  {L(x.get('desc'),lang)}")
    edu = clean_list(d.get("education"), ["degree"])
    if edu:
        o.append("")
        o.append("Education" if lang=="en" else "■ 學歷")
        for x in edu:
            o.append(f"• {x.get('school','')} {L(x.get('degree'),lang)} ({x.get('period','')})")
    o.append("")
    o.append("Contact" if lang=="en" else "■ 聯絡")
    o.append(f"  {p.get('website','')}")
    o.append(f"  {p.get('email','')}")
    if p.get("linkedin") and not is_todo(p["linkedin"]):
        o.append(f"  {p['linkedin']}")

    hdr = {
        ("104","zh"): "（貼到 104 自傳欄；標題見 headline.txt，專長在 104『專長』另外勾選）",
        ("1111","zh"): "（貼到 1111 自傳／專長欄）",
        ("linkedin","en"): "(LinkedIn About — put headline.txt line 1 in your Headline, this text in About)",
        ("linkedin","zh"): "（LinkedIn About 中文版）",
    }.get((platform,lang), "")
    if hdr:
        o.insert(0, hdr); o.insert(1, "")
    return "\n".join(o)

def build_headline(d):
    p = d["profile"]
    return ("LinkedIn / 104 標題（複製其一，前 80 字最關鍵，勿寫 open to work）\n\n"
            f"[EN] {L(p.get('headline'),'en')}\n\n"
            f"[中] {L(p.get('headline'),'zh')}\n")

def main():
    d = load()
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_html(d))
    expdir = os.path.join(HERE, "exports"); os.makedirs(expdir, exist_ok=True)
    outputs = {
        "104.txt": build_text(d, "104", "zh"),
        "1111.txt": build_text(d, "1111", "zh"),
        "linkedin_en.txt": build_text(d, "linkedin", "en"),
        "linkedin_zh.txt": build_text(d, "linkedin", "zh"),
        "headline.txt": build_headline(d),
    }
    for fn, txt in outputs.items():
        with open(os.path.join(expdir, fn), "w", encoding="utf-8") as f:
            f.write(txt)
    print("✅ 已生成：")
    print("   resume/index.html（中英雙語履歷網站）")
    for fn in outputs: print(f"   resume/exports/{fn}")
    # TODO 提醒
    todos = []
    if is_todo(d["profile"].get("linkedin","")): todos.append("profile.linkedin")
    if all(not pr.get("usage") for pr in d.get("projects", [])):
        todos.append("每個作品的真實使用數據 usage（裝流量分析後填）")
    if todos:
        print("\n⚠️  建議補：", "、".join(todos))

if __name__ == "__main__":
    main()
