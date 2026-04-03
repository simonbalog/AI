import sounddevice as sd
import numpy as np
import soundfile as sf
from config.settings import INPUT_DEVICE_ID
from utils.logger import logger

def record_audio(output_path="temp.wav", duration=5, samplerate=16000):
    """
    Records audio from the microphone for a fixed duration.
    """
    logger.info(f"Recording for {duration} seconds (Device ID: {INPUT_DEVICE_ID})...")
    try:
        # If INPUT_DEVICE_ID is -1, sounddevice uses the default
        device = INPUT_DEVICE_ID if INPUT_DEVICE_ID != -1 else None
        
        # Try to record with 1 channel first, then fallback to 2
        try:
            audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16', device=device)
        except Exception as e:
            logger.warning(f"Failed to record with 1 channel, trying 2: {e}")
            audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16', device=device)
        
        sd.wait() # wait for recording to finish
        sf.write(output_path, audio, samplerate)
        logger.info(f"Recording saved to {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Error during recording: {e}")
        return None
