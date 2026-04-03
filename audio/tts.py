import subprocess
import os
from config.settings import PIPER_PATH, PIPER_MODEL, OUTPUT_DEVICE_ID
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
        # Resolve path to piper executable
        piper_exec = PIPER_PATH
        if not os.path.isabs(piper_exec):
            # If relative, make it relative to the project root
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            piper_exec = os.path.join(project_root, PIPER_PATH)

        # Command for Piper
        piper_cmd = [
            piper_exec,
            "--model", PIPER_MODEL,
            "--output_file", output_wav
        ]
        
        subprocess.run(piper_cmd, input=text.encode('utf-8'), check=True, capture_output=True)
        
        # Play the result (optionally with a specific device)
        aplay_cmd = ["aplay", output_wav]
        if OUTPUT_DEVICE_ID != -1:
            # aplay uses -D device_name, which is tricky with IDs. 
            # For now, let's just use default or let the user configure ALSA.
            pass
            
        subprocess.run(aplay_cmd, check=True)
        
        # Cleanup
        if os.path.exists(output_wav):
            os.remove(output_wav)
            
    except Exception as e:
        logger.error(f"Error during TTS: {e}")
        # Fallback to simple print if audio fails
        print(f"AI: {text}")
