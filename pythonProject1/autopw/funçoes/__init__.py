import subprocess
import os
import pyautogui
import time
import cv2


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
  img1 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\iconecorreio_cinza.png'
  while True:
    try:
      localisarimg(img1, 1877, 36, 24, 15)
      pyautogui.press('b')
      break
    except:
      continue

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
    r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\npc01,11.png',
    r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\npc1.2.png']

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

def localisarimg(n,px=0,py=0,rw=0,rh=0):
  time.sleep(3)
  img3 = [n]
  time.sleep(2)
  while True:
    time.sleep(1)
    try:
      for img in img3:
        try:
          local = pyautogui.locateOnScreen(img, confidence=0.5, region=(px, py, rw, rh))
          pyautogui.moveTo(local)
          print("imagem encontrada")
          break
        except pyautogui.ImageNotFoundException:
          time.sleep(1)
          print(f"Imagem {img} não encontrada. Tentando próxima...")
          continue  # Tenta a próxima imagem
      else:  # Executado se nenhuma imagem for encontrada
        print("Nenhuma imagem encontrada.")
        continue  # Volta para o início do loop para tentar novamente

      break  # Sai do loop principal se alguma imagem for encontrada e clicada

    except Exception as e:
      print(f"Ocorreu um erro: {e}")
      break
    return local

def ConverterGray (img):
  imagem = cv2.imread(img)
  #
  # Conveter para tons de Cinza
  img_convertida = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
  # Guarda a imagem
  img_saida = img.replace(".png", "_cinza.png")
  cv2.imwrite(img_saida, img_convertida)
  return img_saida

