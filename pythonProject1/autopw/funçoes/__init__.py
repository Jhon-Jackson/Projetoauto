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


def NpcFrase1(img,w=0,h=0):
  tempo_limite = 30
  tempo_inicial = time.time()
  imagem_encontrada = False
  time.sleep(1)
  while not imagem_encontrada and time.time() - tempo_inicial < tempo_limite:
    try:
      x, y = pyautogui.locateCenterOnScreen(img, confidence=0.8) #region=(0,0, w, h))
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


def clickpertonpc():
  time.sleep(3)

  img3 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\clickpertonpc1.png'
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
        continue  # Volta para o início do loop para tentar novamente

      break  # Sai do loop principal se alguma imagem for encontrada e clicada

    except Exception as e:
      print(f"Ocorreu um erro: {e}")
      break

def acharnpc():
  tempo_limite = 30  # Tempo limite para a busca de imagem (segundos)

  # Lista de imagens a serem procuradas
  imagens_npc = [
    r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Npc01.1.png',
    r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Npc01.png',
    r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\npc01,11.png']

  # Loop principal
  while True:
    try:
      time.sleep(3)  # Espera antes de girar a tela

      # Girar a tela (movimentação relativa do mouse)
      pyautogui.mouseDown(button='right', x=1268, y=418)
      pyautogui.dragRel(-368, 0, button='right')  # Arrastar 368 pixels para a esquerda
      pyautogui.mouseUp(button='right')

      # Buscar pelas imagens
      for imagem in imagens_npc:
        try:
          x, y = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
          pyautogui.click(x, y)
          print(f"Imagem {imagem} encontrada e clicada!")
          break  # Sai do loop após encontrar a imagem
        except pyautogui.ImageNotFoundException:
          print(f"Imagem {imagem} não encontrada. Tentando próxima...")
          continue  # Tenta a próxima imagem
      else:  # Executado se nenhuma imagem for encontrada
        print("Nenhuma imagem de NPC encontrada.")
        continue  # Volta para o início do loop para tentar novamente

      break  # Sai do loop principal se alguma imagem for encontrada e clicada

    except Exception as e:
      print(f"Ocorreu um erro: {e}")
      break