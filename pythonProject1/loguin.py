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

while True:
    try:
        Tocartela()
        print("Encontrei até que fim")
        break
    except Exception as e:
        print("imagen nao encontrada")
    continue

#Procurar Pergaminho Teletransporte.
tempo_limite = 30
tempo_inicial = time.time()

imagem_encontrada = False

time.sleep(1)
while not imagem_encontrada and time.time() - tempo_inicial < tempo_limite:
    try:
        x, y = pyautogui.locateCenterOnScreen(r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\icon\pergaminhoTele.png', confidence=0.8)
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
imgTelealquimia = [r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\icon\Telealquimia.png']
time.sleep(1)
while True:
    try:
        clicar = localisarimg(imgTelealquimia,0.7 ,1235, 578, 94, 40)
        print("Encontrei até que fim")
        break
    except Exception as e:
        print("imagen nao encontrada")
    continue

# local = pyautogui.locateOnScreen(imgTelealquimia, confidence=0.3, region=(1235, 578, 94, 40))
time.sleep(1)
pyautogui.click(clicar,button='left', clicks=2)# ponto de tela vila da alquimia
time.sleep(2)

pyautogui.press('b')

time.sleep(1)

Direção = [r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Mapas\MapaP01\mapa1_cinza.png',
           r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Mapas\MapaP01\minimapa2_cinza.png',
           r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Mapas\MapaP01\minimapa3_cinza.png',
           r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Mapas\MapaP01\minimapa4_cinza.png',
           r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Mapas\MapaP01\minimapa5_cinza.png',
           r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Mapas\MapaP01\minimapa6_cinza.png']

while True:
    GirarTela()
    while True:
        try:
            localisarimg(Direção, 0.7,1720, 41, 172, 136)
            #localisarimg(Direção1, 0.7)
            print("Encontrei até que fim")
            break
        except Exception as e:
            print("imagen nao encontrada")
            GirarTela()
        continue
    break
time.sleep(1)
X, Y = 592, 506
while True:
    if X > 586 and Y <= 506:
        pyautogui.keyDown('w')
        X -= 1
        time.sleep(0.4)
    elif X == 586:
        pyautogui.keyUp('w')
        break

img = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Npcs\npc01,11.png'
img2 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\Frases\frasenpc01.png'

time.sleep(5)
local = NpcFrase1(img)
print(local)
pyautogui.click(local)
time.sleep(3)
cliclar = NpcFrase1(img2)
pyautogui.click(cliclar)
pyautogui.press('space', presses=2,interval=1)


print("Fim do script.")

