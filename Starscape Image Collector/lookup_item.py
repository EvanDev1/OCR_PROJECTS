import keyboard
import mouse

import ahk
import time

AHK = ahk.AHK()


searchbar_pos = (751 * 2, 726 * 2)

# 4k searchbar pos
# searchbar_pos = (659 * 2, 753 * 2)

def type_string(word):
    for char in word:
        if char.isupper():
            keyboard.press_and_release('shift+' + char.lower())
        else:
            keyboard.press_and_release(char)
        time.sleep(0.02)

def move(pos):
    AHK.mouse_move(pos[0], pos[1])

def lookup_item(item_name):
    move(searchbar_pos)
    time.sleep(0.05)
    mouse.click()
    time.sleep(0.05)
    type_string(item_name)
    time.sleep(0.5)
