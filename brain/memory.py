from collections import deque
from config.personality import personality_text # wait, I wrote it as config/personality.txt

class ConversationMemory:
    def __init__(self, max_length=10):
        self.memory = deque(maxlen=max_length)
        # Load personality
        with open("ai_rick_system/config/personality.txt", "r") as f:
            self.personality = f.read()
            
    def add_message(self, role, content):
        self.memory.append({"role": role, "content": content})
        
    def get_messages(self):
        messages = [{"role": "system", "content": self.personality}]
        messages.extend(list(self.memory))
        return messages
    
    def clear(self):
        self.memory.clear()

memory_manager = ConversationMemory()
