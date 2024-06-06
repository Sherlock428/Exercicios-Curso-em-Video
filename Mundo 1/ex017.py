#Teorema de Pitagoras, valor da hipotenusa
import math

def inputs():
    while True:
        try:
            sen = float(input("Digite Seno em Ângulo em Radianos: "))
            cos = float(input("Digite Conseno em Ângulo em Radianos: "))
        except ValueError:
            print("ERROR: Digite um Valor Válido")
        return sen, cos
    
def hipotenusa(seno, coseno):
    sen, cos = seno, coseno
    hipo = math.sqrt(math.sin(sen) ** 2 + math.cos(cos) ** 2)

    return hipo

def entrada():
    print("==========Bem-Vindo ao Hipoteca==========")
    name = input("\nDigite Seu Nome Para Começamos Os Testes: ").capitalize()

    return name
def main():
    while True:
        nome = entrada()
        s, c = inputs()
        hipo = hipotenusa(s, c)
        print(f"\n{nome} O Hipotenusa desse número é: {hipo:.2f}")
        continuar = input("Deseja Continuar a Utilizar o APP S/N ")

        if continuar != "S":
            break
 

main()
 #melhorar esse código mais tarde