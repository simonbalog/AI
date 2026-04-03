import json
import sys
from tools.system_tools import run_command, power_action
from tools.updater import update_system
from tools import rick_tools
from utils.logger import logger

def handle_ai_response(llm_response):
    """
    Parses the AI response. If it's JSON (or contains JSON), it checks for actions.
    Otherwise, it just returns the text.
    """
    if not llm_response:
        return ""

    try:
        # 1. First, try to parse the entire thing as JSON (standard way)
        data = json.loads(llm_response)
    except (json.JSONDecodeError, TypeError):
        # 2. If it's not pure JSON, it might be Rick talking AND THEN a JSON block.
        # Use regex to find the first '{' to the last '}'
        import re
        json_match = re.search(r'\{.*\}', llm_response, re.DOTALL)
        if json_match:
            try:
                json_str = json_match.group(0)
                data = json.loads(json_str)
                # If we successfully got JSON, we also want to keep the text BEFORE the JSON
                # so Rick's verbal sarcasm isn't lost.
                pre_json_text = llm_response[:json_match.start()].strip()
            except:
                return llm_response # Failed to parse the matched part
        else:
            return llm_response # No JSON found at all

    # If we got here, we have a valid 'data' dict
    try:
        if isinstance(data, dict):
            action = data.get("action")
            args = data.get("args")
            # If we had pre-JSON text, combine it with the spoken response
            spoken_response = data.get("response", "")
            if 'pre_json_text' in locals() and pre_json_text:
                spoken_response = f"{pre_json_text} {spoken_response}".strip()
            
            if action == "bash" and args:
                logger.info(f"Executing action: {action} with args: {args}")
                command_result = run_command(args)
                
                # Check if it was a power command to trigger the actual shutdown/reboot
                if "shutdown" in args:
                    power_action("shutdown_pi")
                elif "reboot" in args:
                    power_action("reboot_pi")
                    
                return f"{spoken_response}\n[SYSTEM]: {command_result}"
            
            if action == "power":
                logger.info(f"Power action: {args}")
                res = power_action(args)
                return f"{spoken_response}\n[POWER]: {res}"

            if action == "update":
                logger.info("Executing action: update")
                update_result = update_system()
                return f"{spoken_response}\n[SYSTEM ERROR]: {update_result}"

            # --- NEW RICK TOOLS ---
            if action == "stats":
                return f"{spoken_response}\n[DIAGNOSTICS]: {rick_tools.get_system_stats()}"
            
            if action == "weather":
                return f"{spoken_response}\n[WEATHER]: {rick_tools.get_weather(args or 'Prague')}"
            
            if action == "time":
                return f"{spoken_response}\n[TIME]: {rick_tools.dimension_time(args)}"
            
            if action == "wiki":
                return f"{spoken_response}\n[GALACTIC DATA]: {rick_tools.search_wiki(args)}"
            
            if action == "calculate":
                return f"{spoken_response}\n[MATH]: {rick_tools.calculate(args)}"
            
            if action == "burp":
                return f"{spoken_response} {rick_tools.get_random_burp()}"
            
            if action == "destruct":
                return f"{spoken_response}\n[SECURITY]: {rick_tools.ship_self_destruct(args)}"
            
            if action == "cargo":
                return f"{spoken_response}\n[CARGO]: {rick_tools.list_cargo()}"
            
            if action == "coin":
                return f"{spoken_response}\n[QUANTUM]: {rick_tools.flip_coin()}"
            
            if action == "status":
                return f"{spoken_response}\n[SHIP STATUS]: {rick_tools.get_ship_status()}"
            
            if action == "python":
                return f"{spoken_response}\n[PYTHON LOGIC]: {rick_tools.run_python_logic(args)}"
            
            if action == "wisdom":
                return f"{spoken_response}\n[RICK'S WISDOM]: {rick_tools.rick_wisdom()}"
            
            if action == "roast":
                return f"{spoken_response}\n[INSULT]: {rick_tools.roast_jerry()}"
            
            if action == "fact":
                return f"{spoken_response}\n[MULTIVERSE FACT]: {rick_tools.multiverse_fact()}"
            
            if action == "jump":
                return f"{spoken_response}\n[QUANTUM]: {rick_tools.jump_dimension()}"
            
            return spoken_response
            
    except Exception as e:
        logger.error(f"Error processing agent action: {e}")
        return llm_response
    
    return llm_response
