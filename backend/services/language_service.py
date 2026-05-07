from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

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