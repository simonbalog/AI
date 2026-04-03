from config.settings import ALLOWED_COMMANDS

def is_safe_command(cmd):
    """
    Very basic safety check. In a real Rick ship, this would be more complex.
    We check if the command (first word) is in the whitelist.
    """
    if not cmd:
        return False
    
    # Simple split to get the base command
    parts = cmd.split()
    if not parts:
        return False
        
    base_cmd = parts[0]
    return base_cmd in ALLOWED_COMMANDS
