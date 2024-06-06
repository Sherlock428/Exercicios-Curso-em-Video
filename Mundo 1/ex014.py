"""Analise de preço de Aluguel de Carros"""
def inputs():
    """Função que armazena os inputs e retorna os valores dela"""

    while True:
        try:
            carro = float(input("Quanto Custa O Carro Por Dia ? "))
            ckm = float(input("Quanto É Cobrado por Km ? "))
            dias = int(input("Digite Quantos Dias Será Usado: "))
            km = int(input("Digite Quantos Quilômetros Foram Rodados: "))

        except ValueError:
            print("Digite um Número Válido")

        return carro, ckm, km, dias

def calc(c, ck, km, di):
    """Função que realiza os cálculos"""
    res = c * di  + (km * ck)

    return res

def design():
    """Função de Entrada"""
    print("==========Bem-Vindo Ao Sistema CARALUG==========")
    name = input("Digite Seu Nome: ")
    print(f"Olá\n{name:=^20}\n Iniciando o APP  ")
    return name
def main():
    """Função Principal que Roda todo o código"""
    while True:
        entrada = design()
        car, ckm, km, day = inputs()
        r = calc(car, ckm, km, day)

        print(f"\nCaro, {entrada}O Carro que Será Alugado Custa:\nR$ {car:.2f} reais Por Dia\nSendo Cobrado uma Taxa de {ckm}\nDurante {day} Dias\nUsando Cerca de {km} Rodados\nFicará Por R$ {r:.2f} reais ")

        cont = input("\nDeseja Continuar com Execução do APP S/N ").upper()

        if cont != "S":
            break

main()
#Código simples
# carro = float(input("Quanto custa o preço do Carro por dia ?"))
# kmc = float(input("Quanto é cobrado por km"))

# km = int(input("Digite Quantos km foram rodados: "))
# dias = int(input("Quantos dias usando o carro: "))

# res = carro * dias + (kmc * km)

# print(res)
