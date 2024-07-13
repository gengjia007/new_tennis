import json
import time
import pyautogui
import datetime
from mouse_controller import MouseController
from recognize import Recognize
from wait_black import WaitBlack


if __name__ == "__main__":  # 保证窗口宽度559
    time.sleep(1)
    lighting_time = "07:00"
    print("waiting {} to run".format(lighting_time))

    position = json.load(open("position.json"))
    mc = MouseController()
    rc = Recognize()
    wb = WaitBlack()

    while True:
        time.sleep(0.01)
        current_time = datetime.datetime.now()
        if str(current_time.time()).startswith(lighting_time):
            print("current_time:    " + str(current_time.time()))
            break

    # 进入入口
    '''
    entrace = position['entrace']
    mc.move_and_click(entrace)
    time.sleep(0.5)
    '''
    # 选择最新日期
    latest_date = position['date']
    mc.move_and_click(latest_date)
    wb.wait((0, 0, 303, 488), (297, 485))

    # 选择几号场馆

    num_area = position['num_area']
    mc.move_and_click(num_area)
    wb.wait((0, 0, 303, 488), (297, 485))

    '''
    # 控制下滑
    pyautogui.vscroll(-10000)
    time.sleep(0.5)
    pyautogui.vscroll(-10000)
    '''

    # 识别空场地程序
    res = rc.run((0, 0, 456, 853))
    if len(res)!=0:
        for item in res:
            mc.move_and_click(item)
            # time.sleep(0.1)
        mc.move_and_click((411, 1000))
