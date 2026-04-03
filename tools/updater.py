import subprocess
import os
import sys
from utils.logger import logger

def update_system():
    """
    Pulls the latest code from GitHub and restarts the script.
    """
    logger.info("Starting system update...")
    
    try:
        # 1. Git pull
        logger.info("Pulling latest changes from GitHub...")
        # Ensure we are in the project root
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pull_result = subprocess.run(["git", "-C", project_root, "pull"], capture_output=True, text=True, timeout=30)
        
        if pull_result.returncode != 0:
            return f"Git pull failed: {pull_result.stderr}"
            
        logger.info(f"Git pull output: {pull_result.stdout}")
        
        # 2. Update requirements if they changed
        if "requirements.txt" in pull_result.stdout:
            logger.info("Updating requirements...")
            req_path = os.path.join(project_root, "requirements.txt")
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)

        logger.info("Update successful. Restarting system...")
        
        # 3. Restart the script
        # We use os.execv to replace the current process with a new one
        os.execv(sys.executable, [sys.executable] + sys.argv)
        
    except Exception as e:
        logger.error(f"Update failed: {e}")
        return f"Update failed: {str(e)}"
