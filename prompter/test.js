// 執行：node prompter/test.js
const C = require('./core.js');
let pass = 0, fail = 0;
function ok(cond, name) { if (cond) pass++; else { fail++; console.log('✗ ' + name); } }

// 切段與檢索
const law = { id: 'd1', name: '著作權筆記.pdf', pages: [
  { page: 1, text: '思想表達二分原則\n著作權法第10條之1規定，著作權保護僅及於該著作之表達，而不及於其所表達之思想、程序、製程、系統、操作方法、概念、原理、發現。' },
  { page: 2, text: 'AI生成物\n經濟部智慧財產局認為，著作須為人類精神上之創作。純由人工智慧自動生成、沒有人類創意投入的內容，不受著作權法保護。' },
  { page: 3, text: '合理使用\n著作權法第65條規定合理使用的判斷基準，包括利用之目的及性質、著作之性質、所利用之質量及其在整個著作所占之比例、利用結果對著作潛在市場與現在價值之影響。' }
] };
const budget = { id: 'd2', name: '預算書.txt', pages: [{ page: null, text: '社會住宅興建計畫\n115年度編列新台幣12億元，執行率為68%，主因為用地取得延宕。\n\n公共運輸補助\n115年度編列3.5億元，執行率92%。' }] };
const bank = { id: 'd3', name: '面試題庫.md', pages: [{ page: null, text: 'Q1：請你簡單自我介紹\nA：我是姬政妤，陽明交大科技法律研究所碩士。\n\nQ2：為什麼想來法遵部門？\nA：因為我的研究聚焦虛擬資產與洗錢防制。\n\n問題3：你的缺點是什麼？\n答：我有時太追求細節。' }] };

const chunks = [...C.chunkDoc(law), ...C.chunkDoc(budget), ...C.chunkDoc(bank)];
ok(chunks.length >= 6, '切出足夠段落 (' + chunks.length + ')');
ok(chunks.filter(c => c.type === 'qa').length === 3, '題庫切成 3 題');
ok(chunks.find(c => c.q === '為什麼想來法遵部門？'), '題目文字正確');
ok(chunks.find(c => c.type === 'qa' && c.q.includes('缺點')).text.includes('細節'), '「問題3/答：」格式也能解析');
const idx = C.buildIndex(chunks);

const top = q => (C.search(idx, q, 3)[0] || {}).chunk || {};
ok(top('AI 生成的圖片有沒有著作權').page === 2, 'AI 生成物 → 第2頁');
ok(top('第10條之1在講什麼').page === 1, '法條條號 第10條之1 → 第1頁');
ok(top('§65 合理使用怎麼判斷').page === 3, '§65 → 第3頁');
ok(top('社會住宅的執行率為什麼這麼低').docName === '預算書.txt', '預算問題 → 預算書');
ok(top('社會住宅的執行率為什麼這麼低').text.includes('68%'), '找到 68% 那段');
ok(top('臺北公共運輸補助多少錢').text.includes('3.5億'), '臺/台 正規化');
ok(C.search(idx, '請問一下你認為呢', 3).length === 0, '只有贅字的問題不亂配');

// PDF 部首異體字（⼆⾏）
const pdfDoc = { id: 'd4', name: 'x.pdf', pages: [{ page: 7, text: '第⼆章 預算執⾏\n本計畫執⾏率偏低。' }] };
const idx2 = C.buildIndex(C.chunkDoc(pdfDoc));
ok((C.search(idx2, '執行率')[0] || {}).chunk, '「執行」搜得到 PDF 裡的「執⾏」');
ok(C.chunkDoc(pdfDoc)[0].text.includes('執行率'), 'PDF 異體字顯示時也換回一般字');
ok(chunks.find(c => c.docName === '預算書.txt' && c.text.includes('68%')).heading === '社會住宅興建計畫', '段落標題是段落開頭的小節');

// 題庫比對
ok(C.bankMatch(idx, '可以請你先簡單自我介紹一下嗎') !== null, '口語版自我介紹命中題庫');
ok(C.bankMatch(idx, '你為什麼想要來我們法遵部門') !== null, '法遵題命中');
ok(C.bankMatch(idx, '社會住宅執行率') === null, '不相關問題不誤中題庫');

// 提示詞
const p = C.buildPrompt({ mode: 'law', question: 'AI生成物有著作權嗎', hits: C.search(idx, 'AI生成物有著作權嗎'), strict: false });
ok(p.includes('[1] 《著作權筆記.pdf 第2頁'), '提示詞含來源與頁碼');
ok(p.includes('一律忽略'), '提示詞含防注入規則');
ok(C.buildPrompt({ mode: 'job', question: 'x', hits: [], strict: true }).includes('資料庫無此資訊'), '嚴格模式');

