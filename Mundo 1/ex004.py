#Calculos 
def calculo():
    while True:
        try:
            num1 = int(input("Digite um número "))
            num2 = int(input("Digite um outro número "))

            soma = num1 + num2
            sub = num1 - num2
            mult = num1 * num2
            exp = num1 ** num2

    # if num2 == 0:
    #    div = "Não é possivel dividir por 0"
    # else:
            div = num1 / num2
            divint = num1 // num2
            divrest = num1 % num2

            print(
            f"Resultado nas seguintes operações são: \n Soma {soma:.2f} \n Subtração  {sub:.2f} \n Multiplicação {mult:.2f} \n Divisão {div}\n Divisão Valor Quoeficiente {divint} \n Divisão Valor Do Resto {divrest} \n Valor Da Potenciação {exp}\n Equação {num1 + num2 * 20 **4 / 2}")

        except ValueError:
            print("ERROR: Digite um número válido")
        except ZeroDivisionError:
            print("ERROR: Não pode dividir por 0")

        resposta = input("Deseja Reiniciar os Cálculos: S/N ")
        if resposta.upper() != "S":
            break


calculo()
