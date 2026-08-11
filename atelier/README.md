# Atelier — 捲動驅動精品 Landing Page（接案樣板）

線上：`https://elainechi-art.github.io/atelier/`

一支 `index.html`，零相依、零素材、零建置。整支動畫由 canvas 程式即時繪製。

## 這頁在賣什麼（給客戶的話術）

滑動頁面時，一只機械錶會先繞著鏡頭轉，轉到正面後開始逐層拆解 —— 錶鏡、錶圈、面盤、機芯、自動盤、錶殼、底蓋沿著各自的軸線分開，浮在黑色虛空中，旁邊浮出技術製圖式的零件標註。

這是精品品牌官網的標準語言（Apple、Rolex、Zenith 都在用）。一般做法是拍片或 3D 建模再抽成幾百張圖，成本高、載入慢。

## 技術上跟原版教學的差別

參考的教學（*Build $5K Websites Using Claude Code*）流程是：
Higgsfield AI 生影片 → `ffmpeg` 抽 300+ 張 JPEG → canvas 依捲動進度切換第 N 張。

這裡改成**程式即時算圖**，同樣的視覺，但：

| | 抽幀版 | 這一版 |
|---|---|---|
| 素材 | 300+ 張 JPEG，20–60 MB | 0 bytes |
| 首次載入 | 要預載完才能滑 | 立即 |
| 螢幕解析度 | 固定，Retina 會糊 | 任何 DPR 都銳利 |
| 改顏色／改零件 | 要重生影片 | 改幾個常數 |
| 生成成本 | Higgsfield 訂閱 | 無 |

保留了教學裡兩條關鍵規則：**不用 `<video>`**、**不掛 scroll listener**（只用 `requestAnimationFrame` + `getBoundingClientRect`）。這兩點是捲動不卡的原因。

## 動畫怎麼運作

`index.html` 底部的 `<script>`：

1. **投影** — `plane(cx, cy, zpx, K, theta, S)` 建立一個繪圖平面：先在平面內旋轉 `theta`（鏡頭環繞），再垂直壓扁 `K`（鏡頭俯角）。之後所有零件都當成平面圖形畫（圓就是 `arc()`），透視自動成立。
2. **零件** — `PARTS` 陣列，每個有 `z`（堆疊高度）跟自己的 `draw()`。依 `z` 由低到高畫，遮擋關係自然正確。
3. **相位** — `orbit`（0→0.45 環繞）、`ex`（0.46→1 爆炸）。`ex` 同時拉開 `z` 間距、壓低鏡頭 `K`、縮小整體 `S`（鏡頭後退）、淡入零件標註。
4. **驅動** — rAF 迴圈讀 `#hero` 的 `getBoundingClientRect().top` 換算成 0→1 的進度，變化超過門檻才重畫。

## 換給客戶用

改這幾處就換一個品牌：

- **設計 token** — `<style>` 開頭的 `:root`。`--accent` 換成客戶的品牌色，其餘不動。
- **文案** — HTML 裡全部是真實文案，沒有 lorem ipsum。Hero / Features 六張卡 / Specs 十列 / Closing CTA。
- **產品本體** — `PARTS` 陣列跟各個 `draw*()`。換成別的產品（耳機、香水瓶、引擎、球鞋中底）就是重寫這幾個函式，投影跟捲動邏輯完全不用動。
- **中文版** — 目前是英文（精品慣例）。要中文版把 `--display` 換成襯線中文字體（如 `Noto Serif TC`）再翻文案。

## 注意

品牌 **Aurelis**、型號、參考號、口徑編號全部是虛構的，刻意避開真實品牌的註冊商標（Everose、Oyster、President、Cyclops 等都是 Rolex 的商標）。當展示樣板可以直接用；真的接案時換成客戶自己的品牌資料。

## 相容性

Chrome / Safari / Firefox 現行版。`ctx.letterSpacing` 沒有的瀏覽器會自動略過（標註仍然顯示，只是不加字距）。已處理 `prefers-reduced-motion`：關閉捲動動畫，直接顯示拆解完成的狀態。
