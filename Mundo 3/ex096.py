#Calculando a área

def dados():
    largura = float(input("Digite a Largura(m): "))
    comprimento = float(input("Digite o comprimento(m): "))

    return largura, comprimento

def resultado(l, c):

    area = l * c

    return area

def main():
    l, c = dados()
    res = resultado(l, c)

    print(f"A Área de um terreno {l}x{c} é de {res}")


main()