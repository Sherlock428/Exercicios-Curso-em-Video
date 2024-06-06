def ano():
    try:
        ano_nascimento = int(input("Qual seu ano de nascimento: "))
        ano_atual = int(input("Digite o ano Atual: "))
        return ano_nascimento, ano_atual
    except ValueError:
        print("ERROR: Digite um Número Válido")


def conversor(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento

    if ano_atual < ano_nascimento:
        print("Você ainda não Nasceu Viajante do Tempo")

    elif idade >= 18:
        diferença = idade - 18
        print(f"Você tem {idade}, pode se alistar!\n")
        if diferença > 0:
            print(f"Você já poderia ter se alistado a {diferença} anos\n")

    else:
        diferenca = 18 - idade
        print(
            f"Você ainda não pode se alistar\n" f"Falta {diferenca} para se alistar\n"
        )


def main():
    while True:
        an, at = ano()
        conversor(an, at)

        cont = input("Deseja Continuar executando o Programa (S/N) ").upper()

        if cont != "S":
            break


main()
