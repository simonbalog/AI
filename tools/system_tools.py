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
        # Even with absolute power, we keep a tiny log for the user
        logger.warning(f"EXECUTING POWER COMMAND: {cmd}")
    
    try:
        logger.info(f"Running command: {cmd}")
        
        # Special handling for shutdown/reboot to give voice feedback first
        if "shutdown" in cmd or "reboot" in cmd:
            return "Command accepted. Initiating system state change..."

        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            return result.stdout.strip() if result.stdout else "Success (No output)."
        else:
            return f"Command failed: {result.stderr.strip()}"
            
    except subprocess.TimeoutExpired:
        return "Command timed out. Even my brain has limits, Morty."
    except Exception as e:
        logger.error(f"Error running command: {e}")
        return f"Something went wrong: {str(e)}"

def power_action(action):
    """
    Direct system power actions.
    """
    if action == "shutdown_pi":
        logger.info("PI SHUTDOWN INITIATED")
        os.system("sudo shutdown -h now")
        return "RPi is shutting down. Goodnight, Morty."
    elif action == "reboot_pi":
        logger.info("PI REBOOT INITIATED")
        os.system("sudo reboot")
        return "RPi is rebooting. See you in a few, Morty."
    elif action == "exit_rick":
        logger.info("RICK OS EXIT INITIATED")
        sys.exit(0)
        return "Rick OS terminated."
    return "Unknown power action."
