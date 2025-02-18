from scripts.lookup_info import lookup_item
from scripts.type_string import type_string
from scripts.processing import Processing
from scripts.vio_api import get_item_list
import json

import keyboard
import time

with open("item_list.txt", "r") as file:
    # Initialize an empty list to store the rows
    item_list = []
    hold = []
    # Loop through each line in the file
    for line in file:
        if "-" in line:
            hold.append(line.strip())
        else:
            # Append the line to the list, removing any leading or trailing whitespace characters
            item_list.append(line.strip())

    for item in hold:
        item_list.append(item)

time.sleep(2)


def save_recipes_to_text_file(recipe_data):
    json_data = json.dumps(recipe_data, indent=4)

    # Write the JSON data to the file
    with open("item_recipes.txt", "w") as file:
        file.write(json_data)


items_dict = {}
times_ran = 0

thingy = False


def switch_thingy():
    global thingy
    if thingy == False:
        thingy = True


keyboard.add_hotkey("alt", switch_thingy)


for x in range(7, len(item_list)):

    item = item_list[x]
    item_name = Processing.remove_suffix(item)

    while True:
        time.sleep(0.1)
        if thingy == True:
            thingy = False
            break
    print(item_name)
    lookup_item(item_name, True)


# save_recipes_to_text_file(items_dict)
