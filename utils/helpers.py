import re
import random

def clean_rick_text(text):
    """
    Replaces *burp* or burp with phonetic sounds for Rick.
    """
    if not text:
        return text
        
    rick_burps = [" *uuuuuurp* ", " *buuuuuurp* ", " *brrrrgh* ", " *uuuuuugh* "]
    
    # Replace *burp* or burp (case-insensitive)
    cleaned = re.sub(r'\*?burp\*?', lambda x: random.choice(rick_burps), text, flags=re.IGNORECASE)
    return cleaned
