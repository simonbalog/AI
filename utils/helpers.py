import re
import random

def clean_rick_text(text):
    """
    NUCLEAR OPTION: Eradicates 'burp' and asterisks from existence.
    """
    if not text:
        return text
        
    # Sounds that actually work with Piper (Bryce model)
    # Using phonetic combinations that trigger 'glottal' sounds or realistic interruptions
    rick_noises = [
        " uuu-uhhh-urp ", 
        " ughhh-blugh-huurrp ", 
        " uu-uuurrp ", 
        " buuuuuurp-uuuuggh ", 
        " ggguuurrrp ",
        " uuh-uugh-uuurp "
    ]
    
    # 1. Literal string replacements (the most reliable way)
    # We replace 'burp' variations with phonetic sounds
    text = re.sub(r'\*+burp\*+', lambda x: random.choice(rick_noises), text, flags=re.IGNORECASE)
    text = re.sub(r'\bburp\b', lambda x: random.choice(rick_noises), text, flags=re.IGNORECASE)
    
    # 2. Handle the specific ones the user said don't sound right
    # 'urrrghhh' sounds like 'uuuh', so let's make it more guttural
    text = text.replace("urrrghhh", "uuu-uugh-uuuurp")
    # 'brrrrgh' is being spelled out, so let's make it phonetic
    text = text.replace("brrrrgh", "ugh-bluugh-uuurp")
    
    # 3. Kill ALL asterisks - Piper hates them
    text = text.replace("*", "")
    
    # 4. Clean up whitespace
    text = re.sub(r' +', ' ', text)
    
    return text.strip()
