import subprocess
import os
import sys
from utils.logger import logger
from audio.tts import speak

def update_system():
    """
    Pulls the latest code from GitHub and restarts the script.
    Includes voice feedback for that Rick Prime experience.
    """
    speak("Initiating system synchronization with the central repository. *burp* Try not to touch anything while I fix your mess.")
    logger.info("Starting Rick Prime system update...")
    
    try:
        # 1. Git pull
        logger.info("Pulling latest changes from GitHub...")
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Ensure we have the right remote (using HTTPS as requested for the RPi)
        subprocess.run(["git", "-C", project_root, "remote", "set-url", "origin", "https://github.com/simonbalog/AI.git"], check=True)
        
        pull_result = subprocess.run(["git", "-C", project_root, "pull", "origin", "main"], capture_output=True, text=True, timeout=30)
        
        if pull_result.returncode != 0:
            msg = f"Git pull failed: {pull_result.stderr}"
            speak("Sync failed. Your internet probably sucks, Morty.")
            return msg
            
        logger.info(f"Git pull output: {pull_result.stdout}")
        
        if "Already up to date" in pull_result.stdout:
            speak("We're already at peak performance. *burp* Stop wasting my time.")
            return "Already up to date."

        # 2. Update requirements if they changed
        if "requirements.txt" in pull_result.stdout:
            speak("Updating dependencies. This might take a second, kid.")
            logger.info("Updating requirements...")
            req_path = os.path.join(project_root, "requirements.txt")
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)

        speak("Update complete. Re-materializing system. *burp* See ya on the other side.")
        logger.info("Update successful. Restarting system...")
        
        # 3. Restart the script
        os.execv(sys.executable, [sys.executable] + sys.argv)
        
    except Exception as e:
        logger.error(f"Update failed: {e}")
        speak("Something went wrong. The multiverse is collapsing. *burp* Just kidding, it's just a bug.")
        return f"Update failed: {str(e)}"
