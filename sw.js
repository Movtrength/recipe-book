/* Offline support. Built by build.py: d432d1caceff is a hash of the shipped files,
   so every deploy installs a fresh cache and drops the old one. */
const VERSION = "d432d1caceff";
const APP = "app-" + VERSION;
const FONTS = "fonts-v1";
const PRECACHE = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "icons/icon.svg",
  "icons/icon-192.png",
  "icons/icon-512.png",
  "icons/icon-maskable-512.png",
  "icons/apple-touch-icon.png",
];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(APP).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== APP && k !== FONTS).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Serve the cached copy at once, refresh it in the background (weak signal in a store or kitchen).
function staleWhileRevalidate(cacheName, request, key) {
  return caches.open(cacheName).then((cache) =>
    cache.match(key || request, { ignoreSearch: true }).then((hit) => {
      const net = fetch(request)
        .then((res) => {
          if (res && (res.ok || res.type === "opaque")) cache.put(key || request, res.clone());
          return res;
        })
        .catch(() => hit);
      return hit || net;
    })
  );
}

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);

  if (url.origin === self.location.origin) {
    // Any page load (with #r-12 or ?v=2) is the same single-page app.
    if (req.mode === "navigate") {
      e.respondWith(staleWhileRevalidate(APP, req, new URL("index.html", self.registration.scope).href));
      return;
    }
    e.respondWith(caches.match(req, { ignoreSearch: true }).then((hit) => hit || fetch(req)));
    return;
  }

  if (url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com") {
    e.respondWith(staleWhileRevalidate(FONTS, req));
  }
});
