#!/bin/bash

# --- RICK PRIME OS STARTUP ---
# "Don't think about it, Morty!"

# Navigate to project directory
cd "$(dirname "$0")"

# Visual feedback
echo -e "\033[1;32m[SYSTEM]: Powering up Rick Prime OS...\033[0m"

# 1. Environment Check
if [ ! -f .env ]; then
    echo -e "\033[1;31m[ERROR]: .env file missing. Materialize it from .env.example, Jerry!\033[0m"
    exit 1
fi

# 2. Virtual Environment Management
if [ ! -d "venv" ]; then
    echo -e "\033[1;33m[SYSTEM]: Virtual environment missing. Creating it...\033[0m"
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# 3. Model Check (Ensures Whisper and Piper models are where they should be)
mkdir -p models/whisper models/tts

# 4. Git Sync Check (Ensures the remote is always correct)
git remote set-url origin git@github.com:simonbalog/AI.git 2>/dev/null

# 5. Start the engine
python3 main.py
