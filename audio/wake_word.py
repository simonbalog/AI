import pvporcupine
import pyaudio
import struct
from config.settings import WAKE_WORD_MODEL, PICOVOICE_API_KEY
from utils.logger import logger

class WakeWordDetector:
    def __init__(self, keyword_path=WAKE_WORD_MODEL):
        self.porcupine = None
        self.pa = None
        self.stream = None
        self.keyword_path = keyword_path
        
    def setup(self):
        try:
            self.porcupine = pvporcupine.create(
                access_key=PICOVOICE_API_KEY,
                keyword_paths=[self.keyword_path]
            )
            
            self.pa = pyaudio.PyAudio()
            self.stream = self.pa.open(
                rate=self.porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=self.porcupine.frame_length
            )
            logger.info("Wake word detector initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize wake word detector: {e}")
            raise
            
    def listen(self):
        if not self.porcupine:
            self.setup()
            
        logger.info("Listening for 'Rick'...")
        try:
            while True:
                pcm = self.stream.read(self.porcupine.frame_length)
                pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
                
                keyword_index = self.porcupine.process(pcm)
                
                if keyword_index >= 0:
                    logger.info("Wake word DETECTED!")
                    return True
        except Exception as e:
            logger.error(f"Error in wake word loop: {e}")
            return False
            
    def cleanup(self):
        if self.stream:
            self.stream.close()
        if self.pa:
            self.pa.terminate()
        if self.porcupine:
            self.porcupine.delete()
