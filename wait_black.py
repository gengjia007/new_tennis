import pyautogui
import numpy as np

class WaitBlack:
    def wait(self, region, position):
        flag = 0
        while True:
            # print(flag)
            im = pyautogui.screenshot(region=region)
            res = im.getpixel(position)
            if res[0] != 255 and flag == 0:
                flag += 1
            if res[0] == 255 and flag == 1:
                flag += 1
            if flag == 2:
                print(flag)
                break

    def wait_wanti_date(self, region, position):
        flag = 0
        while True:
            # print(flag)
            im = pyautogui.screenshot(region=region)
            res = im.getpixel(position)
            if res[0] != 255:
                flag += 1
                print(flag)
            if flag == 2:
                break

    def wait_wanti_trans(self, region, position):
        flag = 0
        while True:
            # print(flag)
            im = pyautogui.screenshot(region=region)
            res = im.getpixel(position)
            if res[0] != 255:
                flag += 1
                print(flag)
            if flag == 3:
                break
