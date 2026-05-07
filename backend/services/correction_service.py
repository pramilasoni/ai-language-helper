from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


def correct_text(text: str):

    prompt = f"""
    Correct the grammar and improve the vocabulary
    of the following sentence.

    Sentence:
    {text}
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are an English language correction assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],     
        temperature= DEFAULT_TEMPERATURE
    )

    return response.choices[0].message.content


#You already now have:

#AI-powered backend
#FastAPI API
#Service layer
#Environment variable handling
#Input validation
#LLM integration
#Production-style structure