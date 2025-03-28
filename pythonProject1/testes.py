import subprocess
import os


caminho_atalho = r"C:\Users\Jhowzera\Desktop\AREA DE TRABALHO\PW FALCAO\pwlogin.bat"

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

# Exemplo de uso
caminho_atalho = r"C:\Users\Jhowzera\Desktop\AREA DE TRABALHO\PW FALCAO\pwlogin.bat" # Substitua pelo caminho real do seu atalho
abrir_jogo(caminho_atalho)