def equacao():
    while True:  # Executa um loop caso a opção digitada seja verdadeira
        try:
            print("==========Equação==========")
            print("var1 + var2 * var3 / var4")

            num1 = int(input("Digite o Primeiro valor da Equação "))
            num2 = int(input("Digite o Segundo valor da Equação "))
            num3 = int(input("Digite o Terceiro valor da Equação "))
            num4 = int(input("Digite o Quarto valor da Equação "))

            resul = num1 + num2 * num3 / num4
            print(f"O resultado dessa equação é: {resul:.1f}.")
            name = input("Digite seu nome! ")
            print(f"Parabéns pelo resultado {name:=^20}")

        except ZeroDivisionError:
            print("ERROR: Divisão pode ser realizada por 0")

        except ValueError:
            print("ERROR: Valor inválido")

        resposta = input("Deseja realizar outra Equação ? S/N ")
        if resposta.upper() != "S":  # Faz uma condição que caso a resposta seja diferente de "S" o loop é parado
            break  # Para o loop caso opção digitada "N"


equacao()
