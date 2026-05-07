from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


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