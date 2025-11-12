# webapp-demo — SIAG Software

Simple full-stack demo (FastAPI backend + React frontend) for SIAG Software.

## Quick start (local)

### Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

shell
Copiar código

### Frontend
cd frontend
npm install
npm run dev

csharp
Copiar código

Frontend: http://localhost:5173  
Backend: http://localhost:8000

## Notes
- This is a starter template. Replace token logic with JWT and integrate a real DB (Supabase / Postgres) for production.
- Use `.env` to store secrets and DB URLs.
