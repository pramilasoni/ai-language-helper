import json
from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)

client = OpenAI(api_key=OPENAI_API_KEY)


def create_plan(
    text: str,
    mode: str,
    target_language: str = None,
    previous_result: str = None,
    quality_feedback: str = None
):

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are a planner for an AI Language Helper.

Create a simple execution plan using only these tools:
- detect_language
- correct_text
- translate_text
- evaluate_quality

Rules:
- If mode is "correct", plan correction only.
- If mode is "translate", plan translation.
- If mode is "auto", choose translate_text ONLY if the user explicitly asks to translate.
- If mode is "auto" and the user only gives an incorrect sentence, choose correct_text.
- Do NOT choose translate_text just because target_language is provided.
- If translation is needed and the sentence has grammar issues, use correct_text before translate_text.
- Always finish with evaluate_quality.

Return ONLY valid JSON.

Example for correction:
{
  "goal": "correct grammar",
  "steps": [
    {"tool": "detect_language"},
    {"tool": "correct_text"},
    {"tool": "evaluate_quality"}
  ]
}

Example for translation:
{
  "goal": "translate text to Danish",
  "steps": [
    {"tool": "detect_language"},
    {"tool": "correct_text"},
    {"tool": "translate_text"},
    {"tool": "evaluate_quality"}
  ]
}
"""
            },
            {
                "role": "user",
                "content": f"""
Text:
{text}

Mode:
{mode}

Target language:
{target_language if target_language else "N/A"}

Previous result:
{previous_result if previous_result else "N/A"}

Quality feedback:
{quality_feedback if quality_feedback else "N/A"}
"""
            }
        ],
        temperature=DEFAULT_TEMPERATURE
    )

    content = response.choices[0].message.content.strip()

    return json.loads(content)