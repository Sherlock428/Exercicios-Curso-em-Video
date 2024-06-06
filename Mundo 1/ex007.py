"""Sistema de Cálcular a média de um Aluno"""
def mediaf():
    """Retorna o valor da média"""
    while True:
        try:
            print("=========Calculando Média==========")         
            nome = str(input("Digite o Nome do Aluno "))
            print(f"Seja, Bem Vindo ao Calculando Média,\n {nome:=^20}!")
            nota1 = float(input(f"Digite a Primeira Nota do Aluno {nome} "))
            nota2 = float(input(f"Digite a Segunda Nota do Aluno {nome} "))

            media = (nota1 + nota2) / 2

            print(f"A média do Aluno é {media:.2f}")

            if media > 5:
                print(f"Parabéns {nome}, Você está Aprovado!")
            else:
                print(f"Infelizmente {nome}, Você foi Reprovado!")
        except ValueError:
            print("ERROR: Digite um Valor Válido")
        except TypeError:
            print("ERROR")

        continuar = str(input("Deseja Continuar o App S/N "))

        if continuar.upper() != "S":
            break


mediaf()
