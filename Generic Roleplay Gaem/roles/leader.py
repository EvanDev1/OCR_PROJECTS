import keyboard
import time
import mouse
import ahk
import pyautogui
from PIL import Image
import cv2 as cv

AHK = ahk.AHK()

from roles.account import Account
from actions import move_player, jump, hold_key

tree_colors = [
    (187,134,145), # pink
    (153,107,115),
    (116,178,106), # lime green
    (73,136,70),
    (194,182,12), # yellow
    (129,127,12),
    (175,160,5),
    (96,12,87), # purple
    (57,4,55),
    (11,56,22), # dark green
    (17,71,31),
]
# 60 px wide
# 20 px high
class LeaderAccount(Account):
    taxes = 25
    food_price = 10
    wage = 10
    # Food and tax mouse positions
    sub_tax_pos = (1824, 650)
    add_tax_pos = (1889, 650)
    sub_food_pos = (1822, 525)
    add_food_pos = (1890, 526)
    sub_wage_pos = (1825, 777)
    add_wage_pos = (1890, 777)

    

    def purchase_stores(self):
        # purchasing food stores
        keyboard.press('q')
        move_player('w', 0.3)
        move_player('wa', 2.8)
        hold_key('e', 1)
        move_player('d', 0.4)
        move_player('s', 0.6)
        hold_key('e', 1)
        move_player('d', 3.6)
        hold_key('e', 1)
        move_player('s', 0.6)
        move_player('a', 0.5)
        move_player('w', 0.25)
        keyboard.release('q')

    def set_town_rates(self, new_taxes=None, new_food_price=None, new_wage=None, callback=None):
        def get_rate_clicks(current_rate, new_rate, step, add_pos, sub_pos):
            if new_rate is not None:
                rate_diff = current_rate - new_rate
                clicks = int(abs(rate_diff / step))
                rate_pos = sub_pos if rate_diff > 0 else add_pos
                return clicks, rate_pos
            else:
                return 0, None
        def click_rate(clicks, pos):
            if clicks > 0:
                AHK.mouse_move(pos[0], pos[1])
                time.sleep(0.1)
                mouse.click()
        
        food_clicks, food_pos = get_rate_clicks(self.food_price, new_food_price, 1, self.add_food_pos, self.sub_food_pos)
        tax_clicks, tax_pos = get_rate_clicks(self.taxes, new_taxes, 5, self.add_tax_pos, self.sub_tax_pos)
        wage_clicks, wage_pos = get_rate_clicks(self.wage, new_wage, 2, self.add_wage_pos, self.sub_wage_pos)

        run_amount = max(max(tax_clicks, food_clicks), wage_clicks)
        for x in range(0, run_amount):
            click_rate(food_clicks, food_pos)
            click_rate(tax_clicks, tax_pos)
            click_rate(wage_clicks, wage_pos)
            
            tax_clicks -= 1
            food_clicks -= 1
            wage_clicks -= 1

            if x < run_amount - 1:
                time.sleep(2.5)

        if callback is not None:
            callback()

    def spawn_to_vote(self):
        keyboard.press('q')
        time.sleep(0.05)

        move_player('d', 1.75)
        move_player('dw', 1.75)
        move_player('d', 6.5)
        move_player('s', 1.75)
        jump()
        move_player('d', 0.75)
        move_player('w', 1.25)
        jump()
        move_player('d', 0.5)
        move_player('s', 0.66)
        move_player('d', 0.3)

        keyboard.release('q')
        time.sleep(0.05)

    def vote(self):
        keyboard.press('q')
        time.sleep(0.05)

        move_player('d', 0.6)
        move_player('wd', 0.5)

        keyboard.release('q')

        hold_key('e', 1)

    # wood chopping functions
    