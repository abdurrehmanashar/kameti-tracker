import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")


class TrackerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.split("?", 1)[0] == "/config.js":
            config = {
                "url": os.environ.get("SUPABASE_URL", ""),
                "key": os.environ.get("SUPABASE_PUBLISHABLE_KEY", ""),
            }
            body = f"window.APP_CONFIG = {json.dumps(config)};".encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()


if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"Serving tracker at http://{address[0]}:{address[1]}")
    ThreadingHTTPServer(address, TrackerHandler).serve_forever()