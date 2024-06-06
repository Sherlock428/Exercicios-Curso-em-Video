def dados():
    try:
        peso = float(input("Digite Seu Peso (kg): "))
        altura = float(input("Digite Sua Altura (m): "))

        return peso, altura
    except ValueError:
        print("ERROR: Digite um Valor Válido")

def resultado(peso, altura):

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print(f"Seu {imc:.2f}, Você está Apresentando um Peso Abaixo do Esperado")
    elif imc < 26:
        print(f"Seu {imc:.2f}, Você está Em seu Peso Ideal")
    elif imc  < 30:
        print(f"Seu {imc:.2f}, Você está Com Sobrepeso")
    elif imc  < 40:
        print(f"Seu {imc:.2f}, Você está Com Obesidade Precisa se Cuidar Melhor")
    else:
        print(f"Seu {imc:.2f}, Você está com Obesidade Mórbida")

def design():
    print("""
================================
    índice de Massa Corporal 
================================
    """)

def main():
    while True:
        design()
        p, a = dados()
        resultado(p, a)

        cont = input("Deseja Continuar a Executando o Programa (S/N) ").upper()

        if cont != "S":
            break
    
main()