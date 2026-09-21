/* IGS · 創新治理管理系統
   骨架 = ISO 協調架構（Annex SL）第 4–10 章 = TIPS 2016 ch.4–10 = ISO 56001 = 課程 13 堂順序
   資料存 localStorage（igs_v1），可匯出／匯入 JSON */
'use strict';
const LSKEY = 'igs_v1';
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const today = () => new Date().toISOString().slice(0, 10);

const EMPTY = () => ({
  org: {name:'', industry:'', capital:'', listed:'', scope:'', vision:'', intent:'', topMgmt:'', boardReportDate:''},
  issues:[], stakeholders:[], areas:[],
  leadership:{commitment:{}, policy:{text:'',version:'',approver:'',date:''}, strategy:{text:''}},
  roles:[], objectives:[], riskCriteria:{lowMax:5, midMax:12}, risks:[], initiatives:[], partners:[],
  resources:[], competence:[], comms:[], docs:[], ip:[], audits:[], reviews:[], ncs:[], improvements:[]
});
let S = load();
function load(){ try{ const j = JSON.parse(localStorage.getItem(LSKEY)); if(j) return Object.assign(EMPTY(), j);}catch(e){} return EMPTY(); }
function save(){ try{ localStorage.setItem(LSKEY, JSON.stringify(S)); }catch(e){} renderSide(); }
function toast(m){ const t=$('#toast'); t.textContent=m; t.classList.add('on'); setTimeout(()=>t.classList.remove('on'),1600); }

/* ───────── 集合定義（通用 CRUD） ───────── */
const SEL = (o) => o;
const COLL = {
  issues:{ title:'內外部議題', clause:'4.1', week:'第4堂 10/16', desc:'決定與組織目的及策略方向相關、影響創新治理成效的內外部議題。這是風險評鑑（6.2）與機會領域的輸入。',
    fields:[{k:'type',l:'內／外部',t:'select',o:['外部','內部'],col:1},{k:'cat',l:'類別',t:'select',o:['法規','市場','科技','競爭','社會','人員','技術','財務','流程','其他'],col:1},{k:'desc',l:'議題描述',t:'textarea',full:1,col:1},{k:'impact',l:'性質',t:'select',o:['機會','風險','兩者'],col:1},{k:'note',l:'備註／追蹤',t:'text',col:1}]},
  stakeholders:{ title:'利害關係人', clause:'4.2', week:'第4堂 10/16', desc:'誰在乎這套系統？他們的需要與期望是什麼？公司治理的核心就是「平衡各方利害關係人利益」。',
    fields:[{k:'name',l:'利害關係人',t:'text',col:1},{k:'type',l:'類型',t:'select',o:['治理','客戶','客戶／夥伴','主管機關','員工','產業','供應商','社會'],col:1},{k:'needs',l:'需要',t:'textarea',col:1},{k:'expect',l:'期望',t:'textarea',col:1},{k:'relevance',l:'相關性',t:'select',o:['高','中','低'],col:1}]},
  areas:{ title:'機會領域', clause:'4.1 / 4.3.1', week:'第4堂 10/16', desc:'針對機會的探索主題（ISO 56000）。由內外部議題推導，回頭餵給創新意圖與創新策略。',
    fields:[{k:'theme',l:'機會領域（主題）',t:'text',col:1,full:1},{k:'rationale',l:'依據（哪些議題）',t:'textarea',col:1,full:1},{k:'linkedIntent',l:'對應創新意圖',t:'text',col:1}]},
  roles:{ title:'權責與溝通', clause:'5.4 / 5.3', week:'第6堂 10/30', desc:'最高管理者要指派角色、分配權責。TIPS 5.4：有權責、有部門，各司其職確保制度運作。',
    fields:[{k:'role',l:'角色',t:'text',col:1},{k:'person',l:'人員',t:'text',col:1},{k:'resp',l:'職責',t:'textarea',full:1,col:1},{k:'clause',l:'對應條款',t:'text',col:1}]},
  objectives:{ title:'創新／智財目標', clause:'6.3 / TIPS 5.3', week:'第5堂 10/23', desc:'目標要可量測、與政策一致、有人負責、有期限（SMART）。這裡的 KPI 直接進 9.1 績效監督與董事會報告。',
    fields:[{k:'name',l:'目標',t:'text',col:1},{k:'kpi',l:'KPI',t:'text',col:1},{k:'target',l:'目標值',t:'text',col:1},{k:'actual',l:'目前值',t:'text',col:1},{k:'due',l:'期限',t:'date',col:1},{k:'owner',l:'負責人',t:'text',col:1},{k:'status',l:'狀態',t:'select',o:['規劃中','進行中','已達成','未達成','取消'],col:1}]},
  initiatives:{ title:'創新倡議與創新過程', clause:'8.2 / 6.4', week:'第3堂 10/2', desc:'以創新為目標的一套協調活動。過程：辨識機會→創造概念→驗證概念→開發解決方案→部署。組合：探索／開發／部署。',
    fields:[{k:'name',l:'倡議名稱',t:'text',col:1},{k:'intent',l:'對應創新意圖',t:'text',col:1},{k:'stage',l:'創新過程階段',t:'select',o:['辨識機會','創造概念','驗證概念','開發解決方案','部署'],col:1},{k:'portfolio',l:'組合',t:'select',o:['探索','開發','部署'],col:1},{k:'budget',l:'預算',t:'text',col:1},{k:'uncert',l:'不確定性／假設',t:'textarea',full:1},{k:'owner',l:'負責人',t:'text',col:1},{k:'status',l:'狀態',t:'select',o:['進行中','暫停','已部署','中止'],col:1}]},
  partners:{ title:'協同合作', clause:'6.6 / ISO 56003', week:'第6堂 10/30', desc:'內外部協作夥伴。每一段合作都要有契約，契約裡要有智財歸屬條款（TIPS 8.2 委外管理）。',
    fields:[{k:'name',l:'夥伴',t:'text',col:1},{k:'type',l:'類型',t:'select',o:['學研','產業','供應商','客戶','政府','新創'],col:1},{k:'scope',l:'合作範圍',t:'textarea',col:1},{k:'agreement',l:'契約／智財歸屬',t:'textarea',col:1}]},
  resources:{ title:'資源', clause:'7.1', week:'第8堂 11/13', desc:'ISO 56001 特色成分：人員 7.1.2、時間 7.1.3、財務 7.1.4、基礎設施 7.1.5（含資訊系統、AI 開發工具）、知識 7.1.6。',
    fields:[{k:'kind',l:'資源類型',t:'select',o:['人員','時間','財務','基礎設施','知識'],col:1},{k:'desc',l:'說明',t:'textarea',full:1,col:1},{k:'amount',l:'數量／金額',t:'text',col:1},{k:'owner',l:'負責人',t:'text',col:1}]},
  competence:{ title:'能力（適任性）', clause:'7.2', week:'第8堂 11/13', desc:'能夠應用知識及技能實現預期結果的能力。缺口→訓練→留紀錄。',
    fields:[{k:'person',l:'人員／群體',t:'text',col:1},{k:'skill',l:'所需能力',t:'text',col:1},{k:'level',l:'現況',t:'select',o:['高','中','低'],col:1},{k:'training',l:'訓練／措施',t:'text',col:1},{k:'due',l:'期限',t:'text',col:1}]},
  comms:{ title:'溝通計畫', clause:'7.3', week:'第8堂 11/13', desc:'溝通什麼、對誰、何時、透過什麼管道、誰負責。董事會年度智財報告（ESG S-10）就是一條溝通計畫。',
    fields:[{k:'what',l:'溝通內容',t:'text',col:1},{k:'who',l:'對象',t:'text',col:1},{k:'when',l:'時機',t:'text',col:1},{k:'channel',l:'管道',t:'text',col:1},{k:'owner',l:'負責人',t:'text',col:1}]},
  docs:{ title:'文件化資訊', clause:'7.4', week:'第8堂 11/13', desc:'文件登錄：政策、手冊、程序、表單、紀錄。有版本、有負責人、有審查日期，資訊才「具可用性」。',
    fields:[{k:'code',l:'文件編號',t:'text',col:1},{k:'title',l:'名稱',t:'text',col:1},{k:'type',l:'類型',t:'select',o:['政策','手冊','程序','辦法','表單','紀錄'],col:1},{k:'ver',l:'版本',t:'text',col:1},{k:'owner',l:'負責人',t:'text',col:1},{k:'review',l:'下次審查',t:'date',col:1}]},
  ip:{ title:'智財權利管理流程', clause:'8.1–8.4', week:'第1堂 9/11', desc:'TIPS 核心：提案→成果→取得→保護→維護→運用，過程中避免侵權、保護權利。每一筆智財資產在哪個階段、誰負責、值多少。',
    fields:[{k:'name',l:'智財名稱',t:'text',col:1},{k:'type',l:'類型',t:'select',o:['發明專利','新型專利','設計專利','商標','著作權','營業秘密','授權','其他'],col:1},{k:'stage',l:'流程階段',t:'select',o:['提案','成果','取得','保護','維護','運用'],col:1},{k:'juris',l:'國別／地區',t:'text',col:1},{k:'appNo',l:'申請／註冊號',t:'text'},{k:'date',l:'日期',t:'date',col:1},{k:'owner',l:'負責人',t:'text',col:1},{k:'initiative',l:'來源倡議',t:'text'},{k:'value',l:'價值等級',t:'select',o:['核心','重要','一般','待評估'],col:1},{k:'status',l:'狀態',t:'text',col:1},{k:'note',l:'備註',t:'textarea',full:1}]},
  audits:{ title:'內部稽核', clause:'9.2', week:'第7堂 11/6', desc:'依年度稽核計畫（內控準則 §13 須經董事會通過）查核制度是否符合要求並有效實施。發現→開不符合（10.2）。',
    fields:[{k:'date',l:'日期',t:'date',col:1},{k:'scope',l:'稽核範圍（條款）',t:'text',col:1},{k:'auditor',l:'稽核人員',t:'text',col:1},{k:'finding',l:'發現',t:'textarea',full:1,col:1},{k:'result',l:'結果',t:'text',col:1}]},
  reviews:{ title:'管理審查', clause:'9.3', week:'第7堂 11/6', desc:'最高管理者定期審查系統：輸入（稽核、目標、風險、回饋、資源）→ 決定（改善、資源、政策變更）。',
    fields:[{k:'date',l:'日期',t:'date',col:1},{k:'chair',l:'主持',t:'text',col:1},{k:'inputs',l:'審查輸入',t:'textarea',full:1},{k:'decisions',l:'決議／輸出',t:'textarea',full:1,col:1}]},
  ncs:{ title:'不符合與矯正措施', clause:'10.2', week:'第7堂 11/6', desc:'發現不符合→控制並矯正→分析原因→採取措施防止再發→檢討有效性。',
    fields:[{k:'src',l:'來源',t:'text',col:1},{k:'desc',l:'不符合描述',t:'textarea',full:1,col:1},{k:'cause',l:'根本原因',t:'textarea'},{k:'action',l:'矯正措施',t:'textarea',col:1},{k:'owner',l:'負責人',t:'text',col:1},{k:'due',l:'期限',t:'date',col:1},{k:'status',l:'狀態',t:'select',o:['待處理','進行中','已完成','已驗證'],col:1}]},
  improvements:{ title:'持續改善', clause:'10.3', week:'第7堂 11/6', desc:'持續改善系統的適切性、充分性與有效性。記錄做了什麼、效果如何。',
    fields:[{k:'date',l:'日期',t:'date',col:1},{k:'desc',l:'改善事項',t:'textarea',full:1,col:1},{k:'effect',l:'效果',t:'text',col:1}]}
};

