import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *

time.sleep(3)

img3 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\clickpertonpc1.png'
n = 1
time.sleep(2)
while True:
    time.sleep(1)
    try:

        while True:
            try:
                local = pyautogui.locateOnScreen(img3, confidence=0.4, region=(1768, 52, 113, 106))
                pyautogui.moveTo(local)
                print("imagem encontrada")
                break
            except pyautogui.ImageNotFoundException:
                time.sleep(1)
                buscarnpc()
                print(f"Imagem {img3} não encontrada. Tentando próxima...")
                continue  # Tenta a próxima imagem
        else:  # Executado se nenhuma imagem for encontrada
            print("Nenhuma imagem de NPC encontrada.")
            continue # Volta para o início do loop para tentar novamente

        break  # Sai do loop principal se alguma imagem for encontrada e clicada

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break