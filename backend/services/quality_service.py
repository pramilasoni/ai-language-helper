import json
import logging

from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    CHAT_MODEL,
    DEFAULT_TEMPERATURE
)

logger = logging.getLogger(__name__)

client = OpenAI(api_key=OPENAI_API_KEY)


def evaluate_response(
    original_text: str,
    ai_response: str,
    mode: str,
    target_language: str = None
):
    try:
        response = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a quality evaluator for an AI Language Helper.

Evaluate the AI response based on the task.

Rules:
- For correction: grammar should be improved, meaning preserved
- For translation: output should be in the target language and meaningful
- Minor wording differences are OK
- Do NOT penalize if output is reasonable
- Do NOT be overly strict

Return ONLY valid JSON:

{
  "score": number from 1 to 10,
  "feedback": "short explanation"
}
"""
                },
                {
                    "role": "user",
                    "content": f"""
Original Text:
{original_text}

Mode:
{mode}

Target Language:
{target_language if target_language else "N/A"}

AI Response:
{ai_response}
"""
                }
            ],
            temperature=DEFAULT_TEMPERATURE
        )

        content = response.choices[0].message.content.strip()

        logger.info(f"[QUALITY RAW] {content}")

        parsed = json.loads(content)

        # safety checks
        score = parsed.get("score", 5)
        feedback = parsed.get("feedback", "No feedback")

        return {
            "score": int(score),
            "feedback": feedback
        }

    except Exception as e:
        logger.error(f"[QUALITY ERROR] {str(e)}")

        # fallback (very important)
        return {
            "score": 5,
            "feedback": "Quality evaluation fallback used"
        }