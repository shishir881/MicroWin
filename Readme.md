# MicroWin 🧠⚡

**An AI-powered executive function coach that breaks overwhelming goals into tiny, achievable "Micro-Wins" — personalized for neurodivergent users.**

MicroWin uses adaptive AI granularity, privacy-first encrypted storage, and neuro-inclusive design to help users with ADHD, Autism, and other cognitive needs overcome task paralysis.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **AI Micro-Win Decomposition** | Goals → 3-5 sensory-grounded action steps via Gemini 2.5 Flash |
| **< 5s Latency** | Streaming SSE with time-to-first-token metrics displayed in-app |
| **Individualized Neuro-Profiles** | Encrypted struggle areas, preferences, and granularity (1-5 scale) |
| **PII Masking** | spaCy NER scrubs names, locations, and orgs before LLM ingestion |
| **Encryption at Rest** | Fernet AES-128 for all stored goals, micro-wins, and profile data |
| **Neuro-Inclusive Fonts** | Toggle between Inter, Verdana, OpenDyslexic, and Lexend |
| **Gamification** | Streak counter 🔥, completion badges 🏆, confetti, and sound effects |
| **Mascot (Polo)** | Animated companion with mood states: idle, thinking, happy, celebrating |
| **Single-Task View** | One step at a time with large "I DID IT!" button (reduces overwhelm) |
| **Gamma Wave Focus Music** | Built-in binaural beat player for focus enhancement |
| **Dark/Light Mode** | Warm brown dark mode with muted, low-stimulation palettes |

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React 19, Vite 7, TypeScript, Tailwind CSS 4, Framer Motion |
| **Backend** | FastAPI (async), SQLAlchemy 2 (async), PostgreSQL |
| **AI** | Google Gemini 2.5 Flash via `google-genai` SDK |
| **Privacy** | spaCy NER (PII masking), Fernet encryption (AES-128-CBC) |
| **Auth** | JWT (python-jose) + Google OAuth2 (Implicit Flow) |
| **Deployment** | Docker multi-stage build |

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- A Google Gemini API key
- A PostgreSQL database URL

### 1. Clone & Configure
```bash
git clone https://github.com/your-repo/MicroWin.git
cd MicroWin

# Create backend/.env with required variables
cat > backend/.env << EOF
GEMINI_API_KEY=your-gemini-api-key
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/microwin
DB_ENCRYPTION_KEY=$(python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
JWT_SECRET_KEY=your-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
FRONTEND_URL=http://localhost:8000
EOF
```

### 2. Build & Run
```bash
docker-compose up --build
```
The app will be available at **http://localhost:8000**.

### 3. Run Locally (Development)
```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn main:app --reload

# Frontend (separate terminal)
cd frontend
npm install && npm run dev
```

---

## 🔐 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GEMINI_API_KEY` | ✅ | Google AI Studio API key |
| `DATABASE_URL` | ✅ | PostgreSQL async URL (`postgresql+asyncpg://...`) |
| `DB_ENCRYPTION_KEY` | ✅ | Fernet key for data encryption |
| `JWT_SECRET_KEY` | ⚠️ | Secret for JWT signing (has default, change in prod) |
| `GOOGLE_CLIENT_ID` | ❌ | For Google OAuth login |
| `FRONTEND_URL` | ❌ | CORS origin (default: `http://localhost:5173`) |

---

## 📐 Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Frontend (React)                  │
│  ┌──────────┐ ┌──────────┐ ┌───────────────────┐    │
│  │ Dashboard │ │ Auth     │ │ Components        │    │
│  │ (Quest UI)│ │ (Login/  │ │ (Mascot, Fonts,   │    │
│  │           │ │  Signup) │ │  Settings, Audio) │    │
│  └─────┬─────┘ └────┬─────┘ └───────────────────┘    │
│        │             │                               │
│        ▼             ▼                               │
│  ┌─────────────────────────────────────────┐         │
│  │         API Layer (api.ts)              │         │
│  │   SSE Streaming  │  REST Endpoints      │         │
│  └──────────────────┼──────────────────────┘         │
└─────────────────────┼────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────┐
│                 Backend (FastAPI)                     │
│  ┌──────────────────────────────────────┐            │
│  │  /api/v1/tasks/decompose/stream      │  ◄── SSE  │
│  │  /api/v1/tasks/* (CRUD)              │            │
│  │  /api/v1/auth/* (JWT + OAuth)        │            │
│  │  /api/v1/users/* (Profile)           │            │
│  └───────────┬──────────────────────────┘            │
│              │                                       │
│  ┌───────────▼──────────────────────────┐            │
│  │  Services                             │            │
│  │  ├─ ai_service.py (Gemini + latency)  │            │
│  │  └─ pii_services.py (spaCy NER)      │            │
│  └───────────┬──────────────────────────┘            │
│              │                                       │
│  ┌───────────▼──────────────────────────┐            │
│  │  Security                             │            │
│  │  ├─ Fernet Encryption (AES-128)       │            │
│  │  ├─ bcrypt Password Hashing           │            │
│  │  └─ JWT Token Auth                    │            │
│  └───────────┬──────────────────────────┘            │
│              │                                       │
│  ┌───────────▼──────────────────────────┐            │
│  │  PostgreSQL (Encrypted at Rest)       │            │
│  │  ├─ users (neuro-profiles, streaks)   │            │
│  │  ├─ tasks (encrypted goals)           │            │
│  │  └─ micro_wins (encrypted actions)    │            │
│  └──────────────────────────────────────┘            │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 Judging Criteria Mapping

| Criteria | Weight | Implementation |
|---|---|---|
| **Technical Execution** | 30% | Streaming SSE, latency metering, async PostgreSQL, encrypted storage |
| **Neuro-Inclusive UX** | 25% | 4 font options, single-task view, muted palettes, mascot, gamification sounds |
| **AI Granularity** | 20% | Neuro-profile-personalized prompts, granularity 1-5, sensory-grounded actions |
| **Innovation** | 15% | PII masking, streak gamification, gamma wave audio, animated mascot |
| **Feasibility** | 10% | Docker build, this README, working auth + full CRUD |

---

## 📄 License

Built for the hackathon. MIT License.
