import pyautogui
import time

pyautogui.PAUSE = 2.5
time.sleep(5)

# input('enter')
# pyautogui.position()
# print(pyautogui.position())

# time.sleep(5)
#
# pyautogui.press('b')

# S = Point(x=1816, y=61)
#Point(x=1742, y=49),Point(x=1878, y=148)
# w = 136 h = 99
img = pyautogui.screenshot('my.foto.png', region=(1742,55, 136,99))