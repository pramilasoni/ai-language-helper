# 🚀 AI Language Helper

AI Language Helper is a production-oriented AI-powered language learning assistant built with **React**, **FastAPI**, and **OpenAI APIs**.

The application supports both text and voice workflows for:

- 🎙️ Real-time voice translation
- 🧠 AI-powered grammar correction
- 📈 Language evaluation and scoring
- 🔊 Text-to-speech audio generation
- 🌍 Multi-language learning workflows
- 🤖 Agentic AI orchestration patterns

This project was built to explore practical AI backend architecture, multimodal AI workflows, speech systems, orchestration logic, evaluation loops, and scalable service-oriented backend design.

---

# ✨ Features

## 🎧 Translation Mode

Speak in one language and receive:

- Speech-to-text transcription
- Grammar correction
- Translation into another language
- AI-generated translated audio response

### Example Workflow

```text
Speech
→ Whisper STT
→ AI Correction
→ AI Translation
→ Text-to-Speech Audio
```

---

## 🏆 Perfection Mode

Practice speaking a language and receive:

- Grammar correction
- English meaning
- AI evaluation score
- Detailed improvement feedback
- Corrected pronunciation audio

### Example Workflow

```text
Speech
→ Whisper STT
→ AI Evaluation
→ Grammar Correction
→ English Translation
→ Score + Feedback
→ Corrected Audio
```

---

# 🏗️ High-Level Architecture

```text
Frontend (React)
        ↓
FastAPI Backend
        ↓
Speech-to-Text (Whisper)
        ↓
AI Workflow Orchestration
   ↙                ↘
Translation Flow   Perfection Flow
        ↓
OpenAI LLM
        ↓
Structured JSON Responses
        ↓
Text-to-Speech Generation
        ↓
Frontend Audio Playback
```

---

# 🤖 Agentic AI Workflow

The application follows a lightweight agentic architecture pattern.

Instead of relying on a single LLM call, the backend separates execution into multiple stages:

1. Understand user intent
2. Create execution flow
3. Run language tools step-by-step
4. Evaluate output quality
5. Retry or improve when necessary
6. Return both text and audio responses

This project explores practical AI orchestration patterns such as:

- Planner–Executor workflows
- Tool orchestration
- Evaluation loops
- Multi-step AI execution
- Structured AI responses
- Service-based AI architecture

---

# 🧠 Translation Workflow

```text
User Voice
→ Speech Transcription
→ Grammar Correction
→ Translation
→ Audio Generation
→ Frontend Response
```

---

# 🧠 Perfection Workflow

```text
User Voice
→ Speech Transcription
→ Language Evaluation
→ Grammar Analysis
→ English Translation
→ AI Scoring
→ Feedback Generation
→ Corrected Audio
```

---

# 📁 Project Structure

```text
ai-language-helper/
│
├── backend/
│   ├── main.py
│   │
│   ├── services/
│   │   ├── correction_service.py
│   │   ├── language_evaluator.py
│   │   ├── language_service.py
│   │   ├── openai_client.py
│   │   ├── orchestration_service.py
│   │   ├── planner_service.py
│   │   ├── quality_service.py
│   │   ├── speech_service.py
│   │   ├── tool_agent_service.py
│   │   ├── translation_service.py
│   │   └── tts_service.py
│   │
│   ├── prompts/
│   │   └── evaluation_prompt.py
│   │
│   ├── schemas/
│   │   ├── request_schemas.py
│   │   └── response_schemas.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   ├── audio_responses/
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── api/
│   │   └── App.jsx
│
└── README.md
```

---

# ⚙️ Technologies Used

## Frontend

- React
- Vite
- Axios
- CSS

---

## Backend

- Python
- FastAPI
- Pydantic
- OpenAI SDK

---

## AI & Speech

- GPT-4o-mini
- Whisper-1
- OpenAI TTS

---

# 🚀 Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/pramilasoni/ai-language-helper.git

cd ai-language-helper
```

---

## 2. Backend Setup

```bash
cd backend

pip install -r requirements.txt
```

Create `.env`

```env
OPENAI_API_KEY=your_openai_api_key
```

Run backend:

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# 🎯 API Endpoints

## Translation Workflow

```text
POST /voice-translate
```

### Input

- source language
- target language
- audio file

### Output

- corrected text
- translated text
- translated audio

---

## Perfection Workflow

```text
POST /voice-perfect
```

### Input

- practice language
- audio file

### Output

- corrected text
- English translation
- language score
- improvement feedback
- corrected audio

---

# 📊 AI Evaluation Example

## User Input

```text
Jeg gå til skole i går
```

---

## AI Response

### Corrected Text

```text
Jeg gik i skole i går
```

### English Translation

```text
I went to school yesterday
```

### Score

```text
82/100
```

### Feedback

```text
- Incorrect verb tense
- Improved sentence structure
```

---

# 🛠️ Production-Oriented Design Decisions

This project intentionally follows production-style architecture principles:

- Service-based backend organization
- Centralized OpenAI client
- Modular AI workflows
- Structured request/response schemas
- Voice workflow separation
- Prompt modularization
- Audio lifecycle management
- AI evaluation pipelines
- Environment-based configuration
- Logging standardization
- Multi-step orchestration logic

---

# 🚀 Future Improvements

## AI Improvements

- Pronunciation scoring
- Conversation practice mode
- Adaptive feedback
- Session memory
- Personalized learning paths

---

## Engineering Improvements

- Docker deployment
- Kubernetes deployment
- Redis caching
- CI/CD pipelines
- Monitoring & observability
- Rate limiting
- Async processing
- Persistent database storage
- Streaming audio responses

---

# 📚 Learning Outcomes

This project helped strengthen understanding of:

- AI orchestration patterns
- Agentic workflows
- Multimodal AI systems
- Speech-to-text pipelines
- Text-to-speech generation
- FastAPI backend architecture
- Service-oriented backend design
- Evaluation and retry loops
- Production-style AI system design
- Real-time AI workflow integration

---

# 👨‍💻 Author

Built by Pramila Soni as part of a hands-on AI engineering and solution architecture learning journey focused on:

- AI applications
- Agentic AI systems
- LLM orchestration
- Multimodal workflows
- Cloud-native backend architecture
- Production-ready AI system design

---

# 🔗 Repository

GitHub Repository:

https://github.com/pramilasoni/ai-language-helper