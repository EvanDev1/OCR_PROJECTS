# Starting cost: 8.8k
# 1100
import cv2 as cv

from roblox_mouse import mouse
import keyboard
from threading import Thread
import pygetwindow as gw

import ahk
AHK = ahk.AHK()

import time
from PIL import ImageGrab

import time


# Role imports
from actions import move_player, jump, hold_key
from roles.leader import LeaderAccount
from roles.farmer import FarmerAccount
from roles.lumberjack import Lumberjack as LumberjackAccount

# World imports
from world.check_balance import check_balance
from world.fullscreen import fullscreen_windows
from world.spawner import Spawner as SpawnerClass
from world.game import Game

# User settings
mouse_dpi = 1600


windows = gw.getWindowsWithTitle('Roblox')

Spawner = SpawnerClass()
# trees_screen = trees = [(1147, 292), (1170, 678), (1184, 540), (1212, 250), (1212, 422), (1222, 312), (1247, 363), (1298, 367), (1315, 480), (1362, 394), (1368, 563), (1384, 447)]
# trees = [(182, 408), (205, 22), (219, 160), (247, 450), (247, 278), (257, 388), (282, 337), (333, 333), (350, 220), (397, 306), (403, 137), (419, 253)]

# closest = LumberjackAccount.find_closest_tree(trees)
# print(closest)
# result_image = cv.imread('game_screenshot.png')
# box_width = 5

# # for pixel in trees:
# #     x, y = pixel
# #     cv.rectangle(result_image, (x - box_width, y - box_width), (x + box_width, y + box_width), (0, 0, 255), -1)

# x, y = closest
# # x, y = trees[1]
# cv.rectangle(result_image, (x - box_width, y - box_width), (x + box_width, y + box_width), (0, 0, 255), -1)
# cv.imshow("Result", result_image)
# cv.waitKey(0)
# cv.destroyAllWindows()
Leader = LeaderAccount(windows[0])
# Farmer = FarmerAccount(windows[1])
Lumberjack = LumberjackAccount(windows[1])

# Leader.focus()
# Leader.purchase_stores()

Lumberjack.focus()
time.sleep(2)
Spawner.become_civilian()
Lumberjack.buy_axe_tool()
Lumberjack.farm_wood()


# fullscreen_windows([Leader.account_window, Farmer.account_window])

# def town_rates_finished():
#     print('TOWN RATES ARE FINISHED!!!!')


# town_rates = Thread(target=Leader.set_town_rates, args=(0, 0, 0, town_rates_finished))
# town_rates.start()
# Leader.purchase_stores()






# Leader.focus()
# time.sleep(1)
# Leader.purchase_stores()


# Farmer.begin_farming()

# Leader.focus()
# time.sleep(0.5)
# Leader.set_town_rates(0, 0)




# purchase axe, sickle, and food store
# get approval to 60% using farmer account and all 4 council members

# 8k + 50 + 600 + 50 + 600

# Takes 32 seconds to get to arena
# Takes 1.5 minutes to eat popcorn
# takes 30 seconds to get back from arena



# every 13 mins:
# 36 food for 6 accounts to stay alive
# 5 mins for everyone to eat

# 8 min window to farm

# can make MAX 94 wheat per 8 mins

# cost leader $10 per food that people buy even if leader is selling it
# (when food price is 0)

# takes 210 / # of accounts holding praise signs to get praise to 61%





# durability gets 54 food (54.25 or something idfk)