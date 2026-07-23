# -*- coding: utf-8 -*-
"""台灣實習雷達：從 Yourator 抓台灣技術實習職缺，寫入 career/jobs.json。
每天由 GitHub Action 自動執行。"""
import json, urllib.request, urllib.parse, time, os

BASE = "https://www.yourator.co/api/v4/jobs"
KEYWORDS = ["前端", "全端", "軟體工程師", "區塊鏈", "Web3", "智慧合約", "後端", "Python", "資料工程", "AI"]
INTERN_HINT = ["實習", "intern"]
TECH_HINT = ["工程", "前端", "後端", "全端", "軟體", "程式", "開發", "developer", "engineer",
             "區塊鏈", "web3", "智慧合約", "solidity", "python", "javascript", "react",
             "資料", "data", " ai", "機器學習", "後台"]

def fetch(term, page=1):
    q = urllib.parse.urlencode({"term[]": term, "page": page}, doseq=True)
    req = urllib.request.Request(f"{BASE}?{q}",
        headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r).get("payload", {}).get("jobs", [])

def main():
    seen = {}
    for kw in KEYWORDS:
        try:
            for pg in (1, 2):
                for j in fetch(kw, pg):
                    name = j.get("name", "")
                    tags = j.get("tags", []) if isinstance(j.get("tags"), list) else []
                    blob = (name + " " + " ".join(map(str, tags))).lower()
                    if any(h in blob for h in INTERN_HINT) and any(h in blob for h in TECH_HINT):
                        seen[j["id"]] = {
                            "title": name,
                            "company": (j.get("company") or {}).get("brand", ""),
                            "salary": j.get("salary", "") or "",
                            "location": j.get("location", "") or "",
                            "url": "https://www.yourator.co" + j.get("path", ""),
                            "tags": [str(t) for t in tags[:4]],
                        }
                time.sleep(0.3)
        except Exception as e:
            print("err", kw, e)
    jobs = list(seen.values())[:12]
    out = {"updated": time.strftime("%Y-%m-%d %H:%M UTC"), "count": len(jobs), "jobs": jobs}
    os.makedirs("career", exist_ok=True)
    with open("career/jobs.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"✅ 寫入 {len(jobs)} 筆台灣技術實習")
    for j in jobs:
        print("  -", j["title"][:42], "@", j["company"])

if __name__ == "__main__":
    main()
