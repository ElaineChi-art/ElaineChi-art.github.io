/* 自我移除版 Service Worker：解除註冊、清掉所有快取、讓頁面重新載入最新版。
   目的：移除先前加入的 SW（它可能造成主畫面 App 卡舊版），還原成單純的版本檢查自動更新。
   這會自動發生在每個使用者身上，不需要他們做任何事，也不會動到資料。 */
self.addEventListener('install', () => { self.skipWaiting(); });

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    try {
      const keys = await caches.keys();
      await Promise.all(keys.map(k => caches.delete(k)));   // 清掉所有舊快取
    } catch (_) {}
    try { await self.registration.unregister(); } catch (_) {}   // 解除自己
    try {
      const cs = await self.clients.matchAll({ type: 'window' });
      cs.forEach(c => { try { c.navigate(c.url); } catch (_) {} });  // 重新載入 → 拿最新版
    } catch (_) {}
  })());
});

/* 不再攔截任何請求：一律走瀏覽器原本的網路行為（等同沒有 SW）。 */
