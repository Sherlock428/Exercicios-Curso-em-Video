import math

def numero():
    while True:
        try:
            number1 = float(input("Digite um Número: "))
        except ValueError:
            print("ERROR: Digite um Número Válido")
        return number1
    
def quebrando(n1):
    raiz = math.sqrt(n1)
    up = math.ceil(raiz)
    floor = math.floor(raiz)
    truck = math.trunc(raiz)
    potencia = math.pow(n1, 2)
    #fatorial = math.factorial(n1)

    return raiz, up, floor, truck, potencia, #fatorial 

def entrada():
    print("==========Bem-Vindo Ao Sistema QBNUMBER==========")
    name = input("Digite Seu Nome Para Continuar o Teste: ").capitalize()

    return name

def principal():
    while True:
        nome = entrada()
        n1 = numero()
        ra, up, fl, tr, po = quebrando(n1)

        print(f"\n{nome:=^20}\nQuebrando o Número {n1} São:\n"
            f"A raiz: {ra:.2f}\n"
            f"O número Arredondado Para Valor maior: {up}\n"
            f"O número Arrendondado Para O Valor Menor: {fl}\n"
            f"O Número Sem Vírgula: {tr}\n"
            f"Elevado Ao Quadrado: {po:.2f}\n")
            #f"Fatorial: {fa}") 

        cont = input("Deseja Continuar O QBNUMBER S/N: ").upper()
        if cont != "S":
            break

principal()