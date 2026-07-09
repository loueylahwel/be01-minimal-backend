from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Hello from BE-01!", status="ok")


@app.route("/health")
def health():
    return jsonify(status="healthy", timestamp=datetime.utcnow().isoformat() + "Z")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
