def build_evaluation_prompt(original_text: str, practice_language: str):
    return f"""
You are an AI language tutor.

The user is practicing:
{practice_language}

Evaluate the sentence.

Return ONLY valid JSON.

User sentence:
"{original_text}"

Tasks:
1. Correct grammar mistakes
2. Translate the corrected sentence into English
3. Give language score from 0-100
4. Give feedback about mistakes

JSON format:

{{
  "corrected_text": "",
  "english_translation": "",
  "score": 0,
  "feedback": [
    {{
      "issue": "",
      "suggestion": ""
    }}
  ]
}}
"""