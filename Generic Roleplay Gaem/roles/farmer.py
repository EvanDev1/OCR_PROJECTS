import keyboard
import time

import ahk
import mouse

AHK = ahk.AHK()

from roles.account import Account
from actions import move_player, jump, hold_key

plot_dur = 0.5006
row_len = 21
column_len = 12

column_len = 12
plot1_row_len = 21
plot2_row_len = 31

cir = 0.08

class FarmerAccount(Account):
    current_plot = 1
    direction = 'right'

    def buy_sickle(self):
        keyboard.press_and_release('shift')
        # moves player from civilian spawn to buy best sickle
        keyboard.press('q')
        move_player('s', 1.85)
        move_player('d', 1.6)
        keyboard.release('q')

        time.sleep(4)
        # jump()
    def move_to_field(self):
        keyboard.press('q')
        move_player('wa', 3.5)
        move_player('w', 4.1)
        move_player('wd', 1)
        move_player('d', 0.9)
        move_player('s', 0.3)
        keyboard.release('q')
        keyboard.press_and_release('shift')

    def begin_farming(self):
        self.buy_sickle()
        self.move_to_field()
        time.sleep(1)

        keyboard.press_and_release('shift')
        time.sleep(0.1)


        for x in range(0, 36):
            self.farm_rice()
            self.move_up_plot()
            
            time.sleep(0.5)

        keyboard.press_and_release('shift')


    def move_up_plot(self):
        if self.current_plot % 21 == 0:
            move_player('s', plot_dur)
            if self.direction == 'right':
                self.direction = 'left'
            else:
                self.direction = 'right'
        else:
            if self.direction == 'right':
                move_player('d', plot_dur)
            else:
                move_player('a', plot_dur)
        self.current_plot += 1

    def farm_rice(self):
        time.sleep(0.5)

        for x in range(0, 16):
            mouse.click()
            time.sleep(0.6)