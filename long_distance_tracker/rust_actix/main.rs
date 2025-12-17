mod models;
mod routes;
mod state;

use actix_web::{App, HttpServer, web};
use state::AppState;
use routes::{health, create_track, list_tracks, stats};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let state = web::Data::new(AppState::new());

    println!("🚀 Rust Actix Long Distance Tracker running on port 8003");

    HttpServer::new(move || {
        App::new()
            .app_data(state.clone())
            .service(health)
            .service(create_track)
            .service(list_tracks)
            .service(stats)
    })
    .bind(("0.0.0.0", 8003))?
    .run()
    .await
}
