import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *


pyautogui.PAUSE = 1.5
time.sleep(4)


img3 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\coord1_cinza.png'
while True:
    try:
        for img in img3:
            if img not in img3:
                img = pyautogui.locateOnScreen(img3,1827, 9, 50, 15)
                pyautogui.keyDown('w')
                time.sleep(0.5)
            else:
                continue

        break

    except:
        continue

pyautogui.keyUp('w')