/* ───────── 側欄結構 ───────── */
const NAV = [
  {id:'dash', icon:'🏛', title:'治理儀表板', cl:''},
  {id:'gov', icon:'📋', title:'治理輸出・董事會', cl:'法規'},
  {grp:'第4章 組織全景', wk:'第4堂 10/16'},
  {id:'org', icon:'🧭', title:'範圍・願景・創新意圖', cl:'4.3'},
  {id:'issues', coll:1}, {id:'stakeholders', coll:1}, {id:'areas', coll:1},
  {grp:'第5章 領導', wk:'第6堂 10/30'},
  {id:'lead', icon:'👑', title:'承諾・政策・策略', cl:'5.1–5.3'},
  {id:'roles', coll:1},
  {grp:'第6章 規劃', wk:'第5堂 10/23'},
  {id:'risk', icon:'⚠️', title:'風險評鑑', cl:'6.2'},
  {id:'objectives', coll:1}, {id:'initiatives', coll:1}, {id:'partners', coll:1},
  {grp:'第7章 支援', wk:'第8堂 11/13'},
  {id:'resources', coll:1}, {id:'competence', coll:1}, {id:'comms', coll:1}, {id:'docs', coll:1},
  {grp:'第8章 運作', wk:'第1–3堂'},
  {id:'ip', coll:1},
  {grp:'第9章 績效評估', wk:'第7堂 11/6'},
  {id:'kpi', icon:'📈', title:'監督與量測', cl:'9.1'},
  {id:'audits', coll:1}, {id:'reviews', coll:1},
  {grp:'第10章 改善', wk:'第7堂 11/6'},
  {id:'ncs', coll:1}, {id:'improvements', coll:1},
  {grp:'創新支援系統', wk:'第8–10堂'},
  {id:'isms', icon:'🔐', title:'資訊安全管理系統', cl:'27001', lock:1},
  {id:'aims', icon:'🤖', title:'人工智慧管理系統', cl:'42001', lock:1},
  {grp:'參考', wk:''},
  {id:'map', icon:'🗺', title:'標準對照表', cl:'HS'},
  {id:'settings', icon:'⚙️', title:'設定・匯出匯入', cl:''}
];
const ICONS = {issues:'🌐',stakeholders:'🤝',areas:'🎯',roles:'🧑‍💼',objectives:'🏁',initiatives:'🚀',partners:'🔗',resources:'🧰',competence:'🎓',comms:'📣',docs:'📁',ip:'💎',audits:'🔍',reviews:'🪑',ncs:'🛠',improvements:'♻️'};

let view = location.hash.replace('#','') || 'dash';
function renderSide(){
  const el = $('#side'); let h = '';
  NAV.forEach(n => {
    if(n.grp){ h += `<div class="grp"><span>${n.grp}</span><span class="wk">${n.wk}</span></div>`; return; }
    const c = n.coll ? COLL[n.id] : n;
    const title = n.coll ? c.title : n.title, cl = n.coll ? c.clause : n.cl, icon = n.coll ? ICONS[n.id] : n.icon;
    const cnt = n.coll ? (S[n.id]||[]).length : '';
    h += `<button class="nav ${view===n.id?'on':''} ${n.lock?'lock':''}" onclick="go('${n.id}')"><span class="cl">${cl}</span><span>${icon} ${title}</span>${cnt?`<span class="cnt">${cnt}</span>`:''}</button>`;
  });
  el.innerHTML = h;
  $('#orgName').textContent = S.org.name || '（尚未設定組織）';
}
function go(v){ view = v; location.hash = v; renderSide(); render(); window.scrollTo(0,0); }
window.addEventListener('hashchange', () => { const v = location.hash.replace('#',''); if(v && v!==view){ view=v; renderSide(); render(); } });

function render(){
  const m = $('#main');
  if(COLL[view]) return renderColl(view);
  const fn = { dash:vDash, gov:vGov, org:vOrg, lead:vLead, risk:vRisk, kpi:vKpi, isms:vIsms, aims:vAims, map:vMap, settings:vSettings }[view];
  m.innerHTML = fn ? fn() : '<div class="empty">找不到頁面</div>';
}
function hdr(cl, title, desc, wk){ return `<div class="top"><div><div class="cl">${cl}</div><h2>${title}</h2><div class="desc">${desc||''}</div></div>${wk?`<span class="wk">📅 ${wk}</span>`:''}</div>`; }

