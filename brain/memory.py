import os
from collections import deque

class ConversationMemory:
    def __init__(self, max_length=10):
        self.memory = deque(maxlen=max_length)
        # Load personality
        personality_path = os.path.join(os.path.dirname(__file__), "..", "config", "personality.txt")
        with open(personality_path, "r") as f:
            self.personality = f.read()
            
    def add_message(self, role, content):
        self.memory.append({"role": role, "content": content})
        
    def get_messages(self):
        messages = [{"role": "system", "content": self.personality}]
        messages.extend(list(self.memory))
        # Log for debugging (only first 50 chars of each)
        # logger.debug(f"Sending messages: {[{'role': m['role'], 'content': m['content'][:50]} for m in messages]}")
        return messages
    
    def clear(self):
        self.memory.clear()

memory_manager = ConversationMemory()
