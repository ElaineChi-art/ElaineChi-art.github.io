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

## 第二個產品：香水瓶

`parfum/index.html` — **同一套 3D 手法，換成香水瓶**。攝影棚、運鏡曲線、捲動邏輯、爆炸圖機制完全沿用，只重寫了幾何與材質：

- 瓶身是**中空**的車削幾何（外壁上去、內壁下來），玻璃才有真實厚度可以折射
- 酒液是獨立零件，用 `attenuationColor` + `attenuationDistance` 讓琥珀色隨厚度變深，不是塗上去的顏色
- 燙金字是 canvas 貼圖貼在一段圓柱面上（不是平面貼紙）
- 爆炸時酒液柱會整根浮出瓶外

⚠️ **玻璃需要背光**。純黑背景裡透明材質沒有東西可以折射，瓶子會變成一團黑。解法是 `scrim` 這片柔光幕 —— 而且它必須沿著「鏡頭→產品」的視線方向擺，只把 y 設成瓶身高度是不行的，俯角的透視會把光暈推到畫面上方。

## 產品線（同一套 rig，四個產品）

| 目錄 | 產品 | 這個產品逼出了什麼技術 |
|---|---|---|
| `/` | 玫瑰金機械錶 | 金屬 PBR、環境反射、機芯級修飾（珍珠紋／日內瓦條紋／倒角） |
| `parfum/` | 水晶香水瓶 | 玻璃折射、液體吸收、背光幕 |
| `casque/` | 監聽耳機 | 非垂直的拆解軸線（左右鏡射）、七種材質 |
| `course/` | 針織跑鞋 | **載入真實 3D 模型** + 從網格自動拆件 |

前三個都能用 `LatheGeometry`（剖面繞軸旋轉）解決 —— 那是程式的強項。**鞋不行**：它沒有旋轉對稱軸，是雕出來的有機曲面，那些線條是設計師手工拉的，沒有公式。純程式生成的版本試過了，做得到「一看知道是跑鞋」，做不到「一看就想買」。

所以 `course/` 改成**載入真實模型**（`model/shoe.glb`），攝影棚／運鏡／捲動拆解／標註全部照用 —— 這也才是真實的接案流程：客戶給你產品的 3D 檔。

模型只有**一個網格**，沒有分件，所以爆炸圖是在載入時算出來的：走訪索引緩衝做 union-find 找出 83 個獨立殼體，再依各殼體的重心高度分成鞋帶／鞋口／鞋面／中底／大底五層，各自重建索引（頂點緩衝共用，只有索引分開）。

⚠️ 模型授權：`model/shoe.glb` 是 Khronos 官方樣本 “Materials Variants Shoe”，**© 2021 Shopify, Inc. / CC BY 4.0** —— 可商用但**必須標註出處**，頁尾已加。真的接案時換成客戶自己的模型檔就沒這個限制。

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
