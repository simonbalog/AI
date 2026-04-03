import subprocess
from config.settings import WHISPER_PATH, WHISPER_MODEL
from utils.logger import logger

def transcribe(audio_path):
    """
    Calls whisper.cpp to transcribe the audio.
    """
    if not audio_path:
        return ""
        
    logger.info(f"Transcribing {audio_path}...")
    try:
        # Command for whisper.cpp
        # -m: model path
        # -f: audio file path
        # -nt: no timestamps
        result = subprocess.run(
            [WHISPER_PATH, "-m", WHISPER_MODEL, "-f", audio_path, "-nt"],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            text = result.stdout.strip()
            logger.info(f"Transcription: {text}")
            return text
        else:
            logger.error(f"Whisper.cpp failed: {result.stderr}")
            return ""
            
    except Exception as e:
        logger.error(f"Error during transcription: {e}")
        return ""
