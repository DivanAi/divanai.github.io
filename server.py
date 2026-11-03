#!/usr/bin/env python3
"""
DIVANAI — yerel dosya sunucusu (isteğe bağlı).

Neden var: bazı özellikler (kamera, panoya kopyalama, bazı tarayıcı izinleri)
dosya yolundan (file://) açılınca çalışmaz. Bu betik index.html'i
http://localhost:8080 üzerinden açar; başka hiçbir iş yapmaz.

    python3 server.py          → tarayıcıda http://localhost:8080

Anahtar, model, istek iletme YOKTUR: API çağrıları doğrudan tarayıcıdan
sağlayıcıya gider, anahtar yalnızca tarayıcıda durur. Bu sunucu yalnızca
kendi bilgisayarını dinler (127.0.0.1) — ağdan erişilemez.

Sadece standart kütüphane kullanır; pip install gerekmez.
"""
import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = int(os.environ.get("PORT", "8080"))


CSP = ("default-src 'none'; script-src 'unsafe-inline'; style-src 'self' 'unsafe-inline'; "
       "img-src 'self' data: blob: https:; font-src data:; connect-src https: http:; "
       "media-src data: blob:; object-src 'none'; base-uri 'none'; form-action 'none'; "
       "frame-src 'none'; frame-ancestors 'none'; worker-src 'none'; manifest-src 'none'")


class Handler(SimpleHTTPRequestHandler):
    # Sürüm parmak izi bırakma: yanıt başlığında Python sürümü görünmesin
    server_version = "DIVANAI"
    sys_version = ""

    def version_string(self):
        return self.server_version

    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def send_head(self):
        """Bozuk adres (ör. içinde null bayt olan) sunucuyu çökertmesin:
        normalde yakalanmayan ValueError, istek işleyen iş parçacığını düşürüyordu."""
        try:
            return super().send_head()
        except (ValueError, OSError):
            self.send_error(400, "Bad Request")
            return None

    def log_message(self, fmt, *args):   # konsolu kirletme
        if args and str(args[0]).startswith(("4", "5")):
            sys.stderr.write("  %s\n" % (fmt % args))

    def list_directory(self, path):
        """Klasör listesi KAPALI. Sunucu zaten yalnız 127.0.0.1'i dinliyor ama
        tarayıcıdaki başka bir sekme/uzantı bu adrese istek atabilir; dosya
        adlarının listelenmesi gereksiz bilgi sızdırır.

        Not: durum satırı (status line) yalnız latin-1 taşır; Türkçe karakterli
        bir açıklama yazılırsa bağlantı düşer. Bu yüzden açıklama ASCII, gövde UTF-8."""
        body = "Klasör listesi kapalı.\n".encode("utf-8")
        self.send_response(403, "Forbidden")
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
        return None

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Security-Policy", CSP)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")          # sayfa başka sitede çerçeveye alınamaz
        self.send_header("Referrer-Policy", "no-referrer")
        super().end_headers()


def main():
    index = ROOT / "index.html"
    if index.exists():
        print("index.html bulundu (%.1f KB)" % (index.stat().st_size / 1024))
    else:
        print("UYARI: index.html yok. Bu dosya index.html ile aynı klasörde olmalı.")
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print("DIVANAI hazır  →  http://localhost:%d   (kapatmak için Ctrl+C)" % PORT)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nkapatılıyor…")
    finally:
        srv.server_close()


if __name__ == "__main__":
    main()
