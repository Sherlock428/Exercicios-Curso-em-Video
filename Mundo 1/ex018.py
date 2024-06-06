"""App Que Mostra Os Valores do Seno, Coseno e Tangente"""
import math

def valor():
    while True:
        try:
            grau = int(input("Digite o Grau: "))
        except ValueError:
            print("ERROR: Digite um Valor Válido")
        return grau
    
def radiando(gr):
    rad = gr * math.pi / 180
    sen, cos, tan = math.sin(rad), math.cos(rad), math.tan(rad)

    return rad, sen, cos, tan

def entrada():
    print("==========Bem-Vindo Ao MVSCT==========")
    name = input("Digite Seu Nome Para Continuar: ")

    return name

def principal():
    while True:
        nome = entrada()
        gr = valor()
        rad, sen, cos, tan = radiando(gr)

        print(f"{nome:=^20}\nValor do Radiando {rad:.2f}:\n"
              f"O Seno: {sen:.2f}\n"
              f"Coseno: {cos:.2f}\n"
              f"Tangente: {tan:.2f}\n"
              )
        cont = input("Deseja Continuar A Execução do APP S/N ").upper()

        if cont != "S":
            break

principal()
    #Melhorado Aprender mais sobre os assunstos 