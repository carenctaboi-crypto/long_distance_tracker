from typing import List
from threading import Lock

from .models import Track


class AppState:
    def __init__(self) -> None:
        self._tracks: List[Track] = []
        self._lock = Lock()

    def add_track(self, track: Track) -> None:
        with self._lock:
            self._tracks.append(track)

    def get_tracks_for_user(self, user_id: str) -> List[Track]:
        with self._lock:
            return [t for t in self._tracks if t.user_id == user_id]
    def get_all_tracks(self) -> List[Track]:
        with self._lock:
            return list(self._tracks)       