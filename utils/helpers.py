import re
import random

def clean_rick_text(text):
    """
    Replaces *burp* or burp with phonetic sounds for Rick.
    Also removes any asterisks that might trigger the TTS to say 'asterisk'.
    """
    if not text:
        return text
        
    rick_burps = [" uuuuuurp ", " buuuuuurp ", " brrrrgh ", " uuuuuugh "]
    
    # 1. First, replace any literal *burp* or burp (case-insensitive)
    cleaned = re.sub(r'\*?burp\*?', lambda x: random.choice(rick_burps), text, flags=re.IGNORECASE)
    
    # 2. Remove any remaining asterisks just in case the LLM used them for emphasis
    cleaned = cleaned.replace("*", "")
    
    # 3. Clean up double spaces
    cleaned = re.sub(r' +', ' ', cleaned)
    
    return cleaned.strip()
