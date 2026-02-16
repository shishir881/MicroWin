# MicroWin 🧠⚡ — Presentation Slide Deck Content

> **Suggested Slides:** 12–15 | **Time:** 5–7 min pitch  
> **Design Tip:** Use warm orange/brown tones, muted pastels, large readable fonts (Verdana or Inter)

---

## Slide 1 — Title Slide

- **Title:** MicroWin 🧠⚡
- **Subtitle:** Big Goals. Micro Wins.
- **Tagline:** An AI-powered executive function coach for neurodivergent learners
- **Visual:** App logo + screenshot of landing page hero

---

## Slide 2 — The Problem

- **Heading:** The Challenge
- **Bullets:**
  - 1 in 5 children are neurodivergent (ADHD, Autism, Dyslexia)
  - Task paralysis — big goals feel impossible to start
  - Existing productivity tools are NOT designed for neuro-inclusive needs
  - Kids lose confidence when they can't break tasks into steps
- **Visual:** Simple illustration of an overwhelmed child looking at a long to-do list

---

## Slide 3 — Our Solution

- **Heading:** Meet MicroWin
- **Bullets:**
  - AI-powered coach that breaks any goal into 3–5 tiny, achievable micro-wins
  - Personalized for each user's neuro-profile and struggle areas
  - Sensory-grounded action steps (concrete, not abstract)
  - Gamified experience with mascot, sounds, confetti, and streaks
- **Visual:** Screenshot of Dashboard with quest card visible

---

## Slide 4 — How It Works

- **Heading:** 4 Simple Steps
- **Step 1:** Tell the AI your goal or challenge
- **Step 2:** Get personalized micro-win suggestions
- **Step 3:** Complete one small step at a time
- **Step 4:** Build confidence and momentum daily
- **Visual:** Screenshot of "How it Works" section from landing page, or a simple flow diagram

---

## Slide 5 — Live Demo / Screenshots

- **Heading:** MicroWin in Action
- **Show 3–4 screenshots in a carousel or grid:**
  1. Landing Page — hero section
  2. Dashboard — welcome screen with Polo mascot + stats
  3. Quest in progress — step card with "I DID IT!" button
  4. Quest complete — confetti + trophy celebration
- **Note:** If presenting live, do the demo here instead of screenshots

---

## Slide 6 — Key Features

- **Heading:** What Makes MicroWin Special

| Feature | Detail |
|---|---|
| 🤖 AI Micro-Win Decomposition | Goals → 3–5 sensory-grounded steps via Gemini 2.5 Flash |
| ⚡ < 5s Latency | Streaming SSE with real-time latency displayed |
| 🧩 Neuro-Profiles | Encrypted struggle areas, preferences, granularity (1–5) |
| 🎮 Gamification | Streaks 🔥, trophies 🏆, confetti, varied sound effects |
| 🐻 Mascot (Polo) | Animated companion — idle, thinking, happy, celebrating |
| 🔤 Neuro-Inclusive Fonts | Inter, Verdana, OpenDyslexic, Lexend |
| 🎵 Gamma Wave Focus Music | Built-in binaural beat player |
| 🌗 Dark / Light Mode | Warm brown dark mode with muted palettes |

---

## Slide 7 — Privacy & Security

- **Heading:** Privacy-First Architecture
- **Bullets:**
  - **PII Masking:** spaCy NER scrubs names, locations & orgs BEFORE the LLM sees any data
  - **Encryption at Rest:** Fernet AES-128 for all goals, micro-wins, and profiles
  - **Password Security:** bcrypt hashing
  - **Auth:** JWT tokens + Google OAuth2
  - No personal data is ever sent to the AI unmasked
- **Visual:** Simple data flow diagram: User → PII Mask → AI → Encrypted DB

---

## Slide 8 — Neuro-Inclusive Design

