from pydantic import BaseModel

from enum import Enum
class VoiceTranslationRequest(BaseModel):
    source_language: str
    target_language: str


class VoicePerfectionRequest(BaseModel):
    practice_language: str
    translation_language: str


class ProcessingMode(str, Enum):
    correct = "correct"
    translate = "translate"
    auto = "auto"


class CorrectionRequest(BaseModel):
    text: str


class LanguageDetectionRequest(BaseModel):
    text: str


class TranslationRequest(BaseModel):
    text: str
    target_language: str


class ProcessRequest(BaseModel):
    text: str
    mode: ProcessingMode
    target_language: str | None = None