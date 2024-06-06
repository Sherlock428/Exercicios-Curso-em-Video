def notas():
    try:
        nota1 = float(input("Digite A Primeira Nota do Aluno: "))
        nota2 = float(input("Digite A Segunda Nota do Aluno: "))

        return nota1, nota2
    except ValueError:
        print("ERROR: Digite um Número Válido")


def mediaf(nota1, nota2):
    media = (nota1 + nota2) / 2

    
    if media == 10:
        print(f"PARABÉNS, Você Atingiu a Média Máxima\nSua Média {media} ")
    elif media >= 6 < 9:
        print(f"Parabéns, Você foi Aprovado!\nSua nota é {media}")
    else:
        print(f"Você foi Reprovado\nSua Média {media}")


def main():
    while True:
        n1, n2 = notas()
        mediaf(n1, n2)

        cont = input("Deseja Continuar Executando o Programa? (S/N) ").upper()

        if cont != "S":
            break


main()
