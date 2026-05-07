import os
from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHAT_MODEL = "gpt-4.1-mini"

TTS_MODEL = "gpt-4o-mini-tts"

TTS_VOICE = "alloy"

WHISPER_MODEL = "whisper-1"

DEFAULT_TEMPERATURE = 0