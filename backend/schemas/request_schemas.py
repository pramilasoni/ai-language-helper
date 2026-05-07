from enum import Enum
from pydantic import BaseModel


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