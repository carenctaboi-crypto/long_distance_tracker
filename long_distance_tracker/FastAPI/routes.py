from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, Query
from uuid import uuid4

from .models import TrackCreate, Track, Stats, TracksResponse
from .state import AppState

router = APIRouter()


def get_state() -> AppState:
    # In a larger app, this could plug into dependency injection
    # For now, this will be wired from main.py with dependency_overrides if needed
    raise RuntimeError("AppState dependency not overridden")


@router.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@router.post("/tracks", response_model=Track, status_code=201)
def create_track(
    payload: TrackCreate,
    state: AppState = Depends(get_state),
) -> Track:
    track = Track(
        id=str(uuid4()),
        **payload.dict(),
    )
    state.add_track(track)
    return track


@router.get("/tracks", response_model=TracksResponse)
def list_tracks(
    user_id: str = Query(..., description="User ID to filter tracks"),
    state: AppState = Depends(get_state),
) -> TracksResponse:
    tracks = state.get_tracks_for_user(user_id)
    return TracksResponse(tracks=tracks)


@router.get("/stats", response_model=Stats)
def get_stats(
    user_id: str = Query(..., description="User ID to compute stats for"),
    state: AppState = Depends(get_state),
) -> Stats:
    tracks = state.get_tracks_for_user(user_id)

    if not tracks:
        return Stats(
            user_id=user_id,
            total_distance_km=0.0,
            total_duration_minutes=0.0,
            average_pace_min_per_km=None,
        )

    total_distance = sum(t.distance_km for t in tracks)
    total_duration = sum(t.duration_minutes for t in tracks)
    avg_pace = total_duration / total_distance if total_distance > 0 else None

    return Stats(
        user_id=user_id,
        total_distance_km=total_distance,
        total_duration_minutes=total_duration,
        average_pace_min_per_km=avg_pace,
    )
