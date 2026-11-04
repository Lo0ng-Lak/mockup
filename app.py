# -*- coding: utf-8 -*-
"""
Tool Mockup Áo — server Python local.

Chạy:  python app.py   (hoặc nhấp đúp run.bat)
Mở:    http://localhost:8765  (trình duyệt tự mở)

Việc của server: TÁCH ÁO khỏi nền bằng mô hình AI rembg (U2-Net) và NHUỘM
MÀU áo theo đúng vùng đã tách — phần mà JavaScript thuần trong trình duyệt
làm không đáng tin. Giao diện, khung in, ghép hình in và xuất ảnh vẫn chạy
ở trang web như cũ; trang gọi server qua /api/dye.

Mặt nạ tách áo được cache theo ảnh gốc: nhuộm 10 màu từ 1 ảnh chỉ phải
chạy mô hình 1 lần.
"""
import base64
import hashlib
import json
import os
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import cv2
import numpy as np

PORT = int(os.environ.get("MOCKUP_PORT", "8765"))
ROOT = os.path.dirname(os.path.abspath(__file__))

_session = None
_session_lock = threading.Lock()
_mask_cache: dict[str, np.ndarray] = {}


def get_session():
    global _session
    with _session_lock:
        if _session is None:
            print("[tool] Đang nạp mô hình tách áo (lần đầu sẽ tải ~176MB, chờ chút)...")
            from rembg import new_session
            _session = new_session("u2net")
            print("[tool] Mô hình đã sẵn sàng.")
        return _session


def garment_mask(bgr: np.ndarray, key: str) -> np.ndarray:
    if key in _mask_cache:
        return _mask_cache[key]
    from rembg import remove
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    out = remove(rgb, session=get_session(), only_mask=True)
    m = out.astype(np.float32) / 255.0
    m = cv2.GaussianBlur(m, (0, 0), sigmaX=1.2)
    _mask_cache[key] = m
    return m


def dye(bgr: np.ndarray, hex_color: str, strength: float) -> tuple[str, float]:
    key = hashlib.sha256(bgr.tobytes()).hexdigest()
    m = garment_mask(bgr, key)
    target = np.array(
        [int(hex_color[i:i + 2], 16) for i in (5, 3, 1)], np.float32
    ) * strength  # BGR
    gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY).astype(np.float32)
    fg = m > 0.5
    frac = float(fg.mean())
    ref = max(float(np.percentile(gray[fg], 92)) if fg.any() else 160.0, 25.0)
    f = 0.10 + 0.90 * np.clip(gray / ref, 0, 1.12)
    dyed = np.clip(target[None, None, :] * f[:, :, None], 0, 255)
    res = bgr.astype(np.float32) * (1 - m[:, :, None]) + dyed * m[:, :, None]
    ok, buf = cv2.imencode(".jpg", res.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])
    if not ok:
        raise RuntimeError("encode failed")
    return "data:image/jpeg;base64," + base64.b64encode(buf).decode(), frac


def decode_data_url(data_url: str) -> np.ndarray:
    raw = base64.b64decode(data_url.split(",", 1)[1])
    img = cv2.imdecode(np.frombuffer(raw, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Không đọc được ảnh gửi lên")
    return img


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):  # im lặng
        pass

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            path = os.path.join(ROOT, "index.html")
            try:
                with open(path, "rb") as fh:
                    body = fh.read()
            except OSError:
                self.send_error(404, "missing index.html")
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/api/health":
            self._json({"ok": True, "modelReady": _session is not None})
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path != "/api/dye":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length) or b"{}")
            img = decode_data_url(payload["image"])
            data_url, frac = dye(img, payload.get("hex", "#b03024"),
                                 float(payload.get("strength", 1.0)))
            self._json({"dataUrl": data_url, "maskFrac": round(frac, 4)})
        except Exception as exc:  # báo lỗi rõ ràng cho giao diện
            self._json({"error": str(exc)}, status=400)

    def _json(self, obj, status=200):
        body = json.dumps(obj).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def warmup():
    try:
        get_session()
        dummy = np.full((64, 64, 3), 200, np.uint8)
        garment_mask(dummy, "warmup")
    except Exception as exc:
        print(f"[tool] Nạp mô hình gặp lỗi: {exc}")


if __name__ == "__main__":
    threading.Thread(target=warmup, daemon=True).start()
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"[tool] Tool Mockup Áo đang chạy tại {url}")
    print("[tool] Để nguyên cửa sổ này khi dùng tool; đóng cửa sổ = tắt tool.")
    if not os.environ.get("MOCKUP_NO_BROWSER"):
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
