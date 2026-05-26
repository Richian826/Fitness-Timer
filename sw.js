/* 组间计时 — 离线 Service Worker */
const CACHE = 'timer-v2';
const FILES = ['index.html', 'manifest.json', 'icon-192.png', 'icon-512.png'];

self.addEventListener('install', e => {
  // 逐个缓存，单个失败不影响整体安装
  e.waitUntil(
    caches.open(CACHE).then(c =>
      Promise.allSettled(FILES.map(url =>
        c.add(url).catch(() => {})
      ))
    ).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k))))
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request))
  );
});
