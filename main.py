import time
import sys
from audio.recorder import record_audio
from audio.stt import transcribe
from audio.tts import speak
from brain.llm_client import ask_llm
from brain.agent import handle_ai_response
from brain.memory import memory_manager
from utils.logger import logger
from utils.helpers import clean_rick_text

def print_rick_ascii():
    rick_art = """
    \033[1;32m
    ██████╗ ██╗ ██████╗██╗  ██╗    ██████╗ ██████╗ ██╗███╗   ███╗███████╗
    ██╔══██╗██║██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██║████╗ ████║██╔════╝
    ██████╔╝██║██║     █████╔╝     ██████╔╝██████╔╝██║██╔████╔██║█████╗  
    ██╔══██╗██║██║     ██╔═██╗     ██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝  
    ██║  ██║██║╚██████╗██║  ██╗    ██║     ██║  ██║██║██║ ╚═╝ ██║███████╗
    ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝
    \033[0m
    \033[1;34m--- Rick C-137 OS: Prime Edition v2.0 ---\033[0m
    \033[1;33m"The smartest man in every conceivable universe."\033[0m
    """
    print(rick_art)

def boot_sequence():
    """Simulates a Rick-style system boot."""
    steps = [
        "Initializing portal fluid injectors...",
        "Calibrating microverse battery output...",
        "Bypassing Galactic Federation firewalls...",
        "Loading sarcasm modules...",
        "Injecting burp sounds into audio buffer...",
        "Rick Prime OS Online."
    ]
    for step in steps:
        print(f"\033[1;30m[SYSTEM]: {step}\033[0m")
        time.sleep(0.4)
    print("\n")

def main_loop(mode="text"):
    logger.info(f"Starting Rick Prime OS in {mode.upper()} mode...")
    
    # Ready signal
    speak(f"Rick Prime OS online in {mode} mode, Morty. *burp* Try not to break anything.")
    
    try:
        while True:
            if mode == "audio":
                # Step 1: Record command
                audio_file = record_audio()
                # Step 2: Transcribe
                user_text = transcribe(audio_file)
            else:
                # Step 1 & 2: Get text input with Rick-style prompt
                user_text = input("\033[1;32m[MORTY@RICK-PC]:~\033[0m ")

            if not user_text or len(user_text.strip()) < 2:
                if mode == "audio":
                    logger.warning("No clear command heard. Listening again...")
                    time.sleep(0.5)
                continue
            
            if mode == "audio":
                print(f"\033[1;32m[YOU (Audio)]:\033[0m {user_text}")
            
            # Step 3: Add to memory and ask LLM
            memory_manager.add_message("user", user_text)
            llm_response = ask_llm(memory_manager.get_messages())
            
            # Step 4: Handle response (actions + spoken text)
            processed_response = handle_ai_response(llm_response)
            
            # Step 5: Add AI response to memory
            memory_manager.add_message("assistant", llm_response)
            
            # Clean text for terminal display and speech
            final_display = clean_rick_text(processed_response)
            
            print(f"\033[1;34m[RICK]:\033[0m {final_display}")
            
            # Step 6: Speak (ALWAYS speak, even in text mode)
            speak(final_display)
            
            if mode == "audio":
                time.sleep(0.5)
                
    except KeyboardInterrupt:
        print("\n")
        logger.info("Shutting down... Go away, Morty.")


def main():
    print_rick_ascii()
    boot_sequence()
    
    print("\033[1;36mSelect Operation Mode:\033[0m")
    print("1) \033[1;32mTEXT MODE\033[0m (Keyboard input, Voice output) - *Jerry Proof*")
    print("2) \033[1;34mAUDIO MODE\033[0m (Voice input, Voice output) - *Rick Style*")
    print("3) \033[1;31mABORT MISSION\033[0m")
    
    choice = input("\n\033[1;33mSelection [1-3]:\033[0m ")
    
    if choice == "1":
        main_loop(mode="text")
    elif choice == "2":
        main_loop(mode="audio")
    else:
        print("\033[1;31mWubba Lubba Dub Dub! Portal jumping away...\033[0m")
        sys.exit()

if __name__ == "__main__":
    main()
