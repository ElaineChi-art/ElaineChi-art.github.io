# Atelier — 捲動驅動精品 Landing Page（接案樣板）

線上：`https://elainechi-art.github.io/atelier/`

`index.html` + `vendor/three.module.js`。整只錶是 **WebGL 即時 3D 算圖**，沒有任何模型檔、貼圖檔或影片。

## ⚠️ 本機怎麼開

這頁用 ES modules + importmap，**不能直接雙擊開啟**（`file://` 會被瀏覽器的 CORS 擋掉）。本機要跑一個伺服器：

```
cd "/Users/elaine/Desktop/🎓 學習中心與專案/ElaineChi-art.github.io/atelier"
python3 -m http.server 8777
```

然後開 `http://localhost:8777/`。上到 GitHub Pages 就沒這個問題，直接開網址即可。

## 這頁在賣什麼（給客戶的話術）

滑動頁面時，一只 18ct 玫瑰金機械錶先繞著鏡頭轉，轉到正面後開始逐層拆解 —— 錶鏡、錶圈、面盤、機芯、自動盤、錶殼、底蓋沿各自的軸線分離，錶帶同時淡出，旁邊浮出技術製圖式的零件標註。

金屬上的高光會隨鏡頭移動而流動，因為那是**真的環境反射**，不是畫上去的漸層。

## 技術上跟原版教學的差別

參考的教學（*Build $5K Websites Using Claude Code*）流程是：
Higgsfield AI 生影片 → `ffmpeg` 抽 300+ 張 JPEG → canvas 依捲動進度切換第 N 張。

這裡改成 **three.js 即時 3D 算圖**：

| | 抽幀版 | 這一版 |
|---|---|---|
| 素材 | 300+ 張 JPEG，20–60 MB | 0（three.js 函式庫 687 KB） |
| 首次載入 | 要預載完才能滑 | 立即 |
| 解析度 | 固定，Retina 會糊 | 任何螢幕都銳利 |
| 改顏色／改材質 | 要重生影片 | 改一行材質參數 |
| 換角度／換運鏡 | 重拍 | 改相機曲線 |
| 生成成本 | Higgsfield 訂閱 | 無 |

保留了教學裡兩條關鍵規則：**不掛 scroll listener**（只用 `requestAnimationFrame` + `getBoundingClientRect`）、**不用 `<video>`**。

## 3D 是怎麼做出來的

`index.html` 底部的 `<script type="module">`：

1. **攝影棚環境** — `buildStudio()` 蓋一個房間，裡面擺 7 塊發光板（頭頂大柔光箱、左右兩片大柔光箱、兩條窄硬光條、背面輪廓光、正面補光），再用 `PMREMGenerator.fromScene()` 烘成環境貼圖。金屬看到的所有反射都來自這裡。
   > ⚠️ `fromScene()` 的 near/far 預設是 0.1/100。這個攝影棚有 700 單位大，**一定要明寫 `fromScene(scene, 0.03, 1, 2000)`**，否則整個攝影棚被 far plane 裁掉，環境貼圖會是全黑（然後你會以為是燈不夠亮，怎麼調都沒用）。
2. **零件幾何** — 全部程式生成。錶殼／錶圈／底蓋／龍頭是 `LatheGeometry`（剖面線繞 Y 軸旋轉），錶耳是 `ExtrudeGeometry`，齒輪與時標是 `Cylinder`／`Box`。
3. **紋路** — `flute()` 直接改頂點半徑：`r × (1 + amp·cos(count·θ))`。錶圈的 56 道齒紋、底蓋滾花、龍頭直紋、齒輪齒都是同一個函式做的。
4. **材質** — `MeshPhysicalMaterial`。玫瑰金 `metalness:1, roughness:0.11`；藍寶石 `transmission:1, ior:1.77`；面盤用一張程式生成的放射狀 roughness map 做出旭日紋（光澤來自環境，不是畫上去的顏色）。
5. **運鏡** — 捲動進度 → 方位角、仰角、鏡頭距離、零件 Y 位移。前半段環繞，後半段爆炸＋鏡頭下降後退。

## IG 展示片

`showcase.html` — 1080×1350（IG 直式 4:5）的自動播放版面：以人看電腦的視角擺一台筆電，螢幕裡是**真的 `index.html`**（同源 iframe），12 秒無縫循環自動捲動。

- 直接開 `http://localhost:8777/showcase.html` 就會自動播，可以直接螢幕錄影。
- 加 `?t=3.5` 會凍結在第 3.5 秒 —— 逐格輸出影片就是靠這個。
- 成品影片：`media/atelier-reel-4x5.mp4`

輸出流程（12 秒 × 24fps = 288 格）：

```
# 1. 起本機伺服器
python3 -m http.server 8777

# 2. 逐格截圖 + 編碼（腳本在 scratchpad，可自行改 FPS/秒數）
#    每格用 Chrome headless 截 showcase.html?t=<秒>
#    再用 OpenCV 串成 mp4
```

改標題文案：`showcase.html` 裡的 `.cap-top` / `.cap-bot`。改節奏：`KEYS` 陣列（時間 → 捲動比例）。

## 換給客戶用

- **金屬顏色** — `roseGold` 的 `color`。黃金 `(1.0,0.77,0.34)`、白金／不鏽鋼 `(0.95,0.94,0.92)`。
- **面盤顏色** — `dialMat` 的 `color`。
- **打光** — `buildStudio()` 裡那七行 `light(w,h,d, x,y,z, rx,ry,rz, intensity)`。想要更戲劇性就加大硬光條的 intensity、調暗柔光箱。
- **文案** — HTML 裡全部是真實文案，沒有 lorem ipsum。
- **設計 token** — `<style>` 開頭的 `:root`。
- **換成別的產品** — 重寫那幾個 `part(...)` 區塊。攝影棚、運鏡、捲動邏輯完全不用動。

## 注意

品牌 **Aurelis**、型號、參考號、機芯編號全部是虛構的，刻意避開真實品牌的註冊商標（Everose、Oyster、President、Cyclops 等都是 Rolex 的商標）。當展示樣板可以直接用；真的接案時換成客戶自己的品牌資料。

## 相容性

需要 WebGL2（Chrome / Safari / Firefox 現行版都有）。`prefers-reduced-motion` 開啟時會停掉捲動動畫，直接顯示拆解完成的狀態。
