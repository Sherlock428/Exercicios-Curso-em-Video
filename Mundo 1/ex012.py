"""Calculador de Desconto"""
def valor():
    """Função responsável por executar os valores digitados"""
    while True:
        try:
            price = float(input("Digite O Preço do Produto! "))
            tax = int(input("Digite a Porcentagem do Desconto! "))
        except ValueError:
            print("ERROR: Digite um número válido!")

        return price, tax


def desconto(preco, taxa):
    """Função que é responsável por retornar o desconto"""
    prc, tx = preco, taxa
    desc = prc * (tx / 100)
    desc1 = prc - desc

    return desc, desc1


def entrada():
    """Função responsável pela entrada de informações complementares"""
    print("==================Seja Bem-Vindo Ao PDV====================")
    nomep = input(
        "Digite o Nome do Produto, que Queira Consultar o Valor do Desconto! ")

    print(f"O Produto Escolhido:\n {nomep:=^40}")

    return nomep


def main():
    """Função Principal responsável por rodar todo o código"""
    while True:
        produto = entrada()
        preco, taxa = valor()
        desc, desc1 = desconto(preco, taxa)
        print(
            f"O Valor do {produto}\n R${preco:.2f} reais\n Com Desconto {taxa}%\n Valor Final R${desc1:.2f} Reais\n Valor Descontado de {desc:.2f}")

        continuar = input("\nDeseja Continuar Usando o PDV? S/N ").upper()
        if continuar != "S":
            break


main()


# Melhorar esse código mais tarde
# Código versão simples

#produtov = int(input("Digite o preço do Produto"))
#taxa = int(input("Digite o valor do desconto"))
#desc = produtov * (taxa / 100)
#desc1 = produtov - desc
#print(f"O produto de valor R$ {produtov:.2f} reais, com desconto {taxa}, valor final de R$ {desc1:.2f} reais, tendo valor de {desc:.2f} Descontado")
