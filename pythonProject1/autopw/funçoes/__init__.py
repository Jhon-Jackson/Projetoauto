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
  img1 = [r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\icon\iconecorreio_cinza.png']
  while True:
    try:
      localisarimg(img1,0.5, 1873, 31, 26, 25)
      pyautogui.press('b')
      break
    except:
      continue


def GirarTela():
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
      GirarTela()
    except Exception as e:
      print(f"Ocorreu um erro: {e}")
      break

  return x, y


def localisarimg(n,con=0.7,px=0,py=0,rw=1903,rh=1054):
  img3 = n
  while True:
    time.sleep(1)
    try:
      for img in img3:
        try:
          local = pyautogui.locateOnScreen(img, confidence=con, region=(px, py, rw, rh))
          pyautogui.moveTo(local)
          print("imagem encontrada")
        except pyautogui.ImageNotFoundException:

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

def Andar(a, b, c , d):
    IX,IY = a, b
    FX, FY = c, d

    while True:
        if IX > FX and FY <= IY:
            pyautogui.keyDown('w')
            IX -= 1
            time.sleep(0.4)
        elif IX and IY <= FX and FY:
            pyautogui.keyUp('w')
            break