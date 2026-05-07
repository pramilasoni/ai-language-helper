from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    TTS_MODEL,
    TTS_VOICE,
    DEFAULT_TEMPERATURE
)
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_speech(text: str, output_file: str):

    response = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text
    )

    response.stream_to_file(output_file)