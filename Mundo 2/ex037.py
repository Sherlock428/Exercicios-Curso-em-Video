def valor():
    try:
        num = int(input("Digite um Número: "))

        print("""
        Para qual desses gostaria de converter o número escolhido?

        [1] Binario
        [2] Octal
        [3] Hexdecimal
        """)

        escolha = int(input("Digite Aqui: "))
    except ValueError:
        print("ERROR: Escolha um Valor Válido")
        
    return num, escolha

def conversor(num, escolha):
    if escolha == 1:
        binario = bin(num)
        print(binario)
        return binario
    elif escolha == 2:
        octal = oct(num)
        print(octal)
        return octal
    elif escolha == 3:
        hexadecimal = hex(num)
        print(hexadecimal)
        return hexadecimal
    
def design():
    print("""
=====================================
Conversor Binário, Octal, Hexadecimal
=====================================
    """)

def main():
    while True:
        design()
        n, e = valor()
        c = conversor(n, e)

        cont = input("Deseja Continuar executando o Programa (S/N) ").upper()

        if cont != "S":
            break

main()