import cv2 as cv
import time
import numpy as np
import pyautogui
import win32api
import keyboard
import win32con

from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter

pyautogui.PAUSE = 0.1

window_capture = WindowCapture("TimbermanVS")
vision = Vision('background.png')
# vision.init_control_gui()

hsv_filter = HsvFilter(0, 0, 0, 179, 255, 144, 0, 255, 218, 153)


def l_click():
    pyautogui.leftClick()
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #time.sleep(0.1)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def r_click():
    pyautogui.rightClick()
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    #time.sleep(0.1)
    #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def is_branch(image):
    if np.mean(image) != 102.0:
        return True
    else:
        return False


left_side = True
where = 'L'
time.sleep(1)
while True:

    screenshot = window_capture.get_screenshot()
    processed_image = vision.apply_hsv_filter(screenshot, hsv_filter)
    # cv.imshow('Processed', processed_image)
    # cv.imshow("ss", output_image)

    # [height,width]
    l_image = processed_image[238:260, 235:280]
    # l_lower_branch = processed_image[293:315, 235:280]
    r_image = processed_image[238:260, 350:390]
    # r_lower_branch = processed_image[293:315, 350:390]

    if left_side:
        if is_branch(l_image):
            where = 'R'
            print(1)
        elif is_branch(r_image):
            where = 'L'
            print(2)
        else:
            where = 'L'
            print(3)
    else:
        if is_branch(r_image):
            where = 'L'
            print(4)
        elif is_branch(l_image):
            where = 'R'
            print(5)
        else:
            where = 'R'
            print(6)

    if where == 'L':
        l_click()
        left_side = True
    else:
        r_click()
        left_side = False
    cv.imshow('left', l_image)
    cv.imshow('right', r_image)
    # cv.imshow('right', r_image_branch)
    # cv.imshow('leight', l_image_branch)
