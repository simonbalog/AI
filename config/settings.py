import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_KEY = os.getenv("LLM_API_KEY", "your_api_key_here")
API_URL = os.getenv("LLM_API_URL", "https://api.groq.com/openai/v1/chat/completions") # Default to Groq for speed
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.1-70b-versatile")

# Audio Configuration
WAKE_WORD_MODEL = os.path.join("models", "rick.ppn")
PICOVOICE_API_KEY = os.getenv("PICOVOICE_API_KEY", "your_picovoice_key")

# Paths
WHISPER_PATH = os.getenv("WHISPER_PATH", os.path.join("models", "whisper", "main"))
WHISPER_MODEL = os.getenv("WHISPER_MODEL", os.path.join("models", "whisper", "ggml-base.bin"))
PIPER_PATH = os.getenv("PIPER_PATH", os.path.join("models", "tts", "piper", "piper"))
PIPER_MODEL = os.getenv("PIPER_MODEL", os.path.join("models", "tts", "en_US-lessac-medium.onnx"))

# Audio Device IDs (Update if default -1 doesn't work)
INPUT_DEVICE_ID = int(os.getenv("INPUT_DEVICE_ID", -1))
OUTPUT_DEVICE_ID = int(os.getenv("OUTPUT_DEVICE_ID", -1))

# Safety
ALLOWED_COMMANDS = ["ls", "pwd", "echo", "date", "uptime", "free", "vcgencmd", "git"]
