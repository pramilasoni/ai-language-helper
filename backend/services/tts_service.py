from config import (
    TTS_MODEL,
    TTS_VOICE
)
from services.openai_client import client


def generate_speech(text: str, output_file: str):

    response = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text
    )

    response.stream_to_file(output_file)