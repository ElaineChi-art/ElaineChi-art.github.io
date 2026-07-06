/* 合併版 Service Worker：網路優先（永遠先抓最新，離線才用快取）。
   讓所有裝置（含 iPhone 主畫面圖示）都能自動更新到最新版，且不會卡在舊版。 */
const CACHE = 'lex-cache-v1';

self.addEventListener('install', () => { self.skipWaiting(); });   // 新版立即就位

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.map(k => (k !== CACHE ? caches.delete(k) : null)));
    await self.clients.claim();                                    // 立即接管所有頁面
  })());
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;                      // 只管自家資源

  // 網路優先：永遠先拿最新版；成功就順便更新快取；離線時才退回快取
  e.respondWith((async () => {
    try {
      const res = await fetch(req, { cache: 'no-store' });
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy)).catch(() => {});
      }
      return res;
    } catch (err) {
      const cached = await caches.match(req);
      if (cached) return cached;
      throw err;
    }
  })());
});
