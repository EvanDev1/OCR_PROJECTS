import mouse
import keyboard

import pyperclip



count = 1

left = 0
top = 0
right = 0
bottom = 0

type = 'not normal idk'
# type = 'normal'

positions = []




print('----------|| RED POSITIONS ||----------')

def print_pos():
    global positions
    pos = mouse.get_position()
    positions.append(pos)
    print(len(positions))
    if len(positions) == 10:
        print('----------|| WHITE POSITIONS ||----------')
    if len(positions) == 20:
        print('----------|| SCAN COMPLETE ||----------')
        print(f"{positions},")
        pyperclip.copy(f"{positions},")
        print('---------------------------------------')
        print('----------|| RED POSITIONS ||----------')
        positions = []

keyboard.add_hotkey('alt', print_pos)  
keyboard.wait()  


