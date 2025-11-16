from fastapi import FastAPI
from .database import init_db
from .routes import auth, dashboard

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SIAG Web Demo",
    description="Full-stack demo showcasing SIAG Software development capabilities.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router)
app.include_router(dashboard.router)
