import re
import random

def clean_rick_text(text):
    """
    NUCLEAR OPTION: Eradicates 'burp' and asterisks from existence.
    """
    if not text:
        return text
        
    # Sounds that actually work with Piper
    rick_noises = [" urrrghhh ", " brrrrgh ", " uuuuuurp ", " uuuuuugh "]
    
    # 1. Literal string replacements (the most reliable way)
    text = text.replace("*burp*", random.choice(rick_noises))
    text = text.replace("*Burp*", random.choice(rick_noises))
    text = text.replace("burp", random.choice(rick_noises))
    text = text.replace("Burp", random.choice(rick_noises))
    
    # 2. Regex for cases like *burp or burp* or multiple asterisks
    text = re.sub(r'\*+burp\*+', lambda x: random.choice(rick_noises), text, flags=re.IGNORECASE)
    text = re.sub(r'burp', lambda x: random.choice(rick_noises), text, flags=re.IGNORECASE)
    
    # 3. Kill ALL asterisks - Piper hates them
    text = text.replace("*", "")
    
    # 4. Clean up whitespace
    text = re.sub(r' +', ' ', text)
    
    return text.strip()