/* ───────── 通用集合頁 ───────── */
function renderColl(id){
  const c = COLL[id], rows = S[id] || [];
  const cols = c.fields.filter(f => f.col);
  let h = hdr(`第 ${c.clause} 條`, `${ICONS[id]} ${c.title}`, c.desc, c.week);
  h += `<div class="bar"><button class="btn p" onclick="openForm('${id}')">＋ 新增</button><span class="sp"></span><span class="hint" style="margin:0">${rows.length} 筆</span></div>`;
  if(id==='ip') h += ipPipeline(rows);
  if(id==='initiatives') h += initPipeline(rows);
  if(!rows.length) h += `<div class="empty">還沒有資料。按「＋ 新增」開始，或到 ⚙️ 設定載入示範組織看看填滿是什麼樣子。</div>`;
  else {
    h += `<div class="card" style="padding:6px 8px;overflow:auto"><table><thead><tr>${cols.map(f=>`<th>${f.l}</th>`).join('')}<th></th></tr></thead><tbody>`;
    rows.forEach(r => {
      h += `<tr>${cols.map(f=>`<td>${cell(id,f,r[f.k])}</td>`).join('')}<td class="act"><button class="btn sm" onclick="openForm('${id}',${r.id})">編輯</button> <button class="btn sm d" onclick="del('${id}',${r.id})">刪</button></td></tr>`;
    });
    h += `</tbody></table></div>`;
  }
  $('#main').innerHTML = h;
}
function cell(id, f, v){
  if(v==null||v==='') return '<span style="color:#c4c8d0">—</span>';
  if(f.k==='status'||f.k==='impact'||f.k==='relevance'||f.k==='level'||f.k==='value'||f.k==='stage'||f.k==='portfolio'||f.k==='type'&&id==='issues'||f.k==='result'){
    const cls = /已達成|已完成|已驗證|符合$|已部署|高|核心|機會|運用/.test(v)?'ok':/未達成|不符合|中止|取消|風險|低/.test(v)?'bad':/進行中|處理中|審查中|中|重要|兩者/.test(v)?'warn':'';
    return `<span class="pill ${cls}">${esc(v)}</span>`;
  }
  return esc(v);
}
let editing = null;
function openForm(id, rid){
  const c = COLL[id]; const r = rid!=null ? (S[id].find(x=>x.id===rid)||{}) : {};
  editing = {id, rid};
  $('#mTitle').textContent = (rid!=null?'編輯：':'新增：') + c.title;
  $('#mBody').innerHTML = `<div class="form">${c.fields.map(f => `<div class="${f.full?'full':''}"><label>${f.l}</label>${input(f, r[f.k])}</div>`).join('')}</div>`;
  $('#modal').classList.add('on');
  const first = $('#mBody input,#mBody textarea,#mBody select'); if(first) first.focus();
}
function input(f, v){
  v = v ?? '';
  if(f.t==='textarea') return `<textarea name="${f.k}">${esc(v)}</textarea>`;
  if(f.t==='select') return `<select name="${f.k}">${f.o.map(o=>`<option ${o===v?'selected':''}>${o}</option>`).join('')}</select>`;
  return `<input name="${f.k}" type="${f.t==='date'?'date':f.t==='number'?'number':'text'}" value="${esc(v)}">`;
}
function saveForm(){
  const {id, rid} = editing; const c = COLL[id]; const o = {};
  c.fields.forEach(f => { const el = $(`#mBody [name="${f.k}"]`); o[f.k] = el ? el.value.trim() : ''; });
  if(rid!=null){ const i = S[id].findIndex(x=>x.id===rid); S[id][i] = Object.assign({}, S[id][i], o); }
  else { o.id = Date.now(); S[id].push(o); }
  save(); closeModal(); render(); toast('已儲存');
}
function del(id, rid){ if(!confirm('確定刪除這筆？')) return; S[id] = S[id].filter(x=>x.id!==rid); save(); render(); }
function closeModal(){ $('#modal').classList.remove('on'); editing=null; }

/* ───────── 8.x 智財管線 / 創新過程管線 ───────── */
function ipPipeline(rows){
  const st = COLL.ip.fields.find(f=>f.k==='stage').o;
  return `<div class="card"><h3><span class="cl">TIPS 0.2</span>權利管理流程</h3><div class="hint">提案 → 成果 → <b>取得（8.1）</b> → <b>保護（8.2）</b> → <b>維護（8.3）</b> → <b>運用（8.4）</b>。點卡片可編輯。</div><div class="pipe" style="grid-template-columns:repeat(6,1fr)">${st.map(s=>{const it=rows.filter(r=>r.stage===s);return `<div class="col"><h4>${s}<span>${it.length}</span></h4>${it.map(r=>`<div class="it" onclick="openForm('ip',${r.id})">${esc(r.name)}<div class="t">${esc(r.type)}${r.value?' · '+esc(r.value):''}</div></div>`).join('')}</div>`}).join('')}</div></div>`;
}
function initPipeline(rows){
  const st = COLL.initiatives.fields.find(f=>f.k==='stage').o;
  return `<div class="card"><h3><span class="cl">ISO 56002</span>創新過程</h3><div class="hint">辨識機會 → 創造概念 → 驗證概念 → 開發解決方案 → 部署。不是每個倡議都會變成創新——中止也是正常結果。</div><div class="pipe">${st.map(s=>{const it=rows.filter(r=>r.stage===s);return `<div class="col"><h4>${s}<span>${it.length}</span></h4>${it.map(r=>`<div class="it" onclick="openForm('initiatives',${r.id})">${esc(r.name)}<div class="t">${esc(r.portfolio)}組合 · ${esc(r.status)}</div></div>`).join('')}</div>`}).join('')}</div></div>`;
}

/* ───────── 4.3 組織 ───────── */
function vOrg(){
  const o = S.org;
  return hdr('第 4.3 / 4.3.1 條','🧭 適用範圍・願景・創新意圖','先決定系統管什麼（範圍），再從願景寫出創新意圖——「針對創新的宣示性抱負」，它是整條鏈的起點：機會領域＋願景 → 創新意圖 → 政策 → 策略 → 組合 → 倡議。','第4堂 10/16') +
  `<div class="card"><div class="form">
    <div><label>組織名稱</label><input id="o_name" value="${esc(o.name)}"></div>
    <div><label>產業</label><input id="o_industry" value="${esc(o.industry)}"></div>
    <div><label>實收資本額（元）</label><input id="o_capital" type="number" value="${esc(o.capital)}"></div>
    <div><label>公開發行狀態</label><select id="o_listed">${['未公開發行','公開發行','興櫃','上櫃','上市'].map(x=>`<option ${x===o.listed?'selected':''}>${x}</option>`).join('')}</select></div>
    <div><label>最高管理者</label><input id="o_topMgmt" value="${esc(o.topMgmt)}"></div>
    <div><label>最近一次向董事會報告智財管理計畫</label><input id="o_boardReportDate" type="date" value="${esc(o.boardReportDate)}"></div>
    <div class="full"><label>4.3 適用範圍（系統涵蓋哪些業務、地點、產品服務）</label><textarea id="o_scope">${esc(o.scope)}</textarea></div>
    <div class="full"><label>組織願景（希望成為或實現什麼）</label><textarea id="o_vision">${esc(o.vision)}</textarea></div>
    <div class="full"><label>4.3.1 創新意圖（例：數位轉型、組織更新、永續運作、健康工作環境、循環物料流、有吸引力的品牌）</label><textarea id="o_intent">${esc(o.intent)}</textarea></div>
  </div><div class="bar" style="margin-top:12px"><span class="sp"></span><button class="btn p" onclick="saveOrg()">儲存</button></div></div>`;
}
function saveOrg(){ ['name','industry','capital','listed','topMgmt','boardReportDate','scope','vision','intent'].forEach(k => S.org[k] = $('#o_'+k).value.trim()); save(); toast('已儲存'); }

