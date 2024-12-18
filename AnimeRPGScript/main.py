import pyautogui
import keyboard
import time
import random

clicking = False

def toggle_clicking():
    global clicking
    clicking = not clicking
    if clicking:
        print("Auto-clicker started")
    else:
        print("Auto-clicker stopped")

# Bind the 'p' key to toggle the clicking state
keyboard.add_hotkey('p', toggle_clicking)

print("Press 'p' to start/stop auto-clicker")

# Define the keys for random pressing
random_keys = ['e', 'r', 'f', 'x', '1']

last_random_key_press = time.time()
random_key_interval = 1  # seconds

while True:
    if clicking:
        # Perform mouse click
        pyautogui.click()
        time.sleep(0.0001)  # Adjust this to change how frequently it clicks

        # Check if it's time to press a random key
        current_time = time.time()
        if current_time - last_random_key_press >= random_key_interval:
            random_key = random.choice(random_keys)
            for _ in range(3):  # Triple click the random key
                keyboard.press_and_release(random_key)  # Use keyboard library for key presses
                time.sleep(0.05)  # Slight delay between key presses
            print(f"Pressed random key three times: {random_key}")
            last_random_key_press = current_time

    time.sleep(0.001)  # Prevents the loop from running too fast when not clicking