- **Heading:** Designed for Every Brain
- **Bullets:**
  - Single-task view — only one step visible at a time (reduces overwhelm)
  - Large "I DID IT!" button — tactile, satisfying interaction
  - Muted color palettes — no flashing, no neon, no eye strain
  - 4 font options including OpenDyslexic and Lexend
  - Warm, friendly mascot provides emotional support
  - Sound effects and confetti for positive reinforcement
- **Visual:** Side-by-side of light/dark mode dashboard

---

## Slide 9 — Tech Stack

- **Heading:** Under the Hood

| Layer | Technology |
|---|---|
| Frontend | React 19, Vite 7, TypeScript, Tailwind CSS 4, Framer Motion |
| Backend | FastAPI (async), SQLAlchemy 2 (async), PostgreSQL |
| AI | Google Gemini 2.5 Flash via `google-genai` SDK |
| Privacy | spaCy NER (PII masking), Fernet encryption (AES-128-CBC) |
| Auth | JWT (`python-jose`) + Google OAuth2 |
| Deployment | Docker multi-stage build |

- **Visual:** Architecture diagram (use the one from the README)

---

## Slide 10 — Architecture Diagram

- **Heading:** System Architecture
- **Content:** Use the diagram from the README showing:
  - Frontend (React) → API Layer (SSE + REST)
  - Backend (FastAPI) → Services (AI, PII) → Security (Encryption, Hashing, JWT)
  - PostgreSQL with encrypted tables (users, tasks, micro_wins)
- **Visual:** Render the ASCII diagram as a clean graphic

---

## Slide 11 — AI Personalization

- **Heading:** Adaptive AI Granularity
- **Bullets:**
  - Each user has a neuro-profile with struggle areas and preferences
  - Granularity scale (1–5): from broad steps to extremely detailed micro-actions
  - Profile data is encrypted and used to personalize prompts
  - Gemini generates sensory-grounded, actionable steps tailored to the user
- **Example:**
  - Goal: *"Clean my room"*
  - Micro-Win: *"Pick up the 3 things closest to your feet and put them on your bed"*

---

## Slide 12 — Judging Criteria Mapping

- **Heading:** How We Meet the Criteria

| Criteria | Weight | Our Implementation |
|---|---|---|
| Technical Execution | 30% | Streaming SSE, latency metering, async PostgreSQL, encrypted storage |
| Neuro-Inclusive UX | 25% | 4 fonts, single-task view, muted palettes, mascot, gamification |
| AI Granularity | 20% | Neuro-profile-personalized prompts, granularity 1–5, sensory-grounded |
| Innovation | 15% | PII masking, streak gamification, gamma wave audio, animated mascot |
| Feasibility | 10% | Docker build, full README, working auth + full CRUD |

---

## Slide 13 — Impact & Vision

- **Heading:** The Bigger Picture
- **Bullets:**
  - Helps neurodivergent kids build executive function skills independently
  - Turns "I can't do this" into "I just did that!" — one step at a time
  - Future: parent/teacher dashboards, more gamification, mobile app
  - Scalable to schools, therapy centers, and homes
- **Visual:** Quote or testimonial-style text: *"Every micro-win builds a mountain of confidence."*

---

## Slide 14 — Thank You / Q&A

- **Title:** Thank You! 🙏
- **Subtitle:** Big goals. Micro wins. Start winning today.
- **Content:**
  - GitHub: `github.com/your-repo/MicroWin`
  - Team members & roles
  - QR code to live demo (if deployed)
- **Visual:** App logo + Polo mascot celebrating

---

## 🎨 Design Recommendations

| Element | Suggestion |
|---|---|
| **Color palette** | Primary: `#d97706` (warm amber), Dark BG: `#2C241B`, Light BG: `#FFF7ED` |
| **Fonts** | Headings: Inter Bold or Verdana Bold, Body: Inter / Verdana |
| **Icons** | Use Lucide icons (same as the app) for consistency |
| **Slide BG** | Use a subtle gradient or warm muted tones, not pure white |
| **Animations** | Minimal — fade/slide only, no flashy transitions (neuro-inclusive!) |
| **Screenshots** | Take in dark mode for a premium feel on projectors |