/* ───────── 5 領導 ───────── */
const COMMIT = [
  {k:'c1',cl:'5.1',t:'確保智財／創新管理政策與目標已建立，且與組織策略方向一致'},
  {k:'c2',cl:'5.1',t:'確保系統要求已整合進組織的營運流程（不是另一套獨立文件）'},
  {k:'c3',cl:'5.1',t:'確保系統所需資源（人、時間、財務、基礎設施、知識）可取得'},
  {k:'c4',cl:'5.4',t:'倡導支持創新的文化：對變革開放、容許風險承擔、鼓勵協同合作'},
  {k:'c5',cl:'5.1',t:'指導並支持人員為系統有效性做出貢獻；指派權責'},
  {k:'c6',cl:'9.3',t:'主持管理審查，並就系統成效向董事會報告（治理實務守則 §37-2）'}
];
function vLead(){
  const L = S.leadership;
  return hdr('第 5.1–5.3 條','👑 管理階層承諾・政策・策略','最高管理者要「以身作則」展現承諾。政策由最高管理階層正式核定；策略回答「在哪裡創新、創新什麼、誰參與、要什麼資源、誰負責、何時完成、怎麼衡量」。','第6堂 10/30') +
  `<div class="grid2"><div class="card"><h3><span class="cl">5.1</span>管理階層承諾自評</h3>${COMMIT.map(c=>`<div class="chk"><input type="checkbox" ${L.commitment[c.k]?'checked':''} onchange="S.leadership.commitment['${c.k}']=this.checked;save()"><span class="cl">${c.cl}</span><div>${c.t}</div></div>`).join('')}</div>
  <div class="card"><h3><span class="cl">5.2</span>智財／創新管理政策</h3><div class="form"><div class="full"><label>政策全文</label><textarea id="p_text" style="min-height:150px">${esc(L.policy.text)}</textarea></div><div><label>版本</label><input id="p_version" value="${esc(L.policy.version)}"></div><div><label>核定者</label><input id="p_approver" value="${esc(L.policy.approver)}"></div><div><label>核定日期</label><input id="p_date" type="date" value="${esc(L.policy.date)}"></div></div><div class="bar" style="margin-top:10px"><span class="sp"></span><button class="btn p" onclick="saveLead()">儲存</button></div></div></div>
  <div class="card"><h3><span class="cl">5.3</span>創新策略（ISO 56000 備考 3 的八個選擇）</h3><div class="hint">重點領域・創新類型・誰參與・需要什麼（資源／結構／流程）・誰負責・何時完成・結果如何被監測量測評估・如何保護溝通記錄</div><textarea id="s_text" style="min-height:130px">${esc(L.strategy.text)}</textarea><div class="bar" style="margin-top:10px"><span class="sp"></span><button class="btn p" onclick="saveLead()">儲存</button></div></div>`;
}
function saveLead(){ S.leadership.policy = {text:$('#p_text').value.trim(), version:$('#p_version').value.trim(), approver:$('#p_approver').value.trim(), date:$('#p_date').value}; S.leadership.strategy = {text:$('#s_text').value.trim()}; save(); toast('已儲存'); }

/* ───────── 6.2 風險評鑑 ───────── */
const RF = [{k:'src',l:'風險來源',t:'text',col:1},{k:'desc',l:'風險描述（事件→後果）',t:'textarea',full:1,col:1},{k:'cat',l:'類別',t:'select',o:['智財','資安','AI','法遵','經營','人員','其他'],col:1},{k:'L',l:'可能性 1–5',t:'select',o:['1','2','3','4','5'],col:1},{k:'I',l:'衝擊 1–5',t:'select',o:['1','2','3','4','5'],col:1},{k:'treat',l:'處理方式',t:'select',o:['降低','避免','移轉','接受'],col:1},{k:'control',l:'控制措施',t:'textarea',full:1},{k:'owner',l:'負責人',t:'text',col:1},{k:'status',l:'狀態',t:'select',o:['待處理','處理中','監控中','已結案'],col:1}];
COLL.risks = {title:'風險登錄', clause:'6.2', week:'第5堂 10/23', desc:'', fields:RF};
function rLevel(r){ const s = (+r.L||0)*(+r.I||0); const c = S.riskCriteria; return s<=c.lowMax?{n:'低',c:'ok',l:1}:s<=c.midMax?{n:'中',c:'warn',l:2}:s<20?{n:'高',c:'bad',l:3}:{n:'極高',c:'bad',l:4}; }
function vRisk(){
  const rs = S.risks, c = S.riskCriteria;
  const cnt = {低:0,中:0,高:0,極高:0}; rs.forEach(r=>cnt[rLevel(r).n]++);
  let heat = `<div class="heat"><div></div>${[1,2,3,4,5].map(i=>`<div class="h">衝擊 ${i}</div>`).join('')}`;
  for(let L=5; L>=1; L--){ heat += `<div class="h" style="align-self:center">可能性 ${L}</div>`; for(let I=1;I<=5;I++){ const s=L*I; const lv = s<=c.lowMax?1:s<=c.midMax?2:s<20?3:4; const it = rs.filter(r=>+r.L===L&&+r.I===I); heat += `<div class="c l${lv}"><b>${s}</b>${it.map(r=>`<span title="${esc(r.desc)}">${esc(r.desc.slice(0,14))}</span>`).join('')}</div>`; } }
  heat += '</div>';
  return hdr('第 6.2 條','⚠️ 風險評鑑與處理','TIPS 6.2 四步驟：① 訂定風險評估準則 → ② 風險鑑別（來源與後果）→ ③ 風險分析（可能性×衝擊）→ ④ 風險評估（排優先次序）→ 處理（降低／避免／移轉／接受）。管理不確定性是八大原則之一。','第5堂 10/23') +
  `<div class="tiles"><div class="tile"><div class="v">${rs.length}</div><div class="k">登錄風險</div></div><div class="tile bad"><div class="v">${cnt.極高+cnt.高}</div><div class="k">高／極高</div></div><div class="tile warn"><div class="v">${cnt.中}</div><div class="k">中</div></div><div class="tile ok"><div class="v">${cnt.低}</div><div class="k">低</div></div><div class="tile acc"><div class="v">${rs.filter(r=>r.status==='已結案').length}</div><div class="k">已結案</div></div></div>
  <div class="grid2"><div class="card"><h3><span class="cl">① 準則</span>風險評估準則</h3><div class="hint">分數＝可能性×衝擊（1–25）。設定「低」與「中」的上限，其餘為高／極高（≥20）。</div><div class="form"><div><label>低 ≤</label><input type="number" id="rc_low" value="${c.lowMax}" min="1" max="24"></div><div><label>中 ≤</label><input type="number" id="rc_mid" value="${c.midMax}" min="2" max="24"></div></div><div class="bar" style="margin-top:10px"><span class="sp"></span><button class="btn" onclick="S.riskCriteria={lowMax:+$('#rc_low').value,midMax:+$('#rc_mid').value};save();render()">套用</button></div></div>
  <div class="card"><h3><span class="cl">③④</span>風險矩陣</h3>${heat}</div></div>
  <div class="bar"><button class="btn p" onclick="openForm('risks')">＋ 鑑別新風險</button><span class="sp"></span></div>
  ${rs.length?`<div class="card" style="padding:6px 8px;overflow:auto"><table><thead><tr><th>來源</th><th>風險</th><th>類別</th><th>L×I</th><th>等級</th><th>處理</th><th>控制措施</th><th>負責</th><th>狀態</th><th></th></tr></thead><tbody>${rs.slice().sort((a,b)=>(b.L*b.I)-(a.L*a.I)).map(r=>{const lv=rLevel(r);return `<tr><td>${esc(r.src)}</td><td>${esc(r.desc)}</td><td><span class="pill info">${esc(r.cat)}</span></td><td>${r.L}×${r.I}=${r.L*r.I}</td><td><span class="pill ${lv.c}">${lv.n}</span></td><td>${esc(r.treat)}</td><td style="font-size:12.5px;color:#4a4e58">${esc(r.control)}</td><td>${esc(r.owner)}</td><td>${cell('risks',{k:'status'},r.status)}</td><td class="act"><button class="btn sm" onclick="openForm('risks',${r.id})">編輯</button> <button class="btn sm d" onclick="del('risks',${r.id})">刪</button></td></tr>`}).join('')}</tbody></table></div>`:'<div class="empty">還沒有風險。從「內外部議題」裡標為風險的項目開始鑑別。</div>'}`;
}

