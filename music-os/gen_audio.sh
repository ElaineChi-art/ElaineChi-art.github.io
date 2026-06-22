#!/bin/bash
# Generate offline narration audio (.m4a) via macOS `say` + `afconvert`
set -e
cd "$(dirname "$0")"
mkdir -p audio
ZH="Meijia"      # zh_TW 美佳
EN="Samantha"    # en_US
TMP="$(mktemp -d)"

mk(){  # mk <voice> <outname> <text>
  local voice="$1" out="$2" text="$3"
  say -v "$voice" -o "$TMP/$out.aiff" "$text"
  afconvert "$TMP/$out.aiff" "audio/$out.m4a" -f m4af -d aac >/dev/null 2>&1
  echo "  ✓ audio/$out.m4a"
}

# ---- TOUR (8) ----
TOUR_ZH=(
"歡迎使用音樂版稅作業系統。這是一套把音樂版權變成可投資、可自動分潤的金融資產的完整系統。"
"應用層：藝人上傳並鑄造作品，粉絲購買碎片化的版稅 NFT，成為作品的股東。"
"平台層的版稅引擎，依照持份比例，即時把收入分配給每一位權利人。"
"區塊鏈層：所有交易在以太坊上結算，經過記憶池、出塊，大約十二點八分鐘達到最終性。"
"智能合約執行：一筆二手轉售在以太坊虛擬機裡，讀取版稅比例、相乘、相除，再寫入餘額並發出事件。"
"全球九大收益來源，以資料流注入版稅引擎，每個平台都有真實的每千次串流分潤費率。"
"智慧合約自動且透明地，把收入分配給藝人、NFT 持有人、製作人、出版商與平台財庫。"
"這不只是視覺化，而是一個你可以實際操作、邊使用邊理解的音樂經濟作業系統。"
)
TOUR_EN=(
"Welcome to a financial operating system that turns music rights into an investable, auto-distributing asset class."
"In the application layer, artists mint songs and fans buy fractional royalty NFTs, becoming shareholders."
"The platform's royalty engine distributes income in real time by ownership percentage."
"Everything settles on Ethereum: the mempool, block production, and Casper finality in about twelve point eight minutes."
"Here a secondary sale executes inside the E V M: load the royalty rate, multiply, divide, then write balances and emit events."
"Nine global revenue sources stream in, each with real per-thousand-stream payout rates."
"Smart contracts split the income automatically and transparently among artists, holders, producers and the treasury."
"This is not a diagram. It is a guided system you operate to understand the entire music economy."
)

# ---- STORY (12) ----
STORY_ZH=(
"第一步，藝人創作了一首新歌《回聲》，這是一切價值的源頭。"
"第二步，登錄詞曲、錄音與表演的授權，並在鏈上設定百分之五的版稅。"
"第三步，音檔存入 IPFS 去中心化儲存，token URI 指向它的內容位址。"
"第四步，鑄造成 ERC-721 音樂 NFT，並寫入 ERC-2981 版稅標準。打開實驗室可以看到 storage 的變化。"
"第五步，粉絲買入碎片化份額，成為這首歌未來收益的股東。"
"第六步，Spotify、Apple Music、YouTube 開始串流播放，產生真實收益。"
"第七步，二手轉售觸發版稅智慧合約，逐一執行每一個指令。"
"第八步，合約自動把收益依比例分配給所有權利人。"
"第九步，平台抽成進入 Safe 多重簽章財庫。"
"第十步，每一位持有人的餘額與年化收益即時更新。"
"第十一步，收益表現亮眼，二級市場價格隨之上漲。"
"第十二步，持有人發起治理提案，重新授權這首歌的使用。"
)
STORY_EN=(
"An artist finishes a new song called Echoes, the origin of all value."
"Rights and licensing terms are registered, with a five percent royalty set on chain."
"The audio is stored on I P F S, and the token U R I points to its content address."
"The song is minted as an E R C seven twenty one N F T with E R C twenty nine eighty one royalties. Open the lab to watch storage change."
"Fans buy fractional shares and become shareholders in the song's future income."
"Streaming begins on Spotify, Apple Music and YouTube, generating real revenue."
"A secondary sale triggers the royalty contract. Watch it execute opcode by opcode."
"The contract splits the revenue automatically among all rights holders."
"The platform fee flows into the Safe multi-signature treasury."
"Each holder's balance and yield update in real time."
"Strong performance pushes the secondary market price up."
"Holders raise a governance proposal to re-license the song."
)

echo "Generating TOUR…"
for i in "${!TOUR_ZH[@]}"; do mk "$ZH" "tour_zh_$i" "${TOUR_ZH[$i]}"; mk "$EN" "tour_en_$i" "${TOUR_EN[$i]}"; done
echo "Generating STORY…"
for i in "${!STORY_ZH[@]}"; do mk "$ZH" "story_zh_$i" "${STORY_ZH[$i]}"; mk "$EN" "story_en_$i" "${STORY_EN[$i]}"; done
echo "Generating test…"
mk "$ZH" "test_zh" "語音導覽已啟用，歡迎使用音樂版稅作業系統。"
mk "$EN" "test_en" "Narration enabled. Welcome to the Music Royalty Operating System."

rm -rf "$TMP"
echo "DONE → $(ls audio | wc -l | tr -d ' ') files in audio/"
