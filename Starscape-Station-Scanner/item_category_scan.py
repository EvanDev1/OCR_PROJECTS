import json
import time
import mouse
import keyboard
from ahk import AHK as ahk

AHK = ahk()


def read_json_file(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    return data


def save_to_json_file(data, file_name):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def type_string(word):
    for char in word:
        if char.isupper():
            keyboard.press_and_release("shift+" + char.lower())
        elif char == "(":
            keyboard.press_and_release("shift+9")  # '(' character
        elif char == ")":
            keyboard.press_and_release("shift+0")  # ')' character
        else:
            keyboard.press_and_release(char)
        time.sleep(0.01)


ready_to_continue = False


def y_pressed():
    global ready_to_continue
    ready_to_continue = True


keyboard.add_hotkey("alt", y_pressed)


def lookup_item(item_name):
    global ready_to_continue

    while True:
        if ready_to_continue == True:
            ready_to_continue = False
            break
        time.sleep(0.1)

    lookup_name = item_name
    if "-" in item_name:
        lookup_name = item_name.split("-")[0]
        print(f"Complex name for item: {item_name}, skipping over it :)")

    AHK.mouse_move(835, 379)
    mouse.click()

    time.sleep(0.5)

    AHK.mouse_move(655, 695)
    mouse.click()

    time.sleep(1)
    type_string(lookup_name)


with open("item_list.txt", "r") as file:
    # Initialize an empty Python array
    my_array = []
    # Read each line in the file
    for line in file:
        # Remove any leading or trailing whitespace characters
        line = line.strip()
        # Append the line to the array
        my_array.append(line)

# Print the array to check the contents


def scan_everything():
    items = read_json_file("item_data.json")
    existing_items = read_json_file("item_categories.json")

    add_obj = existing_items

    categories = []

    for item_name, category in existing_items.items():
        for cat in category:
            if cat not in categories:
                categories.append(cat)

    print(categories)


# time.sleep(2)
scan_everything()
