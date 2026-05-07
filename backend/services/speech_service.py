from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    DEFAULT_TEMPERATURE,WHISPER_MODEL
)
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


def transcribe_audio(audio_file_path: str):

    with open(audio_file_path, "rb") as audio_file:

        transcription = client.audio.transcriptions.create(
            model=WHISPER_MODEL,
            file=audio_file
        )

    return transcription.text