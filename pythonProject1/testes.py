import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *

pyautogui.PAUSE = 1.5
time.sleep(4)


# Direção = [r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\mapa1_cinza.png',
#            r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa2_cinza.png',
#            r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa3_cinza.png',
#            r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa4_cinza.png',
#            r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa5_cinza.png',
#            r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa6_cinza.png']
#
# while True:
#     GirarTela()
#     while True:
#         try:
#             localisarimg(Direção, 0.7,1720, 41, 172, 136)
#             #localisarimg(Direção1, 0.7)
#             print("Encontrei até que fim")
#             break
#         except Exception as e:
#             print("imagen nao encontrada")
#             GirarTela()
#         continue
#     break


pyautogui.keyUp('w')
