from flask import Blueprint, request, jsonify
from uuid import uuid4
from dateutil import parser

from .models import TrackCreate, Track, Stats
from .state import AppState

bp = Blueprint("routes", __name__)
state: AppState = None  # Will be injected from app.py


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@bp.route("/tracks", methods=["POST"])
def create_track():
    data = request.get_json() or {}

    required = ["user_id", "distance_km", "duration_minutes", "date"]
    if not all(k in data for k in required):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        distance = float(data["distance_km"])
        duration = float(data["duration_minutes"])
        if distance <= 0 or duration <= 0:
            return jsonify({"error": "Distance and duration must be positive"}), 400
    except ValueError:
        return jsonify({"error": "distance_km and duration_minutes must be numbers"}), 400

    try:
        date = parser.isoparse(data["date"])
    except Exception:
        return jsonify({"error": "Invalid date format, use ISO"}), 400

    track_create = TrackCreate(
        user_id=data["user_id"],
        distance_km=distance,
        duration_minutes=duration,
        date=date,
    )

    track = Track(
        id=str(uuid4()),
        **track_create.__dict__,
    )

    state.add_track(track)

    return jsonify(track.__dict__), 201


@bp.route("/tracks", methods=["GET"])
def list_tracks():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    tracks = state.get_tracks_for_user(user_id)
    return jsonify([t.__dict__ for t in tracks])


@bp.route("/stats", methods=["GET"])
def stats():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    tracks = state.get_tracks_for_user(user_id)

    if not tracks:
        return jsonify(
            Stats(
                user_id=user_id,
                total_distance_km=0.0,
                total_duration_minutes=0.0,
                average_pace_min_per_km=None,
            ).__dict__
        )

    total_distance = sum(t.distance_km for t in tracks)
    total_duration = sum(t.duration_minutes for t in tracks)
    avg_pace = total_duration / total_distance if total_distance > 0 else None

    stats = Stats(
        user_id=user_id,
        total_distance_km=total_distance,
        total_duration_minutes=total_duration,
        average_pace_min_per_km=avg_pace,
    )

    return jsonify(stats.__dict__)
