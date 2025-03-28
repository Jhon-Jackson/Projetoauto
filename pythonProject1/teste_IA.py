import pyautogui
import time

pyautogui.PAUSE = 2.5
time.sleep(5)

tempo_limite = 30
tempo_inicial = time.time()



imagem_encontrada = False
pyautogui.press('b')
time.sleep(1)
while not imagem_encontrada and time.time() - tempo_inicial < tempo_limite:
    try:
        x, y = pyautogui.locateCenterOnScreen('pergaminhoTele.png', confidence=0.8)
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

pyautogui.click(x, y, button='right', clicks=1)
pyautogui.click(x=705, y=495)# posição quedanunca
pyautogui.moveTo(x=1270, y=594)
time.sleep(1)
pyautogui.click(x=1270, y=594,button='left', clicks=2)# ponto de tela vila da alquimia
time.sleep(2)
pyautogui.press('b')
time.sleep(1)

pyautogui.click(x=1789, y=112)#anda para perto do npc.
time.sleep(2)
tempo_limite = 30  # Tempo limite para a busca de imagem (segundos)

# Lista de imagens a serem procuradas
imagens_npc = ['Npc01.1.png', 'Npc01.png', 'npc01,11.png']

# Loop principal
while True:
    try:
        time.sleep(5)  # Espera antes de girar a tela

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
            continue # Volta para o início do loop para tentar novamente

        break  # Sai do loop principal se alguma imagem for encontrada e clicada

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        break

print("Fim do script.")


