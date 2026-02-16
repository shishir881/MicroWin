# MicroWin 🧠⚡ — Video Walkthrough Script

> **Estimated Length:** 2–3 minutes  
> **Tone:** Warm, enthusiastic, accessible  
> **Audience:** Hackathon judges / general viewers

---

## SCENE 1 — Opening Hook (0:00 – 0:15)

**[Screen: Landing Page — hero section visible]**

> *"What if a single, overwhelming goal could be broken into tiny steps — personalized just for you? Meet MicroWin — an AI-powered executive function coach built for neurodivergent learners."*

---

## SCENE 2 — Landing Page Tour (0:15 – 0:35)

**[Scroll down the Landing Page slowly]**

> *"The landing page introduces the concept: Big goals, micro wins. MicroWin is designed especially for kids with autism and dyslexia to overcome task paralysis."*

**[Scroll to "How it Works" section — let the step-by-step animations play]**

> *"The process is simple — four steps:*
> 1. *Tell the AI your goal,*
> 2. *Get personalized micro-win suggestions,*
> 3. *Complete one small step at a time, and*
> 4. *Build confidence and momentum daily."*

**[Point out the Font Switcher in the nav bar — click through options]**

> *"Notice the font switcher — users can toggle between Inter, Verdana, OpenDyslexic, and Lexend for a fully neuro-inclusive reading experience."*

---

## SCENE 3 — Sign Up / Login (0:35 – 0:55)

**[Click "Start for free" → navigate to Sign Up page]**

> *"Signing up is quick. Users can create an account with email and password, or use Google OAuth for one-click login."*

**[Show the Sign Up form briefly, then navigate to Login page]**

> *"All passwords are securely hashed with bcrypt, and sessions use JWT tokens."*

**[Log in with a demo account]**

---

## SCENE 4 — Welcome & Dashboard Overview (0:55 – 1:25)

**[Dashboard loads — show Welcome Modal if it appears]**

> *"First-time users are greeted by a Welcome Modal where they can set their name."*

**[Welcome screen visible — show the Mascot (Polo), stats cards, and greeting]**

> *"The dashboard greets users by name. Meet Polo — our animated mascot companion who reacts to your progress. You'll also see your stats at a glance: total Quests, your current Streak 🔥, and completed tasks."*

**[Point out the sidebar — Mission Log, New Quest button]**

> *"The sidebar shows your Mission Log — a history of all your quests. You can jump back into any past quest or start a new one."*

**[Point out the header toolbar — Gamma Wave player, Settings, Font Switcher, Dark/Light toggle]**

> *"The toolbar includes a Gamma Wave binaural beat player for focus, a font switcher, preferences panel, and a dark/light mode toggle."*

---

## SCENE 5 — Creating a Quest (1:25 – 2:00)

**[Click into the input area, type a goal like: "I want to clean my room but it feels too overwhelming"]**

> *"Let's create a quest. The user types a goal — it can be something that feels overwhelming."*

**[Press Enter — show Polo switching to "thinking" mode, the loading state]**

> *"Polo starts thinking! Behind the scenes, the goal is sent to Google Gemini 2.5 Flash. But first, spaCy NER masks any personal information — names, locations, organizations — before it ever reaches the AI. The response streams back via Server-Sent Events in under 5 seconds."*

**[Steps appear — show the latency badge and the Step card]**

> *"The AI breaks the goal into 3–5 sensory-grounded micro-steps. Notice the real-time latency counter — we display time-to-first-token right in the UI."*

---

## SCENE 6 — Completing Steps & Gamification (2:00 – 2:30)

**[Show the current step card — large text, single-task view]**

> *"Each step is shown one at a time — a single-task view that reduces overwhelm. The action is displayed in large, clear text."*

**[Click "I DID IT!" button]**

> *"When you complete a step, you press 'I DID IT!' Polo celebrates, a motivating sound plays, and you get instant positive feedback."*

**[Complete another step — show the progress bar advancing]**

> *"The progress bar fills as you advance. Each sub-step plays a different motivating sound to keep things engaging."*

**[Complete the final step — show confetti, celebration sound, Quest Complete screen]**

> *"When the quest is fully complete — confetti explodes! 🎉 Polo goes into full celebration mode, a special completion sound plays, and the Quest Complete screen appears with a trophy. Your streak and completion count update in real-time."*

---

## SCENE 7 — Privacy & Security (2:30 – 2:45)

**[Toggle to Settings / briefly show the app architecture]**

> *"Privacy is built into every layer. All stored goals, micro-wins, and neuro-profiles are encrypted at rest with Fernet AES-128 encryption. PII is masked before it reaches the LLM. And JWT + OAuth2 handle authentication securely."*

---

## SCENE 8 — Closing (2:45 – 3:00)

**[Return to Dashboard — show Polo in idle/happy state]**

> *"MicroWin turns overwhelming goals into daily progress — one micro-win at a time. It's built with empathy, designed for neurodivergent learners, and powered by cutting-edge AI."*

**[Fade to logo or Landing Page hero]**

> *"Big goals. Micro wins. Start winning today."*

---

## 📋 Recording Tips

| Tip | Detail |
|---|---|
| **Resolution** | Record at 1920×1080 (1080p) minimum |
| **Browser** | Use Chrome or Edge with no extensions visible |
| **Tab** | Only the MicroWin tab should be open |
| **Cursor** | Use a large, visible cursor or spotlight effect |
| **Audio** | Record voiceover separately for cleaner audio, or use a quiet room |
| **Pace** | Pause 1–2 seconds on each key screen for viewers to absorb |
| **Dark Mode** | Consider recording in dark mode — it looks premium on video |
