from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import secrets

from .. import models, schemas, database

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(prefix="/auth", tags=["auth"])

# simple token store (demo). Replace with JWT or DB-backed tokens later.
_token_store = {}

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.Token)
def register(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == payload.username).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed = pwd_context.hash(payload.password)
    new = models.User(username=payload.username, hashed_password=hashed)
    db.add(new); db.commit(); db.refresh(new)
    token = secrets.token_hex(16)
    _token_store[token] = new.username
    return {"access_token": token}

@router.post("/login", response_model=schemas.Token)
def login(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == payload.username).first()
    if not user or not pwd_context.verify(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = secrets.token_hex(16)
    _token_store[token] = user.username
    return {"access_token": token, "token_type": "bearer"}

