import pyautogui
import numpy as np


class Recognize:
    def __init__(self) -> None:
        pass

    def run(self, region):
        im = pyautogui.screenshot(region=region)
        p1 = [(177, 773), (258, 769), (338, 771), (419, 770)]
        p2 = [(177, 828), (258, 828), (338, 828), (419, 828)]
        res = []
        for item in p1:
            if im.getpixel(item)[0] != 221:
                res.append(item)
                break
        for item in p2:
            if im.getpixel(item)[0] != 221:
                res.append(item)
                break
        return res

    def run_wanti(self, region):
        im = pyautogui.screenshot(region=region)
        p1 = [(200, 216), (280, 216), (357, 216)]
        p2 = [(200, 256), (280, 256), (357, 256)]
        res = []
        for item in p1:
            if im.getpixel(item)[0] == 255:
                res.append(item)
                break
        for item in p2:
            if im.getpixel(item)[0] == 255:
                res.append(item)
                break
        return res
