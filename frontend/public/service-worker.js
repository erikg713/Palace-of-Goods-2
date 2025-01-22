// Cache names
const STATIC_CACHE = "palace-of-goods-static-v1";
const DYNAMIC_CACHE = "palace-of-goods-dynamic-v1";
const OFFLINE_CACHE = "palace-of-goods-offline-v1";
const STATIC_ASSETS = [
  "/",
  "/index.html",
  "/static/js/main.js",
  "/static/css/main.css",
  "/favicon.ico",
  "/offline.html",
];

// Install event: Precache static assets
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then((cache) => {
      console.log("[Service Worker] Precaching static assets...");
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting(); // Activate the new service worker immediately
});

// Activate event: Clean up old caches
self.addEventListener("activate", (event) => {
  console.log("[Service Worker] Activating...");
  event.waitUntil(
    caches.keys().then((cacheNames) =>
      Promise.all(
        cacheNames.map((cache) => {
          if (![STATIC_CACHE, DYNAMIC_CACHE, OFFLINE_CACHE].includes(cache)) {
            console.log(`[Service Worker] Deleting old cache: ${cache}`);
            return caches.delete(cache);
          }
        })
      )
    )
  );
  self.clients.claim(); // Take control of all pages immediately
});

// Fetch event: Serve cached assets, fall back to network, then offline
self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return; // Ignore non-GET requests

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse; // Serve from cache
      }

      return fetch(event.request)
        .then((networkResponse) => {
          // Cache the new network response dynamically
          return caches.open(DYNAMIC_CACHE).then((cache) => {
            cache.put(event.request, networkResponse.clone());
            return networkResponse;
          });
        })
        .catch(() => {
          // Serve offline fallback for HTML pages
          if (event.request.destination === "document") {
            return caches.match("/offline.html");
          }
        });
    })
  );
});

// Push notification event
self.addEventListener("push", (event) => {
  const data = event.data ? JSON.parse(event.data.text()) : {};
  const title = data.title || "New Notification";
  const options = {
    body: data.body || "You have a new update!",
    icon: "/favicon.ico",
    badge: "/favicon.ico",
  };

  event.waitUntil(self.registration.showNotification(title, options));
});

// Background sync event: Retry failed requests
self.addEventListener("sync", (event) => {
  if (event.tag === "sync-failed-requests") {
    event.waitUntil(
      retryFailedRequests().catch((error) => {
        console.error("[Service Worker] Background sync failed:", error);
      })
    );
  }
});

// Helper: Retry failed requests stored in IndexedDB
async function retryFailedRequests() {
  const db = await openFailedRequestsDB();
  const store = db.transaction("failed-requests", "readwrite").objectStore("failed-requests");

  const requests = await store.getAll();
  for (const request of requests) {
    try {
      await fetch(request.url, request.options);
      store.delete(request.id);
      console.log(`[Service Worker] Retried and succeeded: ${request.url}`);
    } catch (error) {
      console.error(`[Service Worker] Retry failed for: ${request.url}`, error);
    }
  }
}

// Helper: Open IndexedDB for failed requests
function openFailedRequestsDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open("failed-requests", 1);
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
    request.onupgradeneeded = () => {
      const db = request.result;
      if (!db.objectStoreNames.contains("failed-requests")) {
        db.createObjectStore("failed-requests", { keyPath: "id", autoIncrement: true });
      }
    };
  });
}
