from services.language_service import detect_language
from services.correction_service import correct_text
from services.translation_service import translate_text


def process_request(
    text: str,
    mode: str,
    target_language: str = None
):

    detected_language = detect_language(text)

    if mode == "correct":

        result = correct_text(text)

        return {
            "mode": mode,
            "detected_language": detected_language,
            "original_text": text,
            "result_text": result
        }

    elif mode == "translate":

        result = translate_text(
            text,
            target_language
        )

        return {
            "mode": mode,
            "detected_language": detected_language,
            "target_language": target_language,
            "original_text": text,
            "result_text": result
        }

    else:

        return {
            "error": "Invalid mode"
        }