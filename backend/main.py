import logging
import os
import shutil
import uuid

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from services.correction_service import correct_text
from services.language_service import detect_language
from services.translation_service import translate_text
from services.orchestration_service import process_request
from services.speech_service import transcribe_audio
from services.tts_service import generate_speech

from schemas.request_schemas import (
    CorrectionRequest,
    LanguageDetectionRequest,
    TranslationRequest,
    ProcessRequest,
)

from schemas.response_schemas import (
    CorrectionResponse,
    LanguageDetectionResponse,
    TranslationResponse,
    ProcessResponse,
    VoiceProcessResponse,
    TranscriptionResponse,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Language Helper",
    description="Voice-based AI app for correction and translation",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/audio",
    StaticFiles(directory="audio_responses"),
    name="audio",
)


@app.get("/")
def home():
    return {
        "message": "AI Language Helper API is running"
    }


@app.post("/correct", response_model=CorrectionResponse)
def correct_sentence(request: CorrectionRequest):
    corrected = correct_text(request.text)

    return {
        "original_text": request.text,
        "corrected_text": corrected,
    }


@app.post(
    "/detect-language",
    response_model=LanguageDetectionResponse,
)
def detect_text_language(request: LanguageDetectionRequest):
    detected_language = detect_language(request.text)

    return {
        "text": request.text,
        "detected_language": detected_language,
    }


@app.post("/translate", response_model=TranslationResponse)
def translate_sentence(request: TranslationRequest):
    translated = translate_text(
        request.text,
        request.target_language,
    )

    return {
        "original_text": request.text,
        "target_language": request.target_language,
        "translated_text": translated,
    }


@app.post("/process", response_model=ProcessResponse)
def process_text(request: ProcessRequest):
    logger.info(f"[TEXT FLOW] Mode: {request.mode}")

    response = process_request(
        text=request.text,
        mode=request.mode,
        target_language=request.target_language,
    )

    if "error" in response:
        raise HTTPException(
            status_code=400,
            detail=response,
        )

    return response


@app.post("/transcribe", response_model=TranscriptionResponse)
def transcribe(file: UploadFile = File(...)):
    temp_file_path = f"temp_{uuid.uuid4()}_{file.filename}"

    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcription = transcribe_audio(temp_file_path)

        return {
            "transcribed_text": transcription,
        }

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


@app.post("/voice-process", response_model=VoiceProcessResponse)
def process_voice(
    mode: str = Form(...),
    target_language: str = Form(None),
    file: UploadFile = File(...),
):
    temp_file_path = f"temp_{uuid.uuid4()}_{file.filename}"

    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcribed_text = transcribe_audio(temp_file_path)

        logger.info(
            f"[VOICE FLOW] Transcribed text: {transcribed_text}"
        )

        response = process_request(
            text=transcribed_text,
            mode=mode,
            target_language=target_language,
        )

        logger.info(f"[VOICE FLOW] Mode: {mode}")
        logger.info(f"[VOICE FLOW] Workflow response: {response}")

        if "error" in response:
            raise HTTPException(
                status_code=400,
                detail=response,
            )

        result_text = response["result_text"]

        audio_filename = f"{uuid.uuid4()}.mp3"
        audio_output_path = f"audio_responses/{audio_filename}"

        generate_speech(
            text=result_text,
            output_file=audio_output_path,
        )

        return {
            "transcribed_text": transcribed_text,
            "response": response,
            "audio_response_url": f"/audio/{audio_filename}",
        }

    except HTTPException:
        raise

    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)