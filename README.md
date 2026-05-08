# AI Language Helper

## Overview

AI Language Helper is an agentic AI application that helps users improve communication through grammar correction, translation, and speech-based interactions.

The system supports both text and voice input and uses a planner–executor–evaluator workflow to dynamically decide how language tasks should be processed.

Instead of relying on a single LLM call, the application follows a multi-step orchestration approach where the system:

1. Understands the user request
2. Creates an execution plan
3. Runs language tools step-by-step
4. Evaluates output quality
5. Re-plans when quality is insufficient
6. Returns both text and audio responses

This project was built to explore practical AI backend architecture patterns, agentic workflows, orchestration logic, and production-style service separation.

---

# Features

- Speech-to-text transcription using Whisper
- Grammar and vocabulary correction
- Text translation between languages
- Combined correction + translation workflow
- Automatic language detection
- Planner-based AI orchestration
- Tool execution pipeline
- Output evaluation and retry loop
- Text-to-speech audio responses
- FastAPI backend architecture
- React frontend interface
- Modular service-based design

---

# High-Level Architecture

```text
User Speech/Text
        ↓
FastAPI API Endpoint
        ↓
Whisper Transcription (optional)
        ↓
Planner (LLM creates execution plan)
        ↓
Executor (runs tools step-by-step)
        ↓
Evaluator (checks response quality)
        ↓
Re-planning if quality is low
        ↓
Final Response
        ↓
Text-to-Speech Generation
        ↓
Audio Response Returned
```

---

# Agentic AI Workflow

The core idea behind this project is the use of an agentic architecture.

Instead of directly asking an LLM to generate the final answer in one step, the system separates the workflow into multiple stages:

## 1. Planner

The planner receives the user request and creates a structured execution plan.

Example:

```json
[
  {
    "tool": "correct_text",
    "input": "I has a apple"
  },
  {
    "tool": "translate_text",
    "target_language": "Danish"
  }
]
```

---

## 2. Executor

The executor runs tools step-by-step.

Example tools:

- `correct_text`
- `translate_text`
- `detect_language`
- `generate_speech`

The output from one step becomes the input for the next step.

Example:

```text
I has a apple
→ I have an apple
→ Jeg har et æble
```

---

## 3. Evaluator

The evaluator reviews the final response quality.

The system checks:

- grammar quality
- translation quality
- response completeness
- execution success

A quality score is generated.

---

## 4. Re-planning Loop

If the quality score is below the threshold, the planner generates an improved execution plan and retries the workflow.

This creates a lightweight autonomous AI execution loop.

---

# Tech Stack

## Backend

- Python
- FastAPI
- Pydantic
- OpenAI API
- Whisper

## Frontend

- React
- Vite
- JavaScript

## AI Architecture Concepts

- Agentic AI
- Planner–Executor pattern
- Evaluation loops
- Tool orchestration
- Service modularization
- AI workflow orchestration

---

# Project Structure

```text
backend/
│
├── providers/
│   └── LLM and AI provider integrations
│
├── routers/
│   └── FastAPI API endpoints
│
├── schemas/
│   └── Pydantic request/response models
│
├── services/
│   ├── orchestration_service.py
│   ├── tool_agent_service.py
│   ├── translation_service.py
│   ├── correction_service.py
│   ├── tts_service.py
│   └── transcription_service.py
│
└── main.py

frontend/
│
├── React UI
├── Audio recording support
└── API integration
```

---

# API Flow Example

## Input

```json
{
  "text": "I has a apple",
  "mode": "correct_translate",
  "target_language": "Danish"
}
```

---

## Internal Workflow

```text
1. Detect language
2. Create execution plan
3. Correct grammar
4. Translate corrected text
5. Evaluate quality
6. Return final response
```

---

## Output

```json
{
  "result_text": "Jeg har et æble"
}
```

---

# Running the Project

## Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Frontend

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

# Future Improvements

Potential future enhancements:

- Conversation memory
- Session context handling
- LangGraph integration
- Streaming responses
- Vector database memory
- Multi-agent orchestration
- Observability dashboards
- User authentication
- Persistent conversation history
- Real-time speech streaming

---

# Learning Outcomes

This project helped strengthen understanding of:

- AI orchestration patterns
- Agentic workflows
- LLM planning strategies
- Multi-step AI execution
- FastAPI backend architecture
- Service-based backend design
- Speech-to-text pipelines
- Text-to-speech integration
- Evaluation and retry loops
- Production-style AI system design

---

# Repository

GitHub Repository:

https://github.com/pramilasoni/ai-language-helper