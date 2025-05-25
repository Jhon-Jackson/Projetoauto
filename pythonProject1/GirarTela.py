import subprocess
import os
import pyautogui
import time
import cv2
from autopw.funçoes import *

time.sleep(3)

img3 = [
    r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa.png']

time.sleep(2)
while True:
    time.sleep(1)
    try:
        for img in img3:
            try:
                local = pyautogui.locateOnScreen(img, confidence=0.5, region=(1720, 41, 172, 136))
                # pyautogui.moveTo(local)
                pyautogui.click(1833, 78, button='left', clicks=1)
                print("imagem encontrada")
                break
            except pyautogui.ImageNotFoundException:
                time.sleep(1)
                buscarnpc()
                print(f"Imagem {img} não encontrada. Tentando próxima...")
                continue  # Tenta a próxima imagem
        else:  # Executado se nenhuma imagem for encontrada
            print("Nenhuma imagem de NPC encontrada.")
            continue # Volta para o início do loop para tentar novamente

        break  # Sai do loop principal se alguma imagem for encontrada e clicada

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break