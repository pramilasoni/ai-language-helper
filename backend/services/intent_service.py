from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)

client = OpenAI(api_key=OPENAI_API_KEY)


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
    if intent not in ["correct", "translate"]:
        
        return "correct"

    return intent