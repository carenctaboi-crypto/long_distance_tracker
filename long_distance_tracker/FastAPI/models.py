from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, validator


class TrackCreate(BaseModel):
    user_id: str
    distance_km: float
    duration_minutes: float
    date: datetime

    @validator("distance_km")
    def validate_distance(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("distance_km must be positive")
        return v

    @validator("duration_minutes")
    def validate_duration(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("duration_minutes must be positive")
        return v


class Track(TrackCreate):
    id: str


class Stats(BaseModel):
    user_id: str
    total_distance_km: float
    total_duration_minutes: float
    average_pace_min_per_km: Optional[float]


class TracksResponse(BaseModel):
    tracks: List[Track]
class StatsResponse(BaseModel):
    stats: Stats        
    