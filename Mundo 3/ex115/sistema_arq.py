import os

def arquivo_existe(nome):
    try:
        diretorio = os.path.dirname(__file__)
        caminho_arq = os.path.join(diretorio, nome)
        abrir = open(caminho_arq, "rt")
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome):
    try:
        diretorio = os.path.dirname(__file__)
        caminho_arq = os.path.join(diretorio, nome)

        a = open(caminho_arq, "wt+")
        a.close()
    except:
        print("ERROR: Ao criar arquivo")
    else: 
        print("Arquivo Criado")