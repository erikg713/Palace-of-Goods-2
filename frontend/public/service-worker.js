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
  console.log("[Service Worker] Installing and caching static assets...");
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
});

// Activate event: Clean up old caches and claim clients
self.addEventListener("activate", (event) => {
  console.log("[Service Worker] Activating...");
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
  self.clients.claim(); // Take control of all open pages immediately
});

// Fetch event: Serve from cache, fallback to network, then offline page
self.addEventListener("fetch", (event) => {
  console.log(`[Service Worker] Fetching: ${event.request.url}`);
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return (
        cachedResponse ||
        fetch(event.request)
          .then((networkResponse) => {
            if (event.request.method === "GET") {
              // Dynamically cache network responses
              caches.open(CACHE_NAME).then((cache) => {
                cache.put(event.request, networkResponse.clone());
              });
            }
            return networkResponse;
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

// Notify user of service worker updates
self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "SKIP_WAITING") {
    self.skipWaiting();
  }
});

// Workbox configuration: Cache images with CacheFirst strategy
if (typeof workbox !== "undefined") {
  console.log("[Service Worker] Workbox loaded.");
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

  // Add caching for JS and CSS files
  workbox.routing.registerRoute(
    ({ request }) => request.destination === "script" || request.destination === "style",
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: "static-resources",
    })
  );

  // Add caching for API requests
  workbox.routing.registerRoute(
    ({ url }) => url.pathname.startsWith("/api/"),
    new workbox.strategies.NetworkFirst({
      cacheName: "api-cache",
    })
  );
} else {
  console.log("[Service Worker] Workbox could not be loaded.");
}
