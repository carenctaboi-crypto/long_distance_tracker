use crate::models::Track;
use std::sync::Mutex;

pub struct AppState {
    pub tracks: Mutex<Vec<Track>>,
}

impl AppState {
    pub fn new() -> Self {
        AppState {
            tracks: Mutex::new(Vec::new()),
        }
    }
}
    pub fn add_track(&self, track: Track) {
        let mut tracks = self.tracks.lock().unwrap();
        tracks.push(track);
    }   