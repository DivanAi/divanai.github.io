/* DivanAI · service worker (Kol 117)
   ---------------------------------------------------------------------------
   Tek işi: telefondan kurulan uygulama internet yokken de AÇILSIN.

   Strateji "ağ önce": internet varsa her zaman sunucudaki taze dosya gelir
   (eski sürüm takılı kalmasın diye). İnternet yoksa son görülen kopya açılır.

   Dokunmadığı yerler: başka alan adlarına giden istekler (model servisleri).
   Onlar önbelleğe alınmaz, araya girilmez.
   --------------------------------------------------------------------------- */

var SURUM = 'divanai-117';
var CEKIRDEK = ['./', './index.html', './manifest.json', './icon-192.png', './icon-512.png'];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(SURUM)
      .then(function (k) {
        /* biri 404 olsa bile kurulum düşmesin */
        return Promise.all(CEKIRDEK.map(function (u) { return k.add(u).catch(function () {}); }));
      })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys()
      .then(function (adlar) {
        return Promise.all(adlar.map(function (a) { return a === SURUM ? null : caches.delete(a); }));
      })
      .then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  var r = e.request;
  if (r.method !== 'GET') return;

  var u;
  try { u = new URL(r.url); } catch (err) { return; }
  if (u.origin !== self.location.origin) return;   /* model servisleri: karışma */

  e.respondWith(
    fetch(r)
      .then(function (yanit) {
        if (yanit && yanit.ok) {
          var kopya = yanit.clone();
          caches.open(SURUM).then(function (k) { k.put(r, kopya).catch(function () {}); });
        }
        return yanit;
      })
      .catch(function () {
        return caches.open(SURUM).then(function (k) {
          return k.match(r, { ignoreSearch: true }).then(function (v) {
            if (v) return v;
            if (r.mode === 'navigate') {
              return k.match('./index.html').then(function (idx) { return idx || Response.error(); });
            }
            return Response.error();
          });
        });
      })
  );
});
