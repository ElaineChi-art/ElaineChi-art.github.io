#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每週流量報告（本機自動執行版）
抓 GoatCounter 公開看板 → 產生中文報告到 ~/Desktop/流量報告/ → 跳 Mac 通知。
由 launchd 每週一 09:00 自動執行；也可手動 `python3 weekly_report.py` 立即產生。
"""
import re, os, json, datetime, urllib.request, ssl, subprocess

GC_URL = "https://elainechi.goatcounter.com/"
OUT_DIR = os.path.expanduser("~/Desktop/流量報告")
STATE = os.path.join(OUT_DIR, ".history.json")   # 記錄每週快照，用來算增減

# 路徑 → 作品友善名稱
NAMES = {
    "/resume": "👤 履歷",
    "/music-os/ecosystem.html": "🎵 音樂版稅 OS",
    "/music-os/": "🎵 音樂版稅 OS",
    "/judicial/": "📚 司法官複習",
    "/vocab/": "🔤 英文單字",
    "/taiwan-stock-dashboard/": "📈 台股儀表板",
    "/research-radar/": "🔬 研究雷達",
    "/exam-radar/": "⚖️ 申論雷達",
    "/": "🏠 首頁",
}

def friendly(path):
    for k, v in NAMES.items():
        if path.startswith(k) and k != "/":
            return v
    return NAMES.get(path, path)

def fetch(url):
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
        return r.read().decode("utf-8", "replace")

def parse(html):
    """回傳 {path: count}。每個路徑第一次出現後，緊接著的 data-count 就是它的數字。"""
    pages, last, seen = {}, None, set()
    token = re.compile(r'data-count="(\d+)"|(/[\w/.\-]*)')
    known = ("/resume", "/judicial", "/vocab", "/music-os",
             "/taiwan-stock-dashboard", "/research-radar", "/exam-radar")
    for m in token.finditer(html):
        if m.group(2) is not None:                       # 是一個路徑
            p = m.group(2)
            if any(p.startswith(k) for k in known):
                last = p
        elif m.group(1) is not None and last and last not in seen:  # 是 count
            pages[last] = int(m.group(1)); seen.add(last); last = None
    return pages

def load_state():
    try:
        with open(STATE, encoding="utf-8") as f: return json.load(f)
    except Exception:
        return {}

def notify(title, msg):
    try:
        subprocess.run(["osascript", "-e",
            f'display notification "{msg}" with title "{title}" sound name "Glass"'],
            check=False)
    except Exception:
        pass

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    today = datetime.date.today().isoformat()
    try:
        html = fetch(GC_URL)
    except Exception as ex:
        notify("流量報告失敗", f"讀不到 GoatCounter：{ex}")
        return
    if "Sign in" in html and "data-count" not in html:
        notify("流量報告", "看板不是公開的，讀不到數據。請到 GoatCounter Settings 設為公開。")
        return

    pages = parse(html)
    total = sum(pages.values())

    # 與上一份快照比較
    hist = load_state()
    prev = hist.get("last", {})
    prev_total = prev.get("total", 0)
    delta = total - prev_total
    delta_str = f"（較上次 {'+' if delta>=0 else ''}{delta}）" if prev else "（首次紀錄）"

    # 排序頁面
    rows = sorted(pages.items(), key=lambda kv: kv[1], reverse=True)

    lines = [f"# 📊 流量報告 · {today}", ""]
    lines.append(f"**總瀏覽：{total} 次** {delta_str}")
    lines.append("")
    lines.append("| 作品 | 瀏覽 |")
    lines.append("|---|---|")
    for path, cnt in rows:
        lines.append(f"| {friendly(path)} ({path}) | {cnt} |")
    if not rows:
        lines.append("| （目前尚無紀錄） | 0 |")
    lines.append("")
    lines.append(f"看板：{GC_URL}")
    lines.append(f"履歷：https://elainechi-art.github.io/resume/")
    lines.append("")
    lines.append("> 提示：把履歷連結多散到 LinkedIn / IG / 投遞信裡，數字才會長。")
    report = "\n".join(lines)

    out = os.path.join(OUT_DIR, f"{today}.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(report)

    # 更新快照
    hist["last"] = {"date": today, "total": total, "pages": pages}
    hist.setdefault("weeks", []).append({"date": today, "total": total})
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(hist, f, ensure_ascii=False, indent=2)

    top = friendly(rows[0][0]) if rows else "—"
    notify("本週流量報告好了 📊", f"總瀏覽 {total} 次{delta_str}，最熱門：{top}。報告已存到桌面／流量報告")
    print(report)
    print(f"\n✅ 已存：{out}")

if __name__ == "__main__":
    main()
