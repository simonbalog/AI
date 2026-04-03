#!/bin/bash

# Rick C-137 System Startup Script
# This script ensures the environment is ready and starts the AI.

# Navigate to the script's directory
cd "$(dirname "$0")"

# Check if .env exists
if [ ! -f .env ]; then
    echo "Error: .env file not found! Copy .env.example to .env and add your keys."
    exit 1
fi

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Ensure models directory exists
mkdir -p models/whisper models/tts

echo "Starting Rick C-137 AI..."
# Run the main script
python3 main.py
