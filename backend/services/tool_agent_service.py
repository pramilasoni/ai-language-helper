
import logging
from services.language_service import detect_language
from services.correction_service import correct_text
from services.translation_service import translate_text
from services.quality_service import evaluate_response
from services.planner_service import create_plan
import json
logger = logging.getLogger(__name__)



tools = [
    {
        "type": "function",
        "function": {
            "name": "detect_language",
            "description": "Detect the language of the input text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "correct_text",
            "description": "Correct grammar and improve vocabulary while preserving meaning.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"}
                },
                "required": ["text"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "translate_text",
            "description": "Translate text into a target language.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "target_language": {"type": "string"}
                },
                "required": ["text", "target_language"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "evaluate_quality",
            "description": "Evaluate quality of correction or translation response.",
            "parameters": {
                "type": "object",
                "properties": {
                    "original_text": {"type": "string"},
                    "ai_response": {"type": "string"},
                    "mode": {"type": "string"},
                    "target_language": {"type": "string"}
                },
                "required": ["original_text", "ai_response", "mode"]
            }
        }
    }
]


def execute_tool(tool_name: str, arguments: dict):
    logger.info(f"[TOOL CALL] {tool_name} with {arguments}")

    if tool_name == "detect_language":
        return detect_language(arguments["text"])

    if tool_name == "correct_text":
        return correct_text(arguments["text"])

    if tool_name == "translate_text":
        return translate_text(
            arguments["text"],
            arguments.get("target_language", "Danish")
        )

    if tool_name == "evaluate_quality":
        return evaluate_response(
            original_text=arguments["original_text"],
            ai_response=arguments["ai_response"],
            mode=arguments["mode"],
            target_language=arguments.get("target_language")
        )

    raise ValueError(f"Unknown tool: {tool_name}")

def run_tool_agent(
    text: str,
    mode: str,
    target_language: str = None
):
    max_attempts = 3
    quality_threshold = 7

    previous_result = None
    quality_feedback = None

    best_result = None
    best_quality = None

    full_trace = {
        "input": text,
        "mode": mode,
        "target_language": target_language,
        "attempts": [],
        "final_result": None,
        "final_quality": None
    }

    for attempt in range(max_attempts):

        logger.info(f"[AGENT LOOP] Attempt {attempt + 1}")

        plan = create_plan(
            text=text,
            mode=mode,
            target_language=target_language,
            previous_result=previous_result,
            quality_feedback=quality_feedback
        )

        context = {
            "text": text,
            "original_text": text,
            "mode": mode,
            "target_language": target_language,
            "result": previous_result,
            "quality": None,
            "detected_language": None
        }

        attempt_trace = {
            "attempt": attempt + 1,
            "plan": plan,
            "steps": [],
            "result": None,
            "quality": None
        }

        steps = plan.get("steps", [])

        for step in steps:
            tool_name = step.get("tool")

            tool_input = {}
            tool_output = None

            if tool_name == "detect_language":
                tool_input = {"text": context["text"]}
                tool_output = execute_tool("detect_language", tool_input)
                context["detected_language"] = tool_output

            elif tool_name == "correct_text":
                tool_input = {"text": context["text"]}
                tool_output = execute_tool("correct_text", tool_input)
                context["result"] = tool_output
                context["text"] = tool_output
                context["mode"] = "correct"

            elif tool_name == "translate_text":
                tool_input = {
                    "text": context["text"],
                    "target_language": context.get("target_language") or "Danish"
                }
                tool_output = execute_tool("translate_text", tool_input)
                context["result"] = tool_output
                context["mode"] = "translate"
                context["target_language"] = tool_input["target_language"]

            elif tool_name == "evaluate_quality":
                tool_input = {
                    "original_text": context["original_text"],
                    "ai_response": context["result"],
                    "mode": context["mode"],
                    "target_language": context.get("target_language")
                }
                tool_output = execute_tool("evaluate_quality", tool_input)
                context["quality"] = tool_output

            attempt_trace["steps"].append({
                "tool": tool_name,
                "input": tool_input,
                "output": tool_output
            })

        attempt_trace["result"] = context["result"]
        attempt_trace["quality"] = context["quality"]

        full_trace["attempts"].append(attempt_trace)

        best_result = context["result"]
        best_quality = context["quality"]

        if context["quality"] and context["quality"]["score"] >= quality_threshold:
            logger.info("[AGENT LOOP] Quality threshold met. Stopping.")
            break

        previous_result = context["result"]

        if context["quality"]:
            quality_feedback = context["quality"].get("feedback")

    full_trace["final_result"] = best_result
    full_trace["final_quality"] = best_quality

    logger.info(
        f"[AGENT TRACE]\n{json.dumps(full_trace, indent=2, ensure_ascii=False)}"
    )

    return {
        "mode": mode,
        "result_text": best_result,
        "quality": best_quality,
        "trace": full_trace
    }