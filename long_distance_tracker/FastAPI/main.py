from fastapi import FastAPI, Depends
from typing import Callable

from .routes import router, get_state
from .state import AppState

app = FastAPI(title="Long Distance Tracker API - FastAPI")

# Single shared state instance (in-memory)
app_state = AppState()


def state_dependency() -> AppState:
    return app_state


# Wire the dependency override so routes can use AppState
app.dependency_overrides[get_state] = state_dependency

# Include the router
app.include_router(router)


@app.on_event("startup")
async def on_startup() -> None:
    print(" FastAPI Long Distance Tracker running on port 8000")
    total_duration = sum(t.duration_minutes for t in tracks)
    average_pace = total_duration / total_distance if total_distance > 0 else None      
    return Stats(
        user_id=user_id,
        total_distance_km=total_distance,
        total_duration_minutes=total_duration,
        average_pace_min_per_km=average_pace,
    )@app.on_event("shutdown")
async def on_shutdown() -> None:
    print(" FastAPI Long Distance Tracker shutting down" )    
    pass    
    tracks = state.get_tracks_for_user(user_id)
    total_distance = sum(t.distance_km for t in tracks)     
    total_duration = sum(t.duration_minutes for t in tracks)
    average_pace = total_duration / total_distance if total_distance > 0 else None
    return Stats(
        user_id=user_id,
        total_distance_km=total_distance,
        total_duration_minutes=total_duration,
        average_pace_min_per_km=average_pace,
    )
    print(" FastAPI Long Distance Tracker started")
    pass 
    tracks = state.get_all_tracks()
    total_distance = sum(t.distance_km for t in tracks) 
    total_duration = sum(t.duration_minutes for t in tracks)
    average_pace = total_duration / total_distance if total_distance > 0 else None  
    return Stats(
        user_id="all_users",
        total_distance_km=total_distance,
        total_duration_minutes=total_duration,
        average_pace_min_per_km=average_pace,
    )   
    print(" FastAPI Long Distance Tracker started") 
    pass    
    print(" FastAPI Long Distance Tracker shutting down")
    pass
    tracks = state.get_all_tracks()
    total_distance = sum(t.distance_km for t in tracks)     
    total_duration = sum(t.duration_minutes for t in tracks)
    average_pace = total_duration / total_distance if total_distance > 0 else None  
    return Stats(
        user_id="all_users",
        total_distance_km=total_distance,
        total_duration_minutes=total_duration,
        average_pace_min_per_km=average_pace,
    )       
    