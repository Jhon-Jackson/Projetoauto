import subprocess
import os
import pyautogui
import time


pyautogui.PAUSE = 1.5
time.sleep(5)

while True:
  try:
    # Girar a tela (movimentação relativa do mouse)
    pyautogui.mouseDown(button='right', x=1268, y=418)
    pyautogui.dragRel(-368, 0, button='right')  # Arrastar 368 pixels para a esquerda
    pyautogui.mouseUp(button='right')
    time.sleep(5)
  except:
    break
  #   buscarpc()
  #   npc = Npc01()
  #   while True:
  #     try:
  #       pyautogui.click(npc)
  #       print("Imagem encontrada e clicada!")
  #       break
  #     except pyautogui.ImageNotFoundException:
  #       print("Imagem  não encontrada. Tentando próxima...")
  #     continue  # Tenta a próxima imagem
  #   else: # Executado se nenhuma imagem for encontrada
  #     print("Nenhuma imagem de NPC encontrada.")
  #     continue  # Volta para o início do loop para tentar novamente
  # except Exception as e:
  #   print(f"Ocorreu um erro: {e}")
  #   break
