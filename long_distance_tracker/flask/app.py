from flask import Flask

from .routes import bp, state
from .state import AppState

app = Flask(__name__)

# Create shared in-memory state
app_state = AppState()

# Inject state into routes module
state = app_state

# Register routes
app.register_blueprint(bp)


if __name__ == "__main__":
    print(" Flask Long Distance Tracker running on port 8002")
    app.run(host="0.0.0.0", port=8002)
    print(" Flask Long Distance Tracker shutting down")   
    pass
