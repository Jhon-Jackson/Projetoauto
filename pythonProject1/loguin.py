import pyautogui
import time
import subprocess
import os
from autopw.funçoes import *


# pegar posiçoes do mouse e da tela
# print(pyautogui.position())
# print(pyautogui.size())
pyautogui.PAUSE = 1.5
time.sleep(5)
# Fazer loguin
caminho_atalho = r"C:\Users\Jhowzera\Desktop\AREA DE TRABALHO\PW FALCAO\pwlogin.bat"
abrir_jogo(caminho_atalho) #função

time.sleep(40)
# esperar logar e  abrir bag
Tocartela()
# pyautogui.moveTo(x=957, y=542)
# pyautogui.click(button= 'right', clicks=1)
# pyautogui.press('b')

#Procurar Pergaminho Teletransporte.
tempo_limite = 30
tempo_inicial = time.time()

imagem_encontrada = False

time.sleep(1)
while not imagem_encontrada and time.time() - tempo_inicial < tempo_limite:
    try:
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\pergaminhoTele.png', confidence=0.8)
        pyautogui.moveTo(x, y)
        print("Imagem encontrada e clicada!")
        imagem_encontrada = True
    except pyautogui.ImageNotFoundException:
        time.sleep(1)
        print('Imagem não encontrada. Tentando novamente...')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break

if not imagem_encontrada:
    print(f"Tempo limite de {tempo_limite} segundos excedido. Imagem não encontrada.")

# Telar para quedanunca
pyautogui.click(x, y, button='right', clicks=1)
pyautogui.click(x=705, y=495)# posição quedanunca
#pyautogui.moveTo(x=1271, y=594)
time.sleep(1)
imgTelealquimia = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Telealquimia.png'
time.sleep(1)
clicar = localisarimg(imgTelealquimia,1235, 578, 94, 40)
# local = pyautogui.locateOnScreen(imgTelealquimia, confidence=0.3, region=(1235, 578, 94, 40))
time.sleep(1)
pyautogui.click(clicar,button='left', clicks=2)# ponto de tela vila da alquimia
time.sleep(2)

pyautogui.press('b')

time.sleep(2)

clickpertonpc()

time.sleep(2)

acharnpc()

img = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\npc01,11.png'
img2 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\frasenpc01.png'

time.sleep(5)
local = NpcFrase1(img)
print(local)
pyautogui.click(local)
time.sleep(3)
cliclar = NpcFrase1(img2)
pyautogui.click(cliclar)
pyautogui.press('space', presses=2,interval=1)


print("Fim do script.")

