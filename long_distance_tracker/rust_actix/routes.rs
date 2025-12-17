use actix_web::{get, post, web, HttpResponse, Responder};
use uuid::Uuid;

use crate::models::{Track, TrackCreate, Stats};
use crate::state::AppState;

#[get("/health")]
pub async fn health() -> impl Responder {
    HttpResponse::Ok().json(serde_json::json!({ "status": "ok" }))
}

#[post("/tracks")]
pub async fn create_track(
    data: web::Data<AppState>,
    payload: web::Json<TrackCreate>,
) -> impl Responder {
    if payload.distance_km <= 0.0 || payload.duration_minutes <= 0.0 {
        return HttpResponse::BadRequest().json(
            serde_json::json!({"error": "Distance and duration must be positive"})
        );
    }

    let track = Track {
        id: Uuid::new_v4().to_string(),
        user_id: payload.user_id.clone(),
        distance_km: payload.distance_km,
        duration_minutes: payload.duration_minutes,
        date: payload.date,
    };

    let mut tracks = data.tracks.lock().unwrap();
    tracks.push(track.clone());

    HttpResponse::Created().json(track)
}

#[get("/tracks")]
pub async fn list_tracks(
    data: web::Data<AppState>,
    query: web::Query<std::collections::HashMap<String, String>>,
) -> impl Responder {
    let user_id = match query.get("user_id") {
        Some(u) => u,
        None => {
            return HttpResponse::BadRequest().json(
                serde_json::json!({"error": "user_id is required"})
            )
        }
    };

    let tracks = data.tracks.lock().unwrap();
    let user_tracks: Vec<Track> = tracks
        .iter()
        .filter(|t| &t.user_id == user_id)
        .cloned()
        .collect();

    HttpResponse::Ok().json(user_tracks)
}

#[get("/stats")]
pub async fn stats(
    data: web::Data<AppState>,
    query: web::Query<std::collections::HashMap<String, String>>,
) -> impl Responder {
    let user_id = match query.get("user_id") {
        Some(u) => u,
        None => {
            return HttpResponse::BadRequest().json(
                serde_json::json!({"error": "user_id is required"})
            )
        }
    };

    let tracks = data.tracks.lock().unwrap();
    let user_tracks: Vec<&Track> = tracks
        .iter()
        .filter(|t| &t.user_id == user_id)
        .collect();

    if user_tracks.is_empty() {
        let stats = Stats {
            user_id: user_id.clone(),
            total_distance_km: 0.0,
            total_duration_minutes: 0.0,
            average_pace_min_per_km: None,
        };
        return HttpResponse::Ok().json(stats);
    }

    let total_distance: f64 = user_tracks.iter().map(|t| t.distance_km).sum();
    let total_duration: f64 = user_tracks.iter().map(|t| t.duration_minutes).sum();
    let avg_pace = if total_distance > 0.0 {
        Some(total_duration / total_distance)
    } else {
        None
    };

    let stats = Stats {
        user_id: user_id.clone(),
        total_distance_km: total_distance,
        total_duration_minutes: total_duration,
        average_pace_min_per_km: avg_pace,
    };

    HttpResponse::Ok().json(stats)
}
