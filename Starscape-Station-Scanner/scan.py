import json
import time
import mouse
import keyboard
from ahk import AHK as ahk

AHK = ahk()
from PIL import ImageGrab, ImageFilter, ImageOps
import tempfile
import os
import re

from ocrspace import API
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

OCR_api_key = "K87155629288957"

OCR_api = API(api_key=OCR_api_key, language="eng", ocrengine="2")


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
    # global ready_to_continue

    # while True:
    #     if ready_to_continue == True:
    #         ready_to_continue = False
    #         break
    #     time.sleep(0.1)

    lookup_name = item_name
    if "-" in item_name:
        lookup_name = item_name.split("-")[0]
        print(f"Complex name for item: {item_name}, skipping over it :)")

    AHK.mouse_move(1154, 322)
    mouse.click()
    time.sleep(0.2)

    AHK.mouse_move(835, 379)
    mouse.click()

    time.sleep(0.5)

    AHK.mouse_move(655, 695)
    mouse.click()

    time.sleep(1)
    type_string(lookup_name)

    time.sleep(0.2)
    AHK.mouse_move(658, 733)
    mouse.click()

    time.sleep(0.2)
    AHK.mouse_move(661, 754)
    mouse.click()

    time.sleep(0.2)
    AHK.mouse_move(778, 395)
    mouse.click()

    time.sleep(0.2)
    AHK.mouse_move(1224, 745)
    mouse.click()


class Processing:
    def capture(cords, threshold=False):
        region = cords
        capture = ImageGrab.grab(bbox=region)

        capture = ImageOps.grayscale(capture)
        capture = capture.filter(ImageFilter.SHARPEN)

        if threshold:
            capture = capture.point(lambda p: 0 if p < threshold else 255)

        return capture

    def extract_text(image):
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img:
            temp_img_path = temp_img.name
            image.save(temp_img_path)

        # text = pytesseract.image_to_string(temp_img_path, lang='eng', config=f"--psm 6 --oem 3")
        # text = OCR_api.ocr_file(temp_img_path)
        text = pytesseract.image_to_string(image)

        os.unlink(temp_img_path)
        return text

    def get_station_buy(item_name):
        capture = Processing.capture((1003, 365, 1107, 384))
        text = Processing.extract_text(capture)

        text = text.replace(",", "")
        try:
            text = int(text)
            return text
        except:
            print(f"Could not scan station buy for item: {item_name}!!")


def scan_everything():
    items = read_json_file("item_data.json")
    saved_items = items
    for item_name, item in items.items():
        if item["station_buy"] == 0:
            lookup_item(item_name)
            time.sleep(0.5)
            buy = Processing.get_station_buy(item_name)
            if buy:
                saved_items[item_name]["station_buy"] = buy
                save_to_json_file(saved_items, "item_data.json")
                time.sleep(0.2)

        # break


time.sleep(2)
scan_everything()

# (658, 733) order items by
# (661, 754) name
# (778, 395) first item in list
# (1224, 745) select button
# (1154, 322) exit button

# 1003 365 1107 384
