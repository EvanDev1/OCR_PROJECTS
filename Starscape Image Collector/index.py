import time
import mouse
import keyboard

from item_list import item_list
from take_screenshot import take_screenshot
from lookup_item import lookup_item

complex_items = []
normal_items = []

for item in item_list:
    if ')' in item or '(' in item or '|' in item or '_' in item or '-' in item:
        if 'Ethereal' in item:
            continue
        complex_items.append(item)
    else:
        normal_items.append(item)

time.sleep(3)

import re

def remove_text_after_special_characters(input_string):
    # Define the pattern to match special characters and the text after them
    pattern = re.compile(r'[\-\(\[]')
    # Search for the pattern in the string
    match = pattern.search(input_string)
    if match:
        # Return the substring before the special character
        return input_string[:match.start()].strip()
    else:
        # If no special character is found, return the original string
        return input_string

def delete_text():
    mouse.click()
    time.sleep(0.05)
    mouse.click()
    time.sleep(0.05)
    mouse.click()
    time.sleep(0.05)

count = 0

# Get prospector image somehow..?

normal_items = [
    'Ancient beacon',
    'Ancient drone core',
    'Crystal shard',
    'Yuma',
    'Fargo',
]

item_rows = {}
current_item = ''
go = False

def add_item_row1():
    item_rows[current_item] = 1
    global go
    go = True
def add_item_row2():
    item_rows[current_item] = 2
    global go
    go = True
def add_item_row3():
    item_rows[current_item] = 3
    global go
    go = True
def add_item_row4():
    item_rows[current_item] = 4
    global go
    go = True
def add_item_row5():
    item_rows[current_item] = 5
    global go
    go = True
def add_item_row6():
    item_rows[current_item] = 6
    global go
    go = True
def add_item_row7():
    item_rows[current_item] = 7
    global go
    go = True
def add_item_row8():
    item_rows[current_item] = 8
    global go
    go = True
def add_item_row9():
    item_rows[current_item] = 9
    global go
    go = True
def add_item_row10():
    item_rows[current_item] = 10
    global go
    go = True
def add_item_row11():
    item_rows[current_item] = 11
    global go
    go = True
def add_item_row12():
    item_rows[current_item] = 12
    global go
    go = True
def add_item_row13():
    item_rows[current_item] = 'difficult :('
    global go
    go = True

keyboard.add_hotkey('1', add_item_row1)
keyboard.add_hotkey('2', add_item_row2)
keyboard.add_hotkey('3', add_item_row3)
keyboard.add_hotkey('4', add_item_row4)
keyboard.add_hotkey('5', add_item_row5)
keyboard.add_hotkey('6', add_item_row6)
keyboard.add_hotkey('7', add_item_row7)
keyboard.add_hotkey('8', add_item_row8)
keyboard.add_hotkey('9', add_item_row9)
keyboard.add_hotkey('0', add_item_row10)
keyboard.add_hotkey('a', add_item_row11)
keyboard.add_hotkey('s', add_item_row12)
keyboard.add_hotkey('w', add_item_row13)

