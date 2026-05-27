from config import (
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)
from services.openai_client import client

def detect_language(text: str) -> str:
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You detect the language of the given text. Return only the language name, nothing else."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=DEFAULT_TEMPERATURE
    )

    return response.choices[0].message.content.strip()