/* ───────── 9.1 監督與量測 ───────── */
function pct(o){ const t=parseFloat(String(o.target).replace(/[^\d.]/g,'')), a=parseFloat(String(o.actual).replace(/[^\d.]/g,'')); if(o.status==='已達成') return 100; if(isNaN(t)||isNaN(a)||!t) return null; return Math.min(100, Math.round(100*a/t)); }
function vKpi(){
  const os = S.objectives;
  return hdr('第 9.1 條','📈 監督、量測、分析與評估','要監督什麼、用什麼方法、何時做、何時分析。目標達成率直接來自「創新／智財目標」的 KPI；風險、稽核、不符合的狀態也在這裡一眼看完。','第7堂 11/6') +
  `<div class="card"><h3><span class="cl">目標</span>KPI 達成情形</h3>${os.length?os.map(o=>{const p=pct(o);return `<div style="margin-bottom:12px"><div style="display:flex;justify-content:space-between;font-size:13.5px"><span><b>${esc(o.name)}</b> <span class="hint" style="display:inline">${esc(o.kpi)}</span></span><span>${esc(o.actual)} / ${esc(o.target)} ${p!=null?`<b style="color:${p>=100?'#1f9d55':p>=60?'#e0a300':'#d03b3b'}">${p}%</b>`:''} ${cell('',{k:'status'},o.status)}</span></div><div class="prog"><i style="width:${p??0}%"></i></div><div class="hint" style="margin:0">負責 ${esc(o.owner)} · 期限 ${esc(o.due)}</div></div>`}).join(''):'<div class="empty">先到「創新／智財目標」建立目標與 KPI。</div>'}</div>
  <div class="grid3">${stat('風險',S.risks.length,`高／極高 ${S.risks.filter(r=>rLevel(r).l>=3).length}`)}${stat('不符合',S.ncs.length,`未結案 ${S.ncs.filter(n=>!/已完成|已驗證/.test(n.status)).length}`)}${stat('文件逾期審查',S.docs.filter(d=>d.review&&d.review<today()).length,'需要更新版本')}</div>`;
}
function stat(k,v,s){ return `<div class="tile"><div class="v">${v}</div><div class="k">${k}</div><div class="s">${s}</div></div>`; }

/* ───────── 儀表板 ───────── */
function completeness(){
  const chk = [
    ['4 組織全景', [S.org.scope, S.org.intent, S.issues.length, S.stakeholders.length, S.areas.length], 'P'],
    ['5 領導', [S.leadership.policy.text, S.leadership.strategy.text, S.roles.length, Object.values(S.leadership.commitment).filter(Boolean).length>=4], 'P'],
    ['6 規劃', [S.risks.length, S.objectives.length, S.initiatives.length], 'P'],
    ['7 支援', [S.resources.length, S.competence.length, S.comms.length, S.docs.length], 'D'],
    ['8 運作', [S.ip.length, S.ip.some(i=>i.stage==='保護'), S.ip.some(i=>i.stage==='運用'), S.initiatives.length], 'D'],
    ['9 績效評估', [S.objectives.some(o=>o.actual), S.audits.length, S.reviews.length], 'C'],
    ['10 改善', [S.ncs.length, S.improvements.length], 'A']
  ];
  return chk.map(([n,a,q]) => ({n, q, p: Math.round(100*a.filter(Boolean).length/a.length)}));
}
function esgS10(){
  const y = new Date(); y.setFullYear(y.getFullYear()-1); const yr = y.toISOString().slice(0,10);
  return [
    ['已制訂智財管理政策（5.2）', !!S.leadership.policy.text],
    ['智財管理目標與營運目標連結（6.3）', S.objectives.length>0],
    ['智財管理計畫執行情形可追蹤（KPI 有目前值）', S.objectives.some(o=>o.actual)],
    ['一年內向董事會報告', !!S.org.boardReportDate && S.org.boardReportDate>=yr],
    ['智財登錄涵蓋取得／保護／維護／運用', S.ip.length>0],
    ['一年內執行內部稽核（9.2）', S.audits.some(a=>a.date>=yr)],
    ['一年內完成管理審查（9.3）', S.reviews.some(r=>r.date>=yr)],
    ['加分：導入 TIPS／ISO 56001 並經第三方驗證', false]
  ];
}
function vDash(){
  const comp = completeness(); const all = Math.round(comp.reduce((a,c)=>a+c.p,0)/comp.length);
  const pd = q => { const c = comp.filter(x=>x.q===q); return Math.round(c.reduce((a,x)=>a+x.p,0)/c.length); };
  const s10 = esgS10(); const s10n = s10.filter(x=>x[1]).length;
  const hi = S.risks.filter(r=>rLevel(r).l>=3);
  const ipStage = {}; S.ip.forEach(i=>ipStage[i.stage]=(ipStage[i.stage]||0)+1);
  const overdue = S.ncs.filter(n=>n.due&&n.due<today()&&!/已完成|已驗證/.test(n.status));
  return hdr('創新治理 × 公司治理','🏛 治理儀表板',`${S.org.name?esc(S.org.name)+' · ':''}最高管理者一眼看：系統建置到哪、風險在哪、智財在哪個階段、董事會要的東西備齊了沒。`) +
  (S.org.name?'':`<div class="card" style="border-color:#f0d68a;background:#fffbea"><b>還沒有組織資料。</b> 到 <a href="#org" onclick="go('org')">🧭 範圍・願景・創新意圖</a> 開始建置，或到 <a href="#settings" onclick="go('settings')">⚙️ 設定</a> 載入示範組織（音樂 NFT 授權平台）。</div>`) +
  `<div class="pdca"><div class="q P"><h4>PLAN</h4><div class="n">${pd('P')}%</div><div class="s">4 組織全景・5 領導・6 規劃</div></div><div class="q D"><h4>DO</h4><div class="n">${pd('D')}%</div><div class="s">7 支援・8 運作</div></div><div class="q C"><h4>CHECK</h4><div class="n">${pd('C')}%</div><div class="s">9 績效評估</div></div><div class="q A"><h4>ACT</h4><div class="n">${pd('A')}%</div><div class="s">10 改善</div></div></div>
  <div class="grid2" style="margin-top:16px"><div class="card"><h3>系統建置完成度 <span class="pill gold">${all}%</span></h3>${comp.map(c=>`<div style="display:flex;justify-content:space-between;font-size:13px"><span>${c.n}</span><span>${c.p}%</span></div><div class="prog"><i style="width:${c.p}%"></i></div>`).join('')}</div>
  <div class="card"><h3>ESG 評鑑 S-10 智財管理 <span class="pill ${s10n>=7?'ok':s10n>=4?'warn':'bad'}">${s10n}/8</span></h3>${s10.map(x=>`<div class="chk" style="padding:5px 0"><span style="width:18px">${x[1]?'✅':'⬜️'}</span><div style="font-size:13px">${x[0]}</div></div>`).join('')}<div class="hint" style="margin-top:8px">S-12 資通安全 → 待 ISMS 模組（第 8–9 堂）</div></div></div>
  <div class="tiles"><div class="tile ${hi.length?'bad':'ok'}"><div class="v">${hi.length}</div><div class="k">高／極高風險</div><div class="s">共 ${S.risks.length} 項</div></div><div class="tile acc"><div class="v">${S.ip.length}</div><div class="k">智財資產</div><div class="s">${Object.entries(ipStage).map(([k,v])=>`${k}${v}`).join(' · ')||'—'}</div></div><div class="tile"><div class="v">${S.initiatives.filter(i=>i.status==='進行中').length}</div><div class="k">進行中創新倡議</div><div class="s">共 ${S.initiatives.length} 項</div></div><div class="tile ${overdue.length?'bad':''}"><div class="v">${overdue.length}</div><div class="k">逾期矯正措施</div><div class="s">不符合共 ${S.ncs.length}</div></div><div class="tile"><div class="v">${S.objectives.filter(o=>o.status==='已達成').length}/${S.objectives.length}</div><div class="k">目標已達成</div></div></div>
  ${hi.length?`<div class="card"><h3>⚠️ 需要最高管理者關注的風險</h3><table><thead><tr><th>風險</th><th>類別</th><th>等級</th><th>控制措施</th><th>負責</th></tr></thead><tbody>${hi.map(r=>`<tr><td>${esc(r.desc)}</td><td>${esc(r.cat)}</td><td><span class="pill bad">${rLevel(r).n}</span></td><td style="font-size:12.5px">${esc(r.control)}</td><td>${esc(r.owner)}</td></tr>`).join('')}</tbody></table></div>`:''}
  <div class="card"><h3>創新意圖指導鏈</h3><div class="hint">機會領域＋願景 → 4.3.1 創新意圖 → 5.2 政策 → 5.3 策略 → 6.4 組合 → 8.2 倡議 → 8.x 智財</div><table><tbody>
  <tr><td style="white-space:nowrap"><b>機會領域</b></td><td>${S.areas.map(a=>`<span class="pill">${esc(a.theme)}</span>`).join(' ')||'—'}</td></tr>
  <tr><td><b>創新意圖</b></td><td>${esc(S.org.intent)||'—'}</td></tr>
  <tr><td><b>政策</b></td><td>${S.leadership.policy.text?`已核定 ${esc(S.leadership.policy.version)}（${esc(S.leadership.policy.approver)} ${esc(S.leadership.policy.date)}）`:'—'}</td></tr>
  <tr><td><b>創新組合</b></td><td>${['探索','開發','部署'].map(p=>`<span class="pill info">${p} ${S.initiatives.filter(i=>i.portfolio===p).length}</span>`).join(' ')}</td></tr>
  <tr><td><b>智財成果</b></td><td>${S.ip.filter(i=>i.initiative).length} 項智財可回溯至倡議</td></tr></tbody></table></div>`;
}

