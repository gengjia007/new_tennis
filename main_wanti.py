import json
import time
import pyautogui
import datetime
from mouse_controller import MouseController
from wait_black import WaitBlack
from recognize import Recognize

if __name__ == "__main__":  # 保证窗口宽度559
    time.sleep(1)
    lighting_time = "12:00"
    print("waiting {} to run".format(lighting_time))

    mc = MouseController()
    wb = WaitBlack()
    rc = Recognize()

    while True:
        time.sleep(0.001)
        current_time = datetime.datetime.now()
        if str(current_time.time()).startswith(lighting_time):
            print("current_time:    " + str(current_time.time()))
            break

    # 进入入口

    entrace = (371, 766)
    mc.move_and_click(entrace)
    wb.wait_wanti_date((0,0,410,636), (371,603))

    # 选择最新日期
    latest_date = (382, 594)
    # latest_date = (127, 594)
    mc.move(latest_date)
    mc.hscroll(-500)
    time.sleep(0.2)
    mc.click()
    wb.wait((0,0,250,400), (244,396))


    mc.move((371, 657))
    time.sleep(0.2)
    mc.vscroll(-500)
    time.sleep(0.4)
    mc.hscroll(-500)

    res = rc.run_wanti((0, 0, 406, 700))

    if len(res)!=0:
        for item in res:
            mc.move_and_click(item)
            # time.sleep(0.1)
        mc.move_and_click((315, 751))
        wb.wait_wanti_date((0,0,400, 700),(338, 645))
        mc.move_and_click((61, 600))
        time.sleep(0.2)
        mc.move_and_click((61, 531))
        time.sleep(0.2)
        mc.move_and_click((25, 708))
        time.sleep(0.2)
        mc.move_and_click((313, 758))
