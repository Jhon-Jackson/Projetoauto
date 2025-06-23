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
            pyautogui.keyDown('w')
            time.sleep(0.5)
        break

    except:
        continue

pyautogui.keyUp('w')