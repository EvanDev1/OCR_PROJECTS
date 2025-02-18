import keyboard
import time

def jump():
    keyboard.press('space')
    time.sleep(0.05)
    keyboard.release('space')

def hold_key(key, duration):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

def move_player(direction, duration):
    for key in direction:
        keyboard.press(key)

    time.sleep(duration)
    
    for key in direction:
        keyboard.release(key)
