import json
from tools.system_tools import run_command
from tools.updater import update_system
from utils.logger import logger

def handle_ai_response(response_text):
    """
    Parses the AI response. If it's JSON, it checks for actions.
    Otherwise, it just returns the text.
    """
    try:
        # Try to parse as JSON
        data = json.loads(response_text)
        
        # If it's a dict, check for action
        if isinstance(data, dict):
            action = data.get("action")
            args = data.get("args")
            spoken_response = data.get("response", "")
            
            if action == "bash" and args:
                logger.info(f"Executing action: {action} with args: {args}")
                command_result = run_command(args)
                return f"{spoken_response}\n[SYSTEM]: {command_result}"
            
            if action == "update":
                logger.info("Executing action: update")
                update_result = update_system()
                # If we get here, the update/restart failed
                return f"{spoken_response}\n[SYSTEM ERROR]: {update_result}"
            
            return spoken_response
            
    except (json.JSONDecodeError, TypeError):
        # Not JSON, just return the text
        return response_text
    
    return response_text
