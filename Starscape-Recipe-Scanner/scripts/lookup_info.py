# def open_item(item):
#     AHK.mouse_move(792, 739)
#     AHK.click()
#     time.sleep(0.75)
#     type_word(item)
#     AHK.mouse_move(836, 359)
#     time.sleep(0.1)
#     AHK.click()
#     AHK.mouse_move(1138, 409)
#     for x in range (0, 6):
#         time.sleep(0.1)
#         AHK.run_script(scroll_down_script)
#     time.sleep(0.5)
import mouse

import keyboard

import ahk

AHK = ahk.AHK()

import json

from scripts.type_string import type_string
from scripts.processing import Processing

import time

mouse_pos = {
    # 'search_bar': (792, 739),
    "search_bar": (630, 760),
    "info_box": (1138, 409),
    "item_list": [
        (840, 358),
        (840, 396),
        (840, 434),
        (840, 471),
        (840, 509),
        (840, 543),
        (840, 582),
        (840, 619),
        (840, 655),
        (840, 691),
        (840, 726),
        (840, 765),
    ],
}


def save_output(var):
    json_data = json.dumps(var, indent=4)

    # Write the JSON data to the file
    with open("output.txt", "w") as file:
        file.write(json_data)


def create_whitelist(item_name):
    seen_chars = set()  # Set to keep track of seen characters
    whitelist = ""
    for char in item_name:
        char_lower = char.lower()
        if (
            char_lower not in seen_chars
        ):  # Check if lowercase version of char is not in seen_chars
            seen_chars.add(char_lower)  # Add lowercase char to seen_chars
            seen_chars.add(
                char_lower.upper()
            )  # Also add uppercase version to seen_chars
            whitelist += char  # Add char to whitelist
    return whitelist


ready_to_continue = False


def y_pressed():
    global ready_to_continue
    ready_to_continue = True


keyboard.add_hotkey("y", y_pressed)


def lookup_item(item_name, simple=False):
    global ready_to_continue

    lookup_name = item_name
    complex_search = False
    if "-" in item_name:
        lookup_name = item_name.split("-")[0]
        complex_search = True

    AHK.mouse_move(1329, 261)
    mouse.click()
    time.sleep(0.2)

    AHK.mouse_move(835, 379)
    mouse.click()

    time.sleep(0.2)

    AHK.mouse_move(655, 695)
    mouse.click()

    time.sleep(1)
    type_string(lookup_name)

    # AHK.mouse_move(840, 345)
    # mouse.click()
    # time.sleep(0.2)

    # AHK.mouse_move(1229, 818)
    # mouse.click()

    if simple == False:
        if complex_search == True:
            time.sleep(0.25)
            print(
                f"Complex item name ({item_name})! Press (y) once you have opened up the item info"
            )
            while True:
                time.sleep(1)
                if ready_to_continue == True:
                    ready_to_continue = False
                    break
        else:
            AHK.mouse_move(mouse_pos["item_list"][0][0], mouse_pos["item_list"][0][1])
            mouse.click()

        time.sleep(0.2)
        AHK.mouse_move(mouse_pos["info_box"][0], mouse_pos["info_box"][1])
        time.sleep(0.1)
        for x in range(0, 20):
            mouse.wheel(-1)
            time.sleep(0.01)
