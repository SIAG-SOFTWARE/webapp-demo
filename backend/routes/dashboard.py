from fastapi import APIRouter, Depends, Header, HTTPException
from .. import database

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

# Access demo: check simple bearer token against in-memory store in auth module
from .auth import _token_store

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing authorization header")
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise
    except:
        raise HTTPException(status_code=401, detail="Malformed authorization header")
    if token not in _token_store:
        raise HTTPException(status_code=401, detail="Invalid token")
    return _token_store[token]

@router.get("/stats")
def stats(user: str = Depends(get_current_user)):
    # Demo data: replace with DB queries
    return {
        "user": user,
        "active_clients": 12,
        "mrr_usd": 420,
        "tasks_pending": 3
    }