complex_items = {'Cannon-M III': 6, 'Hybrid Blaster-M': 3, 'Banner (Foralkan)': 2, 'Uniform (CoreSec)': 1, 'Railgun-M II': 11, 'Dread Railgun-M': 3, 'Coilgun-M III': 8, 'Hybrid Blaster-M blueprint': 4, 'Dread Coilgun-M': 3, 'Beam-M III': 6, 'Dread Railgun-M blueprint': 4, 'Blaster-M III': 6, 'Hybrid Cannon-M blueprint': 4, 'Hybrid Beam-M': 3, 'Beam-M II': 5, 'Pants (CoreSec)': 5, 'Lightburner-M III': 5, 'Ancient Overdrive-M': 2, 'Pants (Syndicate)': 'difficult :(', 'Banner (Trade Union)': 7, 'Ancient Overdrive-L': 1, 'Ancient Railgun-M': 2, 'Ancient Afterburner-S': 1, 'Overdrive-M III': 10, 'Blaster-M I': 4, 'Gal-31': 1, 'Blaster-M II': 5, 'Ancient Coilgun-M': 2, 'Ancient Lightburner-L': 1, 'Ancient Lightburner-S': 3, 'Holoprojector (Foralkan)': 2, 'Uniform (Lycentian Admiral)': 8, 'LG0-T': 1, 'Hybrid Ion-M': 4, 'Hybrid Cannon-M': 3, 'Hybrid Ion-M blueprint': 5, 'Firework (snowflake)': 9, 'Hybrid Overdrive-M': 2, 'T-shirt': 'difficult :(', 'Hybrid Afterburner-S': 1, 'Hybrid Beam-M blueprint': 4, 'Dread Coilgun-M blueprint': 4, 'Ancient Lightburner-M': 2, 'Uniform (Syndicate)': 12, 'RR-5000': 'difficult :(', 'Axnit (pristine)': 2, 'Lightburner-S III': 6, 'Lightburner-L III': 4, 'Cannon-M II': 5, 'Damaged Spice (Silver)': 12, 'Gal-32': 2, 'Holoprojector (Lycentian)': 4, 'Hybrid Overdrive-L': 1, 'LGS-T': 'difficult :(', 'Reknite (inferior)': 2, 'Uniform (Kavani)': 7, 'Wall (long)': 2, 'Afterburner-S III': 3, 'FG-88': 1, 'Holoprojector (CoreSec)': 1, 'Cannon-M I': 4, 'Overdrive-M II': 9, 'Ion-M I': 'difficult :(', 'Coilgun-M II': 7, 'Afterburner-S I': 1, 'Railgun-M III': 12, 'Overdrive-L III': 7, 'Damaged Spice (Blue)': 3, 'H3-X': 1, 'Overdrive-L I': 5, 'Pants (Lycentian)': 'difficult :(', 'Uniform (Lycentian)': 10, 'Ion-M II': 'difficult :(', 'Overdrive-L II': 6, 'Pants (Foralkan)': 8, 'Uniform (Foralkan)': 4, 'Korrelite (inferior)': 2, 'Damaged Spice (Ruby)': 10, 'Korrelite (pristine)': 3, 'Banner (CoreSec)': 1, 'LG9-T': 1, 'Damaged Spice (Yellow)': 'difficult :(', 'Reknite (superior)': 4, 'Pants (Trade Union)': 'difficult :(', 'Uniform (Trade Union)': 'difficult :(', 'Gellium (superior)': 4, 'Railgun-M I': 10, 'Damaged Spice (Purple)': 8, 'Gellium (pristine)': 3, 'Coilgun-M I': 6, 'Pants (Lycentian Admiral)': 12, 'Korrelite (superior)': 4, 'Uniform (Kavani Marshal)': 6, 'Counter (bar)': 3, 'Pants (Kavani)': 11, 'Holoprojector (Trade Union)': 7, 'Damaged Spice (Amethyst)': 2, 'Afterburner-S II': 2, 'Damaged Spice (Amber)': 1, 'Pants (Mining Guild)': 'difficult :(', 'Uniform (Mining Guild)': 11, 'Beam-M I': 4, 'Damaged Spice (Orange)': 7, 'Gal-33': 3, 'Gellium (inferior)': 2, 'Pants (Kavani Command)': 9, 'Uniform (Kavani Command)': 5, 'Damaged Spice (Red)': 9, 'Damaged Spice (Jasper)': 6, 'Damaged Spice (Sapphire)': 11, 'Couch (center)': 1, 'Couch (left)': 3, 'Couch (right)': 4, 'Banner (Lycentian)': 4, 'Reknite (pristine)': 3, 'Ion-M III': 'difficult :(', 'Uniform (Foralkan Command)': 3, 'Pants (Foralkan Command)': 7, 'Pants (Lycentian Command)': 'difficult :(', 'Pants (Foralkan Admiral)': 6, 'Uniform (Foralkan Admiral)': 2, 'Holoprojector (Mining Guild)': 5}

# check size of following items after:
# 6
# 

complex_positions = [
    (),
    (332 * 2 + 1, 365 * 2 - 1),
    (369 * 2 + 1, 402 * 2 - 1),
    (405 * 2 + 3, 439 * 2 - 1),
    (444 * 2 - 1, 476 * 2 - 1),
    (480 * 2 + 1, 513 * 2 - 1),
    (516 * 2 + 3, 550 * 2 - 1),
    (553 * 2 + 4, 588 * 2 - 2),
    (591 * 2 + 2, 625 * 2 - 2),
    (627 * 2 + 4, 662 * 2 - 2),
    (664 * 2 + 4, 698 * 2),
    (701 * 2 + 4, 736 * 2 - 2),
    (739 * 2 + 2, 773 * 2 - 2),
]

y1 = None
y2 = None

def add_cord():
    global y1
    global y2

    pos = mouse.get_position()

    if y1 is None:
        y1 = pos[1]
        print(y1)
    elif y2 is None:
        y2 = pos[1]
        print(y2)

keyboard.add_hotkey('alt', add_cord)

# LGS-T doesn't exist idk

for item, key in complex_items.items():
    if key == 'difficult :(':
        print(item)
        lookup_item(remove_text_after_special_characters(item))
        
        while True:
            if y1 is not None and y2 is not None:
                break
            time.sleep(0.05)

        take_screenshot(item, y1, y2)
        time.sleep(0.2)
        delete_text()
        time.sleep(0.1)

        y1 = None
        y2 = None


