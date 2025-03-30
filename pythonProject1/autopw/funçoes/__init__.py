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

def buscarnpc():
    try:
      while True:
        # Girar a tela (movimentação relativa do mouse)
        pyautogui.vscroll(10)
        pyautogui.mouseDown(button='right', x=1268, y=418)
        pyautogui.dragRel(-368, 0, button='right')  # Arrastar 368 pixels para a esquerda
        pyautogui.mouseUp(button='right')
        break
    except KeyboardInterrupt:
      print('\n')


def NpcFrase1(img):
  tempo_limite = 30
  tempo_inicial = time.time()
  imagem_encontrada = False
  time.sleep(1)
  while not imagem_encontrada and time.time() - tempo_inicial < tempo_limite:
    try:
      x, y = pyautogui.locateCenterOnScreen(img, confidence=0.8)
      pyautogui.moveTo(x, y)
      print("Imagem encontrada e clicada!")
      imagem_encontrada = True
    except pyautogui.ImageNotFoundException:
      time.sleep(1)
      print('Imagem não encontrada. Tentando novamente...')
      buscarnpc()
    except Exception as e:
      print(f"Ocorreu um erro: {e}")
      break

  return x, y

