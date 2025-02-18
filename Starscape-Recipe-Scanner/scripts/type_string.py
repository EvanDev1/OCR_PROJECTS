import keyboard
import time

def type_string(word):
    for char in word:
        if char.isupper():
            keyboard.press_and_release('shift+' + char.lower())
        else:
            keyboard.press_and_release(char)
        time.sleep(0.01)