/* ───────── 治理輸出（法規對接） ───────── */
function vGov(){
  const o = S.org; const cap = +o.capital||0;
  return hdr('公司治理對接','📋 治理輸出・董事會報告','把系統裡的資料，變成董事會與法規要的東西：ESG 評鑑、內控準則、取得處分資產準則、年報揭露、治理實務守則。這一頁就是「Level 3 公司治理」。') +
  `<div class="grid2">
  <div class="card"><h3><span class="cl">§11</span>取得或處分無形資產：會計師意見門檻試算</h3><div class="hint">公開發行公司取得或處分資產處理準則 §3 無形資產（專利、著作、商標、特許權）適用；§11 交易金額達<b>實收資本額 20%</b> 或 <b>新臺幣 3 億元</b>以上者，應於事實發生日前洽請會計師就交易價格合理性表示意見（與國內政府機關交易除外）。</div>
  <div class="form"><div><label>實收資本額（元）</label><input id="g_cap" type="number" value="${cap||''}"></div><div><label>交易金額（元）</label><input id="g_amt" type="number" placeholder="例如 400000000"></div><div class="full"><label><input type="checkbox" id="g_gov" style="width:auto;margin-right:6px">與國內政府機關交易</label></div></div>
  <div class="bar" style="margin-top:8px"><button class="btn p" onclick="calc11()">試算</button></div><div class="calc-out" id="g_out">輸入金額後試算。</div>
  <div class="hint" style="margin-top:10px"><b>§6 程序：</b>處理程序須經董事會通過 → 送各監察人（審計委員會）→ 提報股東會同意；修正時亦同。</div></div>
  <div class="card"><h3><span class="cl">§7</span>內控制度處理準則：研發循環檢核</h3><div class="hint">研發循環應涵蓋以下政策及程序。系統對應項目自動判斷。</div>
  ${[['基礎研究、產品設計、技術研發、試作與測試',S.initiatives.length>0,'8.2 創新倡議'],['研發紀錄與文件保管',S.docs.some(d=>/研發紀錄|紀錄/.test(d.title)),'7.4 文件 / 8.1'],['智慧財產權取得政策及程序',S.ip.some(i=>/取得|提案|成果/.test(i.stage))||S.docs.some(d=>/取得|程序/.test(d.title)),'8.1'],['智慧財產權維護政策及程序',S.ip.some(i=>i.stage==='維護'),'8.3'],['智慧財產權運用政策及程序',S.ip.some(i=>i.stage==='運用'),'8.4'],['年度稽核計畫含研發循環，經董事會通過（§13）',S.audits.length>0,'9.2']].map(x=>`<div class="chk" style="padding:5px 0"><span style="width:18px">${x[1]?'✅':'⬜️'}</span><div style="font-size:13px">${x[0]}<div class="d">${x[2]}</div></div></div>`).join('')}</div></div>
  <div class="card"><h3><span class="cl">§37-2</span>上市上櫃公司治理實務守則：董事會智財 PDCA 對照</h3><table class="map"><thead><tr><th>守則要求</th><th>系統對應</th><th>狀態</th></tr></thead><tbody>
  ${[['制訂與營運策略連結之智財政策與目標','5.2 政策 / 6.3 目標',!!S.leadership.policy.text&&S.objectives.length>0],['建立取得、保護、維護與運用制度','8.1–8.4 智財流程',S.ip.length>0],['提供所需資源','7.1 資源',S.resources.length>0],['因應風險與機會','6.2 風險評鑑',S.risks.length>0],['董事會評估與監督智財經營方向與績效','9.3 管理審查 / 董事會報告',S.reviews.length>0],['持續改善','10.2–10.3',S.improvements.length>0||S.ncs.length>0]].map(x=>`<tr><td>${x[0]}</td><td>${x[1]}</td><td>${x[2]?'<span class="pill ok">已建立</span>':'<span class="pill bad">缺</span>'}</td></tr>`).join('')}</tbody></table>
  <div class="hint" style="margin-top:8px"><b>誠信經營守則 §7 II：</b>防範方案至少涵蓋侵害營業秘密、商標、專利、著作權之防範措施——對應 6.2 智財類風險 ${S.risks.filter(r=>r.cat==='智財').length} 項、8.2 保護階段智財 ${S.ip.filter(i=>i.stage==='保護').length} 項。</div></div>
  <div class="bar"><button class="btn g" onclick="$('#rep').style.display='block';$('#rep').scrollIntoView({behavior:'smooth'})">📄 產生董事會年度智財管理報告（ESG S-10）</button><button class="btn" onclick="window.print()">🖨 列印／存 PDF</button></div>
  <div id="rep" style="display:none">${boardReport()}</div>`;
}
function calc11(){
  const cap=+$('#g_cap').value||0, amt=+$('#g_amt').value||0, gov=$('#g_gov').checked;
  if(cap) { S.org.capital = cap; save(); }
  const th20 = cap*0.2, hit20 = cap && amt>=th20, hit3 = amt>=3e8;
  let h = `交易金額 <b>${amt.toLocaleString()}</b> 元；實收資本額 20% ＝ <b>${th20.toLocaleString()}</b> 元；法定門檻 3 億元。<br>`;
  if(!amt) h='請輸入交易金額。';
  else if(gov) h += `→ 與國內政府機關交易，<b>免</b>洽請會計師表示意見（§11 但書）。仍須依 §6 程序辦理並依規定公告申報。`;
  else if(hit20||hit3) h += `→ ${hit20?'達實收資本額 20%':''}${hit20&&hit3?'且':''}${hit3?'達 3 億元':''}，<b>應於事實發生日前洽請會計師就交易價格合理性表示意見</b>（§11）。另請確認：處理程序已依 §6 經董事會→監察人→股東會；董事會決議；年報 §18 揭露重要契約。`;
  else h += `→ 未達門檻，<b>不須</b>會計師意見；仍應依公司取得或處分資產處理程序辦理（§6）。`;
  $('#g_out').innerHTML = h;
}
function boardReport(){
  const o=S.org, L=S.leadership, yr=new Date().getFullYear();
  const byStage = s => S.ip.filter(i=>i.stage===s);
  return `<div class="report"><h1>${esc(o.name)||'（組織名稱）'}</h1><div class="meta">${yr} 年度智慧財產管理計畫執行情形報告（董事會）· 依 ESG 評鑑指標 S-10 與公司治理實務守則 §37-2 編製 · ${today()}</div>
  <h2>一、智財管理政策與制度</h2><p>${esc(L.policy.text)||'（尚未制訂政策）'}</p><p>政策版本 ${esc(L.policy.version)||'—'}，${esc(L.policy.approver)||'—'} 於 ${esc(L.policy.date)||'—'} 核定。本公司依 TIPS／ISO 56001 架構建立創新治理管理系統，適用範圍：${esc(o.scope)||'—'}</p>
  <h2>二、與營運目標連結之智財管理目標及執行情形</h2><table><thead><tr><th>目標</th><th>KPI</th><th>目標值</th><th>目前值</th><th>狀態</th></tr></thead><tbody>${S.objectives.map(x=>`<tr><td>${esc(x.name)}</td><td>${esc(x.kpi)}</td><td>${esc(x.target)}</td><td>${esc(x.actual)}</td><td>${esc(x.status)}</td></tr>`).join('')||'<tr><td colspan="5">—</td></tr>'}</tbody></table>
  <h2>三、智慧財產資產概況（取得・保護・維護・運用）</h2><ul><li>取得中（提案／成果／申請）：${byStage('提案').length+byStage('成果').length+byStage('取得').length} 項 — ${[...byStage('提案'),...byStage('成果'),...byStage('取得')].map(i=>esc(i.name)).join('、')||'—'}</li><li>保護中（營業秘密等）：${byStage('保護').length} 項</li><li>維護中（已取得權利）：${byStage('維護').length} 項 — ${byStage('維護').map(i=>esc(i.name)).join('、')||'—'}</li><li>運用中（授權／技轉）：${byStage('運用').length} 項 — ${byStage('運用').map(i=>esc(i.name)+(i.note?'（'+esc(i.note)+'）':'')).join('、')||'—'}</li></ul>
  <h2>四、創新組合與研發概況（年報準則 §18 參考）</h2><ul>${S.initiatives.map(i=>`<li>${esc(i.name)}：${esc(i.stage)}，${esc(i.portfolio)}組合，預算 ${esc(i.budget)||'—'}</li>`).join('')||'<li>—</li>'}</ul>
  <h2>五、智財與創新相關風險及處置（年報準則 §20 參考）</h2><table><thead><tr><th>風險</th><th>等級</th><th>處理</th><th>控制措施</th></tr></thead><tbody>${S.risks.filter(r=>rLevel(r).l>=2).sort((a,b)=>b.L*b.I-a.L*a.I).map(r=>`<tr><td>${esc(r.desc)}</td><td>${rLevel(r).n}</td><td>${esc(r.treat)}</td><td>${esc(r.control)}</td></tr>`).join('')||'<tr><td colspan="4">—</td></tr>'}</tbody></table>
  <h2>六、內部稽核與管理審查</h2><ul>${S.audits.map(a=>`<li>${esc(a.date)} 內部稽核（${esc(a.scope)}）：${esc(a.result)}</li>`).join('')}${S.reviews.map(r=>`<li>${esc(r.date)} 管理審查（${esc(r.chair)}）：${esc(r.decisions)}</li>`).join('')||'<li>—</li>'}</ul>
  <h2>七、不符合事項與改善</h2><ul>${S.ncs.map(n=>`<li>${esc(n.desc)} → ${esc(n.action)}（${esc(n.status)}）</li>`).join('')}${S.improvements.map(i=>`<li>${esc(i.date)} ${esc(i.desc)}：${esc(i.effect)}</li>`).join('')||'<li>—</li>'}</ul>
  <h2>八、資源投入與下年度計畫</h2><ul>${S.resources.map(r=>`<li>${esc(r.kind)}：${esc(r.desc)} ${esc(r.amount)}</li>`).join('')||'<li>—</li>'}</ul><p>下年度：依管理審查決議推動；評估導入第三方驗證（TIPS／ISO 56001）以取得 ESG 評鑑 S-10 加分；資通安全（S-12）納入 ISMS 導入計畫。</p>
  <p style="margin-top:18px;text-align:right">報告人：${esc((S.roles.find(r=>/智財/.test(r.role))||{}).person)||'（智財管理主管）'}　　最高管理者：${esc(o.topMgmt)||'—'}</p></div>`;
}

