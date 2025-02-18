import keyboard
import math
import time
import mouse
import ahk
import pyautogui
from PIL import Image, ImageGrab, ImageFilter, ImageOps, ImageEnhance
import cv2 as cv
import numpy as np

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

AHK = ahk.AHK()

from roles.account import Account
from actions import move_player, jump, hold_key


tree_colors = [
    (187,134,145), # pink
    (153,107,115),
    (100, 60, 60),
    (116,178,106), # lime green
    (73,136,70),
    (50, 100, 40),
    (194,182,12), # yellow
    (129,127,12),
    (175,160,5),
    (106, 104, 0),
    (96,12,87), # purple
    (57,4,55),
    (11,56,22), # dark green
    (17,71,31),
    (4, 40, 11),
    (100, 100, 100), # white
    (150, 150, 150),
    (255, 255, 255),
    (235, 235, 235),
    
]

x_time = 3.1
y_time = 3.4

x_px_time = x_time / 450
y_px_time = y_time / 450

# Tree health and wood
# Normal: 50 health, 10 wood
# Food tree: 100 health, 10 wood, 10 food
# Money tree: 250 health, 100 wood

class Lumberjack(Account):
    wood = 0
    pos = (0, 0)

    @staticmethod
    def buy_axe_tool():
        keyboard.press('q')
        move_player('s', 2.6)
        move_player('d', 0.2)
        keyboard.release('q')

        time.sleep(4)

        keyboard.press('q')
        move_player('d', 2)
        keyboard.release('q')

    @staticmethod
    def decode_tree_health(health, max_health):
        if health is not None and max_health is not None:
            if max_health == 50 or max_health == 59:
                print('add 10 wood')
                return 9
            elif max_health == 100 or max_health == 109 or max_health == 199:
                print('add 10 wood, 10 food')
                return 15
            elif max_health == 250 or max_health == 259:
                print('add 100 wood')
                return 35
        else:
            print("Couldn't find it :c")
            return None

    def chop_tree(self, tree_pos):
        keyboard.press('q')

        move_x = tree_pos[0] - self.pos[0]
        move_y = tree_pos[1] - self.pos[1]

        move_player('d', move_x * x_px_time)
        move_player('w', move_y * y_px_time)
        
        keyboard.release('q')

        mouse.click()
        
        time.sleep(0.5)
        keyboard.press_and_release('shift')
        time.sleep(0.5)
        health, max_health = self.get_tree_health()
        keyboard.press_and_release('shift')
        clicks = self.decode_tree_health(health, max_health)
        for x in range(0, clicks):
            mouse.click()
            time.sleep(0.5)
            if x % 2 == 0:
                move_player('a', 0.3)
            else:
                move_player('d', 0.3)
            
            time.sleep(0.2)
        
        self.pos = tree_pos

    @staticmethod
    def find_closest_tree(points):
        # Function to calculate Euclidean distance from (0, 0) to a point (x, y)
        def distance_to_origin(x, y):
            return math.sqrt(x**2 + y**2)
        
        # Initialize variables to keep track of the minimum distance and corresponding point
        min_distance = float('inf')
        closest_point = None
        
        # Iterate through each point in the list
        for (x, y) in points:
            # Calculate distance from (0, 0) to the current point
            dist = distance_to_origin(x, y)
            
            # Update minimum distance and closest point if current point is closer
            if dist < min_distance:
                min_distance = dist
                closest_point = (x, y)
        
        return closest_point

    def farm_wood(self):
        self.birds_eye_view()
        time.sleep(0.5)
        screenshot = pyautogui.screenshot()
        screenshot.save('game_screenshot.png')
        keyboard.press_and_release('shift')
        time.sleep(0.1)
        keyboard.press('q')
        move_player('s', 1.1)
        move_player('d', 0.2)
        keyboard.release('q')

        

        keyboard.press_and_release('shift')

        matched_trees = self.scan_tree_positions(1)

        trees_pos = []
        for tree in matched_trees:
            x_pos = tree[0] - 980 #+ 15
            y_pos = (450 - (tree[1] - 250)) #- 15 # the 15 is so it doesn't run into the tree
            trees_pos.append((x_pos, y_pos))

        # closest_tree = self.find_closest_tree(trees_pos)
        self.forward_view()
        self.chop_tree(trees_pos[0])
        self.chop_tree(trees_pos[1])
        self.chop_tree(trees_pos[2])
        

    @staticmethod
    def detect_tree_match(pixel_color, tree_colors):
        for color in tree_colors:
            r, g, b = color
            pr, pg, pb = pixel_color
            if abs(r - pr) <= 5 and abs(g - pg) <= 5 and abs(b - pb) <= 5:
                return True  # Return True if a match is found
        return False  # Return False if no match is found

    @staticmethod
    def check_within_distance(pixel1, pixel2, max_distance=5):
        # Calculate the differences in x and y coordinates
        delta_x = abs(pixel2[0] - pixel1[0])
        delta_y = abs(pixel2[1] - pixel1[1])

        # Check if both differences are within the maximum distance
        if delta_x <= max_distance and delta_y <= max_distance:
            return True
        else:
            return False

    

    @staticmethod
    def scan_tree_positions(box_size):
        screen = Image.open('game_screenshot.png')
        result_image = cv.imread('game_screenshot.png')

        matched_pixels = []

        for x in range(980, 1430, box_size):
            for y in range(250, 700, box_size):
                pixel_color = screen.getpixel((x, y))
                if Lumberjack.detect_tree_match(pixel_color, tree_colors):
                    matched_pixels.append((x, y))
                    # cv.rectangle(result_image, (x - box_size // 2, y - box_size // 2), 
                    #              (x + box_size // 2, y + box_size // 2), (0, 0, 255), 1)


        filtered_pixels = []
        remove_pixels = []

        for pixel in matched_pixels:
            if pixel in remove_pixels:
                continue

            filtered_pixels.append(pixel)

            for pixel2 in matched_pixels:
                if pixel == pixel2 or pixel2 in remove_pixels:
                    continue

                within_distance = Lumberjack.check_within_distance(pixel, pixel2, 50)
                if within_distance:
                    remove_pixels.append(pixel2)


        box_width = 5
        for pixel in filtered_pixels:
            x, y = pixel
            cv.rectangle(result_image, (x - box_width, y - box_width), (x + box_width, y + box_width), (0, 0, 255), -1)

        # cv.imshow("Result", result_image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        return filtered_pixels

    @staticmethod
    def get_tree_health():
        def extract_numbers(s):
            return int(''.join([char for char in s if char.isdigit()]))
        capture = ImageGrab.grab(bbox=(360, 370, 1600, 790))
        capture = capture.convert("RGBA")
    
        # Convert the image to a NumPy array
        data = np.array(capture)
        
        # Define a mask to isolate the exact green pixels
        white_mask = (data[:, :, 0] == 255) & (data[:, :, 1] == 255) & (data[:, :, 2] == 255) & (data[:, :, 3] == 255)
        
        # Create a new image where the exact green pixels are white and other pixels are black
        filtered_data = np.zeros_like(data)
        filtered_data[white_mask] = [255, 255, 255, 255]
        
        # Convert the filtered data back to an image
        filtered_image = Image.fromarray(filtered_data)
        
        # Convert the image to grayscale
        capture = ImageOps.grayscale(filtered_image)
        
        # Increase the contrast
        enhancer = ImageEnhance.Contrast(capture)
        capture = enhancer.enhance(2)

        # Sharpen the image
        capture = capture.filter(ImageFilter.SHARPEN)
        
        # Apply thresholding
        capture = capture.point(lambda x: 0 if x < 140 else 255, '1')
        
        # Resize the image to improve OCR accuracy
        capture = capture.resize((capture.width * 2, capture.height * 2), Image.Resampling.LANCZOS)

        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789/'
        text = pytesseract.image_to_string(capture, config=custom_config)
        
        health = text.split('/')

        if health[0] and health[1]:
            return extract_numbers(health[0]), extract_numbers(health[1])
        return None, None
    
