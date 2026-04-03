import re
import random

def clean_rick_text(text):
    """
    ULTRA HARD FILTER: Removes all traces of 'burp' and asterisks.
    Forces phonetic sounds for TTS stability.
    """
    if not text:
        return text
        
    # Phonetic sounds that Piper reads as real noises
    rick_noises = [" urrrghhh ", " brrrrgh ", " uuuuuurp ", " uuuuuugh "]
    
    # 1. Brutal regex to catch 'burp', '*burp*', 'Burp', etc.
    # We replace it with a random phonetic noise
    cleaned = re.sub(r'\*?burp\*?', lambda x: random.choice(rick_noises), text, flags=re.IGNORECASE)
    
    # 2. Kill all asterisks - they are the enemy of TTS
    cleaned = cleaned.replace("*", "")
    
    # 3. Final safety: if the LLM still wrote 'burp' somehow
    cleaned = cleaned.replace("burp", random.choice(rick_noises))
    cleaned = cleaned.replace("Burp", random.choice(rick_noises))
    
    # 4. Clean up whitespace
    cleaned = re.sub(r' +', ' ', cleaned)
    
    return cleaned.strip()
