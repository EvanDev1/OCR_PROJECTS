import os
from PIL import Image
import pyautogui
import keyboard
import time
from actions import *

class Spawner():
    positions = [
        [(511, 409), (1133, 419), (1264, 505), (1129, 415), (537, 477), (1036, 375), (511, 397), (1121, 423)], # 1
        [(146, 457), (1215, 505), (709, 500), (190, 418), (137, 425), (753, 431)], # 2
        [(13, 481), (493, 539), (783, 419), (50, 434), (647, 427)], # 3
        [(553, 383), (1111, 404), (1209, 460), (554, 381), (1109, 407), (1424, 555)], # 4
        [(462, 395), (363, 558), (1159, 461)], # 5
        [(149, 423), (591, 487), (808, 406)], # 6
        [(228, 491), (1105, 391), (1187, 435)], # 7
        [(890, 392), (1120, 432), (469, 490)], # 8
        [(303, 491), (820, 391), (787, 425)] # 9
    ]
    spawn_movement = [
        [['d', 0.25], ['w', 1.7]], # 1
        [['w', 1.7]], # 2
        [['a', 0.25], ['w', 1.7]], # 3
        [['d', 0.25], ['w', 1.95]], # 4
        [['w', 1.95]], # 5
        [['a', 0.25], ['w', 1.95]], # 6
        [['d', 0.25], ['w', 2.2]], # 7
        [['w', 2.2]], # 8
        [['a', 0.25], ['w', 2.2]], # 9
    ]

    @staticmethod
    def is_white(rgb):
        r, g, b = rgb
        if r > 120 and g > 120 and b > 120:
            if abs(r - g) <= 20 and abs(g - b) <= 20 and abs(b - r) <= 20:
                return True
        return False
    
    @staticmethod
    def is_red(rgb):
        r, g, b = rgb
        if r > 70 and g < 20 and b < 20:
            return True
        return

    def check_pixels_in_screenshot(self):
        """Check if the specified pixels in a screenshot are white."""
        screenshot = pyautogui.screenshot()
        for index, pos_group in enumerate(self.positions):
            for pos in pos_group:
                if not self.is_white(screenshot.getpixel(pos)):
                    break
            else:
                return index
        return None

    def get_spawn(self):
        """Check pixel positions in the current screenshot."""
        index = self.check_pixels_in_screenshot()
        if index is not None:
            return index
        else:
            print("The screenshot does not match any of the arrays. ERROR")

    def move_to_center(self):
        """Move player from spawn to the center of the red carpet"""
        spawn = self.get_spawn()
        if spawn is not None:
            keyboard.press_and_release('shift')
            keyboard.press('q')
            for movement in self.spawn_movement[spawn]:
                move_player(movement[0], movement[1])
        else:
            print('SPAWN NOT RECOGNIZED BIG ISSUE UH OHHHHH')

    def become_civilian(self):
        self.move_to_center()
        move_player('a', 1.25)
        move_player('wa', 0.25)
        keyboard.release('q')
        hold_key('e', 1)

    def become_council(self):
        self.move_to_center()
        move_player('d', 1.2)
        move_player('w', 2.75)
        move_player('d', 0.2)
        keyboard.release('q')
        # hold_key('e', 1)

    def clear_spawn(self, accounts):
        for account in accounts:
            account.account_window.activate()
            keyboard.press('q')
            keyboard.press('space')
            move_player('s', 1.5)
            move_player('d', 3)
            keyboard.release('space')
            keyboard.release('q')
            time.sleep(0.05)

    @staticmethod
    def reset():
        keyboard.press_and_release('esc')
        time.sleep(0.5)
        keyboard.press_and_release('r')
        time.sleep(0.2)
        keyboard.press_and_release('enter')
        time.sleep(1)
        keyboard.press_and_release('space')
        time.sleep(6)

