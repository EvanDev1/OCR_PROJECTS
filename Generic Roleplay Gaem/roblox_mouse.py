import win32api, win32con
import ctypes
import time

# from normal to fully up is 850 pixels up

MOUSEEVENTF_WHEEL = 0x0800

class mouse:
    degree360 = 3597

    def move(x, y, relative=False, duration=0):
        screen_width = win32api.GetSystemMetrics(0)
        screen_height = win32api.GetSystemMetrics(1)

        x_movement = x
        y_movement = y

        if relative == False:
            mouse_x, mouse_y = win32api.GetCursorPos()

            relative_x = x - mouse_x
            relative_y = y - mouse_y

            x_movement = int(relative_x * (7680 / screen_width))
            y_movement = int(relative_y * (4320 / screen_height))

        if duration == 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x_movement, y_movement)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 1)
        else:
            print('DURATION IS NOT SET UP')
            for x in range(0, max(x_movement, y_movement)):
                move_x = 0
                move_y = 0
                if x_movement > 0:
                    move_x = int(x_movement / abs(x_movement))
                if y_movement > 0:
                    move_y = int(y_movement / abs(y_movement))
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, move_x, move_y)

                x_movement -= 1
                y_movement -= 1

                time.sleep(duration / 1000000)

    def click():
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def wheel(delta):
        # win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, delta, 0)
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, delta, 0)

    def smooth_scroll(delta):
        steps = 50
        step_delta = delta // steps
        remainder = delta % steps
        for _ in range(steps):
            mouse.wheel(step_delta)
            time.sleep(0.01)  # Small delay to ensure events are registered
        if remainder:
            mouse.wheel(remainder)

    def move_degrees(degrees):
        pixels = int(mouse.degree360 / 360 * degrees)
        print(pixels)
        mouse.move(pixels, 0, True)

    # def birds_eye_view():
    #     time.sleep(0.05)
    #     AHK.mouse_move(y=40, relative=True, speed=10)
    #     time.sleep(0.05)

    #     for x in range(0, 18):
    #         mouse.wheel(-1)
    #         time.sleep(0.05)

    #     time.sleep(0.05)