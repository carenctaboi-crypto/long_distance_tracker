import express from "express";
import { v4 as uuidv4 } from "uuid";
import { Track, TrackCreate, Stats } from "./models.js";
import { appState } from "./state.js";

export const router = express.Router();

router.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

router.post("/tracks", (req, res) => {
  const { user_id, distance_km, duration_minutes, date } = req.body;

  if (!user_id || !distance_km || !duration_minutes || !date) {
    return res.status(400).json({ error: "Missing required fields" });
  }

  const distance = Number(distance_km);
  const duration = Number(duration_minutes);

  if (isNaN(distance) || isNaN(duration) || distance <= 0 || duration <= 0) {
    return res.status(400).json({ error: "Distance and duration must be positive numbers" });
  }

  const trackCreate = new TrackCreate(
    user_id,
    distance,
    duration,
    new Date(date).toISOString()
  );

  const track = new Track(
    uuidv4(),
    trackCreate.user_id,
    trackCreate.distance_km,
    trackCreate.duration_minutes,
    trackCreate.date
  );

  appState.addTrack(track);

  res.status(201).json(track);
});

router.get("/tracks", (req, res) => {
  const { user_id } = req.query;

  if (!user_id) {
    return res.status(400).json({ error: "user_id is required" });
  }

  const tracks = appState.getTracksForUser(user_id);
  res.json(tracks);
});

router.get("/stats", (req, res) => {
  const { user_id } = req.query;

  if (!user_id) {
    return res.status(400).json({ error: "user_id is required" });
  }

  const tracks = appState.getTracksForUser(user_id);

  if (tracks.length === 0) {
    return res.json(
      new Stats(user_id, 0.0, 0.0, null)
    );
  }

  const total_distance = tracks.reduce((sum, t) => sum + t.distance_km, 0);
  const total_duration = tracks.reduce((sum, t) => sum + t.duration_minutes, 0);
  const avg_pace = total_duration / total_distance;

  res.json(
    new Stats(user_id, total_distance, total_duration, avg_pace)
  );
});
