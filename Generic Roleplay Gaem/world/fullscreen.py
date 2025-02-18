import time
import pygetwindow as gw
import pyautogui

# Step 3: Check if the window is already fullscreen
def is_fullscreen(window):
    screen_width, screen_height = pyautogui.size()
    return window.width == screen_width and window.height == screen_height

def fullscreen_windows(windows):
    minimized = []

    for window in windows:
        if not is_fullscreen(window):
            minimized.append(window)
        else:
            print('Window is already fullscreened :)')

    for window in minimized:
        window.activate()
        pyautogui.hotkey('alt', 'enter')