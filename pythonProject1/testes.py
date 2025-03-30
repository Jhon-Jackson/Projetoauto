import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *


pyautogui.PAUSE = 1.5
time.sleep(4)

img3 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\sul.png'
for pos in pyautogui.locateAllOnScreen(img3, confidense=0.8):
    print(pos)
# fixo = 1816, 61
# while True:
#     local = NpcFrase1(img3,w=50,h=50)
#     posisao = pyautogui.position(local)
#     time.sleep(4)
#     if posisao == fixo:
#         print('localizado')
#         break
#     else:
#         buscarnpc
