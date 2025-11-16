from fastapi import FastAPI
from .database import init_db
from .routes import auth, dashboard

app = FastAPI(
    title="SIAG Web Demo",
    description="Full-stack demo showcasing SIAG Software development capabilities.",
    version="1.0.0"
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # o reemplazar con tu dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router)
app.include_router(dashboard.router)
