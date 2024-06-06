"""App que verifica se seu nome tem Silva"""
def names():
    """Função que Retorna o nome completo digitado"""
    name = input("Digite Seu Nome Completo: ")

    return name

def check(name):
    """Função que faz o check verificando se à Silva no Nome, retornando um resposta caso sim ou caso não"""
    n = name

    if n.find("Silva") != -1:
        print(f"O Nome {n} possui 'Silva' ")
    else:
        print(f"O Nome {n}, Não Possui 'Silva'")

def design():
    """Função que faz um Design Simples"""
    print("==========Bem-Vindo Ao Você é o Silva?==========")

def main():
    """Função Principal Responsável por rodar todo o código"""
    design()
    name = names()
    check(name)




#Código Versão mais simples
#name = input("Digite Seu Nome Completo ").title()

#if name.find("Silva") != -1:
#    print(f"Seu nome {name} tem 'Silva' ")

#else: 
#   print(f"Seu nome {name} Não Tem 'Silva' ")
