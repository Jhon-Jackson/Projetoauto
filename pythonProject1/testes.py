import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *


pyautogui.PAUSE = 1.5
time.sleep(4)

img3 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\my.foto.png'
local = pyautogui.locateOnScreen(img3, confidence=0.5, region=(1742,55, 136,99))
if local:
    x, y = pyautogui.center(local)

    pyautogui.moveTo(x, y)

    print('Imagem encontrada nas coordenadas:', x, y)



