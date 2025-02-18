import time
import pygetwindow as gw
import pyautogui

# Step 1: Find the Roblox window
def find_roblox_window():
    windows = gw.getWindowsWithTitle('Roblox')
    if windows:
        return windows[1]
    else:
        return None

# Step 2: Focus on the Roblox window
def focus_roblox_window(window):
    window.activate()

# Step 3: Check if the window is already fullscreen
def is_fullscreen(window):
    screen_width, screen_height = pyautogui.size()
    return window.width == screen_width and window.height == screen_height

# Step 4: Fullscreen the Roblox window
def fullscreen_roblox_window():
    pyautogui.hotkey('alt', 'enter')

# Main function
def main():
    roblox_window = find_roblox_window()
    if roblox_window:
        focus_roblox_window(roblox_window)
        time.sleep(1)  # Wait for the window to come to the foreground
        if not is_fullscreen(roblox_window):
            fullscreen_roblox_window()
        else:
            print("Roblox window is already fullscreen.")
    else:
        print("Roblox window not found.")

if __name__ == "__main__":
    main()