import mouse
import keyboard

count = 1

left = 0
top = 0
right = 0
bottom = 0

type = 'not normal idk'
# type = 'normal'
 
def print_pos():
    pos = mouse.get_position()
    print(pos)
 
keyboard.add_hotkey('space', print_pos)  
keyboard.wait()
 