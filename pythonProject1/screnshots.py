import pyautogui
import time
import cv2

from autopw.funçoes import ConverterGray

pyautogui.PAUSE = 2.5
time.sleep(5)

#img = pyautogui.screenshot('autopw/imagenss/minimapa3.png', region=(1720, 41, 172, 136))
# img = pyautogui.screenshot('autopw/imagenss/iconecorreio.png', region=(1873, 31, 26, 25))
img1 = r'C:\Users\Jhowzera\PycharmProjects\CursoemVideo\Projetoauto\pythonProject1\autopw\imagenss\minimapa2.png'

ConverterGray(img1)
# img_cinza = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
# abrir a imagem

# imagem = cv2.imread(img1)
# #
# # Conveter para tons de Cinza
# img_convertida = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# #
# # Guarda a imagem
# img_saida = img1.replace(".png", "_cinza.png")
# cv2.imwrite(img_saida, img_convertida)

