import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *


pyautogui.PAUSE = 1.5
time.sleep(4)

img3 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\sul.png'

tempo_limite = 30
tempo_inicial = time.time()
imagem_encontrada = False
time.sleep(1)
while not imagem_encontrada and time.time() - tempo_inicial < tempo_limite:
    try:
      x, y = pyautogui.locateCenterOnScreen(img3, confidence=0.8) #region=(0,0, w, h))
      pyautogui.moveTo(x, y)
      print("Imagem encontrada e clicada!")
      imagem_encontrada = True
    except pyautogui.ImageNotFoundException:
      time.sleep(1)
      print('Imagem não encontrada. Tentando novamente...')

    except Exception as e:
      print(f"Ocorreu um erro: {e}")
      break
