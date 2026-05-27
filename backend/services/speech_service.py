from config import (
    WHISPER_MODEL
)
from services.openai_client import client


def transcribe_audio(audio_file_path: str):

    with open(audio_file_path, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            model=WHISPER_MODEL,
            file=audio_file
        )

    return transcription.text