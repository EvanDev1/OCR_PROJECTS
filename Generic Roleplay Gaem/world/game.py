import time
import pyautogui
from PIL import ImageGrab

council_color = (107, 50, 124)
flood_color = (51,88,130)

class Game():
    
    def detect_events():
        def get_pixel_color(x, y):
            # Capture the screen
            screen = ImageGrab.grab()
            # Get the color of the pixel at (x, y)
            color = screen.getpixel((x, y))
            return color
        
        while True:
            # Get the colors of the pixels at specified positions
            pixel1 = get_pixel_color(500, 150)
            pixel2 = get_pixel_color(950, 150)
            pixel3 = get_pixel_color(1400, 150)
            
            if pixel1 == pixel2 and pixel2 == pixel3:
                if pixel1 == council_color:
                    print('COUNCIL EVENT')
                elif pixel1 == flood_color:
                    print('FLOOD EVENT')
                else:
                    print(f'unkown event color: {pixel1}')
            
            # Wait for 5 seconds
            break
            time.sleep(5)
