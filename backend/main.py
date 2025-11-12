from fastapi import FastAPI
from .database import init_db
from .routes import auth, dashboard

app = FastAPI(title="SIAG Web Demo")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router)
app.include_router(dashboard.router)
