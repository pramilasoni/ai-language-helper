from pydantic import BaseModel


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


class VoiceProcessResponse(BaseModel):
    transcribed_text: str
    response: ProcessResponse
    audio_response_url: str | None = None
    
class TranscriptionResponse(BaseModel):
    transcribed_text: str