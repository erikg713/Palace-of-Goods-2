// Define cache names and assets to cache
const CACHE_NAME = "palace-of-goods-cache-v1";
const OFFLINE_CACHE_NAME = "offline-cache-v1";
const STATIC_ASSETS = [
  "/",
  "/index.html",
  "/static/js/main.js",
  "/static/css/main.css",
  "/favicon.ico",
  "/offline.html", // Offline fallback
];

// Install event: Cache static assets
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log("[Service Worker] Pre-caching static assets");
      return cache.addAll(STATIC_ASSETS);
    })
  );
});

// Activate event: Clean up old caches
self.addEventListener("activate", (event) => {
  const cacheWhitelist = [CACHE_NAME, OFFLINE_CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) =>
      Promise.all(
        cacheNames.map((cacheName) => {
          if (!cacheWhitelist.includes(cacheName)) {
            console.log(`[Service Worker] Deleting old cache: ${cacheName}`);
            return caches.delete(cacheName);
          }
        })
      )
    )
  );
});

// Fetch event: Serve from cache, fallback to network, then offline page
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return (
        cachedResponse ||
        fetch(event.request)
          .then((networkResponse) => {
            // Cache the network response dynamically
            return caches.open(CACHE_NAME).then((cache) => {
              if (event.request.method === "GET") {
                cache.put(event.request, networkResponse.clone());
              }
              return networkResponse;
            });
          })
          .catch(() => {
            // Serve offline fallback for HTML requests
            if (event.request.destination === "document") {
              return caches.match("/offline.html");
            }
          })
      );
    })
  );
});

// Workbox configuration: Cache images with CacheFirst strategy
if (typeof workbox !== "undefined") {
  workbox.routing.registerRoute(
    ({ request }) => request.destination === "image",
    new workbox.strategies.CacheFirst({
      cacheName: "image-cache",
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 50,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
        }),
      ],
    })
  );
} else {
  console.log("[Service Worker] Workbox could not be loaded.");
}
