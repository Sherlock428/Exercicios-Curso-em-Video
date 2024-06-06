"""Mostrar Dobro, Triplo e Raiz Quadrada de um número"""
def dtr():
    """Retorna os valores"""
    while True:
        try: 
            num = int(input("Digite um Número Inteiro "))

            dobro = num * 2
            triplo = num * 3
            raiz = num **(1/2)

            print(f"O Dobro do é {dobro}, o Triplo {triplo} e a Raíz {raiz:.0f}")

        except ValueError:
            print("ERROR, Digite um número inteiro!")
        continuar = str(input("Deseja Continuar a Execução do Programa S/N "))
        
        if continuar.upper() != "S":
            break


dtr()
