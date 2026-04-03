import json
import sys
from tools.system_tools import run_command, power_action
from tools.updater import update_system
from tools import rick_tools
from utils.logger import logger

def handle_ai_response(llm_response):
    """
    Parses the AI response. If it's JSON, it checks for actions.
    Otherwise, it just returns the text.
    """
    try:
        # Try to parse as JSON
        data = json.loads(llm_response)
        
        # If it's a dict, check for action
        if isinstance(data, dict):
            action = data.get("action")
            args = data.get("args")
            spoken_response = data.get("response", "")
            
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
            
    except (json.JSONDecodeError, TypeError):
        # Not JSON, just return the text
        return llm_response
    
    return llm_response
