Long Distance Tracker
A small multi-language example API for tracking long-distance activities (runs, rides, etc.). This repository provides four independent implementations of the same API so you can compare idiomatic...

Quick overview
Shared API contract: openapi.yaml (canonical source of truth)
Implementations:
FastAPI/ (port 8000) — production-ready FastAPI example
node_express/ (port 8001) — Node + Express example
flask/ (port 8002) — Flask example
rust_actix/ (port 8003) — Rust (Actix) example
All services use in-memory state for simplicity (data is not persisted across restarts).
Running the services (copy/paste)
FastAPI
python -m pip install -r FastAPI/requirements.txt
uvicorn FastAPI.main:app --reload --port 8000
Visit: http://localhost:8000/docs for Swagger UI

Node + Express
cd node_express
npm install
npm start
Flask
python -m pip install -r flask/requirements.txt
python flask/app.py
Rust (Actix)
cd rust_actix
cargo run
API (high level)
The API surface is defined in openapi.yaml. Important endpoints:

GET /health — health check
POST /tracks — create a track (payload: user_id, distance_km, duration_minutes, date)
GET /tracks?user_id=<id> — list tracks for a user
GET /stats?user_id=<id> — aggregated stats for a user
Example curl to create a track:

curl -X POST http://localhost:8000/tracks \
	-H "Content-Type: application/json" \
	-d '{"user_id":"alice","distance_km":5.0,"duration_minutes":30,"date":"2025-12-01T07:00:00Z"}'
Project structure
FastAPI/, flask/, node_express/, rust_actix/ — implementation-specific code
openapi.yaml — canonical API definition
docs/ — documentation and utility files (see docs/toolkit.md and docs/ai prompt journal)
Development notes & contributing
When modifying the API, update openapi.yaml and mirror changes in the implementations.
Keep changes scoped to one implementation unless making a cross-cutting improvement or adding tests/examples.
If you add persistence, document how to configure it and consider adding integration tests.
Additional Documentation: Google Doc.
Troubleshooting
If a port is in use, stop the conflicting service or change the port in the respective implementation's entry file.
Unexpected data loss? Remember that state is in-memory by design.
License
This project is intended as an educational toolkit. See the repository LICENSE (if present) for details.
