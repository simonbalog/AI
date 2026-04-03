import subprocess
import os
from config.settings import PIPER_PATH, PIPER_MODEL
from utils.logger import logger

def speak(text):
    """
    Uses Piper TTS to generate speech and aplay to play it.
    """
    if not text:
        return
        
    logger.info(f"Speaking: {text}")
    output_wav = "output.wav"
    
    try:
        # Command for Piper
        # We pipe the text to stdin
        piper_cmd = [
            PIPER_PATH,
            "--model", PIPER_MODEL,
            "--output_file", output_wav
        ]
        
        subprocess.run(piper_cmd, input=text.encode('utf-8'), check=True, capture_output=True)
        
        # Play the result
        subprocess.run(["aplay", output_wav], check=True)
        
        # Cleanup
        if os.path.exists(output_wav):
            os.remove(output_wav)
            
    except Exception as e:
        logger.error(f"Error during TTS: {e}")
        # Fallback to simple print if audio fails
        print(f"AI: {text}")
