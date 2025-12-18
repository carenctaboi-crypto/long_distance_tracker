# Long Distance Tracker

A small multi-language example API for tracking long-distance activities (such as runs and rides). This repository provides four independent implementations of the same API for comparison of idiomatic designs across languages and frameworks.

---

## Quick Overview

**Shared API Contract**: `openapi.yaml` (the canonical source of truth)

### Implementations:
- **FastAPI** (port 8000) — Production-ready FastAPI example
- **Node + Express** (port 8001) — Node.js with Express example
- **Flask** (port 8002) — Flask microframework example
- **Rust + Actix** (port 8003) — Rust with Actix Web example

> **Important Note**: 
> All services use in-memory state for simplicity. Data is not persisted across restarts.

---

## Running the Services

Below are the steps to run each implementation. You can copy-paste these commands into your terminal.

### **FastAPI**
```bash
python -m pip install -r FastAPI/requirements.txt
uvicorn FastAPI.main:app --reload --port 8000
```
Visit the Swagger UI at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### **Node + Express**
```bash
cd node_express
npm install
npm start
```

---

### **Flask**
```bash
python -m pip install -r flask/requirements.txt
python flask/app.py
```

---

### **Rust (Actix)**
```bash
cd rust_actix
cargo run
```

---

## API (High Level)

The API surface is defined in `openapi.yaml`. Below is a quick reference for key endpoints:

**Endpoints**
- `GET /health` — Simple health check
- `POST /tracks` — Create a track  
  - Payload: `{ "user_id": "string", "distance_km": number, "duration_minutes": number, "date": "datetime" }`
- `GET /tracks?user_id=<id>` — List all tracks for a user
- `GET /stats?user_id=<id>` — Aggregated stats for a user

### Example
Create a track using `curl`:
```bash
curl -X POST http://localhost:8000/tracks \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "alice",
    "distance_km": 5.0,
    "duration_minutes": 30,
    "date": "2025-12-01T07:00:00Z"
  }'
```

---

## Project Structure
- **`FastAPI/`**, **`flask/`**, **`node_express/`**, **`rust_actix/`** — Framework-specific implementation directories
- **`openapi.yaml`** — Canonical API definition
- **`docs/`** — Documentation and utility files  
  - See `docs/toolkit.md` and `docs/ai prompt journal`

---

## Development Notes & Contributing

- When modifying the API, update `openapi.yaml` and mirror changes across all implementations.
- Keep changes scoped to one implementation unless making cross-cutting improvements or adding tests/examples.
- If persistence is added, document its configuration and consider including integration tests.

> **Additional Documentation**: [Google Doc](#).

---

## Troubleshooting

- **Port conflicts**: Stop the conflicting service or change the port in the implementation's entry file.
- **Unexpected data loss**: Remember that all state is in-memory by design.

---

## License

This project is intended as an educational toolkit. Refer to the repository `LICENSE` file for details.