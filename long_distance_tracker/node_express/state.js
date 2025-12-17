export class AppState {
  constructor() {
    this.tracks = [];
  }

  addTrack(track) {
    this.tracks.push(track);
  }

  getTracksForUser(user_id) {
    return this.tracks.filter((t) => t.user_id === user_id);
  }
}

export const appState = new AppState();
export const getAllTracks = () => {
  return appState.tracks;
}   