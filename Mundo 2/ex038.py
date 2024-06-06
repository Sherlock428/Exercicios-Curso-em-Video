def numeros():
    try:

        num1 = int(input("Digite um Número "))
        num2 = int(input("Digite Outro Número "))
        return num1, num2
    except ValueError:
        print("ERROR: Digite um valor válido")

def comparacao(num1, num2):
    if num1 > num2:
        print(f"{num1} é maior que {num2}")
    elif num2 > num1:
        print(f"{num2} é maior que {num1}")
    else:
        print("Os números são iguais")

def design():
    print("""
================================
    Comparando Números
================================
    """)

def main():
    while True:
        design()
        n1, n2 = numeros()
        comparacao(n1, n2)

        cont = input("Deseja Continuar Usando o App (S/N) ").upper()

        if cont != "S":
            break