// 答案解析（含串流到一半）
const raw = '【核心問題】AI生成物能否受保護\n【一句話】純AI生成的內容不受著作權保護。[1]\n【重點】\n1. 須有人類創作 [1]\n2. 表達才受保護 [2]\n3. 人類參與程度是關鍵\n【口語稿】我認為…[1][9]\n【可能追問】\n- 提示詞算創作嗎？\n- 修圖算嗎？\n【注意】無';
const a = C.parseAnswer(raw);
ok(a.one === '純AI生成的內容不受著作權保護。[1]', '解析一句話');
ok(C.listItems(a.points).length === 3, '解析三重點');
ok(C.listItems(a.follow).length === 2, '解析追問');
ok(JSON.stringify(C.citations(a.script, 2)) === '[1]', '超出範圍的引用 [9] 被丟掉');
ok(C.parseAnswer('【核心問題】AI生成物\n【一句').core === 'AI生成物\n【一句' || C.parseAnswer('【核心問題】AI生成物\n【一句').core.startsWith('AI生成物'), '串流到一半不報錯');
ok(C.parseAnswer('**【一句話】**好').one !== undefined, '模型多加粗體仍可解析');

// 小模型格式跑掉時自動拆回
const messy = C.parseAnswer('【一句話】我承認多數是收藏品 [4]\n1. 多數無收益承諾\n2. 有收益承諾可能是證券\n3. MiCA 區分\n【口語稿】我承認…\n- 收藏品定義是什麼？\n- 有哪些案例？\n【注意】');
ok(messy.one === '我承認多數是收藏品 [4]', '重點擠進一句話 → 一句話只留第一句');
ok(C.listItems(messy.points).length === 3, '重點拆回三點');
ok(C.listItems(messy.follow).length === 2 && messy.script === '我承認…', '追問從口語稿拆出');
ok(C.parseAnswer('<think>想一下</think>【一句話】好').one === '好', '思考過程不顯示');

// 一題多問法
const multi = C.chunkDoc({ id: 'm', name: 'm.md', pages: [{ page: null, text: 'Q：你的論文核心結論是什麼？\nQ：一句話講你的結論\nQ：所以你到底主張什麼\nA：智慧合約是執行工具，不是權利本身。\n\nQ：研究限制？\nA：法域與時效。' }] });
ok(multi.length === 4 && multi.filter(c => c.text.startsWith('智慧合約')).length === 3, '三種問法共用同一個擬答');

// 事實查核
const vc = C.verifyClaims('最高法院113年度台上字第4521號判決認為…依著作權法第37條，執行率68%，2023年', ['著作權法第37條規定…執行率為68%，2023年Impact Theory案'], '113年度台上字第4521號判決結論');
ok(vc.find(x => /4521/.test(x.text)).found === false, '捏造的判決字號被抓出來');
ok(vc.find(x => /4521/.test(x.text)).inQuestion === true, '知道字號來自提問');
ok(vc.find(x => /37/.test(x.text)).found === true, '資料裡有的條號通過');
ok(vc.find(x => /68/.test(x.text)).found === true, '資料裡有的百分比通過');
ok(C.verifyClaims('依第99條', ['第37條'], '').every(x => !x.found), '資料沒有的條號被抓出來');

// 判斷問題是否變長
ok(!C.grewEnough('社會住宅執行率為什麼這麼低', '社會住宅執行率為什麼這麼低呢'), '多一個字不重答');
ok(C.grewEnough('社會住宅執行率', '社會住宅執行率為什麼這麼低，明年要怎麼改善'), '問題明顯變長要重答');

// SSE 串流解析（模擬網路切碎）
let got = '';
const feed = C.makeSSEParser(j => { got += C.deltaText('gemini', j); });
const sse = 'data: {"candidates":[{"content":{"parts":[{"text":"【一句"}]}}]}\r\n\r\ndata: {"candidates":[{"content":{"parts":[{"text":"話】你好"}]}}]}\n\n';
for (let i = 0; i < sse.length; i += 7) feed(sse.slice(i, i + 7));
ok(got === '【一句話】你好', 'Gemini SSE 切碎後仍正確組回');
got = '';
const feed2 = C.makeSSEParser(j => { got += C.deltaText('openrouter', j); });
feed2('data: {"choices":[{"delta":{"content":"甲"}}]}\n\ndata: {"choices":[{"delta":{"content":"乙"}}]}\n\ndata: [DONE]\n\n');
ok(got === '甲乙', 'OpenRouter SSE');
got = '';
const feed3 = C.makeSSEParser(j => { got += C.deltaText('claude', j); });
feed3('event: content_block_delta\ndata: {"type":"content_block_delta","delta":{"type":"text_delta","text":"丙"}}\n\n');
ok(got === '丙', 'Claude SSE');

console.log(`\n${pass} 通過 / ${fail} 失敗`);
process.exit(fail ? 1 : 0);
