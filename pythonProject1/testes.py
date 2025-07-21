import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *


pyautogui.PAUSE = 1.5
time.sleep(4)

# X,Y = 592, 506
# print(X, Y)
#
# while True:
#     if X > 586 and Y <= 506:
#         pyautogui.keyDown('w')
#         X -= 1
#         time.sleep(0.4)
#     elif X == 586:
#         pyautogui.keyUp('w')
#         break

Direção = [r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\mapa1_cinza.png',
           r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa2_cinza.png',
           r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa3_cinza.png']
#Direção1 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\pergaminhoTele.png'
while True:
    GirarTela()
    while True:
        try:
            localisarimg(Direção, 0.7,1720, 41, 172, 136)
            #localisarimg(Direção1, 0.7)
            print("Encontrei até que fim")
            break
        except Exception as e:
            print("imagen nao encontrada")
            GirarTela()
        continue
    break

