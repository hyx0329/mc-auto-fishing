import sys
import time

if sys.platform.startswith('linux'):
    from mcfishing.actions_linux import *
elif sys.platform.startswith('win32'):
    from mcfishing.actions_win import *
else:
    raise EnvironmentError("Not supported platform!")

from mcfishing.image_process import *

from pynput.mouse import Button as mBtn
from pynput.mouse import Controller as mCon
from pynput.keyboard import Key as kKey
from pynput.keyboard import Controller as kCon

# from pynput import keyboard
import matplotlib.pyplot as plt


mouse = mCon()
keyboard = kCon()


def mouse_click():
    mouse.press(mBtn.right)
    mouse.release(mBtn.right)


def on_press_esc(key):
    if key == keyboard.Key.esc:
        exit(0)


def run():
    target_window_id = search_window()
    if len(target_window_id) == 0:
        print('No game window found! Exiting')
        exit(1)
    activate_window(target_window_id)
    time.sleep(1)
    keyboard.press(kKey.esc)
    keyboard.release(kKey.esc)
    time.sleep(1)
    mouse_click()
    time.sleep(2)

    # listener = keyboard.Listener(
    #     on_press=on_press_esc
    # )
    # listener.start()

    def get_ratio():
        window_capture = shot_window(target_window_id)
        window_center = cutout_center(window_capture, width=20, height=20)
        split_mask = split_by_color_distance(window_center, np.array([0,0,0]), 10)
        a = np.sum(split_mask)
        b = np.prod(np.shape(split_mask))
        ratio = a/b
        print(ratio)
        return ratio

    while True:
        current_window_id = get_current_active_window()
        if current_window_id != target_window_id:
            print("window changed! now exiting")
            break
        
        ratio = get_ratio()
        if ratio > 0.025:
            continue

        # fish caught
        print('fish caught (possibly)')
        mouse_click()
        time.sleep(1)

        ratio = get_ratio()
        if ratio < 0.025:  # which means the line is not present
            # start another shot
            print('start another round')
            mouse_click()
            # wait for stablize
            time.sleep(2)

    return None
