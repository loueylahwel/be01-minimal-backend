# be01-minimal-backend

Minimal Flask server with two JSON endpoints — assignment BE-01.

## Endpoints

- `GET /` — `{"message": "Hello from BE-01!", "status": "ok"}`
- `GET /health` — `{"status": "healthy", "timestamp": "..."}`

## Run

```bash
pip install -r requirements.txt
python server.py
```
