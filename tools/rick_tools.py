import os
import psutil
import datetime
import random
import requests
from utils.logger import logger

def get_system_stats():
    """1. Ship Diagnostics: CPU, RAM, Temp."""
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    try:
        # RPi specific temp check
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000
    except:
        temp = "N/A"
    return f"CPU: {cpu}%, RAM: {ram}%, Core Temp: {temp}°C. Everything is marginally functional, Morty."

def get_weather(city="Prague"):
    """2. Intergalactic Weather (Scraping or simple API)."""
    try:
        # Using a simple wttr.in for no-key weather
        res = requests.get(f"https://wttr.in/{city}?format=3", timeout=5)
        return res.text.strip()
    except:
        return "Weather sensors are jammed by galactic interference."

def get_random_burp():
    """3. Burp Generator."""
    burps = ["*BURP*", "*buuuuuurp*", "*long wet burp*", "*tiny classy burp*"]
    return random.choice(burps)

def dimension_time(dimension=None):
    """4. Multi-dimensional Time."""
    now = datetime.datetime.now()
    if not dimension:
        return f"Current Earth C-137 time is {now.strftime('%H:%M:%S')}. Stop asking, it's irrelevant."
    # Fake multi-dimensional offset
    offset = random.randint(-12, 12)
    dim_time = now + datetime.timedelta(hours=offset)
    return f"In Dimension {dimension}, it's currently {dim_time.strftime('%H:%M:%S')}. Happy now?"

def ship_self_destruct(code):
    """5. Self-Destruct (Fake)."""
    if code == "1234":
        return "SELF-DESTRUCT INITIATED. 10... 9... Just kidding, Morty. *burp* You actually fell for that?"
    return "Incorrect authorization code. Security drones deployed. Run."

def list_cargo():
    """6. Cargo Manager."""
    files = os.listdir(".")
    return f"The cargo bay contains: {', '.join(files[:5])}... and a lot of junk."

def search_wiki(query):
    """7. Galactic Knowledge (Wikipedia)."""
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
        data = requests.get(url, timeout=5).json()
        return data.get("extract", "I couldn't find that in the database. Maybe it doesn't exist in this reality.")
    except:
        return "The central brain is busy thinking about something actually important."

def flip_coin():
    """8. Probability Stabilizer (Coin Flip)."""
    result = random.choice(["Heads", "Tails"])
    return f"The multiverse has collapsed into a state of: {result}. *burp*"

def calculate(expression):
    """9. Scientific Calculator."""
    try:
        # Very basic safe eval (Morty-proof)
        allowed = set("0123456789+-*/(). ")
        if all(c in allowed for c in expression):
            return f"The answer is {eval(expression)}. Even a Meeseeks could have done that."
        return "Invalid characters. Are you trying to hack me, Morty?"
    except:
        return "Math error. You probably divided by zero and killed a galaxy."

def get_ship_status():
    """10. Full Ship Status."""
    return "Shields: 12%. Fuel: Low. Sarcasm: 100%. We're doing great."

def run_python_logic(code):
    """11. Rick's Python Executor (Scientific Logic)."""
    try:
        # Warning: This is a simplified executor for fun
        # In a real Rick ship, this would be a secure sandbox
        exec_globals = {}
        exec(code, exec_globals)
        return f"Logic executed. Result: {exec_globals.get('result', 'No result variable found.')}"
    except Exception as e:
        return f"Logic error: {str(e)}. Stick to the basics, Morty."

def rick_wisdom():
    """12. Random Rick Nihilism."""
    quotes = [
        "To live is to risk it all; otherwise you're just an inert chunk of randomly assembled molecules floating wherever the universe blows you.",
        "Nobody exists on purpose. Nobody belongs anywhere. Everybody's gonna die. Come watch TV?",
        "Wubba Lubba Dub Dub! (I am in great pain, please help me.)",
        "The universe is basically an animal. It grazes on the ordinary. It creates infinite idiots just to eat them.",
        "Scientific tradition is to take the shortest path to the answer."
    ]
    return random.choice(quotes)

def roast_jerry():
    """14. Roast Jerry (Random insult)."""
    insults = [
        "Jerry, you're a human Participation Trophy.",
        "Your resume is just a list of places where people were polite to you before firing you.",
        "You're the only person I know who can fail at doing nothing.",
        "If stupidity was a currency, you'd be a billionaire, Jerry.",
        "I'd explain it to you, Jerry, but I don't have enough crayons."
    ]
    return random.choice(insults)

def multiverse_fact():
    """15. Weird Multiverse Fact."""
    facts = [
        "In Dimension C-500, humans evolved from telepathic giant spiders. The internet is literally a web.",
        "There's a reality where everything is exactly the same, but the word 'pizza' means 'nuclear war'.",
        "In one universe, the RPi 5 was invented in 1952 by a sentient toaster.",
        "Time is linear in only 4% of the multiverse. In the rest, it's a fractal soup.",
        "You're currently being watched by 14 different versions of yourself through various portal-mirrors."
    ]
    return random.choice(facts)

def jump_dimension():
    """13. Terminal Color Jump."""
    colors = ["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"]
    color = random.choice(colors)
    return f"{color}DIMENSION JUMP SUCCESSFUL. Terminal stabilized in new reality.\033[0m"
