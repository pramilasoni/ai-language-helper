
from config import (
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)

from services.openai_client import client


def detect_intent(text: str) -> str:
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are an intent router for an AI language helper.

Classify the user's intent into only one of these:
- correct
- translate

Return only the intent word.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=DEFAULT_TEMPERATURE
    )

    return response.choices[0].message.content.strip().lower()
    intent = (
    response.choices[0]
    .message
    .content
    .strip()
    .lower()
    )

    if intent not in ["correct", "translate"]:
        return "correct"

    return intent
