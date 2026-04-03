import subprocess
from tools.safety import is_safe_command
from utils.logger import logger

def run_command(cmd):
    """
    Executes a bash command if it passes the safety check.
    """
    if not is_safe_command(cmd):
        logger.warning(f"BLOCKED UNSAFE COMMAND: {cmd}")
        return "Nice try, Morty. *burp* That command is locked for security reasons."
    
    try:
        logger.info(f"Running command: {cmd}")
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Command failed: {result.stderr.strip()}"
            
    except subprocess.TimeoutExpired:
        return "Command timed out. Even my brain has limits, Morty."
    except Exception as e:
        logger.error(f"Error running command: {e}")
        return f"Something went wrong: {str(e)}"
