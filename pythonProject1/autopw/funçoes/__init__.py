import subprocess
import os
import pyautogui
import time

def abrir_jogo(caminho_atalho):
  """
  Abre um jogo externo a partir de um arquivo de atalho (.lnk).

  Args:
    caminho_atalho: O caminho para o arquivo de atalho do jogo.
  """

  try:
    # Verifica se o arquivo de atalho existe
    if not os.path.exists(caminho_atalho):
      raise FileNotFoundError(f"Arquivo de atalho não encontrado: {caminho_atalho}")

    # Abre o jogo usando o subprocess
    subprocess.Popen([caminho_atalho])

  except FileNotFoundError as e:
    print(f"Erro: {e}")
  except Exception as e:
    print(f"Erro ao abrir o jogo: {e}")

def Tocartela():
  pyautogui.moveTo(x=957, y=542)
  pyautogui.click(button='right', clicks=1)
  pyautogui.press('b')

# def buscarpc():
#   Npc01()
#
# def Npc01(img):
#   x, y = pyautogui.locateCenterOnScreen(img, confidense= 0.8)
#   pyautogui.moveTo(x, y)
#   return x, y
#
#
# imagem = [r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\npc01,11.png']
# Npc01(imagem)
