import subprocess
import os
import random
import re
from config.settings import PIPER_PATH, PIPER_MODEL, OUTPUT_DEVICE_ID
from utils.logger import logger
from utils.helpers import clean_rick_text

def play_audio_file(file_path, boost=False):
    """
    Plays an audio file using available system players (mpg123, ffplay, or aplay).
    If boost=True, tries to play it louder (for burps).
    """
    if not os.path.exists(file_path):
        logger.error(f"Audio file not found: {file_path}")
        return

    # Try different players commonly available on Linux/RPi
    # mpg123: -f 32768 is default, we can double it or use -g for gain
    # ffplay: -volume 100 is default, we can go up to 200 (though clipping may occur)
    players = [
        ["mpg123", "-q", "-g", "100" if boost else "60"], # -g 100 is max gain, 60 is normal
        ["ffplay", "-nodisp", "-autoexit", "-volume", "100" if boost else "70"],
        ["cvlc", "--play-and-exit", "--gain", "2.0" if boost else "1.0"]
    ]
    
    # If it's a wav, we can use aplay (no easy volume boost in aplay without amixer)
    if file_path.endswith(".wav"):
        players.insert(0, ["aplay", "-q"])

    for player_cmd in players:
        try:
            full_cmd = player_cmd + [file_path]
            subprocess.run(full_cmd, check=True, capture_output=True)
            return # Success!
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue
            
    logger.error(f"Failed to play {file_path}. Please install mpg123 or ffplay.")

def speak(text):
    """
    Uses Piper TTS to generate speech and aplay to play it.
    Splits text by [[BURP]] to play real audio files instead of synthetic sounds.
    """
    if not text:
        return
        
    # Final cleanup before speech
    clean_text = clean_rick_text(text)
    logger.info(f"Speaking (sanitized): {clean_text}")
    
    # Split text by [[BURP]] tag
    parts = re.split(r'(\[\[BURP\]\])', clean_text)
    
    audio_dir = os.path.dirname(os.path.abspath(__file__))
    output_wav = "output.wav"
    
    try:
        # Resolve path to piper executable
        piper_exec = PIPER_PATH
        if not os.path.isabs(piper_exec):
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            piper_exec = os.path.join(project_root, PIPER_PATH)

        for part in parts:
            part = part.strip()
            if not part:
                continue
                
            if part == "[[BURP]]":
                # Play a random burp sound with BOOST
                burp_file = os.path.join(audio_dir, f"burp{random.randint(1, 3)}.mp3")
                logger.info(f"Playing real burp (BOOSTED): {burp_file}")
                play_audio_file(burp_file, boost=True)
            else:
                # Use Piper for text parts
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
                
                subprocess.run(piper_cmd, input=part.encode('utf-8'), check=True, capture_output=True)
                
                # Play the synthesized text (normal volume)
                subprocess.run(["aplay", "-q", output_wav], check=True)
                
                # Cleanup
                if os.path.exists(output_wav):
                    os.remove(output_wav)
            
    except Exception as e:
        logger.error(f"Error during TTS: {e}")
        # Fallback to simple print if audio fails
        print(f"AI: {text}")
