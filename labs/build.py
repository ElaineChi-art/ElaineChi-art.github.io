#!/usr/bin/env python3
"""
技能實驗室 (Skill Lab) 靜態頁面產生器
單一資料來源：data/topics.json
用法：python3 build.py  →  產出 index.html 與 category/*.html

之後要把某個主題標記為「已上線」，只要在 topics.json 該主題物件加：
  "status": "live", "url": "https://...", "tagline": "一句話說明這個專案做了什麼"
再重跑一次 build.py 即可（跟 resume/build.py 的 resume.json 是同一套習慣）。
"""
import json
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
DATA = json.loads((ROOT / "data" / "topics.json").read_text(encoding="utf-8"))
SITE = DATA["site"]
CATEGORIES = DATA["categories"]

GOATCOUNTER = '<script data-goatcounter="https://elainechi.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'


def slugify(title: str) -> str:
    s = re.sub(r"[^\w一-鿿]+", "-", title.strip().lower())
    return s.strip("-")


BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Inter","PingFang TC","Microsoft JhengHei",system-ui,sans-serif;
     background:linear-gradient(160deg,#14161c,#26262f);color:#e8e6e0;line-height:1.7;min-height:100vh}
a{color:inherit}
.topnav{display:flex;gap:6px;background:#0b0d12;padding:10px 20px;border-bottom:1px solid #262b36;
        position:sticky;top:0;z-index:50;overflow-x:auto}
.topnav a{color:#9aa4b2;text-decoration:none;font-size:14px;font-weight:600;padding:7px 16px;border-radius:8px;white-space:nowrap}
.topnav a:hover{background:#161922;color:#e6e6e6}
.topnav a.active{background:#1f2e3a;color:#7fb5ff}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px 60px}
"""

HOME_EXTRA_CSS = """
header{padding:44px 0 30px;text-align:center}
h1{font-size:36px;letter-spacing:1px}
.tagline{color:#b9b3a3;font-size:16px;max-width:640px;margin:12px auto 0}
.stats{display:inline-flex;gap:10px;margin-top:20px;align-items:center;font-size:14px;color:#f0d68a;
       background:#20263180;border:1px solid #33405255;border-radius:20px;padding:7px 18px}
.bar{width:140px;height:8px;background:#2a2f3a;border-radius:6px;overflow:hidden}
.bar-fill{height:100%;background:linear-gradient(90deg,#7fb5ff,#f0d68a)}
.cats{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:22px;margin-top:38px}
a.catcard{display:block;background:#fffdf7;color:#26262b;text-decoration:none;border-radius:20px;
          padding:26px 24px;box-shadow:0 10px 26px rgba(0,0,0,.25);transition:.18s;border-top:6px solid var(--c)}
a.catcard:hover{transform:translateY(-5px);box-shadow:0 16px 34px rgba(0,0,0,.35)}
.catcard .ic{font-size:40px;margin-bottom:10px}
.catcard .ti{font-size:20px;font-weight:bold;margin-bottom:6px}
.catcard .su{font-size:13.5px;color:#666;line-height:1.6;margin-bottom:14px}
.catcard .prog{font-size:12.5px;color:#888;display:flex;align-items:center;gap:8px}
.catcard .pbar{flex:1;height:6px;background:#eee5d0;border-radius:4px;overflow:hidden}
.catcard .pbar-fill{height:100%;background:var(--c)}
footer{margin-top:56px;text-align:center;color:#8a8576;font-size:13px}
footer a{color:#8a8576}
"""

CATEGORY_EXTRA_CSS = """
.crumb{padding:18px 0 0;font-size:13px;color:#8a8576}
.crumb a{color:#7fb5ff;text-decoration:none}
.hero{margin-top:18px;border:1px solid #33405255;border-radius:18px;padding:34px 30px;
      background:linear-gradient(135deg,#0e0f14,#1c1e26);position:relative}
.hero .badge{position:absolute;top:18px;right:22px;background:var(--c);color:#fff;font-size:12px;
             font-weight:700;padding:5px 14px;border-radius:20px}
.hero .ic{font-size:44px}
.hero h1{font-size:30px;margin-top:8px}
.hero .su{color:#b9b3a3;margin-top:6px;font-size:15px}
section{margin-top:38px}
h2{font-size:20px;color:#f0d68a;border-left:4px solid var(--c);padding-left:12px;margin-bottom:16px}
.intro{color:#d8d4ca;font-size:15px;max-width:760px}
.pill{display:inline-block;margin-top:6px;font-size:13px;font-weight:600;color:#fff;background:var(--c);
      border-radius:20px;padding:6px 16px}
.progline{margin-top:14px;font-size:13px;color:#9aa4b2}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;margin-top:20px}
.topic{display:block;border-radius:16px;padding:22px;text-decoration:none;transition:.18s}
.topic.live{background:#fffdf7;color:#26262b;box-shadow:0 8px 22px rgba(0,0,0,.3);cursor:pointer}
.topic.live:hover{transform:translateY(-4px);box-shadow:0 14px 30px rgba(0,0,0,.45)}
.topic.planned{background:#1c1e26;color:#8a8f9c;border:1px dashed #33405270;cursor:pointer}
.topic .ti{font-size:16.5px;font-weight:bold}
.topic.live .ti{color:#26262b}
.topic .tg{font-size:13px;margin-top:8px;color:#777}
.topic.planned .tg{color:#6b7280}
.topic .badge2{display:inline-block;margin-top:14px;font-size:12px;border-radius:14px;padding:3px 11px}
.topic.live .badge2{background:var(--c);color:#fff;font-weight:700}
.topic.planned .badge2{background:#2a2f3a;color:#9aa4b2}
"""


def page_shell(title: str, extra_css: str, body: str, active_href: str = "") -> str:
    nav_links = [
        ("./", "🧪 技能實驗室首頁"),
        ("../", "🏠 學習中心"),
        ("../resume/", "👤 我的履歷"),
    ]
    nav_html = "".join(
        f'<a class="{"active" if href == active_href else ""}" href="{href}">{label}</a>'
        for href, label in nav_links
    )
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<style>{BASE_CSS}{extra_css}</style>
</head>
<body>
<nav class="topnav">{nav_html}</nav>
<div class="wrap">
{body}
</div>
{GOATCOUNTER}
</body>
</html>
"""


def build_index():
    total = sum(len(c["topics"]) for c in CATEGORIES)
    live = sum(1 for c in CATEGORIES for t in c["topics"] if t.get("status") == "live")
    pct = round(live / total * 100) if total else 0

    cards = []
    for c in CATEGORIES:
        n = len(c["topics"])
        n_live = sum(1 for t in c["topics"] if t.get("status") == "live")
        p = round(n_live / n * 100) if n else 0
        cards.append(f"""
    <a class="catcard" style="--c:{c['color']}" href="category/{c['id']}.html">
      <div class="ic">{c['icon']}</div>
      <div class="ti">{html.escape(c['title'])}</div>
      <div class="su">{html.escape(c['subtitle'])}</div>
      <div class="prog"><span>{n_live}/{n}</span><div class="pbar"><div class="pbar-fill" style="width:{p}%"></div></div></div>
    </a>""")

    body = f"""
  <header>
    <h1>{html.escape(SITE['title'])} <span style="color:#7fb5ff;font-size:22px">· {html.escape(SITE['title_en'])}</span></h1>
    <div class="tagline">{html.escape(SITE['subtitle'])}</div>
    <div class="stats">🚀 全站進度 <b>{live}/{total}</b> 已上線<div class="bar"><div class="bar-fill" style="width:{pct}%"></div></div></div>
  </header>
  <div class="cats">{''.join(cards)}
  </div>
  <footer>
    © 2026 姬政妤 Elaine Chi · {html.escape(SITE['footer_note'])}<br>
    <a href="mailto:chengyuchi849@gmail.com">✉️ chengyuchi849@gmail.com</a> · <a href="https://github.com/ElaineChi-art" target="_blank">💻 GitHub</a>
  </footer>
"""
    (ROOT / "index.html").write_text(
        page_shell(f"{SITE['title']} · {SITE['title_en']} — Elaine Chi", HOME_EXTRA_CSS, body, "./"),
        encoding="utf-8",
    )


def build_category(c):
    n = len(c["topics"])
    n_live = sum(1 for t in c["topics"] if t.get("status") == "live")

    cards = []
    for t in c["topics"]:
        status = t.get("status", "planned")
        title = html.escape(t["title"])
        tagline = html.escape(t.get("tagline", "")) if t.get("tagline") else ""
        if status == "live":
            url = t["url"]
            cards.append(f"""
    <a class="topic live" style="--c:{c['color']}" href="{html.escape(url)}" target="_blank">
      <div class="ti">{title}</div>
      {f'<div class="tg">{tagline}</div>' if tagline else ''}
      <span class="badge2">▶ 進入專案</span>
    </a>""")
        else:
            label = "🔧 製作中" if status == "in-progress" else "🔒 規劃中"
            cards.append(f"""
    <a class="topic planned" onclick="comingSoon(event,'{title}')">
      <div class="ti">{title}</div>
      <div class="tg">之後會放上一個真的能點進去玩的小專案</div>
      <span class="badge2">{label}</span>
    </a>""")

    body = f"""
  <div class="crumb"><a href="../index.html">🧪 技能實驗室</a> / {html.escape(c['title'])}</div>
  <div class="hero" style="--c:{c['color']}">
    <span class="badge">{n_live}/{n} 已上線</span>
    <div class="ic">{c['icon']}</div>
    <h1>{html.escape(c['title'])}</h1>
    <div class="su">{html.escape(c['subtitle'])}</div>
  </div>

  <section>
    <h2 style="--c:{c['color']}">介紹</h2>
    <p class="intro">{html.escape(c['intro'])}</p>
  </section>

  <section>
    <h2 style="--c:{c['color']}">包含項目</h2>
    <span class="pill" style="--c:{c['color']}">全部分類</span>
    <div class="progline">📋 清單 · 共 {n} 個主題，{n_live} 個已上線</div>
    <div class="grid">{''.join(cards)}
    </div>
  </section>

  <footer>© 2026 姬政妤 Elaine Chi</footer>
  <script>
    function comingSoon(e,name){{
      e.preventDefault();
      alert('「'+name+'」還在製作中。\\n之後會做成一個真的可以互動、商業等級的專案 demo，不只是介紹頁。');
    }}
  </script>
"""
    (ROOT / "category" / f"{c['id']}.html").write_text(
        page_shell(f"{c['title']} — {SITE['title']} — Elaine Chi", CATEGORY_EXTRA_CSS, body, ""),
        encoding="utf-8",
    )


if __name__ == "__main__":
    build_index()
    for c in CATEGORIES:
        build_category(c)
    total = sum(len(c["topics"]) for c in CATEGORIES)
    print(f"✅ 產出 index.html + {len(CATEGORIES)} 個分類頁，共 {total} 個主題")
