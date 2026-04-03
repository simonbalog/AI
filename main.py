import time
from audio.wake_word import WakeWordDetector
from audio.recorder import record_audio
from audio.stt import transcribe
from audio.tts import speak
from brain.llm_client import ask_llm
from brain.agent import handle_ai_response
from brain.memory import memory_manager
from utils.logger import logger

def main():
    logger.info("Initializing Rick C-137 System (Direct Mode)...")
    
    # Ready signal
    speak("System online, Morty. *burp* What do you want now?")
    
    try:
        while True:
            # Step 1: Record command (Starts recording immediately)
            audio_file = record_audio()
            
            # Step 2: Transcribe
            user_text = transcribe(audio_file)
            
            if not user_text or len(user_text.strip()) < 2:
                logger.warning("No clear command heard. Listening again...")
                time.sleep(1) # Small pause to avoid tight loops
                continue
            
            print(f"YOU: {user_text}")
            
            # Step 3: Add to memory and ask LLM
            memory_manager.add_message("user", user_text)
            llm_response = ask_llm(memory_manager.get_messages())
            
            # Step 4: Handle response (actions + spoken text)
            processed_response = handle_ai_response(llm_response)
            
            # Step 5: Add AI response to memory
            memory_manager.add_message("assistant", llm_response)
            
            print(f"RICK: {processed_response}")
            
            # Step 6: Speak
            speak(processed_response)
            
            # Step 7: Wait a moment before next listen to avoid hearing itself
            time.sleep(1)
                
    except KeyboardInterrupt:
        logger.info("Shutting down...")


if __name__ == "__main__":
    main()
