def comprimentos():
    try:
        com1 = float(input("Digite o Comprimento a: "))
        com2 = float(input("Digite o Comprimento b: "))
        com3 = float(input("Digite o Comprimento c: "))

        return com1, com2, com3
    
    except ValueError:
        print("ERROR, Digite Apenas Valores Válidos")

def triangulos(a, b, c):

    if a != b != c:
        print("Formou-se um Triangulo Escaleno")
        
    
    elif (a == b == c) or (b == c == a) or (a == c == b):
        print("Você formou um Triângulo Equilátero")
        
    else:
        print("Você formou um Triângulo Isosceles")    
        
def design():
    print(""" 
=================================
      Equilátero, Escaleno
            Isosceles
=================================
    
    """)
def main():
    while True:
        design()
        a, b, c = comprimentos()
        triangulos(a, b, c)

        cont = input("Deseja Continuar executando o APP (S/N) ").upper()

        if cont != "S":
            break


main()
