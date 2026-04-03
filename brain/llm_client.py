import requests
import json
from config.settings import API_KEY, API_URL, MODEL_NAME
from utils.logger import logger

def ask_llm(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        logger.error(f"Error calling LLM: {e}")
        return "I'm having some technical difficulties with the multiverse connection, Morty. *burp* Try again."
