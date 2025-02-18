import pyautogui
import os

def take_screenshot(item_name, y1, y2):
    # top_left_x = 822 * 2
    # top_left_y = 333 * 2
    # bottom_right_x = 854 * 2
    # bottom_right_y = 365 * 2

    #4k cords
    top_left_x = 822 * 2
    top_left_y = 333 * 2 - 1
    bottom_right_x = 854 * 2
    bottom_right_y = 365 * 2 - 1

    top_left_y = y1
    bottom_right_y = y2

    #4k market cords
    # top_left_x = 730 * 2 + 4
    # top_left_y = 314 * 2 + 4
    # bottom_right_x = 766 * 2 - 4
    # bottom_right_y = 349 * 2 - 2
    

    # Calculate the width and height of the region
    width = bottom_right_x - top_left_x
    height = bottom_right_y - top_left_y

    # Directory to save the screenshot
    # save_directory = r'C:\Users\evanl\OneDrive\Pictures\1scarscape-items'
    save_directory = r'C:\Users\evanl\OneDrive\Pictures\1complex-items'

    # Ensure the directory exists
    os.makedirs(save_directory, exist_ok=True)

    # Capture the screenshot
    screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))

    # Save the screenshot with a timestamp
    file_path = os.path.join(save_directory, f"{item_name}.png")
    screenshot.save(file_path)

    print(f"Screenshot saved as '{file_path}'") 