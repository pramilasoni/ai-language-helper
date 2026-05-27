from config import (
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)
from services.openai_client import client


def translate_text(text: str, target_language: str):

    prompt = f"""
    Translate the following text into {target_language}.

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a professional translation assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=DEFAULT_TEMPERATURE
    )

    return response.choices[0].message.content.strip()


#Grammar correction	✅
#Language detection	✅
#Translation	✅
#Service architecture	✅
#FastAPI backend	✅
#OpenAI integration	✅