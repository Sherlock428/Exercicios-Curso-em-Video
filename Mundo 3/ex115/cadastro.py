import os
from cores import cores
from sistema_arq import criar_arquivo
from menu import design

arq = 'pessoas.txt'

def ler_txt(caminho_arq):
    try:
        with open(caminho_arq, "r", encoding="utf-8") as f:        
            return f.readlines()
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Erro ao ler aquivo: {e}")
        return []

def escrever_txt(caminho_arq, pessoa):
    try:
        with open(caminho_arq, "a", encoding="utf-8") as f:
            f.write(f"{pessoa['nome']}       \t{pessoa['idade']} Anos\n")
    except Exception:
        print("ERRO ao escrever arquivo")



def verificar_arquivo():
    diretorio = os.path.dirname(__file__)
    caminho_arq = os.path.join(diretorio, arq)
    return caminho_arq


def cadastrar_pessoas():
    
    if not verificar_arquivo():
        criar_arquivo(arq)

    while True:
        os.system('cls')
        print(f"""
{cores[2] + '-' * 30 + cores[4]}
{cores[1] + 'CADASTRAMENTO'.center(30) + cores[1]}
{cores[2] + '-' * 30 + cores[4]}
""")
        try: 
            pessoa = {'nome': input('Nome: ').capitalize(),
                    'idade': int(input("Idade: "))}
            
            print(f"{cores[1] + pessoa['nome']} Foi Adicionado com Sucesso" + cores[4])
            escrever_txt(verificar_arquivo(), pessoa)
            input(cores[3] + "[Enter] -> Retornar ao Menu " + cores[4])
            return
        except (ValueError, TypeError):
            print(cores[0] + "ERROR: Digite Apenas Valores Válidos" + cores[4])
            input(cores[3] + "[Enter] -> para tentar novamente: " + cores[4])
        

def ver_pessoas():
    os.system('cls')
    caminho_arq = verificar_arquivo()
    print(f"""
{cores[2] + '-' * 30 + cores[4]}
{cores[1] + 'PESSOAS CADASTRADAS'.center(30) + cores[4]}
{cores[2] + '-' * 30 + cores[4]} 
""")

    lista_txt = ler_txt(caminho_arq)
    if lista_txt:
        for pessoa in lista_txt:
            print(cores[5] + pessoa.strip() + cores[4])
    else:
        print(cores[3] + "Nenhuma pessoa cadastrada" + cores[4])
    
    input(cores[3] + "\n[Enter] -> Retornar ao Menu: " + cores[4])
def menu():
    while True:
        os.system('cls')
        print(design)
        try:
            opcao = int(input(cores[2] + "Selecione uma opção: " + cores[4]))

            if opcao == 1:
                ver_pessoas()
            elif opcao == 2:
                cadastrar_pessoas()
            elif opcao == 3:
                print(f"""
{cores[2] + '-' * 30 + cores[4]}
{cores[1] +  'OBRIGADO POR USAR O SISTEMA'.center(30) + cores[4]}
{cores[2] + '-' * 30 + cores[4]}  
""")
                break
            else:
                print(cores[0] + "ERROR: Digite um valor válido" + cores[4])
        except (ValueError, TypeError):
            print(cores[0] +"ERROR: Digite um valor válido" + cores[4])

menu()
# menu()