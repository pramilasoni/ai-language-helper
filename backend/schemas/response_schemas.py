from typing import List
from pydantic import BaseModel

# -------------------------
# Voice workflow responses
# -------------------------

class FeedbackItem(BaseModel):
    issue: str
    suggestion: str


class VoiceTranslationResponse(BaseModel):
    original_text: str
    corrected_text: str
    translated_text: str
    audio_response_url: str | None = None


class VoicePerfectionResponse(BaseModel):
    original_text: str
    corrected_text: str
    english_translation: str
    score: int
    feedback: List[FeedbackItem]
    audio_response_url: str | None = None

# -------------------------
# Legacy response schemas
# -------------------------




class CorrectionResponse(BaseModel):
    original_text: str
    corrected_text: str


class LanguageDetectionResponse(BaseModel):
    text: str
    detected_language: str


class TranslationResponse(BaseModel):
    original_text: str
    target_language: str
    translated_text: str


class ProcessResponse(BaseModel):
    mode: str
    detected_language: str
    original_text: str
    result_text: str
    target_language: str | None = None


    
class TranscriptionResponse(BaseModel):
    transcribed_text: str