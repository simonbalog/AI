import sounddevice as sd
import numpy as np
import soundfile as sf
from utils.logger import logger

def record_audio(output_path="temp.wav", duration=5, samplerate=16000):
    """
    Records audio from the microphone for a fixed duration.
    In a more advanced version, we would use voice activity detection (VAD).
    """
    logger.info(f"Recording for {duration} seconds...")
    try:
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
        sd.wait() # wait for recording to finish
        sf.write(output_path, audio, samplerate)
        logger.info(f"Recording saved to {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Error during recording: {e}")
        return None
