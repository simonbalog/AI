import subprocess
import os
import random
import re
from config.settings import PIPER_PATH, PIPER_MODEL, OUTPUT_DEVICE_ID
from utils.logger import logger

def speak(text):
    """
    Uses Piper TTS to generate speech and aplay to play it.
    """
    if not text:
        return
        
    logger.info(f"Speaking: {text}")
    
    # Replace *burp* or burp with phonetic sounds for Rick (case-insensitive)
    # Piper handles these better as strange phonetics
    rick_burps = [" uuuuuurp ", " buuuuuuuurp ", " brrrrrrrgh ", " uuuuuuuuugh "]
    
    # Use regex for case-insensitive replacement of *burp* or burp
    clean_text = re.sub(r'\*?burp\*?', lambda x: random.choice(rick_burps), text, flags=re.IGNORECASE)
    
    output_wav = "output.wav"
    
    try:
        # Resolve path to piper executable
        piper_exec = PIPER_PATH
        if not os.path.isabs(piper_exec):
            # If relative, make it relative to the project root
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            piper_exec = os.path.join(project_root, PIPER_PATH)

        # Command for Piper
        # We adjust parameters to make the voice sound more like Rick Sanchez
        # - length_scale: Speed of speech (lower = faster)
        # - sentence_silence: Silence between sentences
        # - noise_scale: Variability in pitch (adds that 'raspy' feel)
        # - noise_w: Variability in phoneme duration
        
        # Check if we're using a low or medium quality model to adjust parameters
        is_low_quality = "low" in PIPER_MODEL
        
        piper_cmd = [
            piper_exec,
            "--model", PIPER_MODEL,
            "--output_file", output_wav,
            "--length_scale", "0.82" if is_low_quality else "0.85",
            "--sentence_silence", "0.1",
            "--noise_scale", "0.667",
            "--noise_w", "0.8"
        ]
        
        subprocess.run(piper_cmd, input=clean_text.encode('utf-8'), check=True, capture_output=True)
        
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
