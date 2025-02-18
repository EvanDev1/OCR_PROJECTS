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
    if type == 'normal':
        print((pos[0], pos[1]))
    else:  
        global count
        global left  
        global top
        global right
        global bottom
        
        if count == 1:
            print('scanned')        
            left = pos[0]
            top = pos[1]
            count = count + 1
        else: 
            right = pos[0]
            bottom = pos[1]
            print(left, top, right, bottom)
            count = 1

keyboard.add_hotkey('space', print_pos)  
keyboard.wait()
       