/* ───────── ISMS / AIMS 骨架 ───────── */
function vIsms(){
  return hdr('ISO/IEC 27001:2022','🔐 資訊安全管理系統（ISMS）','創新支援系統之一。同一個協調架構第 4–10 章，只是「風險」換成資訊安全風險、「運作」換成 Annex A 控制措施。對應 ESG 評鑑 S-12。','第8–9堂 11/13・11/20') +
  `<div class="lockbox">🔒 課程第 8–9 堂才會教到。骨架已預留，講義到了就把這裡長出來。</div>
  <div class="card" style="margin-top:16px"><h3>預計模組</h3><table class="map"><tbody>
  <tr><td>4 組織全景</td><td>沿用本系統的內外部議題與利害關係人，加上資訊資產盤點</td></tr>
  <tr><td>5 領導</td><td>資訊安全政策（與智財政策同層級核定）</td></tr>
  <tr><td>6.1.2 資安風險評鑑</td><td>沿用 6.2 風險登錄，類別＝資安；加上資產—威脅—弱點三元組</td></tr>
  <tr><td>6.1.3 風險處理 / 適用性聲明（SoA）</td><td>Annex A 93 項控制措施（組織 37・人員 8・實體 14・技術 34）逐項適用／不適用與理由</td></tr>
  <tr><td>8 運作</td><td>控制措施實施紀錄；與 TIPS 8.2 機密管理共用（資訊系統、AI 開發工具）</td></tr>
  <tr><td>9 / 10</td><td>共用內部稽核、管理審查、不符合</td></tr>
  <tr><td>治理輸出</td><td>ESG S-12：資通安全風險管理架構、政策、具體管理方案、投入資源；上市櫃公司資通安全管理辦法（資安長、資安人員）</td></tr></tbody></table>
  <div class="hint">目前風險登錄中資安類風險：${S.risks.filter(r=>r.cat==='資安').length} 項——導入 ISMS 時直接接手。</div></div>`;
}
function vAims(){
  return hdr('ISO/IEC 42001:2023','🤖 人工智慧管理系統（AIMS）','創新支援系統之一。AI 已經是基礎設施（7.1.5 開發工具）也是風險來源（AI 生成內容的著作權、訓練資料授權）。同一骨架，加上 AI 影響評估。','第10堂 11/27') +
  `<div class="lockbox">🔒 課程第 10 堂才會教到。骨架已預留。</div>
  <div class="card" style="margin-top:16px"><h3>預計模組</h3><table class="map"><tbody>
  <tr><td>4 組織全景</td><td>組織在 AI 系統中的角色（提供者／使用者／開發者）</td></tr>
  <tr><td>5 領導</td><td>AI 政策（負責任 AI 原則：透明、公平、可問責、安全）</td></tr>
  <tr><td>6.1.2–6.1.4</td><td>AI 風險評鑑、AI 系統影響評估（對個人、群體、社會）</td></tr>
  <tr><td>8 運作</td><td>AI 系統生命週期管理、資料管理（訓練資料授權 ← 接 TIPS 8.4 運用）</td></tr>
  <tr><td>Annex A</td><td>控制目標與控制措施；Annex B 實施指引</td></tr>
  <tr><td>與智財的交會</td><td>AI 生成物權利歸屬、訓練資料授權、AI 開發工具產出的程式碼權利與機密</td></tr></tbody></table>
  <div class="hint">目前風險登錄中 AI 類風險：${S.risks.filter(r=>r.cat==='AI').length} 項。</div></div>`;
}

