import time
import sys
from audio.recorder import record_audio
from audio.stt import transcribe
from audio.tts import speak
from brain.llm_client import ask_llm
from brain.agent import handle_ai_response
from brain.memory import memory_manager
from utils.logger import logger

def print_rick_ascii():
    rick_art = """
    #######################################
    #        RICK C-137 OS v1.0           #
    #  "Don't think about it, Morty!"     #
    #######################################
    """
    print(rick_art)

def main_loop(mode="text"):
    logger.info(f"Starting Rick C-137 System in {mode.upper()} mode...")
    
    # Ready signal
    speak(f"System online in {mode} mode, Morty. *burp* What do you want now?")
    
    try:
        while True:
            if mode == "audio":
                # Step 1: Record command
                audio_file = record_audio()
                # Step 2: Transcribe
                user_text = transcribe(audio_file)
            else:
                # Step 1 & 2: Get text input
                user_text = input("\n[YOU]: ")

            if not user_text or len(user_text.strip()) < 2:
                if mode == "audio":
                    logger.warning("No clear command heard. Listening again...")
                    time.sleep(1)
                continue
            
            if mode == "audio":
                print(f"YOU (Audio): {user_text}")
            
            # Step 3: Add to memory and ask LLM
            memory_manager.add_message("user", user_text)
            llm_response = ask_llm(memory_manager.get_messages())
            
            # Step 4: Handle response (actions + spoken text)
            processed_response = handle_ai_response(llm_response)
            
            # Step 5: Add AI response to memory
            memory_manager.add_message("assistant", llm_response)
            
            print(f"RICK: {processed_response}")
            
            # Step 6: Speak (ALWAYS speak, even in text mode)
            speak(processed_response)
            
            if mode == "audio":
                time.sleep(1)
                
    except KeyboardInterrupt:
        logger.info("Shutting down...")

def main():
    print_rick_ascii()
    print("Select Operation Mode:")
    print("1) TEXT ONLY (You type, Rick speaks) - *Recommended for microphoneless Jerry's*")
    print("2) AUDIO ONLY (Full Voice Control)")
    print("3) EXIT")
    
    choice = input("\nSelection [1-3]: ")
    
    if choice == "1":
        main_loop(mode="text")
    elif choice == "2":
        main_loop(mode="audio")
    else:
        print("Wubba Lubba Dub Dub! See ya.")
        sys.exit()

if __name__ == "__main__":
    main()
