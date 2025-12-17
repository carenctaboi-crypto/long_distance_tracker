export class TrackCreate {
  constructor(user_id, distance_km, duration_minutes, date) {
    this.user_id = user_id;
    this.distance_km = distance_km;
    this.duration_minutes = duration_minutes;
    this.date = date;
  }
}

export class Track {
  constructor(id, user_id, distance_km, duration_minutes, date) {
    this.id = id;
    this.user_id = user_id;
    this.distance_km = distance_km;
    this.duration_minutes = duration_minutes;
    this.date = date;
  }
}

export class Stats {
  constructor(user_id, total_distance_km, total_duration_minutes, average_pace_min_per_km) {
    this.user_id = user_id;
    this.total_distance_km = total_distance_km;
    this.total_duration_minutes = total_duration_minutes;
    this.average_pace_min_per_km = average_pace_min_per_km;
  }
}
export class TracksResponse {
  constructor(tracks) {
    this.tracks = tracks;
  }
}

export class StatsResponse {
  constructor(stats) {
    this.stats = stats;
  }
}