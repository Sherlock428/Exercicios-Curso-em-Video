"""Conversor de Reais em Dolares"""
def moeda():
    """Função responsável por retorna o valor reais digiitado"""
    while True:
        try:
            reais = float(input("Digite Quantos reais você tem na carteira "))

        except ValueError:
            print("ERROR, Digite um Valor Válido!")
        return reais


def conversor(seila):
    """Função responsável por converter reias em dolares, usando o valor retornado de moedas"""
    dolar = seila / 5.05

    return dolar

def design():
    """Função Responsável Pelo Design"""
    while True:
        print("==========Conversor de Reais em Dolar==========")
        name = input("Digite Seu Nome ")
        print(f"Seja {name} Bem-vindo ao App CDRED, Seu Parceiro de Financias")      
        fin = input("Deseja Consultar Quantos Dolares Você Pode Comprar? S/N ").upper

        if fin != "S":
            break

    return name





def main():
    """Função principal responsável por rodar todo o código"""
    while True:
        graf = design()
        real = moeda()
        dolar = conversor(real)
        print(f"Caro úsuario {graf}, Você Tem R$ {real} em sua Carteira Digital, Que É Cerca De US$ {dolar:.2f}")

        continuar = input(f"Deseja Continuar {graf} Na Operação S/N ").upper()
        if continuar != "S":
            break
        

main()
