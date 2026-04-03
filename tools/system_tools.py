import subprocess
import os
from tools.safety import is_safe_command
from utils.logger import logger

def set_volume(percentage):
    """
    Sets the system volume using amixer (for RPi).
    """
    try:
        # amixer set Master 80%
        # On RPi, it's often 'Headphone' or 'HDMI' or 'Speaker'
        # We'll try common control names
        controls = ["Master", "Headphone", "HDMI", "PCM", "Speaker"]
        success = False
        
        for control in controls:
            cmd = ["amixer", "set", control, f"{percentage}%"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                success = True
                break
        
        if success:
            logger.info(f"Volume set to {percentage}%")
            return f"Volume adjusted to {percentage}%."
        else:
            return "Failed to find a valid audio control (Master/Headphone/PCM)."
            
    except Exception as e:
        logger.error(f"Error setting volume: {e}")
        return f"Volume error: {str(e)}"

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
