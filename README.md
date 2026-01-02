# StudyGuard AI

**An ethical AI study assistant that helps students learn — not cheat.**

## Overview
StudyGuard AI is a web app designed to promote understanding and independent learning. It explains concepts step-by-step, generates practice questions, and refuses to provide direct answers for graded assignments.

## Features
- Ethical AI with guardrails
- Step-by-step explanations
- Practice question generation
- Refuses to cheat on homework, tests, or quizzes
- Runs locally — no OpenAI API key required

## Tech Stack
- Python + Flask (backend)
- GPT4All (local LLM)
- HTML / CSS / JS (frontend)

## Model
- **Phi‑3 Mini** (local, ~2 GB)  
- Placed in `models/phi-3-mini.bin`  
- Ensures the AI can run locally without API keys

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/player-is-afk/Studyguard.git
