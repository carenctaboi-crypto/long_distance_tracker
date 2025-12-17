use serde::{Deserialize, Serialize};
use chrono::{DateTime, Utc};

#[derive(Deserialize)]
pub struct TrackCreate {
    pub user_id: String,
    pub distance_km: f64,
    pub duration_minutes: f64,
    pub date: DateTime<Utc>,
}

#[derive(Serialize, Clone)]
pub struct Track {
    pub id: String,
    pub user_id: String,
    pub distance_km: f64,
    pub duration_minutes: f64,
    pub date: DateTime<Utc>,
}

#[derive(Serialize)]
pub struct Stats {
    pub user_id: String,
    pub total_distance_km: f64,
    pub total_duration_minutes: f64,
    pub average_pace_min_per_km: Option<f64>,
}
#[derive(Serialize)]
pub struct TracksResponse {
    pub tracks: Vec<Track>,
}       