from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TrackCreate:
    user_id: str
    distance_km: float
    duration_minutes: float
    date: datetime


@dataclass
class Track:
    id: str
    user_id: str
    distance_km: float
    duration_minutes: float
    date: datetime


@dataclass
class Stats:
    user_id: str
    total_distance_km: float
    total_duration_minutes: float
    average_pace_min_per_km: Optional[float]
@dataclass
class StatsResponse:
    stats: Stats    
    