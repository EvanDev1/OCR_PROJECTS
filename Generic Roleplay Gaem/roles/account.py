from roblox_mouse import mouse
import time


class Account:
    def __init__(self, account_window):
        self.account_window = account_window

    def focus(self):
        self.account_window.activate()

    @staticmethod
    def birds_eye_view():
        mouse.move(0, 850, True, duration=25)
        mouse.smooth_scroll(-6000) # 5975 for exact 1st person to zoomed out

    @staticmethod
    def forward_view():
        mouse.smooth_scroll(3000)
        mouse.move(0, -850, True)