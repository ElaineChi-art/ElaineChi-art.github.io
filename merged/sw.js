/* 合併版 Service Worker v2：HTML / JS / JSON 一律只走網路最新（永不提供舊版），
   其他靜態資源才快取。並在啟用時清掉舊版快取，解決「主畫面 App 卡舊版」。 */
const CACHE = 'lex-cache-v2';

self.addEventListener('install', () => { self.skipWaiting(); });

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.map(k => (k !== CACHE ? caches.delete(k) : null)));  // 清掉所有舊快取
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;

  const p = url.pathname;
  // 程式檔（頁面/HTML/JS/JSON）→ 只走網路，永遠最新；離線才退回快取
  const isCode = req.mode === 'navigate' || p.endsWith('/') ||
                 p.endsWith('.html') || p.endsWith('.js') || p.endsWith('.json');

  e.respondWith((async () => {
    try {
      const res = await fetch(req, { cache: 'no-store' });
      if (!isCode && res && res.ok) {                 // 只快取圖片等靜態資源，不快取程式檔
        const c = await caches.open(CACHE);
        c.put(req, res.clone());
      }
      return res;
    } catch (err) {
      const cached = await caches.match(req);
      if (cached) return cached;
      throw err;
    }
  })());
});
