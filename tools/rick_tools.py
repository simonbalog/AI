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
