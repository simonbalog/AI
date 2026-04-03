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
        
        # Query device info to see how many channels it supports
        device_info = sd.query_devices(device, 'input')
        max_channels = device_info.get('max_input_channels', 0)
        logger.info(f"Device info: {device_info['name']} supports up to {max_channels} input channels.")
        
        if max_channels == 0:
            raise ValueError(f"Device {device} does not support input (recording).")
            
        # Use the maximum available channels if 1 isn't supported, 
        # but most models expect mono (1) or stereo (2)
        channels = 1 if max_channels >= 1 else max_channels
        
        logger.info(f"Attempting to record with {channels} channel(s)...")
        audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16', device=device)
        
        sd.wait() # wait for recording to finish
        sf.write(output_path, audio, samplerate)
        logger.info(f"Recording saved to {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Error during recording: {e}")
        return None