/* ───────── 標準對照表 ───────── */
function vMap(){
  const rows = [
    ['4 組織環境','4.1 內外部議題 / 4.2 利害關係人','4.1–4.4（含 4.3.1 創新意圖、機會領域）','4.1–4.4','4.1–4.4','第4堂','issues'],
    ['5 領導','5.1 承諾 / 5.2 政策 / 5.3 目標 / 5.4 權責與溝通','5.1–5.4（含 5.4 文化）','5.1–5.3','5.1–5.3','第6堂','lead'],
    ['6 規劃','6.1 基本要求 / 6.2 風險與機會 / 6.3 變更','6.1–6.6（創新組合 6.4、組織結構 6.5、協同合作 6.6）','6.1 風險評鑑處理 / 6.2 目標','6.1 風險與影響評估 / 6.2 目標','第5堂','risk'],
    ['7 支援','7.1 資源 / 7.2 能力 / 7.3 溝通 / 7.4 文件化','7.1（人員時間財務基礎設施知識）–7.5','7.1–7.5','7.1–7.5','第8堂','resources'],
    ['8 運作','8.1 取得 / 8.2 保護 / 8.3 維護 / 8.4 運用','8.1 規劃管制 / 8.2 創新倡議 / 8.3 創新過程','8.1–8.3 資安風險處理','8.1–8.4 AI 影響評估','第1–3堂','ip'],
    ['9 績效評估','9.1 監督評估分析 / 9.2 內部稽核 / 9.3 管理審查','9.1–9.3','9.1–9.3','9.1–9.3','第7堂','kpi'],
    ['10 改善','10.1 基本要求 / 10.2 矯正 / 10.3 持續改善','10.1–10.2','10.1–10.2','10.1–10.2','第7堂','ncs']
  ];
  return hdr('Harmonized Structure（Annex SL）','🗺 標準對照表','ISO 管理系統標準統一 10 章（2012/4 Annex SL 首次公告，現行版 2025/7/30）。TIPS 以 ISO 9001 PDCA 為基礎，章節同構。這張表就是本系統為什麼能同時裝下智財、創新、資安、AI 四套系統的理由（TIPS 0.6 與其他管理系統之相容性）。') +
  `<div class="card" style="overflow:auto"><table class="map"><thead><tr><th>協調架構</th><th>TIPS 2016</th><th>ISO 56001:2024</th><th>ISO/IEC 27001:2022</th><th>ISO/IEC 42001:2023</th><th>課程</th><th>本系統</th></tr></thead><tbody>${rows.map(r=>`<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td><td class="week">${r[5]}</td><td><a href="#${r[6]}" onclick="go('${r[6]}')">→ 開啟</a></td></tr>`).join('')}</tbody></table></div>
  <div class="grid2"><div class="card"><h3>PDCA 對應</h3><table class="map"><tbody><tr><td>Plan</td><td>4 組織環境・5 領導・6 規劃（7 支援）</td></tr><tr><td>Do</td><td>7 支援・8 運作</td></tr><tr><td>Check</td><td>9 績效評估</td></tr><tr><td>Act</td><td>10 改善</td></tr></tbody></table></div>
  <div class="card"><h3>ISO 56000 八大創新管理原則 → 系統哪裡體現</h3><table class="map"><tbody><tr><td>價值之實現</td><td>8.4 運用・9.1 KPI</td></tr><tr><td>著眼未來的領導者</td><td>5.1 承諾・4.3.1 創新意圖</td></tr><tr><td>策略方向</td><td>5.3 策略・6.3 目標</td></tr><tr><td>文化</td><td>5.4 承諾自評 c4・7.2 能力</td></tr><tr><td>開發運用洞察</td><td>4.1 議題・4.2 利害關係人・機會領域</td></tr><tr><td>管理不確定性</td><td>6.2 風險評鑑・8.2 倡議的不確定性欄</td></tr><tr><td>可調適性</td><td>9.3 管理審查・10.3 持續改善</td></tr><tr><td>系統方法</td><td>整個協調架構</td></tr></tbody></table></div></div>`;
}

/* ───────── 設定 ───────── */
function vSettings(){
  return hdr('','⚙️ 設定・匯出匯入','資料只存在這台瀏覽器的 localStorage。定期匯出 JSON 備份；換裝置就匯入。') +
  `<div class="grid2"><div class="card"><h3>示範組織</h3><p class="hint">載入「鏈譜音樂科技」——一家（虛構的）音樂 NFT 授權平台，把七章全部填滿，看看一套創新治理管理系統跑起來的樣子。會覆蓋目前資料。</p><button class="btn g" onclick="loadDemo()">🎼 載入示範組織</button></div>
  <div class="card"><h3>備份</h3><div class="bar"><button class="btn p" onclick="exportJson()">⬇️ 匯出 JSON</button><label class="btn" style="display:inline-block">⬆️ 匯入 JSON<input type="file" accept=".json" style="display:none" onchange="importJson(this)"></label><button class="btn d" onclick="if(confirm('清空全部資料？'))\{S=EMPTY();save();render();\}">🗑 清空</button></div></div></div>
  <div class="card"><h3>關於這套系統</h3><p class="hint" style="font-size:13.5px">IGS（Innovation Governance System）是把「智財管理 → 創新治理 → 公司治理」三個層級做成一套可操作的系統：骨架用 ISO 協調架構第 4–10 章（＝TIPS 2016 章節＝ISO 56001＝PDCA），運作層放 TIPS 的權利管理流程與 ISO 56002 的創新過程，治理輸出層對接台灣公開發行公司的內控準則、取得處分資產準則、年報準則、治理實務守則與 ESG 評鑑 S-10／S-12。資安（ISO 27001）與 AI（ISO 42001）模組掛在同一骨架上。<br>由 Elaine Chi 於陽明交大科法所「公司治理之創新與資安管理實踐」課程（115 上）逐週建置。</p></div>`;
}
function loadDemo(){ if(!confirm('載入示範資料會覆蓋目前內容，確定？')) return; S = Object.assign(EMPTY(), JSON.parse(JSON.stringify(window.IGS_DEMO))); save(); go('dash'); toast('已載入示範組織'); }
function exportJson(){ const a=document.createElement('a'); a.href='data:application/json;charset=utf-8,'+encodeURIComponent(JSON.stringify(S,null,2)); a.download=`igs-${(S.org.name||'backup')}-${today()}.json`; a.click(); }
function importJson(inp){ const f=inp.files[0]; if(!f) return; const r=new FileReader(); r.onload=()=>{ try{ S=Object.assign(EMPTY(), JSON.parse(r.result)); save(); go('dash'); toast('已匯入'); }catch(e){ alert('JSON 格式錯誤'); } }; r.readAsText(f); }

/* ───────── init ───────── */
document.addEventListener('keydown', e => { if(e.key==='Escape') closeModal(); if((e.metaKey||e.ctrlKey)&&e.key==='Enter'&&editing) saveForm(); });
renderSide(); render();
