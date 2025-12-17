# Toolkit — Long Distance Tracker ⚙️

## Overview

This repository contains multiple example implementations of the **Long Distance Tracker API** so you can compare idiomatic approaches in different ecosystems (Python/FastAPI, Python/Flask, Node + Express, Rust/Actix). Each implementation exposes the same API surface described in `openapi.yaml`.

> Note: Each service runs independently and uses **in-memory** state. Data is NOT shared between services and will be lost when the process exits. 🔧

---

## Quick Start (per implementation)

### FastAPI (Python) 
- Location: `FastAPI/`
- Entry: `FastAPI/main.py`
- Port: **8000**
- Install & run:

```bash
python -m pip install -r FastAPI/requirements.txt
uvicorn FastAPI.main:app --reload --port 8000
```

When running, open http://localhost:8000/docs for the auto-generated Swagger UI.

### Node + Express 
- Location: `node_express/`
- Entry: `node_express/index.js`
- Port: **8001**
- Install & run:

```bash
cd node_express
npm install
npm start
```

### Flask (Python) 
- Location: `flask/`
- Entry: `flask/app.py`
- Port: **8002**
- Install & run:

```bash
python -m pip install -r flask/requirements.txt
python flask/app.py
```

### Rust (Actix) 
- Location: `rust_actix/`
- Entry: `rust_actix/main.rs`
- Port: **8003**
- Install & run (requires Rust toolchain):

```bash
cd rust_actix
cargo run
```

---

## API (common contract)

Refer to `openapi.yaml` for the canonical API. Main endpoints:

- `GET /health` — health check
- `POST /tracks` — create a track (payload: `user_id`, `distance_km`, `duration_minutes`, `date`)
- `GET /tracks?user_id=<id>` — list tracks for a user
- `GET /stats?user_id=<id>` — aggregated stats for a user

Example `curl` (create a track):

```bash
curl -X POST http://localhost:8000/tracks \
	-H "Content-Type: application/json" \
	-d '{"user_id":"alice","distance_km":5.0,"duration_minutes":30,"date":"2025-12-01T07:00:00Z"}'
```

Example `curl` (get stats):

```bash
curl "http://localhost:8000/stats?user_id=alice"
```

Tip: swap the port to target a different implementation (8001, 8002, 8003).

---

## Project structure highlights 

- `*/models*` — language-specific models and validation
- `*/routes*` — HTTP handlers for the API
- `*/state*` — in-memory state container and helpers
- `openapi.yaml` — shared API contract

---

## Development & Contributing 

- Keep changes isolated to a single implementation unless you're adding a shared spec or example.
- When changing the API, update `openapi.yaml` and add tests or examples for each implementation you modify.
- If you add long-lived state or persistence, document it clearly and provide migration or seed scripts.

---

## Troubleshooting & Notes 

> If you see unexpected data loss: the implementations use **in-memory** storage by design for simplicity. If you need persistence for demos, add a small SQLite/Postgres backend and document how to configure it.

If a port is already in use, stop the conflicting service or change the port in the implementation's entry file.

---

## License & Contact

This repo is intended as an educational toolkit. For questions, open an issue or contact the maintainer.

---


