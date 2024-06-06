"""Tabuada"""
def valor_digi():
    """Função Responsável por armazenar os valores digitados"""
    while True:
        try:
            number = int(input("Digite o número "))

        except ValueError:
            print("ERROR: Digite um número válido ")
        return number


def tabuada(number):
    """Função Responsável pela Tabuada"""
    for multi in range(0, 11):
     resultado = number * multi
     print(f"{number} x {multi} = {resultado}") 
    return resultado, multi
   


def main():
    """Função Respónsável por rodar o código"""
    while True:
        print("===========Tabuada===========")
        n = valor_digi()
        tabuada(n)
        
        continuar = input("Deseja continuar com operação S/N ").upper()
        if continuar != "S":
            break
        


main()
