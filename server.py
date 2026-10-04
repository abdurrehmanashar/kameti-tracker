import json
import os
from pathlib import Path

from flask import Flask, Response, send_from_directory
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

app = Flask(__name__, static_folder=None)


@app.get("/config.js")
def config():
    settings = {
        "url": os.environ.get("SUPABASE_URL", ""),
        "key": os.environ.get("SUPABASE_PUBLISHABLE_KEY", ""),
    }
    response = Response(
        f"window.APP_CONFIG = {json.dumps(settings)};",
        mimetype="application/javascript",
    )
    response.headers["Cache-Control"] = "no-store"
    return response


@app.get("/")
@app.get("/Kameti Tracker (MVP).html")
def tracker():
    return send_from_directory(ROOT, "Kameti Tracker (MVP).html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)