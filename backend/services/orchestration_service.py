from services.language_service import detect_language
from services.tool_agent_service import run_tool_agent

import logging

logger = logging.getLogger(__name__)


def process_request(
    text: str,
    mode: str,
    target_language: str = None
):
    detected_language = detect_language(text)
    logger.info(f"[AI FLOW] Detected language: {detected_language}")

    agent_result = run_tool_agent(
        text=text,
        mode=mode,
        target_language=target_language
    )

    return {
        "mode": agent_result.get("mode", mode),
        "detected_language": detected_language,
        "original_text": text,
        "target_language": target_language,
        "result_text": agent_result.get("result_text"),
        "quality": agent_result.get("quality"),
        "steps": agent_result.get("steps")
    }