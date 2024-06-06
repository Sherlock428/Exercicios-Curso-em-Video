def comprimentos():
    while True:
        try:
            com1 = float(input("Digite O Primeiro Comprimento: "))
            com2 = float(input("Digite O Segundo Comprimento: "))
            com3 = float(input("Digite O Terceiro Comprimento: "))

            return com1, com2, com3
        except ValueError:
            print("ERROR: Digite Apenas Valores Válidos")

def triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: 
        return False
    
    if (a + b > c) or (b + c > a) or (c + a > b):
        return True

def main():
    while True: 
        com1, com2, com3 = comprimentos()
        if triangulo(com1, com2, com3):
            print("É possível formar um Triangulo")
        else:
            print("Não é possível formar um Triangulo")

main()