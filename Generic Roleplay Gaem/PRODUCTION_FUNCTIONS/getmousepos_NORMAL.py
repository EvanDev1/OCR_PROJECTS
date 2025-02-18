import mouse
import keyboard
import ahk as AHK
ahk = AHK.AHK()
# positions = []

def print_pos():
    # global positions
    # print('added')
    pos = mouse.get_position()
    # print(pos)
    print(ahk.get_mouse_position())
    # positions.append(pos)
    # if len(positions) == 3:
    #     print(positions)
    #     positions = []

keyboard.add_hotkey('alt', print_pos)  
keyboard.wait()  

