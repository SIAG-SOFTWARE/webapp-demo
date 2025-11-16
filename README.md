# 🚀 SIAG Software – Webapp Demo  
Full-stack example built with **FastAPI (backend)** and **React + Vite (frontend)**.

This demo shows how SIAG Software structures modern, scalable applications using clean architecture, API authentication, databases, and simple dashboard data retrieval.  
It is intentionally minimal so clients can quickly understand how a real SIAG webapp is built.

---

## 🌐 Features

- 🔐 User registration & login  
- 🔑 Token-based authentication (demo: in-memory token store)  
- 📊 Protected dashboard (`/dashboard/stats`)  
- 🗄️ SQLite database (SQLAlchemy ORM)  
- ⚡ FastAPI backend with CORS enabled  
- 🎨 React + Vite frontend  
- 🐳 Optional Docker setup (docker-compose included)  

---

## 🧱 Project Structure
```
webapp-demo/
│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── routes/
│ │ ├── auth.py
│ │ └── dashboard.py
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── package.json
│ └── src/
│ ├── App.jsx
│ ├── api.js
│ └── main.jsx
│
├── docker-compose.yml
└── .env.example
```

---

## 🛠️ Backend Setup (FastAPI)

### 1. Install dependencies  
```bash
cd backend
pip install -r requirements.txt
2. Create environment file
Copy .env.example → .env

3. Run backend
bash
Copiar código
uvicorn backend.main:app --reload
Backend URL:

arduino
Copiar código
http://localhost:8000
🎨 Frontend Setup (React + Vite)
1. Install dependencies
bash
Copiar código
cd frontend
npm install
2. Run dev server
bash
Copiar código
npm run dev
Frontend URL:

arduino
Copiar código
http://localhost:5173
🔌 API Overview
POST /auth/register
Registers a new user.

POST /auth/login
Returns a token.

GET /dashboard/stats
Protected route. Requires header:

makefile
Copiar código
Authorization: Bearer <token>
Response example:

json
Copiar código
{
  "user": "demo_user",
  "active_clients": 12,
  "mrr_usd": 420,
  "tasks_pending": 3
}
🐳 Docker (Optional)
bash
Copiar código
docker-compose up --build
Backend: http://localhost:8000
Frontend: http://localhost:5173

📜 License — MIT
This project is licensed under the MIT License.
© 2025 SIAG Software

🧩 About SIAG Software
SIAG Software builds AI-driven tools, automation systems, full-stack apps, workflow integrations and enterprise solutions.

Website: Coming soon

Contact: siag.software@protonmail.com

GitHub: https://github.com/SIAG-SOFTWARE
