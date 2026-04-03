import re
import random

def clean_rick_text(text):
    """
    NUCLEAR OPTION: Eradicates 'burp' and asterisks from existence.
    """
    if not text:
        return text
        
    # Tag for the TTS engine to play a real burp sound file
    burp_tag = " [[BURP]] "
    
    # 1. Replace 'burp' variations with the tag
    text = re.sub(r'\*+burp\*+', burp_tag, text, flags=re.IGNORECASE)
    text = re.sub(r'\bburp\b', burp_tag, text, flags=re.IGNORECASE)
    text = re.sub(r'\burgh\b', burp_tag, text, flags=re.IGNORECASE)
    text = re.sub(r'\bburrrgh\b', burp_tag, text, flags=re.IGNORECASE)
    
    # 2. Handle the specific ones that were phonetics
    text = text.replace("urrrghhh", burp_tag)
    text = text.replace("brrrrgh", burp_tag)
    text = text.replace("uuu-uugh-uuuurp", burp_tag)
    text = text.replace("ugh-bluugh-uuurp", burp_tag)
    text = text.replace("ggguuurrrp", burp_tag)
    text = text.replace("uu-uuurrp", burp_tag)
    
    # 3. Kill ALL asterisks - Piper hates them
    text = text.replace("*", "")
    
    # 4. Clean up whitespace
    text = re.sub(r' +', ' ', text)
    
    return text.strip()
