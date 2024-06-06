"""Programa que mostra o Sucessor e Antecessor de um número"""

def suceand_ante():
    """A Função retorna o Sucessor e Antecessor"""
    while True:
        try:
            print("============Sucessor, Antecessor e Raiz===========")
            numero = int(input("Digite um número "))

            sucessor = numero + 1
            antecessor = numero - 1

            print(f"O Número escolhido {numero}\nSeu Sucessor é {sucessor} \nE o Seu Antecessor {antecessor}")

        except ValueError:
            print("ERROR: Digite um Número Inteiro Válido")

        continuar = input("Deseja Continuar no App? S/N ")
        if continuar.upper() != "S":
            break


suceand_ante()
