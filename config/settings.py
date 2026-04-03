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
WHISPER_PATH = os.path.join("models", "whisper", "main") # whisper.cpp executable
WHISPER_MODEL = os.path.join("models", "whisper", "ggml-base.bin")
PIPER_PATH = "piper" # assuming it's in the system path or local
PIPER_MODEL = os.path.join("models", "tts", "en_US-lessac-medium.onnx")

# Safety
ALLOWED_COMMANDS = ["ls", "pwd", "echo", "date", "uptime", "free", "vcgencmd", "git"]
