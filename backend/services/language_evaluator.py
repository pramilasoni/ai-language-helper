import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from prompts.evaluation_prompt import (
    build_evaluation_prompt,
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def evaluate_language(
    original_text: str,
    practice_language: str,
):

    prompt = build_evaluation_prompt(
        original_text,
        practice_language,
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":
                    "You are a language tutor.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.2,
    )

    content = (
        response.choices[0]
        .message
        .content
    )

    return json.loads(content)